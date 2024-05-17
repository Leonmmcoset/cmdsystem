# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .ReferenceCount import ReferenceCount

class NurbsCurveEvaluator(ReferenceCount):
    """
    /**
     * This class is an abstraction for evaluating NURBS curves.  It accepts an
     * array of vertices, each of which may be in a different coordinate space (as
     * defined by a NodePath), as well as an optional knot vector.
     *
     * This is not related to NurbsCurve, CubicCurveseg or any of the
     * ParametricCurve-derived objects in this module.  It is a completely
     * parallel implementation of NURBS curves, and will probably eventually
     * replace the whole ParametricCurve class hierarchy.
     */
    """
    def evaluate(self, NurbsCurveEvaluator_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        evaluate(NurbsCurveEvaluator self)
        evaluate(NurbsCurveEvaluator self, const NodePath rel_to)
        evaluate(NurbsCurveEvaluator self, const NodePath rel_to, const LMatrix4f mat)
        
        /**
         * Returns a NurbsCurveResult object that represents the result of applying
         * the knots to all of the current values of the vertices, transformed into
         * the indicated coordinate space.
         */
        
        /**
         * Returns a NurbsCurveResult object that represents the result of applying
         * the knots to all of the current values of the vertices, transformed into
         * the indicated coordinate space, and then further transformed by the
         * indicated matrix.
         */
        """
        pass

    def getExtendedVertex(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_extended_vertex(NurbsCurveEvaluator self, int i, int d)
        
        /**
         * Returns an n-dimensional vertex value.  See set_extended_vertex().  This
         * returns the value set for the indicated dimension, or 0.0 if nothing has
         * been set.
         */
        """
        pass

    def getKnot(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_knot(NurbsCurveEvaluator self, int i)
        
        /**
         * Returns the value of the nth knot.
         */
        """
        pass

    def getKnots(self, *args, **kwargs): # real signature unknown
        pass

    def getNumKnots(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_knots(NurbsCurveEvaluator self)
        
        /**
         * Returns the number of knot values in the curve.  This is based on the
         * number of vertices and the order.
         */
        """
        pass

    def getNumSegments(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_segments(NurbsCurveEvaluator self)
        
        /**
         * Returns the number of piecewise continuous segments in the curve.  This is
         * based on the knot vector.
         */
        """
        pass

    def getNumVertices(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_vertices(NurbsCurveEvaluator self)
        
        /**
         * Returns the number of control vertices in the curve.  This is the number
         * passed to the last call to reset().
         */
        """
        pass

    def getOrder(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_order(NurbsCurveEvaluator self)
        
        /**
         * Returns the order of the curve as set by a previous call to set_order().
         */
        """
        pass

    def getVertex(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_vertex(NurbsCurveEvaluator self, int i)
        get_vertex(NurbsCurveEvaluator self, int i, const NodePath rel_to)
        
        /**
         * Returns the nth control vertex of the curve, relative to its indicated
         * coordinate space.
         */
        
        /**
         * Returns the nth control vertex of the curve, relative to the given
         * coordinate space.
         */
        """
        pass

    def getVertexSpace(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_vertex_space(NurbsCurveEvaluator self, int i, const NodePath rel_to)
        
        /**
         * Returns the coordinate space of the nth control vertex of the curve,
         * expressed as a NodePath.
         */
        """
        pass

    def getVertices(self, *args, **kwargs): # real signature unknown
        pass

    def get_extended_vertex(self, NurbsCurveEvaluator_self, int_i, int_d): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_extended_vertex(NurbsCurveEvaluator self, int i, int d)
        
        /**
         * Returns an n-dimensional vertex value.  See set_extended_vertex().  This
         * returns the value set for the indicated dimension, or 0.0 if nothing has
         * been set.
         */
        """
        pass

    def get_knot(self, NurbsCurveEvaluator_self, int_i): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_knot(NurbsCurveEvaluator self, int i)
        
        /**
         * Returns the value of the nth knot.
         */
        """
        pass

    def get_knots(self, *args, **kwargs): # real signature unknown
        pass

    def get_num_knots(self, NurbsCurveEvaluator_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_knots(NurbsCurveEvaluator self)
        
        /**
         * Returns the number of knot values in the curve.  This is based on the
         * number of vertices and the order.
         */
        """
        pass

    def get_num_segments(self, NurbsCurveEvaluator_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_segments(NurbsCurveEvaluator self)
        
        /**
         * Returns the number of piecewise continuous segments in the curve.  This is
         * based on the knot vector.
         */
        """
        pass

    def get_num_vertices(self, NurbsCurveEvaluator_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_vertices(NurbsCurveEvaluator self)
        
        /**
         * Returns the number of control vertices in the curve.  This is the number
         * passed to the last call to reset().
         */
        """
        pass

    def get_order(self, NurbsCurveEvaluator_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_order(NurbsCurveEvaluator self)
        
        /**
         * Returns the order of the curve as set by a previous call to set_order().
         */
        """
        pass

    def get_vertex(self, NurbsCurveEvaluator_self, int_i): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_vertex(NurbsCurveEvaluator self, int i)
        get_vertex(NurbsCurveEvaluator self, int i, const NodePath rel_to)
        
        /**
         * Returns the nth control vertex of the curve, relative to its indicated
         * coordinate space.
         */
        
        /**
         * Returns the nth control vertex of the curve, relative to the given
         * coordinate space.
         */
        """
        pass

    def get_vertex_space(self, NurbsCurveEvaluator_self, int_i, const_NodePath_rel_to): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_vertex_space(NurbsCurveEvaluator self, int i, const NodePath rel_to)
        
        /**
         * Returns the coordinate space of the nth control vertex of the curve,
         * expressed as a NodePath.
         */
        """
        pass

    def get_vertices(self, *args, **kwargs): # real signature unknown
        pass

    def normalizeKnots(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        normalize_knots(const NurbsCurveEvaluator self)
        
        /**
         * Normalizes the knot sequence so that the parametric range of the curve is 0
         * .. 1.
         */
        """
        pass

    def normalize_knots(self, const_NurbsCurveEvaluator_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        normalize_knots(const NurbsCurveEvaluator self)
        
        /**
         * Normalizes the knot sequence so that the parametric range of the curve is 0
         * .. 1.
         */
        """
        pass

    def output(self, NurbsCurveEvaluator_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(NurbsCurveEvaluator self, ostream out)
        
        /**
         *
         */
        """
        pass

    def reset(self, const_NurbsCurveEvaluator_self, int_num_vertices): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        reset(const NurbsCurveEvaluator self, int num_vertices)
        
        /**
         * Resets all the vertices and knots to their default values, and sets the
         * curve up with the indicated number of vertices.  You must then call
         * set_vertex() repeatedly to fill in all of the vertex values appropriately.
         */
        """
        pass

    def setExtendedVertex(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_extended_vertex(const NurbsCurveEvaluator self, int i, int d, float value)
        
        /**
         * Sets an n-dimensional vertex value.  This allows definition of a NURBS
         * surface or curve in a sparse n-dimensional space, typically used for
         * associating additional properties (like color or joint membership) with
         * each vertex of a surface.
         *
         * The value d is an arbitrary integer value and specifies the dimension of
         * question for this particular vertex.  Any number of dimensions may be
         * specified, and they need not be consecutive.  If a value for a given
         * dimension is not specified, is it implicitly 0.0.
         *
         * The value is implicitly scaled by the homogenous weight value--that is, the
         * fourth component of the value passed to set_vertex().  This means the
         * ordinary vertex must be set first, before the extended vertices can be set.
         */
        """
        pass

    def setExtendedVertices(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_extended_vertices(const NurbsCurveEvaluator self, int i, int d, buffer values, int num_values)
        
        /**
         * Simultaneously sets several extended values in the slots d through (d +
         * num_values - 1) from the num_values elements of the indicated array.  This
         * is equivalent to calling set_extended_vertex() num_values times.  See
         * set_extended_vertex().
         */
        """
        pass

    def setKnot(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_knot(const NurbsCurveEvaluator self, int i, float knot)
        
        /**
         * Sets the value of the nth knot.  Each knot value should be greater than or
         * equal to the preceding value.  If no knot values are set, a default knot
         * vector is supplied.
         */
        """
        pass

    def setOrder(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_order(const NurbsCurveEvaluator self, int order)
        
        /**
         * Sets the order of the curve.  This resets the knot vector to the default
         * knot vector for the number of vertices.
         *
         * The order must be 1, 2, 3, or 4, and the value is one more than the degree
         * of the curve.
         */
        """
        pass

    def setVertex(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_vertex(const NurbsCurveEvaluator self, int i, const LVecBase3f vertex, float weight)
        set_vertex(const NurbsCurveEvaluator self, int i, const LVecBase4f vertex)
        
        /**
         * Sets the nth control vertex of the curve, as a vertex in 4-d homogeneous
         * space.  In this form, the first three components of the vertex should
         * already have been scaled by the fourth component, which is the homogeneous
         * weight.
         */
        
        /**
         * Sets the nth control vertex of the curve.  This flavor sets the vertex as a
         * 3-d coordinate and a weight; the 3-d coordinate values are implicitly
         * scaled up by the weight factor.
         */
        """
        pass

    def setVertexSpace(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_vertex_space(const NurbsCurveEvaluator self, int i, const NodePath space)
        set_vertex_space(const NurbsCurveEvaluator self, int i, str space)
        
        /**
         * Sets the coordinate space of the nth control vertex.  If this is not
         * specified, or is set to an empty NodePath, the nth control vertex is deemed
         * to be in the coordinate space passed to evaluate().
         *
         * This specifies the space as a fixed NodePath, which is always the same
         * NodePath.  Also see setting the space as a path string, which can specify a
         * different NodePath for different instances of the curve.
         */
        
        /**
         * Sets the coordinate space of the nth control vertex.  If this is not
         * specified, or is set to an empty string, the nth control vertex is deemed
         * to be in the coordinate space passed to evaluate().
         *
         * This specifies the space as a string, which describes the path to find the
         * node relative to the rel_to NodePath when the curve is evaluated.
         */
        """
        pass

    def set_extended_vertex(self, const_NurbsCurveEvaluator_self, int_i, int_d, float_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_extended_vertex(const NurbsCurveEvaluator self, int i, int d, float value)
        
        /**
         * Sets an n-dimensional vertex value.  This allows definition of a NURBS
         * surface or curve in a sparse n-dimensional space, typically used for
         * associating additional properties (like color or joint membership) with
         * each vertex of a surface.
         *
         * The value d is an arbitrary integer value and specifies the dimension of
         * question for this particular vertex.  Any number of dimensions may be
         * specified, and they need not be consecutive.  If a value for a given
         * dimension is not specified, is it implicitly 0.0.
         *
         * The value is implicitly scaled by the homogenous weight value--that is, the
         * fourth component of the value passed to set_vertex().  This means the
         * ordinary vertex must be set first, before the extended vertices can be set.
         */
        """
        pass

    def set_extended_vertices(self, const_NurbsCurveEvaluator_self, int_i, int_d, buffer_values, int_num_values): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_extended_vertices(const NurbsCurveEvaluator self, int i, int d, buffer values, int num_values)
        
        /**
         * Simultaneously sets several extended values in the slots d through (d +
         * num_values - 1) from the num_values elements of the indicated array.  This
         * is equivalent to calling set_extended_vertex() num_values times.  See
         * set_extended_vertex().
         */
        """
        pass

    def set_knot(self, const_NurbsCurveEvaluator_self, int_i, float_knot): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_knot(const NurbsCurveEvaluator self, int i, float knot)
        
        /**
         * Sets the value of the nth knot.  Each knot value should be greater than or
         * equal to the preceding value.  If no knot values are set, a default knot
         * vector is supplied.
         */
        """
        pass

    def set_order(self, const_NurbsCurveEvaluator_self, int_order): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_order(const NurbsCurveEvaluator self, int order)
        
        /**
         * Sets the order of the curve.  This resets the knot vector to the default
         * knot vector for the number of vertices.
         *
         * The order must be 1, 2, 3, or 4, and the value is one more than the degree
         * of the curve.
         */
        """
        pass

    def set_vertex(self, const_NurbsCurveEvaluator_self, int_i, const_LVecBase3f_vertex, float_weight): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_vertex(const NurbsCurveEvaluator self, int i, const LVecBase3f vertex, float weight)
        set_vertex(const NurbsCurveEvaluator self, int i, const LVecBase4f vertex)
        
        /**
         * Sets the nth control vertex of the curve, as a vertex in 4-d homogeneous
         * space.  In this form, the first three components of the vertex should
         * already have been scaled by the fourth component, which is the homogeneous
         * weight.
         */
        
        /**
         * Sets the nth control vertex of the curve.  This flavor sets the vertex as a
         * 3-d coordinate and a weight; the 3-d coordinate values are implicitly
         * scaled up by the weight factor.
         */
        """
        pass

    def set_vertex_space(self, const_NurbsCurveEvaluator_self, int_i, const_NodePath_space): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_vertex_space(const NurbsCurveEvaluator self, int i, const NodePath space)
        set_vertex_space(const NurbsCurveEvaluator self, int i, str space)
        
        /**
         * Sets the coordinate space of the nth control vertex.  If this is not
         * specified, or is set to an empty NodePath, the nth control vertex is deemed
         * to be in the coordinate space passed to evaluate().
         *
         * This specifies the space as a fixed NodePath, which is always the same
         * NodePath.  Also see setting the space as a path string, which can specify a
         * different NodePath for different instances of the curve.
         */
        
        /**
         * Sets the coordinate space of the nth control vertex.  If this is not
         * specified, or is set to an empty string, the nth control vertex is deemed
         * to be in the coordinate space passed to evaluate().
         *
         * This specifies the space as a string, which describes the path to find the
         * node relative to the rel_to NodePath when the curve is evaluated.
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

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.NurbsCurveEvaluator' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.NurbsCurveEvaluator' objects>"
        '__doc__': '/**\n * This class is an abstraction for evaluating NURBS curves.  It accepts an\n * array of vertices, each of which may be in a different coordinate space (as\n * defined by a NodePath), as well as an optional knot vector.\n *\n * This is not related to NurbsCurve, CubicCurveseg or any of the\n * ParametricCurve-derived objects in this module.  It is a completely\n * parallel implementation of NURBS curves, and will probably eventually\n * replace the whole ParametricCurve class hierarchy.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.NurbsCurveEvaluator' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE34EF00>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.NurbsCurveEvaluator' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.NurbsCurveEvaluator' objects>"
        'evaluate': None, # (!) real value is "<method 'evaluate' of 'panda3d.core.NurbsCurveEvaluator' objects>"
        'getExtendedVertex': None, # (!) real value is "<method 'getExtendedVertex' of 'panda3d.core.NurbsCurveEvaluator' objects>"
        'getKnot': None, # (!) real value is "<method 'getKnot' of 'panda3d.core.NurbsCurveEvaluator' objects>"
        'getKnots': None, # (!) real value is "<method 'getKnots' of 'panda3d.core.NurbsCurveEvaluator' objects>"
        'getNumKnots': None, # (!) real value is "<method 'getNumKnots' of 'panda3d.core.NurbsCurveEvaluator' objects>"
        'getNumSegments': None, # (!) real value is "<method 'getNumSegments' of 'panda3d.core.NurbsCurveEvaluator' objects>"
        'getNumVertices': None, # (!) real value is "<method 'getNumVertices' of 'panda3d.core.NurbsCurveEvaluator' objects>"
        'getOrder': None, # (!) real value is "<method 'getOrder' of 'panda3d.core.NurbsCurveEvaluator' objects>"
        'getVertex': None, # (!) real value is "<method 'getVertex' of 'panda3d.core.NurbsCurveEvaluator' objects>"
        'getVertexSpace': None, # (!) real value is "<method 'getVertexSpace' of 'panda3d.core.NurbsCurveEvaluator' objects>"
        'getVertices': None, # (!) real value is "<method 'getVertices' of 'panda3d.core.NurbsCurveEvaluator' objects>"
        'get_extended_vertex': None, # (!) real value is "<method 'get_extended_vertex' of 'panda3d.core.NurbsCurveEvaluator' objects>"
        'get_knot': None, # (!) real value is "<method 'get_knot' of 'panda3d.core.NurbsCurveEvaluator' objects>"
        'get_knots': None, # (!) real value is "<method 'get_knots' of 'panda3d.core.NurbsCurveEvaluator' objects>"
        'get_num_knots': None, # (!) real value is "<method 'get_num_knots' of 'panda3d.core.NurbsCurveEvaluator' objects>"
        'get_num_segments': None, # (!) real value is "<method 'get_num_segments' of 'panda3d.core.NurbsCurveEvaluator' objects>"
        'get_num_vertices': None, # (!) real value is "<method 'get_num_vertices' of 'panda3d.core.NurbsCurveEvaluator' objects>"
        'get_order': None, # (!) real value is "<method 'get_order' of 'panda3d.core.NurbsCurveEvaluator' objects>"
        'get_vertex': None, # (!) real value is "<method 'get_vertex' of 'panda3d.core.NurbsCurveEvaluator' objects>"
        'get_vertex_space': None, # (!) real value is "<method 'get_vertex_space' of 'panda3d.core.NurbsCurveEvaluator' objects>"
        'get_vertices': None, # (!) real value is "<method 'get_vertices' of 'panda3d.core.NurbsCurveEvaluator' objects>"
        'normalizeKnots': None, # (!) real value is "<method 'normalizeKnots' of 'panda3d.core.NurbsCurveEvaluator' objects>"
        'normalize_knots': None, # (!) real value is "<method 'normalize_knots' of 'panda3d.core.NurbsCurveEvaluator' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.NurbsCurveEvaluator' objects>"
        'reset': None, # (!) real value is "<method 'reset' of 'panda3d.core.NurbsCurveEvaluator' objects>"
        'setExtendedVertex': None, # (!) real value is "<method 'setExtendedVertex' of 'panda3d.core.NurbsCurveEvaluator' objects>"
        'setExtendedVertices': None, # (!) real value is "<method 'setExtendedVertices' of 'panda3d.core.NurbsCurveEvaluator' objects>"
        'setKnot': None, # (!) real value is "<method 'setKnot' of 'panda3d.core.NurbsCurveEvaluator' objects>"
        'setOrder': None, # (!) real value is "<method 'setOrder' of 'panda3d.core.NurbsCurveEvaluator' objects>"
        'setVertex': None, # (!) real value is "<method 'setVertex' of 'panda3d.core.NurbsCurveEvaluator' objects>"
        'setVertexSpace': None, # (!) real value is "<method 'setVertexSpace' of 'panda3d.core.NurbsCurveEvaluator' objects>"
        'set_extended_vertex': None, # (!) real value is "<method 'set_extended_vertex' of 'panda3d.core.NurbsCurveEvaluator' objects>"
        'set_extended_vertices': None, # (!) real value is "<method 'set_extended_vertices' of 'panda3d.core.NurbsCurveEvaluator' objects>"
        'set_knot': None, # (!) real value is "<method 'set_knot' of 'panda3d.core.NurbsCurveEvaluator' objects>"
        'set_order': None, # (!) real value is "<method 'set_order' of 'panda3d.core.NurbsCurveEvaluator' objects>"
        'set_vertex': None, # (!) real value is "<method 'set_vertex' of 'panda3d.core.NurbsCurveEvaluator' objects>"
        'set_vertex_space': None, # (!) real value is "<method 'set_vertex_space' of 'panda3d.core.NurbsCurveEvaluator' objects>"
    }


