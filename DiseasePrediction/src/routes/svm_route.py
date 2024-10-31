import os
import joblib
import pandas as pd
from pydantic import BaseModel
from fastapi import APIRouter
from rich import print
from .random_forest import PredictBody
from src.utils.model_creator import ModelCreator

svm_router = APIRouter(prefix="/svm", tags=["SVM Model"])

@svm_router.post("/predict")
async def svm_predict(body: PredictBody):
    print(body)
    ### check if the model exists
    model_path = './models/svm_pca.joblib'

    ### if no model, create the model
    if not os.path.exists(model_path):
        ModelCreator('datasets/covid_data_2020_2021.csv').create_svm()

    model = joblib.load(model_path)

    ### convert the user inputs into a dataframe
    user_inputs = pd.DataFrame([body.model_dump()])
    user_inputs.drop(['hospital_id'], axis=1, inplace=True)

    # Convert boolean columns to 0s and 1s
    boolean_columns = ['cough', 'fever', 'sore_throat', 'shortness_of_breath', 'head_ache']
    user_inputs[boolean_columns] = user_inputs[boolean_columns].astype(int)

    ### continue to make predictions
    prediction = model.predict(user_inputs)

    return {
        "prediction": prediction[0].item(),
        'message': 'This is the SVM response'
    }