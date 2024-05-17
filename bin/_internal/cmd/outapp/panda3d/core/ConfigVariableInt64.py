# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .ConfigVariable import ConfigVariable

class ConfigVariableInt64(ConfigVariable):
    """
    /**
     * This is a convenience class to specialize ConfigVariable as a 64-bit
     * integer type.
     */
    """
    def assign(self, const_ConfigVariableInt64_self, long_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        assign(const ConfigVariableInt64 self, long value)
        """
        pass

    def getDefaultValue(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_default_value(ConfigVariableInt64 self)
        
        /**
         * Returns the variable's default value.
         */
        """
        pass

    def getValue(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_value(ConfigVariableInt64 self)
        
        /**
         * Returns the variable's value.
         */
        """
        pass

    def getWord(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_word(ConfigVariableInt64 self, int n)
        
        /**
         * Returns the variable's nth value.
         */
        """
        pass

    def get_default_value(self, ConfigVariableInt64_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_default_value(ConfigVariableInt64 self)
        
        /**
         * Returns the variable's default value.
         */
        """
        pass

    def get_value(self, ConfigVariableInt64_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_value(ConfigVariableInt64 self)
        
        /**
         * Returns the variable's value.
         */
        """
        pass

    def get_word(self, ConfigVariableInt64_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_word(ConfigVariableInt64 self, int n)
        
        /**
         * Returns the variable's nth value.
         */
        """
        pass

    def setValue(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_value(const ConfigVariableInt64 self, long value)
        
        /**
         * Reassigns the variable's local value.
         */
        """
        pass

    def setWord(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_word(const ConfigVariableInt64 self, int n, long value)
        
        /**
         * Reassigns the variable's nth value.  This makes a local copy of the
         * variable's overall value.
         */
        """
        pass

    def set_value(self, const_ConfigVariableInt64_self, long_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_value(const ConfigVariableInt64 self, long value)
        
        /**
         * Reassigns the variable's local value.
         */
        """
        pass

    def set_word(self, const_ConfigVariableInt64_self, int_n, long_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_word(const ConfigVariableInt64 self, int n, long value)
        
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

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __int__(self, *args, **kwargs): # real signature unknown
        """ int(self) """
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    default_value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.ConfigVariableInt64' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.ConfigVariableInt64' objects>"
        '__doc__': '/**\n * This is a convenience class to specialize ConfigVariable as a 64-bit\n * integer type.\n */',
        '__getitem__': None, # (!) real value is "<slot wrapper '__getitem__' of 'panda3d.core.ConfigVariableInt64' objects>"
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.ConfigVariableInt64' objects>"
        '__int__': None, # (!) real value is "<slot wrapper '__int__' of 'panda3d.core.ConfigVariableInt64' objects>"
        '__len__': None, # (!) real value is "<slot wrapper '__len__' of 'panda3d.core.ConfigVariableInt64' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE263840>'
        'assign': None, # (!) real value is "<method 'assign' of 'panda3d.core.ConfigVariableInt64' objects>"
        'default_value': None, # (!) real value is "<attribute 'default_value' of 'panda3d.core.ConfigVariableInt64' objects>"
        'getDefaultValue': None, # (!) real value is "<method 'getDefaultValue' of 'panda3d.core.ConfigVariableInt64' objects>"
        'getValue': None, # (!) real value is "<method 'getValue' of 'panda3d.core.ConfigVariableInt64' objects>"
        'getWord': None, # (!) real value is "<method 'getWord' of 'panda3d.core.ConfigVariableInt64' objects>"
        'get_default_value': None, # (!) real value is "<method 'get_default_value' of 'panda3d.core.ConfigVariableInt64' objects>"
        'get_value': None, # (!) real value is "<method 'get_value' of 'panda3d.core.ConfigVariableInt64' objects>"
        'get_word': None, # (!) real value is "<method 'get_word' of 'panda3d.core.ConfigVariableInt64' objects>"
        'setValue': None, # (!) real value is "<method 'setValue' of 'panda3d.core.ConfigVariableInt64' objects>"
        'setWord': None, # (!) real value is "<method 'setWord' of 'panda3d.core.ConfigVariableInt64' objects>"
        'set_value': None, # (!) real value is "<method 'set_value' of 'panda3d.core.ConfigVariableInt64' objects>"
        'set_word': None, # (!) real value is "<method 'set_word' of 'panda3d.core.ConfigVariableInt64' objects>"
        'value': None, # (!) real value is "<attribute 'value' of 'panda3d.core.ConfigVariableInt64' objects>"
    }


