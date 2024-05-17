# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class NurbsCurveInterface(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * This abstract class defines the interface only for a Nurbs-style curve,
     * with knots and coordinates in homogeneous space.
     *
     * The NurbsCurve class inherits both from this and from ParametricCurve.
     */
    """
    def appendCv(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        append_cv(const NurbsCurveInterface self, const LVecBase3f v)
        append_cv(const NurbsCurveInterface self, const LVecBase4f v)
        append_cv(const NurbsCurveInterface self, float x, float y, float z)
        
        /**
         *
         */
        
        /**
         *
         */
        
        /**
         *
         */
        """
        pass

    def append_cv(self, const_NurbsCurveInterface_self, const_LVecBase3f_v): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        append_cv(const NurbsCurveInterface self, const LVecBase3f v)
        append_cv(const NurbsCurveInterface self, const LVecBase4f v)
        append_cv(const NurbsCurveInterface self, float x, float y, float z)
        
        /**
         *
         */
        
        /**
         *
         */
        
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

    def getCv(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_cv(NurbsCurveInterface self, int n)
        """
        pass

    def getCvPoint(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_cv_point(NurbsCurveInterface self, int n)
        
        /**
         * Returns the position of the indicated CV.
         */
        """
        pass

    def getCvs(self, *args, **kwargs): # real signature unknown
        pass

    def getCvWeight(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_cv_weight(NurbsCurveInterface self, int n)
        
        /**
         * Returns the weight of the indicated CV.
         */
        """
        pass

    def getKnot(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_knot(NurbsCurveInterface self, int n)
        """
        pass

    def getKnots(self, *args, **kwargs): # real signature unknown
        pass

    def getNumCvs(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_cvs(NurbsCurveInterface self)
        """
        pass

    def getNumKnots(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_knots(NurbsCurveInterface self)
        """
        pass

    def getOrder(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_order(NurbsCurveInterface self)
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_cv(self, NurbsCurveInterface_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_cv(NurbsCurveInterface self, int n)
        """
        pass

    def get_cvs(self, *args, **kwargs): # real signature unknown
        pass

    def get_cv_point(self, NurbsCurveInterface_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_cv_point(NurbsCurveInterface self, int n)
        
        /**
         * Returns the position of the indicated CV.
         */
        """
        pass

    def get_cv_weight(self, NurbsCurveInterface_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_cv_weight(NurbsCurveInterface self, int n)
        
        /**
         * Returns the weight of the indicated CV.
         */
        """
        pass

    def get_knot(self, NurbsCurveInterface_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_knot(NurbsCurveInterface self, int n)
        """
        pass

    def get_knots(self, *args, **kwargs): # real signature unknown
        pass

    def get_num_cvs(self, NurbsCurveInterface_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_cvs(NurbsCurveInterface self)
        """
        pass

    def get_num_knots(self, NurbsCurveInterface_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_knots(NurbsCurveInterface self)
        """
        pass

    def get_order(self, NurbsCurveInterface_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_order(NurbsCurveInterface self)
        """
        pass

    def insertCv(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        insert_cv(const NurbsCurveInterface self, float t)
        """
        pass

    def insert_cv(self, const_NurbsCurveInterface_self, float_t): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        insert_cv(const NurbsCurveInterface self, float t)
        """
        pass

    def removeAllCvs(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_all_cvs(const NurbsCurveInterface self)
        """
        pass

    def removeCv(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_cv(const NurbsCurveInterface self, int n)
        """
        pass

    def remove_all_cvs(self, const_NurbsCurveInterface_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_all_cvs(const NurbsCurveInterface self)
        """
        pass

    def remove_cv(self, const_NurbsCurveInterface_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_cv(const NurbsCurveInterface self, int n)
        """
        pass

    def setCv(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_cv(const NurbsCurveInterface self, int n, const LVecBase4f v)
        """
        pass

    def setCvPoint(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_cv_point(const NurbsCurveInterface self, int n, const LVecBase3f v)
        set_cv_point(const NurbsCurveInterface self, int n, float x, float y, float z)
        
        /**
         * Repositions the indicated CV.  Returns true if successful, false otherwise.
         */
        
        /**
         * Repositions the indicated CV.  Returns true if successful, false otherwise.
         */
        """
        pass

    def setCvWeight(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_cv_weight(const NurbsCurveInterface self, int n, float w)
        
        /**
         * Sets the weight of the indicated CV without affecting its position in 3-d
         * space.
         */
        """
        pass

    def setKnot(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_knot(const NurbsCurveInterface self, int n, float t)
        """
        pass

    def setOrder(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_order(const NurbsCurveInterface self, int order)
        """
        pass

    def set_cv(self, const_NurbsCurveInterface_self, int_n, const_LVecBase4f_v): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_cv(const NurbsCurveInterface self, int n, const LVecBase4f v)
        """
        pass

    def set_cv_point(self, const_NurbsCurveInterface_self, int_n, const_LVecBase3f_v): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_cv_point(const NurbsCurveInterface self, int n, const LVecBase3f v)
        set_cv_point(const NurbsCurveInterface self, int n, float x, float y, float z)
        
        /**
         * Repositions the indicated CV.  Returns true if successful, false otherwise.
         */
        
        /**
         * Repositions the indicated CV.  Returns true if successful, false otherwise.
         */
        """
        pass

    def set_cv_weight(self, const_NurbsCurveInterface_self, int_n, float_w): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_cv_weight(const NurbsCurveInterface self, int n, float w)
        
        /**
         * Sets the weight of the indicated CV without affecting its position in 3-d
         * space.
         */
        """
        pass

    def set_knot(self, const_NurbsCurveInterface_self, int_n, float_t): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_knot(const NurbsCurveInterface self, int n, float t)
        """
        pass

    def set_order(self, const_NurbsCurveInterface_self, int_order): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_order(const NurbsCurveInterface self, int order)
        """
        pass

    def writeCv(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        write_cv(NurbsCurveInterface self, ostream out, int n)
        
        /**
         *
         */
        """
        pass

    def write_cv(self, NurbsCurveInterface_self, ostream_out, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write_cv(NurbsCurveInterface self, ostream out, int n)
        
        /**
         *
         */
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
        '__doc__': '/**\n * This abstract class defines the interface only for a Nurbs-style curve,\n * with knots and coordinates in homogeneous space.\n *\n * The NurbsCurve class inherits both from this and from ParametricCurve.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.NurbsCurveInterface' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE34E990>'
        'appendCv': None, # (!) real value is "<method 'appendCv' of 'panda3d.core.NurbsCurveInterface' objects>"
        'append_cv': None, # (!) real value is "<method 'append_cv' of 'panda3d.core.NurbsCurveInterface' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE34E990>)>'
        'getCv': None, # (!) real value is "<method 'getCv' of 'panda3d.core.NurbsCurveInterface' objects>"
        'getCvPoint': None, # (!) real value is "<method 'getCvPoint' of 'panda3d.core.NurbsCurveInterface' objects>"
        'getCvWeight': None, # (!) real value is "<method 'getCvWeight' of 'panda3d.core.NurbsCurveInterface' objects>"
        'getCvs': None, # (!) real value is "<method 'getCvs' of 'panda3d.core.NurbsCurveInterface' objects>"
        'getKnot': None, # (!) real value is "<method 'getKnot' of 'panda3d.core.NurbsCurveInterface' objects>"
        'getKnots': None, # (!) real value is "<method 'getKnots' of 'panda3d.core.NurbsCurveInterface' objects>"
        'getNumCvs': None, # (!) real value is "<method 'getNumCvs' of 'panda3d.core.NurbsCurveInterface' objects>"
        'getNumKnots': None, # (!) real value is "<method 'getNumKnots' of 'panda3d.core.NurbsCurveInterface' objects>"
        'getOrder': None, # (!) real value is "<method 'getOrder' of 'panda3d.core.NurbsCurveInterface' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE34E990>)>'
        'get_cv': None, # (!) real value is "<method 'get_cv' of 'panda3d.core.NurbsCurveInterface' objects>"
        'get_cv_point': None, # (!) real value is "<method 'get_cv_point' of 'panda3d.core.NurbsCurveInterface' objects>"
        'get_cv_weight': None, # (!) real value is "<method 'get_cv_weight' of 'panda3d.core.NurbsCurveInterface' objects>"
        'get_cvs': None, # (!) real value is "<method 'get_cvs' of 'panda3d.core.NurbsCurveInterface' objects>"
        'get_knot': None, # (!) real value is "<method 'get_knot' of 'panda3d.core.NurbsCurveInterface' objects>"
        'get_knots': None, # (!) real value is "<method 'get_knots' of 'panda3d.core.NurbsCurveInterface' objects>"
        'get_num_cvs': None, # (!) real value is "<method 'get_num_cvs' of 'panda3d.core.NurbsCurveInterface' objects>"
        'get_num_knots': None, # (!) real value is "<method 'get_num_knots' of 'panda3d.core.NurbsCurveInterface' objects>"
        'get_order': None, # (!) real value is "<method 'get_order' of 'panda3d.core.NurbsCurveInterface' objects>"
        'insertCv': None, # (!) real value is "<method 'insertCv' of 'panda3d.core.NurbsCurveInterface' objects>"
        'insert_cv': None, # (!) real value is "<method 'insert_cv' of 'panda3d.core.NurbsCurveInterface' objects>"
        'removeAllCvs': None, # (!) real value is "<method 'removeAllCvs' of 'panda3d.core.NurbsCurveInterface' objects>"
        'removeCv': None, # (!) real value is "<method 'removeCv' of 'panda3d.core.NurbsCurveInterface' objects>"
        'remove_all_cvs': None, # (!) real value is "<method 'remove_all_cvs' of 'panda3d.core.NurbsCurveInterface' objects>"
        'remove_cv': None, # (!) real value is "<method 'remove_cv' of 'panda3d.core.NurbsCurveInterface' objects>"
        'setCv': None, # (!) real value is "<method 'setCv' of 'panda3d.core.NurbsCurveInterface' objects>"
        'setCvPoint': None, # (!) real value is "<method 'setCvPoint' of 'panda3d.core.NurbsCurveInterface' objects>"
        'setCvWeight': None, # (!) real value is "<method 'setCvWeight' of 'panda3d.core.NurbsCurveInterface' objects>"
        'setKnot': None, # (!) real value is "<method 'setKnot' of 'panda3d.core.NurbsCurveInterface' objects>"
        'setOrder': None, # (!) real value is "<method 'setOrder' of 'panda3d.core.NurbsCurveInterface' objects>"
        'set_cv': None, # (!) real value is "<method 'set_cv' of 'panda3d.core.NurbsCurveInterface' objects>"
        'set_cv_point': None, # (!) real value is "<method 'set_cv_point' of 'panda3d.core.NurbsCurveInterface' objects>"
        'set_cv_weight': None, # (!) real value is "<method 'set_cv_weight' of 'panda3d.core.NurbsCurveInterface' objects>"
        'set_knot': None, # (!) real value is "<method 'set_knot' of 'panda3d.core.NurbsCurveInterface' objects>"
        'set_order': None, # (!) real value is "<method 'set_order' of 'panda3d.core.NurbsCurveInterface' objects>"
        'writeCv': None, # (!) real value is "<method 'writeCv' of 'panda3d.core.NurbsCurveInterface' objects>"
        'write_cv': None, # (!) real value is "<method 'write_cv' of 'panda3d.core.NurbsCurveInterface' objects>"
    }


