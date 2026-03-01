'''
'''

from fastapi import FastAPI
from src.visualizer import generate_visualization

app = FastAPI()

@app.post("/visualize")
def visualize(data: dict):
    result = generate_visualization(data["transformed_id"])
    return result
