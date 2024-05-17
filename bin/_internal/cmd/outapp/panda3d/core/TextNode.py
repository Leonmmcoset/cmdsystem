# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .PandaNode import PandaNode

from .TextEncoder import TextEncoder

from .TextProperties import TextProperties

class TextNode(PandaNode, TextEncoder, TextProperties):
    """
    /**
     * The primary interface to this module.  This class does basic text assembly;
     * given a string of text and a TextFont object, it creates a piece of
     * geometry that may be placed in the 3-d or 2-d world to represent the
     * indicated text.
     *
     * The TextNode may be used in one of two ways.  Naively, it may simply be
     * parented directly into the scene graph and rendered as if it were a
     * GeomNode; in this mode, the actual polygon geometry that renders the text
     * is not directly visible or accessible, but remains hidden within the
     * TextNode.
     *
     * The second way TextNode may be used is as a text generator.  To use it in
     * this way, do not parent the TextNode to the scene graph; instead, set the
     * properties of the text and call generate() to return an ordinary node,
     * containing ordinary geometry, which you may use however you like.  Each
     * time you call generate() a new node is returned.
     */
    """
    def calcWidth(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        calc_width(TextNode self, unicode line)
        calc_width(TextNode self, str line)
        calc_width(TextNode self, unicode char character)
        
        // These methods calculate the width of a single character or a line of text
        // in the current font.
        
        /**
         * Returns the width of a line of text of arbitrary characters.  The line
         * should not include the newline character.
         */
        
        /**
         * Returns the width of a single character of the font, or 0.0 if the
         * character is not known.  This may be a wide character (greater than 255).
         */
        
        /**
         * Returns the width of a line of text of arbitrary characters.  The line
         * should not include the newline character or any embedded control characters
         * like \1 or \3.
         */
        """
        pass

    def calc_width(self, TextNode_self, unicode_line): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        calc_width(TextNode self, unicode line)
        calc_width(TextNode self, str line)
        calc_width(TextNode self, unicode char character)
        
        // These methods calculate the width of a single character or a line of text
        // in the current font.
        
        /**
         * Returns the width of a line of text of arbitrary characters.  The line
         * should not include the newline character.
         */
        
        /**
         * Returns the width of a single character of the font, or 0.0 if the
         * character is not known.  This may be a wide character (greater than 255).
         */
        
        /**
         * Returns the width of a line of text of arbitrary characters.  The line
         * should not include the newline character or any embedded control characters
         * like \1 or \3.
         */
        """
        pass

    def clearAlign(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_align(const TextNode self)
        
        /**
         *
         */
        """
        pass

    def clearBin(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_bin(const TextNode self)
        
        /**
         * Removes the effect of a previous call to set_bin().  Text will be drawn in
         * whatever bin it would like to be drawn in, with no explicit ordering.
         */
        """
        pass

    def clearCard(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_card(const TextNode self)
        
        /**
         * Specifies that a card will not be drawn behind the text.
         */
        """
        pass

    def clearCardBorder(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_card_border(const TextNode self)
        
        /**
         *
         */
        """
        pass

    def clearCardTexture(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_card_texture(const TextNode self)
        
        /**
         *
         */
        """
        pass

    def clearDrawOrder(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_draw_order(const TextNode self)
        
        /**
         *
         */
        """
        pass

    def clearFont(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_font(const TextNode self)
        
        /**
         * Resets the font to the default font.
         */
        """
        pass

    def clearFrame(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_frame(const TextNode self)
        
        /**
         * Specifies that a border will not be drawn around the text.
         */
        """
        pass

    def clearGlyphScale(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_glyph_scale(const TextNode self)
        
        /**
         *
         */
        """
        pass

    def clearGlyphShift(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_glyph_shift(const TextNode self)
        
        /**
         *
         */
        """
        pass

    def clearIndent(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_indent(const TextNode self)
        
        /**
         *
         */
        """
        pass

    def clearMaxRows(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_max_rows(const TextNode self)
        
        /**
         * Resets the TextNode's default behavior of not limiting the number of rows
         * of text.
         */
        """
        pass

    def clearShadow(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_shadow(const TextNode self)
        
        /**
         * Specifies that a shadow will not be drawn behind the text.
         */
        """
        pass

    def clearShadowColor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_shadow_color(const TextNode self)
        
        /**
         *
         */
        """
        pass

    def clearSlant(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_slant(const TextNode self)
        
        /**
         *
         */
        """
        pass

    def clearSmallCaps(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_small_caps(const TextNode self)
        
        /**
         *
         */
        """
        pass

    def clearSmallCapsScale(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_small_caps_scale(const TextNode self)
        
        /**
         *
         */
        """
        pass

    def clearTabWidth(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_tab_width(const TextNode self)
        
        /**
         *
         */
        """
        pass

    def clearTextColor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_text_color(const TextNode self)
        
        /**
         * Removes the text color specification; the text will be colored whatever it
         * was in the source font file.
         */
        """
        pass

    def clearWordwrap(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_wordwrap(const TextNode self)
        
        /**
         * Removes the wordwrap setting from the TextNode.  Text will be as wide as it
         * is.
         */
        """
        pass

    def clear_align(self, const_TextNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_align(const TextNode self)
        
        /**
         *
         */
        """
        pass

    def clear_bin(self, const_TextNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_bin(const TextNode self)
        
        /**
         * Removes the effect of a previous call to set_bin().  Text will be drawn in
         * whatever bin it would like to be drawn in, with no explicit ordering.
         */
        """
        pass

    def clear_card(self, const_TextNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_card(const TextNode self)
        
        /**
         * Specifies that a card will not be drawn behind the text.
         */
        """
        pass

    def clear_card_border(self, const_TextNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_card_border(const TextNode self)
        
        /**
         *
         */
        """
        pass

    def clear_card_texture(self, const_TextNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_card_texture(const TextNode self)
        
        /**
         *
         */
        """
        pass

    def clear_draw_order(self, const_TextNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_draw_order(const TextNode self)
        
        /**
         *
         */
        """
        pass

    def clear_font(self, const_TextNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_font(const TextNode self)
        
        /**
         * Resets the font to the default font.
         */
        """
        pass

    def clear_frame(self, const_TextNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_frame(const TextNode self)
        
        /**
         * Specifies that a border will not be drawn around the text.
         */
        """
        pass

    def clear_glyph_scale(self, const_TextNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_glyph_scale(const TextNode self)
        
        /**
         *
         */
        """
        pass

    def clear_glyph_shift(self, const_TextNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_glyph_shift(const TextNode self)
        
        /**
         *
         */
        """
        pass

    def clear_indent(self, const_TextNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_indent(const TextNode self)
        
        /**
         *
         */
        """
        pass

    def clear_max_rows(self, const_TextNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_max_rows(const TextNode self)
        
        /**
         * Resets the TextNode's default behavior of not limiting the number of rows
         * of text.
         */
        """
        pass

    def clear_shadow(self, const_TextNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_shadow(const TextNode self)
        
        /**
         * Specifies that a shadow will not be drawn behind the text.
         */
        """
        pass

    def clear_shadow_color(self, const_TextNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_shadow_color(const TextNode self)
        
        /**
         *
         */
        """
        pass

    def clear_slant(self, const_TextNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_slant(const TextNode self)
        
        /**
         *
         */
        """
        pass

    def clear_small_caps(self, const_TextNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_small_caps(const TextNode self)
        
        /**
         *
         */
        """
        pass

    def clear_small_caps_scale(self, const_TextNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_small_caps_scale(const TextNode self)
        
        /**
         *
         */
        """
        pass

    def clear_tab_width(self, const_TextNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_tab_width(const TextNode self)
        
        /**
         *
         */
        """
        pass

    def clear_text_color(self, const_TextNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_text_color(const TextNode self)
        
        /**
         * Removes the text color specification; the text will be colored whatever it
         * was in the source font file.
         */
        """
        pass

    def clear_wordwrap(self, const_TextNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_wordwrap(const TextNode self)
        
        /**
         * Removes the wordwrap setting from the TextNode.  Text will be as wide as it
         * is.
         */
        """
        pass

    def forceUpdate(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        force_update(const TextNode self)
        
        /**
         * Forces the TextNode to recompute itself now, even if it believes nothing
         * has changed.  Normally, this should not need to be called, but it may be
         * useful if some properties change outside of the TextNode's knowledge (for
         * instance, within the font).
         */
        """
        pass

    def force_update(self, const_TextNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        force_update(const TextNode self)
        
        /**
         * Forces the TextNode to recompute itself now, even if it believes nothing
         * has changed.  Normally, this should not need to be called, but it may be
         * useful if some properties change outside of the TextNode's knowledge (for
         * instance, within the font).
         */
        """
        pass

    def generate(self, const_TextNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        generate(const TextNode self)
        
        /**
         * Generates the text, according to the parameters indicated within the
         * TextNode, and returns a Node that may be parented within the tree to
         * represent it.
         */
        """
        pass

    def getBottom(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_bottom(TextNode self)
        
        /**
         * Returns the bottommost extent of the text in local 2-d coordinates,
         * unmodified by the set_transform() matrix.
         */
        """
        pass

    def getCardActual(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_card_actual(TextNode self)
        
        /**
         * Returns the actual dimensions of the card around the text.  If the card was
         * set via set_card_as_margin(), the result returned by this function reflects
         * the size of the current text; if the card was set via set_card_actual(),
         * this returns the values actually set.
         *
         * If the text has no card at all, this returns the dimensions of the text
         * itself, as if the card were set with a margin of 0, 0, 0, 0.
         */
        """
        pass

    def getCardAsSet(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_card_as_set(TextNode self)
        
        /**
         * Returns the dimensions of the card as set by set_card_as_margin() or
         * set_card_actual().  Use is_card_actual() to determine how to interpret the
         * values returned by this function.  It is an error to call this if
         * has_card() is false.
         */
        """
        pass

    def getCardBorderSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_card_border_size(TextNode self)
        
        /**
         *
         */
        """
        pass

    def getCardBorderUvPortion(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_card_border_uv_portion(TextNode self)
        
        /**
         *
         */
        """
        pass

    def getCardColor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_card_color(TextNode self)
        
        /**
         *
         */
        """
        pass

    def getCardDecal(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_card_decal(TextNode self)
        
        /**
         * Returns the card_decal flag.  See set_card_decal().
         */
        """
        pass

    def getCardTexture(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_card_texture(TextNode self)
        
        /**
         *
         */
        """
        pass

    def getCardTransformed(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_card_transformed(TextNode self)
        
        /**
         * Returns the actual card dimensions, transformed by the matrix set by
         * set_transform().  This returns the card dimensions in actual coordinates as
         * seen by the rest of the world.  Also see get_upper_left_3d() and
         * get_lower_right_3d().
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getCoordinateSystem(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_coordinate_system(TextNode self)
        
        /**
         *
         */
        """
        pass

    def getFlattenFlags(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_flatten_flags(TextNode self)
        
        /**
         * Returns the flatten flags.  See set_flatten_flags().
         */
        """
        pass

    def getFrameActual(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_frame_actual(TextNode self)
        
        /**
         * Returns the actual dimensions of the frame around the text.  If the frame
         * was set via set_frame_as_margin(), the result returned by this function
         * reflects the size of the current text; if the frame was set via
         * set_frame_actual(), this returns the values actually set.
         *
         * If the text has no frame at all, this returns the dimensions of the text
         * itself, as if the frame were set with a margin of 0, 0, 0, 0.
         */
        """
        pass

    def getFrameAsSet(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_frame_as_set(TextNode self)
        
        /**
         * Returns the dimensions of the frame as set by set_frame_as_margin() or
         * set_frame_actual().  Use is_frame_actual() to determine how to interpret
         * the values returned by this function.  It is an error to call this if
         * has_frame() is false.
         */
        """
        pass

    def getFrameColor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_frame_color(TextNode self)
        
        /**
         *
         */
        """
        pass

    def getFrameCorners(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_frame_corners(TextNode self)
        
        /**
         *
         */
        """
        pass

    def getFrameLineWidth(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_frame_line_width(TextNode self)
        
        /**
         * Returns the thickness of the lines that will be used to draw the frame.
         */
        """
        pass

    def getHeight(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_height(TextNode self)
        
        /**
         * Returns the net height of the text in local 2-d coordinates.
         */
        """
        pass

    def getInternalGeom(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_internal_geom(TextNode self)
        
        /**
         * Returns the actual node that is used internally to render the text, if the
         * TextNode is parented within the scene graph.
         *
         * In general, you should not call this method.  Call generate() instead if
         * you want to get a handle to geometry that represents the text.  This method
         * is provided as a debugging aid only.
         */
        """
        pass

    def getLeft(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_left(TextNode self)
        
        // The following functions return information about the text that was last
        // built (and is currently visible).
        
        /**
         * Returns the leftmost extent of the text in local 2-d coordinates,
         * unmodified by the set_transform() matrix.
         */
        """
        pass

    def getLineHeight(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_line_height(TextNode self)
        
        /**
         * Returns the number of units high each line of text is.  This is based on
         * the font.  Note that it is possible for the text to include nested font
         * change commands, in which case the value of this method is questionable.
         */
        """
        pass

    def getLowerRight3d(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_lower_right_3d(TextNode self)
        
        /**
         * Returns the lower-right extent of the text object, after it has been
         * transformed into 3-d space by applying the set_transform() matrix.
         */
        """
        pass

    def getMaxRows(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_max_rows(TextNode self)
        
        /**
         * Returns the limit on the height of the TextNode specified by
         * set_max_rows().
         */
        """
        pass

    def getNumRows(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_rows(TextNode self)
        
        /**
         * Returns the number of rows of text that were generated.  This counts word-
         * wrapped rows as well as rows generated due to embedded newlines.
         */
        """
        pass

    def getRight(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_right(TextNode self)
        
        /**
         * Returns the rightmost extent of the text in local 2-d coordinates,
         * unmodified by the set_transform() matrix.
         */
        """
        pass

    def getTop(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_top(TextNode self)
        
        /**
         * Returns the topmost extent of the text in local 2-d coordinates, unmodified
         * by the set_transform() matrix.
         */
        """
        pass

    def getTransform(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_transform(TextNode self)
        
        /**
         *
         */
        """
        pass

    def getUpperLeft3d(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_upper_left_3d(TextNode self)
        
        /**
         * Returns the upper-left extent of the text object, after it has been
         * transformed into 3-d space by applying the set_transform() matrix.
         */
        """
        pass

    def getUsageHint(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_usage_hint(TextNode self)
        
        /**
         * Returns the UsageHint that will be applied to generated geometry.  See
         * set_usage_hint().
         */
        """
        pass

    def getWidth(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_width(TextNode self)
        
        /**
         * Returns the net width of the text in local 2-d coordinates.
         */
        """
        pass

    def getWordwrappedText(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_wordwrapped_text(TextNode self)
        
        // After the text has been set, you can query this to determine how it will
        // be wordwrapped.
        
        /**
         * Returns a string that represents the contents of the text, as it has been
         * formatted by wordwrap rules.
         *
         * In earlier versions, this did not contain any embedded special characters
         * like \1 or \3; now it does.
         */
        """
        pass

    def getWordwrappedWtext(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_wordwrapped_wtext(TextNode self)
        
        /**
         * Returns a wstring that represents the contents of the text, as it has been
         * formatted by wordwrap rules.
         *
         * In earlier versions, this did not contain any embedded special characters
         * like \1 or \3; now it does.
         */
        """
        pass

    def get_bottom(self, TextNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_bottom(TextNode self)
        
        /**
         * Returns the bottommost extent of the text in local 2-d coordinates,
         * unmodified by the set_transform() matrix.
         */
        """
        pass

    def get_card_actual(self, TextNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_card_actual(TextNode self)
        
        /**
         * Returns the actual dimensions of the card around the text.  If the card was
         * set via set_card_as_margin(), the result returned by this function reflects
         * the size of the current text; if the card was set via set_card_actual(),
         * this returns the values actually set.
         *
         * If the text has no card at all, this returns the dimensions of the text
         * itself, as if the card were set with a margin of 0, 0, 0, 0.
         */
        """
        pass

    def get_card_as_set(self, TextNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_card_as_set(TextNode self)
        
        /**
         * Returns the dimensions of the card as set by set_card_as_margin() or
         * set_card_actual().  Use is_card_actual() to determine how to interpret the
         * values returned by this function.  It is an error to call this if
         * has_card() is false.
         */
        """
        pass

    def get_card_border_size(self, TextNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_card_border_size(TextNode self)
        
        /**
         *
         */
        """
        pass

    def get_card_border_uv_portion(self, TextNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_card_border_uv_portion(TextNode self)
        
        /**
         *
         */
        """
        pass

    def get_card_color(self, TextNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_card_color(TextNode self)
        
        /**
         *
         */
        """
        pass

    def get_card_decal(self, TextNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_card_decal(TextNode self)
        
        /**
         * Returns the card_decal flag.  See set_card_decal().
         */
        """
        pass

    def get_card_texture(self, TextNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_card_texture(TextNode self)
        
        /**
         *
         */
        """
        pass

    def get_card_transformed(self, TextNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_card_transformed(TextNode self)
        
        /**
         * Returns the actual card dimensions, transformed by the matrix set by
         * set_transform().  This returns the card dimensions in actual coordinates as
         * seen by the rest of the world.  Also see get_upper_left_3d() and
         * get_lower_right_3d().
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_coordinate_system(self, TextNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_coordinate_system(TextNode self)
        
        /**
         *
         */
        """
        pass

    def get_flatten_flags(self, TextNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_flatten_flags(TextNode self)
        
        /**
         * Returns the flatten flags.  See set_flatten_flags().
         */
        """
        pass

    def get_frame_actual(self, TextNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_frame_actual(TextNode self)
        
        /**
         * Returns the actual dimensions of the frame around the text.  If the frame
         * was set via set_frame_as_margin(), the result returned by this function
         * reflects the size of the current text; if the frame was set via
         * set_frame_actual(), this returns the values actually set.
         *
         * If the text has no frame at all, this returns the dimensions of the text
         * itself, as if the frame were set with a margin of 0, 0, 0, 0.
         */
        """
        pass

    def get_frame_as_set(self, TextNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_frame_as_set(TextNode self)
        
        /**
         * Returns the dimensions of the frame as set by set_frame_as_margin() or
         * set_frame_actual().  Use is_frame_actual() to determine how to interpret
         * the values returned by this function.  It is an error to call this if
         * has_frame() is false.
         */
        """
        pass

    def get_frame_color(self, TextNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_frame_color(TextNode self)
        
        /**
         *
         */
        """
        pass

    def get_frame_corners(self, TextNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_frame_corners(TextNode self)
        
        /**
         *
         */
        """
        pass

    def get_frame_line_width(self, TextNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_frame_line_width(TextNode self)
        
        /**
         * Returns the thickness of the lines that will be used to draw the frame.
         */
        """
        pass

    def get_height(self, TextNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_height(TextNode self)
        
        /**
         * Returns the net height of the text in local 2-d coordinates.
         */
        """
        pass

    def get_internal_geom(self, TextNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_internal_geom(TextNode self)
        
        /**
         * Returns the actual node that is used internally to render the text, if the
         * TextNode is parented within the scene graph.
         *
         * In general, you should not call this method.  Call generate() instead if
         * you want to get a handle to geometry that represents the text.  This method
         * is provided as a debugging aid only.
         */
        """
        pass

    def get_left(self, TextNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_left(TextNode self)
        
        // The following functions return information about the text that was last
        // built (and is currently visible).
        
        /**
         * Returns the leftmost extent of the text in local 2-d coordinates,
         * unmodified by the set_transform() matrix.
         */
        """
        pass

    def get_line_height(self, TextNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_line_height(TextNode self)
        
        /**
         * Returns the number of units high each line of text is.  This is based on
         * the font.  Note that it is possible for the text to include nested font
         * change commands, in which case the value of this method is questionable.
         */
        """
        pass

    def get_lower_right_3d(self, TextNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_lower_right_3d(TextNode self)
        
        /**
         * Returns the lower-right extent of the text object, after it has been
         * transformed into 3-d space by applying the set_transform() matrix.
         */
        """
        pass

    def get_max_rows(self, TextNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_max_rows(TextNode self)
        
        /**
         * Returns the limit on the height of the TextNode specified by
         * set_max_rows().
         */
        """
        pass

    def get_num_rows(self, TextNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_rows(TextNode self)
        
        /**
         * Returns the number of rows of text that were generated.  This counts word-
         * wrapped rows as well as rows generated due to embedded newlines.
         */
        """
        pass

    def get_right(self, TextNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_right(TextNode self)
        
        /**
         * Returns the rightmost extent of the text in local 2-d coordinates,
         * unmodified by the set_transform() matrix.
         */
        """
        pass

    def get_top(self, TextNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_top(TextNode self)
        
        /**
         * Returns the topmost extent of the text in local 2-d coordinates, unmodified
         * by the set_transform() matrix.
         */
        """
        pass

    def get_transform(self, TextNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_transform(TextNode self)
        
        /**
         *
         */
        """
        pass

    def get_upper_left_3d(self, TextNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_upper_left_3d(TextNode self)
        
        /**
         * Returns the upper-left extent of the text object, after it has been
         * transformed into 3-d space by applying the set_transform() matrix.
         */
        """
        pass

    def get_usage_hint(self, TextNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_usage_hint(TextNode self)
        
        /**
         * Returns the UsageHint that will be applied to generated geometry.  See
         * set_usage_hint().
         */
        """
        pass

    def get_width(self, TextNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_width(TextNode self)
        
        /**
         * Returns the net width of the text in local 2-d coordinates.
         */
        """
        pass

    def get_wordwrapped_text(self, TextNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_wordwrapped_text(TextNode self)
        
        // After the text has been set, you can query this to determine how it will
        // be wordwrapped.
        
        /**
         * Returns a string that represents the contents of the text, as it has been
         * formatted by wordwrap rules.
         *
         * In earlier versions, this did not contain any embedded special characters
         * like \1 or \3; now it does.
         */
        """
        pass

    def get_wordwrapped_wtext(self, TextNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_wordwrapped_wtext(TextNode self)
        
        /**
         * Returns a wstring that represents the contents of the text, as it has been
         * formatted by wordwrap rules.
         *
         * In earlier versions, this did not contain any embedded special characters
         * like \1 or \3; now it does.
         */
        """
        pass

    def hasCard(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_card(TextNode self)
        
        /**
         *
         */
        """
        pass

    def hasCardBorder(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_card_border(TextNode self)
        
        /**
         *
         */
        """
        pass

    def hasCardTexture(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_card_texture(TextNode self)
        
        /**
         *
         */
        """
        pass

    def hasCharacter(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_character(TextNode self, unicode char character)
        
        /**
         * Returns true if the named character exists in the font or can be
         * synthesized by Panda, false otherwise.  (Panda can synthesize some accented
         * characters by combining similar-looking glyphs from the font.)
         *
         * This returns true for whitespace and Unicode whitespace characters (if they
         * exist in the font), but returns false for characters that would render with
         * the "invalid glyph".
         */
        """
        pass

    def hasExactCharacter(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_exact_character(TextNode self, unicode char character)
        
        /**
         * Returns true if the named character exists in the font exactly as named,
         * false otherwise.  Note that because Panda can assemble glyphs together
         * automatically using cheesy accent marks, this is not a reliable indicator
         * of whether a suitable glyph can be rendered for the character.  For that,
         * use has_character() instead.
         *
         * This returns true for whitespace and Unicode whitespace characters (if they
         * exist in the font), but returns false for characters that would render with
         * the "invalid glyph".  It also returns false for characters that would be
         * synthesized within Panda, but see has_character().
         */
        """
        pass

    def hasFrame(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_frame(TextNode self)
        
        /**
         *
         */
        """
        pass

    def hasMaxRows(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_max_rows(TextNode self)
        
        /**
         * Returns true if a limit on the height of the TextNode has been set via
         * set_max_rows(), false otherwise.
         */
        """
        pass

    def hasOverflow(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_overflow(TextNode self)
        
        /**
         * Returns true if the last text set on the text node exceeded the max_rows
         * constraint, or false if it all fit.
         */
        """
        pass

    def has_card(self, TextNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_card(TextNode self)
        
        /**
         *
         */
        """
        pass

    def has_card_border(self, TextNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_card_border(TextNode self)
        
        /**
         *
         */
        """
        pass

    def has_card_texture(self, TextNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_card_texture(TextNode self)
        
        /**
         *
         */
        """
        pass

    def has_character(self, TextNode_self, unicode_char_character): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_character(TextNode self, unicode char character)
        
        /**
         * Returns true if the named character exists in the font or can be
         * synthesized by Panda, false otherwise.  (Panda can synthesize some accented
         * characters by combining similar-looking glyphs from the font.)
         *
         * This returns true for whitespace and Unicode whitespace characters (if they
         * exist in the font), but returns false for characters that would render with
         * the "invalid glyph".
         */
        """
        pass

    def has_exact_character(self, TextNode_self, unicode_char_character): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_exact_character(TextNode self, unicode char character)
        
        /**
         * Returns true if the named character exists in the font exactly as named,
         * false otherwise.  Note that because Panda can assemble glyphs together
         * automatically using cheesy accent marks, this is not a reliable indicator
         * of whether a suitable glyph can be rendered for the character.  For that,
         * use has_character() instead.
         *
         * This returns true for whitespace and Unicode whitespace characters (if they
         * exist in the font), but returns false for characters that would render with
         * the "invalid glyph".  It also returns false for characters that would be
         * synthesized within Panda, but see has_character().
         */
        """
        pass

    def has_frame(self, TextNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_frame(TextNode self)
        
        /**
         *
         */
        """
        pass

    def has_max_rows(self, TextNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_max_rows(TextNode self)
        
        /**
         * Returns true if a limit on the height of the TextNode has been set via
         * set_max_rows(), false otherwise.
         */
        """
        pass

    def has_overflow(self, TextNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_overflow(TextNode self)
        
        /**
         * Returns true if the last text set on the text node exceeded the max_rows
         * constraint, or false if it all fit.
         */
        """
        pass

    def isCardAsMargin(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_card_as_margin(TextNode self)
        
        /**
         * If this is true, the card was set via a call to set_card_as_margin(), and
         * the dimension of the card as returned by get_card_as_set() represent a
         * margin all around the text.  If false, then the card was set via a call to
         * set_card_actual(), and the dimensions of the card as returned by
         * get_card_as_set() are relative to the text's origin.
         */
        """
        pass

    def isFrameAsMargin(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_frame_as_margin(TextNode self)
        
        /**
         * If this is true, the frame was set via a call to set_frame_as_margin(), and
         * the dimension of the frame as returned by get_frame_as_set() represent a
         * margin all around the text.  If false, then the frame was set via a call to
         * set_frame_actual(), and the dimensions of the frame as returned by
         * get_frame_as_set() are relative to the text's origin.
         */
        """
        pass

    def isWhitespace(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_whitespace(TextNode self, unicode char character)
        
        /**
         * Returns true if the indicated character represents whitespace in the font,
         * or false if anything visible will be rendered for it.
         *
         * This returns true for whitespace and Unicode whitespace characters (if they
         * exist in the font), and returns false for any other characters, including
         * characters that do not exist in the font (these would be rendered with the
         * "invalid glyph", which is visible).
         *
         * Note that this function can be reliably used to identify Unicode whitespace
         * characters only if the font has all of the whitespace characters defined.
         * It will return false for any character not in the font, even if it is an
         * official Unicode whitespace character.
         */
        """
        pass

    def is_card_as_margin(self, TextNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_card_as_margin(TextNode self)
        
        /**
         * If this is true, the card was set via a call to set_card_as_margin(), and
         * the dimension of the card as returned by get_card_as_set() represent a
         * margin all around the text.  If false, then the card was set via a call to
         * set_card_actual(), and the dimensions of the card as returned by
         * get_card_as_set() are relative to the text's origin.
         */
        """
        pass

    def is_frame_as_margin(self, TextNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_frame_as_margin(TextNode self)
        
        /**
         * If this is true, the frame was set via a call to set_frame_as_margin(), and
         * the dimension of the frame as returned by get_frame_as_set() represent a
         * margin all around the text.  If false, then the frame was set via a call to
         * set_frame_actual(), and the dimensions of the frame as returned by
         * get_frame_as_set() are relative to the text's origin.
         */
        """
        pass

    def is_whitespace(self, TextNode_self, unicode_char_character): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_whitespace(TextNode self, unicode char character)
        
        /**
         * Returns true if the indicated character represents whitespace in the font,
         * or false if anything visible will be rendered for it.
         *
         * This returns true for whitespace and Unicode whitespace characters (if they
         * exist in the font), and returns false for any other characters, including
         * characters that do not exist in the font (these would be rendered with the
         * "invalid glyph", which is visible).
         *
         * Note that this function can be reliably used to identify Unicode whitespace
         * characters only if the font has all of the whitespace characters defined.
         * It will return false for any character not in the font, even if it is an
         * official Unicode whitespace character.
         */
        """
        pass

    def output(self, TextNode_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(TextNode self, ostream out)
        
        /**
         *
         */
        """
        pass

    def setAlign(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_align(const TextNode self, int align_type)
        
        /**
         *
         */
        """
        pass

    def setBin(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_bin(const TextNode self, str bin)
        
        /**
         * Names the GeomBin that the TextNode geometry should be assigned to.  If
         * this is set, then a GeomBinTransition will be created to explicitly place
         * each component in the named bin.
         *
         * The draw_order value will also be passed to each GeomBinTransition as
         * appropriate; this is particularly useful if this names a GeomBinFixed, e.g.
         * "fixed".
         */
        """
        pass

    def setCardActual(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_card_actual(const TextNode self, float left, float right, float bottom, float top)
        
        /**
         * Similar to set_card_as_margin, except the card is specified in actual
         * coordinate units (relative to the text's origin), irrespective of the size
         * of the text.  The left and bottom coordinates should generally be negative,
         * while the right and top coordinates should generally be positive.
         */
        """
        pass

    def setCardAsMargin(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_card_as_margin(const TextNode self, float left, float right, float bottom, float top)
        
        /**
         * Specifies that a (possibly opaque or semitransparent) card will be held
         * behind the text when it is next created.  Like set_frame_as_margin, the
         * parameters are the amount of additional padding to insert around the text
         * in each dimension, and all should generally be positive.
         */
        """
        pass

    def setCardBorder(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_card_border(const TextNode self, float size, float uv_portion)
        
        /**
         *
         */
        """
        pass

    def setCardColor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_card_color(const TextNode self, const LVecBase4f card_color)
        set_card_color(const TextNode self, float r, float g, float b, float a)
        
        /**
         *
         */
        
        /**
         *
         */
        """
        pass

    def setCardDecal(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_card_decal(const TextNode self, bool card_decal)
        
        /**
         * Sets the card_decal flag.  When this is true, the text is decalled onto the
         * card, which is necessary if the TextNode is to be rendered in the 3-d world
         * without putting it in a bin.
         */
        """
        pass

    def setCardTexture(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_card_texture(const TextNode self, Texture card_texture)
        
        /**
         *
         */
        """
        pass

    def setCoordinateSystem(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_coordinate_system(const TextNode self, int cs)
        
        /**
         * Specifies the coordinate system in which the text will be generated.
         */
        """
        pass

    def setDrawOrder(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_draw_order(const TextNode self, int draw_order)
        
        /**
         * Sets the drawing order of text created by the TextMaker.  This is actually
         * the draw order of the card and frame.  The shadow is drawn at
         * _draw_order+1, and the text at _draw_order+2.
         *
         * This affects the sorting order assigned to the arcs as they are created,
         * and also is passed to whatever bin may be assigned via set_bin().
         *
         * The return value is the first unused draw_order number, e.g.  _draw_order +
         * 3.
         */
        """
        pass

    def setFlattenFlags(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_flatten_flags(const TextNode self, int flatten_flags)
        
        /**
         * Sets the flatten flags.  This should be a union of the
         * TextNode::FlattenFlags options.  This controls the degree of flattening
         * performed on the TextNode's internal geometry (i.e.  the scene graph
         * returned by generate()) each time the text is changed.  In general, more
         * flattening means a more optimal result, but it will take more time to
         * generate.
         *
         * The choice may be any of these three:
         *
         * FF_none - No flatten operation is called.  The letters are left as
         * independent Geoms.
         *
         * FF_light - A flatten_light() operation is called.  The attributes are
         * applied to the vertices, but no nodes are removed.
         *
         * FF_medium - A flatten_medium() operation is called.  The attributes are
         * applied to the vertices, and a few trivial nodes are removed.
         *
         * FF_strong - A flatten_strong() operation is called.  The attributes are
         * applied to the vertices, and the resulting nodes are aggressively combined
         * into as few nodes as possible.
         *
         * In addition to the above choices, you may optionally include the following
         * flag:
         *
         * FF_dynamic_merge - Copy the geoms into a single GeomVertexData as we go,
         * instead of relying on the flatten operation at the end.  This pre-flattens
         * the text considerably, and may obviate the need for flatten altogether; it
         * also tends to improve performance considerably even if you do call flatten.
         * However, it is not as fast as not calling flatten at all.
         *
         * The default is taken from the text-flatten and text-dynamic-merge config
         * variables.
         */
        """
        pass

    def setFont(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_font(const TextNode self, TextFont font)
        
        /**
         * Sets the font that will be used when making text.  If this is set to NULL,
         * the default font will be used, which can be set via set_default_font().
         */
        """
        pass

    def setFrameActual(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_frame_actual(const TextNode self, float left, float right, float bottom, float top)
        
        /**
         * Similar to set_frame_as_margin, except the frame is specified in actual
         * coordinate units (relative to the text's origin), irrespective of the size
         * of the text.  The left and bottom coordinates should generally be negative,
         * while the right and top coordinates should generally be positive.
         */
        """
        pass

    def setFrameAsMargin(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_frame_as_margin(const TextNode self, float left, float right, float bottom, float top)
        
        /**
         * Specifies that a border will be drawn around the text when it is next
         * created.  The parameters are the amount of additional padding to insert
         * between the frame and the text in each dimension, and all should generally
         * be positive.
         */
        """
        pass

    def setFrameColor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_frame_color(const TextNode self, const LVecBase4f frame_color)
        set_frame_color(const TextNode self, float r, float g, float b, float a)
        
        /**
         *
         */
        
        /**
         *
         */
        """
        pass

    def setFrameCorners(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_frame_corners(const TextNode self, bool corners)
        
        /**
         * Enables or disables the drawing of corners for the frame.  These are extra
         * points drawn at each of the four corners, to soften the ugly edges
         * generated when the line width is greater than one.
         */
        """
        pass

    def setFrameLineWidth(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_frame_line_width(const TextNode self, float line_width)
        
        /**
         * Specifies the thickness of the lines that will be used to draw the frame.
         */
        """
        pass

    def setGlyphScale(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_glyph_scale(const TextNode self, float glyph_scale)
        
        /**
         * Specifies the factor by which to scale each letter of the text as it is
         * placed.  This can be used (possibly in conjunction with set_glyph_shift())
         * to implement superscripting or subscripting.
         */
        """
        pass

    def setGlyphShift(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_glyph_shift(const TextNode self, float glyph_shift)
        
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
        set_indent(const TextNode self, float indent)
        
        /**
         * Specifies the amount of extra space that is inserted before the first
         * character of each line.  This can be thought of as a left margin.
         */
        """
        pass

    def setMaxRows(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_max_rows(const TextNode self, int max_rows)
        
        /**
         * Sets the maximum number of rows that may be formatted by the TextNode.  If
         * more text than this is attempted, it will be truncated and has_overflow()
         * will return true.
         */
        """
        pass

    def setShadow(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_shadow(const TextNode self, const LVecBase2f shadow_offset)
        set_shadow(const TextNode self, float xoffset, float yoffset)
        
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
        set_shadow_color(const TextNode self, const LVecBase4f shadow_color)
        set_shadow_color(const TextNode self, float r, float g, float b, float a)
        
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
        set_slant(const TextNode self, float slant)
        
        /**
         *
         */
        """
        pass

    def setSmallCaps(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_small_caps(const TextNode self, bool small_caps)
        
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
        set_small_caps_scale(const TextNode self, float small_caps_scale)
        
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
        set_tab_width(const TextNode self, float tab_width)
        
        /**
         * Sets the width of each tab stop, in screen units.  A tab character embedded
         * in the text will advance the horizontal position to the next tab stop.
         */
        """
        pass

    def setTextColor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_text_color(const TextNode self, const LVecBase4f text_color)
        set_text_color(const TextNode self, float r, float g, float b, float a)
        
        /**
         *
         */
        
        /**
         *
         */
        """
        pass

    def setTransform(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_transform(const TextNode self, const LMatrix4f transform)
        
        /**
         * Sets an additional transform that is applied to the entire text paragraph.
         */
        """
        pass

    def setUsageHint(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_usage_hint(const TextNode self, int usage_hint)
        
        /**
         * Specifies the UsageHint that will be applied to generated geometry.  The
         * default is UH_static, which is probably the right setting, but if you know
         * the TextNode's geometry will have a short lifespan, it may be better to set
         * it to UH_stream.  See geomEnums.h.
         */
        """
        pass

    def setWordwrap(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_wordwrap(const TextNode self, float wordwrap)
        
        /**
         * Sets the text up to automatically wordwrap when it exceeds the indicated
         * width.  This can be thought of as a right margin or margin width.
         */
        """
        pass

    def set_align(self, const_TextNode_self, int_align_type): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_align(const TextNode self, int align_type)
        
        /**
         *
         */
        """
        pass

    def set_bin(self, const_TextNode_self, str_bin): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_bin(const TextNode self, str bin)
        
        /**
         * Names the GeomBin that the TextNode geometry should be assigned to.  If
         * this is set, then a GeomBinTransition will be created to explicitly place
         * each component in the named bin.
         *
         * The draw_order value will also be passed to each GeomBinTransition as
         * appropriate; this is particularly useful if this names a GeomBinFixed, e.g.
         * "fixed".
         */
        """
        pass

    def set_card_actual(self, const_TextNode_self, float_left, float_right, float_bottom, float_top): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_card_actual(const TextNode self, float left, float right, float bottom, float top)
        
        /**
         * Similar to set_card_as_margin, except the card is specified in actual
         * coordinate units (relative to the text's origin), irrespective of the size
         * of the text.  The left and bottom coordinates should generally be negative,
         * while the right and top coordinates should generally be positive.
         */
        """
        pass

    def set_card_as_margin(self, const_TextNode_self, float_left, float_right, float_bottom, float_top): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_card_as_margin(const TextNode self, float left, float right, float bottom, float top)
        
        /**
         * Specifies that a (possibly opaque or semitransparent) card will be held
         * behind the text when it is next created.  Like set_frame_as_margin, the
         * parameters are the amount of additional padding to insert around the text
         * in each dimension, and all should generally be positive.
         */
        """
        pass

    def set_card_border(self, const_TextNode_self, float_size, float_uv_portion): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_card_border(const TextNode self, float size, float uv_portion)
        
        /**
         *
         */
        """
        pass

    def set_card_color(self, const_TextNode_self, const_LVecBase4f_card_color): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_card_color(const TextNode self, const LVecBase4f card_color)
        set_card_color(const TextNode self, float r, float g, float b, float a)
        
        /**
         *
         */
        
        /**
         *
         */
        """
        pass

    def set_card_decal(self, const_TextNode_self, bool_card_decal): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_card_decal(const TextNode self, bool card_decal)
        
        /**
         * Sets the card_decal flag.  When this is true, the text is decalled onto the
         * card, which is necessary if the TextNode is to be rendered in the 3-d world
         * without putting it in a bin.
         */
        """
        pass

    def set_card_texture(self, const_TextNode_self, Texture_card_texture): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_card_texture(const TextNode self, Texture card_texture)
        
        /**
         *
         */
        """
        pass

    def set_coordinate_system(self, const_TextNode_self, int_cs): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_coordinate_system(const TextNode self, int cs)
        
        /**
         * Specifies the coordinate system in which the text will be generated.
         */
        """
        pass

    def set_draw_order(self, const_TextNode_self, int_draw_order): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_draw_order(const TextNode self, int draw_order)
        
        /**
         * Sets the drawing order of text created by the TextMaker.  This is actually
         * the draw order of the card and frame.  The shadow is drawn at
         * _draw_order+1, and the text at _draw_order+2.
         *
         * This affects the sorting order assigned to the arcs as they are created,
         * and also is passed to whatever bin may be assigned via set_bin().
         *
         * The return value is the first unused draw_order number, e.g.  _draw_order +
         * 3.
         */
        """
        pass

    def set_flatten_flags(self, const_TextNode_self, int_flatten_flags): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_flatten_flags(const TextNode self, int flatten_flags)
        
        /**
         * Sets the flatten flags.  This should be a union of the
         * TextNode::FlattenFlags options.  This controls the degree of flattening
         * performed on the TextNode's internal geometry (i.e.  the scene graph
         * returned by generate()) each time the text is changed.  In general, more
         * flattening means a more optimal result, but it will take more time to
         * generate.
         *
         * The choice may be any of these three:
         *
         * FF_none - No flatten operation is called.  The letters are left as
         * independent Geoms.
         *
         * FF_light - A flatten_light() operation is called.  The attributes are
         * applied to the vertices, but no nodes are removed.
         *
         * FF_medium - A flatten_medium() operation is called.  The attributes are
         * applied to the vertices, and a few trivial nodes are removed.
         *
         * FF_strong - A flatten_strong() operation is called.  The attributes are
         * applied to the vertices, and the resulting nodes are aggressively combined
         * into as few nodes as possible.
         *
         * In addition to the above choices, you may optionally include the following
         * flag:
         *
         * FF_dynamic_merge - Copy the geoms into a single GeomVertexData as we go,
         * instead of relying on the flatten operation at the end.  This pre-flattens
         * the text considerably, and may obviate the need for flatten altogether; it
         * also tends to improve performance considerably even if you do call flatten.
         * However, it is not as fast as not calling flatten at all.
         *
         * The default is taken from the text-flatten and text-dynamic-merge config
         * variables.
         */
        """
        pass

    def set_font(self, const_TextNode_self, TextFont_font): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_font(const TextNode self, TextFont font)
        
        /**
         * Sets the font that will be used when making text.  If this is set to NULL,
         * the default font will be used, which can be set via set_default_font().
         */
        """
        pass

    def set_frame_actual(self, const_TextNode_self, float_left, float_right, float_bottom, float_top): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_frame_actual(const TextNode self, float left, float right, float bottom, float top)
        
        /**
         * Similar to set_frame_as_margin, except the frame is specified in actual
         * coordinate units (relative to the text's origin), irrespective of the size
         * of the text.  The left and bottom coordinates should generally be negative,
         * while the right and top coordinates should generally be positive.
         */
        """
        pass

    def set_frame_as_margin(self, const_TextNode_self, float_left, float_right, float_bottom, float_top): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_frame_as_margin(const TextNode self, float left, float right, float bottom, float top)
        
        /**
         * Specifies that a border will be drawn around the text when it is next
         * created.  The parameters are the amount of additional padding to insert
         * between the frame and the text in each dimension, and all should generally
         * be positive.
         */
        """
        pass

    def set_frame_color(self, const_TextNode_self, const_LVecBase4f_frame_color): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_frame_color(const TextNode self, const LVecBase4f frame_color)
        set_frame_color(const TextNode self, float r, float g, float b, float a)
        
        /**
         *
         */
        
        /**
         *
         */
        """
        pass

    def set_frame_corners(self, const_TextNode_self, bool_corners): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_frame_corners(const TextNode self, bool corners)
        
        /**
         * Enables or disables the drawing of corners for the frame.  These are extra
         * points drawn at each of the four corners, to soften the ugly edges
         * generated when the line width is greater than one.
         */
        """
        pass

    def set_frame_line_width(self, const_TextNode_self, float_line_width): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_frame_line_width(const TextNode self, float line_width)
        
        /**
         * Specifies the thickness of the lines that will be used to draw the frame.
         */
        """
        pass

    def set_glyph_scale(self, const_TextNode_self, float_glyph_scale): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_glyph_scale(const TextNode self, float glyph_scale)
        
        /**
         * Specifies the factor by which to scale each letter of the text as it is
         * placed.  This can be used (possibly in conjunction with set_glyph_shift())
         * to implement superscripting or subscripting.
         */
        """
        pass

    def set_glyph_shift(self, const_TextNode_self, float_glyph_shift): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_glyph_shift(const TextNode self, float glyph_shift)
        
        /**
         * Specifies a vertical amount to shift each letter of the text as it is
         * placed.  This can be used (possibly in conjunction with set_glyph_scale())
         * to implement superscripting or subscripting.
         */
        """
        pass

    def set_indent(self, const_TextNode_self, float_indent): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_indent(const TextNode self, float indent)
        
        /**
         * Specifies the amount of extra space that is inserted before the first
         * character of each line.  This can be thought of as a left margin.
         */
        """
        pass

    def set_max_rows(self, const_TextNode_self, int_max_rows): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_max_rows(const TextNode self, int max_rows)
        
        /**
         * Sets the maximum number of rows that may be formatted by the TextNode.  If
         * more text than this is attempted, it will be truncated and has_overflow()
         * will return true.
         */
        """
        pass

    def set_shadow(self, const_TextNode_self, const_LVecBase2f_shadow_offset): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_shadow(const TextNode self, const LVecBase2f shadow_offset)
        set_shadow(const TextNode self, float xoffset, float yoffset)
        
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

    def set_shadow_color(self, const_TextNode_self, const_LVecBase4f_shadow_color): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_shadow_color(const TextNode self, const LVecBase4f shadow_color)
        set_shadow_color(const TextNode self, float r, float g, float b, float a)
        
        /**
         *
         */
        
        /**
         *
         */
        """
        pass

    def set_slant(self, const_TextNode_self, float_slant): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_slant(const TextNode self, float slant)
        
        /**
         *
         */
        """
        pass

    def set_small_caps(self, const_TextNode_self, bool_small_caps): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_small_caps(const TextNode self, bool small_caps)
        
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

    def set_small_caps_scale(self, const_TextNode_self, float_small_caps_scale): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_small_caps_scale(const TextNode self, float small_caps_scale)
        
        /**
         * Sets the scale factor applied to lowercase letters from their uppercase
         * equivalents, when the small_caps flag is in effect.  See set_small_caps().
         * Normally, this will be a number less than one.
         */
        """
        pass

    def set_tab_width(self, const_TextNode_self, float_tab_width): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_tab_width(const TextNode self, float tab_width)
        
        /**
         * Sets the width of each tab stop, in screen units.  A tab character embedded
         * in the text will advance the horizontal position to the next tab stop.
         */
        """
        pass

    def set_text_color(self, const_TextNode_self, const_LVecBase4f_text_color): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_text_color(const TextNode self, const LVecBase4f text_color)
        set_text_color(const TextNode self, float r, float g, float b, float a)
        
        /**
         *
         */
        
        /**
         *
         */
        """
        pass

    def set_transform(self, const_TextNode_self, const_LMatrix4f_transform): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_transform(const TextNode self, const LMatrix4f transform)
        
        /**
         * Sets an additional transform that is applied to the entire text paragraph.
         */
        """
        pass

    def set_usage_hint(self, const_TextNode_self, int_usage_hint): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_usage_hint(const TextNode self, int usage_hint)
        
        /**
         * Specifies the UsageHint that will be applied to generated geometry.  The
         * default is UH_static, which is probably the right setting, but if you know
         * the TextNode's geometry will have a short lifespan, it may be better to set
         * it to UH_stream.  See geomEnums.h.
         */
        """
        pass

    def set_wordwrap(self, const_TextNode_self, float_wordwrap): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_wordwrap(const TextNode self, float wordwrap)
        
        /**
         * Sets the text up to automatically wordwrap when it exceeds the indicated
         * width.  This can be thought of as a right margin or margin width.
         */
        """
        pass

    def upcastToPandaNode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_PandaNode(const TextNode self)
        
        upcast from TextNode to PandaNode
        """
        pass

    def upcastToTextEncoder(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_TextEncoder(const TextNode self)
        
        upcast from TextNode to TextEncoder
        """
        pass

    def upcastToTextProperties(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_TextProperties(const TextNode self)
        
        upcast from TextNode to TextProperties
        """
        pass

    def upcast_to_PandaNode(self, const_TextNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_PandaNode(const TextNode self)
        
        upcast from TextNode to PandaNode
        """
        pass

    def upcast_to_TextEncoder(self, const_TextNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_TextEncoder(const TextNode self)
        
        upcast from TextNode to TextEncoder
        """
        pass

    def upcast_to_TextProperties(self, const_TextNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_TextProperties(const TextNode self)
        
        upcast from TextNode to TextProperties
        """
        pass

    def update(self, const_TextNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        update(const TextNode self)
        
        /**
         * Can be called after the TextNode has been fully configured, to force the
         * node to recompute its text immediately, rather than waiting for it to be
         * drawn.  This call is optional.
         */
        """
        pass

    def write(self, TextNode_self, ostream_out, int_indent_level): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(TextNode self, ostream out, int indent_level)
        
        /**
         *
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    align = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """/**
 *
 */"""

    bin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """/**
 * Returns the drawing bin set with set_bin(), or empty string if no bin has
 * been set.
 */"""

    card_color = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    card_texture = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    coordinate_system = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    draw_order = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """/**
 * Returns the drawing order set with set_draw_order().
 */"""

    flatten_flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    font = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """/**
 * Returns the font currently in use, if any.  If no font is in use, this
 * returns the default font.
 */"""

    frame_color = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    frame_corners = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    frame_line_width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glyph_scale = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """/**
 * Returns the scale factor of each letter as specified by set_glyph_scale().
 */"""

    glyph_shift = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """/**
 * Returns the vertical shift of each letter as specified by
 * set_glyph_shift().
 */"""

    indent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """/**
 *
 */"""

    max_rows = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    preserve_trailing_whitespace = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """/**
 * Returns the preserve_trailing_whitespace flag.  See
 * set_preserve_trailing_whitespace().
 */"""

    shadow = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """/**
 * Returns the offset of the shadow as set by set_shadow().  It is an error to
 * call this if has_shadow() is false.
 */"""

    shadow_color = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """/**
 *
 */"""

    slant = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """/**
 * Returns the factor by which the text is specified to slant to the right.
 */"""

    small_caps = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """/**
 * Returns the small_caps flag.  See set_small_caps().
 */"""

    small_caps_scale = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """/**
 * Returns the scale factor applied to lowercase letters from their uppercase
 * equivalents, when the small_caps flag is in effect.  See set_small_caps()
 * and set_small_caps_scale().
 */"""

    tab_width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """/**
 * Returns the width set via set_tab_width().
 */"""

    text_color = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """/**
 *
 */"""

    text_scale = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """/**
 * Returns the scale factor of the text as specified by set_text_scale().
 */"""

    transform = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    underscore = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """/**
 * Returns the underscore flag.  See set_underscore().
 */"""

    underscore_height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """/**
 * Returns the vertical height of the underscore; see set_underscore_height().
 */"""

    usage_hint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    wordwrap = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """/**
 *
 */"""


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        'FFDynamicMerge': 8,
        'FFLight': 1,
        'FFMedium': 2,
        'FFNone': 0,
        'FFStrong': 4,
        'FF_dynamic_merge': 8,
        'FF_light': 1,
        'FF_medium': 2,
        'FF_none': 0,
        'FF_strong': 4,
        '__doc__': '/**\n * The primary interface to this module.  This class does basic text assembly;\n * given a string of text and a TextFont object, it creates a piece of\n * geometry that may be placed in the 3-d or 2-d world to represent the\n * indicated text.\n *\n * The TextNode may be used in one of two ways.  Naively, it may simply be\n * parented directly into the scene graph and rendered as if it were a\n * GeomNode; in this mode, the actual polygon geometry that renders the text\n * is not directly visible or accessible, but remains hidden within the\n * TextNode.\n *\n * The second way TextNode may be used is as a text generator.  To use it in\n * this way, do not parent the TextNode to the scene graph; instead, set the\n * properties of the text and call generate() to return an ordinary node,\n * containing ordinary geometry, which you may use however you like.  Each\n * time you call generate() a new node is returned.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.TextNode' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE35F3D0>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.TextNode' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.TextNode' objects>"
        'align': None, # (!) real value is "<attribute 'align' of 'panda3d.core.TextNode' objects>"
        'bin': None, # (!) real value is "<attribute 'bin' of 'panda3d.core.TextNode' objects>"
        'calcWidth': None, # (!) real value is "<method 'calcWidth' of 'panda3d.core.TextNode' objects>"
        'calc_width': None, # (!) real value is "<method 'calc_width' of 'panda3d.core.TextNode' objects>"
        'card_color': None, # (!) real value is "<attribute 'card_color' of 'panda3d.core.TextNode' objects>"
        'card_texture': None, # (!) real value is "<attribute 'card_texture' of 'panda3d.core.TextNode' objects>"
        'clearAlign': None, # (!) real value is "<method 'clearAlign' of 'panda3d.core.TextNode' objects>"
        'clearBin': None, # (!) real value is "<method 'clearBin' of 'panda3d.core.TextNode' objects>"
        'clearCard': None, # (!) real value is "<method 'clearCard' of 'panda3d.core.TextNode' objects>"
        'clearCardBorder': None, # (!) real value is "<method 'clearCardBorder' of 'panda3d.core.TextNode' objects>"
        'clearCardTexture': None, # (!) real value is "<method 'clearCardTexture' of 'panda3d.core.TextNode' objects>"
        'clearDrawOrder': None, # (!) real value is "<method 'clearDrawOrder' of 'panda3d.core.TextNode' objects>"
        'clearFont': None, # (!) real value is "<method 'clearFont' of 'panda3d.core.TextNode' objects>"
        'clearFrame': None, # (!) real value is "<method 'clearFrame' of 'panda3d.core.TextNode' objects>"
        'clearGlyphScale': None, # (!) real value is "<method 'clearGlyphScale' of 'panda3d.core.TextNode' objects>"
        'clearGlyphShift': None, # (!) real value is "<method 'clearGlyphShift' of 'panda3d.core.TextNode' objects>"
        'clearIndent': None, # (!) real value is "<method 'clearIndent' of 'panda3d.core.TextNode' objects>"
        'clearMaxRows': None, # (!) real value is "<method 'clearMaxRows' of 'panda3d.core.TextNode' objects>"
        'clearShadow': None, # (!) real value is "<method 'clearShadow' of 'panda3d.core.TextNode' objects>"
        'clearShadowColor': None, # (!) real value is "<method 'clearShadowColor' of 'panda3d.core.TextNode' objects>"
        'clearSlant': None, # (!) real value is "<method 'clearSlant' of 'panda3d.core.TextNode' objects>"
        'clearSmallCaps': None, # (!) real value is "<method 'clearSmallCaps' of 'panda3d.core.TextNode' objects>"
        'clearSmallCapsScale': None, # (!) real value is "<method 'clearSmallCapsScale' of 'panda3d.core.TextNode' objects>"
        'clearTabWidth': None, # (!) real value is "<method 'clearTabWidth' of 'panda3d.core.TextNode' objects>"
        'clearTextColor': None, # (!) real value is "<method 'clearTextColor' of 'panda3d.core.TextNode' objects>"
        'clearWordwrap': None, # (!) real value is "<method 'clearWordwrap' of 'panda3d.core.TextNode' objects>"
        'clear_align': None, # (!) real value is "<method 'clear_align' of 'panda3d.core.TextNode' objects>"
        'clear_bin': None, # (!) real value is "<method 'clear_bin' of 'panda3d.core.TextNode' objects>"
        'clear_card': None, # (!) real value is "<method 'clear_card' of 'panda3d.core.TextNode' objects>"
        'clear_card_border': None, # (!) real value is "<method 'clear_card_border' of 'panda3d.core.TextNode' objects>"
        'clear_card_texture': None, # (!) real value is "<method 'clear_card_texture' of 'panda3d.core.TextNode' objects>"
        'clear_draw_order': None, # (!) real value is "<method 'clear_draw_order' of 'panda3d.core.TextNode' objects>"
        'clear_font': None, # (!) real value is "<method 'clear_font' of 'panda3d.core.TextNode' objects>"
        'clear_frame': None, # (!) real value is "<method 'clear_frame' of 'panda3d.core.TextNode' objects>"
        'clear_glyph_scale': None, # (!) real value is "<method 'clear_glyph_scale' of 'panda3d.core.TextNode' objects>"
        'clear_glyph_shift': None, # (!) real value is "<method 'clear_glyph_shift' of 'panda3d.core.TextNode' objects>"
        'clear_indent': None, # (!) real value is "<method 'clear_indent' of 'panda3d.core.TextNode' objects>"
        'clear_max_rows': None, # (!) real value is "<method 'clear_max_rows' of 'panda3d.core.TextNode' objects>"
        'clear_shadow': None, # (!) real value is "<method 'clear_shadow' of 'panda3d.core.TextNode' objects>"
        'clear_shadow_color': None, # (!) real value is "<method 'clear_shadow_color' of 'panda3d.core.TextNode' objects>"
        'clear_slant': None, # (!) real value is "<method 'clear_slant' of 'panda3d.core.TextNode' objects>"
        'clear_small_caps': None, # (!) real value is "<method 'clear_small_caps' of 'panda3d.core.TextNode' objects>"
        'clear_small_caps_scale': None, # (!) real value is "<method 'clear_small_caps_scale' of 'panda3d.core.TextNode' objects>"
        'clear_tab_width': None, # (!) real value is "<method 'clear_tab_width' of 'panda3d.core.TextNode' objects>"
        'clear_text_color': None, # (!) real value is "<method 'clear_text_color' of 'panda3d.core.TextNode' objects>"
        'clear_wordwrap': None, # (!) real value is "<method 'clear_wordwrap' of 'panda3d.core.TextNode' objects>"
        'coordinate_system': None, # (!) real value is "<attribute 'coordinate_system' of 'panda3d.core.TextNode' objects>"
        'draw_order': None, # (!) real value is "<attribute 'draw_order' of 'panda3d.core.TextNode' objects>"
        'flatten_flags': None, # (!) real value is "<attribute 'flatten_flags' of 'panda3d.core.TextNode' objects>"
        'font': None, # (!) real value is "<attribute 'font' of 'panda3d.core.TextNode' objects>"
        'forceUpdate': None, # (!) real value is "<method 'forceUpdate' of 'panda3d.core.TextNode' objects>"
        'force_update': None, # (!) real value is "<method 'force_update' of 'panda3d.core.TextNode' objects>"
        'frame_color': None, # (!) real value is "<attribute 'frame_color' of 'panda3d.core.TextNode' objects>"
        'frame_corners': None, # (!) real value is "<attribute 'frame_corners' of 'panda3d.core.TextNode' objects>"
        'frame_line_width': None, # (!) real value is "<attribute 'frame_line_width' of 'panda3d.core.TextNode' objects>"
        'generate': None, # (!) real value is "<method 'generate' of 'panda3d.core.TextNode' objects>"
        'getBottom': None, # (!) real value is "<method 'getBottom' of 'panda3d.core.TextNode' objects>"
        'getCardActual': None, # (!) real value is "<method 'getCardActual' of 'panda3d.core.TextNode' objects>"
        'getCardAsSet': None, # (!) real value is "<method 'getCardAsSet' of 'panda3d.core.TextNode' objects>"
        'getCardBorderSize': None, # (!) real value is "<method 'getCardBorderSize' of 'panda3d.core.TextNode' objects>"
        'getCardBorderUvPortion': None, # (!) real value is "<method 'getCardBorderUvPortion' of 'panda3d.core.TextNode' objects>"
        'getCardColor': None, # (!) real value is "<method 'getCardColor' of 'panda3d.core.TextNode' objects>"
        'getCardDecal': None, # (!) real value is "<method 'getCardDecal' of 'panda3d.core.TextNode' objects>"
        'getCardTexture': None, # (!) real value is "<method 'getCardTexture' of 'panda3d.core.TextNode' objects>"
        'getCardTransformed': None, # (!) real value is "<method 'getCardTransformed' of 'panda3d.core.TextNode' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE35F3D0>)>'
        'getCoordinateSystem': None, # (!) real value is "<method 'getCoordinateSystem' of 'panda3d.core.TextNode' objects>"
        'getFlattenFlags': None, # (!) real value is "<method 'getFlattenFlags' of 'panda3d.core.TextNode' objects>"
        'getFrameActual': None, # (!) real value is "<method 'getFrameActual' of 'panda3d.core.TextNode' objects>"
        'getFrameAsSet': None, # (!) real value is "<method 'getFrameAsSet' of 'panda3d.core.TextNode' objects>"
        'getFrameColor': None, # (!) real value is "<method 'getFrameColor' of 'panda3d.core.TextNode' objects>"
        'getFrameCorners': None, # (!) real value is "<method 'getFrameCorners' of 'panda3d.core.TextNode' objects>"
        'getFrameLineWidth': None, # (!) real value is "<method 'getFrameLineWidth' of 'panda3d.core.TextNode' objects>"
        'getHeight': None, # (!) real value is "<method 'getHeight' of 'panda3d.core.TextNode' objects>"
        'getInternalGeom': None, # (!) real value is "<method 'getInternalGeom' of 'panda3d.core.TextNode' objects>"
        'getLeft': None, # (!) real value is "<method 'getLeft' of 'panda3d.core.TextNode' objects>"
        'getLineHeight': None, # (!) real value is "<method 'getLineHeight' of 'panda3d.core.TextNode' objects>"
        'getLowerRight3d': None, # (!) real value is "<method 'getLowerRight3d' of 'panda3d.core.TextNode' objects>"
        'getMaxRows': None, # (!) real value is "<method 'getMaxRows' of 'panda3d.core.TextNode' objects>"
        'getNumRows': None, # (!) real value is "<method 'getNumRows' of 'panda3d.core.TextNode' objects>"
        'getRight': None, # (!) real value is "<method 'getRight' of 'panda3d.core.TextNode' objects>"
        'getTop': None, # (!) real value is "<method 'getTop' of 'panda3d.core.TextNode' objects>"
        'getTransform': None, # (!) real value is "<method 'getTransform' of 'panda3d.core.TextNode' objects>"
        'getUpperLeft3d': None, # (!) real value is "<method 'getUpperLeft3d' of 'panda3d.core.TextNode' objects>"
        'getUsageHint': None, # (!) real value is "<method 'getUsageHint' of 'panda3d.core.TextNode' objects>"
        'getWidth': None, # (!) real value is "<method 'getWidth' of 'panda3d.core.TextNode' objects>"
        'getWordwrappedText': None, # (!) real value is "<method 'getWordwrappedText' of 'panda3d.core.TextNode' objects>"
        'getWordwrappedWtext': None, # (!) real value is "<method 'getWordwrappedWtext' of 'panda3d.core.TextNode' objects>"
        'get_bottom': None, # (!) real value is "<method 'get_bottom' of 'panda3d.core.TextNode' objects>"
        'get_card_actual': None, # (!) real value is "<method 'get_card_actual' of 'panda3d.core.TextNode' objects>"
        'get_card_as_set': None, # (!) real value is "<method 'get_card_as_set' of 'panda3d.core.TextNode' objects>"
        'get_card_border_size': None, # (!) real value is "<method 'get_card_border_size' of 'panda3d.core.TextNode' objects>"
        'get_card_border_uv_portion': None, # (!) real value is "<method 'get_card_border_uv_portion' of 'panda3d.core.TextNode' objects>"
        'get_card_color': None, # (!) real value is "<method 'get_card_color' of 'panda3d.core.TextNode' objects>"
        'get_card_decal': None, # (!) real value is "<method 'get_card_decal' of 'panda3d.core.TextNode' objects>"
        'get_card_texture': None, # (!) real value is "<method 'get_card_texture' of 'panda3d.core.TextNode' objects>"
        'get_card_transformed': None, # (!) real value is "<method 'get_card_transformed' of 'panda3d.core.TextNode' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE35F3D0>)>'
        'get_coordinate_system': None, # (!) real value is "<method 'get_coordinate_system' of 'panda3d.core.TextNode' objects>"
        'get_flatten_flags': None, # (!) real value is "<method 'get_flatten_flags' of 'panda3d.core.TextNode' objects>"
        'get_frame_actual': None, # (!) real value is "<method 'get_frame_actual' of 'panda3d.core.TextNode' objects>"
        'get_frame_as_set': None, # (!) real value is "<method 'get_frame_as_set' of 'panda3d.core.TextNode' objects>"
        'get_frame_color': None, # (!) real value is "<method 'get_frame_color' of 'panda3d.core.TextNode' objects>"
        'get_frame_corners': None, # (!) real value is "<method 'get_frame_corners' of 'panda3d.core.TextNode' objects>"
        'get_frame_line_width': None, # (!) real value is "<method 'get_frame_line_width' of 'panda3d.core.TextNode' objects>"
        'get_height': None, # (!) real value is "<method 'get_height' of 'panda3d.core.TextNode' objects>"
        'get_internal_geom': None, # (!) real value is "<method 'get_internal_geom' of 'panda3d.core.TextNode' objects>"
        'get_left': None, # (!) real value is "<method 'get_left' of 'panda3d.core.TextNode' objects>"
        'get_line_height': None, # (!) real value is "<method 'get_line_height' of 'panda3d.core.TextNode' objects>"
        'get_lower_right_3d': None, # (!) real value is "<method 'get_lower_right_3d' of 'panda3d.core.TextNode' objects>"
        'get_max_rows': None, # (!) real value is "<method 'get_max_rows' of 'panda3d.core.TextNode' objects>"
        'get_num_rows': None, # (!) real value is "<method 'get_num_rows' of 'panda3d.core.TextNode' objects>"
        'get_right': None, # (!) real value is "<method 'get_right' of 'panda3d.core.TextNode' objects>"
        'get_top': None, # (!) real value is "<method 'get_top' of 'panda3d.core.TextNode' objects>"
        'get_transform': None, # (!) real value is "<method 'get_transform' of 'panda3d.core.TextNode' objects>"
        'get_upper_left_3d': None, # (!) real value is "<method 'get_upper_left_3d' of 'panda3d.core.TextNode' objects>"
        'get_usage_hint': None, # (!) real value is "<method 'get_usage_hint' of 'panda3d.core.TextNode' objects>"
        'get_width': None, # (!) real value is "<method 'get_width' of 'panda3d.core.TextNode' objects>"
        'get_wordwrapped_text': None, # (!) real value is "<method 'get_wordwrapped_text' of 'panda3d.core.TextNode' objects>"
        'get_wordwrapped_wtext': None, # (!) real value is "<method 'get_wordwrapped_wtext' of 'panda3d.core.TextNode' objects>"
        'glyph_scale': None, # (!) real value is "<attribute 'glyph_scale' of 'panda3d.core.TextNode' objects>"
        'glyph_shift': None, # (!) real value is "<attribute 'glyph_shift' of 'panda3d.core.TextNode' objects>"
        'hasCard': None, # (!) real value is "<method 'hasCard' of 'panda3d.core.TextNode' objects>"
        'hasCardBorder': None, # (!) real value is "<method 'hasCardBorder' of 'panda3d.core.TextNode' objects>"
        'hasCardTexture': None, # (!) real value is "<method 'hasCardTexture' of 'panda3d.core.TextNode' objects>"
        'hasCharacter': None, # (!) real value is "<method 'hasCharacter' of 'panda3d.core.TextNode' objects>"
        'hasExactCharacter': None, # (!) real value is "<method 'hasExactCharacter' of 'panda3d.core.TextNode' objects>"
        'hasFrame': None, # (!) real value is "<method 'hasFrame' of 'panda3d.core.TextNode' objects>"
        'hasMaxRows': None, # (!) real value is "<method 'hasMaxRows' of 'panda3d.core.TextNode' objects>"
        'hasOverflow': None, # (!) real value is "<method 'hasOverflow' of 'panda3d.core.TextNode' objects>"
        'has_card': None, # (!) real value is "<method 'has_card' of 'panda3d.core.TextNode' objects>"
        'has_card_border': None, # (!) real value is "<method 'has_card_border' of 'panda3d.core.TextNode' objects>"
        'has_card_texture': None, # (!) real value is "<method 'has_card_texture' of 'panda3d.core.TextNode' objects>"
        'has_character': None, # (!) real value is "<method 'has_character' of 'panda3d.core.TextNode' objects>"
        'has_exact_character': None, # (!) real value is "<method 'has_exact_character' of 'panda3d.core.TextNode' objects>"
        'has_frame': None, # (!) real value is "<method 'has_frame' of 'panda3d.core.TextNode' objects>"
        'has_max_rows': None, # (!) real value is "<method 'has_max_rows' of 'panda3d.core.TextNode' objects>"
        'has_overflow': None, # (!) real value is "<method 'has_overflow' of 'panda3d.core.TextNode' objects>"
        'indent': None, # (!) real value is "<attribute 'indent' of 'panda3d.core.TextNode' objects>"
        'isCardAsMargin': None, # (!) real value is "<method 'isCardAsMargin' of 'panda3d.core.TextNode' objects>"
        'isFrameAsMargin': None, # (!) real value is "<method 'isFrameAsMargin' of 'panda3d.core.TextNode' objects>"
        'isWhitespace': None, # (!) real value is "<method 'isWhitespace' of 'panda3d.core.TextNode' objects>"
        'is_card_as_margin': None, # (!) real value is "<method 'is_card_as_margin' of 'panda3d.core.TextNode' objects>"
        'is_frame_as_margin': None, # (!) real value is "<method 'is_frame_as_margin' of 'panda3d.core.TextNode' objects>"
        'is_whitespace': None, # (!) real value is "<method 'is_whitespace' of 'panda3d.core.TextNode' objects>"
        'max_rows': None, # (!) real value is "<attribute 'max_rows' of 'panda3d.core.TextNode' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.TextNode' objects>"
        'preserve_trailing_whitespace': None, # (!) real value is "<attribute 'preserve_trailing_whitespace' of 'panda3d.core.TextNode' objects>"
        'setAlign': None, # (!) real value is "<method 'setAlign' of 'panda3d.core.TextNode' objects>"
        'setBin': None, # (!) real value is "<method 'setBin' of 'panda3d.core.TextNode' objects>"
        'setCardActual': None, # (!) real value is "<method 'setCardActual' of 'panda3d.core.TextNode' objects>"
        'setCardAsMargin': None, # (!) real value is "<method 'setCardAsMargin' of 'panda3d.core.TextNode' objects>"
        'setCardBorder': None, # (!) real value is "<method 'setCardBorder' of 'panda3d.core.TextNode' objects>"
        'setCardColor': None, # (!) real value is "<method 'setCardColor' of 'panda3d.core.TextNode' objects>"
        'setCardDecal': None, # (!) real value is "<method 'setCardDecal' of 'panda3d.core.TextNode' objects>"
        'setCardTexture': None, # (!) real value is "<method 'setCardTexture' of 'panda3d.core.TextNode' objects>"
        'setCoordinateSystem': None, # (!) real value is "<method 'setCoordinateSystem' of 'panda3d.core.TextNode' objects>"
        'setDrawOrder': None, # (!) real value is "<method 'setDrawOrder' of 'panda3d.core.TextNode' objects>"
        'setFlattenFlags': None, # (!) real value is "<method 'setFlattenFlags' of 'panda3d.core.TextNode' objects>"
        'setFont': None, # (!) real value is "<method 'setFont' of 'panda3d.core.TextNode' objects>"
        'setFrameActual': None, # (!) real value is "<method 'setFrameActual' of 'panda3d.core.TextNode' objects>"
        'setFrameAsMargin': None, # (!) real value is "<method 'setFrameAsMargin' of 'panda3d.core.TextNode' objects>"
        'setFrameColor': None, # (!) real value is "<method 'setFrameColor' of 'panda3d.core.TextNode' objects>"
        'setFrameCorners': None, # (!) real value is "<method 'setFrameCorners' of 'panda3d.core.TextNode' objects>"
        'setFrameLineWidth': None, # (!) real value is "<method 'setFrameLineWidth' of 'panda3d.core.TextNode' objects>"
        'setGlyphScale': None, # (!) real value is "<method 'setGlyphScale' of 'panda3d.core.TextNode' objects>"
        'setGlyphShift': None, # (!) real value is "<method 'setGlyphShift' of 'panda3d.core.TextNode' objects>"
        'setIndent': None, # (!) real value is "<method 'setIndent' of 'panda3d.core.TextNode' objects>"
        'setMaxRows': None, # (!) real value is "<method 'setMaxRows' of 'panda3d.core.TextNode' objects>"
        'setShadow': None, # (!) real value is "<method 'setShadow' of 'panda3d.core.TextNode' objects>"
        'setShadowColor': None, # (!) real value is "<method 'setShadowColor' of 'panda3d.core.TextNode' objects>"
        'setSlant': None, # (!) real value is "<method 'setSlant' of 'panda3d.core.TextNode' objects>"
        'setSmallCaps': None, # (!) real value is "<method 'setSmallCaps' of 'panda3d.core.TextNode' objects>"
        'setSmallCapsScale': None, # (!) real value is "<method 'setSmallCapsScale' of 'panda3d.core.TextNode' objects>"
        'setTabWidth': None, # (!) real value is "<method 'setTabWidth' of 'panda3d.core.TextNode' objects>"
        'setTextColor': None, # (!) real value is "<method 'setTextColor' of 'panda3d.core.TextNode' objects>"
        'setTransform': None, # (!) real value is "<method 'setTransform' of 'panda3d.core.TextNode' objects>"
        'setUsageHint': None, # (!) real value is "<method 'setUsageHint' of 'panda3d.core.TextNode' objects>"
        'setWordwrap': None, # (!) real value is "<method 'setWordwrap' of 'panda3d.core.TextNode' objects>"
        'set_align': None, # (!) real value is "<method 'set_align' of 'panda3d.core.TextNode' objects>"
        'set_bin': None, # (!) real value is "<method 'set_bin' of 'panda3d.core.TextNode' objects>"
        'set_card_actual': None, # (!) real value is "<method 'set_card_actual' of 'panda3d.core.TextNode' objects>"
        'set_card_as_margin': None, # (!) real value is "<method 'set_card_as_margin' of 'panda3d.core.TextNode' objects>"
        'set_card_border': None, # (!) real value is "<method 'set_card_border' of 'panda3d.core.TextNode' objects>"
        'set_card_color': None, # (!) real value is "<method 'set_card_color' of 'panda3d.core.TextNode' objects>"
        'set_card_decal': None, # (!) real value is "<method 'set_card_decal' of 'panda3d.core.TextNode' objects>"
        'set_card_texture': None, # (!) real value is "<method 'set_card_texture' of 'panda3d.core.TextNode' objects>"
        'set_coordinate_system': None, # (!) real value is "<method 'set_coordinate_system' of 'panda3d.core.TextNode' objects>"
        'set_draw_order': None, # (!) real value is "<method 'set_draw_order' of 'panda3d.core.TextNode' objects>"
        'set_flatten_flags': None, # (!) real value is "<method 'set_flatten_flags' of 'panda3d.core.TextNode' objects>"
        'set_font': None, # (!) real value is "<method 'set_font' of 'panda3d.core.TextNode' objects>"
        'set_frame_actual': None, # (!) real value is "<method 'set_frame_actual' of 'panda3d.core.TextNode' objects>"
        'set_frame_as_margin': None, # (!) real value is "<method 'set_frame_as_margin' of 'panda3d.core.TextNode' objects>"
        'set_frame_color': None, # (!) real value is "<method 'set_frame_color' of 'panda3d.core.TextNode' objects>"
        'set_frame_corners': None, # (!) real value is "<method 'set_frame_corners' of 'panda3d.core.TextNode' objects>"
        'set_frame_line_width': None, # (!) real value is "<method 'set_frame_line_width' of 'panda3d.core.TextNode' objects>"
        'set_glyph_scale': None, # (!) real value is "<method 'set_glyph_scale' of 'panda3d.core.TextNode' objects>"
        'set_glyph_shift': None, # (!) real value is "<method 'set_glyph_shift' of 'panda3d.core.TextNode' objects>"
        'set_indent': None, # (!) real value is "<method 'set_indent' of 'panda3d.core.TextNode' objects>"
        'set_max_rows': None, # (!) real value is "<method 'set_max_rows' of 'panda3d.core.TextNode' objects>"
        'set_shadow': None, # (!) real value is "<method 'set_shadow' of 'panda3d.core.TextNode' objects>"
        'set_shadow_color': None, # (!) real value is "<method 'set_shadow_color' of 'panda3d.core.TextNode' objects>"
        'set_slant': None, # (!) real value is "<method 'set_slant' of 'panda3d.core.TextNode' objects>"
        'set_small_caps': None, # (!) real value is "<method 'set_small_caps' of 'panda3d.core.TextNode' objects>"
        'set_small_caps_scale': None, # (!) real value is "<method 'set_small_caps_scale' of 'panda3d.core.TextNode' objects>"
        'set_tab_width': None, # (!) real value is "<method 'set_tab_width' of 'panda3d.core.TextNode' objects>"
        'set_text_color': None, # (!) real value is "<method 'set_text_color' of 'panda3d.core.TextNode' objects>"
        'set_transform': None, # (!) real value is "<method 'set_transform' of 'panda3d.core.TextNode' objects>"
        'set_usage_hint': None, # (!) real value is "<method 'set_usage_hint' of 'panda3d.core.TextNode' objects>"
        'set_wordwrap': None, # (!) real value is "<method 'set_wordwrap' of 'panda3d.core.TextNode' objects>"
        'shadow': None, # (!) real value is "<attribute 'shadow' of 'panda3d.core.TextNode' objects>"
        'shadow_color': None, # (!) real value is "<attribute 'shadow_color' of 'panda3d.core.TextNode' objects>"
        'slant': None, # (!) real value is "<attribute 'slant' of 'panda3d.core.TextNode' objects>"
        'small_caps': None, # (!) real value is "<attribute 'small_caps' of 'panda3d.core.TextNode' objects>"
        'small_caps_scale': None, # (!) real value is "<attribute 'small_caps_scale' of 'panda3d.core.TextNode' objects>"
        'tab_width': None, # (!) real value is "<attribute 'tab_width' of 'panda3d.core.TextNode' objects>"
        'text_color': None, # (!) real value is "<attribute 'text_color' of 'panda3d.core.TextNode' objects>"
        'text_scale': None, # (!) real value is "<attribute 'text_scale' of 'panda3d.core.TextNode' objects>"
        'transform': None, # (!) real value is "<attribute 'transform' of 'panda3d.core.TextNode' objects>"
        'underscore': None, # (!) real value is "<attribute 'underscore' of 'panda3d.core.TextNode' objects>"
        'underscore_height': None, # (!) real value is "<attribute 'underscore_height' of 'panda3d.core.TextNode' objects>"
        'upcastToPandaNode': None, # (!) real value is "<method 'upcastToPandaNode' of 'panda3d.core.TextNode' objects>"
        'upcastToTextEncoder': None, # (!) real value is "<method 'upcastToTextEncoder' of 'panda3d.core.TextNode' objects>"
        'upcastToTextProperties': None, # (!) real value is "<method 'upcastToTextProperties' of 'panda3d.core.TextNode' objects>"
        'upcast_to_PandaNode': None, # (!) real value is "<method 'upcast_to_PandaNode' of 'panda3d.core.TextNode' objects>"
        'upcast_to_TextEncoder': None, # (!) real value is "<method 'upcast_to_TextEncoder' of 'panda3d.core.TextNode' objects>"
        'upcast_to_TextProperties': None, # (!) real value is "<method 'upcast_to_TextProperties' of 'panda3d.core.TextNode' objects>"
        'update': None, # (!) real value is "<method 'update' of 'panda3d.core.TextNode' objects>"
        'usage_hint': None, # (!) real value is "<attribute 'usage_hint' of 'panda3d.core.TextNode' objects>"
        'wordwrap': None, # (!) real value is "<attribute 'wordwrap' of 'panda3d.core.TextNode' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.core.TextNode' objects>"
    }
    FFDynamicMerge = 8
    FFLight = 1
    FFMedium = 2
    FFNone = 0
    FFStrong = 4
    FF_dynamic_merge = 8
    FF_light = 1
    FF_medium = 2
    FF_none = 0
    FF_strong = 4


