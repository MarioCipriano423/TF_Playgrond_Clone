# pyright: reportMissingImports=false
# pyright: reportMissingModuleSource=false

from src.modules.pipeline_core import Pipeline

class PipelineInterface:

    def __init__(self):
        pass

    def run_pipeline(self, *args, **kwargs):
        pipeline = Pipeline()
        pipeline.setup()
        return pipeline.execute_pipeline(*args, **kwargs)
