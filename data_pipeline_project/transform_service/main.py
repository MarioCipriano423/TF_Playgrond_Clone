# pyright: reportMissingImports=false
'''
'''

from fastapi import FastAPI
from .src.transformer import transform_dataset

app = FastAPI()

@app.post("/transform")
def transform(data: dict):
    transformed_id = transform_dataset(data["dataset_id"])
    return{"transformed_id": transformed_id}
