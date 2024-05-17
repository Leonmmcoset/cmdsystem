# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .Namable import Namable

class FreetypeFont(Namable):
    """
    /**
     * This is a common base class for both DynamicTextFont and PNMTextMaker.
     * Both of these are utility classes that use the FreeType library to generate
     * glyphs from fonts; this class abstracts out that common wrapper around
     * FreeType.
     */
    """
    def getFontPixelSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_font_pixel_size(FreetypeFont self)
        
        /**
         * This is used to report whether the requested pixel size is being only
         * approximated by a fixed-pixel-size font.  This returns 0 in the normal
         * case, in which a scalable font is used, or the fixed-pixel-size font has
         * exactly the requested pixel size.
         *
         * If this returns non-zero, it is the pixel size of the font that we are
         * using to approximate our desired size.
         */
        """
        pass

    def getLineHeight(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_line_height(FreetypeFont self)
        
        /**
         * Returns the number of units high each line of text is.
         */
        """
        pass

    def getNativeAntialias(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_native_antialias(FreetypeFont self)
        
        /**
         * Returns whether Freetype's built-in antialias mode is enabled.  See
         * set_native_antialias().
         */
        """
        pass

    def getPixelSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_pixel_size(FreetypeFont self)
        
        /**
         * Returns the size of the font in pixels, as it appears in the texture.
         */
        """
        pass

    def getPixelsPerUnit(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_pixels_per_unit(FreetypeFont self)
        
        /**
         * Returns the resolution of the texture map.  See set_pixels_per_unit().
         */
        """
        pass

    def getPointSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_point_size(FreetypeFont self)
        
        /**
         * Returns the point size of the font.
         */
        """
        pass

    def getPointsPerInch(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_points_per_inch()
        
        /**
         * Returns the number of points in one inch.  This is a universal typographic
         * convention.
         */
        """
        pass

    def getPointsPerUnit(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_points_per_unit()
        
        /**
         * Returns the point size of the font that is one Panda unit high.  This is an
         * arbitrary Panda convention for text, and is set to 10.0.
         */
        """
        pass

    def getScaleFactor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_scale_factor(FreetypeFont self)
        
        /**
         * Returns the antialiasing scale factor.  See set_scale_factor().
         */
        """
        pass

    def getSpaceAdvance(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_space_advance(FreetypeFont self)
        
        /**
         * Returns the number of units wide a space is.
         */
        """
        pass

    def getWindingOrder(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_winding_order(FreetypeFont self)
        
        /**
         * Returns the winding order set via set_winding_order().
         */
        """
        pass

    def get_font_pixel_size(self, FreetypeFont_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_font_pixel_size(FreetypeFont self)
        
        /**
         * This is used to report whether the requested pixel size is being only
         * approximated by a fixed-pixel-size font.  This returns 0 in the normal
         * case, in which a scalable font is used, or the fixed-pixel-size font has
         * exactly the requested pixel size.
         *
         * If this returns non-zero, it is the pixel size of the font that we are
         * using to approximate our desired size.
         */
        """
        pass

    def get_line_height(self, FreetypeFont_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_line_height(FreetypeFont self)
        
        /**
         * Returns the number of units high each line of text is.
         */
        """
        pass

    def get_native_antialias(self, FreetypeFont_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_native_antialias(FreetypeFont self)
        
        /**
         * Returns whether Freetype's built-in antialias mode is enabled.  See
         * set_native_antialias().
         */
        """
        pass

    def get_pixels_per_unit(self, FreetypeFont_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_pixels_per_unit(FreetypeFont self)
        
        /**
         * Returns the resolution of the texture map.  See set_pixels_per_unit().
         */
        """
        pass

    def get_pixel_size(self, FreetypeFont_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_pixel_size(FreetypeFont self)
        
        /**
         * Returns the size of the font in pixels, as it appears in the texture.
         */
        """
        pass

    def get_points_per_inch(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_points_per_inch()
        
        /**
         * Returns the number of points in one inch.  This is a universal typographic
         * convention.
         */
        """
        pass

    def get_points_per_unit(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_points_per_unit()
        
        /**
         * Returns the point size of the font that is one Panda unit high.  This is an
         * arbitrary Panda convention for text, and is set to 10.0.
         */
        """
        pass

    def get_point_size(self, FreetypeFont_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_point_size(FreetypeFont self)
        
        /**
         * Returns the point size of the font.
         */
        """
        pass

    def get_scale_factor(self, FreetypeFont_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_scale_factor(FreetypeFont self)
        
        /**
         * Returns the antialiasing scale factor.  See set_scale_factor().
         */
        """
        pass

    def get_space_advance(self, FreetypeFont_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_space_advance(FreetypeFont self)
        
        /**
         * Returns the number of units wide a space is.
         */
        """
        pass

    def get_winding_order(self, FreetypeFont_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_winding_order(FreetypeFont self)
        
        /**
         * Returns the winding order set via set_winding_order().
         */
        """
        pass

    def setNativeAntialias(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_native_antialias(const FreetypeFont self, bool native_antialias)
        
        /**
         * Sets whether the Freetype library's built-in antialias mode is enabled.
         * There are two unrelated ways to achieve antialiasing: with Freetype's
         * native antialias mode, and with the use of a scale_factor greater than one.
         * By default, both modes are enabled.
         *
         * At low resolutions, some fonts may do better with one mode or the other.
         * In general, Freetype's native antialiasing will produce less blurry
         * results, but may introduce more artifacts.
         */
        """
        pass

    def setPixelSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_pixel_size(const FreetypeFont self, float pixel_size)
        
        /**
         * Computes the appropriate pixels_per_unit value to set the size of the font
         * in the texture to the indicated number of pixels.  This is just another way
         * to specify pixels_per_unit().
         */
        """
        pass

    def setPixelsPerUnit(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_pixels_per_unit(const FreetypeFont self, float pixels_per_unit)
        
        /**
         * Set the resolution of the texture map, and hence the clarity of the
         * resulting font.  This sets the number of pixels in the texture map that are
         * used for each onscreen unit.
         *
         * Setting this number larger results in an easier to read font, but at the
         * cost of more texture memory.
         *
         * This should only be called before any characters have been requested out of
         * the font, or immediately after calling clear().
         */
        """
        pass

    def setPointSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_point_size(const FreetypeFont self, float point_size)
        
        /**
         * Sets the point size of the font.  This controls the apparent size of the
         * font onscreen.  By convention, a 10 point font is about 1 screen unit high.
         *
         * This should only be called before any characters have been requested out of
         * the font, or immediately after calling clear().
         */
        """
        pass

    def setScaleFactor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_scale_factor(const FreetypeFont self, float scale_factor)
        
        /**
         * Sets the factor by which the font is rendered larger by the FreeType
         * library before being filtered down to its actual size in the texture as
         * specified by set_pixels_per_unit().  This may be set to a number larger
         * than 1.0 to improve the font's antialiasing (since FreeType doesn't really
         * do a swell job of antialiasing by itself).  There is some performance
         * implication for setting this different than 1.0.
         *
         * This should only be called before any characters have been requested out of
         * the font, or immediately after calling clear().
         */
        """
        pass

    def setWindingOrder(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_winding_order(const FreetypeFont self, int winding_order)
        
        /**
         * Specifies an explicitly winding order on this particular font.  This is
         * only necessary if the render_mode is RM_polygon or RM_solid, and only if
         * FreeType appears to guess wrong on this font.  Normally, you should leave
         * this at WO_default.
         */
        """
        pass

    def set_native_antialias(self, const_FreetypeFont_self, bool_native_antialias): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_native_antialias(const FreetypeFont self, bool native_antialias)
        
        /**
         * Sets whether the Freetype library's built-in antialias mode is enabled.
         * There are two unrelated ways to achieve antialiasing: with Freetype's
         * native antialias mode, and with the use of a scale_factor greater than one.
         * By default, both modes are enabled.
         *
         * At low resolutions, some fonts may do better with one mode or the other.
         * In general, Freetype's native antialiasing will produce less blurry
         * results, but may introduce more artifacts.
         */
        """
        pass

    def set_pixels_per_unit(self, const_FreetypeFont_self, float_pixels_per_unit): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_pixels_per_unit(const FreetypeFont self, float pixels_per_unit)
        
        /**
         * Set the resolution of the texture map, and hence the clarity of the
         * resulting font.  This sets the number of pixels in the texture map that are
         * used for each onscreen unit.
         *
         * Setting this number larger results in an easier to read font, but at the
         * cost of more texture memory.
         *
         * This should only be called before any characters have been requested out of
         * the font, or immediately after calling clear().
         */
        """
        pass

    def set_pixel_size(self, const_FreetypeFont_self, float_pixel_size): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_pixel_size(const FreetypeFont self, float pixel_size)
        
        /**
         * Computes the appropriate pixels_per_unit value to set the size of the font
         * in the texture to the indicated number of pixels.  This is just another way
         * to specify pixels_per_unit().
         */
        """
        pass

    def set_point_size(self, const_FreetypeFont_self, float_point_size): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_point_size(const FreetypeFont self, float point_size)
        
        /**
         * Sets the point size of the font.  This controls the apparent size of the
         * font onscreen.  By convention, a 10 point font is about 1 screen unit high.
         *
         * This should only be called before any characters have been requested out of
         * the font, or immediately after calling clear().
         */
        """
        pass

    def set_scale_factor(self, const_FreetypeFont_self, float_scale_factor): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_scale_factor(const FreetypeFont self, float scale_factor)
        
        /**
         * Sets the factor by which the font is rendered larger by the FreeType
         * library before being filtered down to its actual size in the texture as
         * specified by set_pixels_per_unit().  This may be set to a number larger
         * than 1.0 to improve the font's antialiasing (since FreeType doesn't really
         * do a swell job of antialiasing by itself).  There is some performance
         * implication for setting this different than 1.0.
         *
         * This should only be called before any characters have been requested out of
         * the font, or immediately after calling clear().
         */
        """
        pass

    def set_winding_order(self, const_FreetypeFont_self, int_winding_order): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_winding_order(const FreetypeFont self, int winding_order)
        
        /**
         * Specifies an explicitly winding order on this particular font.  This is
         * only necessary if the render_mode is RM_polygon or RM_solid, and only if
         * FreeType appears to guess wrong on this font.  Normally, you should leave
         * this at WO_default.
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    winding_order = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        'WODefault': 0,
        'WOInvalid': 3,
        'WOLeft': 1,
        'WORight': 2,
        'WO_default': 0,
        'WO_invalid': 3,
        'WO_left': 1,
        'WO_right': 2,
        '__doc__': '/**\n * This is a common base class for both DynamicTextFont and PNMTextMaker.\n * Both of these are utility classes that use the FreeType library to generate\n * glyphs from fonts; this class abstracts out that common wrapper around\n * FreeType.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.FreetypeFont' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE393A10>'
        'getFontPixelSize': None, # (!) real value is "<method 'getFontPixelSize' of 'panda3d.core.FreetypeFont' objects>"
        'getLineHeight': None, # (!) real value is "<method 'getLineHeight' of 'panda3d.core.FreetypeFont' objects>"
        'getNativeAntialias': None, # (!) real value is "<method 'getNativeAntialias' of 'panda3d.core.FreetypeFont' objects>"
        'getPixelSize': None, # (!) real value is "<method 'getPixelSize' of 'panda3d.core.FreetypeFont' objects>"
        'getPixelsPerUnit': None, # (!) real value is "<method 'getPixelsPerUnit' of 'panda3d.core.FreetypeFont' objects>"
        'getPointSize': None, # (!) real value is "<method 'getPointSize' of 'panda3d.core.FreetypeFont' objects>"
        'getPointsPerInch': None, # (!) real value is '<staticmethod(<built-in method getPointsPerInch of type object at 0x00007FFCFE393A10>)>'
        'getPointsPerUnit': None, # (!) real value is '<staticmethod(<built-in method getPointsPerUnit of type object at 0x00007FFCFE393A10>)>'
        'getScaleFactor': None, # (!) real value is "<method 'getScaleFactor' of 'panda3d.core.FreetypeFont' objects>"
        'getSpaceAdvance': None, # (!) real value is "<method 'getSpaceAdvance' of 'panda3d.core.FreetypeFont' objects>"
        'getWindingOrder': None, # (!) real value is "<method 'getWindingOrder' of 'panda3d.core.FreetypeFont' objects>"
        'get_font_pixel_size': None, # (!) real value is "<method 'get_font_pixel_size' of 'panda3d.core.FreetypeFont' objects>"
        'get_line_height': None, # (!) real value is "<method 'get_line_height' of 'panda3d.core.FreetypeFont' objects>"
        'get_native_antialias': None, # (!) real value is "<method 'get_native_antialias' of 'panda3d.core.FreetypeFont' objects>"
        'get_pixel_size': None, # (!) real value is "<method 'get_pixel_size' of 'panda3d.core.FreetypeFont' objects>"
        'get_pixels_per_unit': None, # (!) real value is "<method 'get_pixels_per_unit' of 'panda3d.core.FreetypeFont' objects>"
        'get_point_size': None, # (!) real value is "<method 'get_point_size' of 'panda3d.core.FreetypeFont' objects>"
        'get_points_per_inch': None, # (!) real value is '<staticmethod(<built-in method get_points_per_inch of type object at 0x00007FFCFE393A10>)>'
        'get_points_per_unit': None, # (!) real value is '<staticmethod(<built-in method get_points_per_unit of type object at 0x00007FFCFE393A10>)>'
        'get_scale_factor': None, # (!) real value is "<method 'get_scale_factor' of 'panda3d.core.FreetypeFont' objects>"
        'get_space_advance': None, # (!) real value is "<method 'get_space_advance' of 'panda3d.core.FreetypeFont' objects>"
        'get_winding_order': None, # (!) real value is "<method 'get_winding_order' of 'panda3d.core.FreetypeFont' objects>"
        'setNativeAntialias': None, # (!) real value is "<method 'setNativeAntialias' of 'panda3d.core.FreetypeFont' objects>"
        'setPixelSize': None, # (!) real value is "<method 'setPixelSize' of 'panda3d.core.FreetypeFont' objects>"
        'setPixelsPerUnit': None, # (!) real value is "<method 'setPixelsPerUnit' of 'panda3d.core.FreetypeFont' objects>"
        'setPointSize': None, # (!) real value is "<method 'setPointSize' of 'panda3d.core.FreetypeFont' objects>"
        'setScaleFactor': None, # (!) real value is "<method 'setScaleFactor' of 'panda3d.core.FreetypeFont' objects>"
        'setWindingOrder': None, # (!) real value is "<method 'setWindingOrder' of 'panda3d.core.FreetypeFont' objects>"
        'set_native_antialias': None, # (!) real value is "<method 'set_native_antialias' of 'panda3d.core.FreetypeFont' objects>"
        'set_pixel_size': None, # (!) real value is "<method 'set_pixel_size' of 'panda3d.core.FreetypeFont' objects>"
        'set_pixels_per_unit': None, # (!) real value is "<method 'set_pixels_per_unit' of 'panda3d.core.FreetypeFont' objects>"
        'set_point_size': None, # (!) real value is "<method 'set_point_size' of 'panda3d.core.FreetypeFont' objects>"
        'set_scale_factor': None, # (!) real value is "<method 'set_scale_factor' of 'panda3d.core.FreetypeFont' objects>"
        'set_winding_order': None, # (!) real value is "<method 'set_winding_order' of 'panda3d.core.FreetypeFont' objects>"
        'winding_order': None, # (!) real value is "<attribute 'winding_order' of 'panda3d.core.FreetypeFont' objects>"
    }
    WODefault = 0
    WOInvalid = 3
    WOLeft = 1
    WORight = 2
    WO_default = 0
    WO_invalid = 3
    WO_left = 1
    WO_right = 2


