import os
from datetime import date
from dotenv import load_dotenv
from fastapi import APIRouter, HTTPException, status

from src.routes.knn_routes import knn_router
from src.routes.naive_bayes import naive_bayes_router
### import all the routers
from src.routes.random_forest import random_forest_router
from src.routes.svm_route import svm_router
from src.routes.xgboost_route import xgboost_router
from src.routes.logistic_regression import logistic_regression_router

app_router = APIRouter()

@app_router.get('/')
def root():
    return {"name": "Edwards Disease prediction",
            "version": '0.0.1',
            "route": '/',
            'date': date.today().strftime('%B %d, %Y')
            }


### attach other routes
app_router.include_router(svm_router)
app_router.include_router(random_forest_router)
app_router.include_router(xgboost_router)
app_router.include_router(logistic_regression_router)
app_router.include_router(naive_bayes_router)
app_router.include_router(knn_router)
