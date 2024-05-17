# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class TextAssembler(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * This class is not normally used directly by user code, but is used by the
     * TextNode to lay out a block of text and convert it into rows of Geoms
     * according to the TextProperties.  However, user code may take advantage of
     * it, if desired, for very low-level text operations.
     */
    """
    def assembleText(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        assemble_text(const TextAssembler self)
        
        /**
         * Actually assembles all of the text into a GeomNode, and returns the node
         * (or possibly a parent of the node, to keep the shadow separate).  Once this
         * has been called, you may query the extents of the text via get_ul(),
         * get_lr().
         */
        """
        pass

    def assemble_text(self, const_TextAssembler_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        assemble_text(const TextAssembler self)
        
        /**
         * Actually assembles all of the text into a GeomNode, and returns the node
         * (or possibly a parent of the node, to keep the shadow separate).  Once this
         * has been called, you may query the extents of the text via get_ul(),
         * get_lr().
         */
        """
        pass

    def assign(self, const_TextAssembler_self, const_TextAssembler_copy): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        assign(const TextAssembler self, const TextAssembler copy)
        """
        pass

    def calcC(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        calc_c(TextAssembler self, int n)
        
        /**
         * Computes the column index of the nth character or graphic object in the
         * text and returns it.
         *
         * If the nth character is not a normal printable character with a position in
         * the wordwrapped string, returns -1 (for instance, a soft-hyphen character,
         * or a newline character, may not have a corresponding position).
         */
        """
        pass

    def calcIndex(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        calc_index(TextAssembler self, int r, int c)
        
        /**
         * Computes the character index of the character at the rth row and cth column
         * position.  This is the inverse of calc_r_c().
         *
         * It is legal for c to exceed the index number of the last column by 1, and
         * it is legal for r to exceed the index number of the last row by 1, if c is
         * 0.
         */
        """
        pass

    def calcR(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        calc_r(TextAssembler self, int n)
        
        /**
         * Computes the row index of the nth character or graphic object in the text
         * and returns it.
         *
         * If the nth character is not a normal printable character with a position in
         * the wordwrapped string, returns -1 (for instance, a soft-hyphen character,
         * or a newline character, may not have a corresponding position).
         */
        """
        pass

    def calcWidth(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        calc_width(const TextGraphic graphic, const TextProperties properties)
        calc_width(unicode char character, const TextProperties properties)
        
        /**
         * Returns the width of a single character, according to its associated font.
         */
        
        /**
         * Returns the width of a single character, according to its associated font.
         * This also correctly calculates the width of cheesy ligatures and accented
         * characters, which may not exist in the font as such.
         *
         * This does not take kerning into account, however.
         */
        
        /**
         * Returns the width of a single TextGraphic image.
         */
        """
        pass

    def calc_c(self, TextAssembler_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        calc_c(TextAssembler self, int n)
        
        /**
         * Computes the column index of the nth character or graphic object in the
         * text and returns it.
         *
         * If the nth character is not a normal printable character with a position in
         * the wordwrapped string, returns -1 (for instance, a soft-hyphen character,
         * or a newline character, may not have a corresponding position).
         */
        """
        pass

    def calc_index(self, TextAssembler_self, int_r, int_c): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        calc_index(TextAssembler self, int r, int c)
        
        /**
         * Computes the character index of the character at the rth row and cth column
         * position.  This is the inverse of calc_r_c().
         *
         * It is legal for c to exceed the index number of the last column by 1, and
         * it is legal for r to exceed the index number of the last row by 1, if c is
         * 0.
         */
        """
        pass

    def calc_r(self, TextAssembler_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        calc_r(TextAssembler self, int n)
        
        /**
         * Computes the row index of the nth character or graphic object in the text
         * and returns it.
         *
         * If the nth character is not a normal printable character with a position in
         * the wordwrapped string, returns -1 (for instance, a soft-hyphen character,
         * or a newline character, may not have a corresponding position).
         */
        """
        pass

    def calc_width(self, const_TextGraphic_graphic, const_TextProperties_properties): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        calc_width(const TextGraphic graphic, const TextProperties properties)
        calc_width(unicode char character, const TextProperties properties)
        
        /**
         * Returns the width of a single character, according to its associated font.
         */
        
        /**
         * Returns the width of a single character, according to its associated font.
         * This also correctly calculates the width of cheesy ligatures and accented
         * characters, which may not exist in the font as such.
         *
         * This does not take kerning into account, however.
         */
        
        /**
         * Returns the width of a single TextGraphic image.
         */
        """
        pass

    def clear(self, const_TextAssembler_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear(const TextAssembler self)
        
        /**
         * Reinitializes the contents of the TextAssembler.
         */
        """
        pass

    def getCharacter(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_character(TextAssembler self, int n)
        get_character(TextAssembler self, int r, int c)
        
        /**
         * Returns the character at the indicated position in the pre-wordwrapped
         * string.  If the object at this position is a graphic object instead of a
         * character, returns 0.
         */
        
        /**
         * Returns the character at the indicated position in the indicated row.  If
         * the object at this position is a graphic object instead of a character,
         * returns 0.
         */
        """
        pass

    def getDynamicMerge(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_dynamic_merge(TextAssembler self)
        
        /**
         * Returns the dynamic_merge flag.  See TextNode::set_flatten_flags().
         */
        """
        pass

    def getGraphic(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_graphic(TextAssembler self, int n)
        get_graphic(TextAssembler self, int r, int c)
        
        /**
         * Returns the graphic object at the indicated position in the pre-wordwrapped
         * string.  If the object at this position is a character instead of a graphic
         * object, returns NULL.
         */
        
        /**
         * Returns the graphic object at the indicated position in the indicated row.
         * If the object at this position is a character instead of a graphic object,
         * returns NULL.
         */
        """
        pass

    def getLr(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_lr(TextAssembler self)
        
        /**
         * Returns the lower-right corner of the assembled text, in 2-d text
         * coordinates.
         */
        """
        pass

    def getMaxRows(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_max_rows(TextAssembler self)
        
        /**
         * If max_rows is greater than zero, no more than max_rows will be accepted.
         * Text beyond that will be truncated.
         */
        """
        pass

    def getMultilineMode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_multiline_mode(TextAssembler self)
        
        /**
         * Returns the multline_mode flag.  See TextNode::set_multiline_mode().
         */
        """
        pass

    def getNumCharacters(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_characters(TextAssembler self)
        
        /**
         * Returns the number of characters of text, before wordwrapping.
         */
        """
        pass

    def getNumCols(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_cols(TextAssembler self, int r)
        
        /**
         * Returns the number of characters and/or graphic objects in the nth row.
         */
        """
        pass

    def getNumRows(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_rows(TextAssembler self)
        
        /**
         * Returns the number of rows of text after it has all been wordwrapped and
         * assembled.
         */
        """
        pass

    def getPlainWtext(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_plain_wtext(TextAssembler self)
        
        /**
         * Returns a wstring that represents the contents of the text, without any
         * embedded properties characters.  If there is an embedded graphic object, a
         * zero value is inserted in that position.
         *
         * This string has the same length as get_num_characters(), and the characters
         * in this string correspond one-to-one with the characters returned by
         * get_character(n).
         */
        """
        pass

    def getProperties(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_properties(TextAssembler self)
        get_properties(TextAssembler self, int n)
        get_properties(TextAssembler self, int r, int c)
        
        /**
         * Returns the default TextProperties that are applied to the text in the
         * absence of any nested property change sequences.
         */
        
        /**
         * Returns the TextProperties in effect for the object at the indicated
         * position in the pre-wordwrapped string.
         */
        
        /**
         * Returns the TextProperties in effect for the object at the indicated
         * position in the indicated row.
         */
        """
        pass

    def getUl(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_ul(TextAssembler self)
        
        /**
         * Returns the upper-left corner of the assembled text, in 2-d text
         * coordinates.
         */
        """
        pass

    def getUsageHint(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_usage_hint(TextAssembler self)
        
        /**
         * Returns the UsageHint that will be applied to generated geometry.  See
         * set_usage_hint().
         */
        """
        pass

    def getWidth(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_width(TextAssembler self, int n)
        get_width(TextAssembler self, int r, int c)
        
        /**
         * Returns the width of the character or object at the indicated position in
         * the pre-wordwrapped string.
         */
        
        /**
         * Returns the width of the character or object at the indicated position in
         * the indicated row.
         */
        """
        pass

    def getWordwrappedPlainWtext(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_wordwrapped_plain_wtext(TextAssembler self)
        
        /**
         * Returns a wstring that represents the contents of the text, with newlines
         * inserted according to the wordwrapping.  The string will contain no
         * embedded properties characters.  If there is an embedded graphic object, a
         * zero value is inserted in that position.
         *
         * This string has the same number of newline characters as get_num_rows(),
         * and the characters in this string correspond one-to-one with the characters
         * returned by get_character(r, c).
         */
        """
        pass

    def getWordwrappedWtext(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_wordwrapped_wtext(TextAssembler self)
        
        /**
         * Returns a wstring that represents the contents of the text, with newlines
         * inserted according to the wordwrapping.
         *
         * The string will contain embedded properties characters, which may not
         * exactly match the embedded properties characters of the original string,
         * but it will encode the same way.
         *
         * Embedded properties characters will be closed before every newline, then
         * reopened (if necessary) on the subsequent character following the newline.
         * This means it will be safe to divide the text up at the newline characters
         * and treat each line as an independent piece.
         */
        """
        pass

    def getWtext(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_wtext(TextAssembler self)
        
        /**
         * Returns a wstring that represents the contents of the text.
         *
         * The string will contain embedded properties characters, which may not
         * exactly match the embedded properties characters of the original string,
         * but it will encode the same way.
         */
        """
        pass

    def getXpos(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_xpos(TextAssembler self, int r, int c)
        
        /**
         * Returns the x position of the origin of the character or graphic object at
         * the indicated position in the indicated row.
         *
         * It is legal for c to exceed the index number of the last column by 1, and
         * it is legal for r to exceed the index number of the last row by 1, if c is
         * 0.
         */
        """
        pass

    def getYpos(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_ypos(TextAssembler self, int r, int c)
        
        /**
         * Returns the y position of the origin of all of the characters or graphic
         * objects in the indicated row.
         *
         * It is legal for r to exceed the index number of the last row by 1.  The
         * value of c is presently ignored.
         */
        """
        pass

    def get_character(self, TextAssembler_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_character(TextAssembler self, int n)
        get_character(TextAssembler self, int r, int c)
        
        /**
         * Returns the character at the indicated position in the pre-wordwrapped
         * string.  If the object at this position is a graphic object instead of a
         * character, returns 0.
         */
        
        /**
         * Returns the character at the indicated position in the indicated row.  If
         * the object at this position is a graphic object instead of a character,
         * returns 0.
         */
        """
        pass

    def get_dynamic_merge(self, TextAssembler_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_dynamic_merge(TextAssembler self)
        
        /**
         * Returns the dynamic_merge flag.  See TextNode::set_flatten_flags().
         */
        """
        pass

    def get_graphic(self, TextAssembler_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_graphic(TextAssembler self, int n)
        get_graphic(TextAssembler self, int r, int c)
        
        /**
         * Returns the graphic object at the indicated position in the pre-wordwrapped
         * string.  If the object at this position is a character instead of a graphic
         * object, returns NULL.
         */
        
        /**
         * Returns the graphic object at the indicated position in the indicated row.
         * If the object at this position is a character instead of a graphic object,
         * returns NULL.
         */
        """
        pass

    def get_lr(self, TextAssembler_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_lr(TextAssembler self)
        
        /**
         * Returns the lower-right corner of the assembled text, in 2-d text
         * coordinates.
         */
        """
        pass

    def get_max_rows(self, TextAssembler_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_max_rows(TextAssembler self)
        
        /**
         * If max_rows is greater than zero, no more than max_rows will be accepted.
         * Text beyond that will be truncated.
         */
        """
        pass

    def get_multiline_mode(self, TextAssembler_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_multiline_mode(TextAssembler self)
        
        /**
         * Returns the multline_mode flag.  See TextNode::set_multiline_mode().
         */
        """
        pass

    def get_num_characters(self, TextAssembler_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_characters(TextAssembler self)
        
        /**
         * Returns the number of characters of text, before wordwrapping.
         */
        """
        pass

    def get_num_cols(self, TextAssembler_self, int_r): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_cols(TextAssembler self, int r)
        
        /**
         * Returns the number of characters and/or graphic objects in the nth row.
         */
        """
        pass

    def get_num_rows(self, TextAssembler_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_rows(TextAssembler self)
        
        /**
         * Returns the number of rows of text after it has all been wordwrapped and
         * assembled.
         */
        """
        pass

    def get_plain_wtext(self, TextAssembler_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_plain_wtext(TextAssembler self)
        
        /**
         * Returns a wstring that represents the contents of the text, without any
         * embedded properties characters.  If there is an embedded graphic object, a
         * zero value is inserted in that position.
         *
         * This string has the same length as get_num_characters(), and the characters
         * in this string correspond one-to-one with the characters returned by
         * get_character(n).
         */
        """
        pass

    def get_properties(self, TextAssembler_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_properties(TextAssembler self)
        get_properties(TextAssembler self, int n)
        get_properties(TextAssembler self, int r, int c)
        
        /**
         * Returns the default TextProperties that are applied to the text in the
         * absence of any nested property change sequences.
         */
        
        /**
         * Returns the TextProperties in effect for the object at the indicated
         * position in the pre-wordwrapped string.
         */
        
        /**
         * Returns the TextProperties in effect for the object at the indicated
         * position in the indicated row.
         */
        """
        pass

    def get_ul(self, TextAssembler_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_ul(TextAssembler self)
        
        /**
         * Returns the upper-left corner of the assembled text, in 2-d text
         * coordinates.
         */
        """
        pass

    def get_usage_hint(self, TextAssembler_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_usage_hint(TextAssembler self)
        
        /**
         * Returns the UsageHint that will be applied to generated geometry.  See
         * set_usage_hint().
         */
        """
        pass

    def get_width(self, TextAssembler_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_width(TextAssembler self, int n)
        get_width(TextAssembler self, int r, int c)
        
        /**
         * Returns the width of the character or object at the indicated position in
         * the pre-wordwrapped string.
         */
        
        /**
         * Returns the width of the character or object at the indicated position in
         * the indicated row.
         */
        """
        pass

    def get_wordwrapped_plain_wtext(self, TextAssembler_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_wordwrapped_plain_wtext(TextAssembler self)
        
        /**
         * Returns a wstring that represents the contents of the text, with newlines
         * inserted according to the wordwrapping.  The string will contain no
         * embedded properties characters.  If there is an embedded graphic object, a
         * zero value is inserted in that position.
         *
         * This string has the same number of newline characters as get_num_rows(),
         * and the characters in this string correspond one-to-one with the characters
         * returned by get_character(r, c).
         */
        """
        pass

    def get_wordwrapped_wtext(self, TextAssembler_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_wordwrapped_wtext(TextAssembler self)
        
        /**
         * Returns a wstring that represents the contents of the text, with newlines
         * inserted according to the wordwrapping.
         *
         * The string will contain embedded properties characters, which may not
         * exactly match the embedded properties characters of the original string,
         * but it will encode the same way.
         *
         * Embedded properties characters will be closed before every newline, then
         * reopened (if necessary) on the subsequent character following the newline.
         * This means it will be safe to divide the text up at the newline characters
         * and treat each line as an independent piece.
         */
        """
        pass

    def get_wtext(self, TextAssembler_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_wtext(TextAssembler self)
        
        /**
         * Returns a wstring that represents the contents of the text.
         *
         * The string will contain embedded properties characters, which may not
         * exactly match the embedded properties characters of the original string,
         * but it will encode the same way.
         */
        """
        pass

    def get_xpos(self, TextAssembler_self, int_r, int_c): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_xpos(TextAssembler self, int r, int c)
        
        /**
         * Returns the x position of the origin of the character or graphic object at
         * the indicated position in the indicated row.
         *
         * It is legal for c to exceed the index number of the last column by 1, and
         * it is legal for r to exceed the index number of the last row by 1, if c is
         * 0.
         */
        """
        pass

    def get_ypos(self, TextAssembler_self, int_r, int_c): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_ypos(TextAssembler self, int r, int c)
        
        /**
         * Returns the y position of the origin of all of the characters or graphic
         * objects in the indicated row.
         *
         * It is legal for r to exceed the index number of the last row by 1.  The
         * value of c is presently ignored.
         */
        """
        pass

    def hasCharacter(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_character(unicode char character, const TextProperties properties)
        
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
        has_exact_character(unicode char character, const TextProperties properties)
        
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

    def has_character(self, unicode_char_character, const_TextProperties_properties): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_character(unicode char character, const TextProperties properties)
        
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

    def has_exact_character(self, unicode_char_character, const_TextProperties_properties): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_exact_character(unicode char character, const TextProperties properties)
        
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

    def isWhitespace(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_whitespace(unicode char character, const TextProperties properties)
        
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

    def is_whitespace(self, unicode_char_character, const_TextProperties_properties): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_whitespace(unicode char character, const TextProperties properties)
        
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

    def setDynamicMerge(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_dynamic_merge(const TextAssembler self, bool dynamic_merge)
        
        /**
         * Sets the dynamic_merge flag.  See TextNode::set_flatten_flags().
         */
        """
        pass

    def setMaxRows(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_max_rows(const TextAssembler self, int max_rows)
        
        /**
         * If max_rows is greater than zero, no more than max_rows will be accepted.
         * Text beyond that will be truncated.
         *
         * Setting this will not truncate text immediately.  You must follow this up
         * with a call to set_wtext() to truncate the existing text.
         */
        """
        pass

    def setMultilineMode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_multiline_mode(const TextAssembler self, bool flag)
        
        /**
         * Sets the multiline mode flag.  Set the multiline mode to allow text to
         * wrap.  It defaults to true.
         */
        """
        pass

    def setProperties(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_properties(const TextAssembler self, const TextProperties properties)
        
        /**
         * Specifies the default TextProperties that are applied to the text in the
         * absence of any nested property change sequences.
         */
        """
        pass

    def setUsageHint(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_usage_hint(const TextAssembler self, int usage_hint)
        
        /**
         * Specifies the UsageHint that will be applied to generated geometry.  The
         * default is UH_static, which is probably the right setting, but if you know
         * the TextNode's geometry will have a short lifespan, it may be better to set
         * it to UH_stream.  See geomEnums.h.
         */
        """
        pass

    def setWsubstr(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_wsubstr(const TextAssembler self, unicode wtext, int start, int count)
        
        /**
         * Replaces the 'count' characters from 'start' of the current text with the
         * indicated replacement text.  If the replacement text does not have count
         * characters, the length of the string will be changed accordingly.
         *
         * The substring may include nested formatting characters, but they must be
         * self-contained and self-closed.  The formatting characters are not
         * literally saved in the internal string; they are parsed at the time of the
         * set_wsubstr() call.
         *
         * The return value is true if all the text is accepted, or false if some was
         * truncated (see set_max_rows()).
         */
        """
        pass

    def setWtext(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_wtext(const TextAssembler self, unicode wtext)
        
        /**
         * Accepts a new text string and associated properties structure, and
         * precomputes the wordwrapping layout appropriately.  After this call,
         * get_wordwrapped_wtext() and get_num_rows() can be called.
         *
         * The return value is true if all the text is accepted, or false if some was
         * truncated (see set_max_rows()).
         */
        """
        pass

    def set_dynamic_merge(self, const_TextAssembler_self, bool_dynamic_merge): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_dynamic_merge(const TextAssembler self, bool dynamic_merge)
        
        /**
         * Sets the dynamic_merge flag.  See TextNode::set_flatten_flags().
         */
        """
        pass

    def set_max_rows(self, const_TextAssembler_self, int_max_rows): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_max_rows(const TextAssembler self, int max_rows)
        
        /**
         * If max_rows is greater than zero, no more than max_rows will be accepted.
         * Text beyond that will be truncated.
         *
         * Setting this will not truncate text immediately.  You must follow this up
         * with a call to set_wtext() to truncate the existing text.
         */
        """
        pass

    def set_multiline_mode(self, const_TextAssembler_self, bool_flag): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_multiline_mode(const TextAssembler self, bool flag)
        
        /**
         * Sets the multiline mode flag.  Set the multiline mode to allow text to
         * wrap.  It defaults to true.
         */
        """
        pass

    def set_properties(self, const_TextAssembler_self, const_TextProperties_properties): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_properties(const TextAssembler self, const TextProperties properties)
        
        /**
         * Specifies the default TextProperties that are applied to the text in the
         * absence of any nested property change sequences.
         */
        """
        pass

    def set_usage_hint(self, const_TextAssembler_self, int_usage_hint): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_usage_hint(const TextAssembler self, int usage_hint)
        
        /**
         * Specifies the UsageHint that will be applied to generated geometry.  The
         * default is UH_static, which is probably the right setting, but if you know
         * the TextNode's geometry will have a short lifespan, it may be better to set
         * it to UH_stream.  See geomEnums.h.
         */
        """
        pass

    def set_wsubstr(self, const_TextAssembler_self, unicode_wtext, int_start, int_count): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_wsubstr(const TextAssembler self, unicode wtext, int start, int count)
        
        /**
         * Replaces the 'count' characters from 'start' of the current text with the
         * indicated replacement text.  If the replacement text does not have count
         * characters, the length of the string will be changed accordingly.
         *
         * The substring may include nested formatting characters, but they must be
         * self-contained and self-closed.  The formatting characters are not
         * literally saved in the internal string; they are parsed at the time of the
         * set_wsubstr() call.
         *
         * The return value is true if all the text is accepted, or false if some was
         * truncated (see set_max_rows()).
         */
        """
        pass

    def set_wtext(self, const_TextAssembler_self, unicode_wtext): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_wtext(const TextAssembler self, unicode wtext)
        
        /**
         * Accepts a new text string and associated properties structure, and
         * precomputes the wordwrapping layout appropriately.  After this call,
         * get_wordwrapped_wtext() and get_num_rows() can be called.
         *
         * The return value is true if all the text is accepted, or false if some was
         * truncated (see set_max_rows()).
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

    dynamic_merge = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    max_rows = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    multiline_mode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    properties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    usage_hint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.TextAssembler' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.TextAssembler' objects>"
        '__doc__': '/**\n * This class is not normally used directly by user code, but is used by the\n * TextNode to lay out a block of text and convert it into rows of Geoms\n * according to the TextProperties.  However, user code may take advantage of\n * it, if desired, for very low-level text operations.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.TextAssembler' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE35F200>'
        'assembleText': None, # (!) real value is "<method 'assembleText' of 'panda3d.core.TextAssembler' objects>"
        'assemble_text': None, # (!) real value is "<method 'assemble_text' of 'panda3d.core.TextAssembler' objects>"
        'assign': None, # (!) real value is "<method 'assign' of 'panda3d.core.TextAssembler' objects>"
        'calcC': None, # (!) real value is "<method 'calcC' of 'panda3d.core.TextAssembler' objects>"
        'calcIndex': None, # (!) real value is "<method 'calcIndex' of 'panda3d.core.TextAssembler' objects>"
        'calcR': None, # (!) real value is "<method 'calcR' of 'panda3d.core.TextAssembler' objects>"
        'calcWidth': None, # (!) real value is '<staticmethod(<built-in method calcWidth of type object at 0x00007FFCFE35F200>)>'
        'calc_c': None, # (!) real value is "<method 'calc_c' of 'panda3d.core.TextAssembler' objects>"
        'calc_index': None, # (!) real value is "<method 'calc_index' of 'panda3d.core.TextAssembler' objects>"
        'calc_r': None, # (!) real value is "<method 'calc_r' of 'panda3d.core.TextAssembler' objects>"
        'calc_width': None, # (!) real value is '<staticmethod(<built-in method calc_width of type object at 0x00007FFCFE35F200>)>'
        'clear': None, # (!) real value is "<method 'clear' of 'panda3d.core.TextAssembler' objects>"
        'dynamic_merge': None, # (!) real value is "<attribute 'dynamic_merge' of 'panda3d.core.TextAssembler' objects>"
        'getCharacter': None, # (!) real value is "<method 'getCharacter' of 'panda3d.core.TextAssembler' objects>"
        'getDynamicMerge': None, # (!) real value is "<method 'getDynamicMerge' of 'panda3d.core.TextAssembler' objects>"
        'getGraphic': None, # (!) real value is "<method 'getGraphic' of 'panda3d.core.TextAssembler' objects>"
        'getLr': None, # (!) real value is "<method 'getLr' of 'panda3d.core.TextAssembler' objects>"
        'getMaxRows': None, # (!) real value is "<method 'getMaxRows' of 'panda3d.core.TextAssembler' objects>"
        'getMultilineMode': None, # (!) real value is "<method 'getMultilineMode' of 'panda3d.core.TextAssembler' objects>"
        'getNumCharacters': None, # (!) real value is "<method 'getNumCharacters' of 'panda3d.core.TextAssembler' objects>"
        'getNumCols': None, # (!) real value is "<method 'getNumCols' of 'panda3d.core.TextAssembler' objects>"
        'getNumRows': None, # (!) real value is "<method 'getNumRows' of 'panda3d.core.TextAssembler' objects>"
        'getPlainWtext': None, # (!) real value is "<method 'getPlainWtext' of 'panda3d.core.TextAssembler' objects>"
        'getProperties': None, # (!) real value is "<method 'getProperties' of 'panda3d.core.TextAssembler' objects>"
        'getUl': None, # (!) real value is "<method 'getUl' of 'panda3d.core.TextAssembler' objects>"
        'getUsageHint': None, # (!) real value is "<method 'getUsageHint' of 'panda3d.core.TextAssembler' objects>"
        'getWidth': None, # (!) real value is "<method 'getWidth' of 'panda3d.core.TextAssembler' objects>"
        'getWordwrappedPlainWtext': None, # (!) real value is "<method 'getWordwrappedPlainWtext' of 'panda3d.core.TextAssembler' objects>"
        'getWordwrappedWtext': None, # (!) real value is "<method 'getWordwrappedWtext' of 'panda3d.core.TextAssembler' objects>"
        'getWtext': None, # (!) real value is "<method 'getWtext' of 'panda3d.core.TextAssembler' objects>"
        'getXpos': None, # (!) real value is "<method 'getXpos' of 'panda3d.core.TextAssembler' objects>"
        'getYpos': None, # (!) real value is "<method 'getYpos' of 'panda3d.core.TextAssembler' objects>"
        'get_character': None, # (!) real value is "<method 'get_character' of 'panda3d.core.TextAssembler' objects>"
        'get_dynamic_merge': None, # (!) real value is "<method 'get_dynamic_merge' of 'panda3d.core.TextAssembler' objects>"
        'get_graphic': None, # (!) real value is "<method 'get_graphic' of 'panda3d.core.TextAssembler' objects>"
        'get_lr': None, # (!) real value is "<method 'get_lr' of 'panda3d.core.TextAssembler' objects>"
        'get_max_rows': None, # (!) real value is "<method 'get_max_rows' of 'panda3d.core.TextAssembler' objects>"
        'get_multiline_mode': None, # (!) real value is "<method 'get_multiline_mode' of 'panda3d.core.TextAssembler' objects>"
        'get_num_characters': None, # (!) real value is "<method 'get_num_characters' of 'panda3d.core.TextAssembler' objects>"
        'get_num_cols': None, # (!) real value is "<method 'get_num_cols' of 'panda3d.core.TextAssembler' objects>"
        'get_num_rows': None, # (!) real value is "<method 'get_num_rows' of 'panda3d.core.TextAssembler' objects>"
        'get_plain_wtext': None, # (!) real value is "<method 'get_plain_wtext' of 'panda3d.core.TextAssembler' objects>"
        'get_properties': None, # (!) real value is "<method 'get_properties' of 'panda3d.core.TextAssembler' objects>"
        'get_ul': None, # (!) real value is "<method 'get_ul' of 'panda3d.core.TextAssembler' objects>"
        'get_usage_hint': None, # (!) real value is "<method 'get_usage_hint' of 'panda3d.core.TextAssembler' objects>"
        'get_width': None, # (!) real value is "<method 'get_width' of 'panda3d.core.TextAssembler' objects>"
        'get_wordwrapped_plain_wtext': None, # (!) real value is "<method 'get_wordwrapped_plain_wtext' of 'panda3d.core.TextAssembler' objects>"
        'get_wordwrapped_wtext': None, # (!) real value is "<method 'get_wordwrapped_wtext' of 'panda3d.core.TextAssembler' objects>"
        'get_wtext': None, # (!) real value is "<method 'get_wtext' of 'panda3d.core.TextAssembler' objects>"
        'get_xpos': None, # (!) real value is "<method 'get_xpos' of 'panda3d.core.TextAssembler' objects>"
        'get_ypos': None, # (!) real value is "<method 'get_ypos' of 'panda3d.core.TextAssembler' objects>"
        'hasCharacter': None, # (!) real value is '<staticmethod(<built-in method hasCharacter of type object at 0x00007FFCFE35F200>)>'
        'hasExactCharacter': None, # (!) real value is '<staticmethod(<built-in method hasExactCharacter of type object at 0x00007FFCFE35F200>)>'
        'has_character': None, # (!) real value is '<staticmethod(<built-in method has_character of type object at 0x00007FFCFE35F200>)>'
        'has_exact_character': None, # (!) real value is '<staticmethod(<built-in method has_exact_character of type object at 0x00007FFCFE35F200>)>'
        'isWhitespace': None, # (!) real value is '<staticmethod(<built-in method isWhitespace of type object at 0x00007FFCFE35F200>)>'
        'is_whitespace': None, # (!) real value is '<staticmethod(<built-in method is_whitespace of type object at 0x00007FFCFE35F200>)>'
        'max_rows': None, # (!) real value is "<attribute 'max_rows' of 'panda3d.core.TextAssembler' objects>"
        'multiline_mode': None, # (!) real value is "<attribute 'multiline_mode' of 'panda3d.core.TextAssembler' objects>"
        'properties': None, # (!) real value is "<attribute 'properties' of 'panda3d.core.TextAssembler' objects>"
        'setDynamicMerge': None, # (!) real value is "<method 'setDynamicMerge' of 'panda3d.core.TextAssembler' objects>"
        'setMaxRows': None, # (!) real value is "<method 'setMaxRows' of 'panda3d.core.TextAssembler' objects>"
        'setMultilineMode': None, # (!) real value is "<method 'setMultilineMode' of 'panda3d.core.TextAssembler' objects>"
        'setProperties': None, # (!) real value is "<method 'setProperties' of 'panda3d.core.TextAssembler' objects>"
        'setUsageHint': None, # (!) real value is "<method 'setUsageHint' of 'panda3d.core.TextAssembler' objects>"
        'setWsubstr': None, # (!) real value is "<method 'setWsubstr' of 'panda3d.core.TextAssembler' objects>"
        'setWtext': None, # (!) real value is "<method 'setWtext' of 'panda3d.core.TextAssembler' objects>"
        'set_dynamic_merge': None, # (!) real value is "<method 'set_dynamic_merge' of 'panda3d.core.TextAssembler' objects>"
        'set_max_rows': None, # (!) real value is "<method 'set_max_rows' of 'panda3d.core.TextAssembler' objects>"
        'set_multiline_mode': None, # (!) real value is "<method 'set_multiline_mode' of 'panda3d.core.TextAssembler' objects>"
        'set_properties': None, # (!) real value is "<method 'set_properties' of 'panda3d.core.TextAssembler' objects>"
        'set_usage_hint': None, # (!) real value is "<method 'set_usage_hint' of 'panda3d.core.TextAssembler' objects>"
        'set_wsubstr': None, # (!) real value is "<method 'set_wsubstr' of 'panda3d.core.TextAssembler' objects>"
        'set_wtext': None, # (!) real value is "<method 'set_wtext' of 'panda3d.core.TextAssembler' objects>"
        'usage_hint': None, # (!) real value is "<attribute 'usage_hint' of 'panda3d.core.TextAssembler' objects>"
    }


