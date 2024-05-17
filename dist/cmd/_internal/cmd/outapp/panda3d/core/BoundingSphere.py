# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .FiniteBoundingVolume import FiniteBoundingVolume

class BoundingSphere(FiniteBoundingVolume):
    """
    /**
     * This defines a bounding sphere, consisting of a center and a radius.  It is
     * always a sphere, and never an ellipsoid or other quadric.
     */
    """
    def getCenter(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_center(BoundingSphere self)
        
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

    def getRadius(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_radius(BoundingSphere self)
        
        /**
         *
         */
        """
        pass

    def get_center(self, BoundingSphere_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_center(BoundingSphere self)
        
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

    def get_radius(self, BoundingSphere_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_radius(BoundingSphere self)
        
        /**
         *
         */
        """
        pass

    def setCenter(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_center(const BoundingSphere self, const LPoint3f center)
        
        /**
         * Sets the center point of the sphere.
         */
        """
        pass

    def setRadius(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_radius(const BoundingSphere self, float radius)
        
        /**
         * Sets the radius of the sphere.
         */
        """
        pass

    def set_center(self, const_BoundingSphere_self, const_LPoint3f_center): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_center(const BoundingSphere self, const LPoint3f center)
        
        /**
         * Sets the center point of the sphere.
         */
        """
        pass

    def set_radius(self, const_BoundingSphere_self, float_radius): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_radius(const BoundingSphere self, float radius)
        
        /**
         * Sets the radius of the sphere.
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

    radius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * This defines a bounding sphere, consisting of a center and a radius.  It is\n * always a sphere, and never an ellipsoid or other quadric.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.BoundingSphere' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE3421C0>'
        'center': None, # (!) real value is "<attribute 'center' of 'panda3d.core.BoundingSphere' objects>"
        'getCenter': None, # (!) real value is "<method 'getCenter' of 'panda3d.core.BoundingSphere' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE3421C0>)>'
        'getRadius': None, # (!) real value is "<method 'getRadius' of 'panda3d.core.BoundingSphere' objects>"
        'get_center': None, # (!) real value is "<method 'get_center' of 'panda3d.core.BoundingSphere' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE3421C0>)>'
        'get_radius': None, # (!) real value is "<method 'get_radius' of 'panda3d.core.BoundingSphere' objects>"
        'radius': None, # (!) real value is "<attribute 'radius' of 'panda3d.core.BoundingSphere' objects>"
        'setCenter': None, # (!) real value is "<method 'setCenter' of 'panda3d.core.BoundingSphere' objects>"
        'setRadius': None, # (!) real value is "<method 'setRadius' of 'panda3d.core.BoundingSphere' objects>"
        'set_center': None, # (!) real value is "<method 'set_center' of 'panda3d.core.BoundingSphere' objects>"
        'set_radius': None, # (!) real value is "<method 'set_radius' of 'panda3d.core.BoundingSphere' objects>"
    }


