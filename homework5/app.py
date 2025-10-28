from fastapi import FastAPI
from pydantic import BaseModel
import pickle

with open("pipeline_v1.bin", "rb") as f:
    model = pickle.load(f)

class Lead(BaseModel):
    lead_source: str
    number_of_courses_viewed: int
    annual_income: float

app = FastAPI()

@app.post("/predict")
def predict(lead: Lead):
    data = lead.dict()
    prob = model.predict_proba([data])[0, 1]
    return {"conversion_probability": prob}
