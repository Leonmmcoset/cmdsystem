# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .TextFont import TextFont

from .FreetypeFont import FreetypeFont

class DynamicTextFont(TextFont, FreetypeFont):
    """
    /**
     * A DynamicTextFont is a special TextFont object that rasterizes its glyphs
     * from a standard font file (e.g.  a TTF file) on the fly.  It requires the
     * FreeType 2.0 library (or any higher, backward-compatible version).
     */
    """
    def clear(self, const_DynamicTextFont_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear(const DynamicTextFont self)
        
        /**
         * Drops all the glyphs out of the cache and frees any association with any
         * previously-generated pages.
         *
         * Calling this frequently can result in wasted texture memory, as any
         * previously rendered text will still keep a pointer to the old, previously-
         * generated pages.  As long as the previously rendered text remains around,
         * the old pages will also remain around.
         */
        """
        pass

    def garbageCollect(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        garbage_collect(const DynamicTextFont self)
        
        /**
         * Removes all of the glyphs from the font that are no longer being used by
         * any Geoms.  Returns the number of glyphs removed.
         */
        """
        pass

    def garbage_collect(self, const_DynamicTextFont_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        garbage_collect(const DynamicTextFont self)
        
        /**
         * Removes all of the glyphs from the font that are no longer being used by
         * any Geoms.  Returns the number of glyphs removed.
         */
        """
        pass

    def getAnisotropicDegree(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_anisotropic_degree(DynamicTextFont self)
        
        /**
         * Returns the current anisotropic degree for textures created for this font.
         * See set_anisotropic_degree().
         */
        """
        pass

    def getBg(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_bg(DynamicTextFont self)
        
        /**
         * Returns the color of the background pixels of the font as they are rendered
         * into the font texture.  See set_bg().
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getFg(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_fg(DynamicTextFont self)
        
        /**
         * Returns the color of the foreground pixels of the font as they are rendered
         * into the font texture.  See set_fg().
         */
        """
        pass

    def getFontPixelSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_font_pixel_size(DynamicTextFont self)
        
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
        get_line_height(DynamicTextFont self)
        
        /**
         * Returns the number of units high each line of text is.
         */
        """
        pass

    def getMagfilter(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_magfilter(DynamicTextFont self)
        
        /**
         * Returns the filter type used when enlarging the textures created for this
         * font.
         */
        """
        pass

    def getMinfilter(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_minfilter(DynamicTextFont self)
        
        /**
         * Returns the filter type used when minimizing the textures created for this
         * font.
         */
        """
        pass

    def getName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_name(DynamicTextFont self)
        
        /**
         * Disambiguates the get_name() method between that inherited from TextFont
         * and that inherited from FreetypeFont.
         */
        """
        pass

    def getNativeAntialias(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_native_antialias(DynamicTextFont self)
        
        /**
         * Returns whether Freetype's built-in antialias mode is enabled.  See
         * set_native_antialias().
         */
        """
        pass

    def getNumPages(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_pages(DynamicTextFont self)
        
        /**
         * Returns the number of pages associated with the font.  Initially, the font
         * has zero pages; when the first piece of text is rendered with the font, it
         * will add additional pages as needed.  Each page is a Texture object that
         * contains the images for each of the glyphs currently in use somewhere.
         */
        """
        pass

    def getOutlineColor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_outline_color(DynamicTextFont self)
        
        /**
         * Returns the color of the outline pixels of the font as they are rendered
         * into the font texture.  See set_outline().
         */
        """
        pass

    def getOutlineFeather(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_outline_feather(DynamicTextFont self)
        
        /**
         * Returns the softness of the outline pixels of the font, as a value in the
         * range 0.0 to 1.0. See set_outline().
         */
        """
        pass

    def getOutlineWidth(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_outline_width(DynamicTextFont self)
        
        /**
         * Returns the width of the outline pixels of the font, as the number of
         * points beyond each letter.  See set_outline().
         */
        """
        pass

    def getPage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_page(DynamicTextFont self, int n)
        
        /**
         * Returns the nth page associated with the font.  Initially, the font has
         * zero pages; when the first piece of text is rendered with the font, it will
         * add additional pages as needed.  Each page is a Texture object that
         * contains the images for each of the glyphs currently in use somewhere.
         */
        """
        pass

    def getPages(self, *args, **kwargs): # real signature unknown
        pass

    def getPageSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_page_size(DynamicTextFont self)
        
        /**
         * Returns the size of the textures that are created for the DynamicTextFont.
         * See set_page_size().
         */
        """
        pass

    def getPageXSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_page_x_size(DynamicTextFont self)
        
        /**
         * Returns the x size of the textures that are created for the
         * DynamicTextFont.  See set_page_size().
         */
        """
        pass

    def getPageYSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_page_y_size(DynamicTextFont self)
        
        /**
         * Returns the y size of the textures that are created for the
         * DynamicTextFont.  See set_page_size().
         */
        """
        pass

    def getPixelsPerUnit(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_pixels_per_unit(DynamicTextFont self)
        
        /**
         * Returns the resolution of the texture map.  See set_pixels_per_unit().
         */
        """
        pass

    def getPointSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_point_size(DynamicTextFont self)
        
        /**
         * Returns the point size of the font.
         */
        """
        pass

    def getPolyMargin(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_poly_margin(DynamicTextFont self)
        
        /**
         * Returns the number of pixels of padding that is included around each glyph
         * in the generated polygons.  See set_poly_margin().
         */
        """
        pass

    def getRenderMode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_render_mode(DynamicTextFont self)
        
        /**
         * Returns the way the glyphs on this particular font are generated.  See
         * set_render_mode().
         */
        """
        pass

    def getScaleFactor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_scale_factor(DynamicTextFont self)
        
        /**
         * Returns the antialiasing scale factor.  See set_scale_factor().
         */
        """
        pass

    def getSpaceAdvance(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_space_advance(DynamicTextFont self)
        
        /**
         * Returns the number of units wide a space is.
         */
        """
        pass

    def getTexFormat(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_tex_format(DynamicTextFont self)
        
        /**
         * Returns the texture format used to render the individual pages.  This is
         * set automatically according to the colors selected.
         */
        """
        pass

    def getTextureMargin(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_texture_margin(DynamicTextFont self)
        
        /**
         * Returns the number of pixels of padding that is added around the border of
         * each glyph in the texture map.  See set_texture_margin().
         */
        """
        pass

    def get_anisotropic_degree(self, DynamicTextFont_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_anisotropic_degree(DynamicTextFont self)
        
        /**
         * Returns the current anisotropic degree for textures created for this font.
         * See set_anisotropic_degree().
         */
        """
        pass

    def get_bg(self, DynamicTextFont_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_bg(DynamicTextFont self)
        
        /**
         * Returns the color of the background pixels of the font as they are rendered
         * into the font texture.  See set_bg().
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_fg(self, DynamicTextFont_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_fg(DynamicTextFont self)
        
        /**
         * Returns the color of the foreground pixels of the font as they are rendered
         * into the font texture.  See set_fg().
         */
        """
        pass

    def get_font_pixel_size(self, DynamicTextFont_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_font_pixel_size(DynamicTextFont self)
        
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

    def get_line_height(self, DynamicTextFont_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_line_height(DynamicTextFont self)
        
        /**
         * Returns the number of units high each line of text is.
         */
        """
        pass

    def get_magfilter(self, DynamicTextFont_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_magfilter(DynamicTextFont self)
        
        /**
         * Returns the filter type used when enlarging the textures created for this
         * font.
         */
        """
        pass

    def get_minfilter(self, DynamicTextFont_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_minfilter(DynamicTextFont self)
        
        /**
         * Returns the filter type used when minimizing the textures created for this
         * font.
         */
        """
        pass

    def get_name(self, DynamicTextFont_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_name(DynamicTextFont self)
        
        /**
         * Disambiguates the get_name() method between that inherited from TextFont
         * and that inherited from FreetypeFont.
         */
        """
        pass

    def get_native_antialias(self, DynamicTextFont_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_native_antialias(DynamicTextFont self)
        
        /**
         * Returns whether Freetype's built-in antialias mode is enabled.  See
         * set_native_antialias().
         */
        """
        pass

    def get_num_pages(self, DynamicTextFont_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_pages(DynamicTextFont self)
        
        /**
         * Returns the number of pages associated with the font.  Initially, the font
         * has zero pages; when the first piece of text is rendered with the font, it
         * will add additional pages as needed.  Each page is a Texture object that
         * contains the images for each of the glyphs currently in use somewhere.
         */
        """
        pass

    def get_outline_color(self, DynamicTextFont_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_outline_color(DynamicTextFont self)
        
        /**
         * Returns the color of the outline pixels of the font as they are rendered
         * into the font texture.  See set_outline().
         */
        """
        pass

    def get_outline_feather(self, DynamicTextFont_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_outline_feather(DynamicTextFont self)
        
        /**
         * Returns the softness of the outline pixels of the font, as a value in the
         * range 0.0 to 1.0. See set_outline().
         */
        """
        pass

    def get_outline_width(self, DynamicTextFont_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_outline_width(DynamicTextFont self)
        
        /**
         * Returns the width of the outline pixels of the font, as the number of
         * points beyond each letter.  See set_outline().
         */
        """
        pass

    def get_page(self, DynamicTextFont_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_page(DynamicTextFont self, int n)
        
        /**
         * Returns the nth page associated with the font.  Initially, the font has
         * zero pages; when the first piece of text is rendered with the font, it will
         * add additional pages as needed.  Each page is a Texture object that
         * contains the images for each of the glyphs currently in use somewhere.
         */
        """
        pass

    def get_pages(self, *args, **kwargs): # real signature unknown
        pass

    def get_page_size(self, DynamicTextFont_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_page_size(DynamicTextFont self)
        
        /**
         * Returns the size of the textures that are created for the DynamicTextFont.
         * See set_page_size().
         */
        """
        pass

    def get_page_x_size(self, DynamicTextFont_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_page_x_size(DynamicTextFont self)
        
        /**
         * Returns the x size of the textures that are created for the
         * DynamicTextFont.  See set_page_size().
         */
        """
        pass

    def get_page_y_size(self, DynamicTextFont_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_page_y_size(DynamicTextFont self)
        
        /**
         * Returns the y size of the textures that are created for the
         * DynamicTextFont.  See set_page_size().
         */
        """
        pass

    def get_pixels_per_unit(self, DynamicTextFont_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_pixels_per_unit(DynamicTextFont self)
        
        /**
         * Returns the resolution of the texture map.  See set_pixels_per_unit().
         */
        """
        pass

    def get_point_size(self, DynamicTextFont_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_point_size(DynamicTextFont self)
        
        /**
         * Returns the point size of the font.
         */
        """
        pass

    def get_poly_margin(self, DynamicTextFont_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_poly_margin(DynamicTextFont self)
        
        /**
         * Returns the number of pixels of padding that is included around each glyph
         * in the generated polygons.  See set_poly_margin().
         */
        """
        pass

    def get_render_mode(self, DynamicTextFont_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_render_mode(DynamicTextFont self)
        
        /**
         * Returns the way the glyphs on this particular font are generated.  See
         * set_render_mode().
         */
        """
        pass

    def get_scale_factor(self, DynamicTextFont_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_scale_factor(DynamicTextFont self)
        
        /**
         * Returns the antialiasing scale factor.  See set_scale_factor().
         */
        """
        pass

    def get_space_advance(self, DynamicTextFont_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_space_advance(DynamicTextFont self)
        
        /**
         * Returns the number of units wide a space is.
         */
        """
        pass

    def get_texture_margin(self, DynamicTextFont_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_texture_margin(DynamicTextFont self)
        
        /**
         * Returns the number of pixels of padding that is added around the border of
         * each glyph in the texture map.  See set_texture_margin().
         */
        """
        pass

    def get_tex_format(self, DynamicTextFont_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_tex_format(DynamicTextFont self)
        
        /**
         * Returns the texture format used to render the individual pages.  This is
         * set automatically according to the colors selected.
         */
        """
        pass

    def makeCopy(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_copy(DynamicTextFont self)
        
        /**
         * Returns a new copy of the same font.
         */
        """
        pass

    def make_copy(self, DynamicTextFont_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_copy(DynamicTextFont self)
        
        /**
         * Returns a new copy of the same font.
         */
        """
        pass

    def setAnisotropicDegree(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_anisotropic_degree(const DynamicTextFont self, int anisotropic_degree)
        
        /**
         * Enables or disables anisotropic filtering on the textures created for this
         * font.  The default value is specified by the text-anisotropic-degree
         * variable.  See Texture::set_anisotropic_degree().
         */
        """
        pass

    def setBg(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_bg(const DynamicTextFont self, const LVecBase4f bg)
        
        /**
         * Changes the color of the background pixels of the font as they are rendered
         * into the font texture.  The default is (1, 1, 1, 0), or transparent white,
         * which allows text created with the font to be colored individually.  (Note
         * that it should not generally be (0, 0, 0, 0), which would tend to bleed
         * into the foreground color, unless you have also specified a outline color
         * of (0, 0, 0, 1)) .
         *
         * Normally, you would not change this unless you really need a particular
         * color effect to appear in the font itself.
         *
         * This should only be called before any characters have been requested out of
         * the font, or immediately after calling clear().
         */
        """
        pass

    def setFg(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_fg(const DynamicTextFont self, const LVecBase4f fg)
        
        /**
         * Changes the color of the foreground pixels of the font as they are rendered
         * into the font texture.  The default is (1, 1, 1, 1), or opaque white, which
         * allows text created with the font to be colored individually.  Normally,
         * you would not change this unless you really need a particular color effect
         * to appear in the font itself.
         *
         * This should only be called before any characters have been requested out of
         * the font, or immediately after calling clear().
         */
        """
        pass

    def setMagfilter(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_magfilter(const DynamicTextFont self, int filter)
        
        /**
         * Sets the filter type used when enlarging the textures created for this
         * font.
         */
        """
        pass

    def setMinfilter(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_minfilter(const DynamicTextFont self, int filter)
        
        /**
         * Sets the filter type used when minimizing the textures created for this
         * font.
         */
        """
        pass

    def setNativeAntialias(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_native_antialias(const DynamicTextFont self, bool native_antialias)
        
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

    def setOutline(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_outline(const DynamicTextFont self, const LVecBase4f outline_color, float outline_width, float outline_feather)
        
        /**
         * Sets up the font to have an outline around each font letter.  This is
         * achieved via a Gaussian post-process as each letter is generated; there is
         * some runtime cost for this effect, but it is minimal as each letter is
         * normally generated only once and then cached.
         *
         * The color is the desired color of the outline, width is the number of
         * points beyond the letter that the outline extends (a typical font is 10
         * points high), and feather is a number in the range 0.0 .. 1.0 that controls
         * the softness of the outline.  Set the width to 0.0 to disable the outline.
         *
         * This should only be called before any characters have been requested out of
         * the font, or immediately after calling clear().
         */
        """
        pass

    def setPageSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_page_size(const DynamicTextFont self, const LVecBase2i page_size)
        set_page_size(const DynamicTextFont self, int x_size, int y_size)
        
        /**
         * Sets the x, y size of the textures that are created for the
         * DynamicTextFont.
         */
        
        /**
         * Sets the x, y size of the textures that are created for the
         * DynamicTextFont.
         */
        """
        pass

    def setPixelsPerUnit(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_pixels_per_unit(const DynamicTextFont self, float pixels_per_unit)
        
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
        set_point_size(const DynamicTextFont self, float point_size)
        
        /**
         * Sets the point size of the font.  This controls the apparent size of the
         * font onscreen.  By convention, a 10 point font is about 1 screen unit high.
         *
         * This should only be called before any characters have been requested out of
         * the font, or immediately after calling clear().
         */
        """
        pass

    def setPolyMargin(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_poly_margin(const DynamicTextFont self, float poly_margin)
        
        /**
         * Sets the number of pixels of padding that is included around each glyph in
         * the generated polygons.  This helps prevent the edges of the glyphs from
         * being cut off at small minifications.  It is not related to the amount of
         * extra pixels reserved in the texture map (but it should be set somewhat
         * smaller than this number, which is controlled by set_texture_margin(), to
         * prevent bleed-in from neighboring letters in the texture).
         */
        """
        pass

    def setRenderMode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_render_mode(const DynamicTextFont self, int render_mode)
        
        /**
         * Specifies the way the glyphs on this particular font are generated.  The
         * default is RM_texture, which is the only mode supported for bitmap fonts.
         * Other modes are possible for most modern fonts.
         */
        """
        pass

    def setScaleFactor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_scale_factor(const DynamicTextFont self, float scale_factor)
        
        /**
         * Sets the factor by which the font is rendered larger by the FreeType
         * library before being filtered down to its actual size in the texture as
         * specified by set_pixels_per_unit().  This may be set to a number larger
         * than 1.0 to improve the font's antialiasing (since FreeType doesn't really
         * do a swell job of antialiasing by itself).  There is some performance
         * implication for setting this different than 1.0, but it is probably small.
         *
         * This should only be called before any characters have been requested out of
         * the font, or immediately after calling clear().
         */
        """
        pass

    def setTextureMargin(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_texture_margin(const DynamicTextFont self, int texture_margin)
        
        /**
         * Sets the number of pixels of padding that is added around the border of
         * each glyph before adding it to the texture map.  This reduces the bleed in
         * from neighboring glyphs in the texture map.
         */
        """
        pass

    def set_anisotropic_degree(self, const_DynamicTextFont_self, int_anisotropic_degree): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_anisotropic_degree(const DynamicTextFont self, int anisotropic_degree)
        
        /**
         * Enables or disables anisotropic filtering on the textures created for this
         * font.  The default value is specified by the text-anisotropic-degree
         * variable.  See Texture::set_anisotropic_degree().
         */
        """
        pass

    def set_bg(self, const_DynamicTextFont_self, const_LVecBase4f_bg): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_bg(const DynamicTextFont self, const LVecBase4f bg)
        
        /**
         * Changes the color of the background pixels of the font as they are rendered
         * into the font texture.  The default is (1, 1, 1, 0), or transparent white,
         * which allows text created with the font to be colored individually.  (Note
         * that it should not generally be (0, 0, 0, 0), which would tend to bleed
         * into the foreground color, unless you have also specified a outline color
         * of (0, 0, 0, 1)) .
         *
         * Normally, you would not change this unless you really need a particular
         * color effect to appear in the font itself.
         *
         * This should only be called before any characters have been requested out of
         * the font, or immediately after calling clear().
         */
        """
        pass

    def set_fg(self, const_DynamicTextFont_self, const_LVecBase4f_fg): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_fg(const DynamicTextFont self, const LVecBase4f fg)
        
        /**
         * Changes the color of the foreground pixels of the font as they are rendered
         * into the font texture.  The default is (1, 1, 1, 1), or opaque white, which
         * allows text created with the font to be colored individually.  Normally,
         * you would not change this unless you really need a particular color effect
         * to appear in the font itself.
         *
         * This should only be called before any characters have been requested out of
         * the font, or immediately after calling clear().
         */
        """
        pass

    def set_magfilter(self, const_DynamicTextFont_self, int_filter): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_magfilter(const DynamicTextFont self, int filter)
        
        /**
         * Sets the filter type used when enlarging the textures created for this
         * font.
         */
        """
        pass

    def set_minfilter(self, const_DynamicTextFont_self, int_filter): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_minfilter(const DynamicTextFont self, int filter)
        
        /**
         * Sets the filter type used when minimizing the textures created for this
         * font.
         */
        """
        pass

    def set_native_antialias(self, const_DynamicTextFont_self, bool_native_antialias): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_native_antialias(const DynamicTextFont self, bool native_antialias)
        
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

    def set_outline(self, const_DynamicTextFont_self, const_LVecBase4f_outline_color, float_outline_width, float_outline_feather): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_outline(const DynamicTextFont self, const LVecBase4f outline_color, float outline_width, float outline_feather)
        
        /**
         * Sets up the font to have an outline around each font letter.  This is
         * achieved via a Gaussian post-process as each letter is generated; there is
         * some runtime cost for this effect, but it is minimal as each letter is
         * normally generated only once and then cached.
         *
         * The color is the desired color of the outline, width is the number of
         * points beyond the letter that the outline extends (a typical font is 10
         * points high), and feather is a number in the range 0.0 .. 1.0 that controls
         * the softness of the outline.  Set the width to 0.0 to disable the outline.
         *
         * This should only be called before any characters have been requested out of
         * the font, or immediately after calling clear().
         */
        """
        pass

    def set_page_size(self, const_DynamicTextFont_self, const_LVecBase2i_page_size): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_page_size(const DynamicTextFont self, const LVecBase2i page_size)
        set_page_size(const DynamicTextFont self, int x_size, int y_size)
        
        /**
         * Sets the x, y size of the textures that are created for the
         * DynamicTextFont.
         */
        
        /**
         * Sets the x, y size of the textures that are created for the
         * DynamicTextFont.
         */
        """
        pass

    def set_pixels_per_unit(self, const_DynamicTextFont_self, float_pixels_per_unit): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_pixels_per_unit(const DynamicTextFont self, float pixels_per_unit)
        
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

    def set_point_size(self, const_DynamicTextFont_self, float_point_size): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_point_size(const DynamicTextFont self, float point_size)
        
        /**
         * Sets the point size of the font.  This controls the apparent size of the
         * font onscreen.  By convention, a 10 point font is about 1 screen unit high.
         *
         * This should only be called before any characters have been requested out of
         * the font, or immediately after calling clear().
         */
        """
        pass

    def set_poly_margin(self, const_DynamicTextFont_self, float_poly_margin): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_poly_margin(const DynamicTextFont self, float poly_margin)
        
        /**
         * Sets the number of pixels of padding that is included around each glyph in
         * the generated polygons.  This helps prevent the edges of the glyphs from
         * being cut off at small minifications.  It is not related to the amount of
         * extra pixels reserved in the texture map (but it should be set somewhat
         * smaller than this number, which is controlled by set_texture_margin(), to
         * prevent bleed-in from neighboring letters in the texture).
         */
        """
        pass

    def set_render_mode(self, const_DynamicTextFont_self, int_render_mode): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_render_mode(const DynamicTextFont self, int render_mode)
        
        /**
         * Specifies the way the glyphs on this particular font are generated.  The
         * default is RM_texture, which is the only mode supported for bitmap fonts.
         * Other modes are possible for most modern fonts.
         */
        """
        pass

    def set_scale_factor(self, const_DynamicTextFont_self, float_scale_factor): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_scale_factor(const DynamicTextFont self, float scale_factor)
        
        /**
         * Sets the factor by which the font is rendered larger by the FreeType
         * library before being filtered down to its actual size in the texture as
         * specified by set_pixels_per_unit().  This may be set to a number larger
         * than 1.0 to improve the font's antialiasing (since FreeType doesn't really
         * do a swell job of antialiasing by itself).  There is some performance
         * implication for setting this different than 1.0, but it is probably small.
         *
         * This should only be called before any characters have been requested out of
         * the font, or immediately after calling clear().
         */
        """
        pass

    def set_texture_margin(self, const_DynamicTextFont_self, int_texture_margin): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_texture_margin(const DynamicTextFont self, int texture_margin)
        
        /**
         * Sets the number of pixels of padding that is added around the border of
         * each glyph before adding it to the texture map.  This reduces the bleed in
         * from neighboring glyphs in the texture map.
         */
        """
        pass

    def upcastToFreetypeFont(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_FreetypeFont(const DynamicTextFont self)
        
        upcast from DynamicTextFont to FreetypeFont
        """
        pass

    def upcastToTextFont(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_TextFont(const DynamicTextFont self)
        
        upcast from DynamicTextFont to TextFont
        """
        pass

    def upcast_to_FreetypeFont(self, const_DynamicTextFont_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_FreetypeFont(const DynamicTextFont self)
        
        upcast from DynamicTextFont to FreetypeFont
        """
        pass

    def upcast_to_TextFont(self, const_DynamicTextFont_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_TextFont(const DynamicTextFont self)
        
        upcast from DynamicTextFont to TextFont
        """
        pass

    def write(self, DynamicTextFont_self, ostream_out, int_indent_level): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(DynamicTextFont self, ostream out, int indent_level)
        
        /**
         *
         */
        """
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __deepcopy__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    anisotropic_degree = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    bg = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    fg = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    font_pixel_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    magfilter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    minfilter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    native_antialias = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pages = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    page_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pixels_per_unit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    point_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    poly_margin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    render_mode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    scale_factor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    texture_margin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tex_format = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.DynamicTextFont' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.DynamicTextFont' objects>"
        '__doc__': '/**\n * A DynamicTextFont is a special TextFont object that rasterizes its glyphs\n * from a standard font file (e.g.  a TTF file) on the fly.  It requires the\n * FreeType 2.0 library (or any higher, backward-compatible version).\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.DynamicTextFont' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE35E550>'
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.DynamicTextFont' objects>"
        'anisotropic_degree': None, # (!) real value is "<attribute 'anisotropic_degree' of 'panda3d.core.DynamicTextFont' objects>"
        'bg': None, # (!) real value is "<attribute 'bg' of 'panda3d.core.DynamicTextFont' objects>"
        'clear': None, # (!) real value is "<method 'clear' of 'panda3d.core.DynamicTextFont' objects>"
        'fg': None, # (!) real value is "<attribute 'fg' of 'panda3d.core.DynamicTextFont' objects>"
        'font_pixel_size': None, # (!) real value is "<attribute 'font_pixel_size' of 'panda3d.core.DynamicTextFont' objects>"
        'garbageCollect': None, # (!) real value is "<method 'garbageCollect' of 'panda3d.core.DynamicTextFont' objects>"
        'garbage_collect': None, # (!) real value is "<method 'garbage_collect' of 'panda3d.core.DynamicTextFont' objects>"
        'getAnisotropicDegree': None, # (!) real value is "<method 'getAnisotropicDegree' of 'panda3d.core.DynamicTextFont' objects>"
        'getBg': None, # (!) real value is "<method 'getBg' of 'panda3d.core.DynamicTextFont' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE35E550>)>'
        'getFg': None, # (!) real value is "<method 'getFg' of 'panda3d.core.DynamicTextFont' objects>"
        'getFontPixelSize': None, # (!) real value is "<method 'getFontPixelSize' of 'panda3d.core.DynamicTextFont' objects>"
        'getLineHeight': None, # (!) real value is "<method 'getLineHeight' of 'panda3d.core.DynamicTextFont' objects>"
        'getMagfilter': None, # (!) real value is "<method 'getMagfilter' of 'panda3d.core.DynamicTextFont' objects>"
        'getMinfilter': None, # (!) real value is "<method 'getMinfilter' of 'panda3d.core.DynamicTextFont' objects>"
        'getName': None, # (!) real value is "<method 'getName' of 'panda3d.core.DynamicTextFont' objects>"
        'getNativeAntialias': None, # (!) real value is "<method 'getNativeAntialias' of 'panda3d.core.DynamicTextFont' objects>"
        'getNumPages': None, # (!) real value is "<method 'getNumPages' of 'panda3d.core.DynamicTextFont' objects>"
        'getOutlineColor': None, # (!) real value is "<method 'getOutlineColor' of 'panda3d.core.DynamicTextFont' objects>"
        'getOutlineFeather': None, # (!) real value is "<method 'getOutlineFeather' of 'panda3d.core.DynamicTextFont' objects>"
        'getOutlineWidth': None, # (!) real value is "<method 'getOutlineWidth' of 'panda3d.core.DynamicTextFont' objects>"
        'getPage': None, # (!) real value is "<method 'getPage' of 'panda3d.core.DynamicTextFont' objects>"
        'getPageSize': None, # (!) real value is "<method 'getPageSize' of 'panda3d.core.DynamicTextFont' objects>"
        'getPageXSize': None, # (!) real value is "<method 'getPageXSize' of 'panda3d.core.DynamicTextFont' objects>"
        'getPageYSize': None, # (!) real value is "<method 'getPageYSize' of 'panda3d.core.DynamicTextFont' objects>"
        'getPages': None, # (!) real value is "<method 'getPages' of 'panda3d.core.DynamicTextFont' objects>"
        'getPixelsPerUnit': None, # (!) real value is "<method 'getPixelsPerUnit' of 'panda3d.core.DynamicTextFont' objects>"
        'getPointSize': None, # (!) real value is "<method 'getPointSize' of 'panda3d.core.DynamicTextFont' objects>"
        'getPolyMargin': None, # (!) real value is "<method 'getPolyMargin' of 'panda3d.core.DynamicTextFont' objects>"
        'getRenderMode': None, # (!) real value is "<method 'getRenderMode' of 'panda3d.core.DynamicTextFont' objects>"
        'getScaleFactor': None, # (!) real value is "<method 'getScaleFactor' of 'panda3d.core.DynamicTextFont' objects>"
        'getSpaceAdvance': None, # (!) real value is "<method 'getSpaceAdvance' of 'panda3d.core.DynamicTextFont' objects>"
        'getTexFormat': None, # (!) real value is "<method 'getTexFormat' of 'panda3d.core.DynamicTextFont' objects>"
        'getTextureMargin': None, # (!) real value is "<method 'getTextureMargin' of 'panda3d.core.DynamicTextFont' objects>"
        'get_anisotropic_degree': None, # (!) real value is "<method 'get_anisotropic_degree' of 'panda3d.core.DynamicTextFont' objects>"
        'get_bg': None, # (!) real value is "<method 'get_bg' of 'panda3d.core.DynamicTextFont' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE35E550>)>'
        'get_fg': None, # (!) real value is "<method 'get_fg' of 'panda3d.core.DynamicTextFont' objects>"
        'get_font_pixel_size': None, # (!) real value is "<method 'get_font_pixel_size' of 'panda3d.core.DynamicTextFont' objects>"
        'get_line_height': None, # (!) real value is "<method 'get_line_height' of 'panda3d.core.DynamicTextFont' objects>"
        'get_magfilter': None, # (!) real value is "<method 'get_magfilter' of 'panda3d.core.DynamicTextFont' objects>"
        'get_minfilter': None, # (!) real value is "<method 'get_minfilter' of 'panda3d.core.DynamicTextFont' objects>"
        'get_name': None, # (!) real value is "<method 'get_name' of 'panda3d.core.DynamicTextFont' objects>"
        'get_native_antialias': None, # (!) real value is "<method 'get_native_antialias' of 'panda3d.core.DynamicTextFont' objects>"
        'get_num_pages': None, # (!) real value is "<method 'get_num_pages' of 'panda3d.core.DynamicTextFont' objects>"
        'get_outline_color': None, # (!) real value is "<method 'get_outline_color' of 'panda3d.core.DynamicTextFont' objects>"
        'get_outline_feather': None, # (!) real value is "<method 'get_outline_feather' of 'panda3d.core.DynamicTextFont' objects>"
        'get_outline_width': None, # (!) real value is "<method 'get_outline_width' of 'panda3d.core.DynamicTextFont' objects>"
        'get_page': None, # (!) real value is "<method 'get_page' of 'panda3d.core.DynamicTextFont' objects>"
        'get_page_size': None, # (!) real value is "<method 'get_page_size' of 'panda3d.core.DynamicTextFont' objects>"
        'get_page_x_size': None, # (!) real value is "<method 'get_page_x_size' of 'panda3d.core.DynamicTextFont' objects>"
        'get_page_y_size': None, # (!) real value is "<method 'get_page_y_size' of 'panda3d.core.DynamicTextFont' objects>"
        'get_pages': None, # (!) real value is "<method 'get_pages' of 'panda3d.core.DynamicTextFont' objects>"
        'get_pixels_per_unit': None, # (!) real value is "<method 'get_pixels_per_unit' of 'panda3d.core.DynamicTextFont' objects>"
        'get_point_size': None, # (!) real value is "<method 'get_point_size' of 'panda3d.core.DynamicTextFont' objects>"
        'get_poly_margin': None, # (!) real value is "<method 'get_poly_margin' of 'panda3d.core.DynamicTextFont' objects>"
        'get_render_mode': None, # (!) real value is "<method 'get_render_mode' of 'panda3d.core.DynamicTextFont' objects>"
        'get_scale_factor': None, # (!) real value is "<method 'get_scale_factor' of 'panda3d.core.DynamicTextFont' objects>"
        'get_space_advance': None, # (!) real value is "<method 'get_space_advance' of 'panda3d.core.DynamicTextFont' objects>"
        'get_tex_format': None, # (!) real value is "<method 'get_tex_format' of 'panda3d.core.DynamicTextFont' objects>"
        'get_texture_margin': None, # (!) real value is "<method 'get_texture_margin' of 'panda3d.core.DynamicTextFont' objects>"
        'magfilter': None, # (!) real value is "<attribute 'magfilter' of 'panda3d.core.DynamicTextFont' objects>"
        'makeCopy': None, # (!) real value is "<method 'makeCopy' of 'panda3d.core.DynamicTextFont' objects>"
        'make_copy': None, # (!) real value is "<method 'make_copy' of 'panda3d.core.DynamicTextFont' objects>"
        'minfilter': None, # (!) real value is "<attribute 'minfilter' of 'panda3d.core.DynamicTextFont' objects>"
        'native_antialias': None, # (!) real value is "<attribute 'native_antialias' of 'panda3d.core.DynamicTextFont' objects>"
        'page_size': None, # (!) real value is "<attribute 'page_size' of 'panda3d.core.DynamicTextFont' objects>"
        'pages': None, # (!) real value is "<attribute 'pages' of 'panda3d.core.DynamicTextFont' objects>"
        'pixels_per_unit': None, # (!) real value is "<attribute 'pixels_per_unit' of 'panda3d.core.DynamicTextFont' objects>"
        'point_size': None, # (!) real value is "<attribute 'point_size' of 'panda3d.core.DynamicTextFont' objects>"
        'poly_margin': None, # (!) real value is "<attribute 'poly_margin' of 'panda3d.core.DynamicTextFont' objects>"
        'render_mode': None, # (!) real value is "<attribute 'render_mode' of 'panda3d.core.DynamicTextFont' objects>"
        'scale_factor': None, # (!) real value is "<attribute 'scale_factor' of 'panda3d.core.DynamicTextFont' objects>"
        'setAnisotropicDegree': None, # (!) real value is "<method 'setAnisotropicDegree' of 'panda3d.core.DynamicTextFont' objects>"
        'setBg': None, # (!) real value is "<method 'setBg' of 'panda3d.core.DynamicTextFont' objects>"
        'setFg': None, # (!) real value is "<method 'setFg' of 'panda3d.core.DynamicTextFont' objects>"
        'setMagfilter': None, # (!) real value is "<method 'setMagfilter' of 'panda3d.core.DynamicTextFont' objects>"
        'setMinfilter': None, # (!) real value is "<method 'setMinfilter' of 'panda3d.core.DynamicTextFont' objects>"
        'setNativeAntialias': None, # (!) real value is "<method 'setNativeAntialias' of 'panda3d.core.DynamicTextFont' objects>"
        'setOutline': None, # (!) real value is "<method 'setOutline' of 'panda3d.core.DynamicTextFont' objects>"
        'setPageSize': None, # (!) real value is "<method 'setPageSize' of 'panda3d.core.DynamicTextFont' objects>"
        'setPixelsPerUnit': None, # (!) real value is "<method 'setPixelsPerUnit' of 'panda3d.core.DynamicTextFont' objects>"
        'setPointSize': None, # (!) real value is "<method 'setPointSize' of 'panda3d.core.DynamicTextFont' objects>"
        'setPolyMargin': None, # (!) real value is "<method 'setPolyMargin' of 'panda3d.core.DynamicTextFont' objects>"
        'setRenderMode': None, # (!) real value is "<method 'setRenderMode' of 'panda3d.core.DynamicTextFont' objects>"
        'setScaleFactor': None, # (!) real value is "<method 'setScaleFactor' of 'panda3d.core.DynamicTextFont' objects>"
        'setTextureMargin': None, # (!) real value is "<method 'setTextureMargin' of 'panda3d.core.DynamicTextFont' objects>"
        'set_anisotropic_degree': None, # (!) real value is "<method 'set_anisotropic_degree' of 'panda3d.core.DynamicTextFont' objects>"
        'set_bg': None, # (!) real value is "<method 'set_bg' of 'panda3d.core.DynamicTextFont' objects>"
        'set_fg': None, # (!) real value is "<method 'set_fg' of 'panda3d.core.DynamicTextFont' objects>"
        'set_magfilter': None, # (!) real value is "<method 'set_magfilter' of 'panda3d.core.DynamicTextFont' objects>"
        'set_minfilter': None, # (!) real value is "<method 'set_minfilter' of 'panda3d.core.DynamicTextFont' objects>"
        'set_native_antialias': None, # (!) real value is "<method 'set_native_antialias' of 'panda3d.core.DynamicTextFont' objects>"
        'set_outline': None, # (!) real value is "<method 'set_outline' of 'panda3d.core.DynamicTextFont' objects>"
        'set_page_size': None, # (!) real value is "<method 'set_page_size' of 'panda3d.core.DynamicTextFont' objects>"
        'set_pixels_per_unit': None, # (!) real value is "<method 'set_pixels_per_unit' of 'panda3d.core.DynamicTextFont' objects>"
        'set_point_size': None, # (!) real value is "<method 'set_point_size' of 'panda3d.core.DynamicTextFont' objects>"
        'set_poly_margin': None, # (!) real value is "<method 'set_poly_margin' of 'panda3d.core.DynamicTextFont' objects>"
        'set_render_mode': None, # (!) real value is "<method 'set_render_mode' of 'panda3d.core.DynamicTextFont' objects>"
        'set_scale_factor': None, # (!) real value is "<method 'set_scale_factor' of 'panda3d.core.DynamicTextFont' objects>"
        'set_texture_margin': None, # (!) real value is "<method 'set_texture_margin' of 'panda3d.core.DynamicTextFont' objects>"
        'tex_format': None, # (!) real value is "<attribute 'tex_format' of 'panda3d.core.DynamicTextFont' objects>"
        'texture_margin': None, # (!) real value is "<attribute 'texture_margin' of 'panda3d.core.DynamicTextFont' objects>"
        'upcastToFreetypeFont': None, # (!) real value is "<method 'upcastToFreetypeFont' of 'panda3d.core.DynamicTextFont' objects>"
        'upcastToTextFont': None, # (!) real value is "<method 'upcastToTextFont' of 'panda3d.core.DynamicTextFont' objects>"
        'upcast_to_FreetypeFont': None, # (!) real value is "<method 'upcast_to_FreetypeFont' of 'panda3d.core.DynamicTextFont' objects>"
        'upcast_to_TextFont': None, # (!) real value is "<method 'upcast_to_TextFont' of 'panda3d.core.DynamicTextFont' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.core.DynamicTextFont' objects>"
    }


