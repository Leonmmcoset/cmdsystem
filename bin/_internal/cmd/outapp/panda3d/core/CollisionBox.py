# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .CollisionSolid import CollisionSolid

class CollisionBox(CollisionSolid):
    """
    /**
     * A cuboid collision volume or object.
     */
    """
    def getCenter(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_center(CollisionBox self)
        
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

    def getDimensions(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_dimensions(CollisionBox self)
        
        /**
         *
         */
        """
        pass

    def getMax(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_max(CollisionBox self)
        
        /**
         *
         */
        """
        pass

    def getMin(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_min(CollisionBox self)
        
        /**
         *
         */
        """
        pass

    def getNumPlanes(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_planes(CollisionBox self)
        
        /**
         * Returns 6: the number of faces of a rectangular solid.
         */
        """
        pass

    def getNumPoints(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_points(CollisionBox self)
        
        /**
         * Returns 8: the number of vertices of a rectangular solid.
         */
        """
        pass

    def getPlane(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_plane(CollisionBox self, int n)
        
        /**
         * Returns the nth face of the rectangular solid.
         */
        """
        pass

    def getPoint(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_point(CollisionBox self, int n)
        
        /**
         * Returns the nth vertex of the OBB.
         */
        """
        pass

    def getPointAabb(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_point_aabb(CollisionBox self, int n)
        
        /**
         * Returns the nth vertex of the Axis Aligned Bounding Box.
         */
        """
        pass

    def get_center(self, CollisionBox_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_center(CollisionBox self)
        
        /**
         *
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_dimensions(self, CollisionBox_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_dimensions(CollisionBox self)
        
        /**
         *
         */
        """
        pass

    def get_max(self, CollisionBox_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_max(CollisionBox self)
        
        /**
         *
         */
        """
        pass

    def get_min(self, CollisionBox_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_min(CollisionBox self)
        
        /**
         *
         */
        """
        pass

    def get_num_planes(self, CollisionBox_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_planes(CollisionBox self)
        
        /**
         * Returns 6: the number of faces of a rectangular solid.
         */
        """
        pass

    def get_num_points(self, CollisionBox_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_points(CollisionBox self)
        
        /**
         * Returns 8: the number of vertices of a rectangular solid.
         */
        """
        pass

    def get_plane(self, CollisionBox_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_plane(CollisionBox self, int n)
        
        /**
         * Returns the nth face of the rectangular solid.
         */
        """
        pass

    def get_point(self, CollisionBox_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_point(CollisionBox self, int n)
        
        /**
         * Returns the nth vertex of the OBB.
         */
        """
        pass

    def get_point_aabb(self, CollisionBox_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_point_aabb(CollisionBox self, int n)
        
        /**
         * Returns the nth vertex of the Axis Aligned Bounding Box.
         */
        """
        pass

    def setCenter(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_center(const CollisionBox self, const LPoint3f center)
        set_center(const CollisionBox self, float x, float y, float z)
        
        /**
         *
         */
        
        /**
         *
         */
        """
        pass

    def setPlane(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_plane(CollisionBox self, int n)
        
        /**
         * Creates the nth face of the rectangular solid.
         */
        """
        pass

    def set_center(self, const_CollisionBox_self, const_LPoint3f_center): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_center(const CollisionBox self, const LPoint3f center)
        set_center(const CollisionBox self, float x, float y, float z)
        
        /**
         *
         */
        
        /**
         *
         */
        """
        pass

    def set_plane(self, CollisionBox_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_plane(CollisionBox self, int n)
        
        /**
         * Creates the nth face of the rectangular solid.
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    center = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dimensions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    max = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    min = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * A cuboid collision volume or object.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.CollisionBox' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2CDD80>'
        'center': None, # (!) real value is "<attribute 'center' of 'panda3d.core.CollisionBox' objects>"
        'dimensions': None, # (!) real value is "<attribute 'dimensions' of 'panda3d.core.CollisionBox' objects>"
        'getCenter': None, # (!) real value is "<method 'getCenter' of 'panda3d.core.CollisionBox' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2CDD80>)>'
        'getDimensions': None, # (!) real value is "<method 'getDimensions' of 'panda3d.core.CollisionBox' objects>"
        'getMax': None, # (!) real value is "<method 'getMax' of 'panda3d.core.CollisionBox' objects>"
        'getMin': None, # (!) real value is "<method 'getMin' of 'panda3d.core.CollisionBox' objects>"
        'getNumPlanes': None, # (!) real value is "<method 'getNumPlanes' of 'panda3d.core.CollisionBox' objects>"
        'getNumPoints': None, # (!) real value is "<method 'getNumPoints' of 'panda3d.core.CollisionBox' objects>"
        'getPlane': None, # (!) real value is "<method 'getPlane' of 'panda3d.core.CollisionBox' objects>"
        'getPoint': None, # (!) real value is "<method 'getPoint' of 'panda3d.core.CollisionBox' objects>"
        'getPointAabb': None, # (!) real value is "<method 'getPointAabb' of 'panda3d.core.CollisionBox' objects>"
        'get_center': None, # (!) real value is "<method 'get_center' of 'panda3d.core.CollisionBox' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2CDD80>)>'
        'get_dimensions': None, # (!) real value is "<method 'get_dimensions' of 'panda3d.core.CollisionBox' objects>"
        'get_max': None, # (!) real value is "<method 'get_max' of 'panda3d.core.CollisionBox' objects>"
        'get_min': None, # (!) real value is "<method 'get_min' of 'panda3d.core.CollisionBox' objects>"
        'get_num_planes': None, # (!) real value is "<method 'get_num_planes' of 'panda3d.core.CollisionBox' objects>"
        'get_num_points': None, # (!) real value is "<method 'get_num_points' of 'panda3d.core.CollisionBox' objects>"
        'get_plane': None, # (!) real value is "<method 'get_plane' of 'panda3d.core.CollisionBox' objects>"
        'get_point': None, # (!) real value is "<method 'get_point' of 'panda3d.core.CollisionBox' objects>"
        'get_point_aabb': None, # (!) real value is "<method 'get_point_aabb' of 'panda3d.core.CollisionBox' objects>"
        'max': None, # (!) real value is "<attribute 'max' of 'panda3d.core.CollisionBox' objects>"
        'min': None, # (!) real value is "<attribute 'min' of 'panda3d.core.CollisionBox' objects>"
        'setCenter': None, # (!) real value is "<method 'setCenter' of 'panda3d.core.CollisionBox' objects>"
        'setPlane': None, # (!) real value is "<method 'setPlane' of 'panda3d.core.CollisionBox' objects>"
        'set_center': None, # (!) real value is "<method 'set_center' of 'panda3d.core.CollisionBox' objects>"
        'set_plane': None, # (!) real value is "<method 'set_plane' of 'panda3d.core.CollisionBox' objects>"
    }


