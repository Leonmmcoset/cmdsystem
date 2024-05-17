# encoding: utf-8
# module panda3d.egg
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\egg.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import panda3d.core as __panda3d_core


from .EggCurve import EggCurve

class EggNurbsCurve(EggCurve):
    """
    /**
     * A parametric NURBS curve.
     */
    """
    def assign(self, const_EggNurbsCurve_self, const_EggNurbsCurve_copy): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        assign(const EggNurbsCurve self, const EggNurbsCurve copy)
        
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

    def getDegree(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_degree(EggNurbsCurve self)
        
        /**
         * Returns the degree of the curve.  For a typical NURBS, the degree is 3.
         */
        """
        pass

    def getKnot(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_knot(EggNurbsCurve self, int k)
        
        /**
         * Returns the nth knot value defined.
         */
        """
        pass

    def getKnots(self, *args, **kwargs): # real signature unknown
        pass

    def getNumCvs(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_cvs(EggNurbsCurve self)
        
        /**
         * Returns the total number of control vertices that *should* be defined for
         * the curve.  This is determined by the number of knots and the order, in
         * each direction; it does not necessarily reflect the number of vertices that
         * have actually been added to the curve.  (However, if the number of vertices
         * in the curve are wrong, the curve is invalid.)
         */
        """
        pass

    def getNumKnots(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_knots(EggNurbsCurve self)
        
        /**
         * Returns the number of knots.
         */
        """
        pass

    def getOrder(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_order(EggNurbsCurve self)
        
        /**
         * Returns the order of the curve.  The order is the degree of the NURBS
         * equation plus 1; for a typical NURBS, the order is 4.  With this
         * implementation of NURBS, the order must be in the range [1, 4].
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_degree(self, EggNurbsCurve_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_degree(EggNurbsCurve self)
        
        /**
         * Returns the degree of the curve.  For a typical NURBS, the degree is 3.
         */
        """
        pass

    def get_knot(self, EggNurbsCurve_self, int_k): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_knot(EggNurbsCurve self, int k)
        
        /**
         * Returns the nth knot value defined.
         */
        """
        pass

    def get_knots(self, *args, **kwargs): # real signature unknown
        pass

    def get_num_cvs(self, EggNurbsCurve_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_cvs(EggNurbsCurve self)
        
        /**
         * Returns the total number of control vertices that *should* be defined for
         * the curve.  This is determined by the number of knots and the order, in
         * each direction; it does not necessarily reflect the number of vertices that
         * have actually been added to the curve.  (However, if the number of vertices
         * in the curve are wrong, the curve is invalid.)
         */
        """
        pass

    def get_num_knots(self, EggNurbsCurve_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_knots(EggNurbsCurve self)
        
        /**
         * Returns the number of knots.
         */
        """
        pass

    def get_order(self, EggNurbsCurve_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_order(EggNurbsCurve self)
        
        /**
         * Returns the order of the curve.  The order is the degree of the NURBS
         * equation plus 1; for a typical NURBS, the order is 4.  With this
         * implementation of NURBS, the order must be in the range [1, 4].
         */
        """
        pass

    def isClosed(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_closed(EggNurbsCurve self)
        
        /**
         * Returns true if the curve appears to be closed.  Since the Egg syntax does
         * not provide a means for explicit indication of closure, this has to be
         * guessed at by examining the curve itself.
         */
        """
        pass

    def isValid(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_valid(EggNurbsCurve self)
        
        /**
         * Returns true if the NURBS parameters are all internally consistent (e.g.
         * it has the right number of vertices to match its number of knots and order
         * in each dimension), or false otherwise.
         */
        """
        pass

    def is_closed(self, EggNurbsCurve_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_closed(EggNurbsCurve self)
        
        /**
         * Returns true if the curve appears to be closed.  Since the Egg syntax does
         * not provide a means for explicit indication of closure, this has to be
         * guessed at by examining the curve itself.
         */
        """
        pass

    def is_valid(self, EggNurbsCurve_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_valid(EggNurbsCurve self)
        
        /**
         * Returns true if the NURBS parameters are all internally consistent (e.g.
         * it has the right number of vertices to match its number of knots and order
         * in each dimension), or false otherwise.
         */
        """
        pass

    def setKnot(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_knot(const EggNurbsCurve self, int k, double value)
        
        /**
         * Resets the value of the indicated knot as indicated.  k must be in the
         * range 0 <= k < get_num_knots(), and the value must be in the range
         * get_knot(k - 1) <= value <= get_knot(k + 1).
         */
        """
        pass

    def setNumKnots(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_num_knots(const EggNurbsCurve self, int num)
        
        /**
         * Directly changes the number of knots.  This will either add zero-valued
         * knots onto the end, or truncate knot values from the end, depending on
         * whether the list is being increased or decreased.  If possible, it is
         * preferable to use the setup() method instead of directly setting the number
         * of knots, as this may result in an invalid curve.
         */
        """
        pass

    def setOrder(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_order(const EggNurbsCurve self, int order)
        
        /**
         * Directly changes the order to the indicated value (which must be an integer
         * in the range 1 <= order <= 4).  If possible, it is preferable to use the
         * setup() method instead of this method, since changing the order directly
         * may result in an invalid curve.
         */
        """
        pass

    def setup(self, const_EggNurbsCurve_self, int_order, int_num_knots): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        setup(const EggNurbsCurve self, int order, int num_knots)
        
        /**
         * Prepares a new curve definition with the indicated order and number of
         * knots.  This also implies a particular number of vertices as well (the
         * number of knots minus the order), but it is up to the user to add the
         * correct number of vertices to the curve by repeatedly calling push_back().
         */
        """
        pass

    def set_knot(self, const_EggNurbsCurve_self, int_k, double_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_knot(const EggNurbsCurve self, int k, double value)
        
        /**
         * Resets the value of the indicated knot as indicated.  k must be in the
         * range 0 <= k < get_num_knots(), and the value must be in the range
         * get_knot(k - 1) <= value <= get_knot(k + 1).
         */
        """
        pass

    def set_num_knots(self, const_EggNurbsCurve_self, int_num): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_num_knots(const EggNurbsCurve self, int num)
        
        /**
         * Directly changes the number of knots.  This will either add zero-valued
         * knots onto the end, or truncate knot values from the end, depending on
         * whether the list is being increased or decreased.  If possible, it is
         * preferable to use the setup() method instead of directly setting the number
         * of knots, as this may result in an invalid curve.
         */
        """
        pass

    def set_order(self, const_EggNurbsCurve_self, int_order): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_order(const EggNurbsCurve self, int order)
        
        /**
         * Directly changes the order to the indicated value (which must be an integer
         * in the range 1 <= order <= 4).  If possible, it is preferable to use the
         * setup() method instead of this method, since changing the order directly
         * may result in an invalid curve.
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

    closed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    degree = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    knots = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    order = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.egg.EggNurbsCurve' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.egg.EggNurbsCurve' objects>"
        '__doc__': '/**\n * A parametric NURBS curve.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.egg.EggNurbsCurve' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDC68D0350>'
        'assign': None, # (!) real value is "<method 'assign' of 'panda3d.egg.EggNurbsCurve' objects>"
        'closed': None, # (!) real value is "<attribute 'closed' of 'panda3d.egg.EggNurbsCurve' objects>"
        'degree': None, # (!) real value is "<attribute 'degree' of 'panda3d.egg.EggNurbsCurve' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFDC68D0350>)>'
        'getDegree': None, # (!) real value is "<method 'getDegree' of 'panda3d.egg.EggNurbsCurve' objects>"
        'getKnot': None, # (!) real value is "<method 'getKnot' of 'panda3d.egg.EggNurbsCurve' objects>"
        'getKnots': None, # (!) real value is "<method 'getKnots' of 'panda3d.egg.EggNurbsCurve' objects>"
        'getNumCvs': None, # (!) real value is "<method 'getNumCvs' of 'panda3d.egg.EggNurbsCurve' objects>"
        'getNumKnots': None, # (!) real value is "<method 'getNumKnots' of 'panda3d.egg.EggNurbsCurve' objects>"
        'getOrder': None, # (!) real value is "<method 'getOrder' of 'panda3d.egg.EggNurbsCurve' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFDC68D0350>)>'
        'get_degree': None, # (!) real value is "<method 'get_degree' of 'panda3d.egg.EggNurbsCurve' objects>"
        'get_knot': None, # (!) real value is "<method 'get_knot' of 'panda3d.egg.EggNurbsCurve' objects>"
        'get_knots': None, # (!) real value is "<method 'get_knots' of 'panda3d.egg.EggNurbsCurve' objects>"
        'get_num_cvs': None, # (!) real value is "<method 'get_num_cvs' of 'panda3d.egg.EggNurbsCurve' objects>"
        'get_num_knots': None, # (!) real value is "<method 'get_num_knots' of 'panda3d.egg.EggNurbsCurve' objects>"
        'get_order': None, # (!) real value is "<method 'get_order' of 'panda3d.egg.EggNurbsCurve' objects>"
        'isClosed': None, # (!) real value is "<method 'isClosed' of 'panda3d.egg.EggNurbsCurve' objects>"
        'isValid': None, # (!) real value is "<method 'isValid' of 'panda3d.egg.EggNurbsCurve' objects>"
        'is_closed': None, # (!) real value is "<method 'is_closed' of 'panda3d.egg.EggNurbsCurve' objects>"
        'is_valid': None, # (!) real value is "<method 'is_valid' of 'panda3d.egg.EggNurbsCurve' objects>"
        'knots': None, # (!) real value is "<attribute 'knots' of 'panda3d.egg.EggNurbsCurve' objects>"
        'order': None, # (!) real value is "<attribute 'order' of 'panda3d.egg.EggNurbsCurve' objects>"
        'setKnot': None, # (!) real value is "<method 'setKnot' of 'panda3d.egg.EggNurbsCurve' objects>"
        'setNumKnots': None, # (!) real value is "<method 'setNumKnots' of 'panda3d.egg.EggNurbsCurve' objects>"
        'setOrder': None, # (!) real value is "<method 'setOrder' of 'panda3d.egg.EggNurbsCurve' objects>"
        'set_knot': None, # (!) real value is "<method 'set_knot' of 'panda3d.egg.EggNurbsCurve' objects>"
        'set_num_knots': None, # (!) real value is "<method 'set_num_knots' of 'panda3d.egg.EggNurbsCurve' objects>"
        'set_order': None, # (!) real value is "<method 'set_order' of 'panda3d.egg.EggNurbsCurve' objects>"
        'setup': None, # (!) real value is "<method 'setup' of 'panda3d.egg.EggNurbsCurve' objects>"
    }


