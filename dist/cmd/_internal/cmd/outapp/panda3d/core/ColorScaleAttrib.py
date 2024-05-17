# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .RenderAttrib import RenderAttrib

class ColorScaleAttrib(RenderAttrib):
    """
    /**
     * Applies a scale to colors in the scene graph and on vertices.
     */
    """
    def getClassSlot(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_slot()
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getScale(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_scale(ColorScaleAttrib self)
        
        /**
         * Returns the scale to be applied to colors.
         */
        """
        pass

    def get_class_slot(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_slot()
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_scale(self, ColorScaleAttrib_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_scale(ColorScaleAttrib self)
        
        /**
         * Returns the scale to be applied to colors.
         */
        """
        pass

    def hasAlphaScale(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_alpha_scale(ColorScaleAttrib self)
        
        /**
         * Returns true if the ColorScaleAttrib has a non-identity scale in the alpha
         * component (ignoring RGB), or false otherwise.
         */
        """
        pass

    def hasRgbScale(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_rgb_scale(ColorScaleAttrib self)
        
        /**
         * Returns true if the ColorScaleAttrib has a non-identity scale in the RGB
         * components (ignoring alpha), or false otherwise.
         */
        """
        pass

    def hasScale(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_scale(ColorScaleAttrib self)
        
        /**
         * Returns true if the ColorScaleAttrib has a non-identity scale, false
         * otherwise (in which case it might be an off attrib or an identity attrib).
         */
        """
        pass

    def has_alpha_scale(self, ColorScaleAttrib_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_alpha_scale(ColorScaleAttrib self)
        
        /**
         * Returns true if the ColorScaleAttrib has a non-identity scale in the alpha
         * component (ignoring RGB), or false otherwise.
         */
        """
        pass

    def has_rgb_scale(self, ColorScaleAttrib_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_rgb_scale(ColorScaleAttrib self)
        
        /**
         * Returns true if the ColorScaleAttrib has a non-identity scale in the RGB
         * components (ignoring alpha), or false otherwise.
         */
        """
        pass

    def has_scale(self, ColorScaleAttrib_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_scale(ColorScaleAttrib self)
        
        /**
         * Returns true if the ColorScaleAttrib has a non-identity scale, false
         * otherwise (in which case it might be an off attrib or an identity attrib).
         */
        """
        pass

    def isIdentity(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_identity(ColorScaleAttrib self)
        
        /**
         * Returns true if the ColorScaleAttrib is an identity attrib, false if it is
         * either an off attrib or it has a scale.
         */
        """
        pass

    def isOff(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_off(ColorScaleAttrib self)
        
        /**
         * Returns true if the ColorScaleAttrib will ignore any color scales inherited
         * from above, false otherwise.  This is not the same thing as !has_scale(); a
         * ColorScaleAttrib may have the "off" flag set and also have another scale
         * specified.
         */
        """
        pass

    def is_identity(self, ColorScaleAttrib_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_identity(ColorScaleAttrib self)
        
        /**
         * Returns true if the ColorScaleAttrib is an identity attrib, false if it is
         * either an off attrib or it has a scale.
         */
        """
        pass

    def is_off(self, ColorScaleAttrib_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_off(ColorScaleAttrib self)
        
        /**
         * Returns true if the ColorScaleAttrib will ignore any color scales inherited
         * from above, false otherwise.  This is not the same thing as !has_scale(); a
         * ColorScaleAttrib may have the "off" flag set and also have another scale
         * specified.
         */
        """
        pass

    def make(self, const_LVecBase4f_scale): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make(const LVecBase4f scale)
        
        /**
         * Constructs a new ColorScaleAttrib object that indicates geometry should be
         * scaled by the indicated factor.
         */
        """
        pass

    def makeDefault(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_default()
        
        /**
         * Returns a RenderAttrib that corresponds to whatever the standard default
         * properties for render attributes of this type ought to be.
         */
        """
        pass

    def makeIdentity(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_identity()
        
        /**
         * Constructs an identity scale attrib.
         */
        """
        pass

    def makeOff(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_off()
        
        /**
         * Constructs a new ColorScaleAttrib object that ignores any ColorScaleAttrib
         * inherited from above.  You may also specify an additional color scale to
         * apply to geometry below (using set_scale()).
         */
        """
        pass

    def make_default(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_default()
        
        /**
         * Returns a RenderAttrib that corresponds to whatever the standard default
         * properties for render attributes of this type ought to be.
         */
        """
        pass

    def make_identity(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_identity()
        
        /**
         * Constructs an identity scale attrib.
         */
        """
        pass

    def make_off(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_off()
        
        /**
         * Constructs a new ColorScaleAttrib object that ignores any ColorScaleAttrib
         * inherited from above.  You may also specify an additional color scale to
         * apply to geometry below (using set_scale()).
         */
        """
        pass

    def setScale(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_scale(ColorScaleAttrib self, const LVecBase4f scale)
        
        /**
         * Returns a new ColorScaleAttrib, just like this one, but with the scale
         * changed to the indicated value.
         */
        """
        pass

    def set_scale(self, ColorScaleAttrib_self, const_LVecBase4f_scale): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_scale(ColorScaleAttrib self, const LVecBase4f scale)
        
        /**
         * Returns a new ColorScaleAttrib, just like this one, but with the scale
         * changed to the indicated value.
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    scale = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    class_slot = 8
    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * Applies a scale to colors in the scene graph and on vertices.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.ColorScaleAttrib' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2955A0>'
        'class_slot': None, # (!) real value is "<attribute 'class_slot' of 'panda3d.core.ColorScaleAttrib'>"
        'getClassSlot': None, # (!) real value is '<staticmethod(<built-in method getClassSlot of type object at 0x00007FFCFE2955A0>)>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2955A0>)>'
        'getScale': None, # (!) real value is "<method 'getScale' of 'panda3d.core.ColorScaleAttrib' objects>"
        'get_class_slot': None, # (!) real value is '<staticmethod(<built-in method get_class_slot of type object at 0x00007FFCFE2955A0>)>'
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2955A0>)>'
        'get_scale': None, # (!) real value is "<method 'get_scale' of 'panda3d.core.ColorScaleAttrib' objects>"
        'hasAlphaScale': None, # (!) real value is "<method 'hasAlphaScale' of 'panda3d.core.ColorScaleAttrib' objects>"
        'hasRgbScale': None, # (!) real value is "<method 'hasRgbScale' of 'panda3d.core.ColorScaleAttrib' objects>"
        'hasScale': None, # (!) real value is "<method 'hasScale' of 'panda3d.core.ColorScaleAttrib' objects>"
        'has_alpha_scale': None, # (!) real value is "<method 'has_alpha_scale' of 'panda3d.core.ColorScaleAttrib' objects>"
        'has_rgb_scale': None, # (!) real value is "<method 'has_rgb_scale' of 'panda3d.core.ColorScaleAttrib' objects>"
        'has_scale': None, # (!) real value is "<method 'has_scale' of 'panda3d.core.ColorScaleAttrib' objects>"
        'isIdentity': None, # (!) real value is "<method 'isIdentity' of 'panda3d.core.ColorScaleAttrib' objects>"
        'isOff': None, # (!) real value is "<method 'isOff' of 'panda3d.core.ColorScaleAttrib' objects>"
        'is_identity': None, # (!) real value is "<method 'is_identity' of 'panda3d.core.ColorScaleAttrib' objects>"
        'is_off': None, # (!) real value is "<method 'is_off' of 'panda3d.core.ColorScaleAttrib' objects>"
        'make': None, # (!) real value is '<staticmethod(<built-in method make of type object at 0x00007FFCFE2955A0>)>'
        'makeDefault': None, # (!) real value is '<staticmethod(<built-in method makeDefault of type object at 0x00007FFCFE2955A0>)>'
        'makeIdentity': None, # (!) real value is '<staticmethod(<built-in method makeIdentity of type object at 0x00007FFCFE2955A0>)>'
        'makeOff': None, # (!) real value is '<staticmethod(<built-in method makeOff of type object at 0x00007FFCFE2955A0>)>'
        'make_default': None, # (!) real value is '<staticmethod(<built-in method make_default of type object at 0x00007FFCFE2955A0>)>'
        'make_identity': None, # (!) real value is '<staticmethod(<built-in method make_identity of type object at 0x00007FFCFE2955A0>)>'
        'make_off': None, # (!) real value is '<staticmethod(<built-in method make_off of type object at 0x00007FFCFE2955A0>)>'
        'scale': None, # (!) real value is "<attribute 'scale' of 'panda3d.core.ColorScaleAttrib' objects>"
        'setScale': None, # (!) real value is "<method 'setScale' of 'panda3d.core.ColorScaleAttrib' objects>"
        'set_scale': None, # (!) real value is "<method 'set_scale' of 'panda3d.core.ColorScaleAttrib' objects>"
    }


