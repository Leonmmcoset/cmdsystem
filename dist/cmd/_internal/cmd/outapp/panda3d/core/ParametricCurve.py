# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .PandaNode import PandaNode

class ParametricCurve(PandaNode):
    """
    /**
     * A virtual base class for parametric curves.  This encapsulates all curves
     * in 3-d space defined for a single parameter t in the range [0,get_max_t()].
     */
    """
    def adjustPoint(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        adjust_point(const ParametricCurve self, float t, float px, float py, float pz)
        
        /**
         * Recomputes the curve such that it passes through the point (px, py, pz) at
         * time t, but keeps the same tangent value at that point.
         */
        """
        pass

    def adjustPt(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        adjust_pt(const ParametricCurve self, float t, float px, float py, float pz, float tx, float ty, float tz)
        
        /**
         * Recomputes the curve such that it passes through the point (px, py, pz)
         * with the tangent (tx, ty, tz).
         */
        """
        pass

    def adjustTangent(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        adjust_tangent(const ParametricCurve self, float t, float tx, float ty, float tz)
        
        /**
         * Recomputes the curve such that it has the tangent (tx, ty, tz) at time t,
         * but keeps the same position at the point.
         */
        """
        pass

    def adjust_point(self, const_ParametricCurve_self, float_t, float_px, float_py, float_pz): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        adjust_point(const ParametricCurve self, float t, float px, float py, float pz)
        
        /**
         * Recomputes the curve such that it passes through the point (px, py, pz) at
         * time t, but keeps the same tangent value at that point.
         */
        """
        pass

    def adjust_pt(self, const_ParametricCurve_self, float_t, float_px, float_py, float_pz, float_tx, float_ty, float_tz): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        adjust_pt(const ParametricCurve self, float t, float px, float py, float pz, float tx, float ty, float tz)
        
        /**
         * Recomputes the curve such that it passes through the point (px, py, pz)
         * with the tangent (tx, ty, tz).
         */
        """
        pass

    def adjust_tangent(self, const_ParametricCurve_self, float_t, float_tx, float_ty, float_tz): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        adjust_tangent(const ParametricCurve self, float t, float tx, float ty, float tz)
        
        /**
         * Recomputes the curve such that it has the tangent (tx, ty, tz) at time t,
         * but keeps the same position at the point.
         */
        """
        pass

    def calcLength(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        calc_length(ParametricCurve self)
        calc_length(ParametricCurve self, float from, float to)
        
        /**
         * Approximates the length of the entire curve to within a few decimal places.
         */
        
        /**
         * Approximates the length of the curve segment from parametric time 'from' to
         * time 'to'.
         */
        """
        pass

    def calc_length(self, ParametricCurve_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        calc_length(ParametricCurve self)
        calc_length(ParametricCurve self, float from, float to)
        
        /**
         * Approximates the length of the entire curve to within a few decimal places.
         */
        
        /**
         * Approximates the length of the curve segment from parametric time 'from' to
         * time 'to'.
         */
        """
        pass

    def findLength(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        find_length(ParametricCurve self, float start_t, float length_offset)
        
        /**
         * Returns the parametric value corresponding to the indicated distance along
         * the curve from the starting parametric value.
         *
         * This is the inverse of calc_length(): rather than determining the length
         * along the curve between two parametric points, it determines the position
         * in parametric time of a point n units along the curve.
         *
         * The search distance must not be negative.
         */
        """
        pass

    def find_length(self, ParametricCurve_self, float_start_t, float_length_offset): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        find_length(ParametricCurve self, float start_t, float length_offset)
        
        /**
         * Returns the parametric value corresponding to the indicated distance along
         * the curve from the starting parametric value.
         *
         * This is the inverse of calc_length(): rather than determining the length
         * along the curve between two parametric points, it determines the position
         * in parametric time of a point n units along the curve.
         *
         * The search distance must not be negative.
         */
        """
        pass

    def get2ndtangent(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_2ndtangent(ParametricCurve self, float t, LVecBase3f tangent2)
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
        get_curve_type(ParametricCurve self)
        
        /**
         * Returns the flag indicating the use to which the curve is intended to be
         * put.
         */
        """
        pass

    def getMaxT(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_max_t(ParametricCurve self)
        
        /**
         * Returns the upper bound of t for the entire curve.  The curve is defined in
         * the range 0.0f <= t <= get_max_t().  This base class function always
         * returns 1.0f; derived classes might override this to return something else.
         */
        """
        pass

    def getNumDimensions(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_dimensions(ParametricCurve self)
        
        /**
         * Returns the number of significant dimensions in the curve's vertices, as
         * set by a previous call to set_num_dimensions().  This is only a hint as to
         * how the curve is intended to be used; the actual number of dimensions of
         * any curve is always three.
         */
        """
        pass

    def getPoint(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_point(ParametricCurve self, float t, LVecBase3f point)
        """
        pass

    def getPt(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_pt(ParametricCurve self, float t, LVecBase3f point, LVecBase3f tangent)
        """
        pass

    def getTangent(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_tangent(ParametricCurve self, float t, LVecBase3f tangent)
        """
        pass

    def get_2ndtangent(self, ParametricCurve_self, float_t, LVecBase3f_tangent2): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_2ndtangent(ParametricCurve self, float t, LVecBase3f tangent2)
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_curve_type(self, ParametricCurve_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_curve_type(ParametricCurve self)
        
        /**
         * Returns the flag indicating the use to which the curve is intended to be
         * put.
         */
        """
        pass

    def get_max_t(self, ParametricCurve_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_max_t(ParametricCurve self)
        
        /**
         * Returns the upper bound of t for the entire curve.  The curve is defined in
         * the range 0.0f <= t <= get_max_t().  This base class function always
         * returns 1.0f; derived classes might override this to return something else.
         */
        """
        pass

    def get_num_dimensions(self, ParametricCurve_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_dimensions(ParametricCurve self)
        
        /**
         * Returns the number of significant dimensions in the curve's vertices, as
         * set by a previous call to set_num_dimensions().  This is only a hint as to
         * how the curve is intended to be used; the actual number of dimensions of
         * any curve is always three.
         */
        """
        pass

    def get_point(self, ParametricCurve_self, float_t, LVecBase3f_point): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_point(ParametricCurve self, float t, LVecBase3f point)
        """
        pass

    def get_pt(self, ParametricCurve_self, float_t, LVecBase3f_point, LVecBase3f_tangent): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_pt(ParametricCurve self, float t, LVecBase3f point, LVecBase3f tangent)
        """
        pass

    def get_tangent(self, ParametricCurve_self, float_t, LVecBase3f_tangent): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_tangent(ParametricCurve self, float t, LVecBase3f tangent)
        """
        pass

    def isValid(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_valid(ParametricCurve self)
        
        /**
         * Returns true if the curve is defined.  This base class function always
         * returns true; derived classes might override this to sometimes return
         * false.
         */
        """
        pass

    def is_valid(self, ParametricCurve_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_valid(ParametricCurve self)
        
        /**
         * Returns true if the curve is defined.  This base class function always
         * returns true; derived classes might override this to sometimes return
         * false.
         */
        """
        pass

    def recompute(self, const_ParametricCurve_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        recompute(const ParametricCurve self)
        
        /**
         * Recalculates the curve, if necessary.  Returns true if the resulting curve
         * is valid, false otherwise.
         */
        """
        pass

    def setCurveType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_curve_type(const ParametricCurve self, int type)
        
        /**
         * Sets the flag indicating the use to which the curve is intended to be put.
         * This flag is optional and only serves to provide a hint to the egg reader
         * and writer code; it has no effect on the curve's behavior.
         *
         * Setting the curve type also sets the num_dimensions to 3 or 1 according to
         * the type.
         *
         * THis flag may have one of the values PCT_XYZ, PCT_HPR, or PCT_T.
         */
        """
        pass

    def setNumDimensions(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_num_dimensions(const ParametricCurve self, int num)
        
        /**
         * Specifies the number of significant dimensions in the curve's vertices.
         * This should be one of 1, 2, or 3. Normally, XYZ and HPR curves have three
         * dimensions; time curves should always have one dimension.  This only serves
         * as a hint to the mopath editor, and also controls how the curve is written
         * out.
         */
        """
        pass

    def set_curve_type(self, const_ParametricCurve_self, int_type): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_curve_type(const ParametricCurve self, int type)
        
        /**
         * Sets the flag indicating the use to which the curve is intended to be put.
         * This flag is optional and only serves to provide a hint to the egg reader
         * and writer code; it has no effect on the curve's behavior.
         *
         * Setting the curve type also sets the num_dimensions to 3 or 1 according to
         * the type.
         *
         * THis flag may have one of the values PCT_XYZ, PCT_HPR, or PCT_T.
         */
        """
        pass

    def set_num_dimensions(self, const_ParametricCurve_self, int_num): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_num_dimensions(const ParametricCurve self, int num)
        
        /**
         * Specifies the number of significant dimensions in the curve's vertices.
         * This should be one of 1, 2, or 3. Normally, XYZ and HPR curves have three
         * dimensions; time curves should always have one dimension.  This only serves
         * as a hint to the mopath editor, and also controls how the curve is written
         * out.
         */
        """
        pass

    def stitch(self, const_ParametricCurve_self, const_ParametricCurve_a, const_ParametricCurve_b): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        stitch(const ParametricCurve self, const ParametricCurve a, const ParametricCurve b)
        
        /**
         * Regenerates this curve as one long curve: the first curve connected end-to-
         * end with the second one.  Either a or b may be the same as 'this'.
         *
         * Returns true if successful, false on failure or if the curve type does not
         * support stitching.
         */
        """
        pass

    def writeEgg(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        write_egg(const ParametricCurve self, Filename filename)
        write_egg(const ParametricCurve self, Filename filename, int cs)
        write_egg(const ParametricCurve self, ostream out, const Filename filename, int cs)
        
        /**
         * Writes an egg description of the nurbs curve to the specified output file.
         * Returns true if the file is successfully written.
         */
        
        /**
         * Writes an egg description of the nurbs curve to the specified output
         * stream.  Returns true if the file is successfully written.
         */
        """
        pass

    def write_egg(self, const_ParametricCurve_self, Filename_filename): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write_egg(const ParametricCurve self, Filename filename)
        write_egg(const ParametricCurve self, Filename filename, int cs)
        write_egg(const ParametricCurve self, ostream out, const Filename filename, int cs)
        
        /**
         * Writes an egg description of the nurbs curve to the specified output file.
         * Returns true if the file is successfully written.
         */
        
        /**
         * Writes an egg description of the nurbs curve to the specified output
         * stream.  Returns true if the file is successfully written.
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
        '__doc__': '/**\n * A virtual base class for parametric curves.  This encapsulates all curves\n * in 3-d space defined for a single parameter t in the range [0,get_max_t()].\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.ParametricCurve' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE34DEB0>'
        'adjustPoint': None, # (!) real value is "<method 'adjustPoint' of 'panda3d.core.ParametricCurve' objects>"
        'adjustPt': None, # (!) real value is "<method 'adjustPt' of 'panda3d.core.ParametricCurve' objects>"
        'adjustTangent': None, # (!) real value is "<method 'adjustTangent' of 'panda3d.core.ParametricCurve' objects>"
        'adjust_point': None, # (!) real value is "<method 'adjust_point' of 'panda3d.core.ParametricCurve' objects>"
        'adjust_pt': None, # (!) real value is "<method 'adjust_pt' of 'panda3d.core.ParametricCurve' objects>"
        'adjust_tangent': None, # (!) real value is "<method 'adjust_tangent' of 'panda3d.core.ParametricCurve' objects>"
        'calcLength': None, # (!) real value is "<method 'calcLength' of 'panda3d.core.ParametricCurve' objects>"
        'calc_length': None, # (!) real value is "<method 'calc_length' of 'panda3d.core.ParametricCurve' objects>"
        'findLength': None, # (!) real value is "<method 'findLength' of 'panda3d.core.ParametricCurve' objects>"
        'find_length': None, # (!) real value is "<method 'find_length' of 'panda3d.core.ParametricCurve' objects>"
        'get2ndtangent': None, # (!) real value is "<method 'get2ndtangent' of 'panda3d.core.ParametricCurve' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE34DEB0>)>'
        'getCurveType': None, # (!) real value is "<method 'getCurveType' of 'panda3d.core.ParametricCurve' objects>"
        'getMaxT': None, # (!) real value is "<method 'getMaxT' of 'panda3d.core.ParametricCurve' objects>"
        'getNumDimensions': None, # (!) real value is "<method 'getNumDimensions' of 'panda3d.core.ParametricCurve' objects>"
        'getPoint': None, # (!) real value is "<method 'getPoint' of 'panda3d.core.ParametricCurve' objects>"
        'getPt': None, # (!) real value is "<method 'getPt' of 'panda3d.core.ParametricCurve' objects>"
        'getTangent': None, # (!) real value is "<method 'getTangent' of 'panda3d.core.ParametricCurve' objects>"
        'get_2ndtangent': None, # (!) real value is "<method 'get_2ndtangent' of 'panda3d.core.ParametricCurve' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE34DEB0>)>'
        'get_curve_type': None, # (!) real value is "<method 'get_curve_type' of 'panda3d.core.ParametricCurve' objects>"
        'get_max_t': None, # (!) real value is "<method 'get_max_t' of 'panda3d.core.ParametricCurve' objects>"
        'get_num_dimensions': None, # (!) real value is "<method 'get_num_dimensions' of 'panda3d.core.ParametricCurve' objects>"
        'get_point': None, # (!) real value is "<method 'get_point' of 'panda3d.core.ParametricCurve' objects>"
        'get_pt': None, # (!) real value is "<method 'get_pt' of 'panda3d.core.ParametricCurve' objects>"
        'get_tangent': None, # (!) real value is "<method 'get_tangent' of 'panda3d.core.ParametricCurve' objects>"
        'isValid': None, # (!) real value is "<method 'isValid' of 'panda3d.core.ParametricCurve' objects>"
        'is_valid': None, # (!) real value is "<method 'is_valid' of 'panda3d.core.ParametricCurve' objects>"
        'recompute': None, # (!) real value is "<method 'recompute' of 'panda3d.core.ParametricCurve' objects>"
        'setCurveType': None, # (!) real value is "<method 'setCurveType' of 'panda3d.core.ParametricCurve' objects>"
        'setNumDimensions': None, # (!) real value is "<method 'setNumDimensions' of 'panda3d.core.ParametricCurve' objects>"
        'set_curve_type': None, # (!) real value is "<method 'set_curve_type' of 'panda3d.core.ParametricCurve' objects>"
        'set_num_dimensions': None, # (!) real value is "<method 'set_num_dimensions' of 'panda3d.core.ParametricCurve' objects>"
        'stitch': None, # (!) real value is "<method 'stitch' of 'panda3d.core.ParametricCurve' objects>"
        'writeEgg': None, # (!) real value is "<method 'writeEgg' of 'panda3d.core.ParametricCurve' objects>"
        'write_egg': None, # (!) real value is "<method 'write_egg' of 'panda3d.core.ParametricCurve' objects>"
    }


