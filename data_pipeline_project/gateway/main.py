# pyright: reportMissingImports=false
'''
'''

from fastapi import FastAPI, UploadFile, File
from .pipeline import execute_pipeline

app = FastAPI()

@app.post("/run-pipeline")
async def run_pipeline(file: UploadFile = File(...)):
    result = await execute_pipeline(file)
    return result
