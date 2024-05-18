# encoding: utf-8
# module matplotlib.ft2font
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\matplotlib\ft2font.cp311-win_amd64.pyd
# by generator 1.147
# no doc
# no imports

# Variables with simple values

BOLD = 2

EXTERNAL_STREAM = 1024

FAST_GLYPHS = 128

FIXED_SIZES = 2
FIXED_WIDTH = 4

GLYPH_NAMES = 512

HORIZONTAL = 16

ITALIC = 1

KERNING = 64

KERNING_DEFAULT = 0
KERNING_UNFITTED = 1
KERNING_UNSCALED = 2

LOAD_CROP_BITMAP = 64

LOAD_DEFAULT = 0

LOAD_FORCE_AUTOHINT = 32

LOAD_IGNORE_GLOBAL_ADVANCE_WIDTH = 512

LOAD_IGNORE_TRANSFORM = 2048

LOAD_LINEAR_DESIGN = 8192

LOAD_MONOCHROME = 4096

LOAD_NO_AUTOHINT = 32768
LOAD_NO_BITMAP = 8
LOAD_NO_HINTING = 2
LOAD_NO_RECURSE = 1024
LOAD_NO_SCALE = 1

LOAD_PEDANTIC = 128
LOAD_RENDER = 4

LOAD_TARGET_LCD = 196608

LOAD_TARGET_LCD_V = 262144

LOAD_TARGET_LIGHT = 65536
LOAD_TARGET_MONO = 131072
LOAD_TARGET_NORMAL = 0

LOAD_VERTICAL_LAYOUT = 16

MULTIPLE_MASTERS = 256

SCALABLE = 1

SFNT = 8

VERTICAL = 32

__freetype_build_type__ = 'local'

__freetype_version__ = '2.6.1'

# no functions
# classes

