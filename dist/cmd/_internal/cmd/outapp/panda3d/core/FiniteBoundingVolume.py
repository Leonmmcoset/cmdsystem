# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .GeometricBoundingVolume import GeometricBoundingVolume

class FiniteBoundingVolume(GeometricBoundingVolume):
    """
    /**
     * A special kind of GeometricBoundingVolume that is known to be finite.  It
     * is possible to query this kind of volume for its minimum and maximum
     * extents.
     */
    """
    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getMax(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_max(FiniteBoundingVolume self)
        """
        pass

    def getMin(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_min(FiniteBoundingVolume self)
        """
        pass

    def getVolume(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_volume(FiniteBoundingVolume self)
        
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

    def get_max(self, FiniteBoundingVolume_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_max(FiniteBoundingVolume self)
        """
        pass

    def get_min(self, FiniteBoundingVolume_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_min(FiniteBoundingVolume self)
        """
        pass

    def get_volume(self, FiniteBoundingVolume_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_volume(FiniteBoundingVolume self)
        
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

    max = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    min = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    volume = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * A special kind of GeometricBoundingVolume that is known to be finite.  It\n * is possible to query this kind of volume for its minimum and maximum\n * extents.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.FiniteBoundingVolume' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE340DD0>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE340DD0>)>'
        'getMax': None, # (!) real value is "<method 'getMax' of 'panda3d.core.FiniteBoundingVolume' objects>"
        'getMin': None, # (!) real value is "<method 'getMin' of 'panda3d.core.FiniteBoundingVolume' objects>"
        'getVolume': None, # (!) real value is "<method 'getVolume' of 'panda3d.core.FiniteBoundingVolume' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE340DD0>)>'
        'get_max': None, # (!) real value is "<method 'get_max' of 'panda3d.core.FiniteBoundingVolume' objects>"
        'get_min': None, # (!) real value is "<method 'get_min' of 'panda3d.core.FiniteBoundingVolume' objects>"
        'get_volume': None, # (!) real value is "<method 'get_volume' of 'panda3d.core.FiniteBoundingVolume' objects>"
        'max': None, # (!) real value is "<attribute 'max' of 'panda3d.core.FiniteBoundingVolume' objects>"
        'min': None, # (!) real value is "<attribute 'min' of 'panda3d.core.FiniteBoundingVolume' objects>"
        'volume': None, # (!) real value is "<attribute 'volume' of 'panda3d.core.FiniteBoundingVolume' objects>"
    }


