# pyright: reportMissingImports=false
# pyright: reportMissingModuleSource=false
'''

'''

from fastapi import FastAPI
from src.transformer_interface import TransformerInterface

app = FastAPI()
transformer = TransformerInterface()

@app.post("/transform")
def transform(data: dict):
    transformed_id = transformer.run_transformer(data["dataset_id"])
    return{"transformed_id": transformed_id}
