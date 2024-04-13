from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI()


gaussian_pipeline = joblib.load('./models/best_gaussian_model.joblib')
encoder = joblib.load('./models/encoder.joblib')
logistic_pipeline = joblib.load('./models/best_logistic_model.joblib')

class blood_features(BaseModel):
    Plasma_glucose:int
    Blood_Work_R1:int
    Blood_Pressure:int
    Blood_Work_R2: int
    Blood_Work_R3: int
    BMI: float
    Blood_Work_R4: float
    
# Index route
@app.get("/")
def index():
    return{'message':'Hello, Welcome to Sepsis Prediction FastAPI API'}


# Create prediction endpoint
@app.post("/predict")
def predict (df:blood_features):


# gausian prediction
 @app.post('/predict')
 def gaussian_prediction(data=blood_features):
   # convert model into a dictionary then a dataframe
    df = pd.DataFrame([data.model_dump()])
    # make predictions
    prediction = gaussian_pipeline.predict(df)
    # convert predictions into an integer instead of an array
    prediction = int(prediction[0])
    # encode the prediction
    prediction = encoder.inverse_transform([prediction])[0]
    # predict probabilities
    prediction_proba = gaussian_pipeline.predict_proba(df)
    # convert probabilities into list
    probabilities = prediction_proba.tolist()

    # return the encoded prediction
    return{'prediction':prediction,'probabilities':probabilities}


 @app.post('/predict')
 def logistic_prediction(data=blood_features):
   # convert model into a dictionary then a dataframe
    df = pd.DataFrame([data.model_dump()])
    # make predictions
    prediction = logistic_pipeline.predict(df)
    # convert predictions into an integer instead of an array
    prediction = int(prediction[0])
    # encode the prediction
    prediction = encoder.inverse_transform([prediction])[0]
    # predict probabilities
    prediction_proba = logistic_pipeline.predict_proba(df)
    # convert probabilities into list
    probabilities = prediction_proba.tolist()

    # return the encoded prediction
    return{'prediction':prediction,'probabilities':probabilities}



    # df_encoded = encoder.transform(df)
   
    # # Prediction
    # raw_prediction = model.predict(df_encoded)

if __name__ == '__main__':
    uvicorn.run(app,host="0.0.0.0",port=8000,debug=True)