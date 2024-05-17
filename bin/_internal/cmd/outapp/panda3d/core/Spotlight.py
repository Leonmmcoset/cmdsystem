# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .LightLensNode import LightLensNode

class Spotlight(LightLensNode):
    """
    /**
     * A light originating from a single point in space, and shining in a
     * particular direction, with a cone-shaped falloff.
     *
     * The Spotlight frustum is defined using a Lens, so it can have any of the
     * properties that a camera lens can have.
     *
     * Note that the class is named Spotlight instead of SpotLight, because
     * "spotlight" is a single English word, instead of two words.
     */
    """
    def clearSpecularColor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_specular_color(const Spotlight self)
        
        /**
         * Clears a custom specular color setting, meaning that the specular color
         * will now come from the color.
         */
        """
        pass

    def clear_specular_color(self, const_Spotlight_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_specular_color(const Spotlight self)
        
        /**
         * Clears a custom specular color setting, meaning that the specular color
         * will now come from the color.
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getMaxDistance(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_max_distance(Spotlight self)
        
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

    def get_max_distance(self, Spotlight_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_max_distance(Spotlight self)
        
        /**
         * Returns the maximum distance at which the light has any effect, as previously
         * specified by set_max_distance.
         */
        """
        pass

    def makeSpot(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_spot(int pixel_width, float full_radius, LVecBase4f fg, LVecBase4f bg)
        
        /**
         * Returns a newly-generated Texture that renders a circular spot image as
         * might be cast from the spotlight.  This may be projected onto target
         * geometry (for instance, via NodePath::project_texture()) instead of
         * actually enabling the light itself, as a cheesy way to make a high-
         * resolution spot appear on the geometry.
         *
         * pixel_width specifies the height and width of the new texture in pixels,
         * full_radius is a value in the range 0..1 that indicates the relative size
         * of the fully bright center spot, and fg and bg are the colors of the
         * interior and exterior of the spot, respectively.
         */
        """
        pass

    def make_spot(self, int_pixel_width, float_full_radius, LVecBase4f_fg, LVecBase4f_bg): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_spot(int pixel_width, float full_radius, LVecBase4f fg, LVecBase4f bg)
        
        /**
         * Returns a newly-generated Texture that renders a circular spot image as
         * might be cast from the spotlight.  This may be projected onto target
         * geometry (for instance, via NodePath::project_texture()) instead of
         * actually enabling the light itself, as a cheesy way to make a high-
         * resolution spot appear on the geometry.
         *
         * pixel_width specifies the height and width of the new texture in pixels,
         * full_radius is a value in the range 0..1 that indicates the relative size
         * of the fully bright center spot, and fg and bg are the colors of the
         * interior and exterior of the spot, respectively.
         */
        """
        pass

    def setAttenuation(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_attenuation(const Spotlight self, const LVecBase3f attenuation)
        
        /**
         * Sets the terms of the attenuation equation for the light.  These are, in
         * order, the constant, linear, and quadratic terms based on the distance from
         * the point to the vertex.
         */
        """
        pass

    def setExponent(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_exponent(const Spotlight self, float exponent)
        
        /**
         * Sets the exponent that controls the amount of light falloff from the center
         * of the spotlight.  The light is attenuated by the cosine of the angle
         * between the direction of the light and the direction of the point being
         * lighted, raised to the power of this exponent.  Thus, higher exponents
         * result in a more focused light source, regardless of the field-of-view of
         * the lens.
         */
        """
        pass

    def setMaxDistance(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_max_distance(const Spotlight self, float max_distance)
        
        /**
         * Sets the radius of the light's sphere of influence.  Beyond this distance, the
         * light may be attenuated to zero, if this is supported by the shader.
         */
        """
        pass

    def setSpecularColor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_specular_color(const Spotlight self, const LVecBase4f color)
        
        /**
         * Sets the color of specular highlights generated by the light.
         */
        """
        pass

    def set_attenuation(self, const_Spotlight_self, const_LVecBase3f_attenuation): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_attenuation(const Spotlight self, const LVecBase3f attenuation)
        
        /**
         * Sets the terms of the attenuation equation for the light.  These are, in
         * order, the constant, linear, and quadratic terms based on the distance from
         * the point to the vertex.
         */
        """
        pass

    def set_exponent(self, const_Spotlight_self, float_exponent): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_exponent(const Spotlight self, float exponent)
        
        /**
         * Sets the exponent that controls the amount of light falloff from the center
         * of the spotlight.  The light is attenuated by the cosine of the angle
         * between the direction of the light and the direction of the point being
         * lighted, raised to the power of this exponent.  Thus, higher exponents
         * result in a more focused light source, regardless of the field-of-view of
         * the lens.
         */
        """
        pass

    def set_max_distance(self, const_Spotlight_self, float_max_distance): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_max_distance(const Spotlight self, float max_distance)
        
        /**
         * Sets the radius of the light's sphere of influence.  Beyond this distance, the
         * light may be attenuated to zero, if this is supported by the shader.
         */
        """
        pass

    def set_specular_color(self, const_Spotlight_self, const_LVecBase4f_color): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_specular_color(const Spotlight self, const LVecBase4f color)
        
        /**
         * Sets the color of specular highlights generated by the light.
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    attenuation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    exponent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    max_distance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    specular_color = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * A light originating from a single point in space, and shining in a\n * particular direction, with a cone-shaped falloff.\n *\n * The Spotlight frustum is defined using a Lens, so it can have any of the\n * properties that a camera lens can have.\n *\n * Note that the class is named Spotlight instead of SpotLight, because\n * "spotlight" is a single English word, instead of two words.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.Spotlight' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE288920>'
        'attenuation': None, # (!) real value is "<attribute 'attenuation' of 'panda3d.core.Spotlight' objects>"
        'clearSpecularColor': None, # (!) real value is "<method 'clearSpecularColor' of 'panda3d.core.Spotlight' objects>"
        'clear_specular_color': None, # (!) real value is "<method 'clear_specular_color' of 'panda3d.core.Spotlight' objects>"
        'exponent': None, # (!) real value is "<attribute 'exponent' of 'panda3d.core.Spotlight' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE288920>)>'
        'getMaxDistance': None, # (!) real value is "<method 'getMaxDistance' of 'panda3d.core.Spotlight' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE288920>)>'
        'get_max_distance': None, # (!) real value is "<method 'get_max_distance' of 'panda3d.core.Spotlight' objects>"
        'makeSpot': None, # (!) real value is '<staticmethod(<built-in method makeSpot of type object at 0x00007FFCFE288920>)>'
        'make_spot': None, # (!) real value is '<staticmethod(<built-in method make_spot of type object at 0x00007FFCFE288920>)>'
        'max_distance': None, # (!) real value is "<attribute 'max_distance' of 'panda3d.core.Spotlight' objects>"
        'setAttenuation': None, # (!) real value is "<method 'setAttenuation' of 'panda3d.core.Spotlight' objects>"
        'setExponent': None, # (!) real value is "<method 'setExponent' of 'panda3d.core.Spotlight' objects>"
        'setMaxDistance': None, # (!) real value is "<method 'setMaxDistance' of 'panda3d.core.Spotlight' objects>"
        'setSpecularColor': None, # (!) real value is "<method 'setSpecularColor' of 'panda3d.core.Spotlight' objects>"
        'set_attenuation': None, # (!) real value is "<method 'set_attenuation' of 'panda3d.core.Spotlight' objects>"
        'set_exponent': None, # (!) real value is "<method 'set_exponent' of 'panda3d.core.Spotlight' objects>"
        'set_max_distance': None, # (!) real value is "<method 'set_max_distance' of 'panda3d.core.Spotlight' objects>"
        'set_specular_color': None, # (!) real value is "<method 'set_specular_color' of 'panda3d.core.Spotlight' objects>"
        'specular_color': None, # (!) real value is "<attribute 'specular_color' of 'panda3d.core.Spotlight' objects>"
    }


