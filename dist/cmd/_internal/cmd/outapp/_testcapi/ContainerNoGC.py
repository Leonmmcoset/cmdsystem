# encoding: utf-8
# module _testcapi
# from C:\Users\leonm\AppData\Local\Programs\Python\Python311\DLLs\_testcapi.pyd
# by generator 1.147
# no doc
# no imports

from .object import object

class ContainerNoGC(object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """a container value for test purposes"""



