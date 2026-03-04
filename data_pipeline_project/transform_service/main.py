'''
'''

import os
from dotenv import load_dotenv
import uvicorn
from fastapi import FastAPI
from .src.transformer import transform_dataset

load_dotenv()

app = FastAPI()

@app.post("/transform")
def transform(data: dict):
    transformed_id = transform_dataset(data["dataset_id"])
    return{"transformed_id": transformed_id}

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=os.getenv("HOST"),
        port=int(os.getenv("TRANSFORM_SERVICE_PORT")),
        reload=True
    )
