# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .CollisionSolid import CollisionSolid

class CollisionPlane(CollisionSolid):
    """
    /**
     *
     */
    """
    def distToPlane(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        dist_to_plane(CollisionPlane self, const LPoint3f point)
        
        /**
         *
         */
        """
        pass

    def dist_to_plane(self, CollisionPlane_self, const_LPoint3f_point): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        dist_to_plane(CollisionPlane self, const LPoint3f point)
        
        /**
         *
         */
        """
        pass

    def flip(self, const_CollisionPlane_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        flip(const CollisionPlane self)
        
        /**
         * Convenience method to flip the plane in-place.
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getNormal(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_normal(CollisionPlane self)
        
        /**
         *
         */
        """
        pass

    def getPlane(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_plane(CollisionPlane self)
        
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

    def get_normal(self, CollisionPlane_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_normal(CollisionPlane self)
        
        /**
         *
         */
        """
        pass

    def get_plane(self, CollisionPlane_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_plane(CollisionPlane self)
        
        /**
         *
         */
        """
        pass

    def setPlane(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_plane(const CollisionPlane self, const LPlanef plane)
        
        /**
         *
         */
        """
        pass

    def set_plane(self, const_CollisionPlane_self, const_LPlanef_plane): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_plane(const CollisionPlane self, const LPlanef plane)
        
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

    normal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    plane = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.CollisionPlane' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.CollisionPlane' objects>"
        '__doc__': '/**\n *\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.CollisionPlane' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2CEA30>'
        'distToPlane': None, # (!) real value is "<method 'distToPlane' of 'panda3d.core.CollisionPlane' objects>"
        'dist_to_plane': None, # (!) real value is "<method 'dist_to_plane' of 'panda3d.core.CollisionPlane' objects>"
        'flip': None, # (!) real value is "<method 'flip' of 'panda3d.core.CollisionPlane' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2CEA30>)>'
        'getNormal': None, # (!) real value is "<method 'getNormal' of 'panda3d.core.CollisionPlane' objects>"
        'getPlane': None, # (!) real value is "<method 'getPlane' of 'panda3d.core.CollisionPlane' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2CEA30>)>'
        'get_normal': None, # (!) real value is "<method 'get_normal' of 'panda3d.core.CollisionPlane' objects>"
        'get_plane': None, # (!) real value is "<method 'get_plane' of 'panda3d.core.CollisionPlane' objects>"
        'normal': None, # (!) real value is "<attribute 'normal' of 'panda3d.core.CollisionPlane' objects>"
        'plane': None, # (!) real value is "<attribute 'plane' of 'panda3d.core.CollisionPlane' objects>"
        'setPlane': None, # (!) real value is "<method 'setPlane' of 'panda3d.core.CollisionPlane' objects>"
        'set_plane': None, # (!) real value is "<method 'set_plane' of 'panda3d.core.CollisionPlane' objects>"
    }


