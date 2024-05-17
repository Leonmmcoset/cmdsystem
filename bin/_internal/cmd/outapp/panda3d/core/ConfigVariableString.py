# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .ConfigVariable import ConfigVariable

class ConfigVariableString(ConfigVariable):
    """
    /**
     * This is a convenience class to specialize ConfigVariable as a string type.
     */
    """
    def assign(self, const_ConfigVariableString_self, str_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        assign(const ConfigVariableString self, str value)
        """
        pass

    def cStr(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        c_str(ConfigVariableString self)
        
        // These methods help the ConfigVariableString act like a C++ string object.
        
        /**
         *
         */
        """
        pass

    def c_str(self, ConfigVariableString_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        c_str(ConfigVariableString self)
        
        // These methods help the ConfigVariableString act like a C++ string object.
        
        /**
         *
         */
        """
        pass

    def empty(self, ConfigVariableString_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        empty(ConfigVariableString self)
        
        /**
         *
         */
        """
        pass

    def getDefaultValue(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_default_value(ConfigVariableString self)
        
        /**
         * Returns the variable's default value.
         */
        """
        pass

    def getValue(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_value(ConfigVariableString self)
        
        /**
         * Returns the variable's value.
         */
        """
        pass

    def getWord(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_word(ConfigVariableString self, int n)
        
        /**
         * Returns the variable's nth value.
         */
        """
        pass

    def get_default_value(self, ConfigVariableString_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_default_value(ConfigVariableString self)
        
        /**
         * Returns the variable's default value.
         */
        """
        pass

    def get_value(self, ConfigVariableString_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_value(ConfigVariableString self)
        
        /**
         * Returns the variable's value.
         */
        """
        pass

    def get_word(self, ConfigVariableString_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_word(ConfigVariableString self, int n)
        
        /**
         * Returns the variable's nth value.
         */
        """
        pass

    def length(self, ConfigVariableString_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        length(ConfigVariableString self)
        
        /**
         *
         */
        """
        pass

    def setValue(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_value(const ConfigVariableString self, str value)
        
        /**
         * Reassigns the variable's local value.
         */
        """
        pass

    def setWord(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_word(const ConfigVariableString self, int n, str value)
        
        /**
         * Reassigns the variable's nth value.  This makes a local copy of the
         * variable's overall value.
         */
        """
        pass

    def set_value(self, const_ConfigVariableString_self, str_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_value(const ConfigVariableString self, str value)
        
        /**
         * Reassigns the variable's local value.
         */
        """
        pass

    def set_word(self, const_ConfigVariableString_self, int_n, str_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_word(const ConfigVariableString self, int n, str value)
        
        /**
         * Reassigns the variable's nth value.  This makes a local copy of the
         * variable's overall value.
         */
        """
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __deepcopy__(self, *args, **kwargs): # real signature unknown
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
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

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
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

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    default_value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.ConfigVariableString' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.ConfigVariableString' objects>"
        '__doc__': '/**\n * This is a convenience class to specialize ConfigVariable as a string type.\n */',
        '__eq__': None, # (!) real value is "<slot wrapper '__eq__' of 'panda3d.core.ConfigVariableString' objects>"
        '__ge__': None, # (!) real value is "<slot wrapper '__ge__' of 'panda3d.core.ConfigVariableString' objects>"
        '__getitem__': None, # (!) real value is "<slot wrapper '__getitem__' of 'panda3d.core.ConfigVariableString' objects>"
        '__gt__': None, # (!) real value is "<slot wrapper '__gt__' of 'panda3d.core.ConfigVariableString' objects>"
        '__hash__': None, # (!) real value is "<slot wrapper '__hash__' of 'panda3d.core.ConfigVariableString' objects>"
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.ConfigVariableString' objects>"
        '__le__': None, # (!) real value is "<slot wrapper '__le__' of 'panda3d.core.ConfigVariableString' objects>"
        '__lt__': None, # (!) real value is "<slot wrapper '__lt__' of 'panda3d.core.ConfigVariableString' objects>"
        '__ne__': None, # (!) real value is "<slot wrapper '__ne__' of 'panda3d.core.ConfigVariableString' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE263DB0>'
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.ConfigVariableString' objects>"
        'assign': None, # (!) real value is "<method 'assign' of 'panda3d.core.ConfigVariableString' objects>"
        'cStr': None, # (!) real value is "<method 'cStr' of 'panda3d.core.ConfigVariableString' objects>"
        'c_str': None, # (!) real value is "<method 'c_str' of 'panda3d.core.ConfigVariableString' objects>"
        'default_value': None, # (!) real value is "<attribute 'default_value' of 'panda3d.core.ConfigVariableString' objects>"
        'empty': None, # (!) real value is "<method 'empty' of 'panda3d.core.ConfigVariableString' objects>"
        'getDefaultValue': None, # (!) real value is "<method 'getDefaultValue' of 'panda3d.core.ConfigVariableString' objects>"
        'getValue': None, # (!) real value is "<method 'getValue' of 'panda3d.core.ConfigVariableString' objects>"
        'getWord': None, # (!) real value is "<method 'getWord' of 'panda3d.core.ConfigVariableString' objects>"
        'get_default_value': None, # (!) real value is "<method 'get_default_value' of 'panda3d.core.ConfigVariableString' objects>"
        'get_value': None, # (!) real value is "<method 'get_value' of 'panda3d.core.ConfigVariableString' objects>"
        'get_word': None, # (!) real value is "<method 'get_word' of 'panda3d.core.ConfigVariableString' objects>"
        'length': None, # (!) real value is "<method 'length' of 'panda3d.core.ConfigVariableString' objects>"
        'setValue': None, # (!) real value is "<method 'setValue' of 'panda3d.core.ConfigVariableString' objects>"
        'setWord': None, # (!) real value is "<method 'setWord' of 'panda3d.core.ConfigVariableString' objects>"
        'set_value': None, # (!) real value is "<method 'set_value' of 'panda3d.core.ConfigVariableString' objects>"
        'set_word': None, # (!) real value is "<method 'set_word' of 'panda3d.core.ConfigVariableString' objects>"
        'value': None, # (!) real value is "<attribute 'value' of 'panda3d.core.ConfigVariableString' objects>"
    }


