# encoding: utf-8
# module _tracemalloc
# from (built-in)
# by generator 1.147
""" Debug module to trace memory blocks allocated by Python. """
# no imports

# functions

def clear_traces(*args, **kwargs): # real signature unknown
    """ Clear traces of memory blocks allocated by Python. """
    pass

def get_traceback_limit(*args, **kwargs): # real signature unknown
    """
    Get the maximum number of frames stored in the traceback of a trace.
    
    By default, a trace of an allocated memory block only stores
    the most recent frame: the limit is 1.
    """
    pass

def get_traced_memory(*args, **kwargs): # real signature unknown
    """
    Get the current size and peak size of memory blocks traced by tracemalloc.
    
    Returns a tuple: (current: int, peak: int).
    """
    pass

def get_tracemalloc_memory(*args, **kwargs): # real signature unknown
    """
    Get the memory usage in bytes of the tracemalloc module.
    
    This memory is used internally to trace memory allocations.
    """
    pass

def is_tracing(*args, **kwargs): # real signature unknown
    """ Return True if the tracemalloc module is tracing Python memory allocations. """
    pass

def reset_peak(*args, **kwargs): # real signature unknown
    """
    Set the peak size of memory blocks traced by tracemalloc to the current size.
    
    Do nothing if the tracemalloc module is not tracing memory allocations.
    """
    pass

def start(*args, **kwargs): # real signature unknown
    """
    Start tracing Python memory allocations.
    
    Also set the maximum number of frames stored in the traceback of a
    trace to nframe.
    """
    pass

def stop(*args, **kwargs): # real signature unknown
    """
    Stop tracing Python memory allocations.
    
    Also clear traces of memory blocks allocated by Python.
    """
    pass

def _get_object_traceback(*args, **kwargs): # real signature unknown
    """
    Get the traceback where the Python object obj was allocated.
    
    Return a tuple of (filename: str, lineno: int) tuples.
    Return None if the tracemalloc module is disabled or did not
    trace the allocation of the object.
    """
    pass

def _get_traces(*args, **kwargs): # real signature unknown
    """
    Get traces of all memory blocks allocated by Python.
    
    Return a list of (size: int, traceback: tuple) tuples.
    traceback is a tuple of (filename: str, lineno: int) tuples.
    
    Return an empty list if the tracemalloc module is disabled.
    """
    pass

# classes

class __loader__(object):
    """
    Meta path import for built-in modules.
    
        All methods are either class or static methods to avoid the need to
        instantiate the class.
    """
    def create_module(spec): # reliably restored by inspect
        """ Create a built-in module """
        pass

    def exec_module(module): # reliably restored by inspect
        """ Exec a built-in module """
        pass

    @classmethod
    def find_module(cls, *args, **kwargs): # real signature unknown
        """
        Find the built-in module.
        
                If 'path' is ever specified then the search is considered a failure.
        
                This method is deprecated.  Use find_spec() instead.
        """
        pass

    @classmethod
    def find_spec(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def get_code(cls, *args, **kwargs): # real signature unknown
        """ Return None as built-in modules do not have code objects. """
        pass

    @classmethod
    def get_source(cls, *args, **kwargs): # real signature unknown
        """ Return None as built-in modules do not have source code. """
        pass

    @classmethod
    def is_package(cls, *args, **kwargs): # real signature unknown
        """ Return False as built-in modules are never packages. """
        pass

    @classmethod
    def load_module(cls, *args, **kwargs): # real signature unknown
        """
        Load the specified module into sys.modules and return it.
        
            This method is deprecated.  Use loader.exec_module() instead.
        """
        pass

    def module_repr(module): # reliably restored by inspect
        """
        Return repr for the module.
        
                The method is deprecated.  The import machinery does the job itself.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    _ORIGIN = 'built-in'
    __dict__ = None # (!) real value is "mappingproxy({'__module__': '_frozen_importlib', '__doc__': 'Meta path import for built-in modules.\\n\\n    All methods are either class or static methods to avoid the need to\\n    instantiate the class.\\n\\n    ', '_ORIGIN': 'built-in', 'module_repr': <staticmethod(<function BuiltinImporter.module_repr at 0x0000020CD3D228E0>)>, 'find_spec': <classmethod(<function BuiltinImporter.find_spec at 0x0000020CD3D22980>)>, 'find_module': <classmethod(<function BuiltinImporter.find_module at 0x0000020CD3D22A20>)>, 'create_module': <staticmethod(<function BuiltinImporter.create_module at 0x0000020CD3D22AC0>)>, 'exec_module': <staticmethod(<function BuiltinImporter.exec_module at 0x0000020CD3D22B60>)>, 'get_code': <classmethod(<function BuiltinImporter.get_code at 0x0000020CD3D22CA0>)>, 'get_source': <classmethod(<function BuiltinImporter.get_source at 0x0000020CD3D22DE0>)>, 'is_package': <classmethod(<function BuiltinImporter.is_package at 0x0000020CD3D22F20>)>, 'load_module': <classmethod(<function _load_module_shim at 0x0000020CD3D21C60>)>, '__dict__': <attribute '__dict__' of 'BuiltinImporter' objects>, '__weakref__': <attribute '__weakref__' of 'BuiltinImporter' objects>})"


# variables with complex values

__spec__ = None # (!) real value is "ModuleSpec(name='_tracemalloc', loader=<class '_frozen_importlib.BuiltinImporter'>, origin='built-in')"

