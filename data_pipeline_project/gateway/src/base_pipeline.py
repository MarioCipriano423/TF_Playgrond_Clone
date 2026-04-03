# pyright: reportMissingImports=false
# pyright: reportMissingModuleSource=false

from abc import ABC, abstractmethod

class BasePipeline(ABC):
    @abstractmethod
    def setup(self):
        pass

    @abstractmethod
    def execute(self):
        pass
