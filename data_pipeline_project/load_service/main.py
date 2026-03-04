'''
'''

import os
from dotenv import load_dotenv
import uvicorn
from fastapi import FastAPI, UploadFile, File
from .src.loader import load_file

load_dotenv()

app = FastAPI()

@app.post("/load")
async def load(file: UploadFile = File(...)):
    dataset_id = await load_file(file)
    return {"dataset_id": dataset_id}

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=os.getenv("HOST"),
        port=int(os.getenv("LOAD_SERVICE_PORT")),
        reload=True
    )
