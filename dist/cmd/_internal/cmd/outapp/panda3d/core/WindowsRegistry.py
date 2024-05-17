# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class WindowsRegistry(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * This class provides a hook to Python to read and write strings and integers
     * to the windows registry.  It automatically converts strings from utf-8
     * encoding and stores them in Unicode (and conversely reconverts them on
     * retrieval).
     */
    """
    def getIntValue(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_int_value(str key, str name, int default_value, int rl)
        
        /**
         * Returns the value associated with the indicated registry key, assuming it
         * is an integer value.  If the key is not defined or is not an integer type
         * value, default_value is returned instead.
         */
        """
        pass

    def getKeyType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_key_type(str key, str name, int rl)
        
        /**
         * Returns the type of the indicated key, or T_none if the key is not known or
         * is some unsupported type.
         */
        """
        pass

    def getStringValue(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_string_value(str key, str name, str default_value, int rl)
        
        /**
         * Returns the value associated with the indicated registry key, assuming it
         * is a string value.  The string value is automatically encoded using
         * TextEncoder::get_default_encoding().  If the key is not defined or is not a
         * string type value, default_value is returned instead.
         */
        """
        pass

    def get_int_value(self, str_key, str_name, int_default_value, int_rl): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_int_value(str key, str name, int default_value, int rl)
        
        /**
         * Returns the value associated with the indicated registry key, assuming it
         * is an integer value.  If the key is not defined or is not an integer type
         * value, default_value is returned instead.
         */
        """
        pass

    def get_key_type(self, str_key, str_name, int_rl): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_key_type(str key, str name, int rl)
        
        /**
         * Returns the type of the indicated key, or T_none if the key is not known or
         * is some unsupported type.
         */
        """
        pass

    def get_string_value(self, str_key, str_name, str_default_value, int_rl): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_string_value(str key, str name, str default_value, int rl)
        
        /**
         * Returns the value associated with the indicated registry key, assuming it
         * is a string value.  The string value is automatically encoded using
         * TextEncoder::get_default_encoding().  If the key is not defined or is not a
         * string type value, default_value is returned instead.
         */
        """
        pass

    def setIntValue(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_int_value(str key, str name, int value, int rl)
        
        /**
         * Sets the registry key to the indicated value as an integer.  The registry
         * key must already exist prior to calling this function.
         */
        """
        pass

    def setStringValue(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_string_value(str key, str name, str value, int rl)
        
        /**
         * Sets the registry key to the indicated value as a string.  The supplied
         * string value is automatically converted from whatever encoding is set by
         * TextEncoder::set_default_encoding() and written as a Unicode string.  The
         * registry key must already exist prior to calling this function.
         */
        """
        pass

    def set_int_value(self, str_key, str_name, int_value, int_rl): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_int_value(str key, str name, int value, int rl)
        
        /**
         * Sets the registry key to the indicated value as an integer.  The registry
         * key must already exist prior to calling this function.
         */
        """
        pass

    def set_string_value(self, str_key, str_name, str_value, int_rl): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_string_value(str key, str name, str value, int rl)
        
        /**
         * Sets the registry key to the indicated value as a string.  The supplied
         * string value is automatically converted from whatever encoding is set by
         * TextEncoder::set_default_encoding() and written as a Unicode string.  The
         * registry key must already exist prior to calling this function.
         */
        """
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __deepcopy__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        'RlMachine': 0,
        'RlUser': 1,
        'TInt': 1,
        'TNone': 0,
        'TString': 2,
        'T_int': 1,
        'T_none': 0,
        'T_string': 2,
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.WindowsRegistry' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.WindowsRegistry' objects>"
        '__doc__': '/**\n * This class provides a hook to Python to read and write strings and integers\n * to the windows registry.  It automatically converts strings from utf-8\n * encoding and stores them in Unicode (and conversely reconverts them on\n * retrieval).\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.WindowsRegistry' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE27B6F0>'
        'getIntValue': None, # (!) real value is '<staticmethod(<built-in method getIntValue of type object at 0x00007FFCFE27B6F0>)>'
        'getKeyType': None, # (!) real value is '<staticmethod(<built-in method getKeyType of type object at 0x00007FFCFE27B6F0>)>'
        'getStringValue': None, # (!) real value is '<staticmethod(<built-in method getStringValue of type object at 0x00007FFCFE27B6F0>)>'
        'get_int_value': None, # (!) real value is '<staticmethod(<built-in method get_int_value of type object at 0x00007FFCFE27B6F0>)>'
        'get_key_type': None, # (!) real value is '<staticmethod(<built-in method get_key_type of type object at 0x00007FFCFE27B6F0>)>'
        'get_string_value': None, # (!) real value is '<staticmethod(<built-in method get_string_value of type object at 0x00007FFCFE27B6F0>)>'
        'rl_machine': 0,
        'rl_user': 1,
        'setIntValue': None, # (!) real value is '<staticmethod(<built-in method setIntValue of type object at 0x00007FFCFE27B6F0>)>'
        'setStringValue': None, # (!) real value is '<staticmethod(<built-in method setStringValue of type object at 0x00007FFCFE27B6F0>)>'
        'set_int_value': None, # (!) real value is '<staticmethod(<built-in method set_int_value of type object at 0x00007FFCFE27B6F0>)>'
        'set_string_value': None, # (!) real value is '<staticmethod(<built-in method set_string_value of type object at 0x00007FFCFE27B6F0>)>'
    }
    RlMachine = 0
    RlUser = 1
    rl_machine = 0
    rl_user = 1
    TInt = 1
    TNone = 0
    TString = 2
    T_int = 1
    T_none = 0
    T_string = 2


