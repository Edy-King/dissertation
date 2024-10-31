import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routes.app_routes import app_router

load_dotenv()
allowed_origins = os.getenv("ALLOWED_ORIGINS")

# ################################################
# ### Register middleware handler
# #################################################


def app_register(app: FastAPI):
    ### CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=allowed_origins.split(','),
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    ### attach the routes
    app.include_router(app_router)