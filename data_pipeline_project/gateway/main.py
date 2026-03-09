# pyright: reportMissingImports=false
'''
'''

import os
from dotenv import load_dotenv
import uvicorn
from fastapi import FastAPI, UploadFile, File
from .pipeline import execute_pipeline

load_dotenv()

app = FastAPI()

@app.post("/run-pipeline")
async def run_pipeline(file: UploadFile = File(...)):
    result = await execute_pipeline(file)
    return result
