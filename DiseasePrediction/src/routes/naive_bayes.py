
import os
import joblib
import pandas as pd
import xgboost as xgb
from fastapi import APIRouter
from src.routes.random_forest import PredictBody
from src.utils.model_creator import ModelCreator

naive_bayes_router = APIRouter(
    prefix="/naive_bayes",
    tags=["Naive Bayes"],
)

@naive_bayes_router.post('/predict')
async def naive_bayes_predict(Body: PredictBody):
    ### check if the model exists
    model_path = './models/naive_bayes_model.joblib'

    ### if no model, create the model
    if not os.path.exists(model_path):
        ModelCreator('datasets/covid_data_2020_2021.csv').create_naive_bayes()

    model = joblib.load(model_path)

    ### convert the user inputs into a dataframe
    user_inputs = pd.DataFrame([Body.model_dump()])
    user_inputs.drop(['hospital_id'], axis=1, inplace=True)

    # Convert boolean columns to 0s and 1s
    boolean_columns = ['cough', 'fever', 'sore_throat', 'shortness_of_breath', 'head_ache']
    user_inputs[boolean_columns] = user_inputs[boolean_columns].astype(int)

    ### continue to make predictions
    prediction = model.predict(user_inputs)

    return {
        "prediction": prediction[0].item(),
        'message': f'Naive Bayes result for the patient with id {Body.hospital_id} is {prediction[0].item()}'
    }