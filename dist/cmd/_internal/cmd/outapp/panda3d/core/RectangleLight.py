# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .LightLensNode import LightLensNode

class RectangleLight(LightLensNode):
    """
    /**
     * This is a type of area light that is an axis aligned rectangle, pointing
     * along the Y axis in the positive direction.
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

    def getMaxDistance(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_max_distance(RectangleLight self)
        
        /**
         * Returns the maximum distance at which the light has any effect, as previously
         * specified by set_max_distance.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_max_distance(self, RectangleLight_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_max_distance(RectangleLight self)
        
        /**
         * Returns the maximum distance at which the light has any effect, as previously
         * specified by set_max_distance.
         */
        """
        pass

    def setMaxDistance(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_max_distance(const RectangleLight self, float max_distance)
        
        /**
         * Sets the radius of the light's sphere of influence.  Beyond this distance, the
         * light may be attenuated to zero, if this is supported by the shader.
         */
        """
        pass

    def set_max_distance(self, const_RectangleLight_self, float_max_distance): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_max_distance(const RectangleLight self, float max_distance)
        
        /**
         * Sets the radius of the light's sphere of influence.  Beyond this distance, the
         * light may be attenuated to zero, if this is supported by the shader.
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    max_distance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * This is a type of area light that is an axis aligned rectangle, pointing\n * along the Y axis in the positive direction.\n *\n * @since 1.10.0\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.RectangleLight' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE288010>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE288010>)>'
        'getMaxDistance': None, # (!) real value is "<method 'getMaxDistance' of 'panda3d.core.RectangleLight' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE288010>)>'
        'get_max_distance': None, # (!) real value is "<method 'get_max_distance' of 'panda3d.core.RectangleLight' objects>"
        'max_distance': None, # (!) real value is "<attribute 'max_distance' of 'panda3d.core.RectangleLight' objects>"
        'setMaxDistance': None, # (!) real value is "<method 'setMaxDistance' of 'panda3d.core.RectangleLight' objects>"
        'set_max_distance': None, # (!) real value is "<method 'set_max_distance' of 'panda3d.core.RectangleLight' objects>"
    }


