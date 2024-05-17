# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .TypedReferenceCount import TypedReferenceCount

class TextGlyph(TypedReferenceCount):
    """
    /**
     * A representation of a single glyph (character) from a font.  This is a
     * piece of renderable geometry of some kind.
     */
    """
    def getAdvance(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_advance(TextGlyph self)
        
        /**
         * Returns the distance by which the character pointer should be advanced
         * after placing this character; i.e.  the approximate width the character
         * takes up on the line.
         */
        """
        pass

    def getCharacter(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_character(TextGlyph self)
        
        /**
         * Returns the Unicode value that corresponds to the character this glyph
         * represents.
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getGeom(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_geom(TextGlyph self, int usage_hint)
        
        /**
         * Returns a Geom that renders the particular glyph.  It will be generated if
         * necessary.
         *
         * This method will always return a copy of the Geom, so the caller is free to
         * modify it.
         */
        """
        pass

    def getQuad(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_quad(TextGlyph self, LVecBase4f dimensions, LVecBase4f texcoords)
        
        /**
         * Assuming that this glyph is representable as a textured quad, returns its
         * dimensions and UV range.  Returns false if it is not representable as a
         * quad, or if it is whitespace.
         *
         * The order of the components is left, bottom, right, top.
         */
        """
        pass

    def getState(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_state(TextGlyph self)
        
        /**
         * Returns the state in which the glyph should be rendered.
         */
        """
        pass

    def get_advance(self, TextGlyph_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_advance(TextGlyph self)
        
        /**
         * Returns the distance by which the character pointer should be advanced
         * after placing this character; i.e.  the approximate width the character
         * takes up on the line.
         */
        """
        pass

    def get_character(self, TextGlyph_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_character(TextGlyph self)
        
        /**
         * Returns the Unicode value that corresponds to the character this glyph
         * represents.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_geom(self, TextGlyph_self, int_usage_hint): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_geom(TextGlyph self, int usage_hint)
        
        /**
         * Returns a Geom that renders the particular glyph.  It will be generated if
         * necessary.
         *
         * This method will always return a copy of the Geom, so the caller is free to
         * modify it.
         */
        """
        pass

    def get_quad(self, TextGlyph_self, LVecBase4f_dimensions, LVecBase4f_texcoords): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_quad(TextGlyph self, LVecBase4f dimensions, LVecBase4f texcoords)
        
        /**
         * Assuming that this glyph is representable as a textured quad, returns its
         * dimensions and UV range.  Returns false if it is not representable as a
         * quad, or if it is whitespace.
         *
         * The order of the components is left, bottom, right, top.
         */
        """
        pass

    def get_state(self, TextGlyph_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_state(TextGlyph self)
        
        /**
         * Returns the state in which the glyph should be rendered.
         */
        """
        pass

    def hasQuad(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_quad(TextGlyph self)
        
        /**
         * Returns true if this glyph contains the definition for a simple quad,
         * rather than a more complex piece of geometry.
         *
         * You may still call get_geom() even if this returns true, which will
         * synthesize a Geom for this quad.
         */
        """
        pass

    def has_quad(self, TextGlyph_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_quad(TextGlyph self)
        
        /**
         * Returns true if this glyph contains the definition for a simple quad,
         * rather than a more complex piece of geometry.
         *
         * You may still call get_geom() even if this returns true, which will
         * synthesize a Geom for this quad.
         */
        """
        pass

    def isWhitespace(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_whitespace(TextGlyph self)
        
        /**
         * Returns true if this glyph represents invisible whitespace, or false if it
         * corresponds to some visible character.
         */
        """
        pass

    def is_whitespace(self, TextGlyph_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_whitespace(TextGlyph self)
        
        /**
         * Returns true if this glyph represents invisible whitespace, or false if it
         * corresponds to some visible character.
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    advance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    character = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * A representation of a single glyph (character) from a font.  This is a\n * piece of renderable geometry of some kind.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.TextGlyph' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE35DE00>'
        'advance': None, # (!) real value is "<attribute 'advance' of 'panda3d.core.TextGlyph' objects>"
        'character': None, # (!) real value is "<attribute 'character' of 'panda3d.core.TextGlyph' objects>"
        'getAdvance': None, # (!) real value is "<method 'getAdvance' of 'panda3d.core.TextGlyph' objects>"
        'getCharacter': None, # (!) real value is "<method 'getCharacter' of 'panda3d.core.TextGlyph' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE35DE00>)>'
        'getGeom': None, # (!) real value is "<method 'getGeom' of 'panda3d.core.TextGlyph' objects>"
        'getQuad': None, # (!) real value is "<method 'getQuad' of 'panda3d.core.TextGlyph' objects>"
        'getState': None, # (!) real value is "<method 'getState' of 'panda3d.core.TextGlyph' objects>"
        'get_advance': None, # (!) real value is "<method 'get_advance' of 'panda3d.core.TextGlyph' objects>"
        'get_character': None, # (!) real value is "<method 'get_character' of 'panda3d.core.TextGlyph' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE35DE00>)>'
        'get_geom': None, # (!) real value is "<method 'get_geom' of 'panda3d.core.TextGlyph' objects>"
        'get_quad': None, # (!) real value is "<method 'get_quad' of 'panda3d.core.TextGlyph' objects>"
        'get_state': None, # (!) real value is "<method 'get_state' of 'panda3d.core.TextGlyph' objects>"
        'hasQuad': None, # (!) real value is "<method 'hasQuad' of 'panda3d.core.TextGlyph' objects>"
        'has_quad': None, # (!) real value is "<method 'has_quad' of 'panda3d.core.TextGlyph' objects>"
        'isWhitespace': None, # (!) real value is "<method 'isWhitespace' of 'panda3d.core.TextGlyph' objects>"
        'is_whitespace': None, # (!) real value is "<method 'is_whitespace' of 'panda3d.core.TextGlyph' objects>"
        'state': None, # (!) real value is "<attribute 'state' of 'panda3d.core.TextGlyph' objects>"
    }


