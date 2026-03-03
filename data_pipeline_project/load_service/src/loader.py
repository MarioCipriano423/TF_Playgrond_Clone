'''
'''

import uuid
import os
from fastapi import UploadFile

DATA_DIR = "datasets"
os.makedirs(DATA_DIR, exist_ok=True)

async def load_file(file: UploadFile):
    dataset_id = str(uuid.uuid4())
    file_extension = file.filename.split(".")[-1]
    safe_filename = f"{dataset_id}.{file_extension}"

    file_path = os.path.join(DATA_DIR, safe_filename)

    with open(file_path, "wb") as buffer:
        content = await file.read()
        buffer.write(content)
    
    return dataset_id
