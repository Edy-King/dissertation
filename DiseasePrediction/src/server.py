import os
from fastapi import FastAPI
from dotenv import load_dotenv
from rich.pretty import pprint as print

from src.middlewares.register import app_register

load_dotenv()
PORT = os.environ.get("PORT")

### create an app instance
app = FastAPI()

### register the middlewares
app_register(app)

### run the server
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app,
                host="0.0.0.0",
                port=int(PORT)
                )
