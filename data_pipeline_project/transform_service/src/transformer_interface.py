# pyright: reportMissingImports=false
# pyright: reportMissingModuleSource=false
'''
HL interface for transform moduels
'''

from src.modules.transformer_core import Transformer

class TransformerInterface:

    def __init__(self):
        pass

    def run_transformer(self, *args, **kwargs):
        transformer = Transformer()
        transformer.setup()
        return transformer.transform_dataset(*args, **kwargs)
