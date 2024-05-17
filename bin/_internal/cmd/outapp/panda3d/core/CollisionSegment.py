# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .CollisionSolid import CollisionSolid

class CollisionSegment(CollisionSolid):
    """
    /**
     * A finite line segment, with two specific endpoints but no thickness.  It's
     * similar to a CollisionRay, except it does not continue to infinity.
     *
     * It does have an ordering, from point A to point B. If more than a single
     * point of the segment is intersecting a solid, the reported intersection
     * point is generally the closest on the segment to point A.
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
        get_point_a(CollisionSegment self)
        
        /**
         *
         */
        """
        pass

    def getPointB(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_point_b(CollisionSegment self)
        
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

    def get_point_a(self, CollisionSegment_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_point_a(CollisionSegment self)
        
        /**
         *
         */
        """
        pass

    def get_point_b(self, CollisionSegment_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_point_b(CollisionSegment self)
        
        /**
         *
         */
        """
        pass

    def setFromLens(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_from_lens(const CollisionSegment self, LensNode camera, const LPoint2f point)
        set_from_lens(const CollisionSegment self, LensNode camera, float px, float py)
        
        /**
         * Accepts a LensNode and a 2-d point in the range [-1,1].  Sets the
         * CollisionSegment so that it begins at the LensNode's near plane and extends
         * to the far plane, making it suitable for picking objects from the screen
         * given a camera and a mouse location.
         */
        
        /**
         * Accepts a LensNode and a 2-d point in the range [-1,1].  Sets the
         * CollisionSegment so that it begins at the LensNode's near plane and extends
         * to the far plane, making it suitable for picking objects from the screen
         * given a camera and a mouse location.
         *
         * Returns true if the point was acceptable, false otherwise.
         */
        """
        pass

    def setPointA(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_point_a(const CollisionSegment self, const LPoint3f a)
        set_point_a(const CollisionSegment self, float x, float y, float z)
        
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
        set_point_b(const CollisionSegment self, const LPoint3f b)
        set_point_b(const CollisionSegment self, float x, float y, float z)
        
        /**
         *
         */
        
        /**
         *
         */
        """
        pass

    def set_from_lens(self, const_CollisionSegment_self, LensNode_camera, const_LPoint2f_point): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_from_lens(const CollisionSegment self, LensNode camera, const LPoint2f point)
        set_from_lens(const CollisionSegment self, LensNode camera, float px, float py)
        
        /**
         * Accepts a LensNode and a 2-d point in the range [-1,1].  Sets the
         * CollisionSegment so that it begins at the LensNode's near plane and extends
         * to the far plane, making it suitable for picking objects from the screen
         * given a camera and a mouse location.
         */
        
        /**
         * Accepts a LensNode and a 2-d point in the range [-1,1].  Sets the
         * CollisionSegment so that it begins at the LensNode's near plane and extends
         * to the far plane, making it suitable for picking objects from the screen
         * given a camera and a mouse location.
         *
         * Returns true if the point was acceptable, false otherwise.
         */
        """
        pass

    def set_point_a(self, const_CollisionSegment_self, const_LPoint3f_a): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_point_a(const CollisionSegment self, const LPoint3f a)
        set_point_a(const CollisionSegment self, float x, float y, float z)
        
        /**
         *
         */
        
        /**
         *
         */
        """
        pass

    def set_point_b(self, const_CollisionSegment_self, const_LPoint3f_b): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_point_b(const CollisionSegment self, const LPoint3f b)
        set_point_b(const CollisionSegment self, float x, float y, float z)
        
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

    point_a = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    point_b = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': "/**\n * A finite line segment, with two specific endpoints but no thickness.  It's\n * similar to a CollisionRay, except it does not continue to infinity.\n *\n * It does have an ordering, from point A to point B. If more than a single\n * point of the segment is intersecting a solid, the reported intersection\n * point is generally the closest on the segment to point A.\n */",
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.CollisionSegment' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2D0730>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2D0730>)>'
        'getPointA': None, # (!) real value is "<method 'getPointA' of 'panda3d.core.CollisionSegment' objects>"
        'getPointB': None, # (!) real value is "<method 'getPointB' of 'panda3d.core.CollisionSegment' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2D0730>)>'
        'get_point_a': None, # (!) real value is "<method 'get_point_a' of 'panda3d.core.CollisionSegment' objects>"
        'get_point_b': None, # (!) real value is "<method 'get_point_b' of 'panda3d.core.CollisionSegment' objects>"
        'point_a': None, # (!) real value is "<attribute 'point_a' of 'panda3d.core.CollisionSegment' objects>"
        'point_b': None, # (!) real value is "<attribute 'point_b' of 'panda3d.core.CollisionSegment' objects>"
        'setFromLens': None, # (!) real value is "<method 'setFromLens' of 'panda3d.core.CollisionSegment' objects>"
        'setPointA': None, # (!) real value is "<method 'setPointA' of 'panda3d.core.CollisionSegment' objects>"
        'setPointB': None, # (!) real value is "<method 'setPointB' of 'panda3d.core.CollisionSegment' objects>"
        'set_from_lens': None, # (!) real value is "<method 'set_from_lens' of 'panda3d.core.CollisionSegment' objects>"
        'set_point_a': None, # (!) real value is "<method 'set_point_a' of 'panda3d.core.CollisionSegment' objects>"
        'set_point_b': None, # (!) real value is "<method 'set_point_b' of 'panda3d.core.CollisionSegment' objects>"
    }


