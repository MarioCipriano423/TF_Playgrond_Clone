# pyright: reportMissingImports=false
# pyright: reportMissingModuleSource=false

from abc import ABC, abstractmethod

class BaseVisualizer(ABC):
    @abstractmethod
    def setup(self):
        pass

    def generate_visualization(self):
        pass
