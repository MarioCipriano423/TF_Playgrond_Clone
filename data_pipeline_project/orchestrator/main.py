# pyright: reportMissingImports=false
# pyright: reportMissingModuleSource=false

from fastapi import FastAPI
from src.builder_face import Builder

app = FastAPI()
pb = Builder()

@app.post("orchestrator")
async def orchestrator(playgrund_config):

    # Getting playground client config for realtime-build pipeline  
    
    # build method for pipeline constructor
    pipeline = pb.build()

    return "Work in progress..."
