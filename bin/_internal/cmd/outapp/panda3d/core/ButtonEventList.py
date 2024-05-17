# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .ParamValueBase import ParamValueBase

class ButtonEventList(ParamValueBase):
    """
    /**
     * Records a set of button events that happened recently.  This class is
     * usually used only in the data graph, to transmit the recent button presses,
     * but it may be used anywhere a list of ButtonEvents is desired.
     */
    """
    def addEvent(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_event(const ButtonEventList self, ButtonEvent event)
        
        /**
         * Adds a new event to the end of the list.
         */
        """
        pass

    def addEvents(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_events(const ButtonEventList self, const ButtonEventList other)
        
        /**
         * Appends the events from the other list onto the end of this one.
         */
        """
        pass

    def add_event(self, const_ButtonEventList_self, ButtonEvent_event): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_event(const ButtonEventList self, ButtonEvent event)
        
        /**
         * Adds a new event to the end of the list.
         */
        """
        pass

    def add_events(self, const_ButtonEventList_self, const_ButtonEventList_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_events(const ButtonEventList self, const ButtonEventList other)
        
        /**
         * Appends the events from the other list onto the end of this one.
         */
        """
        pass

    def assign(self, const_ButtonEventList_self, const_ButtonEventList_copy): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        assign(const ButtonEventList self, const ButtonEventList copy)
        """
        pass

    def clear(self, const_ButtonEventList_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear(const ButtonEventList self)
        
        /**
         * Empties all the events from the list.
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getEvent(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_event(ButtonEventList self, int n)
        
        /**
         * Returns the nth event in the list.  This does not remove the event from the
         * list; the only way to remove events is to empty the whole list with
         * clear().
         */
        """
        pass

    def getNumEvents(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_events(ButtonEventList self)
        
        /**
         * Returns the number of events in the list.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_event(self, ButtonEventList_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_event(ButtonEventList self, int n)
        
        /**
         * Returns the nth event in the list.  This does not remove the event from the
         * list; the only way to remove events is to empty the whole list with
         * clear().
         */
        """
        pass

    def get_num_events(self, ButtonEventList_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_events(ButtonEventList self)
        
        /**
         * Returns the number of events in the list.
         */
        """
        pass

    def updateMods(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        update_mods(ButtonEventList self, ModifierButtons mods)
        
        /**
         * Updates the indicated ModifierButtons object with all of the button up/down
         * transitions indicated in the list.
         */
        """
        pass

    def update_mods(self, ButtonEventList_self, ModifierButtons_mods): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        update_mods(ButtonEventList self, ModifierButtons mods)
        
        /**
         * Updates the indicated ModifierButtons object with all of the button up/down
         * transitions indicated in the list.
         */
        """
        pass

    def write(self, ButtonEventList_self, ostream_out, int_indent_level): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(ButtonEventList self, ostream out, int indent_level)
        
        /**
         *
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

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    events = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.ButtonEventList' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.ButtonEventList' objects>"
        '__doc__': '/**\n * Records a set of button events that happened recently.  This class is\n * usually used only in the data graph, to transmit the recent button presses,\n * but it may be used anywhere a list of ButtonEvents is desired.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.ButtonEventList' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2F0530>'
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.ButtonEventList' objects>"
        'addEvent': None, # (!) real value is "<method 'addEvent' of 'panda3d.core.ButtonEventList' objects>"
        'addEvents': None, # (!) real value is "<method 'addEvents' of 'panda3d.core.ButtonEventList' objects>"
        'add_event': None, # (!) real value is "<method 'add_event' of 'panda3d.core.ButtonEventList' objects>"
        'add_events': None, # (!) real value is "<method 'add_events' of 'panda3d.core.ButtonEventList' objects>"
        'assign': None, # (!) real value is "<method 'assign' of 'panda3d.core.ButtonEventList' objects>"
        'clear': None, # (!) real value is "<method 'clear' of 'panda3d.core.ButtonEventList' objects>"
        'events': None, # (!) real value is "<attribute 'events' of 'panda3d.core.ButtonEventList' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2F0530>)>'
        'getEvent': None, # (!) real value is "<method 'getEvent' of 'panda3d.core.ButtonEventList' objects>"
        'getNumEvents': None, # (!) real value is "<method 'getNumEvents' of 'panda3d.core.ButtonEventList' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2F0530>)>'
        'get_event': None, # (!) real value is "<method 'get_event' of 'panda3d.core.ButtonEventList' objects>"
        'get_num_events': None, # (!) real value is "<method 'get_num_events' of 'panda3d.core.ButtonEventList' objects>"
        'updateMods': None, # (!) real value is "<method 'updateMods' of 'panda3d.core.ButtonEventList' objects>"
        'update_mods': None, # (!) real value is "<method 'update_mods' of 'panda3d.core.ButtonEventList' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.core.ButtonEventList' objects>"
    }


