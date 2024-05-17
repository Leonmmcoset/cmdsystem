# encoding: utf-8
# module _blake2
# from (built-in)
# by generator 1.147
""" _blake2b provides BLAKE2b for hashlib """
# no imports

# Variables with simple values

BLAKE2B_MAX_DIGEST_SIZE = 64

BLAKE2B_MAX_KEY_SIZE = 64

BLAKE2B_PERSON_SIZE = 16

BLAKE2B_SALT_SIZE = 16

BLAKE2S_MAX_DIGEST_SIZE = 32

BLAKE2S_MAX_KEY_SIZE = 32

BLAKE2S_PERSON_SIZE = 8

BLAKE2S_SALT_SIZE = 8

# no functions
# classes

class blake2b(object):
    """ Return a new BLAKE2b hash object. """
    def copy(self, *args, **kwargs): # real signature unknown
        """ Return a copy of the hash object. """
        pass

    def digest(self, *args, **kwargs): # real signature unknown
        """ Return the digest value as a bytes object. """
        pass

    def hexdigest(self, *args, **kwargs): # real signature unknown
        """ Return the digest value as a string of hexadecimal digits. """
        pass

    def update(self, *args, **kwargs): # real signature unknown
        """ Update this hash object's state with the provided bytes-like object. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    block_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    digest_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    MAX_DIGEST_SIZE = 64
    MAX_KEY_SIZE = 64
    PERSON_SIZE = 16
    SALT_SIZE = 16


class blake2s(object):
    """ Return a new BLAKE2s hash object. """
    def copy(self, *args, **kwargs): # real signature unknown
        """ Return a copy of the hash object. """
        pass

    def digest(self, *args, **kwargs): # real signature unknown
        """ Return the digest value as a bytes object. """
        pass

    def hexdigest(self, *args, **kwargs): # real signature unknown
        """ Return the digest value as a string of hexadecimal digits. """
        pass

    def update(self, *args, **kwargs): # real signature unknown
        """ Update this hash object's state with the provided bytes-like object. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    block_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    digest_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    MAX_DIGEST_SIZE = 32
    MAX_KEY_SIZE = 32
    PERSON_SIZE = 8
    SALT_SIZE = 8


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
    __dict__ = None # (!) real value is "mappingproxy({'__module__': '_frozen_importlib', '__doc__': 'Meta path import for built-in modules.\\n\\n    All methods are either class or static methods to avoid the need to\\n    instantiate the class.\\n\\n    ', '_ORIGIN': 'built-in', 'module_repr': <staticmethod(<function BuiltinImporter.module_repr at 0x0000023E045428E0>)>, 'find_spec': <classmethod(<function BuiltinImporter.find_spec at 0x0000023E04542980>)>, 'find_module': <classmethod(<function BuiltinImporter.find_module at 0x0000023E04542A20>)>, 'create_module': <staticmethod(<function BuiltinImporter.create_module at 0x0000023E04542AC0>)>, 'exec_module': <staticmethod(<function BuiltinImporter.exec_module at 0x0000023E04542B60>)>, 'get_code': <classmethod(<function BuiltinImporter.get_code at 0x0000023E04542CA0>)>, 'get_source': <classmethod(<function BuiltinImporter.get_source at 0x0000023E04542DE0>)>, 'is_package': <classmethod(<function BuiltinImporter.is_package at 0x0000023E04542F20>)>, 'load_module': <classmethod(<function _load_module_shim at 0x0000023E04541C60>)>, '__dict__': <attribute '__dict__' of 'BuiltinImporter' objects>, '__weakref__': <attribute '__weakref__' of 'BuiltinImporter' objects>})"


# variables with complex values

__spec__ = None # (!) real value is "ModuleSpec(name='_blake2', loader=<class '_frozen_importlib.BuiltinImporter'>, origin='built-in')"

