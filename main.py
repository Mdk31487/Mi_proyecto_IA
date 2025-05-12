from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from jose import jwt
from datetime import datetime, timedelta

# Inicializaci  n de la aplicaci  n
app = FastAPI()

# Clave secreta para la generaci  n de tokens
SECRET_KEY = "mi_secreto_super_seguro"
ALGORITHM = "HS256"
TOKEN_EXPIRATION_HOURS = 1

# Modelos para validar las entradas
class ModelUploadRequest(BaseModel):
    name: str

class TokenRequest(BaseModel):
    username: str

# Rutas

@app.get("/")
def read_root():
    return {"message": "Bienvenido a tu plataforma de IA"}

@app.post("/upload_model/")
def upload_model(request: ModelUploadRequest):
    # Aqu   ir  a la l  gica para subir y guardar modelos
    # Puedes conectar esta parte con una base de datos o almacenamiento en la nube
    return {"status": "Modelo subido correctamente", "model_name": request.name}

@app.post("/generate_token/")
def generate_token(request: TokenRequest):
    if not request.username:
        raise HTTPException(status_code=400, detail="El nombre de usuario es obligatorio.")

    expiration = datetime.utcnow() + timedelta(hours=TOKEN_EXPIRATION_HOURS)
    token_data = {"sub": request.username, "exp": expiration}
    token = jwt.encode(token_data, SECRET_KEY, algorithm=ALGORITHM)

    return {"access_token": token, "token_type": "bearer", "expires_in": TOKEN_EXPIRATION_HOURS * 3600}
