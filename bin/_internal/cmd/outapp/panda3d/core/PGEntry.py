# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .PGItem import PGItem

class PGEntry(PGItem):
    """
    /**
     * This is a particular kind of PGItem that handles simple one-line or short
     * multi-line text entries, of the sort where the user can type any string.
     *
     * A PGEntry does all of its internal manipulation on a wide string, so it can
     * store the full Unicode character set.  The interface can support either the
     * wide string getters and setters, or the normal 8-bit string getters and
     * setters, which use whatever encoding method is specified by the associated
     * TextNode.
     */
    """
    def clearCursorDef(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_cursor_def(const PGEntry self)
        
        /**
         * Removes all the children from the cursor_def node, in preparation for
         * adding a new definition.
         */
        """
        pass

    def clear_cursor_def(self, const_PGEntry_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_cursor_def(const PGEntry self)
        
        /**
         * Removes all the children from the cursor_def node, in preparation for
         * adding a new definition.
         */
        """
        pass

    def getAcceptEvent(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_accept_event(PGEntry self, const ButtonHandle button)
        
        /**
         * Returns the event name that will be thrown when the entry is accepted
         * normally.
         */
        """
        pass

    def getAcceptFailedEvent(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_accept_failed_event(PGEntry self, const ButtonHandle button)
        
        /**
         * Returns the event name that will be thrown when the entry cannot accept an
         * input
         */
        """
        pass

    def getAcceptFailedPrefix(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_accept_failed_prefix()
        
        /**
         * Returns the prefix that is used to define the accept failed event for all
         * PGEntries.  This event is the concatenation of this string followed by
         * get_id().
         */
        """
        pass

    def getAcceptPrefix(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_accept_prefix()
        
        /**
         * Returns the prefix that is used to define the accept event for all
         * PGEntries.  The accept event is the concatenation of this string followed
         * by get_id().
         */
        """
        pass

    def getBlinkRate(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_blink_rate(PGEntry self)
        
        /**
         * Returns the number of times per second the cursor will blink, or 0 if the
         * cursor is not to blink.
         */
        """
        pass

    def getCandidateActive(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_candidate_active(PGEntry self)
        
        /**
         * See set_candidate_active().
         */
        """
        pass

    def getCandidateInactive(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_candidate_inactive(PGEntry self)
        
        /**
         * See set_candidate_inactive().
         */
        """
        pass

    def getCharacter(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_character(PGEntry self, int n)
        
        /**
         * Returns the character at the indicated position in the entry.  If the
         * object at this position is a graphic object instead of a character, returns
         * 0.
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getCursorDef(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_cursor_def(const PGEntry self)
        
        /**
         * Returns the Node that will be rendered to represent the cursor.  You can
         * attach suitable cursor geometry to this node.
         */
        """
        pass

    def getCursorKeysActive(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_cursor_keys_active(PGEntry self)
        
        /**
         * Returns whether the arrow keys are currently set to control movement of the
         * cursor; see set_cursor_keys_active().
         */
        """
        pass

    def getCursormoveEvent(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_cursormove_event(PGEntry self)
        
        /**
         * Returns the event name that will be thrown whenever the cursor moves
         */
        """
        pass

    def getCursormovePrefix(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_cursormove_prefix()
        
        /**
         * Returns the prefix that is used to define the cursor event for all
         * PGEntries.  The cursor event is the concatenation of this string followed
         * by get_id().
         */
        """
        pass

    def getCursorPosition(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_cursor_position(PGEntry self)
        
        /**
         * Returns the current position of the cursor.
         */
        """
        pass

    def getCursorX(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_cursor_X(PGEntry self)
        """
        pass

    def getCursorY(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_cursor_Y(PGEntry self)
        """
        pass

    def getEraseEvent(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_erase_event(PGEntry self)
        
        /**
         * Returns the event name that will be thrown whenever the user erases
         * characters in the text.
         */
        """
        pass

    def getErasePrefix(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_erase_prefix()
        
        /**
         * Returns the prefix that is used to define the erase event for all
         * PGEntries.  The erase event is the concatenation of this string followed by
         * get_id().
         */
        """
        pass

    def getGraphic(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_graphic(PGEntry self, int n)
        
        /**
         * Returns the graphic object at the indicated position in the pre-wordwrapped
         * string.  If the object at this position is a character instead of a graphic
         * object, returns NULL.
         */
        """
        pass

    def getMaxChars(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_max_chars(PGEntry self)
        
        /**
         * Returns the current maximum number of characters that may be typed into the
         * entry, or 0 if there is no limit.  See set_max_chars().
         */
        """
        pass

    def getMaxWidth(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_max_width(PGEntry self)
        
        /**
         * Returns the current maximum width of the characters that may be typed into
         * the entry, or 0 if there is no limit.  See set_max_width().
         */
        """
        pass

    def getNumCharacters(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_characters(PGEntry self)
        
        /**
         * Returns the number of characters of text in the entry.  This is the actual
         * number of visible characters, not counting implicit newlines due to
         * wordwrapping, or formatted characters for text properties changes.  If
         * there is an embedded TextGraphic object, it counts as one character.
         *
         * This is also the length of the string returned by get_plain_text().
         */
        """
        pass

    def getNumLines(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_lines(PGEntry self)
        
        /**
         * Returns the number of lines of text the PGEntry will use, if _max_width is
         * not 0.  See set_num_lines().
         */
        """
        pass

    def getObscureMode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_obscure_mode(PGEntry self)
        
        /**
         * Specifies whether obscure mode is enabled.  See set_obscure_mode().
         */
        """
        pass

    def getOverflowEvent(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_overflow_event(PGEntry self)
        
        /**
         * Returns the event name that will be thrown when too much text is attempted
         * to be entered into the PGEntry, exceeding either the limit set via
         * set_max_chars() or via set_max_width().
         */
        """
        pass

    def getOverflowMode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_overflow_mode(PGEntry self)
        
        /**
         * Specifies whether overflow mode is enabled.  See set_overflow_mode().
         */
        """
        pass

    def getOverflowPrefix(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_overflow_prefix()
        
        /**
         * Returns the prefix that is used to define the overflow event for all
         * PGEntries.  The overflow event is the concatenation of this string followed
         * by get_id().
         */
        """
        pass

    def getPlainText(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_plain_text(PGEntry self)
        
        /**
         * Returns the text currently displayed within the entry, without any embedded
         * properties characters.
         *
         * This uses the Unicode encoding currently specified for the "focus"
         * TextNode; therefore, the TextNode must exist before calling get_text().
         */
        """
        pass

    def getPlainWtext(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_plain_wtext(PGEntry self)
        
        /**
         * Returns the text currently displayed within the entry, without any embedded
         * properties characters.
         */
        """
        pass

    def getProperties(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_properties(PGEntry self, int n)
        
        /**
         * Returns the TextProperties in effect for the object at the indicated
         * position in the pre-wordwrapped string.
         */
        """
        pass

    def getText(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_text(PGEntry self)
        
        /**
         * Returns the text currently displayed within the entry.  This uses the
         * Unicode encoding currently specified for the "focus" TextNode; therefore,
         * the TextNode must exist before calling get_text().
         */
        """
        pass

    def getTextDef(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_text_def(PGEntry self, int state)
        
        /**
         * Returns the TextNode that will be used to render the text within the entry
         * when the entry is in the indicated state.  See set_text_def().
         */
        """
        pass

    def getTypeEvent(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_type_event(PGEntry self)
        
        /**
         * Returns the event name that will be thrown whenever the user extends the
         * text by typing.
         */
        """
        pass

    def getTypePrefix(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_type_prefix()
        
        /**
         * Returns the prefix that is used to define the type event for all PGEntries.
         * The type event is the concatenation of this string followed by get_id().
         */
        """
        pass

    def getWtext(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_wtext(PGEntry self)
        
        /**
         * Returns the text currently displayed within the entry.
         */
        """
        pass

    def get_accept_event(self, PGEntry_self, const_ButtonHandle_button): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_accept_event(PGEntry self, const ButtonHandle button)
        
        /**
         * Returns the event name that will be thrown when the entry is accepted
         * normally.
         */
        """
        pass

    def get_accept_failed_event(self, PGEntry_self, const_ButtonHandle_button): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_accept_failed_event(PGEntry self, const ButtonHandle button)
        
        /**
         * Returns the event name that will be thrown when the entry cannot accept an
         * input
         */
        """
        pass

    def get_accept_failed_prefix(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_accept_failed_prefix()
        
        /**
         * Returns the prefix that is used to define the accept failed event for all
         * PGEntries.  This event is the concatenation of this string followed by
         * get_id().
         */
        """
        pass

    def get_accept_prefix(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_accept_prefix()
        
        /**
         * Returns the prefix that is used to define the accept event for all
         * PGEntries.  The accept event is the concatenation of this string followed
         * by get_id().
         */
        """
        pass

    def get_blink_rate(self, PGEntry_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_blink_rate(PGEntry self)
        
        /**
         * Returns the number of times per second the cursor will blink, or 0 if the
         * cursor is not to blink.
         */
        """
        pass

    def get_candidate_active(self, PGEntry_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_candidate_active(PGEntry self)
        
        /**
         * See set_candidate_active().
         */
        """
        pass

    def get_candidate_inactive(self, PGEntry_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_candidate_inactive(PGEntry self)
        
        /**
         * See set_candidate_inactive().
         */
        """
        pass

    def get_character(self, PGEntry_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_character(PGEntry self, int n)
        
        /**
         * Returns the character at the indicated position in the entry.  If the
         * object at this position is a graphic object instead of a character, returns
         * 0.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_cursormove_event(self, PGEntry_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_cursormove_event(PGEntry self)
        
        /**
         * Returns the event name that will be thrown whenever the cursor moves
         */
        """
        pass

    def get_cursormove_prefix(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_cursormove_prefix()
        
        /**
         * Returns the prefix that is used to define the cursor event for all
         * PGEntries.  The cursor event is the concatenation of this string followed
         * by get_id().
         */
        """
        pass

    def get_cursor_def(self, const_PGEntry_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_cursor_def(const PGEntry self)
        
        /**
         * Returns the Node that will be rendered to represent the cursor.  You can
         * attach suitable cursor geometry to this node.
         */
        """
        pass

    def get_cursor_keys_active(self, PGEntry_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_cursor_keys_active(PGEntry self)
        
        /**
         * Returns whether the arrow keys are currently set to control movement of the
         * cursor; see set_cursor_keys_active().
         */
        """
        pass

    def get_cursor_position(self, PGEntry_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_cursor_position(PGEntry self)
        
        /**
         * Returns the current position of the cursor.
         */
        """
        pass

    def get_cursor_X(self, PGEntry_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_cursor_X(PGEntry self)
        """
        pass

    def get_cursor_Y(self, PGEntry_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_cursor_Y(PGEntry self)
        """
        pass

    def get_erase_event(self, PGEntry_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_erase_event(PGEntry self)
        
        /**
         * Returns the event name that will be thrown whenever the user erases
         * characters in the text.
         */
        """
        pass

    def get_erase_prefix(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_erase_prefix()
        
        /**
         * Returns the prefix that is used to define the erase event for all
         * PGEntries.  The erase event is the concatenation of this string followed by
         * get_id().
         */
        """
        pass

    def get_graphic(self, PGEntry_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_graphic(PGEntry self, int n)
        
        /**
         * Returns the graphic object at the indicated position in the pre-wordwrapped
         * string.  If the object at this position is a character instead of a graphic
         * object, returns NULL.
         */
        """
        pass

    def get_max_chars(self, PGEntry_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_max_chars(PGEntry self)
        
        /**
         * Returns the current maximum number of characters that may be typed into the
         * entry, or 0 if there is no limit.  See set_max_chars().
         */
        """
        pass

    def get_max_width(self, PGEntry_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_max_width(PGEntry self)
        
        /**
         * Returns the current maximum width of the characters that may be typed into
         * the entry, or 0 if there is no limit.  See set_max_width().
         */
        """
        pass

    def get_num_characters(self, PGEntry_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_characters(PGEntry self)
        
        /**
         * Returns the number of characters of text in the entry.  This is the actual
         * number of visible characters, not counting implicit newlines due to
         * wordwrapping, or formatted characters for text properties changes.  If
         * there is an embedded TextGraphic object, it counts as one character.
         *
         * This is also the length of the string returned by get_plain_text().
         */
        """
        pass

    def get_num_lines(self, PGEntry_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_lines(PGEntry self)
        
        /**
         * Returns the number of lines of text the PGEntry will use, if _max_width is
         * not 0.  See set_num_lines().
         */
        """
        pass

    def get_obscure_mode(self, PGEntry_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_obscure_mode(PGEntry self)
        
        /**
         * Specifies whether obscure mode is enabled.  See set_obscure_mode().
         */
        """
        pass

    def get_overflow_event(self, PGEntry_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_overflow_event(PGEntry self)
        
        /**
         * Returns the event name that will be thrown when too much text is attempted
         * to be entered into the PGEntry, exceeding either the limit set via
         * set_max_chars() or via set_max_width().
         */
        """
        pass

    def get_overflow_mode(self, PGEntry_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_overflow_mode(PGEntry self)
        
        /**
         * Specifies whether overflow mode is enabled.  See set_overflow_mode().
         */
        """
        pass

    def get_overflow_prefix(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_overflow_prefix()
        
        /**
         * Returns the prefix that is used to define the overflow event for all
         * PGEntries.  The overflow event is the concatenation of this string followed
         * by get_id().
         */
        """
        pass

    def get_plain_text(self, PGEntry_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_plain_text(PGEntry self)
        
        /**
         * Returns the text currently displayed within the entry, without any embedded
         * properties characters.
         *
         * This uses the Unicode encoding currently specified for the "focus"
         * TextNode; therefore, the TextNode must exist before calling get_text().
         */
        """
        pass

    def get_plain_wtext(self, PGEntry_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_plain_wtext(PGEntry self)
        
        /**
         * Returns the text currently displayed within the entry, without any embedded
         * properties characters.
         */
        """
        pass

    def get_properties(self, PGEntry_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_properties(PGEntry self, int n)
        
        /**
         * Returns the TextProperties in effect for the object at the indicated
         * position in the pre-wordwrapped string.
         */
        """
        pass

    def get_text(self, PGEntry_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_text(PGEntry self)
        
        /**
         * Returns the text currently displayed within the entry.  This uses the
         * Unicode encoding currently specified for the "focus" TextNode; therefore,
         * the TextNode must exist before calling get_text().
         */
        """
        pass

    def get_text_def(self, PGEntry_self, int_state): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_text_def(PGEntry self, int state)
        
        /**
         * Returns the TextNode that will be used to render the text within the entry
         * when the entry is in the indicated state.  See set_text_def().
         */
        """
        pass

    def get_type_event(self, PGEntry_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_type_event(PGEntry self)
        
        /**
         * Returns the event name that will be thrown whenever the user extends the
         * text by typing.
         */
        """
        pass

    def get_type_prefix(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_type_prefix()
        
        /**
         * Returns the prefix that is used to define the type event for all PGEntries.
         * The type event is the concatenation of this string followed by get_id().
         */
        """
        pass

    def get_wtext(self, PGEntry_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_wtext(PGEntry self)
        
        /**
         * Returns the text currently displayed within the entry.
         */
        """
        pass

    def isWtext(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_wtext(PGEntry self)
        
        /**
         * Returns true if any of the characters in the string returned by get_wtext()
         * are out of the range of an ASCII character (and, therefore, get_wtext()
         * should be called in preference to get_text()).
         */
        """
        pass

    def is_wtext(self, PGEntry_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_wtext(PGEntry self)
        
        /**
         * Returns true if any of the characters in the string returned by get_wtext()
         * are out of the range of an ASCII character (and, therefore, get_wtext()
         * should be called in preference to get_text()).
         */
        """
        pass

    def setAcceptEnabled(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_accept_enabled(const PGEntry self, bool enabled)
        
        /**
         * Sets whether the input may be accepted--use to disable submission by the
         * user
         */
        """
        pass

    def setBlinkRate(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_blink_rate(const PGEntry self, float blink_rate)
        
        /**
         * Sets the number of times per second the cursor will blink while the entry
         * has keyboard focus.
         *
         * If this is 0, the cursor does not blink, but is held steady.
         */
        """
        pass

    def setCandidateActive(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_candidate_active(const PGEntry self, str candidate_active)
        
        /**
         * Specifies the name of the TextProperties structure added to the
         * TextPropertiesManager that will be used to render candidate strings from
         * the IME, used for typing characters in east Asian languages.  Each
         * candidate string represents one possible way to interpret the sequence of
         * keys the user has just entered; it should not be considered typed yet, but
         * it is important for the user to be able to see what he is considering
         * entering.
         *
         * This particular method sets the properties for the subset of the current
         * candidate string that the user can actively scroll through.
         */
        """
        pass

    def setCandidateInactive(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_candidate_inactive(const PGEntry self, str candidate_inactive)
        
        /**
         * Specifies the name of the TextProperties structure added to the
         * TextPropertiesManager that will be used to render candidate strings from
         * the IME, used for typing characters in east Asian languages.  Each
         * candidate string represents one possible way to interpret the sequence of
         * keys the user has just entered; it should not be considered typed yet, but
         * it is important for the user to be able to see what he is considering
         * entering.
         *
         * This particular method sets the properties for the subset of the current
         * candidate string that the user is not actively scrolling through.
         */
        """
        pass

    def setCursorKeysActive(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_cursor_keys_active(const PGEntry self, bool flag)
        
        /**
         * Sets whether the arrow keys (and home/end) control movement of the cursor.
         * If true, they are active; if false, they are ignored.
         */
        """
        pass

    def setCursorPosition(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_cursor_position(const PGEntry self, int position)
        
        /**
         * Sets the current position of the cursor.  This is the position within the
         * text at which the next letter typed by the user will be inserted; normally
         * it is the same as the length of the text.
         */
        """
        pass

    def setMaxChars(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_max_chars(const PGEntry self, int max_chars)
        
        /**
         * Sets the maximum number of characters that may be typed into the entry.
         * This is a limit on the number of characters, as opposed to the width of the
         * entry; see also set_max_width().
         *
         * If this is 0, there is no limit.
         */
        """
        pass

    def setMaxWidth(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_max_width(const PGEntry self, float max_width)
        
        /**
         * Sets the maximum width of all characters that may be typed into the entry.
         * This is a limit on the width of the formatted text, not a fixed limit on
         * the number of characters; also set_max_chars().
         *
         * If this is 0, there is no limit.
         *
         * If _num_lines is more than 1, rather than being a fixed width on the whole
         * entry, this becomes instead the wordwrap width (and the width limit on the
         * entry is essentially _max_width * _num_lines).
         */
        """
        pass

    def setNumLines(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_num_lines(const PGEntry self, int num_lines)
        
        /**
         * Sets the number of lines of text the PGEntry will use.  This only has
         * meaning if _max_width is not 0; _max_width indicates the wordwrap width of
         * each line.
         */
        """
        pass

    def setObscureMode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_obscure_mode(const PGEntry self, bool flag)
        
        /**
         * Specifies whether obscure mode should be enabled.  In obscure mode, a
         * string of asterisks is displayed instead of the literal text, e.g.  for
         * entering passwords.
         *
         * In obscure mode, the width of the text is computed based on the width of
         * the string of asterisks, not on the width of the actual text.  This has
         * implications on the maximum length of text that may be entered if max_width
         * is in effect.
         */
        """
        pass

    def setOverflowMode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_overflow_mode(const PGEntry self, bool flag)
        
        /**
         * Specifies whether overflow mode should be enabled.  In overflow mode, text
         * can overflow the boundaries of the Entry element horizontally.
         *
         * Overflow mode only works when the number of lines is 1.
         */
        """
        pass

    def setText(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_text(const PGEntry self, str text)
        
        /**
         * Changes the text currently displayed within the entry.  This uses the
         * Unicode encoding currently specified for the "focus" TextNode; therefore,
         * the TextNode must exist before calling set_text().
         *
         * The return value is true if all the text is accepted, or false if some was
         * truncated (see set_max_width(), etc.).
         */
        """
        pass

    def setTextDef(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_text_def(const PGEntry self, int state, TextNode node)
        
        /**
         * Changes the TextNode that will be used to render the text within the entry
         * when the entry is in the indicated state.  The default if nothing is
         * specified is the same TextNode returned by PGItem::get_text_node().
         */
        """
        pass

    def setup(self, const_PGEntry_self, float_width, int_num_lines): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        setup(const PGEntry self, float width, int num_lines)
        
        /**
         * Sets up the entry for normal use.  The width is the maximum width of
         * characters that will be typed, and num_lines is the integer number of lines
         * of text of the entry.  Both of these together determine the size of the
         * entry, based on the TextNode in effect.
         */
        """
        pass

    def setupMinimal(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        setup_minimal(const PGEntry self, float width, int num_lines)
        
        /**
         * Sets up the entry without creating any frame or other decoration.
         */
        """
        pass

    def setup_minimal(self, const_PGEntry_self, float_width, int_num_lines): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        setup_minimal(const PGEntry self, float width, int num_lines)
        
        /**
         * Sets up the entry without creating any frame or other decoration.
         */
        """
        pass

    def setWtext(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_wtext(const PGEntry self, unicode wtext)
        
        /**
         * Changes the text currently displayed within the entry.
         *
         * The return value is true if all the text is accepted, or false if some was
         * truncated (see set_max_width(), etc.).
         */
        """
        pass

    def set_accept_enabled(self, const_PGEntry_self, bool_enabled): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_accept_enabled(const PGEntry self, bool enabled)
        
        /**
         * Sets whether the input may be accepted--use to disable submission by the
         * user
         */
        """
        pass

    def set_blink_rate(self, const_PGEntry_self, float_blink_rate): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_blink_rate(const PGEntry self, float blink_rate)
        
        /**
         * Sets the number of times per second the cursor will blink while the entry
         * has keyboard focus.
         *
         * If this is 0, the cursor does not blink, but is held steady.
         */
        """
        pass

    def set_candidate_active(self, const_PGEntry_self, str_candidate_active): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_candidate_active(const PGEntry self, str candidate_active)
        
        /**
         * Specifies the name of the TextProperties structure added to the
         * TextPropertiesManager that will be used to render candidate strings from
         * the IME, used for typing characters in east Asian languages.  Each
         * candidate string represents one possible way to interpret the sequence of
         * keys the user has just entered; it should not be considered typed yet, but
         * it is important for the user to be able to see what he is considering
         * entering.
         *
         * This particular method sets the properties for the subset of the current
         * candidate string that the user can actively scroll through.
         */
        """
        pass

    def set_candidate_inactive(self, const_PGEntry_self, str_candidate_inactive): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_candidate_inactive(const PGEntry self, str candidate_inactive)
        
        /**
         * Specifies the name of the TextProperties structure added to the
         * TextPropertiesManager that will be used to render candidate strings from
         * the IME, used for typing characters in east Asian languages.  Each
         * candidate string represents one possible way to interpret the sequence of
         * keys the user has just entered; it should not be considered typed yet, but
         * it is important for the user to be able to see what he is considering
         * entering.
         *
         * This particular method sets the properties for the subset of the current
         * candidate string that the user is not actively scrolling through.
         */
        """
        pass

    def set_cursor_keys_active(self, const_PGEntry_self, bool_flag): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_cursor_keys_active(const PGEntry self, bool flag)
        
        /**
         * Sets whether the arrow keys (and home/end) control movement of the cursor.
         * If true, they are active; if false, they are ignored.
         */
        """
        pass

    def set_cursor_position(self, const_PGEntry_self, int_position): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_cursor_position(const PGEntry self, int position)
        
        /**
         * Sets the current position of the cursor.  This is the position within the
         * text at which the next letter typed by the user will be inserted; normally
         * it is the same as the length of the text.
         */
        """
        pass

    def set_max_chars(self, const_PGEntry_self, int_max_chars): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_max_chars(const PGEntry self, int max_chars)
        
        /**
         * Sets the maximum number of characters that may be typed into the entry.
         * This is a limit on the number of characters, as opposed to the width of the
         * entry; see also set_max_width().
         *
         * If this is 0, there is no limit.
         */
        """
        pass

    def set_max_width(self, const_PGEntry_self, float_max_width): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_max_width(const PGEntry self, float max_width)
        
        /**
         * Sets the maximum width of all characters that may be typed into the entry.
         * This is a limit on the width of the formatted text, not a fixed limit on
         * the number of characters; also set_max_chars().
         *
         * If this is 0, there is no limit.
         *
         * If _num_lines is more than 1, rather than being a fixed width on the whole
         * entry, this becomes instead the wordwrap width (and the width limit on the
         * entry is essentially _max_width * _num_lines).
         */
        """
        pass

    def set_num_lines(self, const_PGEntry_self, int_num_lines): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_num_lines(const PGEntry self, int num_lines)
        
        /**
         * Sets the number of lines of text the PGEntry will use.  This only has
         * meaning if _max_width is not 0; _max_width indicates the wordwrap width of
         * each line.
         */
        """
        pass

    def set_obscure_mode(self, const_PGEntry_self, bool_flag): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_obscure_mode(const PGEntry self, bool flag)
        
        /**
         * Specifies whether obscure mode should be enabled.  In obscure mode, a
         * string of asterisks is displayed instead of the literal text, e.g.  for
         * entering passwords.
         *
         * In obscure mode, the width of the text is computed based on the width of
         * the string of asterisks, not on the width of the actual text.  This has
         * implications on the maximum length of text that may be entered if max_width
         * is in effect.
         */
        """
        pass

    def set_overflow_mode(self, const_PGEntry_self, bool_flag): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_overflow_mode(const PGEntry self, bool flag)
        
        /**
         * Specifies whether overflow mode should be enabled.  In overflow mode, text
         * can overflow the boundaries of the Entry element horizontally.
         *
         * Overflow mode only works when the number of lines is 1.
         */
        """
        pass

    def set_text(self, const_PGEntry_self, str_text): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_text(const PGEntry self, str text)
        
        /**
         * Changes the text currently displayed within the entry.  This uses the
         * Unicode encoding currently specified for the "focus" TextNode; therefore,
         * the TextNode must exist before calling set_text().
         *
         * The return value is true if all the text is accepted, or false if some was
         * truncated (see set_max_width(), etc.).
         */
        """
        pass

    def set_text_def(self, const_PGEntry_self, int_state, TextNode_node): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_text_def(const PGEntry self, int state, TextNode node)
        
        /**
         * Changes the TextNode that will be used to render the text within the entry
         * when the entry is in the indicated state.  The default if nothing is
         * specified is the same TextNode returned by PGItem::get_text_node().
         */
        """
        pass

    def set_wtext(self, const_PGEntry_self, unicode_wtext): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_wtext(const PGEntry self, unicode wtext)
        
        /**
         * Changes the text currently displayed within the entry.
         *
         * The return value is true if all the text is accepted, or false if some was
         * truncated (see set_max_width(), etc.).
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        'SFocus': 0,
        'SInactive': 2,
        'SNoFocus': 1,
        'S_focus': 0,
        'S_inactive': 2,
        'S_no_focus': 1,
        '__doc__': '/**\n * This is a particular kind of PGItem that handles simple one-line or short\n * multi-line text entries, of the sort where the user can type any string.\n *\n * A PGEntry does all of its internal manipulation on a wide string, so it can\n * store the full Unicode character set.  The interface can support either the\n * wide string getters and setters, or the normal 8-bit string getters and\n * setters, which use whatever encoding method is specified by the associated\n * TextNode.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.PGEntry' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE384540>'
        'clearCursorDef': None, # (!) real value is "<method 'clearCursorDef' of 'panda3d.core.PGEntry' objects>"
        'clear_cursor_def': None, # (!) real value is "<method 'clear_cursor_def' of 'panda3d.core.PGEntry' objects>"
        'getAcceptEvent': None, # (!) real value is "<method 'getAcceptEvent' of 'panda3d.core.PGEntry' objects>"
        'getAcceptFailedEvent': None, # (!) real value is "<method 'getAcceptFailedEvent' of 'panda3d.core.PGEntry' objects>"
        'getAcceptFailedPrefix': None, # (!) real value is '<staticmethod(<built-in method getAcceptFailedPrefix of type object at 0x00007FFCFE384540>)>'
        'getAcceptPrefix': None, # (!) real value is '<staticmethod(<built-in method getAcceptPrefix of type object at 0x00007FFCFE384540>)>'
        'getBlinkRate': None, # (!) real value is "<method 'getBlinkRate' of 'panda3d.core.PGEntry' objects>"
        'getCandidateActive': None, # (!) real value is "<method 'getCandidateActive' of 'panda3d.core.PGEntry' objects>"
        'getCandidateInactive': None, # (!) real value is "<method 'getCandidateInactive' of 'panda3d.core.PGEntry' objects>"
        'getCharacter': None, # (!) real value is "<method 'getCharacter' of 'panda3d.core.PGEntry' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE384540>)>'
        'getCursorDef': None, # (!) real value is "<method 'getCursorDef' of 'panda3d.core.PGEntry' objects>"
        'getCursorKeysActive': None, # (!) real value is "<method 'getCursorKeysActive' of 'panda3d.core.PGEntry' objects>"
        'getCursorPosition': None, # (!) real value is "<method 'getCursorPosition' of 'panda3d.core.PGEntry' objects>"
        'getCursorX': None, # (!) real value is "<method 'getCursorX' of 'panda3d.core.PGEntry' objects>"
        'getCursorY': None, # (!) real value is "<method 'getCursorY' of 'panda3d.core.PGEntry' objects>"
        'getCursormoveEvent': None, # (!) real value is "<method 'getCursormoveEvent' of 'panda3d.core.PGEntry' objects>"
        'getCursormovePrefix': None, # (!) real value is '<staticmethod(<built-in method getCursormovePrefix of type object at 0x00007FFCFE384540>)>'
        'getEraseEvent': None, # (!) real value is "<method 'getEraseEvent' of 'panda3d.core.PGEntry' objects>"
        'getErasePrefix': None, # (!) real value is '<staticmethod(<built-in method getErasePrefix of type object at 0x00007FFCFE384540>)>'
        'getGraphic': None, # (!) real value is "<method 'getGraphic' of 'panda3d.core.PGEntry' objects>"
        'getMaxChars': None, # (!) real value is "<method 'getMaxChars' of 'panda3d.core.PGEntry' objects>"
        'getMaxWidth': None, # (!) real value is "<method 'getMaxWidth' of 'panda3d.core.PGEntry' objects>"
        'getNumCharacters': None, # (!) real value is "<method 'getNumCharacters' of 'panda3d.core.PGEntry' objects>"
        'getNumLines': None, # (!) real value is "<method 'getNumLines' of 'panda3d.core.PGEntry' objects>"
        'getObscureMode': None, # (!) real value is "<method 'getObscureMode' of 'panda3d.core.PGEntry' objects>"
        'getOverflowEvent': None, # (!) real value is "<method 'getOverflowEvent' of 'panda3d.core.PGEntry' objects>"
        'getOverflowMode': None, # (!) real value is "<method 'getOverflowMode' of 'panda3d.core.PGEntry' objects>"
        'getOverflowPrefix': None, # (!) real value is '<staticmethod(<built-in method getOverflowPrefix of type object at 0x00007FFCFE384540>)>'
        'getPlainText': None, # (!) real value is "<method 'getPlainText' of 'panda3d.core.PGEntry' objects>"
        'getPlainWtext': None, # (!) real value is "<method 'getPlainWtext' of 'panda3d.core.PGEntry' objects>"
        'getProperties': None, # (!) real value is "<method 'getProperties' of 'panda3d.core.PGEntry' objects>"
        'getText': None, # (!) real value is "<method 'getText' of 'panda3d.core.PGEntry' objects>"
        'getTextDef': None, # (!) real value is "<method 'getTextDef' of 'panda3d.core.PGEntry' objects>"
        'getTypeEvent': None, # (!) real value is "<method 'getTypeEvent' of 'panda3d.core.PGEntry' objects>"
        'getTypePrefix': None, # (!) real value is '<staticmethod(<built-in method getTypePrefix of type object at 0x00007FFCFE384540>)>'
        'getWtext': None, # (!) real value is "<method 'getWtext' of 'panda3d.core.PGEntry' objects>"
        'get_accept_event': None, # (!) real value is "<method 'get_accept_event' of 'panda3d.core.PGEntry' objects>"
        'get_accept_failed_event': None, # (!) real value is "<method 'get_accept_failed_event' of 'panda3d.core.PGEntry' objects>"
        'get_accept_failed_prefix': None, # (!) real value is '<staticmethod(<built-in method get_accept_failed_prefix of type object at 0x00007FFCFE384540>)>'
        'get_accept_prefix': None, # (!) real value is '<staticmethod(<built-in method get_accept_prefix of type object at 0x00007FFCFE384540>)>'
        'get_blink_rate': None, # (!) real value is "<method 'get_blink_rate' of 'panda3d.core.PGEntry' objects>"
        'get_candidate_active': None, # (!) real value is "<method 'get_candidate_active' of 'panda3d.core.PGEntry' objects>"
        'get_candidate_inactive': None, # (!) real value is "<method 'get_candidate_inactive' of 'panda3d.core.PGEntry' objects>"
        'get_character': None, # (!) real value is "<method 'get_character' of 'panda3d.core.PGEntry' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE384540>)>'
        'get_cursor_X': None, # (!) real value is "<method 'get_cursor_X' of 'panda3d.core.PGEntry' objects>"
        'get_cursor_Y': None, # (!) real value is "<method 'get_cursor_Y' of 'panda3d.core.PGEntry' objects>"
        'get_cursor_def': None, # (!) real value is "<method 'get_cursor_def' of 'panda3d.core.PGEntry' objects>"
        'get_cursor_keys_active': None, # (!) real value is "<method 'get_cursor_keys_active' of 'panda3d.core.PGEntry' objects>"
        'get_cursor_position': None, # (!) real value is "<method 'get_cursor_position' of 'panda3d.core.PGEntry' objects>"
        'get_cursormove_event': None, # (!) real value is "<method 'get_cursormove_event' of 'panda3d.core.PGEntry' objects>"
        'get_cursormove_prefix': None, # (!) real value is '<staticmethod(<built-in method get_cursormove_prefix of type object at 0x00007FFCFE384540>)>'
        'get_erase_event': None, # (!) real value is "<method 'get_erase_event' of 'panda3d.core.PGEntry' objects>"
        'get_erase_prefix': None, # (!) real value is '<staticmethod(<built-in method get_erase_prefix of type object at 0x00007FFCFE384540>)>'
        'get_graphic': None, # (!) real value is "<method 'get_graphic' of 'panda3d.core.PGEntry' objects>"
        'get_max_chars': None, # (!) real value is "<method 'get_max_chars' of 'panda3d.core.PGEntry' objects>"
        'get_max_width': None, # (!) real value is "<method 'get_max_width' of 'panda3d.core.PGEntry' objects>"
        'get_num_characters': None, # (!) real value is "<method 'get_num_characters' of 'panda3d.core.PGEntry' objects>"
        'get_num_lines': None, # (!) real value is "<method 'get_num_lines' of 'panda3d.core.PGEntry' objects>"
        'get_obscure_mode': None, # (!) real value is "<method 'get_obscure_mode' of 'panda3d.core.PGEntry' objects>"
        'get_overflow_event': None, # (!) real value is "<method 'get_overflow_event' of 'panda3d.core.PGEntry' objects>"
        'get_overflow_mode': None, # (!) real value is "<method 'get_overflow_mode' of 'panda3d.core.PGEntry' objects>"
        'get_overflow_prefix': None, # (!) real value is '<staticmethod(<built-in method get_overflow_prefix of type object at 0x00007FFCFE384540>)>'
        'get_plain_text': None, # (!) real value is "<method 'get_plain_text' of 'panda3d.core.PGEntry' objects>"
        'get_plain_wtext': None, # (!) real value is "<method 'get_plain_wtext' of 'panda3d.core.PGEntry' objects>"
        'get_properties': None, # (!) real value is "<method 'get_properties' of 'panda3d.core.PGEntry' objects>"
        'get_text': None, # (!) real value is "<method 'get_text' of 'panda3d.core.PGEntry' objects>"
        'get_text_def': None, # (!) real value is "<method 'get_text_def' of 'panda3d.core.PGEntry' objects>"
        'get_type_event': None, # (!) real value is "<method 'get_type_event' of 'panda3d.core.PGEntry' objects>"
        'get_type_prefix': None, # (!) real value is '<staticmethod(<built-in method get_type_prefix of type object at 0x00007FFCFE384540>)>'
        'get_wtext': None, # (!) real value is "<method 'get_wtext' of 'panda3d.core.PGEntry' objects>"
        'isWtext': None, # (!) real value is "<method 'isWtext' of 'panda3d.core.PGEntry' objects>"
        'is_wtext': None, # (!) real value is "<method 'is_wtext' of 'panda3d.core.PGEntry' objects>"
        'setAcceptEnabled': None, # (!) real value is "<method 'setAcceptEnabled' of 'panda3d.core.PGEntry' objects>"
        'setBlinkRate': None, # (!) real value is "<method 'setBlinkRate' of 'panda3d.core.PGEntry' objects>"
        'setCandidateActive': None, # (!) real value is "<method 'setCandidateActive' of 'panda3d.core.PGEntry' objects>"
        'setCandidateInactive': None, # (!) real value is "<method 'setCandidateInactive' of 'panda3d.core.PGEntry' objects>"
        'setCursorKeysActive': None, # (!) real value is "<method 'setCursorKeysActive' of 'panda3d.core.PGEntry' objects>"
        'setCursorPosition': None, # (!) real value is "<method 'setCursorPosition' of 'panda3d.core.PGEntry' objects>"
        'setMaxChars': None, # (!) real value is "<method 'setMaxChars' of 'panda3d.core.PGEntry' objects>"
        'setMaxWidth': None, # (!) real value is "<method 'setMaxWidth' of 'panda3d.core.PGEntry' objects>"
        'setNumLines': None, # (!) real value is "<method 'setNumLines' of 'panda3d.core.PGEntry' objects>"
        'setObscureMode': None, # (!) real value is "<method 'setObscureMode' of 'panda3d.core.PGEntry' objects>"
        'setOverflowMode': None, # (!) real value is "<method 'setOverflowMode' of 'panda3d.core.PGEntry' objects>"
        'setText': None, # (!) real value is "<method 'setText' of 'panda3d.core.PGEntry' objects>"
        'setTextDef': None, # (!) real value is "<method 'setTextDef' of 'panda3d.core.PGEntry' objects>"
        'setWtext': None, # (!) real value is "<method 'setWtext' of 'panda3d.core.PGEntry' objects>"
        'set_accept_enabled': None, # (!) real value is "<method 'set_accept_enabled' of 'panda3d.core.PGEntry' objects>"
        'set_blink_rate': None, # (!) real value is "<method 'set_blink_rate' of 'panda3d.core.PGEntry' objects>"
        'set_candidate_active': None, # (!) real value is "<method 'set_candidate_active' of 'panda3d.core.PGEntry' objects>"
        'set_candidate_inactive': None, # (!) real value is "<method 'set_candidate_inactive' of 'panda3d.core.PGEntry' objects>"
        'set_cursor_keys_active': None, # (!) real value is "<method 'set_cursor_keys_active' of 'panda3d.core.PGEntry' objects>"
        'set_cursor_position': None, # (!) real value is "<method 'set_cursor_position' of 'panda3d.core.PGEntry' objects>"
        'set_max_chars': None, # (!) real value is "<method 'set_max_chars' of 'panda3d.core.PGEntry' objects>"
        'set_max_width': None, # (!) real value is "<method 'set_max_width' of 'panda3d.core.PGEntry' objects>"
        'set_num_lines': None, # (!) real value is "<method 'set_num_lines' of 'panda3d.core.PGEntry' objects>"
        'set_obscure_mode': None, # (!) real value is "<method 'set_obscure_mode' of 'panda3d.core.PGEntry' objects>"
        'set_overflow_mode': None, # (!) real value is "<method 'set_overflow_mode' of 'panda3d.core.PGEntry' objects>"
        'set_text': None, # (!) real value is "<method 'set_text' of 'panda3d.core.PGEntry' objects>"
        'set_text_def': None, # (!) real value is "<method 'set_text_def' of 'panda3d.core.PGEntry' objects>"
        'set_wtext': None, # (!) real value is "<method 'set_wtext' of 'panda3d.core.PGEntry' objects>"
        'setup': None, # (!) real value is "<method 'setup' of 'panda3d.core.PGEntry' objects>"
        'setupMinimal': None, # (!) real value is "<method 'setupMinimal' of 'panda3d.core.PGEntry' objects>"
        'setup_minimal': None, # (!) real value is "<method 'setup_minimal' of 'panda3d.core.PGEntry' objects>"
    }
    SFocus = 0
    SInactive = 2
    SNoFocus = 1
    S_focus = 0
    S_inactive = 2
    S_no_focus = 1


