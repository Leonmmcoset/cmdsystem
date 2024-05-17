# encoding: utf-8
# module panda3d.egg
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\egg.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import panda3d.core as __panda3d_core


from .EggPrimitive import EggPrimitive

class EggPolygon(EggPrimitive):
    """
    /**
     * A single polygon.
     */
    """
    def assign(self, const_EggPolygon_self, const_EggPolygon_copy): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        assign(const EggPolygon self, const EggPolygon copy)
        
        /**
         *
         */
        """
        pass

    def calculateNormal(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        calculate_normal(EggPolygon self, LVector3d result, int cs)
        
        /**
         * Calculates the true polygon normal--the vector pointing out of the front of
         * the polygon--based on the vertices.  This does not return or change the
         * polygon's normal as set via set_normal().
         *
         * The return value is true if the normal is computed correctly, or false if
         * the polygon is degenerate and does not have at least three noncollinear
         * vertices.
         */
        """
        pass

    def calculate_normal(self, EggPolygon_self, LVector3d_result, int_cs): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        calculate_normal(EggPolygon self, LVector3d result, int cs)
        
        /**
         * Calculates the true polygon normal--the vector pointing out of the front of
         * the polygon--based on the vertices.  This does not return or change the
         * polygon's normal as set via set_normal().
         *
         * The return value is true if the normal is computed correctly, or false if
         * the polygon is degenerate and does not have at least three noncollinear
         * vertices.
         */
        """
        pass

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

    def isPlanar(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_planar(EggPolygon self)
        
        /**
         * Returns true if all of the polygon's vertices lie within the same plane,
         * false otherwise.
         */
        """
        pass

    def is_planar(self, EggPolygon_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_planar(EggPolygon self)
        
        /**
         * Returns true if all of the polygon's vertices lie within the same plane,
         * false otherwise.
         */
        """
        pass

    def recomputePolygonNormal(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        recompute_polygon_normal(const EggPolygon self, int cs)
        
        /**
         * Recalculates the normal according to the order of the vertices, and sets
         * it.  Returns true if the normal is computed correctly, or false if the
         * polygon is degenerate and does not have a normal.
         */
        """
        pass

    def recompute_polygon_normal(self, const_EggPolygon_self, int_cs): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        recompute_polygon_normal(const EggPolygon self, int cs)
        
        /**
         * Recalculates the normal according to the order of the vertices, and sets
         * it.  Returns true if the normal is computed correctly, or false if the
         * polygon is degenerate and does not have a normal.
         */
        """
        pass

    def triangulateInPlace(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        triangulate_in_place(const EggPolygon self, bool convex_also)
        
        /**
         * Subdivides the polygon into triangles and adds those triangles to the
         * parent group node in place of the original polygon.  Returns a pointer to
         * the original polygon, which is likely about to be destructed.
         *
         * If convex_also is true, both concave and convex polygons will be subdivided
         * into triangles; otherwise, only concave polygons will be subdivided, and
         * convex polygons will be copied unchanged into the container.
         */
        """
        pass

    def triangulateInto(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        triangulate_into(EggPolygon self, EggGroupNode container, bool convex_also)
        
        /**
         * Subdivides the polygon into triangles and adds each one to the indicated
         * container.  If the polygon is already a triangle, adds an exact copy of the
         * polygon to the container.  Does not remove the polygon from its existing
         * parent or modify it in any way.
         *
         * Returns true if the triangulation is successful, or false if there was some
         * error (in which case the container may contain some partial triangulation).
         *
         * If convex_also is true, both concave and convex polygons will be subdivided
         * into triangles; otherwise, only concave polygons will be subdivided, and
         * convex polygons will be copied unchanged into the container.
         */
        """
        pass

    def triangulate_into(self, EggPolygon_self, EggGroupNode_container, bool_convex_also): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        triangulate_into(EggPolygon self, EggGroupNode container, bool convex_also)
        
        /**
         * Subdivides the polygon into triangles and adds each one to the indicated
         * container.  If the polygon is already a triangle, adds an exact copy of the
         * polygon to the container.  Does not remove the polygon from its existing
         * parent or modify it in any way.
         *
         * Returns true if the triangulation is successful, or false if there was some
         * error (in which case the container may contain some partial triangulation).
         *
         * If convex_also is true, both concave and convex polygons will be subdivided
         * into triangles; otherwise, only concave polygons will be subdivided, and
         * convex polygons will be copied unchanged into the container.
         */
        """
        pass

    def triangulate_in_place(self, const_EggPolygon_self, bool_convex_also): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        triangulate_in_place(const EggPolygon self, bool convex_also)
        
        /**
         * Subdivides the polygon into triangles and adds those triangles to the
         * parent group node in place of the original polygon.  Returns a pointer to
         * the original polygon, which is likely about to be destructed.
         *
         * If convex_also is true, both concave and convex polygons will be subdivided
         * into triangles; otherwise, only concave polygons will be subdivided, and
         * convex polygons will be copied unchanged into the container.
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
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.egg.EggPolygon' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.egg.EggPolygon' objects>"
        '__doc__': '/**\n * A single polygon.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.egg.EggPolygon' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDC68D0180>'
        'assign': None, # (!) real value is "<method 'assign' of 'panda3d.egg.EggPolygon' objects>"
        'calculateNormal': None, # (!) real value is "<method 'calculateNormal' of 'panda3d.egg.EggPolygon' objects>"
        'calculate_normal': None, # (!) real value is "<method 'calculate_normal' of 'panda3d.egg.EggPolygon' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFDC68D0180>)>'
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFDC68D0180>)>'
        'isPlanar': None, # (!) real value is "<method 'isPlanar' of 'panda3d.egg.EggPolygon' objects>"
        'is_planar': None, # (!) real value is "<method 'is_planar' of 'panda3d.egg.EggPolygon' objects>"
        'recomputePolygonNormal': None, # (!) real value is "<method 'recomputePolygonNormal' of 'panda3d.egg.EggPolygon' objects>"
        'recompute_polygon_normal': None, # (!) real value is "<method 'recompute_polygon_normal' of 'panda3d.egg.EggPolygon' objects>"
        'triangulateInPlace': None, # (!) real value is "<method 'triangulateInPlace' of 'panda3d.egg.EggPolygon' objects>"
        'triangulateInto': None, # (!) real value is "<method 'triangulateInto' of 'panda3d.egg.EggPolygon' objects>"
        'triangulate_in_place': None, # (!) real value is "<method 'triangulate_in_place' of 'panda3d.egg.EggPolygon' objects>"
        'triangulate_into': None, # (!) real value is "<method 'triangulate_into' of 'panda3d.egg.EggPolygon' objects>"
    }


