# encoding: utf-8
# module panda3d.bullet
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\bullet.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import panda3d.core as __panda3d_core


from .BulletShape import BulletShape

class BulletCapsuleShape(BulletShape):
    """
    /**
     *
     */
    """
    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getHalfHeight(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_half_height(BulletCapsuleShape self)
        
        /**
         * Returns half of get_height().
         * @deprecated see get_height() instead.
         */
        """
        pass

    def getRadius(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_radius(BulletCapsuleShape self)
        
        /**
         * Returns the radius that was used to construct this capsule.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_half_height(self, BulletCapsuleShape_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_half_height(BulletCapsuleShape self)
        
        /**
         * Returns half of get_height().
         * @deprecated see get_height() instead.
         */
        """
        pass

    def get_radius(self, BulletCapsuleShape_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_radius(BulletCapsuleShape self)
        
        /**
         * Returns the radius that was used to construct this capsule.
         */
        """
        pass

    def makeFromSolid(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_from_solid(const CollisionCapsule solid)
        
        /**
         * Constructs a new BulletCapsuleShape using the information from a
         * CollisionCapsule from the builtin collision system.
         */
        """
        pass

    def make_from_solid(self, const_CollisionCapsule_solid): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_from_solid(const CollisionCapsule solid)
        
        /**
         * Constructs a new BulletCapsuleShape using the information from a
         * CollisionCapsule from the builtin collision system.
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

    height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    radius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.bullet.BulletCapsuleShape' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.bullet.BulletCapsuleShape' objects>"
        '__doc__': '/**\n *\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.bullet.BulletCapsuleShape' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDC68CCD40>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFDC68CCD40>)>'
        'getHalfHeight': None, # (!) real value is "<method 'getHalfHeight' of 'panda3d.bullet.BulletCapsuleShape' objects>"
        'getRadius': None, # (!) real value is "<method 'getRadius' of 'panda3d.bullet.BulletCapsuleShape' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFDC68CCD40>)>'
        'get_half_height': None, # (!) real value is "<method 'get_half_height' of 'panda3d.bullet.BulletCapsuleShape' objects>"
        'get_radius': None, # (!) real value is "<method 'get_radius' of 'panda3d.bullet.BulletCapsuleShape' objects>"
        'height': None, # (!) real value is "<attribute 'height' of 'panda3d.bullet.BulletCapsuleShape' objects>"
        'makeFromSolid': None, # (!) real value is '<staticmethod(<built-in method makeFromSolid of type object at 0x00007FFDC68CCD40>)>'
        'make_from_solid': None, # (!) real value is '<staticmethod(<built-in method make_from_solid of type object at 0x00007FFDC68CCD40>)>'
        'radius': None, # (!) real value is "<attribute 'radius' of 'panda3d.bullet.BulletCapsuleShape' objects>"
    }


