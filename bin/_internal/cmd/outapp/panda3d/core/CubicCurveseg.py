# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .ParametricCurve import ParametricCurve

class CubicCurveseg(ParametricCurve):
    """
    /**
     * A CubicCurveseg is any curve that can be completely described by four
     * 4-valued basis vectors, one for each dimension in three-space, and one for
     * the homogeneous coordinate.  This includes Beziers, Hermites, and NURBS.
     *
     * This class encapsulates a single curve segment of the cubic curve.
     * Normally, when we think of Bezier and Hermite curves, we think of a
     * piecewise collection of such segments.
     *
     * Although this class includes methods such as hermite_basis() and
     * nurbs_basis(), to generate a Hermite and NURBS curve segment, respectively,
     * only the final basis vectors are stored: the product of the basis matrix of
     * the corresponding curve type, and its geometry vectors.  This is the
     * minimum information needed to evaluate the curve.  However, the individual
     * CV's that were used to compute these basis vectors are not retained; this
     * might be handled in a subclass (for instance, HermiteCurve).
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

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': "/**\n * A CubicCurveseg is any curve that can be completely described by four\n * 4-valued basis vectors, one for each dimension in three-space, and one for\n * the homogeneous coordinate.  This includes Beziers, Hermites, and NURBS.\n *\n * This class encapsulates a single curve segment of the cubic curve.\n * Normally, when we think of Bezier and Hermite curves, we think of a\n * piecewise collection of such segments.\n *\n * Although this class includes methods such as hermite_basis() and\n * nurbs_basis(), to generate a Hermite and NURBS curve segment, respectively,\n * only the final basis vectors are stored: the product of the basis matrix of\n * the corresponding curve type, and its geometry vectors.  This is the\n * minimum information needed to evaluate the curve.  However, the individual\n * CV's that were used to compute these basis vectors are not retained; this\n * might be handled in a subclass (for instance, HermiteCurve).\n */",
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.CubicCurveseg' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE34E080>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE34E080>)>'
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE34E080>)>'
    }


