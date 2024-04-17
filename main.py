from fastapi import FastAPI, HTTPException
import uvicorn
from pydantic import BaseModel
import joblib
import pandas as pd

#  create an instance of fastapi
app = FastAPI()

# Load the models
gaussian_pipeline = joblib.load('./models/best_gaussian_model.joblib')
logistic_pipeline = joblib.load('./models/best_logistic_model.joblib')
# load the encoder
encoder = joblib.load('./models/encoder.joblib')

class BloodFeatures(BaseModel):
    Plasma_glucose: int
    Blood_Work_R1: int
    Blood_Pressure: int
    Blood_Work_R2: int
    Blood_Work_R3: int
    BMI: float
    Blood_Work_R4: float

# Index route
@app.get("/")
def index():
    return {'message': 'Hello, Welcome to Sepsis Prediction with FastAPI'}

# Create prediction endpoint
@app.post("/predict")
def predict(blood_feature: BloodFeatures):
    try:
        # Convert input features into a DataFrame
        df = pd.DataFrame([blood_feature.model_dump()])

        # Make predictions using Gaussian model
        prediction_gaussian = gaussian_pipeline.predict(df)
        prediction_gaussian = int(prediction_gaussian[0])
        prediction_gaussian = encoder.inverse_transform([prediction_gaussian])[0]

        # Make predictions using Logistic model
        prediction_logistic = logistic_pipeline.predict(df)
        prediction_logistic = int(prediction_logistic[0])
        prediction_logistic = encoder.inverse_transform([prediction_logistic])[0]

        return {'gaussian_prediction': prediction_gaussian, 'logistic_prediction': prediction_logistic}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Server Error: {str(e)}')

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000, debug=True)
