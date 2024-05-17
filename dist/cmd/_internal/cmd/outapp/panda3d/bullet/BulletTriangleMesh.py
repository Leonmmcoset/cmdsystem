# encoding: utf-8
# module panda3d.bullet
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\bullet.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import panda3d.core as __panda3d_core


class BulletTriangleMesh(__panda3d_core.TypedWritableReferenceCount):
    """
    /**
     *
     */
    """
    def addArray(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_array(const BulletTriangleMesh self, const PointerToArray points, const PointerToArray indices, bool remove_duplicate_vertices)
        
        /**
         * Adds triangle information from an array of points and indices referring to
         * these points.  This is more efficient than adding triangles one at a time.
         *
         * If remove_duplicate_vertices is true, it will make sure that it does not
         * add duplicate vertices if they already exist in the triangle mesh, within
         * the tolerance specified by set_welding_distance().  This comes at a
         * significant performance cost, especially for large meshes.
         */
        """
        pass

    def addGeom(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_geom(const BulletTriangleMesh self, const Geom geom, bool remove_duplicate_vertices, const TransformState ts)
        
        /**
         * Adds the geometry from the indicated Geom from the triangle mesh.  This is
         * a one-time copy operation, and future updates to the Geom will not be
         * reflected.
         *
         * If remove_duplicate_vertices is true, it will make sure that it does not
         * add duplicate vertices if they already exist in the triangle mesh, within
         * the tolerance specified by set_welding_distance().  This comes at a
         * significant performance cost, especially for large meshes.
         */
        """
        pass

    def addTriangle(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_triangle(const BulletTriangleMesh self, const LPoint3f p0, const LPoint3f p1, const LPoint3f p2, bool remove_duplicate_vertices)
        
        /**
         * Adds a triangle with the indicated coordinates.
         *
         * If remove_duplicate_vertices is true, it will make sure that it does not
         * add duplicate vertices if they already exist in the triangle mesh, within
         * the tolerance specified by set_welding_distance().  This comes at a
         * significant performance cost, especially for large meshes.
         */
        """
        pass

    def add_array(self, const_BulletTriangleMesh_self, const_PointerToArray_points, const_PointerToArray_indices, bool_remove_duplicate_vertices): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_array(const BulletTriangleMesh self, const PointerToArray points, const PointerToArray indices, bool remove_duplicate_vertices)
        
        /**
         * Adds triangle information from an array of points and indices referring to
         * these points.  This is more efficient than adding triangles one at a time.
         *
         * If remove_duplicate_vertices is true, it will make sure that it does not
         * add duplicate vertices if they already exist in the triangle mesh, within
         * the tolerance specified by set_welding_distance().  This comes at a
         * significant performance cost, especially for large meshes.
         */
        """
        pass

    def add_geom(self, const_BulletTriangleMesh_self, const_Geom_geom, bool_remove_duplicate_vertices, const_TransformState_ts): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_geom(const BulletTriangleMesh self, const Geom geom, bool remove_duplicate_vertices, const TransformState ts)
        
        /**
         * Adds the geometry from the indicated Geom from the triangle mesh.  This is
         * a one-time copy operation, and future updates to the Geom will not be
         * reflected.
         *
         * If remove_duplicate_vertices is true, it will make sure that it does not
         * add duplicate vertices if they already exist in the triangle mesh, within
         * the tolerance specified by set_welding_distance().  This comes at a
         * significant performance cost, especially for large meshes.
         */
        """
        pass

    def add_triangle(self, const_BulletTriangleMesh_self, const_LPoint3f_p0, const_LPoint3f_p1, const_LPoint3f_p2, bool_remove_duplicate_vertices): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_triangle(const BulletTriangleMesh self, const LPoint3f p0, const LPoint3f p1, const LPoint3f p2, bool remove_duplicate_vertices)
        
        /**
         * Adds a triangle with the indicated coordinates.
         *
         * If remove_duplicate_vertices is true, it will make sure that it does not
         * add duplicate vertices if they already exist in the triangle mesh, within
         * the tolerance specified by set_welding_distance().  This comes at a
         * significant performance cost, especially for large meshes.
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
        get_num_triangles(BulletTriangleMesh self)
        
        /**
         * Returns the number of triangles in this triangle mesh.
         */
        """
        pass

    def getWeldingDistance(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_welding_distance(BulletTriangleMesh self)
        
        /**
         * Returns the value previously set with set_welding_distance(), or the
         * value of 0 if none was set.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_num_triangles(self, BulletTriangleMesh_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_triangles(BulletTriangleMesh self)
        
        /**
         * Returns the number of triangles in this triangle mesh.
         */
        """
        pass

    def get_welding_distance(self, BulletTriangleMesh_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_welding_distance(BulletTriangleMesh self)
        
        /**
         * Returns the value previously set with set_welding_distance(), or the
         * value of 0 if none was set.
         */
        """
        pass

    def output(self, BulletTriangleMesh_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(BulletTriangleMesh self, ostream out)
        
        /**
         *
         */
        """
        pass

    def preallocate(self, const_BulletTriangleMesh_self, int_num_verts, int_num_indices): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        preallocate(const BulletTriangleMesh self, int num_verts, int num_indices)
        
        /**
         * Used to reserve memory in anticipation of the given amount of vertices and
         * indices being added to the triangle mesh.  This is useful if you are about
         * to call add_triangle() many times, to prevent unnecessary reallocations.
         */
        """
        pass

    def setWeldingDistance(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_welding_distance(const BulletTriangleMesh self, float distance)
        
        /**
         * Sets the square of the distance at which vertices will be merged
         * together when adding geometry with remove_duplicate_vertices set to true.
         *
         * The default is 0, meaning vertices will only be merged if they have the
         * exact same position.
         */
        """
        pass

    def set_welding_distance(self, const_BulletTriangleMesh_self, float_distance): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_welding_distance(const BulletTriangleMesh self, float distance)
        
        /**
         * Sets the square of the distance at which vertices will be merged
         * together when adding geometry with remove_duplicate_vertices set to true.
         *
         * The default is 0, meaning vertices will only be merged if they have the
         * exact same position.
         */
        """
        pass

    def write(self, BulletTriangleMesh_self, ostream_out, int_indent_level): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(BulletTriangleMesh self, ostream out, int indent_level)
        
        /**
         *
         */
        """
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

    triangles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    vertices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    welding_distance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n *\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.bullet.BulletTriangleMesh' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDC68D1D00>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.bullet.BulletTriangleMesh' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.bullet.BulletTriangleMesh' objects>"
        'addArray': None, # (!) real value is "<method 'addArray' of 'panda3d.bullet.BulletTriangleMesh' objects>"
        'addGeom': None, # (!) real value is "<method 'addGeom' of 'panda3d.bullet.BulletTriangleMesh' objects>"
        'addTriangle': None, # (!) real value is "<method 'addTriangle' of 'panda3d.bullet.BulletTriangleMesh' objects>"
        'add_array': None, # (!) real value is "<method 'add_array' of 'panda3d.bullet.BulletTriangleMesh' objects>"
        'add_geom': None, # (!) real value is "<method 'add_geom' of 'panda3d.bullet.BulletTriangleMesh' objects>"
        'add_triangle': None, # (!) real value is "<method 'add_triangle' of 'panda3d.bullet.BulletTriangleMesh' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFDC68D1D00>)>'
        'getNumTriangles': None, # (!) real value is "<method 'getNumTriangles' of 'panda3d.bullet.BulletTriangleMesh' objects>"
        'getWeldingDistance': None, # (!) real value is "<method 'getWeldingDistance' of 'panda3d.bullet.BulletTriangleMesh' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFDC68D1D00>)>'
        'get_num_triangles': None, # (!) real value is "<method 'get_num_triangles' of 'panda3d.bullet.BulletTriangleMesh' objects>"
        'get_welding_distance': None, # (!) real value is "<method 'get_welding_distance' of 'panda3d.bullet.BulletTriangleMesh' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.bullet.BulletTriangleMesh' objects>"
        'preallocate': None, # (!) real value is "<method 'preallocate' of 'panda3d.bullet.BulletTriangleMesh' objects>"
        'setWeldingDistance': None, # (!) real value is "<method 'setWeldingDistance' of 'panda3d.bullet.BulletTriangleMesh' objects>"
        'set_welding_distance': None, # (!) real value is "<method 'set_welding_distance' of 'panda3d.bullet.BulletTriangleMesh' objects>"
        'triangles': None, # (!) real value is "<attribute 'triangles' of 'panda3d.bullet.BulletTriangleMesh' objects>"
        'vertices': None, # (!) real value is "<attribute 'vertices' of 'panda3d.bullet.BulletTriangleMesh' objects>"
        'welding_distance': None, # (!) real value is "<attribute 'welding_distance' of 'panda3d.bullet.BulletTriangleMesh' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.bullet.BulletTriangleMesh' objects>"
    }


