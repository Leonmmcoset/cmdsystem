# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .ReferenceCount import ReferenceCount

class NurbsSurfaceResult(ReferenceCount):
    """
    /**
     * The result of a NurbsSurfaceEvaluator.  This object represents a surface in
     * a particular coordinate space.  It can return the point and/or normal to
     * the surface at any point.
     */
    """
    def evalExtendedPoint(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        eval_extended_point(const NurbsSurfaceResult self, float u, float v, int d)
        
        /**
         * Evaluates the surface in n-dimensional space according to the extended
         * vertices associated with the surface in the indicated dimension.
         */
        """
        pass

    def evalExtendedPoints(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        eval_extended_points(const NurbsSurfaceResult self, float u, float v, int d, buffer result, int num_values)
        
        /**
         * Simultaneously performs eval_extended_point on a contiguous sequence of
         * dimensions.  The dimensions evaluated are d through (d + num_values - 1);
         * the results are filled into the num_values elements in the indicated result
         * array.
         */
        """
        pass

    def evalNormal(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        eval_normal(const NurbsSurfaceResult self, float u, float v, LVecBase3f normal)
        
        /**
         * Computes the normal to the surface at the indicated point in parametric
         * time.  This normal vector will not necessarily be normalized, and could be
         * zero.  See also eval_point().
         */
        """
        pass

    def evalPoint(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        eval_point(const NurbsSurfaceResult self, float u, float v, LVecBase3f point)
        
        /**
         * Computes the point on the surface corresponding to the indicated value in
         * parametric time.  Returns true if the u, v values are valid, false
         * otherwise.
         */
        """
        pass

    def evalSegmentExtendedPoint(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        eval_segment_extended_point(NurbsSurfaceResult self, int ui, int vi, float u, float v, int d)
        
        /**
         * Evaluates the surface in n-dimensional space according to the extended
         * vertices associated with the surface in the indicated dimension.
         */
        """
        pass

    def evalSegmentExtendedPoints(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        eval_segment_extended_points(NurbsSurfaceResult self, int ui, int vi, float u, float v, int d, buffer result, int num_values)
        
        /**
         * Simultaneously performs eval_extended_point on a contiguous sequence of
         * dimensions.  The dimensions evaluated are d through (d + num_values - 1);
         * the results are filled into the num_values elements in the indicated result
         * array.
         */
        """
        pass

    def evalSegmentNormal(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        eval_segment_normal(NurbsSurfaceResult self, int ui, int vi, float u, float v, LVecBase3f normal)
        
        /**
         * As eval_segment_point, but computes the normal to the surface at the
         * indicated point.  The normal vector will not necessarily be normalized, and
         * could be zero.
         */
        """
        pass

    def evalSegmentPoint(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        eval_segment_point(NurbsSurfaceResult self, int ui, int vi, float u, float v, LVecBase3f point)
        
        /**
         * Evaluates the point on the surface corresponding to the indicated value in
         * parametric time within the indicated surface segment.  u and v should be in
         * the range [0, 1].
         *
         * The surface is internally represented as a number of connected (or possibly
         * unconnected) piecewise continuous segments.  The exact number of segments
         * for a particular surface depends on the knot vector, and is returned by
         * get_num_segments().  Normally, eval_point() is used to evaluate a point
         * along the continuous surface, but when you care more about local
         * continuity, you can use eval_segment_point() to evaluate the points along
         * each segment.
         */
        """
        pass

    def eval_extended_point(self, const_NurbsSurfaceResult_self, float_u, float_v, int_d): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        eval_extended_point(const NurbsSurfaceResult self, float u, float v, int d)
        
        /**
         * Evaluates the surface in n-dimensional space according to the extended
         * vertices associated with the surface in the indicated dimension.
         */
        """
        pass

    def eval_extended_points(self, const_NurbsSurfaceResult_self, float_u, float_v, int_d, buffer_result, int_num_values): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        eval_extended_points(const NurbsSurfaceResult self, float u, float v, int d, buffer result, int num_values)
        
        /**
         * Simultaneously performs eval_extended_point on a contiguous sequence of
         * dimensions.  The dimensions evaluated are d through (d + num_values - 1);
         * the results are filled into the num_values elements in the indicated result
         * array.
         */
        """
        pass

    def eval_normal(self, const_NurbsSurfaceResult_self, float_u, float_v, LVecBase3f_normal): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        eval_normal(const NurbsSurfaceResult self, float u, float v, LVecBase3f normal)
        
        /**
         * Computes the normal to the surface at the indicated point in parametric
         * time.  This normal vector will not necessarily be normalized, and could be
         * zero.  See also eval_point().
         */
        """
        pass

    def eval_point(self, const_NurbsSurfaceResult_self, float_u, float_v, LVecBase3f_point): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        eval_point(const NurbsSurfaceResult self, float u, float v, LVecBase3f point)
        
        /**
         * Computes the point on the surface corresponding to the indicated value in
         * parametric time.  Returns true if the u, v values are valid, false
         * otherwise.
         */
        """
        pass

    def eval_segment_extended_point(self, NurbsSurfaceResult_self, int_ui, int_vi, float_u, float_v, int_d): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        eval_segment_extended_point(NurbsSurfaceResult self, int ui, int vi, float u, float v, int d)
        
        /**
         * Evaluates the surface in n-dimensional space according to the extended
         * vertices associated with the surface in the indicated dimension.
         */
        """
        pass

    def eval_segment_extended_points(self, NurbsSurfaceResult_self, int_ui, int_vi, float_u, float_v, int_d, buffer_result, int_num_values): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        eval_segment_extended_points(NurbsSurfaceResult self, int ui, int vi, float u, float v, int d, buffer result, int num_values)
        
        /**
         * Simultaneously performs eval_extended_point on a contiguous sequence of
         * dimensions.  The dimensions evaluated are d through (d + num_values - 1);
         * the results are filled into the num_values elements in the indicated result
         * array.
         */
        """
        pass

    def eval_segment_normal(self, NurbsSurfaceResult_self, int_ui, int_vi, float_u, float_v, LVecBase3f_normal): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        eval_segment_normal(NurbsSurfaceResult self, int ui, int vi, float u, float v, LVecBase3f normal)
        
        /**
         * As eval_segment_point, but computes the normal to the surface at the
         * indicated point.  The normal vector will not necessarily be normalized, and
         * could be zero.
         */
        """
        pass

    def eval_segment_point(self, NurbsSurfaceResult_self, int_ui, int_vi, float_u, float_v, LVecBase3f_point): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        eval_segment_point(NurbsSurfaceResult self, int ui, int vi, float u, float v, LVecBase3f point)
        
        /**
         * Evaluates the point on the surface corresponding to the indicated value in
         * parametric time within the indicated surface segment.  u and v should be in
         * the range [0, 1].
         *
         * The surface is internally represented as a number of connected (or possibly
         * unconnected) piecewise continuous segments.  The exact number of segments
         * for a particular surface depends on the knot vector, and is returned by
         * get_num_segments().  Normally, eval_point() is used to evaluate a point
         * along the continuous surface, but when you care more about local
         * continuity, you can use eval_segment_point() to evaluate the points along
         * each segment.
         */
        """
        pass

    def getEndU(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_end_u(NurbsSurfaceResult self)
        
        /**
         * Returns the last legal value of u on the surface.
         */
        """
        pass

    def getEndV(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_end_v(NurbsSurfaceResult self)
        
        /**
         * Returns the last legal value of v on the surface.
         */
        """
        pass

    def getNumUSegments(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_u_segments(NurbsSurfaceResult self)
        
        /**
         * Returns the number of piecewise continuous segments within the surface in
         * the U direction.  This number is usually not important unless you plan to
         * call eval_segment_point().
         */
        """
        pass

    def getNumVSegments(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_v_segments(NurbsSurfaceResult self)
        
        /**
         * Returns the number of piecewise continuous segments within the surface in
         * the V direction.  This number is usually not important unless you plan to
         * call eval_segment_point().
         */
        """
        pass

    def getSegmentU(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_segment_u(NurbsSurfaceResult self, int ui, float u)
        
        /**
         * Accepts a u value in the range [0, 1], and assumed to be relative to the
         * indicated segment (as in eval_segment_point()), and returns the
         * corresponding u value in the entire surface (as in eval_point()).
         */
        """
        pass

    def getSegmentV(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_segment_v(NurbsSurfaceResult self, int vi, float v)
        
        /**
         * Accepts a v value in the range [0, 1], and assumed to be relative to the
         * indicated segment (as in eval_segment_point()), and returns the
         * corresponding v value in the entire surface (as in eval_point()).
         */
        """
        pass

    def getStartU(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_start_u(NurbsSurfaceResult self)
        
        /**
         * Returns the first legal value of u on the surface.  Usually this is 0.0.
         */
        """
        pass

    def getStartV(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_start_v(NurbsSurfaceResult self)
        
        /**
         * Returns the first legal value of v on the surface.  Usually this is 0.0.
         */
        """
        pass

    def get_end_u(self, NurbsSurfaceResult_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_end_u(NurbsSurfaceResult self)
        
        /**
         * Returns the last legal value of u on the surface.
         */
        """
        pass

    def get_end_v(self, NurbsSurfaceResult_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_end_v(NurbsSurfaceResult self)
        
        /**
         * Returns the last legal value of v on the surface.
         */
        """
        pass

    def get_num_u_segments(self, NurbsSurfaceResult_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_u_segments(NurbsSurfaceResult self)
        
        /**
         * Returns the number of piecewise continuous segments within the surface in
         * the U direction.  This number is usually not important unless you plan to
         * call eval_segment_point().
         */
        """
        pass

    def get_num_v_segments(self, NurbsSurfaceResult_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_v_segments(NurbsSurfaceResult self)
        
        /**
         * Returns the number of piecewise continuous segments within the surface in
         * the V direction.  This number is usually not important unless you plan to
         * call eval_segment_point().
         */
        """
        pass

    def get_segment_u(self, NurbsSurfaceResult_self, int_ui, float_u): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_segment_u(NurbsSurfaceResult self, int ui, float u)
        
        /**
         * Accepts a u value in the range [0, 1], and assumed to be relative to the
         * indicated segment (as in eval_segment_point()), and returns the
         * corresponding u value in the entire surface (as in eval_point()).
         */
        """
        pass

    def get_segment_v(self, NurbsSurfaceResult_self, int_vi, float_v): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_segment_v(NurbsSurfaceResult self, int vi, float v)
        
        /**
         * Accepts a v value in the range [0, 1], and assumed to be relative to the
         * indicated segment (as in eval_segment_point()), and returns the
         * corresponding v value in the entire surface (as in eval_point()).
         */
        """
        pass

    def get_start_u(self, NurbsSurfaceResult_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_start_u(NurbsSurfaceResult self)
        
        /**
         * Returns the first legal value of u on the surface.  Usually this is 0.0.
         */
        """
        pass

    def get_start_v(self, NurbsSurfaceResult_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_start_v(NurbsSurfaceResult self)
        
        /**
         * Returns the first legal value of v on the surface.  Usually this is 0.0.
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
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.NurbsSurfaceResult' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.NurbsSurfaceResult' objects>"
        '__doc__': '/**\n * The result of a NurbsSurfaceEvaluator.  This object represents a surface in\n * a particular coordinate space.  It can return the point and/or normal to\n * the surface at any point.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.NurbsSurfaceResult' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE34F0D0>'
        'evalExtendedPoint': None, # (!) real value is "<method 'evalExtendedPoint' of 'panda3d.core.NurbsSurfaceResult' objects>"
        'evalExtendedPoints': None, # (!) real value is "<method 'evalExtendedPoints' of 'panda3d.core.NurbsSurfaceResult' objects>"
        'evalNormal': None, # (!) real value is "<method 'evalNormal' of 'panda3d.core.NurbsSurfaceResult' objects>"
        'evalPoint': None, # (!) real value is "<method 'evalPoint' of 'panda3d.core.NurbsSurfaceResult' objects>"
        'evalSegmentExtendedPoint': None, # (!) real value is "<method 'evalSegmentExtendedPoint' of 'panda3d.core.NurbsSurfaceResult' objects>"
        'evalSegmentExtendedPoints': None, # (!) real value is "<method 'evalSegmentExtendedPoints' of 'panda3d.core.NurbsSurfaceResult' objects>"
        'evalSegmentNormal': None, # (!) real value is "<method 'evalSegmentNormal' of 'panda3d.core.NurbsSurfaceResult' objects>"
        'evalSegmentPoint': None, # (!) real value is "<method 'evalSegmentPoint' of 'panda3d.core.NurbsSurfaceResult' objects>"
        'eval_extended_point': None, # (!) real value is "<method 'eval_extended_point' of 'panda3d.core.NurbsSurfaceResult' objects>"
        'eval_extended_points': None, # (!) real value is "<method 'eval_extended_points' of 'panda3d.core.NurbsSurfaceResult' objects>"
        'eval_normal': None, # (!) real value is "<method 'eval_normal' of 'panda3d.core.NurbsSurfaceResult' objects>"
        'eval_point': None, # (!) real value is "<method 'eval_point' of 'panda3d.core.NurbsSurfaceResult' objects>"
        'eval_segment_extended_point': None, # (!) real value is "<method 'eval_segment_extended_point' of 'panda3d.core.NurbsSurfaceResult' objects>"
        'eval_segment_extended_points': None, # (!) real value is "<method 'eval_segment_extended_points' of 'panda3d.core.NurbsSurfaceResult' objects>"
        'eval_segment_normal': None, # (!) real value is "<method 'eval_segment_normal' of 'panda3d.core.NurbsSurfaceResult' objects>"
        'eval_segment_point': None, # (!) real value is "<method 'eval_segment_point' of 'panda3d.core.NurbsSurfaceResult' objects>"
        'getEndU': None, # (!) real value is "<method 'getEndU' of 'panda3d.core.NurbsSurfaceResult' objects>"
        'getEndV': None, # (!) real value is "<method 'getEndV' of 'panda3d.core.NurbsSurfaceResult' objects>"
        'getNumUSegments': None, # (!) real value is "<method 'getNumUSegments' of 'panda3d.core.NurbsSurfaceResult' objects>"
        'getNumVSegments': None, # (!) real value is "<method 'getNumVSegments' of 'panda3d.core.NurbsSurfaceResult' objects>"
        'getSegmentU': None, # (!) real value is "<method 'getSegmentU' of 'panda3d.core.NurbsSurfaceResult' objects>"
        'getSegmentV': None, # (!) real value is "<method 'getSegmentV' of 'panda3d.core.NurbsSurfaceResult' objects>"
        'getStartU': None, # (!) real value is "<method 'getStartU' of 'panda3d.core.NurbsSurfaceResult' objects>"
        'getStartV': None, # (!) real value is "<method 'getStartV' of 'panda3d.core.NurbsSurfaceResult' objects>"
        'get_end_u': None, # (!) real value is "<method 'get_end_u' of 'panda3d.core.NurbsSurfaceResult' objects>"
        'get_end_v': None, # (!) real value is "<method 'get_end_v' of 'panda3d.core.NurbsSurfaceResult' objects>"
        'get_num_u_segments': None, # (!) real value is "<method 'get_num_u_segments' of 'panda3d.core.NurbsSurfaceResult' objects>"
        'get_num_v_segments': None, # (!) real value is "<method 'get_num_v_segments' of 'panda3d.core.NurbsSurfaceResult' objects>"
        'get_segment_u': None, # (!) real value is "<method 'get_segment_u' of 'panda3d.core.NurbsSurfaceResult' objects>"
        'get_segment_v': None, # (!) real value is "<method 'get_segment_v' of 'panda3d.core.NurbsSurfaceResult' objects>"
        'get_start_u': None, # (!) real value is "<method 'get_start_u' of 'panda3d.core.NurbsSurfaceResult' objects>"
        'get_start_v': None, # (!) real value is "<method 'get_start_v' of 'panda3d.core.NurbsSurfaceResult' objects>"
    }


