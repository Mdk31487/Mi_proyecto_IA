from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class Prediction(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    feature1: float
    feature2: float
    prediction: float
    timestamp: datetime = Field(default_factory=datetime.utcnow)
