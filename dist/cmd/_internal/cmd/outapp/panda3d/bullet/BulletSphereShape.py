# encoding: utf-8
# module panda3d.bullet
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\bullet.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import panda3d.core as __panda3d_core


from .BulletShape import BulletShape

class BulletSphereShape(BulletShape):
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

    def getRadius(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_radius(BulletSphereShape self)
        
        /**
         * Returns the radius that was used to construct this sphere.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_radius(self, BulletSphereShape_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_radius(BulletSphereShape self)
        
        /**
         * Returns the radius that was used to construct this sphere.
         */
        """
        pass

    def makeFromSolid(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_from_solid(const CollisionSphere solid)
        
        /**
         *
         */
        """
        pass

    def make_from_solid(self, const_CollisionSphere_solid): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_from_solid(const CollisionSphere solid)
        
        /**
         *
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

    radius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.bullet.BulletSphereShape' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.bullet.BulletSphereShape' objects>"
        '__doc__': '/**\n *\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.bullet.BulletSphereShape' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDC68D1790>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFDC68D1790>)>'
        'getRadius': None, # (!) real value is "<method 'getRadius' of 'panda3d.bullet.BulletSphereShape' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFDC68D1790>)>'
        'get_radius': None, # (!) real value is "<method 'get_radius' of 'panda3d.bullet.BulletSphereShape' objects>"
        'makeFromSolid': None, # (!) real value is '<staticmethod(<built-in method makeFromSolid of type object at 0x00007FFDC68D1790>)>'
        'make_from_solid': None, # (!) real value is '<staticmethod(<built-in method make_from_solid of type object at 0x00007FFDC68D1790>)>'
        'radius': None, # (!) real value is "<attribute 'radius' of 'panda3d.bullet.BulletSphereShape' objects>"
    }


