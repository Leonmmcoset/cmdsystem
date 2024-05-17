# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .GeometricBoundingVolume import GeometricBoundingVolume

class BoundingPlane(GeometricBoundingVolume):
    """
    /**
     * This funny bounding volume is an infinite plane that divides space into two
     * regions: the part behind the normal, which is "inside" the bounding volume,
     * and the part in front of the normal, which is "outside" the bounding
     * volume.
     */
    """
    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getPlane(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_plane(BoundingPlane self)
        
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

    def get_plane(self, BoundingPlane_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_plane(BoundingPlane self)
        
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

    plane = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * This funny bounding volume is an infinite plane that divides space into two\n * regions: the part behind the normal, which is "inside" the bounding volume,\n * and the part in front of the normal, which is "outside" the bounding\n * volume.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.BoundingPlane' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE341FF0>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE341FF0>)>'
        'getPlane': None, # (!) real value is "<method 'getPlane' of 'panda3d.core.BoundingPlane' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE341FF0>)>'
        'get_plane': None, # (!) real value is "<method 'get_plane' of 'panda3d.core.BoundingPlane' objects>"
        'plane': None, # (!) real value is "<attribute 'plane' of 'panda3d.core.BoundingPlane' objects>"
    }


