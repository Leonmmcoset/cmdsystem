# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .PiecewiseCurve import PiecewiseCurve

from .NurbsCurveInterface import NurbsCurveInterface

class NurbsCurve(PiecewiseCurve, NurbsCurveInterface):
    """
    /**
     * A Nonuniform Rational B-Spline.
     *
     * This class is actually implemented as a PiecewiseCurve made up of several
     * CubicCurvesegs, each of which is created using the nurbs_basis() method.
     * The list of CV's and knots is kept here, within the NurbsCurve class.
     *
     * This class is the original Panda-native implementation of a NURBS curve.
     * It is typedeffed as "NurbsCurve" and performs all NURBS curve functions if
     * we do not have the NURBS++ library available.
     *
     * However, if we *do* have the NURBS++ library, another class exists, the
     * NurbsPPCurve, which is a wrapper around that library and provides some
     * additional functionality.  In that case, the other class is typedeffed to
     * "NurbsCurve" instead of this one, and performs most of the NURBS curve
     * functions.  This class then becomes vestigial.
     */
    """
    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def upcastToNurbsCurveInterface(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_NurbsCurveInterface(const NurbsCurve self)
        
        upcast from NurbsCurve to NurbsCurveInterface
        """
        pass

    def upcastToPiecewiseCurve(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_PiecewiseCurve(const NurbsCurve self)
        
        upcast from NurbsCurve to PiecewiseCurve
        """
        pass

    def upcast_to_NurbsCurveInterface(self, const_NurbsCurve_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_NurbsCurveInterface(const NurbsCurve self)
        
        upcast from NurbsCurve to NurbsCurveInterface
        """
        pass

    def upcast_to_PiecewiseCurve(self, const_NurbsCurve_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_PiecewiseCurve(const NurbsCurve self)
        
        upcast from NurbsCurve to PiecewiseCurve
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * A Nonuniform Rational B-Spline.\n *\n * This class is actually implemented as a PiecewiseCurve made up of several\n * CubicCurvesegs, each of which is created using the nurbs_basis() method.\n * The list of CV\'s and knots is kept here, within the NurbsCurve class.\n *\n * This class is the original Panda-native implementation of a NURBS curve.\n * It is typedeffed as "NurbsCurve" and performs all NURBS curve functions if\n * we do not have the NURBS++ library available.\n *\n * However, if we *do* have the NURBS++ library, another class exists, the\n * NurbsPPCurve, which is a wrapper around that library and provides some\n * additional functionality.  In that case, the other class is typedeffed to\n * "NurbsCurve" instead of this one, and performs most of the NURBS curve\n * functions.  This class then becomes vestigial.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.NurbsCurve' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE34EB60>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE34EB60>)>'
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE34EB60>)>'
        'upcastToNurbsCurveInterface': None, # (!) real value is "<method 'upcastToNurbsCurveInterface' of 'panda3d.core.NurbsCurve' objects>"
        'upcastToPiecewiseCurve': None, # (!) real value is "<method 'upcastToPiecewiseCurve' of 'panda3d.core.NurbsCurve' objects>"
        'upcast_to_NurbsCurveInterface': None, # (!) real value is "<method 'upcast_to_NurbsCurveInterface' of 'panda3d.core.NurbsCurve' objects>"
        'upcast_to_PiecewiseCurve': None, # (!) real value is "<method 'upcast_to_PiecewiseCurve' of 'panda3d.core.NurbsCurve' objects>"
    }


