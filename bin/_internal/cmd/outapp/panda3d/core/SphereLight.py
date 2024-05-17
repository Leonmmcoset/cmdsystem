# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .PointLight import PointLight

class SphereLight(PointLight):
    """
    /**
     * A sphere light is like a point light, except that it represents a sphere
     * with a radius, rather than being an infinitely thin point in space.
     *
     * @since 1.10.0
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
        get_radius(SphereLight self)
        
        /**
         * Returns the radius of the sphere.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_radius(self, SphereLight_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_radius(SphereLight self)
        
        /**
         * Returns the radius of the sphere.
         */
        """
        pass

    def setRadius(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_radius(const SphereLight self, float radius)
        
        /**
         * Sets the radius of the sphere.
         */
        """
        pass

    def set_radius(self, const_SphereLight_self, float_radius): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_radius(const SphereLight self, float radius)
        
        /**
         * Sets the radius of the sphere.
         */
        """
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
        '__doc__': '/**\n * A sphere light is like a point light, except that it represents a sphere\n * with a radius, rather than being an infinitely thin point in space.\n *\n * @since 1.10.0\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.SphereLight' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE288750>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE288750>)>'
        'getRadius': None, # (!) real value is "<method 'getRadius' of 'panda3d.core.SphereLight' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE288750>)>'
        'get_radius': None, # (!) real value is "<method 'get_radius' of 'panda3d.core.SphereLight' objects>"
        'radius': None, # (!) real value is "<attribute 'radius' of 'panda3d.core.SphereLight' objects>"
        'setRadius': None, # (!) real value is "<method 'setRadius' of 'panda3d.core.SphereLight' objects>"
        'set_radius': None, # (!) real value is "<method 'set_radius' of 'panda3d.core.SphereLight' objects>"
    }


