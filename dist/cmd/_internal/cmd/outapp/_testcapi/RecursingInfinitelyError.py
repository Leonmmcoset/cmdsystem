# encoding: utf-8
# module _testcapi
# from C:\Users\leonm\AppData\Local\Programs\Python\Python311\DLLs\_testcapi.pyd
# by generator 1.147
# no doc
# no imports

from .Exception import Exception

class RecursingInfinitelyError(Exception):
    """ Instantiating this exception starts infinite recursion. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


