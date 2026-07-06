from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  # 👈 السطر ده جديد للأمان
from pydantic import BaseModel
import joblib
import numpy as np

# إنشاء السيرفر
app = FastAPI(title="Titanic Survival Predictor API")

# 👈 الأربع سطور دول عشان المتصفح يرضى يشغل الموقع الاحترافي مع السيرفر
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# تحميل الموديل
model = joblib.load('titanic_model.pkl')

class Passenger(BaseModel):
    PassengerId: int
    Name: str
    Pclass: int
    Age: float
    SibSp: int
    Parch: int
    Sex_1: int 

@app.post("/predict")
def predict_survival(passenger: Passenger):
    input_data = np.array([[
        passenger.PassengerId,
        passenger.Pclass,
        passenger.Age,
        passenger.SibSp,
        passenger.Parch,
        passenger.Sex_1
    ]])
    
    prediction = model.predict(input_data)
    
    if prediction[0] == 1:
        return {"status": "نجاح", "result": f"الراكب ({passenger.Name}) سينجو بإذن الله!"}
    else:
        return {"status": "وفاة", "result": f"للأسف، الراكب ({passenger.Name}) لن ينجو."}