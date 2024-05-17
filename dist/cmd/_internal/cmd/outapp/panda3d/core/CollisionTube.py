# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .CollisionSolid import CollisionSolid

class CollisionTube(CollisionSolid):
    """
    /**
     * This implements a solid consisting of a cylinder with hemispherical endcaps,
     * also known as a capsule or a spherocylinder.
     *
     * This shape was previously erroneously called CollisionTube.
     */
    """
    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getPointA(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_point_a(CollisionCapsule self)
        
        /**
         *
         */
        """
        pass

    def getPointB(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_point_b(CollisionCapsule self)
        
        /**
         *
         */
        """
        pass

    def getRadius(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_radius(CollisionCapsule self)
        
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

    def get_point_a(self, CollisionCapsule_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_point_a(CollisionCapsule self)
        
        /**
         *
         */
        """
        pass

    def get_point_b(self, CollisionCapsule_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_point_b(CollisionCapsule self)
        
        /**
         *
         */
        """
        pass

    def get_radius(self, CollisionCapsule_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_radius(CollisionCapsule self)
        
        /**
         *
         */
        """
        pass

    def setPointA(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_point_a(const CollisionCapsule self, const LPoint3f a)
        set_point_a(const CollisionCapsule self, float x, float y, float z)
        
        /**
         *
         */
        
        /**
         *
         */
        """
        pass

    def setPointB(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_point_b(const CollisionCapsule self, const LPoint3f b)
        set_point_b(const CollisionCapsule self, float x, float y, float z)
        
        /**
         *
         */
        
        /**
         *
         */
        """
        pass

    def setRadius(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_radius(const CollisionCapsule self, float radius)
        
        /**
         *
         */
        """
        pass

    def set_point_a(self, const_CollisionCapsule_self, const_LPoint3f_a): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_point_a(const CollisionCapsule self, const LPoint3f a)
        set_point_a(const CollisionCapsule self, float x, float y, float z)
        
        /**
         *
         */
        
        /**
         *
         */
        """
        pass

    def set_point_b(self, const_CollisionCapsule_self, const_LPoint3f_b): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_point_b(const CollisionCapsule self, const LPoint3f b)
        set_point_b(const CollisionCapsule self, float x, float y, float z)
        
        /**
         *
         */
        
        /**
         *
         */
        """
        pass

    def set_radius(self, const_CollisionCapsule_self, float_radius): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_radius(const CollisionCapsule self, float radius)
        
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

    point_a = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    point_b = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    radius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * This implements a solid consisting of a cylinder with hemispherical endcaps,\n * also known as a capsule or a spherocylinder.\n *\n * This shape was previously erroneously called CollisionTube.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.CollisionCapsule' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2CDF50>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2CDF50>)>'
        'getPointA': None, # (!) real value is "<method 'getPointA' of 'panda3d.core.CollisionCapsule' objects>"
        'getPointB': None, # (!) real value is "<method 'getPointB' of 'panda3d.core.CollisionCapsule' objects>"
        'getRadius': None, # (!) real value is "<method 'getRadius' of 'panda3d.core.CollisionCapsule' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2CDF50>)>'
        'get_point_a': None, # (!) real value is "<method 'get_point_a' of 'panda3d.core.CollisionCapsule' objects>"
        'get_point_b': None, # (!) real value is "<method 'get_point_b' of 'panda3d.core.CollisionCapsule' objects>"
        'get_radius': None, # (!) real value is "<method 'get_radius' of 'panda3d.core.CollisionCapsule' objects>"
        'point_a': None, # (!) real value is "<attribute 'point_a' of 'panda3d.core.CollisionCapsule' objects>"
        'point_b': None, # (!) real value is "<attribute 'point_b' of 'panda3d.core.CollisionCapsule' objects>"
        'radius': None, # (!) real value is "<attribute 'radius' of 'panda3d.core.CollisionCapsule' objects>"
        'setPointA': None, # (!) real value is "<method 'setPointA' of 'panda3d.core.CollisionCapsule' objects>"
        'setPointB': None, # (!) real value is "<method 'setPointB' of 'panda3d.core.CollisionCapsule' objects>"
        'setRadius': None, # (!) real value is "<method 'setRadius' of 'panda3d.core.CollisionCapsule' objects>"
        'set_point_a': None, # (!) real value is "<method 'set_point_a' of 'panda3d.core.CollisionCapsule' objects>"
        'set_point_b': None, # (!) real value is "<method 'set_point_b' of 'panda3d.core.CollisionCapsule' objects>"
        'set_radius': None, # (!) real value is "<method 'set_radius' of 'panda3d.core.CollisionCapsule' objects>"
    }


