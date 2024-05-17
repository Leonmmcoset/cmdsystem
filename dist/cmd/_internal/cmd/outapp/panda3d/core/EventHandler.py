# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .TypedObject import TypedObject

class EventHandler(TypedObject):
    """
    /**
     * A class to monitor events from the C++ side of things.  It maintains a set
     * of "hooks", function pointers assigned to event names, and calls the
     * appropriate hooks when the matching event is detected.
     *
     * This class is not necessary when the hooks are detected and processed
     * entirely by the scripting language, e.g.  via Scheme hooks or the messenger
     * in Python.
     */
    """
    def dispatchEvent(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        dispatch_event(const EventHandler self, const Event event)
        
        /**
         * Calls the hooks assigned to the indicated single event.
         */
        """
        pass

    def dispatch_event(self, const_EventHandler_self, const_Event_event): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        dispatch_event(const EventHandler self, const Event event)
        
        /**
         * Calls the hooks assigned to the indicated single event.
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getFuture(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_future(const EventHandler self, str event_name)
        
        /**
         * Returns a pending future that will be marked as done when the event is next
         * fired.
         */
        """
        pass

    def getGlobalEventHandler(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_global_event_handler(EventQueue queue)
        
        /**
         * Returns a pointer to the one global EventHandler object.  If the global
         * object has not yet been created, this will create it.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_future(self, const_EventHandler_self, str_event_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_future(const EventHandler self, str event_name)
        
        /**
         * Returns a pending future that will be marked as done when the event is next
         * fired.
         */
        """
        pass

    def get_global_event_handler(self, EventQueue_queue): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_global_event_handler(EventQueue queue)
        
        /**
         * Returns a pointer to the one global EventHandler object.  If the global
         * object has not yet been created, this will create it.
         */
        """
        pass

    def processEvents(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        process_events(const EventHandler self)
        
        /**
         * The main processing loop of the EventHandler.  This function must be called
         * periodically to service events.  Walks through each pending event and calls
         * its assigned hooks.
         */
        """
        pass

    def process_events(self, const_EventHandler_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        process_events(const EventHandler self)
        
        /**
         * The main processing loop of the EventHandler.  This function must be called
         * periodically to service events.  Walks through each pending event and calls
         * its assigned hooks.
         */
        """
        pass

    def write(self, EventHandler_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(EventHandler self, ostream out)
        
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

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * A class to monitor events from the C++ side of things.  It maintains a set\n * of "hooks", function pointers assigned to event names, and calls the\n * appropriate hooks when the matching event is detected.\n *\n * This class is not necessary when the hooks are detected and processed\n * entirely by the scripting language, e.g.  via Scheme hooks or the messenger\n * in Python.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.EventHandler' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2F08D0>'
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.EventHandler' objects>"
        'dispatchEvent': None, # (!) real value is "<method 'dispatchEvent' of 'panda3d.core.EventHandler' objects>"
        'dispatch_event': None, # (!) real value is "<method 'dispatch_event' of 'panda3d.core.EventHandler' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2F08D0>)>'
        'getFuture': None, # (!) real value is "<method 'getFuture' of 'panda3d.core.EventHandler' objects>"
        'getGlobalEventHandler': None, # (!) real value is '<staticmethod(<built-in method getGlobalEventHandler of type object at 0x00007FFCFE2F08D0>)>'
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2F08D0>)>'
        'get_future': None, # (!) real value is "<method 'get_future' of 'panda3d.core.EventHandler' objects>"
        'get_global_event_handler': None, # (!) real value is '<staticmethod(<built-in method get_global_event_handler of type object at 0x00007FFCFE2F08D0>)>'
        'processEvents': None, # (!) real value is "<method 'processEvents' of 'panda3d.core.EventHandler' objects>"
        'process_events': None, # (!) real value is "<method 'process_events' of 'panda3d.core.EventHandler' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.core.EventHandler' objects>"
    }


