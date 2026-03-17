# pyright: reportMissingImports=false
# pyright: reportMissingModuleSource=false
'''
HL interface for load modules
'''

from src.modules.loader_core import Loader

class LoaderInterface:

    def __init__(self):
        pass

    def run_loader(self, *args, **kwargs):
        loader = Loader()
        loader.setup()
        return loader.load_file(*args, **kwargs)
