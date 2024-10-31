import os
import joblib
import pandas as pd
import xgboost as xgb
from fastapi import APIRouter
from src.routes.random_forest import PredictBody
from src.utils.model_creator import ModelCreator

xgboost_router = APIRouter(
    prefix="/xgboost",
    tags=["XGBoost"],
)

@xgboost_router.post('/predict')
async def xgb_predict(Body: PredictBody):
    ### check if the model exists
    model_path = './models/xgb_model.joblib'

    ### if no model, create the model
    if not os.path.exists(model_path):
        ModelCreator('datasets/covid_data_2020_2021.csv').create_xgboost()

    model = joblib.load(model_path)

    ### convert the user inputs into a dataframe
    user_inputs = pd.DataFrame([Body.model_dump()])
    user_inputs.drop(['hospital_id'], axis=1, inplace=True)

    ### continue to make predictions
    # For XGBoost, we need to use DMatrix for prediction
    duser_inputs = xgb.DMatrix(user_inputs)
    prediction = model.predict(duser_inputs)

    return {
        "prediction": prediction[0].item(),
        'message': f'The patient with id {Body.hospital_id} is {prediction[0].item()}'
    }