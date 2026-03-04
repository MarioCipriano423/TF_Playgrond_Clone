'''
'''

import os
import httpx
from dotenv import load_dotenv

load_dotenv()

HOST = os.getenv("HOST")

LOAD_URL = f"http://{HOST}:{os.getenv('LOAD_SERVICE_PORT')}/load"
TRANSFORM_URL = f"http://{HOST}:{os.getenv('TRANSFORM_SERVICE_PORT')}/transform"
VISUALIZE_URL = f"http://{HOST}:{os.getenv('VISUALIZATION_SERVICE_PORT')}/visualize"

async def execute_pipeline(file):
    async with httpx.AsyncClient() as client:

        load_response = await client.post(
            LOAD_URL,
            files={"file": (file.filename, await file.read())}
        )
        dataset_id = load_response.json()["dataset_id"]

        transform_response = await client.post(
            TRANSFORM_URL,
            json={"dataset_id": dataset_id}
        )
        transformed_id = transform_response.json()["transformed_id"]

        visualize_response = await client.post(
            VISUALIZE_URL,
            json={"transformed_id": transformed_id}
        )

        return visualize_response.json()