class FT2Font(object):
    """
    Create a new FT2Font object.
    
    Parameters
    ----------
    filename : str or file-like
        The source of the font data in a format (ttf or ttc) that FreeType can read
    
    hinting_factor : int, optional
        Must be positive. Used to scale the hinting in the x-direction
    _fallback_list : list of FT2Font, optional
        A list of FT2Font objects used to find missing glyphs.
    
        .. warning::
            This API is both private and provisional: do not use it directly
    
    _kerning_factor : int, optional
        Used to adjust the degree of kerning.
    
        .. warning::
            This API is private: do not use it directly
    
    Attributes
    ----------
    num_faces : int
        Number of faces in file.
    face_flags, style_flags : int
        Face and style flags; see the ft2font constants.
    num_glyphs : int
        Number of glyphs in the face.
    family_name, style_name : str
        Face family and style name.
    num_fixed_sizes : int
        Number of bitmap in the face.
    scalable : bool
        Whether face is scalable; attributes after this one are only
        defined for scalable faces.
    bbox : tuple[int, int, int, int]
        Face global bounding box (xmin, ymin, xmax, ymax).
    units_per_EM : int
        Number of font units covered by the EM.
    ascender, descender : int
        Ascender and descender in 26.6 units.
    height : int
        Height in 26.6 units; used to compute a default line spacing
        (baseline-to-baseline distance).
    max_advance_width, max_advance_height : int
        Maximum horizontal and vertical cursor advance for all glyphs.
    underline_position, underline_thickness : int
        Vertical position and thickness of the underline bar.
    postscript_name : str
        PostScript name of the font.
    """
    def clear(self, *args, **kwargs): # real signature unknown
        """ Clear all the glyphs, reset for a new call to `.set_text`. """
        pass

    def draw_glyphs_to_bitmap(self, *args, **kwargs): # real signature unknown
        """
        Draw the glyphs that were loaded by `.set_text` to the bitmap.
        The bitmap size will be automatically set to include the glyphs.
        """
        pass

    def draw_glyph_to_bitmap(self, *args, **kwargs): # real signature unknown
        """
        Draw a single glyph to the bitmap at pixel locations x, y
        Note it is your responsibility to set up the bitmap manually
        with ``set_bitmap_size(w, h)`` before this call is made.
        
        If you want automatic layout, use `.set_text` in combinations with
        `.draw_glyphs_to_bitmap`.  This function is instead intended for people
        who want to render individual glyphs (e.g., returned by `.load_char`)
        at precise locations.
        """
        pass

    def get_bitmap_offset(self, *args, **kwargs): # real signature unknown
        """
        Get the (x, y) offset in 26.6 subpixels for the bitmap if ink hangs left or below (0, 0).
        Since Matplotlib only supports left-to-right text, y is always 0.
        """
        pass

    def get_charmap(self, *args, **kwargs): # real signature unknown
        """
        Return a dict that maps the character codes of the selected charmap
        (Unicode by default) to their corresponding glyph indices.
        """
        pass

    def get_char_index(self, *args, **kwargs): # real signature unknown
        """ Return the glyph index corresponding to a character *codepoint*. """
        pass

    def get_descent(self, *args, **kwargs): # real signature unknown
        """
        Get the descent in 26.6 subpixels of the current string set by `.set_text`.
        The rotation of the string is accounted for.  To get the descent
        in pixels, divide this value by 64.
        """
        pass

    def get_glyph_name(self, *args, **kwargs): # real signature unknown
        """
        Retrieve the ASCII name of a given glyph *index* in a face.
        
        Due to Matplotlib's internal design, for fonts that do not contain glyph
        names (per FT_FACE_FLAG_GLYPH_NAMES), this returns a made-up name which
        does *not* roundtrip through `.get_name_index`.
        """
        pass

    def get_image(self, *args, **kwargs): # real signature unknown
        """ Return the underlying image buffer for this font object. """
        pass

    def get_kerning(self, *args, **kwargs): # real signature unknown
        """
        Get the kerning between *left* and *right* glyph indices.
        *mode* is a kerning mode constant:
        
        - KERNING_DEFAULT  - Return scaled and grid-fitted kerning distances
        - KERNING_UNFITTED - Return scaled but un-grid-fitted kerning distances
        - KERNING_UNSCALED - Return the kerning vector in original font units
        """
        pass

    def get_name_index(self, *args, **kwargs): # real signature unknown
        """
        Return the glyph index of a given glyph *name*.
        The glyph index 0 means 'undefined character code'.
        """
        pass

    def get_num_glyphs(self, *args, **kwargs): # real signature unknown
        """ Return the number of loaded glyphs. """
        pass

    def get_path(self, *args, **kwargs): # real signature unknown
        """ Get the path data from the currently loaded glyph as a tuple of vertices, codes. """
        pass

    def get_ps_font_info(self, *args, **kwargs): # real signature unknown
        """ Return the information in the PS Font Info structure. """
        pass

    def get_sfnt(self, *args, **kwargs): # real signature unknown
        """
        Load the entire SFNT names table, as a dict whose keys are
        (platform-ID, ISO-encoding-scheme, language-code, and description)
        tuples.
        """
        pass

    def get_sfnt_table(self, *args, **kwargs): # real signature unknown
        """ Return one of the following SFNT tables: head, maxp, OS/2, hhea, vhea, post, or pclt. """
        pass

    def get_width_height(self, *args, **kwargs): # real signature unknown
        """
        Get the width and height in 26.6 subpixels of the current string set by `.set_text`.
        The rotation of the string is accounted for.  To get width and height
        in pixels, divide these values by 64.
        """
        pass

    def get_xys(self, *args, **kwargs): # real signature unknown
        """
        Get the xy locations of the current glyphs.
        
        .. deprecated:: 3.8
        """
        pass

    def load_char(self, *args, **kwargs): # real signature unknown
        """
        Load character with *charcode* in current fontfile and set glyph.
        *flags* can be a bitwise-or of the LOAD_XXX constants;
        the default value is LOAD_FORCE_AUTOHINT.
        Return value is a Glyph object, with attributes
        
        - width: glyph width
        - height: glyph height
        - bbox: the glyph bbox (xmin, ymin, xmax, ymax)
        - horiBearingX: left side bearing in horizontal layouts
        - horiBearingY: top side bearing in horizontal layouts
        - horiAdvance: advance width for horizontal layout
        - vertBearingX: left side bearing in vertical layouts
        - vertBearingY: top side bearing in vertical layouts
        - vertAdvance: advance height for vertical layout
        """
        pass

    def load_glyph(self, *args, **kwargs): # real signature unknown
        """
        Load character with *glyphindex* in current fontfile and set glyph.
        *flags* can be a bitwise-or of the LOAD_XXX constants;
        the default value is LOAD_FORCE_AUTOHINT.
        Return value is a Glyph object, with attributes
        
        - width: glyph width
        - height: glyph height
        - bbox: the glyph bbox (xmin, ymin, xmax, ymax)
        - horiBearingX: left side bearing in horizontal layouts
        - horiBearingY: top side bearing in horizontal layouts
        - horiAdvance: advance width for horizontal layout
        - vertBearingX: left side bearing in vertical layouts
        - vertBearingY: top side bearing in vertical layouts
        - vertAdvance: advance height for vertical layout
        """
        pass

    def select_charmap(self, *args, **kwargs): # real signature unknown
        """ Select a charmap by its FT_Encoding number. """
        pass

    def set_charmap(self, *args, **kwargs): # real signature unknown
        """ Make the i-th charmap current. """
        pass

    def set_size(self, *args, **kwargs): # real signature unknown
        """ Set the point size and dpi of the text. """
        pass

    def set_text(self, *args, **kwargs): # real signature unknown
        """
        Set the text *string* and *angle*.
        *flags* can be a bitwise-or of the LOAD_XXX constants;
        the default value is LOAD_FORCE_AUTOHINT.
        You must call this before `.draw_glyphs_to_bitmap`.
        A sequence of x,y positions is returned.
        """
        pass

    def _get_fontmap(self, *args, **kwargs): # real signature unknown
        """
        Get a mapping between characters and the font that includes them.
        A dictionary mapping unicode characters to PyFT2Font objects.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    ascender = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    bbox = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    descender = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    face_flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    family_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    fname = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    max_advance_height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    max_advance_width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    num_charmaps = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    num_faces = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    num_fixed_sizes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    num_glyphs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    postscript_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    scalable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    style_flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    style_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    underline_position = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    underline_thickness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    units_per_EM = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class FT2Image(object):
    # no doc
    def draw_rect(self, *args, **kwargs): # real signature unknown
        """
        Draw an empty rectangle to the image.
        
        .. deprecated:: 3.8
        """
        pass

    def draw_rect_filled(self, *args, **kwargs): # real signature unknown
        """ Draw a filled rectangle to the image. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x0000021D04ECFF50>'

__spec__ = None # (!) real value is "ModuleSpec(name='matplotlib.ft2font', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x0000021D04ECFF50>, origin='C:\\\\Users\\\\leonm\\\\PycharmProjects\\\\leonsystem\\\\venv\\\\Lib\\\\site-packages\\\\matplotlib\\\\ft2font.cp311-win_amd64.pyd')"

