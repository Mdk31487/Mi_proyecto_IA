from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from jose import jwt
from datetime import datetime, timedelta
from sqlmodel import Session, select
from database import engine, create_db_and_tables
from models import Prediction
from typing import List

# Inicialización de la aplicación
app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

# Clave secreta para la generación de tokens
SECRET_KEY = "mi_secreto_super_seguro"
ALGORITHM = "HS256"
TOKEN_EXPIRATION_HOURS = 1

# Modelos para validar las entradas
class ModelUploadRequest(BaseModel):
    name: str

class TokenRequest(BaseModel):
    username: str

class PredictionRequest(BaseModel):
    features: list[float]

# Rutas

@app.get("/")
def read_root():
    return {"message": "Bienvenido a tu plataforma de IA"}

@app.post("/upload_model/")
def upload_model(request: ModelUploadRequest):
    # Aquí iría la lógica para subir y guardar modelos
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
def predict(request: PredictionRequest):
    if len(request.features) != 2:
        raise HTTPException(status_code=400, detail="Se requieren exactamente 2 características.")

    # Lógica de predicción (ejemplo simple)
    resultado = sum(request.features)

    return {
        "usuario": "demo_user",  # Puedes extraerlo del token más adelante
        "prediccion": resultado
    }

@app.post("/fastapi/predict/")
def predict(features: List[float], username: str):
    # Aquí iría tu modelo de predicción
    prediction_result = sum(features)  # ejemplo: suma simple

    with Session(engine) as session:
        prediction = Prediction(
            username=username,
            feature1=features[0],
            feature2=features[1],
            prediction=prediction_result
        )
        session.add(prediction)
        session.commit()

    return {"usuario": username, "prediction": prediction_result}

@app.get("/fastapi/predictions/")
def get_predictions():
    with Session(engine) as session:
        predictions = session.exec(select(Prediction)).all()
        return predictions
