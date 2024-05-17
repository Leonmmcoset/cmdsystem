# encoding: utf-8
# module binascii
# from (built-in)
# by generator 1.147
""" Conversion between binary data and ASCII """
# no imports

# functions

def a2b_base64(*args, **kwargs): # real signature unknown
    """
    Decode a line of base64 data.
    
      strict_mode
        When set to True, bytes that are not part of the base64 standard are not allowed.
        The same applies to excess data after padding (= / ==).
    """
    pass

def a2b_hex(*args, **kwargs): # real signature unknown
    """
    Binary data of hexadecimal representation.
    
    hexstr must contain an even number of hex digits (upper or lower case).
    This function is also available as "unhexlify()".
    """
    pass

def a2b_qp(*args, **kwargs): # real signature unknown
    """ Decode a string of qp-encoded data. """
    pass

def a2b_uu(*args, **kwargs): # real signature unknown
    """ Decode a line of uuencoded data. """
    pass

def b2a_base64(*args, **kwargs): # real signature unknown
    """ Base64-code line of data. """
    pass

def b2a_hex(b, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    Hexadecimal representation of binary data.
    
      sep
        An optional single character or byte to separate hex bytes.
      bytes_per_sep
        How many bytes between separators.  Positive values count from the
        right, negative values count from the left.
    
    The return value is a bytes object.  This function is also
    available as "hexlify()".
    
    Example:
    >>> binascii.b2a_hex(b'\xb9\x01\xef')
    b'b901ef'
    >>> binascii.hexlify(b'\xb9\x01\xef', ':')
    b'b9:01:ef'
    >>> binascii.b2a_hex(b'\xb9\x01\xef', b'_', 2)
    b'b9_01ef'
    """
    pass

def b2a_qp(*args, **kwargs): # real signature unknown
    """
    Encode a string using quoted-printable encoding.
    
    On encoding, when istext is set, newlines are not encoded, and white
    space at end of lines is.  When istext is not set, \r and \n (CR/LF)
    are both encoded.  When quotetabs is set, space and tabs are encoded.
    """
    pass

def b2a_uu(*args, **kwargs): # real signature unknown
    """ Uuencode line of data. """
    pass

def crc32(*args, **kwargs): # real signature unknown
    """ Compute CRC-32 incrementally. """
    pass

def crc_hqx(*args, **kwargs): # real signature unknown
    """ Compute CRC-CCITT incrementally. """
    pass

def hexlify(data): # known case of binascii.hexlify
    """
    Hexadecimal representation of binary data.
    
      sep
        An optional single character or byte to separate hex bytes.
      bytes_per_sep
        How many bytes between separators.  Positive values count from the
        right, negative values count from the left.
    
    The return value is a bytes object.  This function is also
    available as "b2a_hex()".
    """
    return b""

def unhexlify(hexstr): # known case of binascii.unhexlify
    """
    Binary data of hexadecimal representation.
    
    hexstr must contain an even number of hex digits (upper or lower case).
    """
    return b""

# classes

class Error(ValueError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class Incomplete(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



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
    __dict__ = None # (!) real value is "mappingproxy({'__module__': '_frozen_importlib', '__doc__': 'Meta path import for built-in modules.\\n\\n    All methods are either class or static methods to avoid the need to\\n    instantiate the class.\\n\\n    ', '_ORIGIN': 'built-in', 'module_repr': <staticmethod(<function BuiltinImporter.module_repr at 0x000002B079B528E0>)>, 'find_spec': <classmethod(<function BuiltinImporter.find_spec at 0x000002B079B52980>)>, 'find_module': <classmethod(<function BuiltinImporter.find_module at 0x000002B079B52A20>)>, 'create_module': <staticmethod(<function BuiltinImporter.create_module at 0x000002B079B52AC0>)>, 'exec_module': <staticmethod(<function BuiltinImporter.exec_module at 0x000002B079B52B60>)>, 'get_code': <classmethod(<function BuiltinImporter.get_code at 0x000002B079B52CA0>)>, 'get_source': <classmethod(<function BuiltinImporter.get_source at 0x000002B079B52DE0>)>, 'is_package': <classmethod(<function BuiltinImporter.is_package at 0x000002B079B52F20>)>, 'load_module': <classmethod(<function _load_module_shim at 0x000002B079B51C60>)>, '__dict__': <attribute '__dict__' of 'BuiltinImporter' objects>, '__weakref__': <attribute '__weakref__' of 'BuiltinImporter' objects>})"


# variables with complex values

__spec__ = None # (!) real value is "ModuleSpec(name='binascii', loader=<class '_frozen_importlib.BuiltinImporter'>, origin='built-in')"

