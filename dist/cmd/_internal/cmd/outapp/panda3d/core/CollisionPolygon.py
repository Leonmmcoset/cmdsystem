# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .CollisionPlane import CollisionPlane

class CollisionPolygon(CollisionPlane):
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

    def getNumPoints(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_points(CollisionPolygon self)
        
        /**
         * Returns the number of vertices of the CollisionPolygon.
         */
        """
        pass

    def getPoint(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_point(CollisionPolygon self, int n)
        
        /**
         * Returns the nth vertex of the CollisionPolygon, expressed in 3-D space.
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

    def get_num_points(self, CollisionPolygon_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_points(CollisionPolygon self)
        
        /**
         * Returns the number of vertices of the CollisionPolygon.
         */
        """
        pass

    def get_point(self, CollisionPolygon_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_point(CollisionPolygon self, int n)
        
        /**
         * Returns the nth vertex of the CollisionPolygon, expressed in 3-D space.
         */
        """
        pass

    def get_points(self, *args, **kwargs): # real signature unknown
        pass

    def isConcave(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_concave(CollisionPolygon self)
        
        /**
         * Returns true if the CollisionPolygon appears to be concave, or false if it
         * is safely convex.
         */
        """
        pass

    def isValid(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_valid(CollisionPolygon self)
        
        /**
         * Returns true if the CollisionPolygon is valid (that is, it has at least
         * three vertices), or false otherwise.
         */
        """
        pass

    def is_concave(self, CollisionPolygon_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_concave(CollisionPolygon self)
        
        /**
         * Returns true if the CollisionPolygon appears to be concave, or false if it
         * is safely convex.
         */
        """
        pass

    def is_valid(self, CollisionPolygon_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_valid(CollisionPolygon self)
        
        /**
         * Returns true if the CollisionPolygon is valid (that is, it has at least
         * three vertices), or false otherwise.
         */
        """
        pass

    def verifyPoints(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        verify_points(const LPoint3f a, const LPoint3f b, const LPoint3f c)
        verify_points(const LPoint3f a, const LPoint3f b, const LPoint3f c, const LPoint3f d)
        
        /**
         * Verifies that the indicated set of points will define a valid
         * CollisionPolygon: that is, at least three non-collinear points, with no
         * points repeated.
         */
        
        /**
         * Verifies that the indicated set of points will define a valid
         * CollisionPolygon: that is, at least three non-collinear points, with no
         * points repeated.
         */
        
        /**
         * Verifies that the indicated set of points will define a valid
         * CollisionPolygon: that is, at least three non-collinear points, with no
         * points repeated.
         *
         * This does not check that the polygon defined is convex; that check is made
         * later, once we have projected the points to 2-d space where the decision is
         * easier.
         */
        """
        pass

    def verify_points(self, const_LPoint3f_a, const_LPoint3f_b, const_LPoint3f_c): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        verify_points(const LPoint3f a, const LPoint3f b, const LPoint3f c)
        verify_points(const LPoint3f a, const LPoint3f b, const LPoint3f c, const LPoint3f d)
        
        /**
         * Verifies that the indicated set of points will define a valid
         * CollisionPolygon: that is, at least three non-collinear points, with no
         * points repeated.
         */
        
        /**
         * Verifies that the indicated set of points will define a valid
         * CollisionPolygon: that is, at least three non-collinear points, with no
         * points repeated.
         */
        
        /**
         * Verifies that the indicated set of points will define a valid
         * CollisionPolygon: that is, at least three non-collinear points, with no
         * points repeated.
         *
         * This does not check that the polygon defined is convex; that check is made
         * later, once we have projected the points to 2-d space where the decision is
         * easier.
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    concave = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    points = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    valid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n *\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.CollisionPolygon' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2CEDD0>'
        'concave': None, # (!) real value is "<attribute 'concave' of 'panda3d.core.CollisionPolygon' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2CEDD0>)>'
        'getNumPoints': None, # (!) real value is "<method 'getNumPoints' of 'panda3d.core.CollisionPolygon' objects>"
        'getPoint': None, # (!) real value is "<method 'getPoint' of 'panda3d.core.CollisionPolygon' objects>"
        'getPoints': None, # (!) real value is "<method 'getPoints' of 'panda3d.core.CollisionPolygon' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2CEDD0>)>'
        'get_num_points': None, # (!) real value is "<method 'get_num_points' of 'panda3d.core.CollisionPolygon' objects>"
        'get_point': None, # (!) real value is "<method 'get_point' of 'panda3d.core.CollisionPolygon' objects>"
        'get_points': None, # (!) real value is "<method 'get_points' of 'panda3d.core.CollisionPolygon' objects>"
        'isConcave': None, # (!) real value is "<method 'isConcave' of 'panda3d.core.CollisionPolygon' objects>"
        'isValid': None, # (!) real value is "<method 'isValid' of 'panda3d.core.CollisionPolygon' objects>"
        'is_concave': None, # (!) real value is "<method 'is_concave' of 'panda3d.core.CollisionPolygon' objects>"
        'is_valid': None, # (!) real value is "<method 'is_valid' of 'panda3d.core.CollisionPolygon' objects>"
        'points': None, # (!) real value is "<attribute 'points' of 'panda3d.core.CollisionPolygon' objects>"
        'valid': None, # (!) real value is "<attribute 'valid' of 'panda3d.core.CollisionPolygon' objects>"
        'verifyPoints': None, # (!) real value is '<staticmethod(<built-in method verifyPoints of type object at 0x00007FFCFE2CEDD0>)>'
        'verify_points': None, # (!) real value is '<staticmethod(<built-in method verify_points of type object at 0x00007FFCFE2CEDD0>)>'
    }


