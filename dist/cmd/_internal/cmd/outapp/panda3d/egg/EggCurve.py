# encoding: utf-8
# module panda3d.egg
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\egg.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import panda3d.core as __panda3d_core


from .EggPrimitive import EggPrimitive

class EggCurve(EggPrimitive):
    """
    /**
     * A parametric curve of some kind.  See EggNurbsCurve.
     */
    """
    def assign(self, const_EggCurve_self, const_EggCurve_copy): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        assign(const EggCurve self, const EggCurve copy)
        
        /**
         *
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getCurveType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_curve_type(EggCurve self)
        
        /**
         * Returns the indicated type of the curve.
         */
        """
        pass

    def getSubdiv(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_subdiv(EggCurve self)
        
        /**
         * Returns the requested number of subdivisions, or 0 if no particular
         * subdivisions have been requested.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_curve_type(self, EggCurve_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_curve_type(EggCurve self)
        
        /**
         * Returns the indicated type of the curve.
         */
        """
        pass

    def get_subdiv(self, EggCurve_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_subdiv(EggCurve self)
        
        /**
         * Returns the requested number of subdivisions, or 0 if no particular
         * subdivisions have been requested.
         */
        """
        pass

    def setCurveType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_curve_type(const EggCurve self, int type)
        
        /**
         * Sets the type of the curve.  This is primarily used as a hint to any code
         * that may need to deal with this curve.
         */
        """
        pass

    def setSubdiv(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_subdiv(const EggCurve self, int subdiv)
        
        /**
         * Sets the number of subdivisions that will be requested across the curve.
         * (This doesn't necessary guarantee that this number of subdivisions will be
         * made; it's just a hint to any curve renderer or quick tesselator.)  Set the
         * number to 0 to disable the hint.
         */
        """
        pass

    def set_curve_type(self, const_EggCurve_self, int_type): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_curve_type(const EggCurve self, int type)
        
        /**
         * Sets the type of the curve.  This is primarily used as a hint to any code
         * that may need to deal with this curve.
         */
        """
        pass

    def set_subdiv(self, const_EggCurve_self, int_subdiv): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_subdiv(const EggCurve self, int subdiv)
        
        /**
         * Sets the number of subdivisions that will be requested across the curve.
         * (This doesn't necessary guarantee that this number of subdivisions will be
         * made; it's just a hint to any curve renderer or quick tesselator.)  Set the
         * number to 0 to disable the hint.
         */
        """
        pass

    def stringCurveType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        string_curve_type(str string)
        
        /**
         * Returns the CurveType value associated with the given string
         * representation, or CT_invalid if the string does not match any known
         * CurveType value.
         */
        """
        pass

    def string_curve_type(self, str_string): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        string_curve_type(str string)
        
        /**
         * Returns the CurveType value associated with the given string
         * representation, or CT_invalid if the string does not match any known
         * CurveType value.
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    CTHpr = 2
    CTNone = 0
    CTT = 3
    CTXyz = 1
    CT_hpr = 2
    CT_none = 0
    CT_t = 3
    CT_xyz = 1
    DtoolClassDict = {
        'CTHpr': 2,
        'CTNone': 0,
        'CTT': 3,
        'CTXyz': 1,
        'CT_hpr': 2,
        'CT_none': 0,
        'CT_t': 3,
        'CT_xyz': 1,
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * A parametric curve of some kind.  See EggNurbsCurve.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.egg.EggCurve' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDC68CF6A0>'
        'assign': None, # (!) real value is "<method 'assign' of 'panda3d.egg.EggCurve' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFDC68CF6A0>)>'
        'getCurveType': None, # (!) real value is "<method 'getCurveType' of 'panda3d.egg.EggCurve' objects>"
        'getSubdiv': None, # (!) real value is "<method 'getSubdiv' of 'panda3d.egg.EggCurve' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFDC68CF6A0>)>'
        'get_curve_type': None, # (!) real value is "<method 'get_curve_type' of 'panda3d.egg.EggCurve' objects>"
        'get_subdiv': None, # (!) real value is "<method 'get_subdiv' of 'panda3d.egg.EggCurve' objects>"
        'setCurveType': None, # (!) real value is "<method 'setCurveType' of 'panda3d.egg.EggCurve' objects>"
        'setSubdiv': None, # (!) real value is "<method 'setSubdiv' of 'panda3d.egg.EggCurve' objects>"
        'set_curve_type': None, # (!) real value is "<method 'set_curve_type' of 'panda3d.egg.EggCurve' objects>"
        'set_subdiv': None, # (!) real value is "<method 'set_subdiv' of 'panda3d.egg.EggCurve' objects>"
        'stringCurveType': None, # (!) real value is '<staticmethod(<built-in method stringCurveType of type object at 0x00007FFDC68CF6A0>)>'
        'string_curve_type': None, # (!) real value is '<staticmethod(<built-in method string_curve_type of type object at 0x00007FFDC68CF6A0>)>'
    }


