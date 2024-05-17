# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .FiniteBoundingVolume import FiniteBoundingVolume

class BoundingHexahedron(FiniteBoundingVolume):
    """
    /**
     * This defines a bounding convex hexahedron.  It is typically used to
     * represent a frustum, but may represent any enclosing convex hexahedron,
     * including simple boxes.  However, if all you want is an axis-aligned
     * bounding box, you may be better off with the simpler BoundingBox class.
     */
    """
    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getNumPlanes(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_planes(BoundingHexahedron self)
        
        /**
         * Returns 6: the number of faces of a hexahedron.
         */
        """
        pass

    def getNumPoints(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_points(BoundingHexahedron self)
        
        /**
         * Returns 8: the number of vertices of a hexahedron.
         */
        """
        pass

    def getPlane(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_plane(BoundingHexahedron self, int n)
        
        /**
         * Returns the nth face of the hexahedron.
         */
        """
        pass

    def getPlanes(self, *args, **kwargs): # real signature unknown
        pass

    def getPoint(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_point(BoundingHexahedron self, int n)
        
        /**
         * Returns the nth vertex of the hexahedron.
         */
        """
        pass

    def getPoints(self, *args, **kwargs): # real signature unknown
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_num_planes(self, BoundingHexahedron_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_planes(BoundingHexahedron self)
        
        /**
         * Returns 6: the number of faces of a hexahedron.
         */
        """
        pass

    def get_num_points(self, BoundingHexahedron_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_points(BoundingHexahedron self)
        
        /**
         * Returns 8: the number of vertices of a hexahedron.
         */
        """
        pass

    def get_plane(self, BoundingHexahedron_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_plane(BoundingHexahedron self, int n)
        
        /**
         * Returns the nth face of the hexahedron.
         */
        """
        pass

    def get_planes(self, *args, **kwargs): # real signature unknown
        pass

    def get_point(self, BoundingHexahedron_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_point(BoundingHexahedron self, int n)
        
        /**
         * Returns the nth vertex of the hexahedron.
         */
        """
        pass

    def get_points(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    planes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    points = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * This defines a bounding convex hexahedron.  It is typically used to\n * represent a frustum, but may represent any enclosing convex hexahedron,\n * including simple boxes.  However, if all you want is an axis-aligned\n * bounding box, you may be better off with the simpler BoundingBox class.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.BoundingHexahedron' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE341C50>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE341C50>)>'
        'getNumPlanes': None, # (!) real value is "<method 'getNumPlanes' of 'panda3d.core.BoundingHexahedron' objects>"
        'getNumPoints': None, # (!) real value is "<method 'getNumPoints' of 'panda3d.core.BoundingHexahedron' objects>"
        'getPlane': None, # (!) real value is "<method 'getPlane' of 'panda3d.core.BoundingHexahedron' objects>"
        'getPlanes': None, # (!) real value is "<method 'getPlanes' of 'panda3d.core.BoundingHexahedron' objects>"
        'getPoint': None, # (!) real value is "<method 'getPoint' of 'panda3d.core.BoundingHexahedron' objects>"
        'getPoints': None, # (!) real value is "<method 'getPoints' of 'panda3d.core.BoundingHexahedron' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE341C50>)>'
        'get_num_planes': None, # (!) real value is "<method 'get_num_planes' of 'panda3d.core.BoundingHexahedron' objects>"
        'get_num_points': None, # (!) real value is "<method 'get_num_points' of 'panda3d.core.BoundingHexahedron' objects>"
        'get_plane': None, # (!) real value is "<method 'get_plane' of 'panda3d.core.BoundingHexahedron' objects>"
        'get_planes': None, # (!) real value is "<method 'get_planes' of 'panda3d.core.BoundingHexahedron' objects>"
        'get_point': None, # (!) real value is "<method 'get_point' of 'panda3d.core.BoundingHexahedron' objects>"
        'get_points': None, # (!) real value is "<method 'get_points' of 'panda3d.core.BoundingHexahedron' objects>"
        'planes': None, # (!) real value is "<attribute 'planes' of 'panda3d.core.BoundingHexahedron' objects>"
        'points': None, # (!) real value is "<attribute 'points' of 'panda3d.core.BoundingHexahedron' objects>"
    }


