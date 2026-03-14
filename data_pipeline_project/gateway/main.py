# pyright: reportMissingImports=false
'''
'''

from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from pipeline import execute_pipeline
import httpx
import io

app = FastAPI()

origins = [
    "http://localhost:5173",   # frontend dev
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/run-pipeline")
async def run_pipeline(file: UploadFile = File(...)):

    result = await execute_pipeline(file)

    image_url = result["internal_plot_url"]

    async with httpx.AsyncClient() as client:
        img_response = await client.get(image_url)

    return StreamingResponse(
        io.BytesIO(img_response.content),
        media_type="image/png"
    )