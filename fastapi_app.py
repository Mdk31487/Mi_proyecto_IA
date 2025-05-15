from fastapi import FastAPI, HTTPException, Depends, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from jose import jwt, JWTError
from datetime import datetime, timedelta

app = FastAPI(root_path="/fastapi")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Montar carpeta de archivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")

# Configurar carpeta de plantillas
templates = Jinja2Templates(directory="templates")

# Configuración JWT
SECRET_KEY = "mi_secreto_super_seguro"
ALGORITHM = "HS256"
TOKEN_EXPIRATION_HOURS = 1
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Modelos
class ModelUploadRequest(BaseModel):
    name: str

class TokenRequest(BaseModel):
    username: str

class PredictRequest(BaseModel):
    features: list[float]

# Función para validar el token
def validar_token(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Token inválido")
        return username
    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido")

# Endpoint raíz para mostrar index.html
@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# dashboar
@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request, username: str = Depends(validar_token)):
    return templates.TemplateResponse("dashboard.html", {"request": request, "username": username})

# Endpoints API
@app.post("/upload_model/")
def upload_model(request: ModelUploadRequest):
    return {"status": "Modelo subido correctamente", "model_name": request.name}

@app.post("/generate_token/")
def generate_token(request: TokenRequest):
    if not request.username:
        raise HTTPException(status_code=400, detail="El nombre de usuario es obligatorio.")

    expiration = datetime.utcnow() + timedelta(hours=TOKEN_EXPIRATION_HOURS)
    token_data = {"sub": request.username, "exp": expiration}
    token = jwt.encode(token_data, SECRET_KEY, algorithm=ALGORITHM)

    return {
        "access_token": token,
        "token_type": "bearer",
        "expires_in": TOKEN_EXPIRATION_HOURS * 3600
    }

@app.post("/predict/")
def predict(request: PredictRequest, username: str = Depends(validar_token)):
    if len(request.features) < 2:
        raise HTTPException(status_code=400, detail="Debes enviar al menos 2 características")

    result = sum(request.features)
    return {
        "usuario": username,
        "prediction": result
   }
