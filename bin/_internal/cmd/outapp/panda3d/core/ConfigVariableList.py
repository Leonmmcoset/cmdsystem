# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .ConfigVariableBase import ConfigVariableBase

class ConfigVariableList(ConfigVariableBase):
    """
    /**
     * This class is similar to ConfigVariable, but it reports its value as a list
     * of strings.  In this special case, all of the declarations of the variable
     * are returned as the elements of this list, in order.
     *
     * Note that this is different from a normal ConfigVariableString, which just
     * returns its topmost value, which can optionally be treated as a number of
     * discrete words by dividing it at the spaces.
     *
     * A ConfigVariableList cannot be modified locally.
     */
    """
    def getNumUniqueValues(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_unique_values(ConfigVariableList self)
        
        /**
         * Returns the number of unique values in the variable.
         */
        """
        pass

    def getNumValues(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_values(ConfigVariableList self)
        
        /**
         * Returns the number of values in the variable.
         */
        """
        pass

    def getStringValue(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_string_value(ConfigVariableList self, int n)
        
        /**
         * Returns the nth value of the variable.
         */
        """
        pass

    def getUniqueValue(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_unique_value(ConfigVariableList self, int n)
        
        /**
         * Returns the nth unique value of the variable.
         */
        """
        pass

    def get_num_unique_values(self, ConfigVariableList_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_unique_values(ConfigVariableList self)
        
        /**
         * Returns the number of unique values in the variable.
         */
        """
        pass

    def get_num_values(self, ConfigVariableList_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_values(ConfigVariableList self)
        
        /**
         * Returns the number of values in the variable.
         */
        """
        pass

    def get_string_value(self, ConfigVariableList_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_string_value(ConfigVariableList self, int n)
        
        /**
         * Returns the nth value of the variable.
         */
        """
        pass

    def get_unique_value(self, ConfigVariableList_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_unique_value(ConfigVariableList self, int n)
        
        /**
         * Returns the nth unique value of the variable.
         */
        """
        pass

    def output(self, ConfigVariableList_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(ConfigVariableList self, ostream out)
        
        /**
         *
         */
        """
        pass

    def write(self, ConfigVariableList_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(ConfigVariableList self, ostream out)
        
        /**
         *
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

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.ConfigVariableList' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.ConfigVariableList' objects>"
        '__doc__': '/**\n * This class is similar to ConfigVariable, but it reports its value as a list\n * of strings.  In this special case, all of the declarations of the variable\n * are returned as the elements of this list, in order.\n *\n * Note that this is different from a normal ConfigVariableString, which just\n * returns its topmost value, which can optionally be treated as a number of\n * discrete words by dividing it at the spaces.\n *\n * A ConfigVariableList cannot be modified locally.\n */',
        '__getitem__': None, # (!) real value is "<slot wrapper '__getitem__' of 'panda3d.core.ConfigVariableList' objects>"
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.ConfigVariableList' objects>"
        '__len__': None, # (!) real value is "<slot wrapper '__len__' of 'panda3d.core.ConfigVariableList' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE263A10>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.ConfigVariableList' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.ConfigVariableList' objects>"
        'getNumUniqueValues': None, # (!) real value is "<method 'getNumUniqueValues' of 'panda3d.core.ConfigVariableList' objects>"
        'getNumValues': None, # (!) real value is "<method 'getNumValues' of 'panda3d.core.ConfigVariableList' objects>"
        'getStringValue': None, # (!) real value is "<method 'getStringValue' of 'panda3d.core.ConfigVariableList' objects>"
        'getUniqueValue': None, # (!) real value is "<method 'getUniqueValue' of 'panda3d.core.ConfigVariableList' objects>"
        'get_num_unique_values': None, # (!) real value is "<method 'get_num_unique_values' of 'panda3d.core.ConfigVariableList' objects>"
        'get_num_values': None, # (!) real value is "<method 'get_num_values' of 'panda3d.core.ConfigVariableList' objects>"
        'get_string_value': None, # (!) real value is "<method 'get_string_value' of 'panda3d.core.ConfigVariableList' objects>"
        'get_unique_value': None, # (!) real value is "<method 'get_unique_value' of 'panda3d.core.ConfigVariableList' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.ConfigVariableList' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.core.ConfigVariableList' objects>"
    }


