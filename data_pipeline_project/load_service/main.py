# pyright: reportMissingImports=false
'''

'''

from fastapi import FastAPI, UploadFile, File
from src.loader_interface import LoaderInterface

app = FastAPI()
loader = LoaderInterface()

@app.post("/load")
async def load(file: UploadFile = File(...)):
    dataset_id = await loader.run_loader(file)
    return {"dataset_id": dataset_id}
