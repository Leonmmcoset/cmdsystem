# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class EventQueue(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * A queue of pending events.  As events are thrown, they are added to this
     * queue; eventually, they will be extracted out again by an EventHandler and
     * processed.
     */
    """
    def clear(self, const_EventQueue_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear(const EventQueue self)
        
        /**
         * Empties all events on the queue, throwing them on the floor.
         */
        """
        pass

    def dequeueEvent(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        dequeue_event(const EventQueue self)
        
        /**
         *
         */
        """
        pass

    def dequeue_event(self, const_EventQueue_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        dequeue_event(const EventQueue self)
        
        /**
         *
         */
        """
        pass

    def getGlobalEventQueue(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_global_event_queue()
        
        /**
         * Returns a pointer to the one global EventQueue object.  If the global
         * object has not yet been created, this will create it.
         */
        """
        pass

    def get_global_event_queue(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_global_event_queue()
        
        /**
         * Returns a pointer to the one global EventQueue object.  If the global
         * object has not yet been created, this will create it.
         */
        """
        pass

    def isQueueEmpty(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_queue_empty(EventQueue self)
        
        /**
         *
         */
        """
        pass

    def isQueueFull(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_queue_full(EventQueue self)
        
        /**
         * @deprecated Always returns false; the queue can never be full.
         */
        """
        pass

    def is_queue_empty(self, EventQueue_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_queue_empty(EventQueue self)
        
        /**
         *
         */
        """
        pass

    def is_queue_full(self, EventQueue_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_queue_full(EventQueue self)
        
        /**
         * @deprecated Always returns false; the queue can never be full.
         */
        """
        pass

    def queueEvent(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        queue_event(const EventQueue self, const Event event)
        
        /**
         *
         */
        """
        pass

    def queue_event(self, const_EventQueue_self, const_Event_event): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        queue_event(const EventQueue self, const Event event)
        
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

    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * A queue of pending events.  As events are thrown, they are added to this\n * queue; eventually, they will be extracted out again by an EventHandler and\n * processed.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.EventQueue' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2F0AA0>'
        'clear': None, # (!) real value is "<method 'clear' of 'panda3d.core.EventQueue' objects>"
        'dequeueEvent': None, # (!) real value is "<method 'dequeueEvent' of 'panda3d.core.EventQueue' objects>"
        'dequeue_event': None, # (!) real value is "<method 'dequeue_event' of 'panda3d.core.EventQueue' objects>"
        'getGlobalEventQueue': None, # (!) real value is '<staticmethod(<built-in method getGlobalEventQueue of type object at 0x00007FFCFE2F0AA0>)>'
        'get_global_event_queue': None, # (!) real value is '<staticmethod(<built-in method get_global_event_queue of type object at 0x00007FFCFE2F0AA0>)>'
        'isQueueEmpty': None, # (!) real value is "<method 'isQueueEmpty' of 'panda3d.core.EventQueue' objects>"
        'isQueueFull': None, # (!) real value is "<method 'isQueueFull' of 'panda3d.core.EventQueue' objects>"
        'is_queue_empty': None, # (!) real value is "<method 'is_queue_empty' of 'panda3d.core.EventQueue' objects>"
        'is_queue_full': None, # (!) real value is "<method 'is_queue_full' of 'panda3d.core.EventQueue' objects>"
        'queueEvent': None, # (!) real value is "<method 'queueEvent' of 'panda3d.core.EventQueue' objects>"
        'queue_event': None, # (!) real value is "<method 'queue_event' of 'panda3d.core.EventQueue' objects>"
    }


