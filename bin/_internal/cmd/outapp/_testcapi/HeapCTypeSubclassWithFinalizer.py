# encoding: utf-8
# module _testcapi
# from C:\Users\leonm\AppData\Local\Programs\Python\Python311\DLLs\_testcapi.pyd
# by generator 1.147
# no doc
# no imports

from .HeapCTypeSubclass import HeapCTypeSubclass

class HeapCTypeSubclassWithFinalizer(HeapCTypeSubclass):
    """
    Subclass of HeapCType with a finalizer that reassigns __class__.
    
    __class__ is set to plain HeapCTypeSubclass during finalization.
    __init__ sets the 'value' attribute to 10 and 'value2' to 20.
    """
    def __del__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    value2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



