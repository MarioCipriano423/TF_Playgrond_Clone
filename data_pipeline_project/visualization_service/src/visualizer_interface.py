# pyright: reportMissingImports=false
# pyright: reportMissingModuleSource=false

from src.modules.visualizer_core import Visualizer

class VisualizerInterface:

    def __init__(self):
        pass

    def run_visualizer(self, *args, **kwargs):
        visualizer = Visualizer()
        visualizer.setup()
        return visualizer.generate_visualization(*args, **kwargs)
