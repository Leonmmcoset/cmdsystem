# encoding: utf-8
# module _bisect
# from (built-in)
# by generator 1.147
"""
Bisection algorithms.

This module provides support for maintaining a list in sorted order without
having to sort the list after each insertion. For long lists of items with
expensive comparison operations, this can be an improvement over the more
common approach.
"""
# no imports

# functions

def bisect_left(*args, **kwargs): # real signature unknown
    """
    Return the index where to insert item x in list a, assuming a is sorted.
    
    The return value i is such that all e in a[:i] have e < x, and all e in
    a[i:] have e >= x.  So if x already appears in the list, a.insert(i, x) will
    insert just before the leftmost x already there.
    
    Optional args lo (default 0) and hi (default len(a)) bound the
    slice of a to be searched.
    """
    pass

def bisect_right(*args, **kwargs): # real signature unknown
    """
    Return the index where to insert item x in list a, assuming a is sorted.
    
    The return value i is such that all e in a[:i] have e <= x, and all e in
    a[i:] have e > x.  So if x already appears in the list, a.insert(i, x) will
    insert just after the rightmost x already there.
    
    Optional args lo (default 0) and hi (default len(a)) bound the
    slice of a to be searched.
    """
    pass

def insort_left(*args, **kwargs): # real signature unknown
    """
    Insert item x in list a, and keep it sorted assuming a is sorted.
    
    If x is already in a, insert it to the left of the leftmost x.
    
    Optional args lo (default 0) and hi (default len(a)) bound the
    slice of a to be searched.
    """
    pass

def insort_right(*args, **kwargs): # real signature unknown
    """
    Insert item x in list a, and keep it sorted assuming a is sorted.
    
    If x is already in a, insert it to the right of the rightmost x.
    
    Optional args lo (default 0) and hi (default len(a)) bound the
    slice of a to be searched.
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
    __dict__ = None # (!) real value is "mappingproxy({'__module__': '_frozen_importlib', '__doc__': 'Meta path import for built-in modules.\\n\\n    All methods are either class or static methods to avoid the need to\\n    instantiate the class.\\n\\n    ', '_ORIGIN': 'built-in', 'module_repr': <staticmethod(<function BuiltinImporter.module_repr at 0x0000025AB65E28E0>)>, 'find_spec': <classmethod(<function BuiltinImporter.find_spec at 0x0000025AB65E2980>)>, 'find_module': <classmethod(<function BuiltinImporter.find_module at 0x0000025AB65E2A20>)>, 'create_module': <staticmethod(<function BuiltinImporter.create_module at 0x0000025AB65E2AC0>)>, 'exec_module': <staticmethod(<function BuiltinImporter.exec_module at 0x0000025AB65E2B60>)>, 'get_code': <classmethod(<function BuiltinImporter.get_code at 0x0000025AB65E2CA0>)>, 'get_source': <classmethod(<function BuiltinImporter.get_source at 0x0000025AB65E2DE0>)>, 'is_package': <classmethod(<function BuiltinImporter.is_package at 0x0000025AB65E2F20>)>, 'load_module': <classmethod(<function _load_module_shim at 0x0000025AB65E1C60>)>, '__dict__': <attribute '__dict__' of 'BuiltinImporter' objects>, '__weakref__': <attribute '__weakref__' of 'BuiltinImporter' objects>})"


# variables with complex values

__spec__ = None # (!) real value is "ModuleSpec(name='_bisect', loader=<class '_frozen_importlib.BuiltinImporter'>, origin='built-in')"

