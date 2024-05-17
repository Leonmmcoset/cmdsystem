# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class ModifierButtons(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * This class monitors the state of a number of individual buttons and tracks
     * whether each button is known to be down or up.
     */
    """
    def addButton(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_button(const ModifierButtons self, ButtonHandle button)
        
        /**
         * Adds the indicated button to the set of buttons that will be monitored for
         * upness and downness.  Returns true if the button was added, false if it was
         * already being monitored or if too many buttons are currently being
         * monitored.
         */
        """
        pass

    def add_button(self, const_ModifierButtons_self, ButtonHandle_button): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_button(const ModifierButtons self, ButtonHandle button)
        
        /**
         * Adds the indicated button to the set of buttons that will be monitored for
         * upness and downness.  Returns true if the button was added, false if it was
         * already being monitored or if too many buttons are currently being
         * monitored.
         */
        """
        pass

    def allButtonsUp(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        all_buttons_up(const ModifierButtons self)
        
        /**
         * Marks all monitored buttons as being in the "up" state.
         */
        """
        pass

    def all_buttons_up(self, const_ModifierButtons_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        all_buttons_up(const ModifierButtons self)
        
        /**
         * Marks all monitored buttons as being in the "up" state.
         */
        """
        pass

    def assign(self, const_ModifierButtons_self, const_ModifierButtons_copy): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        assign(const ModifierButtons self, const ModifierButtons copy)
        """
        pass

    def buttonDown(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        button_down(const ModifierButtons self, ButtonHandle button)
        
        /**
         * Records that a particular button has been pressed.  If the given button is
         * one of the buttons that is currently being monitored, this will update the
         * internal state appropriately; otherwise, it will do nothing.  Returns true
         * if the button is one that was monitored, or false otherwise.
         */
        """
        pass

    def buttonUp(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        button_up(const ModifierButtons self, ButtonHandle button)
        
        /**
         * Records that a particular button has been released.  If the given button is
         * one of the buttons that is currently being monitored, this will update the
         * internal state appropriately; otherwise, it will do nothing.  Returns true
         * if the button is one that was monitored, or false otherwise.
         */
        """
        pass

    def button_down(self, const_ModifierButtons_self, ButtonHandle_button): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        button_down(const ModifierButtons self, ButtonHandle button)
        
        /**
         * Records that a particular button has been pressed.  If the given button is
         * one of the buttons that is currently being monitored, this will update the
         * internal state appropriately; otherwise, it will do nothing.  Returns true
         * if the button is one that was monitored, or false otherwise.
         */
        """
        pass

    def button_up(self, const_ModifierButtons_self, ButtonHandle_button): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        button_up(const ModifierButtons self, ButtonHandle button)
        
        /**
         * Records that a particular button has been released.  If the given button is
         * one of the buttons that is currently being monitored, this will update the
         * internal state appropriately; otherwise, it will do nothing.  Returns true
         * if the button is one that was monitored, or false otherwise.
         */
        """
        pass

    def getButton(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_button(ModifierButtons self, int index)
        
        /**
         * Returns the nth button that the ModifierButtons object is monitoring (the
         * nth button passed to add_button()).  This must be in the range 0 <= index <
         * get_num_buttons().
         */
        """
        pass

    def getButtons(self, *args, **kwargs): # real signature unknown
        pass

    def getNumButtons(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_buttons(ModifierButtons self)
        
        /**
         * Returns the number of buttons that the ModifierButtons object is monitoring
         * (e.g.  the number of buttons passed to add_button()).
         */
        """
        pass

    def getPrefix(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_prefix(ModifierButtons self)
        
        /**
         * Returns a string which can be used to prefix any button name or event name
         * with the unique set of modifier buttons currently being held.
         */
        """
        pass

    def get_button(self, ModifierButtons_self, int_index): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_button(ModifierButtons self, int index)
        
        /**
         * Returns the nth button that the ModifierButtons object is monitoring (the
         * nth button passed to add_button()).  This must be in the range 0 <= index <
         * get_num_buttons().
         */
        """
        pass

    def get_buttons(self, *args, **kwargs): # real signature unknown
        pass

    def get_num_buttons(self, ModifierButtons_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_buttons(ModifierButtons self)
        
        /**
         * Returns the number of buttons that the ModifierButtons object is monitoring
         * (e.g.  the number of buttons passed to add_button()).
         */
        """
        pass

    def get_prefix(self, ModifierButtons_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_prefix(ModifierButtons self)
        
        /**
         * Returns a string which can be used to prefix any button name or event name
         * with the unique set of modifier buttons currently being held.
         */
        """
        pass

    def hasButton(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_button(ModifierButtons self, ButtonHandle button)
        
        /**
         * Returns true if the indicated button is in the set of buttons being
         * monitored, false otherwise.
         */
        """
        pass

    def has_button(self, ModifierButtons_self, ButtonHandle_button): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_button(ModifierButtons self, ButtonHandle button)
        
        /**
         * Returns true if the indicated button is in the set of buttons being
         * monitored, false otherwise.
         */
        """
        pass

    def isAnyDown(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_any_down(ModifierButtons self)
        
        /**
         * Returns true if any of the tracked button are known to be down, or false if
         * all of them are up.
         */
        """
        pass

    def isDown(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_down(ModifierButtons self, ButtonHandle button)
        is_down(ModifierButtons self, int index)
        
        /**
         * Returns true if the indicated button is known to be down, or false if it is
         * known to be up.
         */
        
        /**
         * Returns true if the indicated button is known to be down, or false if it is
         * known to be up or if it is not in the set of buttons being tracked.
         */
        """
        pass

    def is_any_down(self, ModifierButtons_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_any_down(ModifierButtons self)
        
        /**
         * Returns true if any of the tracked button are known to be down, or false if
         * all of them are up.
         */
        """
        pass

    def is_down(self, ModifierButtons_self, ButtonHandle_button): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_down(ModifierButtons self, ButtonHandle button)
        is_down(ModifierButtons self, int index)
        
        /**
         * Returns true if the indicated button is known to be down, or false if it is
         * known to be up.
         */
        
        /**
         * Returns true if the indicated button is known to be down, or false if it is
         * known to be up or if it is not in the set of buttons being tracked.
         */
        """
        pass

    def matches(self, ModifierButtons_self, const_ModifierButtons_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        matches(ModifierButtons self, const ModifierButtons other)
        
        /**
         * Returns true if the set of buttons indicated as down by this
         * ModifierButtons object is the same set of buttons indicated as down by the
         * other ModifierButtons object.  The buttons indicated as up are not
         * relevant.
         */
        """
        pass

    def output(self, ModifierButtons_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(ModifierButtons self, ostream out)
        
        /**
         * Writes a one-line summary of the buttons known to be down.
         */
        """
        pass

    def removeButton(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_button(const ModifierButtons self, ButtonHandle button)
        
        /**
         * Removes the indicated button from the set of buttons being monitored.
         * Returns true if the button was removed, false if it was not being monitored
         * in the first place.
         *
         * Unlike the other methods, you cannot remove a button by removing its alias;
         * you have to remove exactly the button itself.
         */
        """
        pass

    def remove_button(self, const_ModifierButtons_self, ButtonHandle_button): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_button(const ModifierButtons self, ButtonHandle button)
        
        /**
         * Removes the indicated button from the set of buttons being monitored.
         * Returns true if the button was removed, false if it was not being monitored
         * in the first place.
         *
         * Unlike the other methods, you cannot remove a button by removing its alias;
         * you have to remove exactly the button itself.
         */
        """
        pass

    def setButtonList(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_button_list(const ModifierButtons self, const ModifierButtons other)
        
        /**
         * Sets the list of buttons to watch to be the same as that of the other
         * ModifierButtons object.  This makes the lists pointer equivalent (until one
         * or the other is later modified).
         *
         * This will preserve the state of any button that was on the original list
         * and is also on the new lists.  Any other buttons will get reset to the
         * default state of "up".
         */
        """
        pass

    def set_button_list(self, const_ModifierButtons_self, const_ModifierButtons_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_button_list(const ModifierButtons self, const ModifierButtons other)
        
        /**
         * Sets the list of buttons to watch to be the same as that of the other
         * ModifierButtons object.  This makes the lists pointer equivalent (until one
         * or the other is later modified).
         *
         * This will preserve the state of any button that was on the original list
         * and is also on the new lists.  Any other buttons will get reset to the
         * default state of "up".
         */
        """
        pass

    def write(self, ModifierButtons_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(ModifierButtons self, ostream out)
        
        /**
         * Writes a multi-line summary including all of the buttons being monitored
         * and which ones are known to be down.
         */
        """
        pass

    def __and__(self, *args, **kwargs): # real signature unknown
        """ Return self&value. """
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

    def __iand__(self, *args, **kwargs): # real signature unknown
        """ Return self&=value. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __ior__(self, *args, **kwargs): # real signature unknown
        """ Return self|=value. """
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

    def __or__(self, *args, **kwargs): # real signature unknown
        """ Return self|value. """
        pass

    def __rand__(self, *args, **kwargs): # real signature unknown
        """ Return value&self. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __ror__(self, *args, **kwargs): # real signature unknown
        """ Return value|self. """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    buttons = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__and__': None, # (!) real value is "<slot wrapper '__and__' of 'panda3d.core.ModifierButtons' objects>"
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.ModifierButtons' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.ModifierButtons' objects>"
        '__doc__': '/**\n * This class monitors the state of a number of individual buttons and tracks\n * whether each button is known to be down or up.\n */',
        '__eq__': None, # (!) real value is "<slot wrapper '__eq__' of 'panda3d.core.ModifierButtons' objects>"
        '__ge__': None, # (!) real value is "<slot wrapper '__ge__' of 'panda3d.core.ModifierButtons' objects>"
        '__gt__': None, # (!) real value is "<slot wrapper '__gt__' of 'panda3d.core.ModifierButtons' objects>"
        '__hash__': None, # (!) real value is "<slot wrapper '__hash__' of 'panda3d.core.ModifierButtons' objects>"
        '__iand__': None, # (!) real value is "<slot wrapper '__iand__' of 'panda3d.core.ModifierButtons' objects>"
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.ModifierButtons' objects>"
        '__ior__': None, # (!) real value is "<slot wrapper '__ior__' of 'panda3d.core.ModifierButtons' objects>"
        '__le__': None, # (!) real value is "<slot wrapper '__le__' of 'panda3d.core.ModifierButtons' objects>"
        '__lt__': None, # (!) real value is "<slot wrapper '__lt__' of 'panda3d.core.ModifierButtons' objects>"
        '__ne__': None, # (!) real value is "<slot wrapper '__ne__' of 'panda3d.core.ModifierButtons' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE3729C0>'
        '__or__': None, # (!) real value is "<slot wrapper '__or__' of 'panda3d.core.ModifierButtons' objects>"
        '__rand__': None, # (!) real value is "<slot wrapper '__rand__' of 'panda3d.core.ModifierButtons' objects>"
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.ModifierButtons' objects>"
        '__ror__': None, # (!) real value is "<slot wrapper '__ror__' of 'panda3d.core.ModifierButtons' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.ModifierButtons' objects>"
        'addButton': None, # (!) real value is "<method 'addButton' of 'panda3d.core.ModifierButtons' objects>"
        'add_button': None, # (!) real value is "<method 'add_button' of 'panda3d.core.ModifierButtons' objects>"
        'allButtonsUp': None, # (!) real value is "<method 'allButtonsUp' of 'panda3d.core.ModifierButtons' objects>"
        'all_buttons_up': None, # (!) real value is "<method 'all_buttons_up' of 'panda3d.core.ModifierButtons' objects>"
        'assign': None, # (!) real value is "<method 'assign' of 'panda3d.core.ModifierButtons' objects>"
        'buttonDown': None, # (!) real value is "<method 'buttonDown' of 'panda3d.core.ModifierButtons' objects>"
        'buttonUp': None, # (!) real value is "<method 'buttonUp' of 'panda3d.core.ModifierButtons' objects>"
        'button_down': None, # (!) real value is "<method 'button_down' of 'panda3d.core.ModifierButtons' objects>"
        'button_up': None, # (!) real value is "<method 'button_up' of 'panda3d.core.ModifierButtons' objects>"
        'buttons': None, # (!) real value is "<attribute 'buttons' of 'panda3d.core.ModifierButtons' objects>"
        'getButton': None, # (!) real value is "<method 'getButton' of 'panda3d.core.ModifierButtons' objects>"
        'getButtons': None, # (!) real value is "<method 'getButtons' of 'panda3d.core.ModifierButtons' objects>"
        'getNumButtons': None, # (!) real value is "<method 'getNumButtons' of 'panda3d.core.ModifierButtons' objects>"
        'getPrefix': None, # (!) real value is "<method 'getPrefix' of 'panda3d.core.ModifierButtons' objects>"
        'get_button': None, # (!) real value is "<method 'get_button' of 'panda3d.core.ModifierButtons' objects>"
        'get_buttons': None, # (!) real value is "<method 'get_buttons' of 'panda3d.core.ModifierButtons' objects>"
        'get_num_buttons': None, # (!) real value is "<method 'get_num_buttons' of 'panda3d.core.ModifierButtons' objects>"
        'get_prefix': None, # (!) real value is "<method 'get_prefix' of 'panda3d.core.ModifierButtons' objects>"
        'hasButton': None, # (!) real value is "<method 'hasButton' of 'panda3d.core.ModifierButtons' objects>"
        'has_button': None, # (!) real value is "<method 'has_button' of 'panda3d.core.ModifierButtons' objects>"
        'isAnyDown': None, # (!) real value is "<method 'isAnyDown' of 'panda3d.core.ModifierButtons' objects>"
        'isDown': None, # (!) real value is "<method 'isDown' of 'panda3d.core.ModifierButtons' objects>"
        'is_any_down': None, # (!) real value is "<method 'is_any_down' of 'panda3d.core.ModifierButtons' objects>"
        'is_down': None, # (!) real value is "<method 'is_down' of 'panda3d.core.ModifierButtons' objects>"
        'matches': None, # (!) real value is "<method 'matches' of 'panda3d.core.ModifierButtons' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.ModifierButtons' objects>"
        'removeButton': None, # (!) real value is "<method 'removeButton' of 'panda3d.core.ModifierButtons' objects>"
        'remove_button': None, # (!) real value is "<method 'remove_button' of 'panda3d.core.ModifierButtons' objects>"
        'setButtonList': None, # (!) real value is "<method 'setButtonList' of 'panda3d.core.ModifierButtons' objects>"
        'set_button_list': None, # (!) real value is "<method 'set_button_list' of 'panda3d.core.ModifierButtons' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.core.ModifierButtons' objects>"
    }


