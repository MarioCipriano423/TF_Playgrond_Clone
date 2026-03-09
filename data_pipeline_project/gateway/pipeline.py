# pyright: reportMissingImports=false
'''
'''

import os
import httpx
from dotenv import load_dotenv

load_dotenv()

LOAD_URL = f"{os.getenv('LOAD_SERVICE_URL')}/load"
TRANSFORM_URL = f"{os.getenv('TRANSFORM_SERVICE_URL')}/transform"
VISUALIZE_URL = f"{os.getenv('VISUALIZATION_SERVICE_URL')}/visualize"

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
