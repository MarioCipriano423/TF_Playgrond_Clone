# pyright: reportMissingImports=false
# pyright: reportMissingModuleSource=false

import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from src.visualizer_interface import VisualizerInterface

app = FastAPI()
visualizer = VisualizerInterface()

PLOTS_DIR = "/data/plots"
os.makedirs(PLOTS_DIR, exist_ok=True)
app.mount("/plots", StaticFiles(directory=PLOTS_DIR), name="plots")

@app.post("/visualize")
def visualize(data: dict):
    return visualizer.run_visualizer(data["transformed_id"])
