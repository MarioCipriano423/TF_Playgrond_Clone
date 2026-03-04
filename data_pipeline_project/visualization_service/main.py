'''
'''

import os
from dotenv import load_dotenv
import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from .src.visualizer import generate_visualization

load_dotenv()

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app.mount("/plots", StaticFiles(directory=os.path.join(BASE_DIR, "plots")), name="plots")

@app.post("/visualize")
def visualize(data: dict):
    return generate_visualization(data["transformed_id"])

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=os.getenv("HOST"),
        port=int(os.getenv("VISUALIZATION_SERVICE_PORT")),
        reload=True
    )
