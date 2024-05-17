# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .PGItem import PGItem

class PGButton(PGItem):
    """
    /**
     * This is a particular kind of PGItem that is specialized to behave like a
     * normal button object.  It keeps track of its own state, and handles mouse
     * events sensibly.
     */
    """
    def addClickButton(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_click_button(const PGButton self, const ButtonHandle button)
        
        /**
         * Adds the indicated button to the set of buttons that can effectively
         * "click" the PGButton.  Normally, this is just MouseButton::one().  Returns
         * true if the button was added, or false if it was already there.
         */
        """
        pass

    def add_click_button(self, const_PGButton_self, const_ButtonHandle_button): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_click_button(const PGButton self, const ButtonHandle button)
        
        /**
         * Adds the indicated button to the set of buttons that can effectively
         * "click" the PGButton.  Normally, this is just MouseButton::one().  Returns
         * true if the button was added, or false if it was already there.
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getClickEvent(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_click_event(PGButton self, const ButtonHandle button)
        
        /**
         * Returns the event name that will be thrown when the button is clicked
         * normally.
         */
        """
        pass

    def getClickPrefix(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_click_prefix()
        
        /**
         * Returns the prefix that is used to define the click event for all
         * PGButtons.  The click event is the concatenation of this string followed by
         * get_id().
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_click_event(self, PGButton_self, const_ButtonHandle_button): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_click_event(PGButton self, const ButtonHandle button)
        
        /**
         * Returns the event name that will be thrown when the button is clicked
         * normally.
         */
        """
        pass

    def get_click_prefix(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_click_prefix()
        
        /**
         * Returns the prefix that is used to define the click event for all
         * PGButtons.  The click event is the concatenation of this string followed by
         * get_id().
         */
        """
        pass

    def hasClickButton(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_click_button(const PGButton self, const ButtonHandle button)
        
        /**
         * Returns true if the indicated button is on the set of buttons that can
         * effectively "click" the PGButton.  Normally, this is just
         * MouseButton::one().
         */
        """
        pass

    def has_click_button(self, const_PGButton_self, const_ButtonHandle_button): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_click_button(const PGButton self, const ButtonHandle button)
        
        /**
         * Returns true if the indicated button is on the set of buttons that can
         * effectively "click" the PGButton.  Normally, this is just
         * MouseButton::one().
         */
        """
        pass

    def isButtonDown(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_button_down(const PGButton self)
        
        /**
         * Returns true if the user is currently holding the mouse button down on the
         * button, false otherwise.
         */
        """
        pass

    def is_button_down(self, const_PGButton_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_button_down(const PGButton self)
        
        /**
         * Returns true if the user is currently holding the mouse button down on the
         * button, false otherwise.
         */
        """
        pass

    def removeClickButton(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_click_button(const PGButton self, const ButtonHandle button)
        
        /**
         * Removes the indicated button from the set of buttons that can effectively
         * "click" the PGButton.  Normally, this is just MouseButton::one().  Returns
         * true if the button was removed, or false if it was not in the set.
         */
        """
        pass

    def remove_click_button(self, const_PGButton_self, const_ButtonHandle_button): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_click_button(const PGButton self, const ButtonHandle button)
        
        /**
         * Removes the indicated button from the set of buttons that can effectively
         * "click" the PGButton.  Normally, this is just MouseButton::one().  Returns
         * true if the button was removed, or false if it was not in the set.
         */
        """
        pass

    def setup(self, const_PGButton_self, str_label): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        setup(const PGButton self, str label)
        setup(const PGButton self, const NodePath ready)
        setup(const PGButton self, const NodePath ready, const NodePath depressed)
        setup(const PGButton self, str label, float bevel)
        setup(const PGButton self, const NodePath ready, const NodePath depressed, const NodePath rollover)
        setup(const PGButton self, const NodePath ready, const NodePath depressed, const NodePath rollover, const NodePath inactive)
        
        /**
         * Sets up the button using the indicated NodePath as arbitrary geometry.
         */
        
        /**
         * Sets up the button using the indicated NodePath as arbitrary geometry.
         */
        
        /**
         * Sets up the button using the indicated NodePath as arbitrary geometry.
         */
        
        /**
         * Sets up the button as a default text button using the indicated label
         * string.  The TextNode defined by PGItem::get_text_node() will be used to
         * create the label geometry.  This automatically sets up the frame according
         * to the size of the text.
         */
        
        /**
         * Sets up the button using the indicated NodePath as arbitrary geometry.
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    click_prefix = 'click-'
    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        'SDepressed': 1,
        'SInactive': 3,
        'SReady': 0,
        'SRollover': 2,
        'S_depressed': 1,
        'S_inactive': 3,
        'S_ready': 0,
        'S_rollover': 2,
        '__doc__': '/**\n * This is a particular kind of PGItem that is specialized to behave like a\n * normal button object.  It keeps track of its own state, and handles mouse\n * events sensibly.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.PGButton' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE3841A0>'
        'addClickButton': None, # (!) real value is "<method 'addClickButton' of 'panda3d.core.PGButton' objects>"
        'add_click_button': None, # (!) real value is "<method 'add_click_button' of 'panda3d.core.PGButton' objects>"
        'click_prefix': None, # (!) real value is "<attribute 'click_prefix' of 'panda3d.core.PGButton'>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE3841A0>)>'
        'getClickEvent': None, # (!) real value is "<method 'getClickEvent' of 'panda3d.core.PGButton' objects>"
        'getClickPrefix': None, # (!) real value is '<staticmethod(<built-in method getClickPrefix of type object at 0x00007FFCFE3841A0>)>'
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE3841A0>)>'
        'get_click_event': None, # (!) real value is "<method 'get_click_event' of 'panda3d.core.PGButton' objects>"
        'get_click_prefix': None, # (!) real value is '<staticmethod(<built-in method get_click_prefix of type object at 0x00007FFCFE3841A0>)>'
        'hasClickButton': None, # (!) real value is "<method 'hasClickButton' of 'panda3d.core.PGButton' objects>"
        'has_click_button': None, # (!) real value is "<method 'has_click_button' of 'panda3d.core.PGButton' objects>"
        'isButtonDown': None, # (!) real value is "<method 'isButtonDown' of 'panda3d.core.PGButton' objects>"
        'is_button_down': None, # (!) real value is "<method 'is_button_down' of 'panda3d.core.PGButton' objects>"
        'removeClickButton': None, # (!) real value is "<method 'removeClickButton' of 'panda3d.core.PGButton' objects>"
        'remove_click_button': None, # (!) real value is "<method 'remove_click_button' of 'panda3d.core.PGButton' objects>"
        'setup': None, # (!) real value is "<method 'setup' of 'panda3d.core.PGButton' objects>"
    }
    SDepressed = 1
    SInactive = 3
    SReady = 0
    SRollover = 2
    S_depressed = 1
    S_inactive = 3
    S_ready = 0
    S_rollover = 2


