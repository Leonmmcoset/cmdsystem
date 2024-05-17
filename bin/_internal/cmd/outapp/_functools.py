# encoding: utf-8
# module _functools
# from (built-in)
# by generator 1.147
""" Tools that operate on functions. """
# no imports

# functions

def cmp_to_key(*args, **kwargs): # real signature unknown
    """ Convert a cmp= function into a key= function. """
    pass

def reduce(function, iterable, initial=None): # real signature unknown; restored from __doc__
    """
    reduce(function, iterable[, initial]) -> value
    
    Apply a function of two arguments cumulatively to the items of a sequence
    or iterable, from left to right, so as to reduce the iterable to a single
    value.  For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates
    ((((1+2)+3)+4)+5).  If initial is present, it is placed before the items
    of the iterable in the calculation, and serves as a default when the
    iterable is empty.
    """
    pass

# classes

class partial(object):
    """
    partial(func, *args, **keywords) - new function with partial application
        of the given arguments and keywords.
    """
    def __call__(self, *args, **kwargs): # real signature unknown
        """ Call self as a function. """
        pass

    @classmethod
    def __class_getitem__(cls, *args, **kwargs): # real signature unknown
        """ See PEP 585 """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __init__(self, func, *args, **keywords): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    args = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """tuple of arguments to future partial calls"""

    func = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """function object to use in future partial calls"""

    keywords = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """dictionary of keyword arguments to future partial calls"""

    __vectorcalloffset__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is "mappingproxy({'__new__': <built-in method __new__ of type object at 0x000002B6E2AFCA20>, '__repr__': <slot wrapper '__repr__' of 'functools.partial' objects>, '__call__': <slot wrapper '__call__' of 'functools.partial' objects>, '__getattribute__': <slot wrapper '__getattribute__' of 'functools.partial' objects>, '__setattr__': <slot wrapper '__setattr__' of 'functools.partial' objects>, '__delattr__': <slot wrapper '__delattr__' of 'functools.partial' objects>, '__reduce__': <method '__reduce__' of 'functools.partial' objects>, '__setstate__': <method '__setstate__' of 'functools.partial' objects>, '__class_getitem__': <method '__class_getitem__' of 'functools.partial' objects>, 'func': <member 'func' of 'functools.partial' objects>, 'args': <member 'args' of 'functools.partial' objects>, 'keywords': <member 'keywords' of 'functools.partial' objects>, '__vectorcalloffset__': <member '__vectorcalloffset__' of 'functools.partial' objects>, '__dict__': <attribute '__dict__' of 'functools.partial' objects>, '__doc__': 'partial(func, *args, **keywords) - new function with partial application\\n    of the given arguments and keywords.\\n', '__module__': 'functools'})"


class _lru_cache_wrapper(object):
    """
    Create a cached callable that wraps another function.
    
    user_function:      the function being cached
    
    maxsize:  0         for no caching
              None      for unlimited cache size
              n         for a bounded cache
    
    typed:    False     cache f(3) and f(3.0) as identical calls
              True      cache f(3) and f(3.0) as distinct calls
    
    cache_info_type:    namedtuple class with the fields:
                            hits misses currsize maxsize
    """
    def cache_clear(self, *args, **kwargs): # real signature unknown
        pass

    def cache_info(self, *args, **kwargs): # real signature unknown
        pass

    def __call__(self, *args, **kwargs): # real signature unknown
        """ Call self as a function. """
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __deepcopy__(self, *args, **kwargs): # real signature unknown
        pass

    def __get__(self, *args, **kwargs): # real signature unknown
        """ Return an attribute of instance, which is of type owner. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    __dict__ = None # (!) real value is "mappingproxy({'__new__': <built-in method __new__ of type object at 0x000002B6E2AF9C50>, '__call__': <slot wrapper '__call__' of 'functools._lru_cache_wrapper' objects>, '__get__': <slot wrapper '__get__' of 'functools._lru_cache_wrapper' objects>, 'cache_info': <method 'cache_info' of 'functools._lru_cache_wrapper' objects>, 'cache_clear': <method 'cache_clear' of 'functools._lru_cache_wrapper' objects>, '__reduce__': <method '__reduce__' of 'functools._lru_cache_wrapper' objects>, '__copy__': <method '__copy__' of 'functools._lru_cache_wrapper' objects>, '__deepcopy__': <method '__deepcopy__' of 'functools._lru_cache_wrapper' objects>, '__dict__': <attribute '__dict__' of 'functools._lru_cache_wrapper' objects>, '__doc__': 'Create a cached callable that wraps another function.\\n\\nuser_function:      the function being cached\\n\\nmaxsize:  0         for no caching\\n          None      for unlimited cache size\\n          n         for a bounded cache\\n\\ntyped:    False     cache f(3) and f(3.0) as identical calls\\n          True      cache f(3) and f(3.0) as distinct calls\\n\\ncache_info_type:    namedtuple class with the fields:\\n                        hits misses currsize maxsize\\n', '__module__': 'functools'})"


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
    __dict__ = None # (!) real value is "mappingproxy({'__module__': '_frozen_importlib', '__doc__': 'Meta path import for built-in modules.\\n\\n    All methods are either class or static methods to avoid the need to\\n    instantiate the class.\\n\\n    ', '_ORIGIN': 'built-in', 'module_repr': <staticmethod(<function BuiltinImporter.module_repr at 0x000002B6E26728E0>)>, 'find_spec': <classmethod(<function BuiltinImporter.find_spec at 0x000002B6E2672980>)>, 'find_module': <classmethod(<function BuiltinImporter.find_module at 0x000002B6E2672A20>)>, 'create_module': <staticmethod(<function BuiltinImporter.create_module at 0x000002B6E2672AC0>)>, 'exec_module': <staticmethod(<function BuiltinImporter.exec_module at 0x000002B6E2672B60>)>, 'get_code': <classmethod(<function BuiltinImporter.get_code at 0x000002B6E2672CA0>)>, 'get_source': <classmethod(<function BuiltinImporter.get_source at 0x000002B6E2672DE0>)>, 'is_package': <classmethod(<function BuiltinImporter.is_package at 0x000002B6E2672F20>)>, 'load_module': <classmethod(<function _load_module_shim at 0x000002B6E2671C60>)>, '__dict__': <attribute '__dict__' of 'BuiltinImporter' objects>, '__weakref__': <attribute '__weakref__' of 'BuiltinImporter' objects>})"


# variables with complex values

__spec__ = None # (!) real value is "ModuleSpec(name='_functools', loader=<class '_frozen_importlib.BuiltinImporter'>, origin='built-in')"

