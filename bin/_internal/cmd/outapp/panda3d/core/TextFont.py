# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .TypedReferenceCount import TypedReferenceCount

from .Namable import Namable

class TextFont(TypedReferenceCount, Namable):
    """
    /**
     * An encapsulation of a font; i.e.  a set of glyphs that may be assembled
     * together by a TextNode to represent a string of text.
     *
     * This is just an abstract interface; see StaticTextFont or DynamicTextFont
     * for an actual implementation.
     */
    """
    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getGlyph(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_glyph(const TextFont self, int character)
        
        /**
         * Gets the glyph associated with the given character code, as well as an
         * optional scaling parameter that should be applied to the glyph's geometry
         * and advance parameters.  Returns the glyph on success.  On failure, it may
         * still return a printable glyph, or it may return NULL.
         */
        """
        pass

    def getKerning(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_kerning(TextFont self, int first, int second)
        
        /**
         * Returns the amount by which to offset the second glyph when it directly
         * follows the first glyph.  This is an additional offset that is added on top
         * of the advance.
         */
        """
        pass

    def getLineHeight(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_line_height(TextFont self)
        
        /**
         * Returns the number of units high each line of text is.
         */
        """
        pass

    def getSpaceAdvance(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_space_advance(TextFont self)
        
        /**
         * Returns the number of units wide a space is.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_glyph(self, const_TextFont_self, int_character): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_glyph(const TextFont self, int character)
        
        /**
         * Gets the glyph associated with the given character code, as well as an
         * optional scaling parameter that should be applied to the glyph's geometry
         * and advance parameters.  Returns the glyph on success.  On failure, it may
         * still return a printable glyph, or it may return NULL.
         */
        """
        pass

    def get_kerning(self, TextFont_self, int_first, int_second): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_kerning(TextFont self, int first, int second)
        
        /**
         * Returns the amount by which to offset the second glyph when it directly
         * follows the first glyph.  This is an additional offset that is added on top
         * of the advance.
         */
        """
        pass

    def get_line_height(self, TextFont_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_line_height(TextFont self)
        
        /**
         * Returns the number of units high each line of text is.
         */
        """
        pass

    def get_space_advance(self, TextFont_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_space_advance(TextFont self)
        
        /**
         * Returns the number of units wide a space is.
         */
        """
        pass

    def isValid(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_valid(TextFont self)
        
        /**
         * Returns true if the font is valid and ready to use, false otherwise.
         */
        """
        pass

    def is_valid(self, TextFont_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_valid(TextFont self)
        
        /**
         * Returns true if the font is valid and ready to use, false otherwise.
         */
        """
        pass

    def makeCopy(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_copy(TextFont self)
        """
        pass

    def make_copy(self, TextFont_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_copy(TextFont self)
        """
        pass

    def setLineHeight(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_line_height(const TextFont self, float line_height)
        
        /**
         * Changes the number of units high each line of text is.
         */
        """
        pass

    def setSpaceAdvance(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_space_advance(const TextFont self, float space_advance)
        
        /**
         * Changes the number of units wide a space is.
         */
        """
        pass

    def set_line_height(self, const_TextFont_self, float_line_height): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_line_height(const TextFont self, float line_height)
        
        /**
         * Changes the number of units high each line of text is.
         */
        """
        pass

    def set_space_advance(self, const_TextFont_self, float_space_advance): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_space_advance(const TextFont self, float space_advance)
        
        /**
         * Changes the number of units wide a space is.
         */
        """
        pass

    def upcastToNamable(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_Namable(const TextFont self)
        
        upcast from TextFont to Namable
        """
        pass

    def upcastToTypedReferenceCount(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_TypedReferenceCount(const TextFont self)
        
        upcast from TextFont to TypedReferenceCount
        """
        pass

    def upcast_to_Namable(self, const_TextFont_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_Namable(const TextFont self)
        
        upcast from TextFont to Namable
        """
        pass

    def upcast_to_TypedReferenceCount(self, const_TextFont_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_TypedReferenceCount(const TextFont self)
        
        upcast from TextFont to TypedReferenceCount
        """
        pass

    def write(self, TextFont_self, ostream_out, int_indent_level): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(TextFont self, ostream out, int indent_level)
        
        /**
         *
         */
        """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ True if self else False """
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

    line_height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    space_advance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    valid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        'RMDistanceField': 5,
        'RMExtruded': 3,
        'RMInvalid': 6,
        'RMPolygon': 2,
        'RMSolid': 4,
        'RMTexture': 0,
        'RMWireframe': 1,
        'RM_distance_field': 5,
        'RM_extruded': 3,
        'RM_invalid': 6,
        'RM_polygon': 2,
        'RM_solid': 4,
        'RM_texture': 0,
        'RM_wireframe': 1,
        '__bool__': None, # (!) real value is "<slot wrapper '__bool__' of 'panda3d.core.TextFont' objects>"
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.TextFont' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.TextFont' objects>"
        '__doc__': '/**\n * An encapsulation of a font; i.e.  a set of glyphs that may be assembled\n * together by a TextNode to represent a string of text.\n *\n * This is just an abstract interface; see StaticTextFont or DynamicTextFont\n * for an actual implementation.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.TextFont' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE35DFE0>'
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.TextFont' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE35DFE0>)>'
        'getGlyph': None, # (!) real value is "<method 'getGlyph' of 'panda3d.core.TextFont' objects>"
        'getKerning': None, # (!) real value is "<method 'getKerning' of 'panda3d.core.TextFont' objects>"
        'getLineHeight': None, # (!) real value is "<method 'getLineHeight' of 'panda3d.core.TextFont' objects>"
        'getSpaceAdvance': None, # (!) real value is "<method 'getSpaceAdvance' of 'panda3d.core.TextFont' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE35DFE0>)>'
        'get_glyph': None, # (!) real value is "<method 'get_glyph' of 'panda3d.core.TextFont' objects>"
        'get_kerning': None, # (!) real value is "<method 'get_kerning' of 'panda3d.core.TextFont' objects>"
        'get_line_height': None, # (!) real value is "<method 'get_line_height' of 'panda3d.core.TextFont' objects>"
        'get_space_advance': None, # (!) real value is "<method 'get_space_advance' of 'panda3d.core.TextFont' objects>"
        'isValid': None, # (!) real value is "<method 'isValid' of 'panda3d.core.TextFont' objects>"
        'is_valid': None, # (!) real value is "<method 'is_valid' of 'panda3d.core.TextFont' objects>"
        'line_height': None, # (!) real value is "<attribute 'line_height' of 'panda3d.core.TextFont' objects>"
        'makeCopy': None, # (!) real value is "<method 'makeCopy' of 'panda3d.core.TextFont' objects>"
        'make_copy': None, # (!) real value is "<method 'make_copy' of 'panda3d.core.TextFont' objects>"
        'setLineHeight': None, # (!) real value is "<method 'setLineHeight' of 'panda3d.core.TextFont' objects>"
        'setSpaceAdvance': None, # (!) real value is "<method 'setSpaceAdvance' of 'panda3d.core.TextFont' objects>"
        'set_line_height': None, # (!) real value is "<method 'set_line_height' of 'panda3d.core.TextFont' objects>"
        'set_space_advance': None, # (!) real value is "<method 'set_space_advance' of 'panda3d.core.TextFont' objects>"
        'space_advance': None, # (!) real value is "<attribute 'space_advance' of 'panda3d.core.TextFont' objects>"
        'upcastToNamable': None, # (!) real value is "<method 'upcastToNamable' of 'panda3d.core.TextFont' objects>"
        'upcastToTypedReferenceCount': None, # (!) real value is "<method 'upcastToTypedReferenceCount' of 'panda3d.core.TextFont' objects>"
        'upcast_to_Namable': None, # (!) real value is "<method 'upcast_to_Namable' of 'panda3d.core.TextFont' objects>"
        'upcast_to_TypedReferenceCount': None, # (!) real value is "<method 'upcast_to_TypedReferenceCount' of 'panda3d.core.TextFont' objects>"
        'valid': None, # (!) real value is "<attribute 'valid' of 'panda3d.core.TextFont' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.core.TextFont' objects>"
    }
    RMDistanceField = 5
    RMExtruded = 3
    RMInvalid = 6
    RMPolygon = 2
    RMSolid = 4
    RMTexture = 0
    RMWireframe = 1
    RM_distance_field = 5
    RM_extruded = 3
    RM_invalid = 6
    RM_polygon = 2
    RM_solid = 4
    RM_texture = 0
    RM_wireframe = 1


