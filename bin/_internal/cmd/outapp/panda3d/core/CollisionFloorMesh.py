# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .CollisionSolid import CollisionSolid

class CollisionFloorMesh(CollisionSolid):
    """
    /**
     * This object represents a solid made entirely of triangles, which will only
     * be tested again z axis aligned rays
     */
    """
    def addTriangle(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_triangle(const CollisionFloorMesh self, int pointA, int pointB, int pointC)
        
        /**
         * store a triangle for processing
         */
        """
        pass

    def addVertex(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_vertex(const CollisionFloorMesh self, const LPoint3f vert)
        
        /**
         * store away a vertex to index against
         */
        """
        pass

    def add_triangle(self, const_CollisionFloorMesh_self, int_pointA, int_pointB, int_pointC): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_triangle(const CollisionFloorMesh self, int pointA, int pointB, int pointC)
        
        /**
         * store a triangle for processing
         */
        """
        pass

    def add_vertex(self, const_CollisionFloorMesh_self, const_LPoint3f_vert): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_vertex(const CollisionFloorMesh self, const LPoint3f vert)
        
        /**
         * store away a vertex to index against
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getNumTriangles(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_triangles(CollisionFloorMesh self)
        """
        pass

    def getNumVertices(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_vertices(CollisionFloorMesh self)
        """
        pass

    def getTriangle(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_triangle(CollisionFloorMesh self, int index)
        """
        pass

    def getTriangles(self, *args, **kwargs): # real signature unknown
        pass

    def getVertex(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_vertex(CollisionFloorMesh self, int index)
        """
        pass

    def getVertices(self, *args, **kwargs): # real signature unknown
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_num_triangles(self, CollisionFloorMesh_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_triangles(CollisionFloorMesh self)
        """
        pass

    def get_num_vertices(self, CollisionFloorMesh_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_vertices(CollisionFloorMesh self)
        """
        pass

    def get_triangle(self, CollisionFloorMesh_self, int_index): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_triangle(CollisionFloorMesh self, int index)
        """
        pass

    def get_triangles(self, *args, **kwargs): # real signature unknown
        pass

    def get_vertex(self, CollisionFloorMesh_self, int_index): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_vertex(CollisionFloorMesh self, int index)
        """
        pass

    def get_vertices(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    triangles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    vertices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * This object represents a solid made entirely of triangles, which will only\n * be tested again z axis aligned rays\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.CollisionFloorMesh' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2CEC00>'
        'addTriangle': None, # (!) real value is "<method 'addTriangle' of 'panda3d.core.CollisionFloorMesh' objects>"
        'addVertex': None, # (!) real value is "<method 'addVertex' of 'panda3d.core.CollisionFloorMesh' objects>"
        'add_triangle': None, # (!) real value is "<method 'add_triangle' of 'panda3d.core.CollisionFloorMesh' objects>"
        'add_vertex': None, # (!) real value is "<method 'add_vertex' of 'panda3d.core.CollisionFloorMesh' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2CEC00>)>'
        'getNumTriangles': None, # (!) real value is "<method 'getNumTriangles' of 'panda3d.core.CollisionFloorMesh' objects>"
        'getNumVertices': None, # (!) real value is "<method 'getNumVertices' of 'panda3d.core.CollisionFloorMesh' objects>"
        'getTriangle': None, # (!) real value is "<method 'getTriangle' of 'panda3d.core.CollisionFloorMesh' objects>"
        'getTriangles': None, # (!) real value is "<method 'getTriangles' of 'panda3d.core.CollisionFloorMesh' objects>"
        'getVertex': None, # (!) real value is "<method 'getVertex' of 'panda3d.core.CollisionFloorMesh' objects>"
        'getVertices': None, # (!) real value is "<method 'getVertices' of 'panda3d.core.CollisionFloorMesh' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2CEC00>)>'
        'get_num_triangles': None, # (!) real value is "<method 'get_num_triangles' of 'panda3d.core.CollisionFloorMesh' objects>"
        'get_num_vertices': None, # (!) real value is "<method 'get_num_vertices' of 'panda3d.core.CollisionFloorMesh' objects>"
        'get_triangle': None, # (!) real value is "<method 'get_triangle' of 'panda3d.core.CollisionFloorMesh' objects>"
        'get_triangles': None, # (!) real value is "<method 'get_triangles' of 'panda3d.core.CollisionFloorMesh' objects>"
        'get_vertex': None, # (!) real value is "<method 'get_vertex' of 'panda3d.core.CollisionFloorMesh' objects>"
        'get_vertices': None, # (!) real value is "<method 'get_vertices' of 'panda3d.core.CollisionFloorMesh' objects>"
        'triangles': None, # (!) real value is "<attribute 'triangles' of 'panda3d.core.CollisionFloorMesh' objects>"
        'vertices': None, # (!) real value is "<attribute 'vertices' of 'panda3d.core.CollisionFloorMesh' objects>"
    }


