# Titanic Survival Predictor

A small machine learning project that predicts whether a Titanic passenger would have survived, based on passenger details. The trained model is served through a FastAPI endpoint, with two front ends: a Streamlit app and a plain HTML form.

## Input features

| Field | Meaning |
|---|---|
| Pclass | Ticket class (1, 2 or 3) |
| Age | Age in years |
| SibSp | Number of siblings / spouses aboard |
| Parch | Number of parents / children aboard |
| Sex_1 | Sex encoded as a number |
| PassengerId | Passenger number, currently also passed to the model (see Known limitations) |

The passenger name is only used to personalise the result message. It is not a model input.

## Files

- titanic_model.pkl: the trained model, loaded with joblib
- main.py: FastAPI server with a POST /predict endpoint (CORS enabled)
- app.py: Streamlit front end that calls the API
- index.html: HTML form front end that calls the API

## Run locally

1. Install the requirements:
   
   pip install fastapi uvicorn streamlit requests joblib numpy scikit-learn
   
2. Start the API from the project folder:
   
   uvicorn main:app --reload
   
   Docs are at http://127.0.0.1:8000/docs
3. Use one of the front ends:
   - Streamlit: streamlit run app.py
   - HTML: open index.html in a browser

The front ends call http://127.0.0.1:8000/predict, so the API must be running on your machine.

## Model

- Model type: [WRITE THE MODEL YOU USED]
- Accuracy: [WRITE YOUR REAL TEST RESULT, or delete this line]
- Training data: [Titanic dataset source]

## Known limitations

- The model currently takes PassengerId as an input. It is only a row number, so it should be removed and the model retrained.
- It is a learning project, not a live demo: the API runs locally only.
- The training notebook is not in this repo yet.

## Author

Moaz Wael. GitHub: https://github.com/Moaz2006
