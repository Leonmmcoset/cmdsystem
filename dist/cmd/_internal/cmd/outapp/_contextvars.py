# encoding: utf-8
# module _contextvars
# from (built-in)
# by generator 1.147
""" Context Variables """
# no imports

# functions

def copy_context(*args, **kwargs): # real signature unknown
    pass

# classes

class Context(object):
    # no doc
    def copy(self, *args, **kwargs): # real signature unknown
        """ Return a shallow copy of the context object. """
        pass

    def get(self, *args, **kwargs): # real signature unknown
        """
        Return the value for `key` if `key` has the value in the context object.
        
        If `key` does not exist, return `default`. If `default` is not given,
        return None.
        """
        pass

    def items(self, *args, **kwargs): # real signature unknown
        """
        Return all variables and their values in the context object.
        
        The result is returned as a list of 2-tuples (variable, value).
        """
        pass

    def keys(self, *args, **kwargs): # real signature unknown
        """ Return a list of all variables in the context object. """
        pass

    def run(self, *args, **kwargs): # real signature unknown
        pass

    def values(self, *args, **kwargs): # real signature unknown
        """ Return a list of all variables' values in the context object. """
        pass

    def __contains__(self, *args, **kwargs): # real signature unknown
        """ Return key in self. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Implement iter(self). """
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    __hash__ = None


class ContextVar(object):
    # no doc
    def get(self, *args, **kwargs): # real signature unknown
        """
        Return a value for the context variable for the current context.
        
        If there is no value for the variable in the current context, the method will:
         * return the value of the default argument of the method, if provided; or
         * return the default value for the context variable, if it was created
           with one; or
         * raise a LookupError.
        """
        pass

    def reset(self, *args, **kwargs): # real signature unknown
        """
        Reset the context variable.
        
        The variable is reset to the value it had before the `ContextVar.set()` that
        created the token was used.
        """
        pass

    def set(self): # real signature unknown; restored from __doc__
        """
        Call to set a new value for the context variable in the current context.
        
        The required value argument is the new value for the context variable.
        
        Returns a Token object that can be used to restore the variable to its previous
        value via the `ContextVar.reset()` method.
        """
        pass

    @classmethod
    def __class_getitem__(cls, *args, **kwargs): # real signature unknown
        """ See PEP 585 """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class Token(object):
    # no doc
    @classmethod
    def __class_getitem__(cls, *args, **kwargs): # real signature unknown
        """ See PEP 585 """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    old_value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    var = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    MISSING = None # (!) real value is '<Token.MISSING>'
    __hash__ = None


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
    __dict__ = None # (!) real value is "mappingproxy({'__module__': '_frozen_importlib', '__doc__': 'Meta path import for built-in modules.\\n\\n    All methods are either class or static methods to avoid the need to\\n    instantiate the class.\\n\\n    ', '_ORIGIN': 'built-in', 'module_repr': <staticmethod(<function BuiltinImporter.module_repr at 0x000001D27D6E28E0>)>, 'find_spec': <classmethod(<function BuiltinImporter.find_spec at 0x000001D27D6E2980>)>, 'find_module': <classmethod(<function BuiltinImporter.find_module at 0x000001D27D6E2A20>)>, 'create_module': <staticmethod(<function BuiltinImporter.create_module at 0x000001D27D6E2AC0>)>, 'exec_module': <staticmethod(<function BuiltinImporter.exec_module at 0x000001D27D6E2B60>)>, 'get_code': <classmethod(<function BuiltinImporter.get_code at 0x000001D27D6E2CA0>)>, 'get_source': <classmethod(<function BuiltinImporter.get_source at 0x000001D27D6E2DE0>)>, 'is_package': <classmethod(<function BuiltinImporter.is_package at 0x000001D27D6E2F20>)>, 'load_module': <classmethod(<function _load_module_shim at 0x000001D27D6E1C60>)>, '__dict__': <attribute '__dict__' of 'BuiltinImporter' objects>, '__weakref__': <attribute '__weakref__' of 'BuiltinImporter' objects>})"


# variables with complex values

__spec__ = None # (!) real value is "ModuleSpec(name='_contextvars', loader=<class '_frozen_importlib.BuiltinImporter'>, origin='built-in')"

