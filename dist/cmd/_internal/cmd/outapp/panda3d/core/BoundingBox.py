# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .FiniteBoundingVolume import FiniteBoundingVolume

class BoundingBox(FiniteBoundingVolume):
    """
    /**
     * An axis-aligned bounding box; that is, a minimum and maximum coordinate
     * triple.
     *
     * This box is always axis-aligned.  If you need a more general bounding box,
     * try BoundingHexahedron.
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
        get_num_planes(BoundingBox self)
        
        /**
         * Returns 6: the number of faces of a rectangular solid.
         */
        """
        pass

    def getNumPoints(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_points(BoundingBox self)
        
        /**
         * Returns 8: the number of vertices of a rectangular solid.
         */
        """
        pass

    def getPlane(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_plane(BoundingBox self, int n)
        
        /**
         * Returns the nth face of the rectangular solid.
         */
        """
        pass

    def getPlanes(self, *args, **kwargs): # real signature unknown
        pass

    def getPoint(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_point(BoundingBox self, int n)
        
        /**
         * Returns the nth vertex of the rectangular solid.
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

    def get_num_planes(self, BoundingBox_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_planes(BoundingBox self)
        
        /**
         * Returns 6: the number of faces of a rectangular solid.
         */
        """
        pass

    def get_num_points(self, BoundingBox_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_points(BoundingBox self)
        
        /**
         * Returns 8: the number of vertices of a rectangular solid.
         */
        """
        pass

    def get_plane(self, BoundingBox_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_plane(BoundingBox self, int n)
        
        /**
         * Returns the nth face of the rectangular solid.
         */
        """
        pass

    def get_planes(self, *args, **kwargs): # real signature unknown
        pass

    def get_point(self, BoundingBox_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_point(BoundingBox self, int n)
        
        /**
         * Returns the nth vertex of the rectangular solid.
         */
        """
        pass

    def get_points(self, *args, **kwargs): # real signature unknown
        pass

    def setMinMax(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_min_max(const BoundingBox self, const LPoint3f min, const LPoint3f max)
        
        /**
         * Sets the min and max point of the rectangular solid.
         */
        """
        pass

    def set_min_max(self, const_BoundingBox_self, const_LPoint3f_min, const_LPoint3f_max): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_min_max(const BoundingBox self, const LPoint3f min, const LPoint3f max)
        
        /**
         * Sets the min and max point of the rectangular solid.
         */
        """
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
        '__doc__': '/**\n * An axis-aligned bounding box; that is, a minimum and maximum coordinate\n * triple.\n *\n * This box is always axis-aligned.  If you need a more general bounding box,\n * try BoundingHexahedron.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.BoundingBox' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE3416E0>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE3416E0>)>'
        'getNumPlanes': None, # (!) real value is "<method 'getNumPlanes' of 'panda3d.core.BoundingBox' objects>"
        'getNumPoints': None, # (!) real value is "<method 'getNumPoints' of 'panda3d.core.BoundingBox' objects>"
        'getPlane': None, # (!) real value is "<method 'getPlane' of 'panda3d.core.BoundingBox' objects>"
        'getPlanes': None, # (!) real value is "<method 'getPlanes' of 'panda3d.core.BoundingBox' objects>"
        'getPoint': None, # (!) real value is "<method 'getPoint' of 'panda3d.core.BoundingBox' objects>"
        'getPoints': None, # (!) real value is "<method 'getPoints' of 'panda3d.core.BoundingBox' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE3416E0>)>'
        'get_num_planes': None, # (!) real value is "<method 'get_num_planes' of 'panda3d.core.BoundingBox' objects>"
        'get_num_points': None, # (!) real value is "<method 'get_num_points' of 'panda3d.core.BoundingBox' objects>"
        'get_plane': None, # (!) real value is "<method 'get_plane' of 'panda3d.core.BoundingBox' objects>"
        'get_planes': None, # (!) real value is "<method 'get_planes' of 'panda3d.core.BoundingBox' objects>"
        'get_point': None, # (!) real value is "<method 'get_point' of 'panda3d.core.BoundingBox' objects>"
        'get_points': None, # (!) real value is "<method 'get_points' of 'panda3d.core.BoundingBox' objects>"
        'planes': None, # (!) real value is "<attribute 'planes' of 'panda3d.core.BoundingBox' objects>"
        'points': None, # (!) real value is "<attribute 'points' of 'panda3d.core.BoundingBox' objects>"
        'setMinMax': None, # (!) real value is "<method 'setMinMax' of 'panda3d.core.BoundingBox' objects>"
        'set_min_max': None, # (!) real value is "<method 'set_min_max' of 'panda3d.core.BoundingBox' objects>"
    }


