from fastapi import FastAPI

from services.test_service.src.interface import Interface

app = FastAPI()

@app.get("/extract")
def run_extract():

    extractor = Interface()
    result = extractor.execute_module()

    return {"message": result}