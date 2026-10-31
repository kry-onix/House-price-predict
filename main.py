from fastapi import FastAPI
from pydantic import BaseModel
import joblib, pandas as pd

app = FastAPI()
m = joblib.load("model.pkl")
cols = joblib.load("cols.pkl")

class Inp(BaseModel):
	location: str
	sqft: float
	bath: int
	bhk: int

@app.post("/predict")
def predict(d:Inp):
	row = dict.fromkeys(cols, 0)
	row["total_sqft"] = d.sqft
	row["bath"] =d.bath
	row["bhk"] = d.bhk
	k = "location_" + d.location.strip()
	if k not in row:
		k = "locatio_other"
	row[k] = 1
	p = m.predict(pd.DataFrame([row]))[0]
	return {"price_lakh": round(p, 2)}

