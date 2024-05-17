# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .GeometricBoundingVolume import GeometricBoundingVolume

class BoundingLine(GeometricBoundingVolume):
    """
    /**
     * This funny bounding volume is an infinite line with no thickness and
     * extending to infinity in both directions.
     *
     * Note that it *always* extends in both directions, despite the fact that you
     * specify two points to the constructor.  These are not endpoints, they are
     * two arbitrary points on the line.
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
        get_point_a(BoundingLine self)
        
        /**
         * Returns the first point that defines the line.
         */
        """
        pass

    def getPointB(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_point_b(BoundingLine self)
        
        /**
         * Returns the second point that defines the line.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_point_a(self, BoundingLine_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_point_a(BoundingLine self)
        
        /**
         * Returns the first point that defines the line.
         */
        """
        pass

    def get_point_b(self, BoundingLine_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_point_b(BoundingLine self)
        
        /**
         * Returns the second point that defines the line.
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * This funny bounding volume is an infinite line with no thickness and\n * extending to infinity in both directions.\n *\n * Note that it *always* extends in both directions, despite the fact that you\n * specify two points to the constructor.  These are not endpoints, they are\n * two arbitrary points on the line.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.BoundingLine' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE341E20>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE341E20>)>'
        'getPointA': None, # (!) real value is "<method 'getPointA' of 'panda3d.core.BoundingLine' objects>"
        'getPointB': None, # (!) real value is "<method 'getPointB' of 'panda3d.core.BoundingLine' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE341E20>)>'
        'get_point_a': None, # (!) real value is "<method 'get_point_a' of 'panda3d.core.BoundingLine' objects>"
        'get_point_b': None, # (!) real value is "<method 'get_point_b' of 'panda3d.core.BoundingLine' objects>"
    }


