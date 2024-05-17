# encoding: utf-8
# module panda3d.direct
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\direct.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import panda3d.core as __panda3d_core


from .CInterval import CInterval

class CLerpInterval(CInterval):
    """
    /**
     * The base class for a family of intervals that linearly interpolate one or
     * more numeric values over time.
     */
    """
    def getBlendType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_blend_type(CLerpInterval self)
        
        /**
         * Returns the blend type specified for the interval.  This controls how the
         * linear interpolation behaves near the beginning and end of the lerp period.
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_blend_type(self, CLerpInterval_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_blend_type(CLerpInterval self)
        
        /**
         * Returns the blend type specified for the interval.  This controls how the
         * linear interpolation behaves near the beginning and end of the lerp period.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def stringBlendType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        string_blend_type(str blend_type)
        
        /**
         * Returns the BlendType enumerated value corresponding to the indicated
         * string, or BT_invalid if the string doesn't match anything.
         */
        """
        pass

    def string_blend_type(self, str_blend_type): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        string_blend_type(str blend_type)
        
        /**
         * Returns the BlendType enumerated value corresponding to the indicated
         * string, or BT_invalid if the string doesn't match anything.
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

    BTEaseIn = 1
    BTEaseInOut = 3
    BTEaseOut = 2
    BTInvalid = 4
    BTNoBlend = 0
    BT_ease_in = 1
    BT_ease_in_out = 3
    BT_ease_out = 2
    BT_invalid = 4
    BT_no_blend = 0
    DtoolClassDict = {
        'BTEaseIn': 1,
        'BTEaseInOut': 3,
        'BTEaseOut': 2,
        'BTInvalid': 4,
        'BTNoBlend': 0,
        'BT_ease_in': 1,
        'BT_ease_in_out': 3,
        'BT_ease_out': 2,
        'BT_invalid': 4,
        'BT_no_blend': 0,
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.direct.CLerpInterval' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.direct.CLerpInterval' objects>"
        '__doc__': '/**\n * The base class for a family of intervals that linearly interpolate one or\n * more numeric values over time.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.direct.CLerpInterval' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDC68E6020>'
        'getBlendType': None, # (!) real value is "<method 'getBlendType' of 'panda3d.direct.CLerpInterval' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFDC68E6020>)>'
        'get_blend_type': None, # (!) real value is "<method 'get_blend_type' of 'panda3d.direct.CLerpInterval' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFDC68E6020>)>'
        'stringBlendType': None, # (!) real value is '<staticmethod(<built-in method stringBlendType of type object at 0x00007FFDC68E6020>)>'
        'string_blend_type': None, # (!) real value is '<staticmethod(<built-in method string_blend_type of type object at 0x00007FFDC68E6020>)>'
    }


