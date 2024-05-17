# encoding: utf-8
# module _testcapi
# from C:\Users\leonm\AppData\Local\Programs\Python\Python311\DLLs\_testcapi.pyd
# by generator 1.147
# no doc
# no imports

from .object import object

class HeapCTypeSetattr(object):
    """
    A heap type without GC, but with overridden __setattr__.
    
    The 'value' attribute is set to 10 in __init__ and updated via attribute setting.
    """
    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    pvalue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



