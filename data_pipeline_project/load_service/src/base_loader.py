# pyright: reportMissingImports=false
# pyright: reportMissingModuleSource=false
'''
Base class methods for the load service modules
'''

from abc import ABC, abstractmethod

class BaseLoader(ABC):
    @abstractmethod
    def setup(self):
        pass
    
    @abstractmethod
    def load_file(self):
        pass
