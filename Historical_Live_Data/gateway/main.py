from fastapi import FastAPI

from services.QCFD_Service.domain.src.extract.logic import Extract

app = FastAPI()

@app.get("/extract")
def run_extract():

    extractor = Extract()
    result = extractor.run_module()

    return {"message": result}