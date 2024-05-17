# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .BoundingVolume import BoundingVolume

class GeometricBoundingVolume(BoundingVolume):
    """
    /**
     * This is another abstract class, for a general class of bounding volumes
     * that actually enclose points in 3-d space, such as BSP's and bounding
     * spheres.
     */
    """
    def contains(self, GeometricBoundingVolume_self, const_GeometricBoundingVolume_vol): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        contains(GeometricBoundingVolume self, const GeometricBoundingVolume vol)
        contains(GeometricBoundingVolume self, const LPoint3f a, const LPoint3f b)
        
        /**
         * Returns the appropriate set of IntersectionFlags to indicate the amount of
         * intersection with the indicated volume.
         */
        
        /**
         * Returns the appropriate set of IntersectionFlags to indicate the amount of
         * intersection with the indicated point.
         */
        
        /**
         * Returns the appropriate set of IntersectionFlags to indicate the amount of
         * intersection with the indicated line segment.
         */
        """
        pass

    def extendBy(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        extend_by(const GeometricBoundingVolume self, const GeometricBoundingVolume vol)
        
        /**
         * Increases the size of the volume to include the given volume.
         */
        
        /**
         * Increases the size of the volume to include the given point.
         */
        """
        pass

    def extend_by(self, const_GeometricBoundingVolume_self, const_GeometricBoundingVolume_vol): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        extend_by(const GeometricBoundingVolume self, const GeometricBoundingVolume vol)
        
        /**
         * Increases the size of the volume to include the given volume.
         */
        
        /**
         * Increases the size of the volume to include the given point.
         */
        """
        pass

    def getApproxCenter(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_approx_center(GeometricBoundingVolume self)
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_approx_center(self, GeometricBoundingVolume_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_approx_center(GeometricBoundingVolume self)
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def xform(self, const_GeometricBoundingVolume_self, const_LMatrix4f_mat): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        xform(const GeometricBoundingVolume self, const LMatrix4f mat)
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
        '__doc__': "/**\n * This is another abstract class, for a general class of bounding volumes\n * that actually enclose points in 3-d space, such as BSP's and bounding\n * spheres.\n */",
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.GeometricBoundingVolume' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE340C00>'
        'contains': None, # (!) real value is "<method 'contains' of 'panda3d.core.GeometricBoundingVolume' objects>"
        'extendBy': None, # (!) real value is "<method 'extendBy' of 'panda3d.core.GeometricBoundingVolume' objects>"
        'extend_by': None, # (!) real value is "<method 'extend_by' of 'panda3d.core.GeometricBoundingVolume' objects>"
        'getApproxCenter': None, # (!) real value is "<method 'getApproxCenter' of 'panda3d.core.GeometricBoundingVolume' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE340C00>)>'
        'get_approx_center': None, # (!) real value is "<method 'get_approx_center' of 'panda3d.core.GeometricBoundingVolume' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE340C00>)>'
        'xform': None, # (!) real value is "<method 'xform' of 'panda3d.core.GeometricBoundingVolume' objects>"
    }


