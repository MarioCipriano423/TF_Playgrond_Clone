'''
'''

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from src.visualizer import generate_visualization

app = FastAPI()

app.mount("/plots", StaticFiles(directory="plots"), name="plots")

@app.post("/visualize")
def visualize(data: dict):
    return generate_visualization(data["transformed_id"])
