# encoding: utf-8
# module _imp
# from (built-in)
# by generator 1.147
""" (Extremely) low-level import machinery bits as used by importlib and imp. """
# no imports

# Variables with simple values

check_hash_based_pycs = 'default'

# functions

def acquire_lock(*args, **kwargs): # real signature unknown
    """
    Acquires the interpreter's import lock for the current thread.
    
    This lock should be used by import hooks to ensure thread-safety when importing
    modules. On platforms without threads, this function does nothing.
    """
    pass

def create_builtin(*args, **kwargs): # real signature unknown
    """ Create an extension module. """
    pass

def create_dynamic(*args, **kwargs): # real signature unknown
    """ Create an extension module. """
    pass

def exec_builtin(*args, **kwargs): # real signature unknown
    """ Initialize a built-in module. """
    pass

def exec_dynamic(*args, **kwargs): # real signature unknown
    """ Initialize an extension module. """
    pass

def extension_suffixes(*args, **kwargs): # real signature unknown
    """ Returns the list of file suffixes used to identify extension modules. """
    pass

def find_frozen(*args, **kwargs): # real signature unknown
    """
    Return info about the corresponding frozen module (if there is one) or None.
    
    The returned info (a 2-tuple):
    
     * data         the raw marshalled bytes
     * is_package   whether or not it is a package
     * origname     the originally frozen module's name, or None if not
                    a stdlib module (this will usually be the same as
                    the module's current name)
    """
    pass

def get_frozen_object(*args, **kwargs): # real signature unknown
    """ Create a code object for a frozen module. """
    pass

def init_frozen(*args, **kwargs): # real signature unknown
    """ Initializes a frozen module. """
    pass

def is_builtin(*args, **kwargs): # real signature unknown
    """ Returns True if the module name corresponds to a built-in module. """
    pass

def is_frozen(*args, **kwargs): # real signature unknown
    """ Returns True if the module name corresponds to a frozen module. """
    pass

def is_frozen_package(*args, **kwargs): # real signature unknown
    """ Returns True if the module name is of a frozen package. """
    pass

def lock_held(*args, **kwargs): # real signature unknown
    """
    Return True if the import lock is currently held, else False.
    
    On platforms without threads, return False.
    """
    pass

def release_lock(*args, **kwargs): # real signature unknown
    """
    Release the interpreter's import lock.
    
    On platforms without threads, this function does nothing.
    """
    pass

def source_hash(*args, **kwargs): # real signature unknown
    pass

def _fix_co_filename(*args, **kwargs): # real signature unknown
    """
    Changes code.co_filename to specify the passed-in file path.
    
      code
        Code object to change.
      path
        File path to use.
    """
    pass

def _frozen_module_names(*args, **kwargs): # real signature unknown
    """ Returns the list of available frozen modules. """
    pass

def _override_frozen_modules_for_tests(*args, **kwargs): # real signature unknown
    """
    (internal-only) Override PyConfig.use_frozen_modules.
    
    (-1: "off", 1: "on", 0: no override)
    See frozen_modules() in Lib/test/support/import_helper.py.
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
    __dict__ = None # (!) real value is "mappingproxy({'__module__': '_frozen_importlib', '__doc__': 'Meta path import for built-in modules.\\n\\n    All methods are either class or static methods to avoid the need to\\n    instantiate the class.\\n\\n    ', '_ORIGIN': 'built-in', 'module_repr': <staticmethod(<function BuiltinImporter.module_repr at 0x00000214B67228E0>)>, 'find_spec': <classmethod(<function BuiltinImporter.find_spec at 0x00000214B6722980>)>, 'find_module': <classmethod(<function BuiltinImporter.find_module at 0x00000214B6722A20>)>, 'create_module': <staticmethod(<function BuiltinImporter.create_module at 0x00000214B6722AC0>)>, 'exec_module': <staticmethod(<function BuiltinImporter.exec_module at 0x00000214B6722B60>)>, 'get_code': <classmethod(<function BuiltinImporter.get_code at 0x00000214B6722CA0>)>, 'get_source': <classmethod(<function BuiltinImporter.get_source at 0x00000214B6722DE0>)>, 'is_package': <classmethod(<function BuiltinImporter.is_package at 0x00000214B6722F20>)>, 'load_module': <classmethod(<function _load_module_shim at 0x00000214B6721C60>)>, '__dict__': <attribute '__dict__' of 'BuiltinImporter' objects>, '__weakref__': <attribute '__weakref__' of 'BuiltinImporter' objects>})"


# variables with complex values

__spec__ = None # (!) real value is "ModuleSpec(name='_imp', loader=<class '_frozen_importlib.BuiltinImporter'>, origin='built-in')"

