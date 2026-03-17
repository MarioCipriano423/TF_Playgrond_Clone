# pyright: reportMissingImports=false
# pyright: reportMissingModuleSource=false

from src.base_pipeline import BasePipeline
import os
import httpx
from dotenv import load_dotenv

load_dotenv()

class Pipeline(BasePipeline):

    LOAD_URL = f"{os.getenv('LOAD_SERVICE_URL')}/load"
    TRANSFORM_URL = f"{os.getenv('TRANSFORM_SERVICE_URL')}/transform"
    VISUALIZE_URL = f"{os.getenv('VISUALIZATION_SERVICE_URL')}/visualize"
    VISUALIZATION_BASE = os.getenv("VISUALIZATION_SERVICE_URL")

    def __init__(self):
        pass

    def setup(self):
        pass

    async def execute_pipeline(self, file):

        async with httpx.AsyncClient() as client:

            load_response = await client.post(
                self.LOAD_URL,
                files={"file": (file.filename, await file.read())}
            )
            dataset_id = load_response.json()["dataset_id"]

            transform_response = await client.post(
                self.TRANSFORM_URL,
                json={"dataset_id": dataset_id}
            )
            transformed_id = transform_response.json()["transformed_id"]

            visualize_response = await client.post(
                self.VISUALIZE_URL,
                json={"transformed_id": transformed_id}
            )

            data = visualize_response.json()

            data["internal_plot_url"] = f"{self.VISUALIZATION_BASE}{data['plot_url']}"

            return data
