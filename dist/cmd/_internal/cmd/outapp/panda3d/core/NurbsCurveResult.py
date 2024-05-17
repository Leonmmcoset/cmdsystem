# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .ReferenceCount import ReferenceCount

class NurbsCurveResult(ReferenceCount):
    """
    /**
     * The result of a NurbsCurveEvaluator.  This object represents a curve in a
     * particular coordinate space.  It can return the point and/or tangent to the
     * curve at any point.
     *
     * This is not related to NurbsCurve, CubicCurveseg or any of the
     * ParametricCurve-derived objects in this module.  It is a completely
     * parallel implementation of NURBS curves, and will probably eventually
     * replace the whole ParametricCurve class hierarchy.
     */
    """
    def adaptiveSample(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        adaptive_sample(const NurbsCurveResult self, float tolerance)
        
        /**
         * Determines the set of subdivisions necessary to approximate the curve with
         * a set of linear segments, no point of which is farther than tolerance units
         * from the actual curve.
         *
         * After this call, you may walk through the resulting set of samples with
         * get_num_samples(), get_sample_t(), and get_sample_point().
         */
        """
        pass

    def adaptive_sample(self, const_NurbsCurveResult_self, float_tolerance): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        adaptive_sample(const NurbsCurveResult self, float tolerance)
        
        /**
         * Determines the set of subdivisions necessary to approximate the curve with
         * a set of linear segments, no point of which is farther than tolerance units
         * from the actual curve.
         *
         * After this call, you may walk through the resulting set of samples with
         * get_num_samples(), get_sample_t(), and get_sample_point().
         */
        """
        pass

    def evalExtendedPoint(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        eval_extended_point(const NurbsCurveResult self, float t, int d)
        
        /**
         * Evaluates the curve in n-dimensional space according to the extended
         * vertices associated with the curve in the indicated dimension.
         */
        """
        pass

    def evalExtendedPoints(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        eval_extended_points(const NurbsCurveResult self, float t, int d, buffer result, int num_values)
        
        /**
         * Simultaneously performs eval_extended_point on a contiguous sequence of
         * dimensions.  The dimensions evaluated are d through (d + num_values - 1);
         * the results are filled into the num_values elements in the indicated result
         * array.
         */
        """
        pass

    def evalPoint(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        eval_point(const NurbsCurveResult self, float t, LVecBase3f point)
        
        /**
         * Computes the point on the curve corresponding to the indicated value in
         * parametric time.  Returns true if the t value is valid, false otherwise.
         */
        """
        pass

    def evalSegmentExtendedPoint(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        eval_segment_extended_point(NurbsCurveResult self, int segment, float t, int d)
        
        /**
         * Evaluates the curve in n-dimensional space according to the extended
         * vertices associated with the curve in the indicated dimension.
         */
        """
        pass

    def evalSegmentExtendedPoints(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        eval_segment_extended_points(NurbsCurveResult self, int segment, float t, int d, buffer result, int num_values)
        
        /**
         * Simultaneously performs eval_extended_point on a contiguous sequence of
         * dimensions.  The dimensions evaluated are d through (d + num_values - 1);
         * the results are filled into the num_values elements in the indicated result
         * array.
         */
        """
        pass

    def evalSegmentPoint(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        eval_segment_point(NurbsCurveResult self, int segment, float t, LVecBase3f point)
        
        /**
         * Evaluates the point on the curve corresponding to the indicated value in
         * parametric time within the indicated curve segment.  t should be in the
         * range [0, 1].
         *
         * The curve is internally represented as a number of connected (or possibly
         * unconnected) piecewise continuous segments.  The exact number of segments
         * for a particular curve depends on the knot vector, and is returned by
         * get_num_segments().  Normally, eval_point() is used to evaluate a point
         * along the continuous curve, but when you care more about local continuity,
         * you can use eval_segment_point() to evaluate the points along each segment.
         */
        """
        pass

    def evalSegmentTangent(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        eval_segment_tangent(NurbsCurveResult self, int segment, float t, LVecBase3f tangent)
        
        /**
         * As eval_segment_point, but computes the tangent to the curve at the
         * indicated point.  The tangent vector will not necessarily be normalized,
         * and could be zero, particularly at the endpoints.
         */
        """
        pass

    def evalTangent(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        eval_tangent(const NurbsCurveResult self, float t, LVecBase3f tangent)
        
        /**
         * Computes the tangent to the curve at the indicated point in parametric
         * time.  This tangent vector will not necessarily be normalized, and could be
         * zero.  See also eval_point().
         */
        """
        pass

    def eval_extended_point(self, const_NurbsCurveResult_self, float_t, int_d): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        eval_extended_point(const NurbsCurveResult self, float t, int d)
        
        /**
         * Evaluates the curve in n-dimensional space according to the extended
         * vertices associated with the curve in the indicated dimension.
         */
        """
        pass

    def eval_extended_points(self, const_NurbsCurveResult_self, float_t, int_d, buffer_result, int_num_values): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        eval_extended_points(const NurbsCurveResult self, float t, int d, buffer result, int num_values)
        
        /**
         * Simultaneously performs eval_extended_point on a contiguous sequence of
         * dimensions.  The dimensions evaluated are d through (d + num_values - 1);
         * the results are filled into the num_values elements in the indicated result
         * array.
         */
        """
        pass

    def eval_point(self, const_NurbsCurveResult_self, float_t, LVecBase3f_point): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        eval_point(const NurbsCurveResult self, float t, LVecBase3f point)
        
        /**
         * Computes the point on the curve corresponding to the indicated value in
         * parametric time.  Returns true if the t value is valid, false otherwise.
         */
        """
        pass

    def eval_segment_extended_point(self, NurbsCurveResult_self, int_segment, float_t, int_d): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        eval_segment_extended_point(NurbsCurveResult self, int segment, float t, int d)
        
        /**
         * Evaluates the curve in n-dimensional space according to the extended
         * vertices associated with the curve in the indicated dimension.
         */
        """
        pass

    def eval_segment_extended_points(self, NurbsCurveResult_self, int_segment, float_t, int_d, buffer_result, int_num_values): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        eval_segment_extended_points(NurbsCurveResult self, int segment, float t, int d, buffer result, int num_values)
        
        /**
         * Simultaneously performs eval_extended_point on a contiguous sequence of
         * dimensions.  The dimensions evaluated are d through (d + num_values - 1);
         * the results are filled into the num_values elements in the indicated result
         * array.
         */
        """
        pass

    def eval_segment_point(self, NurbsCurveResult_self, int_segment, float_t, LVecBase3f_point): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        eval_segment_point(NurbsCurveResult self, int segment, float t, LVecBase3f point)
        
        /**
         * Evaluates the point on the curve corresponding to the indicated value in
         * parametric time within the indicated curve segment.  t should be in the
         * range [0, 1].
         *
         * The curve is internally represented as a number of connected (or possibly
         * unconnected) piecewise continuous segments.  The exact number of segments
         * for a particular curve depends on the knot vector, and is returned by
         * get_num_segments().  Normally, eval_point() is used to evaluate a point
         * along the continuous curve, but when you care more about local continuity,
         * you can use eval_segment_point() to evaluate the points along each segment.
         */
        """
        pass

    def eval_segment_tangent(self, NurbsCurveResult_self, int_segment, float_t, LVecBase3f_tangent): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        eval_segment_tangent(NurbsCurveResult self, int segment, float t, LVecBase3f tangent)
        
        /**
         * As eval_segment_point, but computes the tangent to the curve at the
         * indicated point.  The tangent vector will not necessarily be normalized,
         * and could be zero, particularly at the endpoints.
         */
        """
        pass

    def eval_tangent(self, const_NurbsCurveResult_self, float_t, LVecBase3f_tangent): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        eval_tangent(const NurbsCurveResult self, float t, LVecBase3f tangent)
        
        /**
         * Computes the tangent to the curve at the indicated point in parametric
         * time.  This tangent vector will not necessarily be normalized, and could be
         * zero.  See also eval_point().
         */
        """
        pass

    def getEndT(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_end_t(NurbsCurveResult self)
        
        /**
         * Returns the last legal value of t on the curve.
         */
        """
        pass

    def getNumSamples(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_samples(NurbsCurveResult self)
        
        /**
         * Returns the number of sample points generated by the previous call to
         * adaptive_sample().
         */
        """
        pass

    def getNumSegments(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_segments(NurbsCurveResult self)
        
        /**
         * Returns the number of piecewise continuous segments within the curve.  This
         * number is usually not important unless you plan to call
         * eval_segment_point().
         */
        """
        pass

    def getSamplePoint(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_sample_point(NurbsCurveResult self, int n)
        
        /**
         * Returns the point on the curve of the nth sample point generated by the
         * previous call to adaptive_sample().
         *
         * For tangents, or extended points, you should use get_sample_t() and pass it
         * into eval_tangent() or eval_extended_point().
         */
        """
        pass

    def getSamplePoints(self, *args, **kwargs): # real signature unknown
        pass

    def getSampleT(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_sample_t(NurbsCurveResult self, int n)
        
        /**
         * Returns the t value of the nth sample point generated by the previous call
         * to adaptive_sample().
         */
        """
        pass

    def getSampleTs(self, *args, **kwargs): # real signature unknown
        pass

    def getSegmentT(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_segment_t(NurbsCurveResult self, int segment, float t)
        
        /**
         * Accepts a t value in the range [0, 1], and assumed to be relative to the
         * indicated segment (as in eval_segment_point()), and returns the
         * corresponding t value in the entire curve (as in eval_point()).
         */
        """
        pass

    def getStartT(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_start_t(NurbsCurveResult self)
        
        /**
         * Returns the first legal value of t on the curve.  Usually this is 0.0.
         */
        """
        pass

    def get_end_t(self, NurbsCurveResult_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_end_t(NurbsCurveResult self)
        
        /**
         * Returns the last legal value of t on the curve.
         */
        """
        pass

    def get_num_samples(self, NurbsCurveResult_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_samples(NurbsCurveResult self)
        
        /**
         * Returns the number of sample points generated by the previous call to
         * adaptive_sample().
         */
        """
        pass

    def get_num_segments(self, NurbsCurveResult_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_segments(NurbsCurveResult self)
        
        /**
         * Returns the number of piecewise continuous segments within the curve.  This
         * number is usually not important unless you plan to call
         * eval_segment_point().
         */
        """
        pass

    def get_sample_point(self, NurbsCurveResult_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_sample_point(NurbsCurveResult self, int n)
        
        /**
         * Returns the point on the curve of the nth sample point generated by the
         * previous call to adaptive_sample().
         *
         * For tangents, or extended points, you should use get_sample_t() and pass it
         * into eval_tangent() or eval_extended_point().
         */
        """
        pass

    def get_sample_points(self, *args, **kwargs): # real signature unknown
        pass

    def get_sample_t(self, NurbsCurveResult_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_sample_t(NurbsCurveResult self, int n)
        
        /**
         * Returns the t value of the nth sample point generated by the previous call
         * to adaptive_sample().
         */
        """
        pass

    def get_sample_ts(self, *args, **kwargs): # real signature unknown
        pass

    def get_segment_t(self, NurbsCurveResult_self, int_segment, float_t): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_segment_t(NurbsCurveResult self, int segment, float t)
        
        /**
         * Accepts a t value in the range [0, 1], and assumed to be relative to the
         * indicated segment (as in eval_segment_point()), and returns the
         * corresponding t value in the entire curve (as in eval_point()).
         */
        """
        pass

    def get_start_t(self, NurbsCurveResult_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_start_t(NurbsCurveResult self)
        
        /**
         * Returns the first legal value of t on the curve.  Usually this is 0.0.
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
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.NurbsCurveResult' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.NurbsCurveResult' objects>"
        '__doc__': '/**\n * The result of a NurbsCurveEvaluator.  This object represents a curve in a\n * particular coordinate space.  It can return the point and/or tangent to the\n * curve at any point.\n *\n * This is not related to NurbsCurve, CubicCurveseg or any of the\n * ParametricCurve-derived objects in this module.  It is a completely\n * parallel implementation of NURBS curves, and will probably eventually\n * replace the whole ParametricCurve class hierarchy.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.NurbsCurveResult' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE34ED30>'
        'adaptiveSample': None, # (!) real value is "<method 'adaptiveSample' of 'panda3d.core.NurbsCurveResult' objects>"
        'adaptive_sample': None, # (!) real value is "<method 'adaptive_sample' of 'panda3d.core.NurbsCurveResult' objects>"
        'evalExtendedPoint': None, # (!) real value is "<method 'evalExtendedPoint' of 'panda3d.core.NurbsCurveResult' objects>"
        'evalExtendedPoints': None, # (!) real value is "<method 'evalExtendedPoints' of 'panda3d.core.NurbsCurveResult' objects>"
        'evalPoint': None, # (!) real value is "<method 'evalPoint' of 'panda3d.core.NurbsCurveResult' objects>"
        'evalSegmentExtendedPoint': None, # (!) real value is "<method 'evalSegmentExtendedPoint' of 'panda3d.core.NurbsCurveResult' objects>"
        'evalSegmentExtendedPoints': None, # (!) real value is "<method 'evalSegmentExtendedPoints' of 'panda3d.core.NurbsCurveResult' objects>"
        'evalSegmentPoint': None, # (!) real value is "<method 'evalSegmentPoint' of 'panda3d.core.NurbsCurveResult' objects>"
        'evalSegmentTangent': None, # (!) real value is "<method 'evalSegmentTangent' of 'panda3d.core.NurbsCurveResult' objects>"
        'evalTangent': None, # (!) real value is "<method 'evalTangent' of 'panda3d.core.NurbsCurveResult' objects>"
        'eval_extended_point': None, # (!) real value is "<method 'eval_extended_point' of 'panda3d.core.NurbsCurveResult' objects>"
        'eval_extended_points': None, # (!) real value is "<method 'eval_extended_points' of 'panda3d.core.NurbsCurveResult' objects>"
        'eval_point': None, # (!) real value is "<method 'eval_point' of 'panda3d.core.NurbsCurveResult' objects>"
        'eval_segment_extended_point': None, # (!) real value is "<method 'eval_segment_extended_point' of 'panda3d.core.NurbsCurveResult' objects>"
        'eval_segment_extended_points': None, # (!) real value is "<method 'eval_segment_extended_points' of 'panda3d.core.NurbsCurveResult' objects>"
        'eval_segment_point': None, # (!) real value is "<method 'eval_segment_point' of 'panda3d.core.NurbsCurveResult' objects>"
        'eval_segment_tangent': None, # (!) real value is "<method 'eval_segment_tangent' of 'panda3d.core.NurbsCurveResult' objects>"
        'eval_tangent': None, # (!) real value is "<method 'eval_tangent' of 'panda3d.core.NurbsCurveResult' objects>"
        'getEndT': None, # (!) real value is "<method 'getEndT' of 'panda3d.core.NurbsCurveResult' objects>"
        'getNumSamples': None, # (!) real value is "<method 'getNumSamples' of 'panda3d.core.NurbsCurveResult' objects>"
        'getNumSegments': None, # (!) real value is "<method 'getNumSegments' of 'panda3d.core.NurbsCurveResult' objects>"
        'getSamplePoint': None, # (!) real value is "<method 'getSamplePoint' of 'panda3d.core.NurbsCurveResult' objects>"
        'getSamplePoints': None, # (!) real value is "<method 'getSamplePoints' of 'panda3d.core.NurbsCurveResult' objects>"
        'getSampleT': None, # (!) real value is "<method 'getSampleT' of 'panda3d.core.NurbsCurveResult' objects>"
        'getSampleTs': None, # (!) real value is "<method 'getSampleTs' of 'panda3d.core.NurbsCurveResult' objects>"
        'getSegmentT': None, # (!) real value is "<method 'getSegmentT' of 'panda3d.core.NurbsCurveResult' objects>"
        'getStartT': None, # (!) real value is "<method 'getStartT' of 'panda3d.core.NurbsCurveResult' objects>"
        'get_end_t': None, # (!) real value is "<method 'get_end_t' of 'panda3d.core.NurbsCurveResult' objects>"
        'get_num_samples': None, # (!) real value is "<method 'get_num_samples' of 'panda3d.core.NurbsCurveResult' objects>"
        'get_num_segments': None, # (!) real value is "<method 'get_num_segments' of 'panda3d.core.NurbsCurveResult' objects>"
        'get_sample_point': None, # (!) real value is "<method 'get_sample_point' of 'panda3d.core.NurbsCurveResult' objects>"
        'get_sample_points': None, # (!) real value is "<method 'get_sample_points' of 'panda3d.core.NurbsCurveResult' objects>"
        'get_sample_t': None, # (!) real value is "<method 'get_sample_t' of 'panda3d.core.NurbsCurveResult' objects>"
        'get_sample_ts': None, # (!) real value is "<method 'get_sample_ts' of 'panda3d.core.NurbsCurveResult' objects>"
        'get_segment_t': None, # (!) real value is "<method 'get_segment_t' of 'panda3d.core.NurbsCurveResult' objects>"
        'get_start_t': None, # (!) real value is "<method 'get_start_t' of 'panda3d.core.NurbsCurveResult' objects>"
    }


