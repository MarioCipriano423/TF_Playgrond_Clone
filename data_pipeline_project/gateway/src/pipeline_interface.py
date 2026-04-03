# pyright: reportMissingImports=false
# pyright: reportMissingModuleSource=false

from src.base_pipeline import BasePipeline
from src.modules.pipeline_core import Pipeline

class PipelineInterface(BasePipeline):

    def __init__(self):
        pass

    def setup(self):
        pass

    def execute(self, *args, **kwargs):
        pipeline = Pipeline()
        pipeline.setup()
        return pipeline.execute_pipeline(*args, **kwargs)
