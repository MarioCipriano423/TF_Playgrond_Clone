import httpx

LOAD_URL = "https://127.0.0.1:8001/load"
TRANSFORM_URL = "https://127.0.0.1:8002/transform"
VISUALIZE_URL = "https://127.0.0.1:8003/visualize"

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
