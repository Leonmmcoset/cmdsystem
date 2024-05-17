# encoding: utf-8
# module deploy_libs._ctypes
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\deploy_libs\_ctypes.pyd
# by generator 1.147
""" Create and manipulate C compatible data types in Python. """

# imports
from _ctypes import (Array, CFuncPtr, COMError, Structure, Union, _Pointer, 
    _SimpleCData)


# Variables with simple values

CTYPES_MAX_ARGCOUNT = 1024

FUNCFLAG_CDECL = 1
FUNCFLAG_HRESULT = 2
FUNCFLAG_PYTHONAPI = 4
FUNCFLAG_STDCALL = 0

FUNCFLAG_USE_ERRNO = 8
FUNCFLAG_USE_LASTERROR = 16

RTLD_GLOBAL = 0
RTLD_LOCAL = 0

_cast_addr = 140728452104400

_memmove_addr = 140728848683792

_memset_addr = 140728848685504

_string_at_addr = 140728452105144

_wstring_at_addr = 140728452105236

__version__ = '1.1.0'

# functions

def addressof(C_instance): # real signature unknown; restored from __doc__
    """
    addressof(C instance) -> integer
    Return the address of the C instance internal buffer
    """
    return 0

def alignment(C_type): # real signature unknown; restored from __doc__
    """
    alignment(C type) -> integer
    alignment(C instance) -> integer
    Return the alignment requirements of a C instance
    """
    return 0

def buffer_info(*args, **kwargs): # real signature unknown
    """ Return buffer interface information """
    pass

def byref(C_instance, offset=0): # real signature unknown; restored from __doc__
    """
    byref(C instance[, offset=0]) -> byref-object
    Return a pointer lookalike to a C instance, only usable
    as function argument
    """
    pass

def call_cdeclfunction(*args, **kwargs): # real signature unknown
    pass

def call_function(*args, **kwargs): # real signature unknown
    pass

def CopyComPointer(src, dst): # real signature unknown; restored from __doc__
    """ CopyComPointer(src, dst) -> HRESULT value """
    pass

def FormatError(integer=None): # real signature unknown; restored from __doc__
    """
    FormatError([integer]) -> string
    
    Convert a win32 error code into a string. If the error code is not
    given, the return value of a call to GetLastError() is used.
    """
    return ""

def FreeLibrary(handle): # real signature unknown; restored from __doc__
    """
    FreeLibrary(handle) -> void
    
    Free the handle of an executable previously loaded by LoadLibrary.
    """
    pass

def get_errno(*args, **kwargs): # real signature unknown
    pass

def get_last_error(*args, **kwargs): # real signature unknown
    pass

def LoadLibrary(name, load_flags): # real signature unknown; restored from __doc__
    """
    LoadLibrary(name, load_flags) -> handle
    
    Load an executable (usually a DLL), and return a handle to it.
    The handle may be used to locate exported functions in this
    module. load_flags are as defined for LoadLibraryEx in the
    Windows API.
    """
    pass

def POINTER(*args, **kwargs): # real signature unknown
    pass

def pointer(*args, **kwargs): # real signature unknown
    pass

def PyObj_FromPtr(*args, **kwargs): # real signature unknown
    pass

def Py_DECREF(*args, **kwargs): # real signature unknown
    pass

def Py_INCREF(*args, **kwargs): # real signature unknown
    pass

def resize(*args, **kwargs): # real signature unknown
    """ Resize the memory buffer of a ctypes instance """
    pass

def set_errno(*args, **kwargs): # real signature unknown
    pass

def set_last_error(*args, **kwargs): # real signature unknown
    pass

def sizeof(C_type): # real signature unknown; restored from __doc__
    """
    sizeof(C type) -> integer
    sizeof(C instance) -> integer
    Return the size in bytes of a C instance
    """
    return 0

def _check_HRESULT(*args, **kwargs): # real signature unknown
    pass

def _unpickle(*args, **kwargs): # real signature unknown
    pass

# classes

class ArgumentError(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



# variables with complex values

_pointer_type_cache = {}

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001F98EA8A250>'

__spec__ = None # (!) real value is "ModuleSpec(name='deploy_libs._ctypes', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001F98EA8A250>, origin='C:\\\\Users\\\\leonm\\\\PycharmProjects\\\\LeonRandomPlus\\\\venv\\\\Lib\\\\site-packages\\\\deploy_libs\\\\_ctypes.pyd')"

