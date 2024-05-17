# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .CollisionSolid import CollisionSolid

class CollisionRay(CollisionSolid):
    """
    /**
     * An infinite ray, with a specific origin and direction.  It begins at its
     * origin and continues in one direction to infinity, and it has no radius.
     * Useful for picking from a window, or for gravity effects.
     */
    """
    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getDirection(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_direction(CollisionRay self)
        
        /**
         *
         */
        """
        pass

    def getOrigin(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_origin(CollisionRay self)
        
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

    def get_direction(self, CollisionRay_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_direction(CollisionRay self)
        
        /**
         *
         */
        """
        pass

    def get_origin(self, CollisionRay_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_origin(CollisionRay self)
        
        /**
         *
         */
        """
        pass

    def setDirection(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_direction(const CollisionRay self, const LVector3f direction)
        set_direction(const CollisionRay self, float x, float y, float z)
        
        /**
         *
         */
        
        /**
         *
         */
        """
        pass

    def setFromLens(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_from_lens(const CollisionRay self, LensNode camera, const LPoint2f point)
        set_from_lens(const CollisionRay self, LensNode camera, float px, float py)
        
        /**
         * Accepts a LensNode and a 2-d point in the range [-1,1].  Sets the
         * CollisionRay so that it begins at the LensNode's near plane and extends to
         * infinity, making it suitable for picking objects from the screen given a
         * camera and a mouse location.
         */
        
        /**
         * Accepts a LensNode and a 2-d point in the range [-1,1].  Sets the
         * CollisionRay so that it begins at the LensNode's near plane and extends to
         * infinity, making it suitable for picking objects from the screen given a
         * camera and a mouse location.
         *
         * Returns true if the point was acceptable, false otherwise.
         */
        """
        pass

    def setOrigin(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_origin(const CollisionRay self, const LPoint3f origin)
        set_origin(const CollisionRay self, float x, float y, float z)
        
        /**
         *
         */
        
        /**
         *
         */
        """
        pass

    def set_direction(self, const_CollisionRay_self, const_LVector3f_direction): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_direction(const CollisionRay self, const LVector3f direction)
        set_direction(const CollisionRay self, float x, float y, float z)
        
        /**
         *
         */
        
        /**
         *
         */
        """
        pass

    def set_from_lens(self, const_CollisionRay_self, LensNode_camera, const_LPoint2f_point): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_from_lens(const CollisionRay self, LensNode camera, const LPoint2f point)
        set_from_lens(const CollisionRay self, LensNode camera, float px, float py)
        
        /**
         * Accepts a LensNode and a 2-d point in the range [-1,1].  Sets the
         * CollisionRay so that it begins at the LensNode's near plane and extends to
         * infinity, making it suitable for picking objects from the screen given a
         * camera and a mouse location.
         */
        
        /**
         * Accepts a LensNode and a 2-d point in the range [-1,1].  Sets the
         * CollisionRay so that it begins at the LensNode's near plane and extends to
         * infinity, making it suitable for picking objects from the screen given a
         * camera and a mouse location.
         *
         * Returns true if the point was acceptable, false otherwise.
         */
        """
        pass

    def set_origin(self, const_CollisionRay_self, const_LPoint3f_origin): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_origin(const CollisionRay self, const LPoint3f origin)
        set_origin(const CollisionRay self, float x, float y, float z)
        
        /**
         *
         */
        
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

    direction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    origin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * An infinite ray, with a specific origin and direction.  It begins at its\n * origin and continues in one direction to infinity, and it has no radius.\n * Useful for picking from a window, or for gravity effects.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.CollisionRay' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2D01C0>'
        'direction': None, # (!) real value is "<attribute 'direction' of 'panda3d.core.CollisionRay' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2D01C0>)>'
        'getDirection': None, # (!) real value is "<method 'getDirection' of 'panda3d.core.CollisionRay' objects>"
        'getOrigin': None, # (!) real value is "<method 'getOrigin' of 'panda3d.core.CollisionRay' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2D01C0>)>'
        'get_direction': None, # (!) real value is "<method 'get_direction' of 'panda3d.core.CollisionRay' objects>"
        'get_origin': None, # (!) real value is "<method 'get_origin' of 'panda3d.core.CollisionRay' objects>"
        'origin': None, # (!) real value is "<attribute 'origin' of 'panda3d.core.CollisionRay' objects>"
        'setDirection': None, # (!) real value is "<method 'setDirection' of 'panda3d.core.CollisionRay' objects>"
        'setFromLens': None, # (!) real value is "<method 'setFromLens' of 'panda3d.core.CollisionRay' objects>"
        'setOrigin': None, # (!) real value is "<method 'setOrigin' of 'panda3d.core.CollisionRay' objects>"
        'set_direction': None, # (!) real value is "<method 'set_direction' of 'panda3d.core.CollisionRay' objects>"
        'set_from_lens': None, # (!) real value is "<method 'set_from_lens' of 'panda3d.core.CollisionRay' objects>"
        'set_origin': None, # (!) real value is "<method 'set_origin' of 'panda3d.core.CollisionRay' objects>"
    }


