# pyright: reportMissingImports=false
# pyright: reportMissingModuleSource=false
'''
'''

from src.base_loader import BaseLoader
import uuid
import os
from fastapi import UploadFile


class Loader(BaseLoader):

    DATA_DIR = "/data/datasets"

    def __init__(self):
        pass

    def setup(self):
        os.makedirs(self.DATA_DIR, exist_ok=True)

    async def load_file(self, file: UploadFile):
        dataset_id = str(uuid.uuid4())
        file_extension = file.filename.split(".")[-1]
        safe_filename = f"{dataset_id}.{file_extension}"

        file_path = os.path.join(self.DATA_DIR, safe_filename)

        with open(file_path, "wb") as buffer:
            content = await file.read()
            buffer.write(content)
        
        return dataset_id
