# encoding: utf-8
# module panda3d.egg
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\egg.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import panda3d.core as __panda3d_core


from .EggSurface import EggSurface

class EggNurbsSurface(EggSurface):
    """
    /**
     * A parametric NURBS surface.
     */
    """
    def assign(self, const_EggNurbsSurface_self, const_EggNurbsSurface_copy): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        assign(const EggNurbsSurface self, const EggNurbsSurface copy)
        
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
        get_cv(EggNurbsSurface self, int ui, int vi)
        
        /**
         * Returns the control vertex at the indicate U, V position.
         */
        """
        pass

    def getNumCvs(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_cvs(EggNurbsSurface self)
        
        /**
         * Returns the total number of control vertices that *should* be defined for
         * the surface.  This is determined by the number of knots and the order, in
         * each direction; it does not necessarily reflect the number of vertices that
         * have actually been added to the surface.  (However, if the number of
         * vertices in the surface are wrong, the surface is invalid.)
         */
        """
        pass

    def getNumUCvs(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_u_cvs(EggNurbsSurface self)
        
        /**
         * Returns the number of control vertices that should be present in the U
         * direction.  This is determined by the number of knots and the order; it
         * does not necessarily reflect the number of vertices that have actually been
         * added to the surface.  (However, if the number of vertices in the surface
         * are wrong, the surface is invalid.)
         */
        """
        pass

    def getNumUKnots(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_u_knots(EggNurbsSurface self)
        
        /**
         * Returns the number of knots in the U direction.
         */
        """
        pass

    def getNumVCvs(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_v_cvs(EggNurbsSurface self)
        
        /**
         * Returns the number of control vertices that should be present in the V
         * direction.  This is determined by the number of knots and the order; it
         * does not necessarily reflect the number of vertices that have actually been
         * added to the surface.  (However, if the number of vertices in the surface
         * are wrong, the surface is invalid.)
         */
        """
        pass

    def getNumVKnots(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_v_knots(EggNurbsSurface self)
        
        /**
         * Returns the number of knots in the V direction.
         */
        """
        pass

    def getUDegree(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_u_degree(EggNurbsSurface self)
        
        /**
         * Returns the degree of the surface in the U direction.  For a typical NURBS,
         * the degree is 3.
         */
        """
        pass

    def getUIndex(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_u_index(EggNurbsSurface self, int vertex_index)
        
        /**
         * Returns the U index number of the given vertex within the EggPrimitive's
         * linear list of vertices.  An EggNurbsSurface maps a linear list of vertices
         * to its 2-d mesh; this returns the U index number that corresponds to the
         * nth vertex in the list.
         */
        """
        pass

    def getUKnot(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_u_knot(EggNurbsSurface self, int k)
        
        /**
         * Returns the nth knot value defined in the U direction.
         */
        """
        pass

    def getUKnots(self, *args, **kwargs): # real signature unknown
        pass

    def getUOrder(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_u_order(EggNurbsSurface self)
        
        /**
         * Returns the order of the surface in the U direction.  The order is the
         * degree of the NURBS equation plus 1; for a typical NURBS, the order is 4.
         * With this implementation of NURBS, the order must be in the range [1, 4].
         */
        """
        pass

    def getVDegree(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_v_degree(EggNurbsSurface self)
        
        /**
         * Returns the degree of the surface in the V direction.  for a typical NURBS,
         * the degree is 3.
         */
        """
        pass

    def getVertexIndex(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_vertex_index(EggNurbsSurface self, int ui, int vi)
        
        /**
         * Returns the index number within the EggPrimitive's list of the control
         * vertex at position ui, vi.
         */
        """
        pass

    def getVIndex(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_v_index(EggNurbsSurface self, int vertex_index)
        
        /**
         * Returns the V index number of the given vertex within the EggPrimitive's
         * linear list of vertices.  An EggNurbsSurface maps a linear list of vertices
         * to its 2-d mesh; this returns the V index number that corresponds to the
         * nth vertex in the list.
         */
        """
        pass

    def getVKnot(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_v_knot(EggNurbsSurface self, int k)
        
        /**
         * Returns the nth knot value defined in the V direction.
         */
        """
        pass

    def getVKnots(self, *args, **kwargs): # real signature unknown
        pass

    def getVOrder(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_v_order(EggNurbsSurface self)
        
        /**
         * Returns the order of the surface in the V direction.  The order is the
         * degree of the NURBS equation plus 1; for a typical NURBS, the order is 4.
         * With this implementation of NURBS, the order must be in the range [1, 4].
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_cv(self, EggNurbsSurface_self, int_ui, int_vi): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_cv(EggNurbsSurface self, int ui, int vi)
        
        /**
         * Returns the control vertex at the indicate U, V position.
         */
        """
        pass

    def get_num_cvs(self, EggNurbsSurface_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_cvs(EggNurbsSurface self)
        
        /**
         * Returns the total number of control vertices that *should* be defined for
         * the surface.  This is determined by the number of knots and the order, in
         * each direction; it does not necessarily reflect the number of vertices that
         * have actually been added to the surface.  (However, if the number of
         * vertices in the surface are wrong, the surface is invalid.)
         */
        """
        pass

    def get_num_u_cvs(self, EggNurbsSurface_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_u_cvs(EggNurbsSurface self)
        
        /**
         * Returns the number of control vertices that should be present in the U
         * direction.  This is determined by the number of knots and the order; it
         * does not necessarily reflect the number of vertices that have actually been
         * added to the surface.  (However, if the number of vertices in the surface
         * are wrong, the surface is invalid.)
         */
        """
        pass

    def get_num_u_knots(self, EggNurbsSurface_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_u_knots(EggNurbsSurface self)
        
        /**
         * Returns the number of knots in the U direction.
         */
        """
        pass

    def get_num_v_cvs(self, EggNurbsSurface_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_v_cvs(EggNurbsSurface self)
        
        /**
         * Returns the number of control vertices that should be present in the V
         * direction.  This is determined by the number of knots and the order; it
         * does not necessarily reflect the number of vertices that have actually been
         * added to the surface.  (However, if the number of vertices in the surface
         * are wrong, the surface is invalid.)
         */
        """
        pass

    def get_num_v_knots(self, EggNurbsSurface_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_v_knots(EggNurbsSurface self)
        
        /**
         * Returns the number of knots in the V direction.
         */
        """
        pass

    def get_u_degree(self, EggNurbsSurface_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_u_degree(EggNurbsSurface self)
        
        /**
         * Returns the degree of the surface in the U direction.  For a typical NURBS,
         * the degree is 3.
         */
        """
        pass

    def get_u_index(self, EggNurbsSurface_self, int_vertex_index): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_u_index(EggNurbsSurface self, int vertex_index)
        
        /**
         * Returns the U index number of the given vertex within the EggPrimitive's
         * linear list of vertices.  An EggNurbsSurface maps a linear list of vertices
         * to its 2-d mesh; this returns the U index number that corresponds to the
         * nth vertex in the list.
         */
        """
        pass

    def get_u_knot(self, EggNurbsSurface_self, int_k): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_u_knot(EggNurbsSurface self, int k)
        
        /**
         * Returns the nth knot value defined in the U direction.
         */
        """
        pass

    def get_u_knots(self, *args, **kwargs): # real signature unknown
        pass

    def get_u_order(self, EggNurbsSurface_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_u_order(EggNurbsSurface self)
        
        /**
         * Returns the order of the surface in the U direction.  The order is the
         * degree of the NURBS equation plus 1; for a typical NURBS, the order is 4.
         * With this implementation of NURBS, the order must be in the range [1, 4].
         */
        """
        pass

    def get_vertex_index(self, EggNurbsSurface_self, int_ui, int_vi): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_vertex_index(EggNurbsSurface self, int ui, int vi)
        
        /**
         * Returns the index number within the EggPrimitive's list of the control
         * vertex at position ui, vi.
         */
        """
        pass

    def get_v_degree(self, EggNurbsSurface_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_v_degree(EggNurbsSurface self)
        
        /**
         * Returns the degree of the surface in the V direction.  for a typical NURBS,
         * the degree is 3.
         */
        """
        pass

    def get_v_index(self, EggNurbsSurface_self, int_vertex_index): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_v_index(EggNurbsSurface self, int vertex_index)
        
        /**
         * Returns the V index number of the given vertex within the EggPrimitive's
         * linear list of vertices.  An EggNurbsSurface maps a linear list of vertices
         * to its 2-d mesh; this returns the V index number that corresponds to the
         * nth vertex in the list.
         */
        """
        pass

    def get_v_knot(self, EggNurbsSurface_self, int_k): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_v_knot(EggNurbsSurface self, int k)
        
        /**
         * Returns the nth knot value defined in the V direction.
         */
        """
        pass

    def get_v_knots(self, *args, **kwargs): # real signature unknown
        pass

    def get_v_order(self, EggNurbsSurface_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_v_order(EggNurbsSurface self)
        
        /**
         * Returns the order of the surface in the V direction.  The order is the
         * degree of the NURBS equation plus 1; for a typical NURBS, the order is 4.
         * With this implementation of NURBS, the order must be in the range [1, 4].
         */
        """
        pass

    def isClosedU(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_closed_u(EggNurbsSurface self)
        
        /**
         * Returns true if the surface appears to be closed in the U direction.  Since
         * the Egg syntax does not provide a means for explicit indication of closure,
         * this has to be guessed at by examining the surface itself.
         */
        """
        pass

    def isClosedV(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_closed_v(EggNurbsSurface self)
        
        /**
         * Returns true if the surface appears to be closed in the V direction.  Since
         * the Egg syntax does not provide a means for explicit indication of closure,
         * this has to be guessed at by examining the surface itself.
         */
        """
        pass

    def isValid(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_valid(EggNurbsSurface self)
        
        /**
         * Returns true if the NURBS parameters are all internally consistent (e.g.
         * it has the right number of vertices to match its number of knots and order
         * in each dimension), or false otherwise.
         */
        """
        pass

    def is_closed_u(self, EggNurbsSurface_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_closed_u(EggNurbsSurface self)
        
        /**
         * Returns true if the surface appears to be closed in the U direction.  Since
         * the Egg syntax does not provide a means for explicit indication of closure,
         * this has to be guessed at by examining the surface itself.
         */
        """
        pass

    def is_closed_v(self, EggNurbsSurface_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_closed_v(EggNurbsSurface self)
        
        /**
         * Returns true if the surface appears to be closed in the V direction.  Since
         * the Egg syntax does not provide a means for explicit indication of closure,
         * this has to be guessed at by examining the surface itself.
         */
        """
        pass

    def is_valid(self, EggNurbsSurface_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_valid(EggNurbsSurface self)
        
        /**
         * Returns true if the NURBS parameters are all internally consistent (e.g.
         * it has the right number of vertices to match its number of knots and order
         * in each dimension), or false otherwise.
         */
        """
        pass

    def setCv(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_cv(const EggNurbsSurface self, int ui, int vi, EggVertex vertex)
        
        /**
         * Redefines the control vertex associated with a particular u, v coordinate
         * pair.  This is just a shorthand to access the EggPrimitive's normal vertex
         * assignment for a 2-d control vertex.
         */
        """
        pass

    def setNumUKnots(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_num_u_knots(const EggNurbsSurface self, int num)
        
        /**
         * Directly changes the number of knots in the U direction.  This will either
         * add zero-valued knots onto the end, or truncate knot values from the end,
         * depending on whether the list is being increased or decreased.  If
         * possible, it is preferable to use the setup() method instead of directly
         * setting the number of knots, as this may result in an invalid surface.
         */
        """
        pass

    def setNumVKnots(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_num_v_knots(const EggNurbsSurface self, int num)
        
        /**
         * Directly changes the number of knots in the V direction.  This will either
         * add zero-valued knots onto the end, or truncate knot values from the end,
         * depending on whether the list is being increased or decreased.  If
         * possible, it is preferable to use the setup() method instead of directly
         * setting the number of knots, as this may result in an invalid surface.
         */
        """
        pass

    def setUKnot(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_u_knot(const EggNurbsSurface self, int k, double value)
        
        /**
         * Resets the value of the indicated knot as indicated.  k must be in the
         * range 0 <= k < get_num_u_knots(), and the value must be in the range
         * get_u_knot(k - 1) <= value <= get_u_knot(k + 1).
         */
        """
        pass

    def setUOrder(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_u_order(const EggNurbsSurface self, int u_order)
        
        /**
         * Directly changes the order in the U direction to the indicated value (which
         * must be an integer in the range 1 <= u_order <= 4).  If possible, it is
         * preferable to use the setup() method instead of this method, since changing
         * the order directly may result in an invalid surface.
         */
        """
        pass

    def setup(self, const_EggNurbsSurface_self, int_u_order, int_v_order, int_num_u_knots, int_num_v_knots): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        setup(const EggNurbsSurface self, int u_order, int v_order, int num_u_knots, int num_v_knots)
        
        /**
         * Prepares a new surface definition with the indicated order and number of
         * knots in each dimension.  This also implies a particular number of vertices
         * in each dimension as well (the number of knots minus the order), but it is
         * up to the user to add the correct number of vertices to the surface by
         * repeatedly calling push_back().
         */
        """
        pass

    def setVKnot(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_v_knot(const EggNurbsSurface self, int k, double value)
        
        /**
         * Resets the value of the indicated knot as indicated.  k must be in the
         * range 0 <= k < get_num_v_knots(), and the value must be in the range
         * get_v_knot(k - 1) <= value <= get_v_knot(k + 1).
         */
        """
        pass

    def setVOrder(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_v_order(const EggNurbsSurface self, int v_order)
        
        /**
         * Directly changes the order in the V direction to the indicated value (which
         * must be an integer in the range 1 <= v_order <= 4).  If possible, it is
         * preferable to use the setup() method instead of this method, since changing
         * the order directly may result in an invalid surface.
         */
        """
        pass

    def set_cv(self, const_EggNurbsSurface_self, int_ui, int_vi, EggVertex_vertex): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_cv(const EggNurbsSurface self, int ui, int vi, EggVertex vertex)
        
        /**
         * Redefines the control vertex associated with a particular u, v coordinate
         * pair.  This is just a shorthand to access the EggPrimitive's normal vertex
         * assignment for a 2-d control vertex.
         */
        """
        pass

    def set_num_u_knots(self, const_EggNurbsSurface_self, int_num): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_num_u_knots(const EggNurbsSurface self, int num)
        
        /**
         * Directly changes the number of knots in the U direction.  This will either
         * add zero-valued knots onto the end, or truncate knot values from the end,
         * depending on whether the list is being increased or decreased.  If
         * possible, it is preferable to use the setup() method instead of directly
         * setting the number of knots, as this may result in an invalid surface.
         */
        """
        pass

    def set_num_v_knots(self, const_EggNurbsSurface_self, int_num): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_num_v_knots(const EggNurbsSurface self, int num)
        
        /**
         * Directly changes the number of knots in the V direction.  This will either
         * add zero-valued knots onto the end, or truncate knot values from the end,
         * depending on whether the list is being increased or decreased.  If
         * possible, it is preferable to use the setup() method instead of directly
         * setting the number of knots, as this may result in an invalid surface.
         */
        """
        pass

    def set_u_knot(self, const_EggNurbsSurface_self, int_k, double_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_u_knot(const EggNurbsSurface self, int k, double value)
        
        /**
         * Resets the value of the indicated knot as indicated.  k must be in the
         * range 0 <= k < get_num_u_knots(), and the value must be in the range
         * get_u_knot(k - 1) <= value <= get_u_knot(k + 1).
         */
        """
        pass

    def set_u_order(self, const_EggNurbsSurface_self, int_u_order): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_u_order(const EggNurbsSurface self, int u_order)
        
        /**
         * Directly changes the order in the U direction to the indicated value (which
         * must be an integer in the range 1 <= u_order <= 4).  If possible, it is
         * preferable to use the setup() method instead of this method, since changing
         * the order directly may result in an invalid surface.
         */
        """
        pass

    def set_v_knot(self, const_EggNurbsSurface_self, int_k, double_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_v_knot(const EggNurbsSurface self, int k, double value)
        
        /**
         * Resets the value of the indicated knot as indicated.  k must be in the
         * range 0 <= k < get_num_v_knots(), and the value must be in the range
         * get_v_knot(k - 1) <= value <= get_v_knot(k + 1).
         */
        """
        pass

    def set_v_order(self, const_EggNurbsSurface_self, int_v_order): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_v_order(const EggNurbsSurface self, int v_order)
        
        /**
         * Directly changes the order in the V direction to the indicated value (which
         * must be an integer in the range 1 <= v_order <= 4).  If possible, it is
         * preferable to use the setup() method instead of this method, since changing
         * the order directly may result in an invalid surface.
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
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.egg.EggNurbsSurface' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.egg.EggNurbsSurface' objects>"
        '__doc__': '/**\n * A parametric NURBS surface.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.egg.EggNurbsSurface' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDC68D06F0>'
        'assign': None, # (!) real value is "<method 'assign' of 'panda3d.egg.EggNurbsSurface' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFDC68D06F0>)>'
        'getCv': None, # (!) real value is "<method 'getCv' of 'panda3d.egg.EggNurbsSurface' objects>"
        'getNumCvs': None, # (!) real value is "<method 'getNumCvs' of 'panda3d.egg.EggNurbsSurface' objects>"
        'getNumUCvs': None, # (!) real value is "<method 'getNumUCvs' of 'panda3d.egg.EggNurbsSurface' objects>"
        'getNumUKnots': None, # (!) real value is "<method 'getNumUKnots' of 'panda3d.egg.EggNurbsSurface' objects>"
        'getNumVCvs': None, # (!) real value is "<method 'getNumVCvs' of 'panda3d.egg.EggNurbsSurface' objects>"
        'getNumVKnots': None, # (!) real value is "<method 'getNumVKnots' of 'panda3d.egg.EggNurbsSurface' objects>"
        'getUDegree': None, # (!) real value is "<method 'getUDegree' of 'panda3d.egg.EggNurbsSurface' objects>"
        'getUIndex': None, # (!) real value is "<method 'getUIndex' of 'panda3d.egg.EggNurbsSurface' objects>"
        'getUKnot': None, # (!) real value is "<method 'getUKnot' of 'panda3d.egg.EggNurbsSurface' objects>"
        'getUKnots': None, # (!) real value is "<method 'getUKnots' of 'panda3d.egg.EggNurbsSurface' objects>"
        'getUOrder': None, # (!) real value is "<method 'getUOrder' of 'panda3d.egg.EggNurbsSurface' objects>"
        'getVDegree': None, # (!) real value is "<method 'getVDegree' of 'panda3d.egg.EggNurbsSurface' objects>"
        'getVIndex': None, # (!) real value is "<method 'getVIndex' of 'panda3d.egg.EggNurbsSurface' objects>"
        'getVKnot': None, # (!) real value is "<method 'getVKnot' of 'panda3d.egg.EggNurbsSurface' objects>"
        'getVKnots': None, # (!) real value is "<method 'getVKnots' of 'panda3d.egg.EggNurbsSurface' objects>"
        'getVOrder': None, # (!) real value is "<method 'getVOrder' of 'panda3d.egg.EggNurbsSurface' objects>"
        'getVertexIndex': None, # (!) real value is "<method 'getVertexIndex' of 'panda3d.egg.EggNurbsSurface' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFDC68D06F0>)>'
        'get_cv': None, # (!) real value is "<method 'get_cv' of 'panda3d.egg.EggNurbsSurface' objects>"
        'get_num_cvs': None, # (!) real value is "<method 'get_num_cvs' of 'panda3d.egg.EggNurbsSurface' objects>"
        'get_num_u_cvs': None, # (!) real value is "<method 'get_num_u_cvs' of 'panda3d.egg.EggNurbsSurface' objects>"
        'get_num_u_knots': None, # (!) real value is "<method 'get_num_u_knots' of 'panda3d.egg.EggNurbsSurface' objects>"
        'get_num_v_cvs': None, # (!) real value is "<method 'get_num_v_cvs' of 'panda3d.egg.EggNurbsSurface' objects>"
        'get_num_v_knots': None, # (!) real value is "<method 'get_num_v_knots' of 'panda3d.egg.EggNurbsSurface' objects>"
        'get_u_degree': None, # (!) real value is "<method 'get_u_degree' of 'panda3d.egg.EggNurbsSurface' objects>"
        'get_u_index': None, # (!) real value is "<method 'get_u_index' of 'panda3d.egg.EggNurbsSurface' objects>"
        'get_u_knot': None, # (!) real value is "<method 'get_u_knot' of 'panda3d.egg.EggNurbsSurface' objects>"
        'get_u_knots': None, # (!) real value is "<method 'get_u_knots' of 'panda3d.egg.EggNurbsSurface' objects>"
        'get_u_order': None, # (!) real value is "<method 'get_u_order' of 'panda3d.egg.EggNurbsSurface' objects>"
        'get_v_degree': None, # (!) real value is "<method 'get_v_degree' of 'panda3d.egg.EggNurbsSurface' objects>"
        'get_v_index': None, # (!) real value is "<method 'get_v_index' of 'panda3d.egg.EggNurbsSurface' objects>"
        'get_v_knot': None, # (!) real value is "<method 'get_v_knot' of 'panda3d.egg.EggNurbsSurface' objects>"
        'get_v_knots': None, # (!) real value is "<method 'get_v_knots' of 'panda3d.egg.EggNurbsSurface' objects>"
        'get_v_order': None, # (!) real value is "<method 'get_v_order' of 'panda3d.egg.EggNurbsSurface' objects>"
        'get_vertex_index': None, # (!) real value is "<method 'get_vertex_index' of 'panda3d.egg.EggNurbsSurface' objects>"
        'isClosedU': None, # (!) real value is "<method 'isClosedU' of 'panda3d.egg.EggNurbsSurface' objects>"
        'isClosedV': None, # (!) real value is "<method 'isClosedV' of 'panda3d.egg.EggNurbsSurface' objects>"
        'isValid': None, # (!) real value is "<method 'isValid' of 'panda3d.egg.EggNurbsSurface' objects>"
        'is_closed_u': None, # (!) real value is "<method 'is_closed_u' of 'panda3d.egg.EggNurbsSurface' objects>"
        'is_closed_v': None, # (!) real value is "<method 'is_closed_v' of 'panda3d.egg.EggNurbsSurface' objects>"
        'is_valid': None, # (!) real value is "<method 'is_valid' of 'panda3d.egg.EggNurbsSurface' objects>"
        'setCv': None, # (!) real value is "<method 'setCv' of 'panda3d.egg.EggNurbsSurface' objects>"
        'setNumUKnots': None, # (!) real value is "<method 'setNumUKnots' of 'panda3d.egg.EggNurbsSurface' objects>"
        'setNumVKnots': None, # (!) real value is "<method 'setNumVKnots' of 'panda3d.egg.EggNurbsSurface' objects>"
        'setUKnot': None, # (!) real value is "<method 'setUKnot' of 'panda3d.egg.EggNurbsSurface' objects>"
        'setUOrder': None, # (!) real value is "<method 'setUOrder' of 'panda3d.egg.EggNurbsSurface' objects>"
        'setVKnot': None, # (!) real value is "<method 'setVKnot' of 'panda3d.egg.EggNurbsSurface' objects>"
        'setVOrder': None, # (!) real value is "<method 'setVOrder' of 'panda3d.egg.EggNurbsSurface' objects>"
        'set_cv': None, # (!) real value is "<method 'set_cv' of 'panda3d.egg.EggNurbsSurface' objects>"
        'set_num_u_knots': None, # (!) real value is "<method 'set_num_u_knots' of 'panda3d.egg.EggNurbsSurface' objects>"
        'set_num_v_knots': None, # (!) real value is "<method 'set_num_v_knots' of 'panda3d.egg.EggNurbsSurface' objects>"
        'set_u_knot': None, # (!) real value is "<method 'set_u_knot' of 'panda3d.egg.EggNurbsSurface' objects>"
        'set_u_order': None, # (!) real value is "<method 'set_u_order' of 'panda3d.egg.EggNurbsSurface' objects>"
        'set_v_knot': None, # (!) real value is "<method 'set_v_knot' of 'panda3d.egg.EggNurbsSurface' objects>"
        'set_v_order': None, # (!) real value is "<method 'set_v_order' of 'panda3d.egg.EggNurbsSurface' objects>"
        'setup': None, # (!) real value is "<method 'setup' of 'panda3d.egg.EggNurbsSurface' objects>"
    }


