# pyright: reportMissingImports=false
# pyright: reportMissingModuleSource=false

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from src.pipeline_interface import PipelineInterface
import httpx
import io

app = FastAPI()
pipeline = PipelineInterface()

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/run-pipeline")
async def run_pipeline(playground_config):
    ORCHESTRATOR_URL = ""
    
    # Gateway POST -> Orchestrator -> Response (image URL)
    async with httpx.AsyncClient() as client:
        pipeline_response = await client.post(
            ORCHESTRATOR_URL,
            json={"playground_config": playground_config}
        )
        result = pipeline_response.json()

    # image URL -> client -> download 
    return {
        "image_url": result["internal_plot_url"]
    }
