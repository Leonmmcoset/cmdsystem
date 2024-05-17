# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .ConfigVariable import ConfigVariable

class ConfigVariableColor(ConfigVariable):
    """
    /**
     * This is a convenience class to specialize ConfigVariable as a set of
     * floating-point types representing a color value.
     *
     * It interprets the color differently depending on how many words were
     * specified: if only one, it is interpreted as a shade of gray with alpha 1.
     * If two values were specified, a grayscale and alpha pair.  If three, a set
     * of R, G, B values with alpha 1, and if four, a complete RGBA color.
     *
     * This isn't defined in dtool because it relies on the LColor class, which is
     * defined in linmath.
     */
    """
    def assign(self, const_ConfigVariableColor_self, const_LVecBase4f_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        assign(const ConfigVariableColor self, const LVecBase4f value)
        """
        pass

    def getDefaultValue(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_default_value(ConfigVariableColor self)
        
        /**
         * Returns the variable's default value.
         */
        """
        pass

    def getValue(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_value(ConfigVariableColor self)
        
        /**
         * Returns the variable's value.
         */
        """
        pass

    def get_default_value(self, ConfigVariableColor_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_default_value(ConfigVariableColor self)
        
        /**
         * Returns the variable's default value.
         */
        """
        pass

    def get_value(self, ConfigVariableColor_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_value(ConfigVariableColor self)
        
        /**
         * Returns the variable's value.
         */
        """
        pass

    def operatorTypecast(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        operator_typecast(ConfigVariableColor self)
        """
        pass

    def operator_typecast(self, ConfigVariableColor_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        operator_typecast(ConfigVariableColor self)
        """
        pass

    def setValue(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_value(const ConfigVariableColor self, const LVecBase4f value)
        
        /**
         * Reassigns the variable's local value.
         */
        """
        pass

    def set_value(self, const_ConfigVariableColor_self, const_LVecBase4f_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_value(const ConfigVariableColor self, const LVecBase4f value)
        
        /**
         * Reassigns the variable's local value.
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

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.ConfigVariableColor' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.ConfigVariableColor' objects>"
        '__doc__': "/**\n * This is a convenience class to specialize ConfigVariable as a set of\n * floating-point types representing a color value.\n *\n * It interprets the color differently depending on how many words were\n * specified: if only one, it is interpreted as a shade of gray with alpha 1.\n * If two values were specified, a grayscale and alpha pair.  If three, a set\n * of R, G, B values with alpha 1, and if four, a complete RGBA color.\n *\n * This isn't defined in dtool because it relies on the LColor class, which is\n * defined in linmath.\n */",
        '__getitem__': None, # (!) real value is "<slot wrapper '__getitem__' of 'panda3d.core.ConfigVariableColor' objects>"
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.ConfigVariableColor' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE326170>'
        'assign': None, # (!) real value is "<method 'assign' of 'panda3d.core.ConfigVariableColor' objects>"
        'getDefaultValue': None, # (!) real value is "<method 'getDefaultValue' of 'panda3d.core.ConfigVariableColor' objects>"
        'getValue': None, # (!) real value is "<method 'getValue' of 'panda3d.core.ConfigVariableColor' objects>"
        'get_default_value': None, # (!) real value is "<method 'get_default_value' of 'panda3d.core.ConfigVariableColor' objects>"
        'get_value': None, # (!) real value is "<method 'get_value' of 'panda3d.core.ConfigVariableColor' objects>"
        'operatorTypecast': None, # (!) real value is "<method 'operatorTypecast' of 'panda3d.core.ConfigVariableColor' objects>"
        'operator_typecast': None, # (!) real value is "<method 'operator_typecast' of 'panda3d.core.ConfigVariableColor' objects>"
        'setValue': None, # (!) real value is "<method 'setValue' of 'panda3d.core.ConfigVariableColor' objects>"
        'set_value': None, # (!) real value is "<method 'set_value' of 'panda3d.core.ConfigVariableColor' objects>"
    }


