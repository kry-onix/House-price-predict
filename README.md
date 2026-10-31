# House Price Predict

## Tech
Python, Pandas, Scikit-learn, (Random Forest), FastAPI

## Model
- Data: Bengluru House Data(13,000+ rows)
- Cleaning: remove outliers and rare locations
- R2 score: 0.71

## Run
pip install -r reqirements.txt
uvicorn main:app --reload

## API
POST /predict

body:
{"location": "Whitefield", "sqft":1200, "bath":2, "bhk":2}
response:
{"price_lakh": 47.93}

## Live
(Render)
