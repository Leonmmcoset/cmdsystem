# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .ConfigVariableBase import ConfigVariableBase

class ConfigVariable(ConfigVariableBase):
    """
    /**
     * This is a generic, untyped ConfigVariable.  It is also the base class for
     * the typed ConfigVariables, and contains all of the code common to
     * ConfigVariables of all types (except ConfigVariableList, which is a bit of
     * a special case).
     *
     * Mostly, this class serves as a thin wrapper around ConfigVariableCore
     * and/or ConfigDeclaration, more or less duplicating the interface presented
     * there.
     */
    """
    def clearValue(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_value(const ConfigVariable self)
        
        /**
         * Removes the value assigned to this variable, and lets its original value
         * (as read from the prc files) show through.
         */
        """
        pass

    def clear_value(self, const_ConfigVariable_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_value(const ConfigVariable self)
        
        /**
         * Removes the value assigned to this variable, and lets its original value
         * (as read from the prc files) show through.
         */
        """
        pass

    def getNumWords(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_words(ConfigVariable self)
        
        /**
         * Returns the number of words in the variable's value.  A word is defined as
         * a sequence of non-whitespace characters delimited by whitespace.
         */
        """
        pass

    def getStringValue(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_string_value(ConfigVariable self)
        
        /**
         * Returns the toplevel value of the variable, formatted as a string.
         */
        """
        pass

    def get_num_words(self, ConfigVariable_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_words(ConfigVariable self)
        
        /**
         * Returns the number of words in the variable's value.  A word is defined as
         * a sequence of non-whitespace characters delimited by whitespace.
         */
        """
        pass

    def get_string_value(self, ConfigVariable_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_string_value(ConfigVariable self)
        
        /**
         * Returns the toplevel value of the variable, formatted as a string.
         */
        """
        pass

    def setStringValue(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_string_value(const ConfigVariable self, str value)
        
        /**
         * Changes the value assigned to this variable.  This creates a local value
         * that shadows any values defined in the .prc files, until
         * clear_local_value() is called.
         */
        """
        pass

    def set_string_value(self, const_ConfigVariable_self, str_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_string_value(const ConfigVariable self, str value)
        
        /**
         * Changes the value assigned to this variable.  This creates a local value
         * that shadows any values defined in the .prc files, until
         * clear_local_value() is called.
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
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.ConfigVariable' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.ConfigVariable' objects>"
        '__doc__': '/**\n * This is a generic, untyped ConfigVariable.  It is also the base class for\n * the typed ConfigVariables, and contains all of the code common to\n * ConfigVariables of all types (except ConfigVariableList, which is a bit of\n * a special case).\n *\n * Mostly, this class serves as a thin wrapper around ConfigVariableCore\n * and/or ConfigDeclaration, more or less duplicating the interface presented\n * there.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.ConfigVariable' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE262F30>'
        'clearValue': None, # (!) real value is "<method 'clearValue' of 'panda3d.core.ConfigVariable' objects>"
        'clear_value': None, # (!) real value is "<method 'clear_value' of 'panda3d.core.ConfigVariable' objects>"
        'getNumWords': None, # (!) real value is "<method 'getNumWords' of 'panda3d.core.ConfigVariable' objects>"
        'getStringValue': None, # (!) real value is "<method 'getStringValue' of 'panda3d.core.ConfigVariable' objects>"
        'get_num_words': None, # (!) real value is "<method 'get_num_words' of 'panda3d.core.ConfigVariable' objects>"
        'get_string_value': None, # (!) real value is "<method 'get_string_value' of 'panda3d.core.ConfigVariable' objects>"
        'setStringValue': None, # (!) real value is "<method 'setStringValue' of 'panda3d.core.ConfigVariable' objects>"
        'set_string_value': None, # (!) real value is "<method 'set_string_value' of 'panda3d.core.ConfigVariable' objects>"
    }


