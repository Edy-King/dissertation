# Disease Prediction API

This project is a FastAPI-based web service for predicting diseases, specifically focused on SARS-CoV-2 (COVID-19) classification using machine learning techniques.

## Table of Contents

1. [Project Structure](#project-structure)
2. [File Descriptions](#file-descriptions)
3. [Requirements](#requirements)
4. [Getting Started](#getting-started)
5. [API Endpoints](#api-endpoints)
6. [Machine Learning Models](#machine-learning-models)
7. [Data Preprocessing](#data-preprocessing)
8. [Environment Variables](#environment-variables)
9. [Contributing](#contributing)
10. [License](#license)

## Project Structure

│
├── src/
│ ├── jupyter/
│ │ └── script.ipynb
│ ├── middlewares/
│ │ └── register.py
│ ├── routes/
│ │ ├── app_routes.py
│ │ ├── random_forest.py
│ │ └── xgboost_route.py
│ ├── utils/
│ │ └── model_creator.py
│ └── server.py
│
├── datasets/
│ └── covid_data_2020_2021.csv
│
├── models/
│ ├── random_forest_model.joblib
│ └── xgboost_model.joblib
│
├── .env
├── README.md
└── requirements.txt

## File Descriptions

1. `src/jupyter/script.ipynb`: Jupyter notebook containing exploratory data analysis, model training, and evaluation.

2. `src/middlewares/register.py`: Handles middleware registration, including CORS configuration.

3. `src/routes/app_routes.py`: Defines the main application routes and includes other route modules.

4. `src/routes/random_forest.py`: Implements the Random Forest prediction endpoint.

5. `src/routes/xgboost_route.py`: Implements the XGBoost prediction endpoint.

6. `src/utils/model_creator.py`: Contains the `ModelCreator` class for data preprocessing and model creation.

7. `src/server.py`: The main entry point for the FastAPI application.

8. `requirements.txt`: Lists all the Python dependencies required for the project.

## Requirements

To run this project, you need:

- Python 3.7+
- pip (Python package installer)

All other dependencies are listed in `requirements.txt`.

## Getting Started

1. Clone the repository:

   ```
   git clone https://github.com/yourusername/disease-prediction-api.git
   cd disease-prediction-api
   ```

2. Create a virtual environment (optional but recommended):

   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:

   ```
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   Create a `.env` file in the root directory and add the following:

   ```
   PORT=8000
   ALLOWED_ORIGINS=http://localhost:3000,http://example.com
   ```

5. Run the server:
   ```
   python src/server.py
   ```

The API should now be running at `http://localhost:8000`.

## API Endpoints

1. Root endpoint:

   - URL: `/`
   - Method: GET
   - Description: Returns basic information about the API.

2. Random Forest Prediction:

   - URL: `/random_forest/predict`
   - Method: POST
   - Body: JSON object with patient symptoms
   - Description: Predicts COVID-19 using Random Forest model.

3. XGBoost Prediction:
   - URL: `/xgboost/predict`
   - Method: POST
   - Body: JSON object with patient symptoms
   - Description: Predicts COVID-19 using XGBoost model.

## Machine Learning Models

The project uses two machine learning models:

1. Random Forest Classifier
2. XGBoost Classifier

Both models are trained on COVID-19 symptom data and can predict the likelihood of a positive case based on input symptoms.

## Data Preprocessing

The `ModelCreator` class in `src/utils/model_creator.py` handles data preprocessing:

- Loads data from CSV
- Selects relevant features
- Encodes target variable
- Applies undersampling to balance the dataset
- Splits data into training and testing sets


## Data availability
https://drive.google.com/file/d/15dDPeekh7qvU6no4RSjP9TwKvs4Bi6fP/view?usp=sharing

## Environment Variables

- `PORT`: The port number on which the server will run.
- `ALLOWED_ORIGINS`: Comma-separated list of allowed origins for CORS.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).
