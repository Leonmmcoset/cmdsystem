# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .ReferenceCount import ReferenceCount

class NurbsSurfaceEvaluator(ReferenceCount):
    """
    /**
     * This class is an abstraction for evaluating NURBS surfaces.  It accepts an
     * array of vertices, each of which may be in a different coordinate space (as
     * defined by a NodePath), as well as an optional knot vector.
     */
    """
    def evaluate(self, NurbsSurfaceEvaluator_self, const_NodePath_rel_to): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        evaluate(NurbsSurfaceEvaluator self, const NodePath rel_to)
        
        /**
         * Returns a NurbsSurfaceResult object that represents the result of applying
         * the knots to all of the current values of the vertices, transformed into
         * the indicated coordinate space.
         */
        """
        pass

    def getExtendedVertex(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_extended_vertex(NurbsSurfaceEvaluator self, int ui, int vi, int d)
        
        /**
         * Returns an n-dimensional vertex value.  See set_extended_vertex().  This
         * returns the value set for the indicated dimension, or 0.0 if nothing has
         * been set.
         */
        """
        pass

    def getNumUKnots(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_u_knots(NurbsSurfaceEvaluator self)
        
        /**
         * Returns the number of knot values in the surface in the U direction.  This
         * is based on the number of vertices and the order.
         */
        """
        pass

    def getNumUSegments(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_u_segments(NurbsSurfaceEvaluator self)
        
        /**
         * Returns the number of piecewise continuous segments in the surface in the U
         * direction.  This is based on the knot vector.
         */
        """
        pass

    def getNumUVertices(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_u_vertices(NurbsSurfaceEvaluator self)
        
        /**
         * Returns the number of control vertices in the U direction on the surface.
         * This is the number passed to the last call to reset().
         */
        """
        pass

    def getNumVKnots(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_v_knots(NurbsSurfaceEvaluator self)
        
        /**
         * Returns the number of knot values in the surface in the V direction.  This
         * is based on the number of vertices and the order.
         */
        """
        pass

    def getNumVSegments(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_v_segments(NurbsSurfaceEvaluator self)
        
        /**
         * Returns the number of piecewise continuous segments in the surface in the V
         * direction.  This is based on the knot vector.
         */
        """
        pass

    def getNumVVertices(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_v_vertices(NurbsSurfaceEvaluator self)
        
        /**
         * Returns the number of control vertices in the V direction on the surface.
         * This is the number passed to the last call to reset().
         */
        """
        pass

    def getUKnot(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_u_knot(NurbsSurfaceEvaluator self, int i)
        
        /**
         * Returns the value of the nth knot.
         */
        """
        pass

    def getUKnots(self, *args, **kwargs): # real signature unknown
        pass

    def getUOrder(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_u_order(NurbsSurfaceEvaluator self)
        
        /**
         * Returns the order of the surface in the U direction as set by a previous
         * call to set_u_order().
         */
        """
        pass

    def getVertex(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_vertex(NurbsSurfaceEvaluator self, int ui, int vi)
        get_vertex(NurbsSurfaceEvaluator self, int ui, int vi, const NodePath rel_to)
        
        /**
         * Returns the nth control vertex of the surface, relative to its indicated
         * coordinate space.
         */
        
        /**
         * Returns the nth control vertex of the surface, relative to the given
         * coordinate space.
         */
        """
        pass

    def getVertexSpace(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_vertex_space(NurbsSurfaceEvaluator self, int ui, int vi, const NodePath rel_to)
        
        /**
         * Returns the coordinate space of the nth control vertex of the surface,
         * expressed as a NodePath.
         */
        """
        pass

    def getVKnot(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_v_knot(NurbsSurfaceEvaluator self, int i)
        
        /**
         * Returns the value of the nth knot.
         */
        """
        pass

    def getVKnots(self, *args, **kwargs): # real signature unknown
        pass

    def getVOrder(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_v_order(NurbsSurfaceEvaluator self)
        
        /**
         * Returns the order of the surface in the V direction as set by a previous
         * call to set_v_order().
         */
        """
        pass

    def get_extended_vertex(self, NurbsSurfaceEvaluator_self, int_ui, int_vi, int_d): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_extended_vertex(NurbsSurfaceEvaluator self, int ui, int vi, int d)
        
        /**
         * Returns an n-dimensional vertex value.  See set_extended_vertex().  This
         * returns the value set for the indicated dimension, or 0.0 if nothing has
         * been set.
         */
        """
        pass

    def get_num_u_knots(self, NurbsSurfaceEvaluator_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_u_knots(NurbsSurfaceEvaluator self)
        
        /**
         * Returns the number of knot values in the surface in the U direction.  This
         * is based on the number of vertices and the order.
         */
        """
        pass

    def get_num_u_segments(self, NurbsSurfaceEvaluator_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_u_segments(NurbsSurfaceEvaluator self)
        
        /**
         * Returns the number of piecewise continuous segments in the surface in the U
         * direction.  This is based on the knot vector.
         */
        """
        pass

    def get_num_u_vertices(self, NurbsSurfaceEvaluator_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_u_vertices(NurbsSurfaceEvaluator self)
        
        /**
         * Returns the number of control vertices in the U direction on the surface.
         * This is the number passed to the last call to reset().
         */
        """
        pass

    def get_num_v_knots(self, NurbsSurfaceEvaluator_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_v_knots(NurbsSurfaceEvaluator self)
        
        /**
         * Returns the number of knot values in the surface in the V direction.  This
         * is based on the number of vertices and the order.
         */
        """
        pass

    def get_num_v_segments(self, NurbsSurfaceEvaluator_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_v_segments(NurbsSurfaceEvaluator self)
        
        /**
         * Returns the number of piecewise continuous segments in the surface in the V
         * direction.  This is based on the knot vector.
         */
        """
        pass

    def get_num_v_vertices(self, NurbsSurfaceEvaluator_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_v_vertices(NurbsSurfaceEvaluator self)
        
        /**
         * Returns the number of control vertices in the V direction on the surface.
         * This is the number passed to the last call to reset().
         */
        """
        pass

    def get_u_knot(self, NurbsSurfaceEvaluator_self, int_i): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_u_knot(NurbsSurfaceEvaluator self, int i)
        
        /**
         * Returns the value of the nth knot.
         */
        """
        pass

    def get_u_knots(self, *args, **kwargs): # real signature unknown
        pass

    def get_u_order(self, NurbsSurfaceEvaluator_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_u_order(NurbsSurfaceEvaluator self)
        
        /**
         * Returns the order of the surface in the U direction as set by a previous
         * call to set_u_order().
         */
        """
        pass

    def get_vertex(self, NurbsSurfaceEvaluator_self, int_ui, int_vi): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_vertex(NurbsSurfaceEvaluator self, int ui, int vi)
        get_vertex(NurbsSurfaceEvaluator self, int ui, int vi, const NodePath rel_to)
        
        /**
         * Returns the nth control vertex of the surface, relative to its indicated
         * coordinate space.
         */
        
        /**
         * Returns the nth control vertex of the surface, relative to the given
         * coordinate space.
         */
        """
        pass

    def get_vertex_space(self, NurbsSurfaceEvaluator_self, int_ui, int_vi, const_NodePath_rel_to): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_vertex_space(NurbsSurfaceEvaluator self, int ui, int vi, const NodePath rel_to)
        
        /**
         * Returns the coordinate space of the nth control vertex of the surface,
         * expressed as a NodePath.
         */
        """
        pass

    def get_v_knot(self, NurbsSurfaceEvaluator_self, int_i): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_v_knot(NurbsSurfaceEvaluator self, int i)
        
        /**
         * Returns the value of the nth knot.
         */
        """
        pass

    def get_v_knots(self, *args, **kwargs): # real signature unknown
        pass

    def get_v_order(self, NurbsSurfaceEvaluator_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_v_order(NurbsSurfaceEvaluator self)
        
        /**
         * Returns the order of the surface in the V direction as set by a previous
         * call to set_v_order().
         */
        """
        pass

    def normalizeUKnots(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        normalize_u_knots(const NurbsSurfaceEvaluator self)
        
        /**
         * Normalizes the knot sequence so that the parametric range of the surface in
         * the U direction is 0 .. 1.
         */
        """
        pass

    def normalizeVKnots(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        normalize_v_knots(const NurbsSurfaceEvaluator self)
        
        /**
         * Normalizes the knot sequence so that the parametric range of the surface in
         * the U direction is 0 .. 1.
         */
        """
        pass

    def normalize_u_knots(self, const_NurbsSurfaceEvaluator_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        normalize_u_knots(const NurbsSurfaceEvaluator self)
        
        /**
         * Normalizes the knot sequence so that the parametric range of the surface in
         * the U direction is 0 .. 1.
         */
        """
        pass

    def normalize_v_knots(self, const_NurbsSurfaceEvaluator_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        normalize_v_knots(const NurbsSurfaceEvaluator self)
        
        /**
         * Normalizes the knot sequence so that the parametric range of the surface in
         * the U direction is 0 .. 1.
         */
        """
        pass

    def output(self, NurbsSurfaceEvaluator_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(NurbsSurfaceEvaluator self, ostream out)
        
        /**
         *
         */
        """
        pass

    def reset(self, const_NurbsSurfaceEvaluator_self, int_num_u_vertices, int_num_v_vertices): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        reset(const NurbsSurfaceEvaluator self, int num_u_vertices, int num_v_vertices)
        
        /**
         * Resets all the vertices and knots to their default values, and sets the
         * surface up with the indicated number of vertices.  You must then call
         * set_vertex() repeatedly to fill in all of the vertex values appropriately.
         */
        """
        pass

    def setExtendedVertex(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_extended_vertex(const NurbsSurfaceEvaluator self, int ui, int vi, int d, float value)
        
        /**
         * Sets an n-dimensional vertex value.  This allows definition of a NURBS
         * surface or surface in a sparse n-dimensional space, typically used for
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
        set_extended_vertices(const NurbsSurfaceEvaluator self, int ui, int vi, int d, buffer values, int num_values)
        
        /**
         * Simultaneously sets several extended values in the slots d through (d +
         * num_values - 1) from the num_values elements of the indicated array.  This
         * is equivalent to calling set_extended_vertex() num_values times.  See
         * set_extended_vertex().
         */
        """
        pass

    def setUKnot(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_u_knot(const NurbsSurfaceEvaluator self, int i, float knot)
        
        /**
         * Sets the value of the nth knot.  Each knot value should be greater than or
         * equal to the preceding value.  If no knot values are set, a default knot
         * vector is supplied.
         */
        """
        pass

    def setUOrder(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_u_order(const NurbsSurfaceEvaluator self, int u_order)
        
        /**
         * Sets the order of the surface in the U direction.  This resets the knot
         * vector to the default knot vector for the number of vertices.
         *
         * The order must be 1, 2, 3, or 4, and the value is one more than the degree
         * of the surface.
         */
        """
        pass

    def setVertex(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_vertex(const NurbsSurfaceEvaluator self, int ui, int vi, const LVecBase3f vertex, float weight)
        set_vertex(const NurbsSurfaceEvaluator self, int ui, int vi, const LVecBase4f vertex)
        
        /**
         * Sets the nth control vertex of the surface, as a vertex in 4-d homogeneous
         * space.  In this form, the first three components of the vertex should
         * already have been scaled by the fourth component, which is the homogeneous
         * weight.
         */
        
        /**
         * Sets the nth control vertex of the surface.  This flavor sets the vertex as
         * a 3-d coordinate and a weight; the 3-d coordinate values are implicitly
         * scaled up by the weight factor.
         */
        """
        pass

    def setVertexSpace(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_vertex_space(const NurbsSurfaceEvaluator self, int ui, int vi, const NodePath space)
        set_vertex_space(const NurbsSurfaceEvaluator self, int ui, int vi, str space)
        
        /**
         * Sets the coordinate space of the nth control vertex.  If this is not
         * specified, or is set to an empty NodePath, the nth control vertex is deemed
         * to be in the coordinate space passed to evaluate().
         *
         * This specifies the space as a fixed NodePath, which is always the same
         * NodePath.  Also see setting the space as a path string, which can specify a
         * different NodePath for different instances of the surface.
         */
        
        /**
         * Sets the coordinate space of the nth control vertex.  If this is not
         * specified, or is set to an empty string, the nth control vertex is deemed
         * to be in the coordinate space passed to evaluate().
         *
         * This specifies the space as a string, which describes the path to find the
         * node relative to the rel_to NodePath when the surface is evaluated.
         */
        """
        pass

    def setVKnot(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_v_knot(const NurbsSurfaceEvaluator self, int i, float knot)
        
        /**
         * Sets the value of the nth knot.  Each knot value should be greater than or
         * equal to the preceding value.  If no knot values are set, a default knot
         * vector is supplied.
         */
        """
        pass

    def setVOrder(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_v_order(const NurbsSurfaceEvaluator self, int v_order)
        
        /**
         * Sets the order of the surface in the V direction.  This resets the knot
         * vector to the default knot vector for the number of vertices.
         *
         * The order must be 1, 2, 3, or 4, and the value is one more than the degree
         * of the surface.
         */
        """
        pass

    def set_extended_vertex(self, const_NurbsSurfaceEvaluator_self, int_ui, int_vi, int_d, float_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_extended_vertex(const NurbsSurfaceEvaluator self, int ui, int vi, int d, float value)
        
        /**
         * Sets an n-dimensional vertex value.  This allows definition of a NURBS
         * surface or surface in a sparse n-dimensional space, typically used for
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

    def set_extended_vertices(self, const_NurbsSurfaceEvaluator_self, int_ui, int_vi, int_d, buffer_values, int_num_values): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_extended_vertices(const NurbsSurfaceEvaluator self, int ui, int vi, int d, buffer values, int num_values)
        
        /**
         * Simultaneously sets several extended values in the slots d through (d +
         * num_values - 1) from the num_values elements of the indicated array.  This
         * is equivalent to calling set_extended_vertex() num_values times.  See
         * set_extended_vertex().
         */
        """
        pass

    def set_u_knot(self, const_NurbsSurfaceEvaluator_self, int_i, float_knot): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_u_knot(const NurbsSurfaceEvaluator self, int i, float knot)
        
        /**
         * Sets the value of the nth knot.  Each knot value should be greater than or
         * equal to the preceding value.  If no knot values are set, a default knot
         * vector is supplied.
         */
        """
        pass

    def set_u_order(self, const_NurbsSurfaceEvaluator_self, int_u_order): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_u_order(const NurbsSurfaceEvaluator self, int u_order)
        
        /**
         * Sets the order of the surface in the U direction.  This resets the knot
         * vector to the default knot vector for the number of vertices.
         *
         * The order must be 1, 2, 3, or 4, and the value is one more than the degree
         * of the surface.
         */
        """
        pass

    def set_vertex(self, const_NurbsSurfaceEvaluator_self, int_ui, int_vi, const_LVecBase3f_vertex, float_weight): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_vertex(const NurbsSurfaceEvaluator self, int ui, int vi, const LVecBase3f vertex, float weight)
        set_vertex(const NurbsSurfaceEvaluator self, int ui, int vi, const LVecBase4f vertex)
        
        /**
         * Sets the nth control vertex of the surface, as a vertex in 4-d homogeneous
         * space.  In this form, the first three components of the vertex should
         * already have been scaled by the fourth component, which is the homogeneous
         * weight.
         */
        
        /**
         * Sets the nth control vertex of the surface.  This flavor sets the vertex as
         * a 3-d coordinate and a weight; the 3-d coordinate values are implicitly
         * scaled up by the weight factor.
         */
        """
        pass

    def set_vertex_space(self, const_NurbsSurfaceEvaluator_self, int_ui, int_vi, const_NodePath_space): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_vertex_space(const NurbsSurfaceEvaluator self, int ui, int vi, const NodePath space)
        set_vertex_space(const NurbsSurfaceEvaluator self, int ui, int vi, str space)
        
        /**
         * Sets the coordinate space of the nth control vertex.  If this is not
         * specified, or is set to an empty NodePath, the nth control vertex is deemed
         * to be in the coordinate space passed to evaluate().
         *
         * This specifies the space as a fixed NodePath, which is always the same
         * NodePath.  Also see setting the space as a path string, which can specify a
         * different NodePath for different instances of the surface.
         */
        
        /**
         * Sets the coordinate space of the nth control vertex.  If this is not
         * specified, or is set to an empty string, the nth control vertex is deemed
         * to be in the coordinate space passed to evaluate().
         *
         * This specifies the space as a string, which describes the path to find the
         * node relative to the rel_to NodePath when the surface is evaluated.
         */
        """
        pass

    def set_v_knot(self, const_NurbsSurfaceEvaluator_self, int_i, float_knot): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_v_knot(const NurbsSurfaceEvaluator self, int i, float knot)
        
        /**
         * Sets the value of the nth knot.  Each knot value should be greater than or
         * equal to the preceding value.  If no knot values are set, a default knot
         * vector is supplied.
         */
        """
        pass

    def set_v_order(self, const_NurbsSurfaceEvaluator_self, int_v_order): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_v_order(const NurbsSurfaceEvaluator self, int v_order)
        
        /**
         * Sets the order of the surface in the V direction.  This resets the knot
         * vector to the default knot vector for the number of vertices.
         *
         * The order must be 1, 2, 3, or 4, and the value is one more than the degree
         * of the surface.
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

    u_knots = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    u_order = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    v_knots = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    v_order = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.NurbsSurfaceEvaluator' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.NurbsSurfaceEvaluator' objects>"
        '__doc__': '/**\n * This class is an abstraction for evaluating NURBS surfaces.  It accepts an\n * array of vertices, each of which may be in a different coordinate space (as\n * defined by a NodePath), as well as an optional knot vector.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.NurbsSurfaceEvaluator' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE34F2A0>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.NurbsSurfaceEvaluator' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.NurbsSurfaceEvaluator' objects>"
        'evaluate': None, # (!) real value is "<method 'evaluate' of 'panda3d.core.NurbsSurfaceEvaluator' objects>"
        'getExtendedVertex': None, # (!) real value is "<method 'getExtendedVertex' of 'panda3d.core.NurbsSurfaceEvaluator' objects>"
        'getNumUKnots': None, # (!) real value is "<method 'getNumUKnots' of 'panda3d.core.NurbsSurfaceEvaluator' objects>"
        'getNumUSegments': None, # (!) real value is "<method 'getNumUSegments' of 'panda3d.core.NurbsSurfaceEvaluator' objects>"
        'getNumUVertices': None, # (!) real value is "<method 'getNumUVertices' of 'panda3d.core.NurbsSurfaceEvaluator' objects>"
        'getNumVKnots': None, # (!) real value is "<method 'getNumVKnots' of 'panda3d.core.NurbsSurfaceEvaluator' objects>"
        'getNumVSegments': None, # (!) real value is "<method 'getNumVSegments' of 'panda3d.core.NurbsSurfaceEvaluator' objects>"
        'getNumVVertices': None, # (!) real value is "<method 'getNumVVertices' of 'panda3d.core.NurbsSurfaceEvaluator' objects>"
        'getUKnot': None, # (!) real value is "<method 'getUKnot' of 'panda3d.core.NurbsSurfaceEvaluator' objects>"
        'getUKnots': None, # (!) real value is "<method 'getUKnots' of 'panda3d.core.NurbsSurfaceEvaluator' objects>"
        'getUOrder': None, # (!) real value is "<method 'getUOrder' of 'panda3d.core.NurbsSurfaceEvaluator' objects>"
        'getVKnot': None, # (!) real value is "<method 'getVKnot' of 'panda3d.core.NurbsSurfaceEvaluator' objects>"
        'getVKnots': None, # (!) real value is "<method 'getVKnots' of 'panda3d.core.NurbsSurfaceEvaluator' objects>"
        'getVOrder': None, # (!) real value is "<method 'getVOrder' of 'panda3d.core.NurbsSurfaceEvaluator' objects>"
        'getVertex': None, # (!) real value is "<method 'getVertex' of 'panda3d.core.NurbsSurfaceEvaluator' objects>"
        'getVertexSpace': None, # (!) real value is "<method 'getVertexSpace' of 'panda3d.core.NurbsSurfaceEvaluator' objects>"
        'get_extended_vertex': None, # (!) real value is "<method 'get_extended_vertex' of 'panda3d.core.NurbsSurfaceEvaluator' objects>"
        'get_num_u_knots': None, # (!) real value is "<method 'get_num_u_knots' of 'panda3d.core.NurbsSurfaceEvaluator' objects>"
        'get_num_u_segments': None, # (!) real value is "<method 'get_num_u_segments' of 'panda3d.core.NurbsSurfaceEvaluator' objects>"
        'get_num_u_vertices': None, # (!) real value is "<method 'get_num_u_vertices' of 'panda3d.core.NurbsSurfaceEvaluator' objects>"
        'get_num_v_knots': None, # (!) real value is "<method 'get_num_v_knots' of 'panda3d.core.NurbsSurfaceEvaluator' objects>"
        'get_num_v_segments': None, # (!) real value is "<method 'get_num_v_segments' of 'panda3d.core.NurbsSurfaceEvaluator' objects>"
        'get_num_v_vertices': None, # (!) real value is "<method 'get_num_v_vertices' of 'panda3d.core.NurbsSurfaceEvaluator' objects>"
        'get_u_knot': None, # (!) real value is "<method 'get_u_knot' of 'panda3d.core.NurbsSurfaceEvaluator' objects>"
        'get_u_knots': None, # (!) real value is "<method 'get_u_knots' of 'panda3d.core.NurbsSurfaceEvaluator' objects>"
        'get_u_order': None, # (!) real value is "<method 'get_u_order' of 'panda3d.core.NurbsSurfaceEvaluator' objects>"
        'get_v_knot': None, # (!) real value is "<method 'get_v_knot' of 'panda3d.core.NurbsSurfaceEvaluator' objects>"
        'get_v_knots': None, # (!) real value is "<method 'get_v_knots' of 'panda3d.core.NurbsSurfaceEvaluator' objects>"
        'get_v_order': None, # (!) real value is "<method 'get_v_order' of 'panda3d.core.NurbsSurfaceEvaluator' objects>"
        'get_vertex': None, # (!) real value is "<method 'get_vertex' of 'panda3d.core.NurbsSurfaceEvaluator' objects>"
        'get_vertex_space': None, # (!) real value is "<method 'get_vertex_space' of 'panda3d.core.NurbsSurfaceEvaluator' objects>"
        'normalizeUKnots': None, # (!) real value is "<method 'normalizeUKnots' of 'panda3d.core.NurbsSurfaceEvaluator' objects>"
        'normalizeVKnots': None, # (!) real value is "<method 'normalizeVKnots' of 'panda3d.core.NurbsSurfaceEvaluator' objects>"
        'normalize_u_knots': None, # (!) real value is "<method 'normalize_u_knots' of 'panda3d.core.NurbsSurfaceEvaluator' objects>"
        'normalize_v_knots': None, # (!) real value is "<method 'normalize_v_knots' of 'panda3d.core.NurbsSurfaceEvaluator' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.NurbsSurfaceEvaluator' objects>"
        'reset': None, # (!) real value is "<method 'reset' of 'panda3d.core.NurbsSurfaceEvaluator' objects>"
        'setExtendedVertex': None, # (!) real value is "<method 'setExtendedVertex' of 'panda3d.core.NurbsSurfaceEvaluator' objects>"
        'setExtendedVertices': None, # (!) real value is "<method 'setExtendedVertices' of 'panda3d.core.NurbsSurfaceEvaluator' objects>"
        'setUKnot': None, # (!) real value is "<method 'setUKnot' of 'panda3d.core.NurbsSurfaceEvaluator' objects>"
        'setUOrder': None, # (!) real value is "<method 'setUOrder' of 'panda3d.core.NurbsSurfaceEvaluator' objects>"
        'setVKnot': None, # (!) real value is "<method 'setVKnot' of 'panda3d.core.NurbsSurfaceEvaluator' objects>"
        'setVOrder': None, # (!) real value is "<method 'setVOrder' of 'panda3d.core.NurbsSurfaceEvaluator' objects>"
        'setVertex': None, # (!) real value is "<method 'setVertex' of 'panda3d.core.NurbsSurfaceEvaluator' objects>"
        'setVertexSpace': None, # (!) real value is "<method 'setVertexSpace' of 'panda3d.core.NurbsSurfaceEvaluator' objects>"
        'set_extended_vertex': None, # (!) real value is "<method 'set_extended_vertex' of 'panda3d.core.NurbsSurfaceEvaluator' objects>"
        'set_extended_vertices': None, # (!) real value is "<method 'set_extended_vertices' of 'panda3d.core.NurbsSurfaceEvaluator' objects>"
        'set_u_knot': None, # (!) real value is "<method 'set_u_knot' of 'panda3d.core.NurbsSurfaceEvaluator' objects>"
        'set_u_order': None, # (!) real value is "<method 'set_u_order' of 'panda3d.core.NurbsSurfaceEvaluator' objects>"
        'set_v_knot': None, # (!) real value is "<method 'set_v_knot' of 'panda3d.core.NurbsSurfaceEvaluator' objects>"
        'set_v_order': None, # (!) real value is "<method 'set_v_order' of 'panda3d.core.NurbsSurfaceEvaluator' objects>"
        'set_vertex': None, # (!) real value is "<method 'set_vertex' of 'panda3d.core.NurbsSurfaceEvaluator' objects>"
        'set_vertex_space': None, # (!) real value is "<method 'set_vertex_space' of 'panda3d.core.NurbsSurfaceEvaluator' objects>"
        'u_knots': None, # (!) real value is "<attribute 'u_knots' of 'panda3d.core.NurbsSurfaceEvaluator' objects>"
        'u_order': None, # (!) real value is "<attribute 'u_order' of 'panda3d.core.NurbsSurfaceEvaluator' objects>"
        'v_knots': None, # (!) real value is "<attribute 'v_knots' of 'panda3d.core.NurbsSurfaceEvaluator' objects>"
        'v_order': None, # (!) real value is "<attribute 'v_order' of 'panda3d.core.NurbsSurfaceEvaluator' objects>"
    }


