# pyright: reportMissingImports=false
# pyright: reportMissingModuleSource=false
'''
'''

import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from .src.visualizer import generate_visualization

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app.mount("/plots", StaticFiles(directory=os.path.join(BASE_DIR, "plots")), name="plots")

@app.post("/visualize")
def visualize(data: dict):
    return generate_visualization(data["transformed_id"])
