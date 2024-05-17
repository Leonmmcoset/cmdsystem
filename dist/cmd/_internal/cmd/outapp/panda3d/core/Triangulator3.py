# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .Triangulator import Triangulator

class Triangulator3(Triangulator):
    """
    /**
     * This is an extension of Triangulator to handle polygons with three-
     * dimensional points.  It assumes all of the points lie in a single plane,
     * and internally projects the supplied points into 2-D for passing to the
     * underlying Triangulator object.
     */
    """
    def addVertex(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_vertex(const Triangulator3 self, const LPoint3d point)
        add_vertex(const Triangulator3 self, double x, double y, double z)
        
        /**
         * Adds a new vertex to the vertex pool.  Returns the vertex index number.
         */
        
        /**
         * Adds a new vertex to the vertex pool.  Returns the vertex index number.
         */
        """
        pass

    def add_vertex(self, const_Triangulator3_self, const_LPoint3d_point): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_vertex(const Triangulator3 self, const LPoint3d point)
        add_vertex(const Triangulator3 self, double x, double y, double z)
        
        /**
         * Adds a new vertex to the vertex pool.  Returns the vertex index number.
         */
        
        /**
         * Adds a new vertex to the vertex pool.  Returns the vertex index number.
         */
        """
        pass

    def clear(self, const_Triangulator3_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear(const Triangulator3 self)
        
        /**
         * Removes all vertices and polygon specifications from the Triangulator, and
         * prepares it to start over.
         */
        """
        pass

    def getNumVertices(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_vertices(Triangulator3 self)
        
        /**
         * Returns the number of vertices in the pool.  Note that the Triangulator
         * might append new vertices, in addition to those added by the user, if any
         * of the polygon is self-intersecting, or if any of the holes intersect some
         * part of the polygon edges.
         */
        """
        pass

    def getPlane(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_plane(Triangulator3 self)
        
        /**
         * Returns the plane of the polygon.  This is only available after calling
         * triangulate().
         */
        """
        pass

    def getVertex(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_vertex(Triangulator3 self, int n)
        
        /**
         * Returns the nth vertex.
         */
        """
        pass

    def getVertices(self, *args, **kwargs): # real signature unknown
        pass

    def get_num_vertices(self, Triangulator3_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_vertices(Triangulator3 self)
        
        /**
         * Returns the number of vertices in the pool.  Note that the Triangulator
         * might append new vertices, in addition to those added by the user, if any
         * of the polygon is self-intersecting, or if any of the holes intersect some
         * part of the polygon edges.
         */
        """
        pass

    def get_plane(self, Triangulator3_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_plane(Triangulator3 self)
        
        /**
         * Returns the plane of the polygon.  This is only available after calling
         * triangulate().
         */
        """
        pass

    def get_vertex(self, Triangulator3_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_vertex(Triangulator3 self, int n)
        
        /**
         * Returns the nth vertex.
         */
        """
        pass

    def get_vertices(self, *args, **kwargs): # real signature unknown
        pass

    def triangulate(self, const_Triangulator3_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        triangulate(const Triangulator3 self)
        
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

    plane = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    vertices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.Triangulator3' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.Triangulator3' objects>"
        '__doc__': '/**\n * This is an extension of Triangulator to handle polygons with three-\n * dimensional points.  It assumes all of the points lie in a single plane,\n * and internally projects the supplied points into 2-D for passing to the\n * underlying Triangulator object.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.Triangulator3' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE343780>'
        'addVertex': None, # (!) real value is "<method 'addVertex' of 'panda3d.core.Triangulator3' objects>"
        'add_vertex': None, # (!) real value is "<method 'add_vertex' of 'panda3d.core.Triangulator3' objects>"
        'clear': None, # (!) real value is "<method 'clear' of 'panda3d.core.Triangulator3' objects>"
        'getNumVertices': None, # (!) real value is "<method 'getNumVertices' of 'panda3d.core.Triangulator3' objects>"
        'getPlane': None, # (!) real value is "<method 'getPlane' of 'panda3d.core.Triangulator3' objects>"
        'getVertex': None, # (!) real value is "<method 'getVertex' of 'panda3d.core.Triangulator3' objects>"
        'getVertices': None, # (!) real value is "<method 'getVertices' of 'panda3d.core.Triangulator3' objects>"
        'get_num_vertices': None, # (!) real value is "<method 'get_num_vertices' of 'panda3d.core.Triangulator3' objects>"
        'get_plane': None, # (!) real value is "<method 'get_plane' of 'panda3d.core.Triangulator3' objects>"
        'get_vertex': None, # (!) real value is "<method 'get_vertex' of 'panda3d.core.Triangulator3' objects>"
        'get_vertices': None, # (!) real value is "<method 'get_vertices' of 'panda3d.core.Triangulator3' objects>"
        'plane': None, # (!) real value is "<attribute 'plane' of 'panda3d.core.Triangulator3' objects>"
        'triangulate': None, # (!) real value is "<method 'triangulate' of 'panda3d.core.Triangulator3' objects>"
        'vertices': None, # (!) real value is "<attribute 'vertices' of 'panda3d.core.Triangulator3' objects>"
    }


