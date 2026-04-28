# pyright: reportMissingImports=false
# pyright: reportMissingModuleSource=false

from pydantic import BaseModel, Field 
from typing import List, Literal, Optional

class DatasetConfig(BaseModel):
    type: Literal["iris", "sintenic"]
    size: float = Field(ge=50, le=100)
    train_test_split: float = Field(ge=0.1, le=0.9)

# In process... 
