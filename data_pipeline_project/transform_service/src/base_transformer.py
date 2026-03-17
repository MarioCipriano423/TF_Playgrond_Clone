# pyright: reportMissingImports=false
# pyright: reportMissingModuleSource=false
'''
Base class methods for the transform service
'''

from abc import ABC, abstractmethod

class BaseTransformer(ABC):
    @abstractmethod
    def setup(self):
        pass

    @abstractmethod
    def transform_dataset(self):
        pass
