'''
Domain interface for modules
'''

from src.extract.logic import Extract

class Interface():

    def __init__(self, module):
        self.module = module

    def execute_module(self, *args, **kwargs):
        return self.module.run_module(*args, **kwargs)
