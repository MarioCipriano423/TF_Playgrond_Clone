'''
Domain interface for modules
'''

from .src.extract.logic import Extract

class Interface():

    extract = Extract()

    def __init__(self):
        pass

    def execute_module(self, *args, **kwargs):
        return self.extract.run_module(*args, **kwargs)
