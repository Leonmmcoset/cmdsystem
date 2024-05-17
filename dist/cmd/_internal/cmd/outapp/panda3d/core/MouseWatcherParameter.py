# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class MouseWatcherParameter(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * This is sent along as a parameter to most events generated for a region to
     * indicate the mouse and button state for the event.
     */
    """
    def getButton(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_button(MouseWatcherParameter self)
        
        /**
         * Returns the mouse or keyboard button associated with this event.  If
         * has_button(), above, returns false, this returns ButtonHandle::none().
         */
        """
        pass

    def getCandidateStringEncoded(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_candidate_string_encoded(MouseWatcherParameter self)
        get_candidate_string_encoded(MouseWatcherParameter self, int encoding)
        
        /**
         * Returns the candidate string associated with this event.  If
         * has_candidate(), above, returns false, this returns the empty string.
         */
        
        /**
         * Returns the candidate string associated with this event.  If
         * has_candidate(), above, returns false, this returns the empty string.
         */
        """
        pass

    def getCursorPos(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_cursor_pos(MouseWatcherParameter self)
        
        /**
         * Returns the position of the user's edit cursor within the candidate string.
         */
        """
        pass

    def getHighlightEnd(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_highlight_end(MouseWatcherParameter self)
        
        /**
         * Returns one more than the last highlighted character in the candidate
         * string.
         */
        """
        pass

    def getHighlightStart(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_highlight_start(MouseWatcherParameter self)
        
        /**
         * Returns the first highlighted character in the candidate string.
         */
        """
        pass

    def getKeycode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_keycode(MouseWatcherParameter self)
        
        /**
         * Returns the keycode associated with this event.  If has_keycode(), above,
         * returns false, this returns 0.
         */
        """
        pass

    def getModifierButtons(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_modifier_buttons(MouseWatcherParameter self)
        
        /**
         * Returns the set of modifier buttons that were being held down while the
         * event was generated.
         */
        """
        pass

    def getMouse(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_mouse(MouseWatcherParameter self)
        
        /**
         * Returns the mouse position at the time the event was generated, in the
         * normalized range (-1 .. 1).  It is valid to call this only if has_mouse()
         * returned true.
         */
        """
        pass

    def get_button(self, MouseWatcherParameter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_button(MouseWatcherParameter self)
        
        /**
         * Returns the mouse or keyboard button associated with this event.  If
         * has_button(), above, returns false, this returns ButtonHandle::none().
         */
        """
        pass

    def get_candidate_string_encoded(self, MouseWatcherParameter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_candidate_string_encoded(MouseWatcherParameter self)
        get_candidate_string_encoded(MouseWatcherParameter self, int encoding)
        
        /**
         * Returns the candidate string associated with this event.  If
         * has_candidate(), above, returns false, this returns the empty string.
         */
        
        /**
         * Returns the candidate string associated with this event.  If
         * has_candidate(), above, returns false, this returns the empty string.
         */
        """
        pass

    def get_cursor_pos(self, MouseWatcherParameter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_cursor_pos(MouseWatcherParameter self)
        
        /**
         * Returns the position of the user's edit cursor within the candidate string.
         */
        """
        pass

    def get_highlight_end(self, MouseWatcherParameter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_highlight_end(MouseWatcherParameter self)
        
        /**
         * Returns one more than the last highlighted character in the candidate
         * string.
         */
        """
        pass

    def get_highlight_start(self, MouseWatcherParameter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_highlight_start(MouseWatcherParameter self)
        
        /**
         * Returns the first highlighted character in the candidate string.
         */
        """
        pass

    def get_keycode(self, MouseWatcherParameter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_keycode(MouseWatcherParameter self)
        
        /**
         * Returns the keycode associated with this event.  If has_keycode(), above,
         * returns false, this returns 0.
         */
        """
        pass

    def get_modifier_buttons(self, MouseWatcherParameter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_modifier_buttons(MouseWatcherParameter self)
        
        /**
         * Returns the set of modifier buttons that were being held down while the
         * event was generated.
         */
        """
        pass

    def get_mouse(self, MouseWatcherParameter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_mouse(MouseWatcherParameter self)
        
        /**
         * Returns the mouse position at the time the event was generated, in the
         * normalized range (-1 .. 1).  It is valid to call this only if has_mouse()
         * returned true.
         */
        """
        pass

    def hasButton(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_button(MouseWatcherParameter self)
        
        /**
         * Returns true if this parameter has an associated mouse or keyboard button,
         * false otherwise.
         */
        """
        pass

    def hasCandidate(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_candidate(MouseWatcherParameter self)
        
        /**
         * Returns true if this parameter has an associated candidate string, false
         * otherwise.
         */
        """
        pass

    def hasKeycode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_keycode(MouseWatcherParameter self)
        
        /**
         * Returns true if this parameter has an associated keycode, false otherwise.
         */
        """
        pass

    def hasMouse(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_mouse(MouseWatcherParameter self)
        
        /**
         * Returns true if this parameter has an associated mouse position, false
         * otherwise.
         */
        """
        pass

    def has_button(self, MouseWatcherParameter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_button(MouseWatcherParameter self)
        
        /**
         * Returns true if this parameter has an associated mouse or keyboard button,
         * false otherwise.
         */
        """
        pass

    def has_candidate(self, MouseWatcherParameter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_candidate(MouseWatcherParameter self)
        
        /**
         * Returns true if this parameter has an associated candidate string, false
         * otherwise.
         */
        """
        pass

    def has_keycode(self, MouseWatcherParameter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_keycode(MouseWatcherParameter self)
        
        /**
         * Returns true if this parameter has an associated keycode, false otherwise.
         */
        """
        pass

    def has_mouse(self, MouseWatcherParameter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_mouse(MouseWatcherParameter self)
        
        /**
         * Returns true if this parameter has an associated mouse position, false
         * otherwise.
         */
        """
        pass

    def isKeyrepeat(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_keyrepeat(MouseWatcherParameter self)
        
        /**
         * Returns true if the button-down even was generated due to keyrepeat, or
         * false if it was an original button down.
         */
        """
        pass

    def isOutside(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_outside(MouseWatcherParameter self)
        
        /**
         * Returns true if the mouse was outside the region at the time the event was
         * generated, false otherwise.  This is only valid for "release" type events.
         */
        """
        pass

    def is_keyrepeat(self, MouseWatcherParameter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_keyrepeat(MouseWatcherParameter self)
        
        /**
         * Returns true if the button-down even was generated due to keyrepeat, or
         * false if it was an original button down.
         */
        """
        pass

    def is_outside(self, MouseWatcherParameter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_outside(MouseWatcherParameter self)
        
        /**
         * Returns true if the mouse was outside the region at the time the event was
         * generated, false otherwise.  This is only valid for "release" type events.
         */
        """
        pass

    def output(self, MouseWatcherParameter_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(MouseWatcherParameter self, ostream out)
        
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

    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * This is sent along as a parameter to most events generated for a region to\n * indicate the mouse and button state for the event.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.MouseWatcherParameter' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE366D80>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.MouseWatcherParameter' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.MouseWatcherParameter' objects>"
        'getButton': None, # (!) real value is "<method 'getButton' of 'panda3d.core.MouseWatcherParameter' objects>"
        'getCandidateStringEncoded': None, # (!) real value is "<method 'getCandidateStringEncoded' of 'panda3d.core.MouseWatcherParameter' objects>"
        'getCursorPos': None, # (!) real value is "<method 'getCursorPos' of 'panda3d.core.MouseWatcherParameter' objects>"
        'getHighlightEnd': None, # (!) real value is "<method 'getHighlightEnd' of 'panda3d.core.MouseWatcherParameter' objects>"
        'getHighlightStart': None, # (!) real value is "<method 'getHighlightStart' of 'panda3d.core.MouseWatcherParameter' objects>"
        'getKeycode': None, # (!) real value is "<method 'getKeycode' of 'panda3d.core.MouseWatcherParameter' objects>"
        'getModifierButtons': None, # (!) real value is "<method 'getModifierButtons' of 'panda3d.core.MouseWatcherParameter' objects>"
        'getMouse': None, # (!) real value is "<method 'getMouse' of 'panda3d.core.MouseWatcherParameter' objects>"
        'get_button': None, # (!) real value is "<method 'get_button' of 'panda3d.core.MouseWatcherParameter' objects>"
        'get_candidate_string_encoded': None, # (!) real value is "<method 'get_candidate_string_encoded' of 'panda3d.core.MouseWatcherParameter' objects>"
        'get_cursor_pos': None, # (!) real value is "<method 'get_cursor_pos' of 'panda3d.core.MouseWatcherParameter' objects>"
        'get_highlight_end': None, # (!) real value is "<method 'get_highlight_end' of 'panda3d.core.MouseWatcherParameter' objects>"
        'get_highlight_start': None, # (!) real value is "<method 'get_highlight_start' of 'panda3d.core.MouseWatcherParameter' objects>"
        'get_keycode': None, # (!) real value is "<method 'get_keycode' of 'panda3d.core.MouseWatcherParameter' objects>"
        'get_modifier_buttons': None, # (!) real value is "<method 'get_modifier_buttons' of 'panda3d.core.MouseWatcherParameter' objects>"
        'get_mouse': None, # (!) real value is "<method 'get_mouse' of 'panda3d.core.MouseWatcherParameter' objects>"
        'hasButton': None, # (!) real value is "<method 'hasButton' of 'panda3d.core.MouseWatcherParameter' objects>"
        'hasCandidate': None, # (!) real value is "<method 'hasCandidate' of 'panda3d.core.MouseWatcherParameter' objects>"
        'hasKeycode': None, # (!) real value is "<method 'hasKeycode' of 'panda3d.core.MouseWatcherParameter' objects>"
        'hasMouse': None, # (!) real value is "<method 'hasMouse' of 'panda3d.core.MouseWatcherParameter' objects>"
        'has_button': None, # (!) real value is "<method 'has_button' of 'panda3d.core.MouseWatcherParameter' objects>"
        'has_candidate': None, # (!) real value is "<method 'has_candidate' of 'panda3d.core.MouseWatcherParameter' objects>"
        'has_keycode': None, # (!) real value is "<method 'has_keycode' of 'panda3d.core.MouseWatcherParameter' objects>"
        'has_mouse': None, # (!) real value is "<method 'has_mouse' of 'panda3d.core.MouseWatcherParameter' objects>"
        'isKeyrepeat': None, # (!) real value is "<method 'isKeyrepeat' of 'panda3d.core.MouseWatcherParameter' objects>"
        'isOutside': None, # (!) real value is "<method 'isOutside' of 'panda3d.core.MouseWatcherParameter' objects>"
        'is_keyrepeat': None, # (!) real value is "<method 'is_keyrepeat' of 'panda3d.core.MouseWatcherParameter' objects>"
        'is_outside': None, # (!) real value is "<method 'is_outside' of 'panda3d.core.MouseWatcherParameter' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.MouseWatcherParameter' objects>"
    }


