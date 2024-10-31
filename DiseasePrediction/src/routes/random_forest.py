import os
import joblib
import pandas as pd
from pydantic import BaseModel
from fastapi import APIRouter
from rich import print

from src.utils.model_creator import ModelCreator

random_forest_router = APIRouter(prefix="/random_forest", tags=["Random Forest"])


### Parameter class types
class PredictBody(BaseModel):
    hospital_id: str
    cough: bool
    fever: bool
    sore_throat: bool
    shortness_of_breath: bool
    head_ache: bool


@random_forest_router.post("/predict")
async def rf_predict(Body: PredictBody):

    print(Body)
    ### check if the model exists
    model_path = './models/random_forest_model.joblib'

    ### if no model, create the model
    if not os.path.exists(model_path):
        ModelCreator('datasets/covid_data_2020_2021.csv').create_random_forest()

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
        'message': 'This is the random forest response'
    }