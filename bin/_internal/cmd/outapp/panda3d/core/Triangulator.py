# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class Triangulator(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * This class can triangulate a convex or concave polygon, even one with
     * holes.  It is adapted from an algorithm published as:
     *
     * Narkhede A. and Manocha D., Fast polygon triangulation algorithm based on
     * Seidel's Algorithm, UNC-CH, 1994.
     *
     * http://www.cs.unc.edu/~dm/CODE/GEM/chapter.html
     *
     * It works strictly on 2-d points.  See Triangulator3 for 3-d points.
     */
    """
    def addHoleVertex(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_hole_vertex(const Triangulator self, int index)
        
        /**
         * Adds the next consecutive vertex of the current hole.  This vertex should
         * index into the vertex pool established by repeated calls to add_vertex().
         *
         * The vertices may be listed in either clockwise or counterclockwise order.
         * Vertices should not be repeated.
         */
        """
        pass

    def addPolygonVertex(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_polygon_vertex(const Triangulator self, int index)
        
        /**
         * Adds the next consecutive vertex of the polygon.  This vertex should index
         * into the vertex pool established by repeated calls to add_vertex().
         *
         * The vertices may be listed in either clockwise or counterclockwise order.
         * Vertices should not be repeated.  In particular, do not repeat the first
         * vertex at the end.
         */
        """
        pass

    def addVertex(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_vertex(const Triangulator self, const LPoint2d point)
        add_vertex(const Triangulator self, double x, double y)
        
        /**
         * Adds a new vertex to the vertex pool.  Returns the vertex index number.
         */
        
        /**
         * Adds a new vertex to the vertex pool.  Returns the vertex index number.
         */
        """
        pass

    def add_hole_vertex(self, const_Triangulator_self, int_index): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_hole_vertex(const Triangulator self, int index)
        
        /**
         * Adds the next consecutive vertex of the current hole.  This vertex should
         * index into the vertex pool established by repeated calls to add_vertex().
         *
         * The vertices may be listed in either clockwise or counterclockwise order.
         * Vertices should not be repeated.
         */
        """
        pass

    def add_polygon_vertex(self, const_Triangulator_self, int_index): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_polygon_vertex(const Triangulator self, int index)
        
        /**
         * Adds the next consecutive vertex of the polygon.  This vertex should index
         * into the vertex pool established by repeated calls to add_vertex().
         *
         * The vertices may be listed in either clockwise or counterclockwise order.
         * Vertices should not be repeated.  In particular, do not repeat the first
         * vertex at the end.
         */
        """
        pass

    def add_vertex(self, const_Triangulator_self, const_LPoint2d_point): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_vertex(const Triangulator self, const LPoint2d point)
        add_vertex(const Triangulator self, double x, double y)
        
        /**
         * Adds a new vertex to the vertex pool.  Returns the vertex index number.
         */
        
        /**
         * Adds a new vertex to the vertex pool.  Returns the vertex index number.
         */
        """
        pass

    def beginHole(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        begin_hole(const Triangulator self)
        
        /**
         * Finishes the previous hole, if any, and prepares to add a new hole.
         */
        """
        pass

    def begin_hole(self, const_Triangulator_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        begin_hole(const Triangulator self)
        
        /**
         * Finishes the previous hole, if any, and prepares to add a new hole.
         */
        """
        pass

    def clear(self, const_Triangulator_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear(const Triangulator self)
        
        /**
         * Removes all vertices and polygon specifications from the Triangulator, and
         * prepares it to start over.
         */
        """
        pass

    def clearPolygon(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_polygon(const Triangulator self)
        
        /**
         * Removes the current polygon definition (and its set of holes), but does not
         * clear the vertex pool.
         */
        """
        pass

    def clear_polygon(self, const_Triangulator_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_polygon(const Triangulator self)
        
        /**
         * Removes the current polygon definition (and its set of holes), but does not
         * clear the vertex pool.
         */
        """
        pass

    def getNumTriangles(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_triangles(Triangulator self)
        
        /**
         * Returns the number of triangles generated by the previous call to
         * triangulate().
         */
        """
        pass

    def getNumVertices(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_vertices(Triangulator self)
        
        /**
         * Returns the number of vertices in the pool.  Note that the Triangulator
         * might append new vertices, in addition to those added by the user, if any
         * of the polygon is self-intersecting, or if any of the holes intersect some
         * part of the polygon edges.
         */
        """
        pass

    def getTriangleV0(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_triangle_v0(Triangulator self, int n)
        
        /**
         * Returns vertex 0 of the nth triangle generated by the previous call to
         * triangulate().
         *
         * This is a zero-based index into the vertices added by repeated calls to
         * add_vertex().
         */
        """
        pass

    def getTriangleV1(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_triangle_v1(Triangulator self, int n)
        
        /**
         * Returns vertex 1 of the nth triangle generated by the previous call to
         * triangulate().
         *
         * This is a zero-based index into the vertices added by repeated calls to
         * add_vertex().
         */
        """
        pass

    def getTriangleV2(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_triangle_v2(Triangulator self, int n)
        
        /**
         * Returns vertex 2 of the nth triangle generated by the previous call to
         * triangulate().
         *
         * This is a zero-based index into the vertices added by repeated calls to
         * add_vertex().
         */
        """
        pass

    def getVertex(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_vertex(Triangulator self, int n)
        
        /**
         * Returns the nth vertex.
         */
        """
        pass

    def getVertices(self, *args, **kwargs): # real signature unknown
        pass

    def get_num_triangles(self, Triangulator_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_triangles(Triangulator self)
        
        /**
         * Returns the number of triangles generated by the previous call to
         * triangulate().
         */
        """
        pass

    def get_num_vertices(self, Triangulator_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_vertices(Triangulator self)
        
        /**
         * Returns the number of vertices in the pool.  Note that the Triangulator
         * might append new vertices, in addition to those added by the user, if any
         * of the polygon is self-intersecting, or if any of the holes intersect some
         * part of the polygon edges.
         */
        """
        pass

    def get_triangle_v0(self, Triangulator_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_triangle_v0(Triangulator self, int n)
        
        /**
         * Returns vertex 0 of the nth triangle generated by the previous call to
         * triangulate().
         *
         * This is a zero-based index into the vertices added by repeated calls to
         * add_vertex().
         */
        """
        pass

    def get_triangle_v1(self, Triangulator_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_triangle_v1(Triangulator self, int n)
        
        /**
         * Returns vertex 1 of the nth triangle generated by the previous call to
         * triangulate().
         *
         * This is a zero-based index into the vertices added by repeated calls to
         * add_vertex().
         */
        """
        pass

    def get_triangle_v2(self, Triangulator_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_triangle_v2(Triangulator self, int n)
        
        /**
         * Returns vertex 2 of the nth triangle generated by the previous call to
         * triangulate().
         *
         * This is a zero-based index into the vertices added by repeated calls to
         * add_vertex().
         */
        """
        pass

    def get_vertex(self, Triangulator_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_vertex(Triangulator self, int n)
        
        /**
         * Returns the nth vertex.
         */
        """
        pass

    def get_vertices(self, *args, **kwargs): # real signature unknown
        pass

    def isLeftWinding(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_left_winding(Triangulator self)
        
        /**
         * Returns true if the polygon vertices are listed in counterclockwise order,
         * or false if they appear to be listed in clockwise order.
         */
        """
        pass

    def is_left_winding(self, Triangulator_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_left_winding(Triangulator self)
        
        /**
         * Returns true if the polygon vertices are listed in counterclockwise order,
         * or false if they appear to be listed in clockwise order.
         */
        """
        pass

    def triangulate(self, const_Triangulator_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        triangulate(const Triangulator self)
        
        /**
         * Does the work of triangulating the specified polygon.  After this call, you
         * may retrieve the new triangles one at a time by iterating through
         * get_triangle_v0/1/2().
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

    vertices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.Triangulator' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.Triangulator' objects>"
        '__doc__': "/**\n * This class can triangulate a convex or concave polygon, even one with\n * holes.  It is adapted from an algorithm published as:\n *\n * Narkhede A. and Manocha D., Fast polygon triangulation algorithm based on\n * Seidel's Algorithm, UNC-CH, 1994.\n *\n * http://www.cs.unc.edu/~dm/CODE/GEM/chapter.html\n *\n * It works strictly on 2-d points.  See Triangulator3 for 3-d points.\n */",
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.Triangulator' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE3435B0>'
        'addHoleVertex': None, # (!) real value is "<method 'addHoleVertex' of 'panda3d.core.Triangulator' objects>"
        'addPolygonVertex': None, # (!) real value is "<method 'addPolygonVertex' of 'panda3d.core.Triangulator' objects>"
        'addVertex': None, # (!) real value is "<method 'addVertex' of 'panda3d.core.Triangulator' objects>"
        'add_hole_vertex': None, # (!) real value is "<method 'add_hole_vertex' of 'panda3d.core.Triangulator' objects>"
        'add_polygon_vertex': None, # (!) real value is "<method 'add_polygon_vertex' of 'panda3d.core.Triangulator' objects>"
        'add_vertex': None, # (!) real value is "<method 'add_vertex' of 'panda3d.core.Triangulator' objects>"
        'beginHole': None, # (!) real value is "<method 'beginHole' of 'panda3d.core.Triangulator' objects>"
        'begin_hole': None, # (!) real value is "<method 'begin_hole' of 'panda3d.core.Triangulator' objects>"
        'clear': None, # (!) real value is "<method 'clear' of 'panda3d.core.Triangulator' objects>"
        'clearPolygon': None, # (!) real value is "<method 'clearPolygon' of 'panda3d.core.Triangulator' objects>"
        'clear_polygon': None, # (!) real value is "<method 'clear_polygon' of 'panda3d.core.Triangulator' objects>"
        'getNumTriangles': None, # (!) real value is "<method 'getNumTriangles' of 'panda3d.core.Triangulator' objects>"
        'getNumVertices': None, # (!) real value is "<method 'getNumVertices' of 'panda3d.core.Triangulator' objects>"
        'getTriangleV0': None, # (!) real value is "<method 'getTriangleV0' of 'panda3d.core.Triangulator' objects>"
        'getTriangleV1': None, # (!) real value is "<method 'getTriangleV1' of 'panda3d.core.Triangulator' objects>"
        'getTriangleV2': None, # (!) real value is "<method 'getTriangleV2' of 'panda3d.core.Triangulator' objects>"
        'getVertex': None, # (!) real value is "<method 'getVertex' of 'panda3d.core.Triangulator' objects>"
        'getVertices': None, # (!) real value is "<method 'getVertices' of 'panda3d.core.Triangulator' objects>"
        'get_num_triangles': None, # (!) real value is "<method 'get_num_triangles' of 'panda3d.core.Triangulator' objects>"
        'get_num_vertices': None, # (!) real value is "<method 'get_num_vertices' of 'panda3d.core.Triangulator' objects>"
        'get_triangle_v0': None, # (!) real value is "<method 'get_triangle_v0' of 'panda3d.core.Triangulator' objects>"
        'get_triangle_v1': None, # (!) real value is "<method 'get_triangle_v1' of 'panda3d.core.Triangulator' objects>"
        'get_triangle_v2': None, # (!) real value is "<method 'get_triangle_v2' of 'panda3d.core.Triangulator' objects>"
        'get_vertex': None, # (!) real value is "<method 'get_vertex' of 'panda3d.core.Triangulator' objects>"
        'get_vertices': None, # (!) real value is "<method 'get_vertices' of 'panda3d.core.Triangulator' objects>"
        'isLeftWinding': None, # (!) real value is "<method 'isLeftWinding' of 'panda3d.core.Triangulator' objects>"
        'is_left_winding': None, # (!) real value is "<method 'is_left_winding' of 'panda3d.core.Triangulator' objects>"
        'triangulate': None, # (!) real value is "<method 'triangulate' of 'panda3d.core.Triangulator' objects>"
        'vertices': None, # (!) real value is "<attribute 'vertices' of 'panda3d.core.Triangulator' objects>"
    }


