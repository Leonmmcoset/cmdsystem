# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class TextProperties(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * This defines the set of visual properties that may be assigned to the
     * individual characters of the text.  (Properties which affect the overall
     * block of text can only be specified on the TextNode directly).
     *
     * Typically, there is just one set of properties on a given block of text,
     * which is set directly on the TextNode (TextNode inherits from
     * TextProperties). That makes all of the text within a particular block have
     * the same appearance.
     *
     * This separate class exists in order to implement multiple different kinds
     * of text appearing within one block.  The text string itself may reference a
     * TextProperties structure by name using the \1 and \2 tokens embedded within
     * the string; each nested TextProperties structure modifies the appearance of
     * subsequent text within the block.
     */
    """
    def addProperties(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_properties(const TextProperties self, const TextProperties other)
        
        /**
         * Sets any properties that are explicitly specified in other on this object.
         * Leaves other properties unchanged.
         */
        """
        pass

    def add_properties(self, const_TextProperties_self, const_TextProperties_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_properties(const TextProperties self, const TextProperties other)
        
        /**
         * Sets any properties that are explicitly specified in other on this object.
         * Leaves other properties unchanged.
         */
        """
        pass

    def assign(self, const_TextProperties_self, const_TextProperties_copy): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        assign(const TextProperties self, const TextProperties copy)
        """
        pass

    def clear(self, const_TextProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear(const TextProperties self)
        
        /**
         * Unsets all properties that have been specified so far, and resets the
         * TextProperties structure to its initial empty state.
         */
        """
        pass

    def clearAlign(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_align(const TextProperties self)
        
        /**
         * Restores the default alignment of the text.
         */
        """
        pass

    def clearBin(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_bin(const TextProperties self)
        
        /**
         * Removes the effect of a previous call to set_bin().  Text will be drawn in
         * whatever bin it would like to be drawn in, with no explicit ordering.
         */
        """
        pass

    def clearDirection(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_direction(const TextProperties self)
        
        /**
         * Clears the text direction setting.  If no text direction is specified, it
         * will be guessed based on the contents of the string.
         *
         * @since 1.10.0
         */
        """
        pass

    def clearDrawOrder(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_draw_order(const TextProperties self)
        
        /**
         *
         */
        """
        pass

    def clearFont(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_font(const TextProperties self)
        
        /**
         * Restores the default font to the text.
         */
        """
        pass

    def clearGlyphScale(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_glyph_scale(const TextProperties self)
        
        /**
         *
         */
        """
        pass

    def clearGlyphShift(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_glyph_shift(const TextProperties self)
        
        /**
         *
         */
        """
        pass

    def clearIndent(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_indent(const TextProperties self)
        
        /**
         * Removes the indent setting from the text.  Text will be as wide as it is.
         */
        """
        pass

    def clearPreserveTrailingWhitespace(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_preserve_trailing_whitespace(const TextProperties self)
        
        /**
         *
         */
        """
        pass

    def clearShadow(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_shadow(const TextProperties self)
        
        /**
         * Specifies that a shadow will not be drawn behind the text.
         */
        """
        pass

    def clearShadowColor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_shadow_color(const TextProperties self)
        
        /**
         * Removes the shadow color specification.
         */
        """
        pass

    def clearSlant(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_slant(const TextProperties self)
        
        /**
         *
         */
        """
        pass

    def clearSmallCaps(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_small_caps(const TextProperties self)
        
        /**
         *
         */
        """
        pass

    def clearSmallCapsScale(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_small_caps_scale(const TextProperties self)
        
        /**
         *
         */
        """
        pass

    def clearTabWidth(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_tab_width(const TextProperties self)
        
        /**
         *
         */
        """
        pass

    def clearTextColor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_text_color(const TextProperties self)
        
        /**
         * Removes the text color specification; the text will be colored whatever it
         * was in the source font file.
         */
        """
        pass

    def clearTextScale(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_text_scale(const TextProperties self)
        
        /**
         *
         */
        """
        pass

    def clearUnderscore(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_underscore(const TextProperties self)
        
        /**
         *
         */
        """
        pass

    def clearUnderscoreHeight(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_underscore_height(const TextProperties self)
        
        /**
         *
         */
        """
        pass

    def clearWordwrap(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_wordwrap(const TextProperties self)
        
        /**
         * Removes the wordwrap setting from the text.  Text will be as wide as it is.
         */
        """
        pass

    def clear_align(self, const_TextProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_align(const TextProperties self)
        
        /**
         * Restores the default alignment of the text.
         */
        """
        pass

    def clear_bin(self, const_TextProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_bin(const TextProperties self)
        
        /**
         * Removes the effect of a previous call to set_bin().  Text will be drawn in
         * whatever bin it would like to be drawn in, with no explicit ordering.
         */
        """
        pass

    def clear_direction(self, const_TextProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_direction(const TextProperties self)
        
        /**
         * Clears the text direction setting.  If no text direction is specified, it
         * will be guessed based on the contents of the string.
         *
         * @since 1.10.0
         */
        """
        pass

    def clear_draw_order(self, const_TextProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_draw_order(const TextProperties self)
        
        /**
         *
         */
        """
        pass

    def clear_font(self, const_TextProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_font(const TextProperties self)
        
        /**
         * Restores the default font to the text.
         */
        """
        pass

    def clear_glyph_scale(self, const_TextProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_glyph_scale(const TextProperties self)
        
        /**
         *
         */
        """
        pass

    def clear_glyph_shift(self, const_TextProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_glyph_shift(const TextProperties self)
        
        /**
         *
         */
        """
        pass

    def clear_indent(self, const_TextProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_indent(const TextProperties self)
        
        /**
         * Removes the indent setting from the text.  Text will be as wide as it is.
         */
        """
        pass

    def clear_preserve_trailing_whitespace(self, const_TextProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_preserve_trailing_whitespace(const TextProperties self)
        
        /**
         *
         */
        """
        pass

    def clear_shadow(self, const_TextProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_shadow(const TextProperties self)
        
        /**
         * Specifies that a shadow will not be drawn behind the text.
         */
        """
        pass

    def clear_shadow_color(self, const_TextProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_shadow_color(const TextProperties self)
        
        /**
         * Removes the shadow color specification.
         */
        """
        pass

    def clear_slant(self, const_TextProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_slant(const TextProperties self)
        
        /**
         *
         */
        """
        pass

    def clear_small_caps(self, const_TextProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_small_caps(const TextProperties self)
        
        /**
         *
         */
        """
        pass

    def clear_small_caps_scale(self, const_TextProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_small_caps_scale(const TextProperties self)
        
        /**
         *
         */
        """
        pass

    def clear_tab_width(self, const_TextProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_tab_width(const TextProperties self)
        
        /**
         *
         */
        """
        pass

    def clear_text_color(self, const_TextProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_text_color(const TextProperties self)
        
        /**
         * Removes the text color specification; the text will be colored whatever it
         * was in the source font file.
         */
        """
        pass

    def clear_text_scale(self, const_TextProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_text_scale(const TextProperties self)
        
        /**
         *
         */
        """
        pass

    def clear_underscore(self, const_TextProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_underscore(const TextProperties self)
        
        /**
         *
         */
        """
        pass

    def clear_underscore_height(self, const_TextProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_underscore_height(const TextProperties self)
        
        /**
         *
         */
        """
        pass

    def clear_wordwrap(self, const_TextProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_wordwrap(const TextProperties self)
        
        /**
         * Removes the wordwrap setting from the text.  Text will be as wide as it is.
         */
        """
        pass

    def getAlign(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_align(TextProperties self)
        
        /**
         *
         */
        """
        pass

    def getBin(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_bin(TextProperties self)
        
        /**
         * Returns the drawing bin set with set_bin(), or empty string if no bin has
         * been set.
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getDefaultFont(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_default_font()
        
        /**
         * Specifies the default font to be used for any TextNode whose font is
         * uninitialized or NULL.  See set_font().
         */
        """
        pass

    def getDirection(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_direction(TextProperties self)
        
        /**
         * Returns the direction of the text as specified by set_direction().
         *
         * @since 1.10.0
         */
        """
        pass

    def getDrawOrder(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_draw_order(TextProperties self)
        
        /**
         * Returns the drawing order set with set_draw_order().
         */
        """
        pass

    def getFont(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_font(TextProperties self)
        
        /**
         * Returns the font currently in use, if any.  If no font is in use, this
         * returns the default font.
         */
        """
        pass

    def getGlyphScale(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_glyph_scale(TextProperties self)
        
        /**
         * Returns the scale factor of each letter as specified by set_glyph_scale().
         */
        """
        pass

    def getGlyphShift(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_glyph_shift(TextProperties self)
        
        /**
         * Returns the vertical shift of each letter as specified by
         * set_glyph_shift().
         */
        """
        pass

    def getIndent(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_indent(TextProperties self)
        
        /**
         *
         */
        """
        pass

    def getPreserveTrailingWhitespace(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_preserve_trailing_whitespace(TextProperties self)
        
        /**
         * Returns the preserve_trailing_whitespace flag.  See
         * set_preserve_trailing_whitespace().
         */
        """
        pass

    def getShadow(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_shadow(TextProperties self)
        
        /**
         * Returns the offset of the shadow as set by set_shadow().  It is an error to
         * call this if has_shadow() is false.
         */
        """
        pass

    def getShadowColor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_shadow_color(TextProperties self)
        
        /**
         *
         */
        """
        pass

    def getSlant(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_slant(TextProperties self)
        
        /**
         * Returns the factor by which the text is specified to slant to the right.
         */
        """
        pass

    def getSmallCaps(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_small_caps(TextProperties self)
        
        /**
         * Returns the small_caps flag.  See set_small_caps().
         */
        """
        pass

    def getSmallCapsScale(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_small_caps_scale(TextProperties self)
        
        /**
         * Returns the scale factor applied to lowercase letters from their uppercase
         * equivalents, when the small_caps flag is in effect.  See set_small_caps()
         * and set_small_caps_scale().
         */
        """
        pass

    def getTabWidth(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_tab_width(TextProperties self)
        
        /**
         * Returns the width set via set_tab_width().
         */
        """
        pass

    def getTextColor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_text_color(TextProperties self)
        
        /**
         *
         */
        """
        pass

    def getTextScale(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_text_scale(TextProperties self)
        
        /**
         * Returns the scale factor of the text as specified by set_text_scale().
         */
        """
        pass

    def getUnderscore(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_underscore(TextProperties self)
        
        /**
         * Returns the underscore flag.  See set_underscore().
         */
        """
        pass

    def getUnderscoreHeight(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_underscore_height(TextProperties self)
        
        /**
         * Returns the vertical height of the underscore; see set_underscore_height().
         */
        """
        pass

    def getWordwrap(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_wordwrap(TextProperties self)
        
        /**
         *
         */
        """
        pass

    def get_align(self, TextProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_align(TextProperties self)
        
        /**
         *
         */
        """
        pass

    def get_bin(self, TextProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_bin(TextProperties self)
        
        /**
         * Returns the drawing bin set with set_bin(), or empty string if no bin has
         * been set.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_default_font(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_default_font()
        
        /**
         * Specifies the default font to be used for any TextNode whose font is
         * uninitialized or NULL.  See set_font().
         */
        """
        pass

    def get_direction(self, TextProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_direction(TextProperties self)
        
        /**
         * Returns the direction of the text as specified by set_direction().
         *
         * @since 1.10.0
         */
        """
        pass

    def get_draw_order(self, TextProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_draw_order(TextProperties self)
        
        /**
         * Returns the drawing order set with set_draw_order().
         */
        """
        pass

    def get_font(self, TextProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_font(TextProperties self)
        
        /**
         * Returns the font currently in use, if any.  If no font is in use, this
         * returns the default font.
         */
        """
        pass

    def get_glyph_scale(self, TextProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_glyph_scale(TextProperties self)
        
        /**
         * Returns the scale factor of each letter as specified by set_glyph_scale().
         */
        """
        pass

    def get_glyph_shift(self, TextProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_glyph_shift(TextProperties self)
        
        /**
         * Returns the vertical shift of each letter as specified by
         * set_glyph_shift().
         */
        """
        pass

    def get_indent(self, TextProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_indent(TextProperties self)
        
        /**
         *
         */
        """
        pass

    def get_preserve_trailing_whitespace(self, TextProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_preserve_trailing_whitespace(TextProperties self)
        
        /**
         * Returns the preserve_trailing_whitespace flag.  See
         * set_preserve_trailing_whitespace().
         */
        """
        pass

    def get_shadow(self, TextProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_shadow(TextProperties self)
        
        /**
         * Returns the offset of the shadow as set by set_shadow().  It is an error to
         * call this if has_shadow() is false.
         */
        """
        pass

    def get_shadow_color(self, TextProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_shadow_color(TextProperties self)
        
        /**
         *
         */
        """
        pass

    def get_slant(self, TextProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_slant(TextProperties self)
        
        /**
         * Returns the factor by which the text is specified to slant to the right.
         */
        """
        pass

    def get_small_caps(self, TextProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_small_caps(TextProperties self)
        
        /**
         * Returns the small_caps flag.  See set_small_caps().
         */
        """
        pass

    def get_small_caps_scale(self, TextProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_small_caps_scale(TextProperties self)
        
        /**
         * Returns the scale factor applied to lowercase letters from their uppercase
         * equivalents, when the small_caps flag is in effect.  See set_small_caps()
         * and set_small_caps_scale().
         */
        """
        pass

    def get_tab_width(self, TextProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_tab_width(TextProperties self)
        
        /**
         * Returns the width set via set_tab_width().
         */
        """
        pass

    def get_text_color(self, TextProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_text_color(TextProperties self)
        
        /**
         *
         */
        """
        pass

    def get_text_scale(self, TextProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_text_scale(TextProperties self)
        
        /**
         * Returns the scale factor of the text as specified by set_text_scale().
         */
        """
        pass

    def get_underscore(self, TextProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_underscore(TextProperties self)
        
        /**
         * Returns the underscore flag.  See set_underscore().
         */
        """
        pass

    def get_underscore_height(self, TextProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_underscore_height(TextProperties self)
        
        /**
         * Returns the vertical height of the underscore; see set_underscore_height().
         */
        """
        pass

    def get_wordwrap(self, TextProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_wordwrap(TextProperties self)
        
        /**
         *
         */
        """
        pass

    def hasAlign(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_align(TextProperties self)
        
        /**
         *
         */
        """
        pass

    def hasBin(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_bin(TextProperties self)
        
        /**
         * Returns true if an explicit drawing bin has been set via set_bin(), false
         * otherwise.
         */
        """
        pass

    def hasDirection(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_direction(TextProperties self)
        
        /**
         * @since 1.10.0
         */
        """
        pass

    def hasDrawOrder(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_draw_order(TextProperties self)
        
        /**
         *
         */
        """
        pass

    def hasFont(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_font(TextProperties self)
        
        /**
         *
         */
        """
        pass

    def hasGlyphScale(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_glyph_scale(TextProperties self)
        
        /**
         *
         */
        """
        pass

    def hasGlyphShift(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_glyph_shift(TextProperties self)
        
        /**
         *
         */
        """
        pass

    def hasIndent(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_indent(TextProperties self)
        
        /**
         *
         */
        """
        pass

    def hasPreserveTrailingWhitespace(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_preserve_trailing_whitespace(TextProperties self)
        
        /**
         *
         */
        """
        pass

    def hasShadow(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_shadow(TextProperties self)
        
        /**
         *
         */
        """
        pass

    def hasShadowColor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_shadow_color(TextProperties self)
        
        /**
         *
         */
        """
        pass

    def hasSlant(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_slant(TextProperties self)
        
        /**
         *
         */
        """
        pass

    def hasSmallCaps(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_small_caps(TextProperties self)
        
        /**
         *
         */
        """
        pass

    def hasSmallCapsScale(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_small_caps_scale(TextProperties self)
        
        /**
         *
         */
        """
        pass

    def hasTabWidth(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_tab_width(TextProperties self)
        
        /**
         *
         */
        """
        pass

    def hasTextColor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_text_color(TextProperties self)
        
        /**
         *
         */
        """
        pass

    def hasTextScale(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_text_scale(TextProperties self)
        
        /**
         *
         */
        """
        pass

    def hasUnderscore(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_underscore(TextProperties self)
        
        /**
         *
         */
        """
        pass

    def hasUnderscoreHeight(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_underscore_height(TextProperties self)
        
        /**
         *
         */
        """
        pass

    def hasWordwrap(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_wordwrap(TextProperties self)
        
        /**
         *
         */
        """
        pass

    def has_align(self, TextProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_align(TextProperties self)
        
        /**
         *
         */
        """
        pass

    def has_bin(self, TextProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_bin(TextProperties self)
        
        /**
         * Returns true if an explicit drawing bin has been set via set_bin(), false
         * otherwise.
         */
        """
        pass

    def has_direction(self, TextProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_direction(TextProperties self)
        
        /**
         * @since 1.10.0
         */
        """
        pass

    def has_draw_order(self, TextProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_draw_order(TextProperties self)
        
        /**
         *
         */
        """
        pass

    def has_font(self, TextProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_font(TextProperties self)
        
        /**
         *
         */
        """
        pass

    def has_glyph_scale(self, TextProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_glyph_scale(TextProperties self)
        
        /**
         *
         */
        """
        pass

    def has_glyph_shift(self, TextProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_glyph_shift(TextProperties self)
        
        /**
         *
         */
        """
        pass

    def has_indent(self, TextProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_indent(TextProperties self)
        
        /**
         *
         */
        """
        pass

    def has_preserve_trailing_whitespace(self, TextProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_preserve_trailing_whitespace(TextProperties self)
        
        /**
         *
         */
        """
        pass

    def has_shadow(self, TextProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_shadow(TextProperties self)
        
        /**
         *
         */
        """
        pass

    def has_shadow_color(self, TextProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_shadow_color(TextProperties self)
        
        /**
         *
         */
        """
        pass

    def has_slant(self, TextProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_slant(TextProperties self)
        
        /**
         *
         */
        """
        pass

    def has_small_caps(self, TextProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_small_caps(TextProperties self)
        
        /**
         *
         */
        """
        pass

    def has_small_caps_scale(self, TextProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_small_caps_scale(TextProperties self)
        
        /**
         *
         */
        """
        pass

    def has_tab_width(self, TextProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_tab_width(TextProperties self)
        
        /**
         *
         */
        """
        pass

    def has_text_color(self, TextProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_text_color(TextProperties self)
        
        /**
         *
         */
        """
        pass

    def has_text_scale(self, TextProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_text_scale(TextProperties self)
        
        /**
         *
         */
        """
        pass

    def has_underscore(self, TextProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_underscore(TextProperties self)
        
        /**
         *
         */
        """
        pass

    def has_underscore_height(self, TextProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_underscore_height(TextProperties self)
        
        /**
         *
         */
        """
        pass

    def has_wordwrap(self, TextProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_wordwrap(TextProperties self)
        
        /**
         *
         */
        """
        pass

    def isAnySpecified(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_any_specified(TextProperties self)
        
        /**
         * Returns true if any properties have been specified, false otherwise.
         */
        """
        pass

    def is_any_specified(self, TextProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_any_specified(TextProperties self)
        
        /**
         * Returns true if any properties have been specified, false otherwise.
         */
        """
        pass

    def setAlign(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_align(const TextProperties self, int align_type)
        
        /**
         * Specifies the alignment of the text within its margins.
         */
        """
        pass

    def setBin(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_bin(const TextProperties self, str bin)
        
        /**
         * Names the CullBin that the text geometry should be assigned to.  If this is
         * set, then a CullBinAttrib will be created to explicitly place each
         * component in the named bin.
         *
         * The draw_order value will also be passed to each CullBinAttrib as
         * appropriate; this is particularly useful if this names a CullBinFixed, e.g.
         * "fixed".
         */
        """
        pass

    def setDefaultFont(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_default_font(TextFont param0)
        
        /**
         * Specifies the default font to be used for any TextNode whose font is
         * uninitialized or NULL.  See set_font().
         */
        """
        pass

    def setDirection(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_direction(const TextProperties self, int direction)
        
        /**
         * Specifies the text direction.  If none is specified, it will be guessed
         * based on the contents of the string.
         *
         * @since 1.10.0
         */
        """
        pass

    def setDrawOrder(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_draw_order(const TextProperties self, int draw_order)
        
        /**
         * Sets the drawing order of text created by the TextNode.  This is actually
         * the draw order of the card and frame.  The shadow is drawn at
         * _draw_order+1, and the text at _draw_order+2.
         *
         * This affects the sorting order assigned to the nodes as they are created,
         * and also is passed to whatever bin may be assigned via set_bin().
         *
         * The return value is the first unused draw_order number, e.g.  _draw_order +
         * 3.
         */
        """
        pass

    def setFont(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_font(const TextProperties self, TextFont font)
        
        /**
         * Sets the font that will be used when making text.  If this is set to NULL,
         * the default font will be used, which can be set via set_default_font().
         */
        """
        pass

    def setGlyphScale(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_glyph_scale(const TextProperties self, float glyph_scale)
        
        /**
         * Specifies the factor by which to scale each letter of the text as it is
         * placed, in addition to any scales inherited from the node or from
         * set_text_scale(). This can be used (possibly in conjunction with
         * set_glyph_shift()) to implement superscripting or subscripting.
         *
         * The glyph scale is cumulative when applied to nested TextProperties.  It is
         * intended primarily for implementing superscripts, not for scaling the text
         * in general.  See also set_text_scale(), which is intended primarily for
         * scaling the text in general, and is not cumulative.
         */
        """
        pass

    def setGlyphShift(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_glyph_shift(const TextProperties self, float glyph_shift)
        
        /**
         * Specifies a vertical amount to shift each letter of the text as it is
         * placed.  This can be used (possibly in conjunction with set_glyph_scale())
         * to implement superscripting or subscripting.
         */
        """
        pass

    def setIndent(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_indent(const TextProperties self, float indent)
        
        /**
         * Specifies the amount of extra space that is inserted before the first
         * character of each line.  This can be thought of as a left margin.
         */
        """
        pass

    def setPreserveTrailingWhitespace(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_preserve_trailing_whitespace(const TextProperties self, bool preserve_trailing_whitespace)
        
        /**
         * Sets the preserve_trailing_whitespace flag.  When this is set, trailing
         * whitespace at the end of the line is not stripped when the text is
         * wordwrapped (it is stripped by default).  Since the trailing whitespace is
         * invisible, this is important primarily for determining the proper width of
         * a frame or card behind the text.
         */
        """
        pass

    def setShadow(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_shadow(const TextProperties self, const LVecBase2f shadow_offset)
        set_shadow(const TextProperties self, float xoffset, float yoffset)
        
        /**
         * Specifies that the text should be drawn with a shadow, by creating a second
         * copy of the text and offsetting it slightly behind the first.
         */
        
        /**
         * Specifies that the text should be drawn with a shadow, by creating a second
         * copy of the text and offsetting it slightly behind the first.
         */
        """
        pass

    def setShadowColor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_shadow_color(const TextProperties self, const LVecBase4f shadow_color)
        set_shadow_color(const TextProperties self, float r, float g, float b, float a)
        
        /**
         *
         */
        
        /**
         *
         */
        """
        pass

    def setSlant(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_slant(const TextProperties self, float slant)
        
        /**
         * Specifies the factor by which the text slants to the right.
         */
        """
        pass

    def setSmallCaps(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_small_caps(const TextProperties self, bool small_caps)
        
        /**
         * Sets the small_caps flag.  When this is set, lowercase letters are
         * generated as scaled-down versions of their uppercase equivalents.  This is
         * particularly useful to set for fonts that do not have lowercase letters.
         *
         * It is also a good idea to set this for a (dynamic) font that has already
         * implemented lowercase letters as scaled-down versions of their uppercase
         * equivalents, since without this flag the texture memory may needlessly
         * duplicate equivalent glyphs for upper and lowercase letters.  Setting this
         * flag causes the texture memory to share the mixed-case letters.
         *
         * The amount by which the lowercase letters are scaled is specified by
         * set_small_caps_scale().
         */
        """
        pass

    def setSmallCapsScale(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_small_caps_scale(const TextProperties self, float small_caps_scale)
        
        /**
         * Sets the scale factor applied to lowercase letters from their uppercase
         * equivalents, when the small_caps flag is in effect.  See set_small_caps().
         * Normally, this will be a number less than one.
         */
        """
        pass

    def setTabWidth(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_tab_width(const TextProperties self, float tab_width)
        
        /**
         * Sets the width of each tab stop, in screen units.  A tab character embedded
         * in the text will advance the horizontal position to the next tab stop.
         */
        """
        pass

    def setTextColor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_text_color(const TextProperties self, const LVecBase4f text_color)
        set_text_color(const TextProperties self, float r, float g, float b, float a)
        
        /**
         *
         */
        
        /**
         *
         */
        """
        pass

    def setTextScale(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_text_scale(const TextProperties self, float text_scale)
        
        /**
         * Specifies the factor by which to scale the text, in addition to any
         * scalings imposed by the node, as well as in addition to the glyph scale.
         *
         * The text scale is not cumulative when applied to nested TextProperties.
         * See also set_glyph_scale(), which is cumulative.
         */
        """
        pass

    def setUnderscore(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_underscore(const TextProperties self, bool underscore)
        
        /**
         * Sets the underscore flag.  When this is set, the text is underscored with a
         * one-pixel line the same color as the text foreground, drawn at the
         * baseline.
         */
        """
        pass

    def setUnderscoreHeight(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_underscore_height(const TextProperties self, float underscore_height)
        
        /**
         * Specifies the vertical height of the underscore, relative to the text
         * baseline.  This only has meaning if the underscore mode is enabled with
         * set_underscore().
         */
        """
        pass

    def setWordwrap(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_wordwrap(const TextProperties self, float wordwrap)
        
        /**
         * Sets the text up to automatically wordwrap when it exceeds the indicated
         * width.  This can be thought of as a right margin or margin width.
         */
        """
        pass

    def set_align(self, const_TextProperties_self, int_align_type): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_align(const TextProperties self, int align_type)
        
        /**
         * Specifies the alignment of the text within its margins.
         */
        """
        pass

    def set_bin(self, const_TextProperties_self, str_bin): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_bin(const TextProperties self, str bin)
        
        /**
         * Names the CullBin that the text geometry should be assigned to.  If this is
         * set, then a CullBinAttrib will be created to explicitly place each
         * component in the named bin.
         *
         * The draw_order value will also be passed to each CullBinAttrib as
         * appropriate; this is particularly useful if this names a CullBinFixed, e.g.
         * "fixed".
         */
        """
        pass

    def set_default_font(self, TextFont_param0): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_default_font(TextFont param0)
        
        /**
         * Specifies the default font to be used for any TextNode whose font is
         * uninitialized or NULL.  See set_font().
         */
        """
        pass

    def set_direction(self, const_TextProperties_self, int_direction): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_direction(const TextProperties self, int direction)
        
        /**
         * Specifies the text direction.  If none is specified, it will be guessed
         * based on the contents of the string.
         *
         * @since 1.10.0
         */
        """
        pass

    def set_draw_order(self, const_TextProperties_self, int_draw_order): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_draw_order(const TextProperties self, int draw_order)
        
        /**
         * Sets the drawing order of text created by the TextNode.  This is actually
         * the draw order of the card and frame.  The shadow is drawn at
         * _draw_order+1, and the text at _draw_order+2.
         *
         * This affects the sorting order assigned to the nodes as they are created,
         * and also is passed to whatever bin may be assigned via set_bin().
         *
         * The return value is the first unused draw_order number, e.g.  _draw_order +
         * 3.
         */
        """
        pass

    def set_font(self, const_TextProperties_self, TextFont_font): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_font(const TextProperties self, TextFont font)
        
        /**
         * Sets the font that will be used when making text.  If this is set to NULL,
         * the default font will be used, which can be set via set_default_font().
         */
        """
        pass

    def set_glyph_scale(self, const_TextProperties_self, float_glyph_scale): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_glyph_scale(const TextProperties self, float glyph_scale)
        
        /**
         * Specifies the factor by which to scale each letter of the text as it is
         * placed, in addition to any scales inherited from the node or from
         * set_text_scale(). This can be used (possibly in conjunction with
         * set_glyph_shift()) to implement superscripting or subscripting.
         *
         * The glyph scale is cumulative when applied to nested TextProperties.  It is
         * intended primarily for implementing superscripts, not for scaling the text
         * in general.  See also set_text_scale(), which is intended primarily for
         * scaling the text in general, and is not cumulative.
         */
        """
        pass

    def set_glyph_shift(self, const_TextProperties_self, float_glyph_shift): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_glyph_shift(const TextProperties self, float glyph_shift)
        
        /**
         * Specifies a vertical amount to shift each letter of the text as it is
         * placed.  This can be used (possibly in conjunction with set_glyph_scale())
         * to implement superscripting or subscripting.
         */
        """
        pass

    def set_indent(self, const_TextProperties_self, float_indent): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_indent(const TextProperties self, float indent)
        
        /**
         * Specifies the amount of extra space that is inserted before the first
         * character of each line.  This can be thought of as a left margin.
         */
        """
        pass

    def set_preserve_trailing_whitespace(self, const_TextProperties_self, bool_preserve_trailing_whitespace): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_preserve_trailing_whitespace(const TextProperties self, bool preserve_trailing_whitespace)
        
        /**
         * Sets the preserve_trailing_whitespace flag.  When this is set, trailing
         * whitespace at the end of the line is not stripped when the text is
         * wordwrapped (it is stripped by default).  Since the trailing whitespace is
         * invisible, this is important primarily for determining the proper width of
         * a frame or card behind the text.
         */
        """
        pass

    def set_shadow(self, const_TextProperties_self, const_LVecBase2f_shadow_offset): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_shadow(const TextProperties self, const LVecBase2f shadow_offset)
        set_shadow(const TextProperties self, float xoffset, float yoffset)
        
        /**
         * Specifies that the text should be drawn with a shadow, by creating a second
         * copy of the text and offsetting it slightly behind the first.
         */
        
        /**
         * Specifies that the text should be drawn with a shadow, by creating a second
         * copy of the text and offsetting it slightly behind the first.
         */
        """
        pass

    def set_shadow_color(self, const_TextProperties_self, const_LVecBase4f_shadow_color): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_shadow_color(const TextProperties self, const LVecBase4f shadow_color)
        set_shadow_color(const TextProperties self, float r, float g, float b, float a)
        
        /**
         *
         */
        
        /**
         *
         */
        """
        pass

    def set_slant(self, const_TextProperties_self, float_slant): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_slant(const TextProperties self, float slant)
        
        /**
         * Specifies the factor by which the text slants to the right.
         */
        """
        pass

    def set_small_caps(self, const_TextProperties_self, bool_small_caps): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_small_caps(const TextProperties self, bool small_caps)
        
        /**
         * Sets the small_caps flag.  When this is set, lowercase letters are
         * generated as scaled-down versions of their uppercase equivalents.  This is
         * particularly useful to set for fonts that do not have lowercase letters.
         *
         * It is also a good idea to set this for a (dynamic) font that has already
         * implemented lowercase letters as scaled-down versions of their uppercase
         * equivalents, since without this flag the texture memory may needlessly
         * duplicate equivalent glyphs for upper and lowercase letters.  Setting this
         * flag causes the texture memory to share the mixed-case letters.
         *
         * The amount by which the lowercase letters are scaled is specified by
         * set_small_caps_scale().
         */
        """
        pass

    def set_small_caps_scale(self, const_TextProperties_self, float_small_caps_scale): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_small_caps_scale(const TextProperties self, float small_caps_scale)
        
        /**
         * Sets the scale factor applied to lowercase letters from their uppercase
         * equivalents, when the small_caps flag is in effect.  See set_small_caps().
         * Normally, this will be a number less than one.
         */
        """
        pass

    def set_tab_width(self, const_TextProperties_self, float_tab_width): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_tab_width(const TextProperties self, float tab_width)
        
        /**
         * Sets the width of each tab stop, in screen units.  A tab character embedded
         * in the text will advance the horizontal position to the next tab stop.
         */
        """
        pass

    def set_text_color(self, const_TextProperties_self, const_LVecBase4f_text_color): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_text_color(const TextProperties self, const LVecBase4f text_color)
        set_text_color(const TextProperties self, float r, float g, float b, float a)
        
        /**
         *
         */
        
        /**
         *
         */
        """
        pass

    def set_text_scale(self, const_TextProperties_self, float_text_scale): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_text_scale(const TextProperties self, float text_scale)
        
        /**
         * Specifies the factor by which to scale the text, in addition to any
         * scalings imposed by the node, as well as in addition to the glyph scale.
         *
         * The text scale is not cumulative when applied to nested TextProperties.
         * See also set_glyph_scale(), which is cumulative.
         */
        """
        pass

    def set_underscore(self, const_TextProperties_self, bool_underscore): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_underscore(const TextProperties self, bool underscore)
        
        /**
         * Sets the underscore flag.  When this is set, the text is underscored with a
         * one-pixel line the same color as the text foreground, drawn at the
         * baseline.
         */
        """
        pass

    def set_underscore_height(self, const_TextProperties_self, float_underscore_height): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_underscore_height(const TextProperties self, float underscore_height)
        
        /**
         * Specifies the vertical height of the underscore, relative to the text
         * baseline.  This only has meaning if the underscore mode is enabled with
         * set_underscore().
         */
        """
        pass

    def set_wordwrap(self, const_TextProperties_self, float_wordwrap): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_wordwrap(const TextProperties self, float wordwrap)
        
        /**
         * Sets the text up to automatically wordwrap when it exceeds the indicated
         * width.  This can be thought of as a right margin or margin width.
         */
        """
        pass

    def write(self, TextProperties_self, ostream_out, int_indent_level): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(TextProperties self, ostream out, int indent_level)
        
        /**
         *
         */
        """
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __deepcopy__(self, *args, **kwargs): # real signature unknown
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    align = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    bin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    direction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    draw_order = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    font = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glyph_scale = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glyph_shift = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    indent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    preserve_trailing_whitespace = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    shadow = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    shadow_color = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    slant = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    small_caps = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    small_caps_scale = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tab_width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    text_color = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    text_scale = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    underscore = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    underscore_height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    wordwrap = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    ABoxedCenter = 5
    ABoxedLeft = 3
    ABoxedRight = 4
    ACenter = 2
    ALeft = 0
    ARight = 1
    A_boxed_center = 5
    A_boxed_left = 3
    A_boxed_right = 4
    A_center = 2
    A_left = 0
    A_right = 1
    DLtr = 0
    DRtl = 1
    DtoolClassDict = {
        'ABoxedCenter': 5,
        'ABoxedLeft': 3,
        'ABoxedRight': 4,
        'ACenter': 2,
        'ALeft': 0,
        'ARight': 1,
        'A_boxed_center': 5,
        'A_boxed_left': 3,
        'A_boxed_right': 4,
        'A_center': 2,
        'A_left': 0,
        'A_right': 1,
        'DLtr': 0,
        'DRtl': 1,
        'D_ltr': 0,
        'D_rtl': 1,
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.TextProperties' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.TextProperties' objects>"
        '__doc__': '/**\n * This defines the set of visual properties that may be assigned to the\n * individual characters of the text.  (Properties which affect the overall\n * block of text can only be specified on the TextNode directly).\n *\n * Typically, there is just one set of properties on a given block of text,\n * which is set directly on the TextNode (TextNode inherits from\n * TextProperties). That makes all of the text within a particular block have\n * the same appearance.\n *\n * This separate class exists in order to implement multiple different kinds\n * of text appearing within one block.  The text string itself may reference a\n * TextProperties structure by name using the \\1 and \\2 tokens embedded within\n * the string; each nested TextProperties structure modifies the appearance of\n * subsequent text within the block.\n */',
        '__eq__': None, # (!) real value is "<slot wrapper '__eq__' of 'panda3d.core.TextProperties' objects>"
        '__ge__': None, # (!) real value is "<slot wrapper '__ge__' of 'panda3d.core.TextProperties' objects>"
        '__gt__': None, # (!) real value is "<slot wrapper '__gt__' of 'panda3d.core.TextProperties' objects>"
        '__hash__': None, # (!) real value is "<slot wrapper '__hash__' of 'panda3d.core.TextProperties' objects>"
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.TextProperties' objects>"
        '__le__': None, # (!) real value is "<slot wrapper '__le__' of 'panda3d.core.TextProperties' objects>"
        '__lt__': None, # (!) real value is "<slot wrapper '__lt__' of 'panda3d.core.TextProperties' objects>"
        '__ne__': None, # (!) real value is "<slot wrapper '__ne__' of 'panda3d.core.TextProperties' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE35EC90>'
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.TextProperties' objects>"
        'addProperties': None, # (!) real value is "<method 'addProperties' of 'panda3d.core.TextProperties' objects>"
        'add_properties': None, # (!) real value is "<method 'add_properties' of 'panda3d.core.TextProperties' objects>"
        'align': None, # (!) real value is "<attribute 'align' of 'panda3d.core.TextProperties' objects>"
        'assign': None, # (!) real value is "<method 'assign' of 'panda3d.core.TextProperties' objects>"
        'bin': None, # (!) real value is "<attribute 'bin' of 'panda3d.core.TextProperties' objects>"
        'clear': None, # (!) real value is "<method 'clear' of 'panda3d.core.TextProperties' objects>"
        'clearAlign': None, # (!) real value is "<method 'clearAlign' of 'panda3d.core.TextProperties' objects>"
        'clearBin': None, # (!) real value is "<method 'clearBin' of 'panda3d.core.TextProperties' objects>"
        'clearDirection': None, # (!) real value is "<method 'clearDirection' of 'panda3d.core.TextProperties' objects>"
        'clearDrawOrder': None, # (!) real value is "<method 'clearDrawOrder' of 'panda3d.core.TextProperties' objects>"
        'clearFont': None, # (!) real value is "<method 'clearFont' of 'panda3d.core.TextProperties' objects>"
        'clearGlyphScale': None, # (!) real value is "<method 'clearGlyphScale' of 'panda3d.core.TextProperties' objects>"
        'clearGlyphShift': None, # (!) real value is "<method 'clearGlyphShift' of 'panda3d.core.TextProperties' objects>"
        'clearIndent': None, # (!) real value is "<method 'clearIndent' of 'panda3d.core.TextProperties' objects>"
        'clearPreserveTrailingWhitespace': None, # (!) real value is "<method 'clearPreserveTrailingWhitespace' of 'panda3d.core.TextProperties' objects>"
        'clearShadow': None, # (!) real value is "<method 'clearShadow' of 'panda3d.core.TextProperties' objects>"
        'clearShadowColor': None, # (!) real value is "<method 'clearShadowColor' of 'panda3d.core.TextProperties' objects>"
        'clearSlant': None, # (!) real value is "<method 'clearSlant' of 'panda3d.core.TextProperties' objects>"
        'clearSmallCaps': None, # (!) real value is "<method 'clearSmallCaps' of 'panda3d.core.TextProperties' objects>"
        'clearSmallCapsScale': None, # (!) real value is "<method 'clearSmallCapsScale' of 'panda3d.core.TextProperties' objects>"
        'clearTabWidth': None, # (!) real value is "<method 'clearTabWidth' of 'panda3d.core.TextProperties' objects>"
        'clearTextColor': None, # (!) real value is "<method 'clearTextColor' of 'panda3d.core.TextProperties' objects>"
        'clearTextScale': None, # (!) real value is "<method 'clearTextScale' of 'panda3d.core.TextProperties' objects>"
        'clearUnderscore': None, # (!) real value is "<method 'clearUnderscore' of 'panda3d.core.TextProperties' objects>"
        'clearUnderscoreHeight': None, # (!) real value is "<method 'clearUnderscoreHeight' of 'panda3d.core.TextProperties' objects>"
        'clearWordwrap': None, # (!) real value is "<method 'clearWordwrap' of 'panda3d.core.TextProperties' objects>"
        'clear_align': None, # (!) real value is "<method 'clear_align' of 'panda3d.core.TextProperties' objects>"
        'clear_bin': None, # (!) real value is "<method 'clear_bin' of 'panda3d.core.TextProperties' objects>"
        'clear_direction': None, # (!) real value is "<method 'clear_direction' of 'panda3d.core.TextProperties' objects>"
        'clear_draw_order': None, # (!) real value is "<method 'clear_draw_order' of 'panda3d.core.TextProperties' objects>"
        'clear_font': None, # (!) real value is "<method 'clear_font' of 'panda3d.core.TextProperties' objects>"
        'clear_glyph_scale': None, # (!) real value is "<method 'clear_glyph_scale' of 'panda3d.core.TextProperties' objects>"
        'clear_glyph_shift': None, # (!) real value is "<method 'clear_glyph_shift' of 'panda3d.core.TextProperties' objects>"
        'clear_indent': None, # (!) real value is "<method 'clear_indent' of 'panda3d.core.TextProperties' objects>"
        'clear_preserve_trailing_whitespace': None, # (!) real value is "<method 'clear_preserve_trailing_whitespace' of 'panda3d.core.TextProperties' objects>"
        'clear_shadow': None, # (!) real value is "<method 'clear_shadow' of 'panda3d.core.TextProperties' objects>"
        'clear_shadow_color': None, # (!) real value is "<method 'clear_shadow_color' of 'panda3d.core.TextProperties' objects>"
        'clear_slant': None, # (!) real value is "<method 'clear_slant' of 'panda3d.core.TextProperties' objects>"
        'clear_small_caps': None, # (!) real value is "<method 'clear_small_caps' of 'panda3d.core.TextProperties' objects>"
        'clear_small_caps_scale': None, # (!) real value is "<method 'clear_small_caps_scale' of 'panda3d.core.TextProperties' objects>"
        'clear_tab_width': None, # (!) real value is "<method 'clear_tab_width' of 'panda3d.core.TextProperties' objects>"
        'clear_text_color': None, # (!) real value is "<method 'clear_text_color' of 'panda3d.core.TextProperties' objects>"
        'clear_text_scale': None, # (!) real value is "<method 'clear_text_scale' of 'panda3d.core.TextProperties' objects>"
        'clear_underscore': None, # (!) real value is "<method 'clear_underscore' of 'panda3d.core.TextProperties' objects>"
        'clear_underscore_height': None, # (!) real value is "<method 'clear_underscore_height' of 'panda3d.core.TextProperties' objects>"
        'clear_wordwrap': None, # (!) real value is "<method 'clear_wordwrap' of 'panda3d.core.TextProperties' objects>"
        'direction': None, # (!) real value is "<attribute 'direction' of 'panda3d.core.TextProperties' objects>"
        'draw_order': None, # (!) real value is "<attribute 'draw_order' of 'panda3d.core.TextProperties' objects>"
        'font': None, # (!) real value is "<attribute 'font' of 'panda3d.core.TextProperties' objects>"
        'getAlign': None, # (!) real value is "<method 'getAlign' of 'panda3d.core.TextProperties' objects>"
        'getBin': None, # (!) real value is "<method 'getBin' of 'panda3d.core.TextProperties' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE35EC90>)>'
        'getDefaultFont': None, # (!) real value is '<staticmethod(<built-in method getDefaultFont of type object at 0x00007FFCFE35EC90>)>'
        'getDirection': None, # (!) real value is "<method 'getDirection' of 'panda3d.core.TextProperties' objects>"
        'getDrawOrder': None, # (!) real value is "<method 'getDrawOrder' of 'panda3d.core.TextProperties' objects>"
        'getFont': None, # (!) real value is "<method 'getFont' of 'panda3d.core.TextProperties' objects>"
        'getGlyphScale': None, # (!) real value is "<method 'getGlyphScale' of 'panda3d.core.TextProperties' objects>"
        'getGlyphShift': None, # (!) real value is "<method 'getGlyphShift' of 'panda3d.core.TextProperties' objects>"
        'getIndent': None, # (!) real value is "<method 'getIndent' of 'panda3d.core.TextProperties' objects>"
        'getPreserveTrailingWhitespace': None, # (!) real value is "<method 'getPreserveTrailingWhitespace' of 'panda3d.core.TextProperties' objects>"
        'getShadow': None, # (!) real value is "<method 'getShadow' of 'panda3d.core.TextProperties' objects>"
        'getShadowColor': None, # (!) real value is "<method 'getShadowColor' of 'panda3d.core.TextProperties' objects>"
        'getSlant': None, # (!) real value is "<method 'getSlant' of 'panda3d.core.TextProperties' objects>"
        'getSmallCaps': None, # (!) real value is "<method 'getSmallCaps' of 'panda3d.core.TextProperties' objects>"
        'getSmallCapsScale': None, # (!) real value is "<method 'getSmallCapsScale' of 'panda3d.core.TextProperties' objects>"
        'getTabWidth': None, # (!) real value is "<method 'getTabWidth' of 'panda3d.core.TextProperties' objects>"
        'getTextColor': None, # (!) real value is "<method 'getTextColor' of 'panda3d.core.TextProperties' objects>"
        'getTextScale': None, # (!) real value is "<method 'getTextScale' of 'panda3d.core.TextProperties' objects>"
        'getUnderscore': None, # (!) real value is "<method 'getUnderscore' of 'panda3d.core.TextProperties' objects>"
        'getUnderscoreHeight': None, # (!) real value is "<method 'getUnderscoreHeight' of 'panda3d.core.TextProperties' objects>"
        'getWordwrap': None, # (!) real value is "<method 'getWordwrap' of 'panda3d.core.TextProperties' objects>"
        'get_align': None, # (!) real value is "<method 'get_align' of 'panda3d.core.TextProperties' objects>"
        'get_bin': None, # (!) real value is "<method 'get_bin' of 'panda3d.core.TextProperties' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE35EC90>)>'
        'get_default_font': None, # (!) real value is '<staticmethod(<built-in method get_default_font of type object at 0x00007FFCFE35EC90>)>'
        'get_direction': None, # (!) real value is "<method 'get_direction' of 'panda3d.core.TextProperties' objects>"
        'get_draw_order': None, # (!) real value is "<method 'get_draw_order' of 'panda3d.core.TextProperties' objects>"
        'get_font': None, # (!) real value is "<method 'get_font' of 'panda3d.core.TextProperties' objects>"
        'get_glyph_scale': None, # (!) real value is "<method 'get_glyph_scale' of 'panda3d.core.TextProperties' objects>"
        'get_glyph_shift': None, # (!) real value is "<method 'get_glyph_shift' of 'panda3d.core.TextProperties' objects>"
        'get_indent': None, # (!) real value is "<method 'get_indent' of 'panda3d.core.TextProperties' objects>"
        'get_preserve_trailing_whitespace': None, # (!) real value is "<method 'get_preserve_trailing_whitespace' of 'panda3d.core.TextProperties' objects>"
        'get_shadow': None, # (!) real value is "<method 'get_shadow' of 'panda3d.core.TextProperties' objects>"
        'get_shadow_color': None, # (!) real value is "<method 'get_shadow_color' of 'panda3d.core.TextProperties' objects>"
        'get_slant': None, # (!) real value is "<method 'get_slant' of 'panda3d.core.TextProperties' objects>"
        'get_small_caps': None, # (!) real value is "<method 'get_small_caps' of 'panda3d.core.TextProperties' objects>"
        'get_small_caps_scale': None, # (!) real value is "<method 'get_small_caps_scale' of 'panda3d.core.TextProperties' objects>"
        'get_tab_width': None, # (!) real value is "<method 'get_tab_width' of 'panda3d.core.TextProperties' objects>"
        'get_text_color': None, # (!) real value is "<method 'get_text_color' of 'panda3d.core.TextProperties' objects>"
        'get_text_scale': None, # (!) real value is "<method 'get_text_scale' of 'panda3d.core.TextProperties' objects>"
        'get_underscore': None, # (!) real value is "<method 'get_underscore' of 'panda3d.core.TextProperties' objects>"
        'get_underscore_height': None, # (!) real value is "<method 'get_underscore_height' of 'panda3d.core.TextProperties' objects>"
        'get_wordwrap': None, # (!) real value is "<method 'get_wordwrap' of 'panda3d.core.TextProperties' objects>"
        'glyph_scale': None, # (!) real value is "<attribute 'glyph_scale' of 'panda3d.core.TextProperties' objects>"
        'glyph_shift': None, # (!) real value is "<attribute 'glyph_shift' of 'panda3d.core.TextProperties' objects>"
        'hasAlign': None, # (!) real value is "<method 'hasAlign' of 'panda3d.core.TextProperties' objects>"
        'hasBin': None, # (!) real value is "<method 'hasBin' of 'panda3d.core.TextProperties' objects>"
        'hasDirection': None, # (!) real value is "<method 'hasDirection' of 'panda3d.core.TextProperties' objects>"
        'hasDrawOrder': None, # (!) real value is "<method 'hasDrawOrder' of 'panda3d.core.TextProperties' objects>"
        'hasFont': None, # (!) real value is "<method 'hasFont' of 'panda3d.core.TextProperties' objects>"
        'hasGlyphScale': None, # (!) real value is "<method 'hasGlyphScale' of 'panda3d.core.TextProperties' objects>"
        'hasGlyphShift': None, # (!) real value is "<method 'hasGlyphShift' of 'panda3d.core.TextProperties' objects>"
        'hasIndent': None, # (!) real value is "<method 'hasIndent' of 'panda3d.core.TextProperties' objects>"
        'hasPreserveTrailingWhitespace': None, # (!) real value is "<method 'hasPreserveTrailingWhitespace' of 'panda3d.core.TextProperties' objects>"
        'hasShadow': None, # (!) real value is "<method 'hasShadow' of 'panda3d.core.TextProperties' objects>"
        'hasShadowColor': None, # (!) real value is "<method 'hasShadowColor' of 'panda3d.core.TextProperties' objects>"
        'hasSlant': None, # (!) real value is "<method 'hasSlant' of 'panda3d.core.TextProperties' objects>"
        'hasSmallCaps': None, # (!) real value is "<method 'hasSmallCaps' of 'panda3d.core.TextProperties' objects>"
        'hasSmallCapsScale': None, # (!) real value is "<method 'hasSmallCapsScale' of 'panda3d.core.TextProperties' objects>"
        'hasTabWidth': None, # (!) real value is "<method 'hasTabWidth' of 'panda3d.core.TextProperties' objects>"
        'hasTextColor': None, # (!) real value is "<method 'hasTextColor' of 'panda3d.core.TextProperties' objects>"
        'hasTextScale': None, # (!) real value is "<method 'hasTextScale' of 'panda3d.core.TextProperties' objects>"
        'hasUnderscore': None, # (!) real value is "<method 'hasUnderscore' of 'panda3d.core.TextProperties' objects>"
        'hasUnderscoreHeight': None, # (!) real value is "<method 'hasUnderscoreHeight' of 'panda3d.core.TextProperties' objects>"
        'hasWordwrap': None, # (!) real value is "<method 'hasWordwrap' of 'panda3d.core.TextProperties' objects>"
        'has_align': None, # (!) real value is "<method 'has_align' of 'panda3d.core.TextProperties' objects>"
        'has_bin': None, # (!) real value is "<method 'has_bin' of 'panda3d.core.TextProperties' objects>"
        'has_direction': None, # (!) real value is "<method 'has_direction' of 'panda3d.core.TextProperties' objects>"
        'has_draw_order': None, # (!) real value is "<method 'has_draw_order' of 'panda3d.core.TextProperties' objects>"
        'has_font': None, # (!) real value is "<method 'has_font' of 'panda3d.core.TextProperties' objects>"
        'has_glyph_scale': None, # (!) real value is "<method 'has_glyph_scale' of 'panda3d.core.TextProperties' objects>"
        'has_glyph_shift': None, # (!) real value is "<method 'has_glyph_shift' of 'panda3d.core.TextProperties' objects>"
        'has_indent': None, # (!) real value is "<method 'has_indent' of 'panda3d.core.TextProperties' objects>"
        'has_preserve_trailing_whitespace': None, # (!) real value is "<method 'has_preserve_trailing_whitespace' of 'panda3d.core.TextProperties' objects>"
        'has_shadow': None, # (!) real value is "<method 'has_shadow' of 'panda3d.core.TextProperties' objects>"
        'has_shadow_color': None, # (!) real value is "<method 'has_shadow_color' of 'panda3d.core.TextProperties' objects>"
        'has_slant': None, # (!) real value is "<method 'has_slant' of 'panda3d.core.TextProperties' objects>"
        'has_small_caps': None, # (!) real value is "<method 'has_small_caps' of 'panda3d.core.TextProperties' objects>"
        'has_small_caps_scale': None, # (!) real value is "<method 'has_small_caps_scale' of 'panda3d.core.TextProperties' objects>"
        'has_tab_width': None, # (!) real value is "<method 'has_tab_width' of 'panda3d.core.TextProperties' objects>"
        'has_text_color': None, # (!) real value is "<method 'has_text_color' of 'panda3d.core.TextProperties' objects>"
        'has_text_scale': None, # (!) real value is "<method 'has_text_scale' of 'panda3d.core.TextProperties' objects>"
        'has_underscore': None, # (!) real value is "<method 'has_underscore' of 'panda3d.core.TextProperties' objects>"
        'has_underscore_height': None, # (!) real value is "<method 'has_underscore_height' of 'panda3d.core.TextProperties' objects>"
        'has_wordwrap': None, # (!) real value is "<method 'has_wordwrap' of 'panda3d.core.TextProperties' objects>"
        'indent': None, # (!) real value is "<attribute 'indent' of 'panda3d.core.TextProperties' objects>"
        'isAnySpecified': None, # (!) real value is "<method 'isAnySpecified' of 'panda3d.core.TextProperties' objects>"
        'is_any_specified': None, # (!) real value is "<method 'is_any_specified' of 'panda3d.core.TextProperties' objects>"
        'preserve_trailing_whitespace': None, # (!) real value is "<attribute 'preserve_trailing_whitespace' of 'panda3d.core.TextProperties' objects>"
        'setAlign': None, # (!) real value is "<method 'setAlign' of 'panda3d.core.TextProperties' objects>"
        'setBin': None, # (!) real value is "<method 'setBin' of 'panda3d.core.TextProperties' objects>"
        'setDefaultFont': None, # (!) real value is '<staticmethod(<built-in method setDefaultFont of type object at 0x00007FFCFE35EC90>)>'
        'setDirection': None, # (!) real value is "<method 'setDirection' of 'panda3d.core.TextProperties' objects>"
        'setDrawOrder': None, # (!) real value is "<method 'setDrawOrder' of 'panda3d.core.TextProperties' objects>"
        'setFont': None, # (!) real value is "<method 'setFont' of 'panda3d.core.TextProperties' objects>"
        'setGlyphScale': None, # (!) real value is "<method 'setGlyphScale' of 'panda3d.core.TextProperties' objects>"
        'setGlyphShift': None, # (!) real value is "<method 'setGlyphShift' of 'panda3d.core.TextProperties' objects>"
        'setIndent': None, # (!) real value is "<method 'setIndent' of 'panda3d.core.TextProperties' objects>"
        'setPreserveTrailingWhitespace': None, # (!) real value is "<method 'setPreserveTrailingWhitespace' of 'panda3d.core.TextProperties' objects>"
        'setShadow': None, # (!) real value is "<method 'setShadow' of 'panda3d.core.TextProperties' objects>"
        'setShadowColor': None, # (!) real value is "<method 'setShadowColor' of 'panda3d.core.TextProperties' objects>"
        'setSlant': None, # (!) real value is "<method 'setSlant' of 'panda3d.core.TextProperties' objects>"
        'setSmallCaps': None, # (!) real value is "<method 'setSmallCaps' of 'panda3d.core.TextProperties' objects>"
        'setSmallCapsScale': None, # (!) real value is "<method 'setSmallCapsScale' of 'panda3d.core.TextProperties' objects>"
        'setTabWidth': None, # (!) real value is "<method 'setTabWidth' of 'panda3d.core.TextProperties' objects>"
        'setTextColor': None, # (!) real value is "<method 'setTextColor' of 'panda3d.core.TextProperties' objects>"
        'setTextScale': None, # (!) real value is "<method 'setTextScale' of 'panda3d.core.TextProperties' objects>"
        'setUnderscore': None, # (!) real value is "<method 'setUnderscore' of 'panda3d.core.TextProperties' objects>"
        'setUnderscoreHeight': None, # (!) real value is "<method 'setUnderscoreHeight' of 'panda3d.core.TextProperties' objects>"
        'setWordwrap': None, # (!) real value is "<method 'setWordwrap' of 'panda3d.core.TextProperties' objects>"
        'set_align': None, # (!) real value is "<method 'set_align' of 'panda3d.core.TextProperties' objects>"
        'set_bin': None, # (!) real value is "<method 'set_bin' of 'panda3d.core.TextProperties' objects>"
        'set_default_font': None, # (!) real value is '<staticmethod(<built-in method set_default_font of type object at 0x00007FFCFE35EC90>)>'
        'set_direction': None, # (!) real value is "<method 'set_direction' of 'panda3d.core.TextProperties' objects>"
        'set_draw_order': None, # (!) real value is "<method 'set_draw_order' of 'panda3d.core.TextProperties' objects>"
        'set_font': None, # (!) real value is "<method 'set_font' of 'panda3d.core.TextProperties' objects>"
        'set_glyph_scale': None, # (!) real value is "<method 'set_glyph_scale' of 'panda3d.core.TextProperties' objects>"
        'set_glyph_shift': None, # (!) real value is "<method 'set_glyph_shift' of 'panda3d.core.TextProperties' objects>"
        'set_indent': None, # (!) real value is "<method 'set_indent' of 'panda3d.core.TextProperties' objects>"
        'set_preserve_trailing_whitespace': None, # (!) real value is "<method 'set_preserve_trailing_whitespace' of 'panda3d.core.TextProperties' objects>"
        'set_shadow': None, # (!) real value is "<method 'set_shadow' of 'panda3d.core.TextProperties' objects>"
        'set_shadow_color': None, # (!) real value is "<method 'set_shadow_color' of 'panda3d.core.TextProperties' objects>"
        'set_slant': None, # (!) real value is "<method 'set_slant' of 'panda3d.core.TextProperties' objects>"
        'set_small_caps': None, # (!) real value is "<method 'set_small_caps' of 'panda3d.core.TextProperties' objects>"
        'set_small_caps_scale': None, # (!) real value is "<method 'set_small_caps_scale' of 'panda3d.core.TextProperties' objects>"
        'set_tab_width': None, # (!) real value is "<method 'set_tab_width' of 'panda3d.core.TextProperties' objects>"
        'set_text_color': None, # (!) real value is "<method 'set_text_color' of 'panda3d.core.TextProperties' objects>"
        'set_text_scale': None, # (!) real value is "<method 'set_text_scale' of 'panda3d.core.TextProperties' objects>"
        'set_underscore': None, # (!) real value is "<method 'set_underscore' of 'panda3d.core.TextProperties' objects>"
        'set_underscore_height': None, # (!) real value is "<method 'set_underscore_height' of 'panda3d.core.TextProperties' objects>"
        'set_wordwrap': None, # (!) real value is "<method 'set_wordwrap' of 'panda3d.core.TextProperties' objects>"
        'shadow': None, # (!) real value is "<attribute 'shadow' of 'panda3d.core.TextProperties' objects>"
        'shadow_color': None, # (!) real value is "<attribute 'shadow_color' of 'panda3d.core.TextProperties' objects>"
        'slant': None, # (!) real value is "<attribute 'slant' of 'panda3d.core.TextProperties' objects>"
        'small_caps': None, # (!) real value is "<attribute 'small_caps' of 'panda3d.core.TextProperties' objects>"
        'small_caps_scale': None, # (!) real value is "<attribute 'small_caps_scale' of 'panda3d.core.TextProperties' objects>"
        'tab_width': None, # (!) real value is "<attribute 'tab_width' of 'panda3d.core.TextProperties' objects>"
        'text_color': None, # (!) real value is "<attribute 'text_color' of 'panda3d.core.TextProperties' objects>"
        'text_scale': None, # (!) real value is "<attribute 'text_scale' of 'panda3d.core.TextProperties' objects>"
        'underscore': None, # (!) real value is "<attribute 'underscore' of 'panda3d.core.TextProperties' objects>"
        'underscore_height': None, # (!) real value is "<attribute 'underscore_height' of 'panda3d.core.TextProperties' objects>"
        'wordwrap': None, # (!) real value is "<attribute 'wordwrap' of 'panda3d.core.TextProperties' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.core.TextProperties' objects>"
    }
    D_ltr = 0
    D_rtl = 1


