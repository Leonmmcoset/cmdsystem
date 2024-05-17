# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class ButtonEvent(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * Records a button event of some kind.  This is either a keyboard or mouse
     * button (or some other kind of button) changing state from up to down, or
     * vice-versa, or it is a single "keystroke".
     *
     * A keystroke is different than a button event in that (a) it does not
     * necessarily correspond to a physical button on a keyboard, but might be the
     * result of a combination of buttons (e.g.  "A" is the result of shift +
     * "a"); and (b) it does not manage separate "up" and "down" events, but is
     * itself an instantaneous event.
     *
     * Normal up/down button events can be used to track the state of a particular
     * button on the keyboard, while keystroke events are best used to monitor
     * what a user is attempting to type.
     *
     * Button up/down events are defined across all the physical keys on the
     * keyboard (and other buttons for which there is a corresponding ButtonHandle
     * object), while keystroke events are defined across the entire Unicode
     * character set.
     *
     * This API should not be considered stable and may change in a future version
     * of Panda3D.
     */
    """
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

    button = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    keycode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    time = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        'TCandidate': 5,
        'TDown': 0,
        'TKeystroke': 4,
        'TMove': 6,
        'TRawDown': 7,
        'TRawUp': 8,
        'TRepeat': 3,
        'TResumeDown': 1,
        'TUp': 2,
        'T_candidate': 5,
        'T_down': 0,
        'T_keystroke': 4,
        'T_move': 6,
        'T_raw_down': 7,
        'T_raw_up': 8,
        'T_repeat': 3,
        'T_resume_down': 1,
        'T_up': 2,
        '__doc__': '/**\n * Records a button event of some kind.  This is either a keyboard or mouse\n * button (or some other kind of button) changing state from up to down, or\n * vice-versa, or it is a single "keystroke".\n *\n * A keystroke is different than a button event in that (a) it does not\n * necessarily correspond to a physical button on a keyboard, but might be the\n * result of a combination of buttons (e.g.  "A" is the result of shift +\n * "a"); and (b) it does not manage separate "up" and "down" events, but is\n * itself an instantaneous event.\n *\n * Normal up/down button events can be used to track the state of a particular\n * button on the keyboard, while keystroke events are best used to monitor\n * what a user is attempting to type.\n *\n * Button up/down events are defined across all the physical keys on the\n * keyboard (and other buttons for which there is a corresponding ButtonHandle\n * object), while keystroke events are defined across the entire Unicode\n * character set.\n *\n * This API should not be considered stable and may change in a future version\n * of Panda3D.\n */',
        '__eq__': None, # (!) real value is "<slot wrapper '__eq__' of 'panda3d.core.ButtonEvent' objects>"
        '__ge__': None, # (!) real value is "<slot wrapper '__ge__' of 'panda3d.core.ButtonEvent' objects>"
        '__gt__': None, # (!) real value is "<slot wrapper '__gt__' of 'panda3d.core.ButtonEvent' objects>"
        '__hash__': None, # (!) real value is "<slot wrapper '__hash__' of 'panda3d.core.ButtonEvent' objects>"
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.ButtonEvent' objects>"
        '__le__': None, # (!) real value is "<slot wrapper '__le__' of 'panda3d.core.ButtonEvent' objects>"
        '__lt__': None, # (!) real value is "<slot wrapper '__lt__' of 'panda3d.core.ButtonEvent' objects>"
        '__ne__': None, # (!) real value is "<slot wrapper '__ne__' of 'panda3d.core.ButtonEvent' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2F0360>'
        'button': None, # (!) real value is "<attribute 'button' of 'panda3d.core.ButtonEvent' objects>"
        'keycode': None, # (!) real value is "<attribute 'keycode' of 'panda3d.core.ButtonEvent' objects>"
        'time': None, # (!) real value is "<attribute 'time' of 'panda3d.core.ButtonEvent' objects>"
        'type': None, # (!) real value is "<attribute 'type' of 'panda3d.core.ButtonEvent' objects>"
    }
    TCandidate = 5
    TDown = 0
    TKeystroke = 4
    TMove = 6
    TRawDown = 7
    TRawUp = 8
    TRepeat = 3
    TResumeDown = 1
    TUp = 2
    T_candidate = 5
    T_down = 0
    T_keystroke = 4
    T_move = 6
    T_raw_down = 7
    T_raw_up = 8
    T_repeat = 3
    T_resume_down = 1
    T_up = 2


