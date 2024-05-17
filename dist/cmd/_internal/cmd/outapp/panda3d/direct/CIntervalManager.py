# encoding: utf-8
# module panda3d.direct
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\direct.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import panda3d.core as __panda3d_core


class CIntervalManager(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * This object holds a number of currently-playing intervals and is
     * responsible for advancing them each frame as needed.
     *
     * There is normally only one IntervalManager object in the world, and it is
     * the responsibility of the scripting language to call step() on this object
     * once each frame, and to then process the events indicated by
     * get_next_event().
     *
     * It is also possible to create multiple IntervalManager objects for special
     * needs.
     */
    """
    def addCInterval(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_c_interval(const CIntervalManager self, CInterval interval, bool external)
        
        /**
         * Adds the interval to the manager, and returns a unique index for the
         * interval.  This index will be unique among all the currently added
         * intervals, but not unique across all intervals ever added to the manager.
         * The maximum index value will never exceed the maximum number of intervals
         * added at any given time.
         *
         * If the external flag is true, the interval is understood to also be stored
         * in the scripting language data structures.  In this case, it will be
         * available for information returned by get_next_event() and
         * get_next_removal().  If external is false, the interval's index will never
         * be returned by these two functions.
         */
        """
        pass

    def add_c_interval(self, const_CIntervalManager_self, CInterval_interval, bool_external): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_c_interval(const CIntervalManager self, CInterval interval, bool external)
        
        /**
         * Adds the interval to the manager, and returns a unique index for the
         * interval.  This index will be unique among all the currently added
         * intervals, but not unique across all intervals ever added to the manager.
         * The maximum index value will never exceed the maximum number of intervals
         * added at any given time.
         *
         * If the external flag is true, the interval is understood to also be stored
         * in the scripting language data structures.  In this case, it will be
         * available for information returned by get_next_event() and
         * get_next_removal().  If external is false, the interval's index will never
         * be returned by these two functions.
         */
        """
        pass

    def findCInterval(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        find_c_interval(CIntervalManager self, str name)
        
        /**
         * Returns the index associated with the named interval, if there is such an
         * interval, or -1 if there is not.
         */
        """
        pass

    def find_c_interval(self, CIntervalManager_self, str_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        find_c_interval(CIntervalManager self, str name)
        
        /**
         * Returns the index associated with the named interval, if there is such an
         * interval, or -1 if there is not.
         */
        """
        pass

    def getCInterval(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_c_interval(CIntervalManager self, int index)
        
        /**
         * Returns the interval associated with the given index.
         */
        """
        pass

    def getEventQueue(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_event_queue(CIntervalManager self)
        
        /**
         * Returns the custom event queue to be used for throwing done events from
         * intervals as they finish.
         */
        """
        pass

    def getGlobalPtr(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_global_ptr()
        
        /**
         * Returns the pointer to the one global CIntervalManager object.
         */
        """
        pass

    def getMaxIndex(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_max_index(CIntervalManager self)
        
        /**
         * Returns one more than the largest interval index number in the manager.  If
         * you walk through all the values between (0, get_max_index()] and call
         * get_c_interval() on each number, you will retrieve all of the managed
         * intervals (and possibly a number of NULL pointers as well).
         */
        """
        pass

    def getNextEvent(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_next_event(const CIntervalManager self)
        
        /**
         * This should be called by the scripting language after each call to step().
         * It returns the index number of the next interval that has events requiring
         * servicing by the scripting language, or -1 if no more intervals have any
         * events pending.
         *
         * If this function returns something other than -1, it is the scripting
         * language's responsibility to query the indicated interval for its next
         * event via get_event_index(), and eventually pop_event().
         *
         * Then get_next_event() should be called again until it returns -1.
         */
        """
        pass

    def getNextRemoval(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_next_removal(const CIntervalManager self)
        
        /**
         * This should be called by the scripting language after each call to step().
         * It returns the index number of an interval that was recently removed, or -1
         * if no intervals were removed.
         *
         * If this returns something other than -1, the scripting language should
         * clean up its own data structures accordingly, and then call
         * get_next_removal() again.
         */
        """
        pass

    def getNumIntervals(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_intervals(CIntervalManager self)
        
        /**
         * Returns the number of currently active intervals.
         */
        """
        pass

    def get_c_interval(self, CIntervalManager_self, int_index): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_c_interval(CIntervalManager self, int index)
        
        /**
         * Returns the interval associated with the given index.
         */
        """
        pass

    def get_event_queue(self, CIntervalManager_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_event_queue(CIntervalManager self)
        
        /**
         * Returns the custom event queue to be used for throwing done events from
         * intervals as they finish.
         */
        """
        pass

    def get_global_ptr(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_global_ptr()
        
        /**
         * Returns the pointer to the one global CIntervalManager object.
         */
        """
        pass

    def get_max_index(self, CIntervalManager_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_max_index(CIntervalManager self)
        
        /**
         * Returns one more than the largest interval index number in the manager.  If
         * you walk through all the values between (0, get_max_index()] and call
         * get_c_interval() on each number, you will retrieve all of the managed
         * intervals (and possibly a number of NULL pointers as well).
         */
        """
        pass

    def get_next_event(self, const_CIntervalManager_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_next_event(const CIntervalManager self)
        
        /**
         * This should be called by the scripting language after each call to step().
         * It returns the index number of the next interval that has events requiring
         * servicing by the scripting language, or -1 if no more intervals have any
         * events pending.
         *
         * If this function returns something other than -1, it is the scripting
         * language's responsibility to query the indicated interval for its next
         * event via get_event_index(), and eventually pop_event().
         *
         * Then get_next_event() should be called again until it returns -1.
         */
        """
        pass

    def get_next_removal(self, const_CIntervalManager_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_next_removal(const CIntervalManager self)
        
        /**
         * This should be called by the scripting language after each call to step().
         * It returns the index number of an interval that was recently removed, or -1
         * if no intervals were removed.
         *
         * If this returns something other than -1, the scripting language should
         * clean up its own data structures accordingly, and then call
         * get_next_removal() again.
         */
        """
        pass

    def get_num_intervals(self, CIntervalManager_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_intervals(CIntervalManager self)
        
        /**
         * Returns the number of currently active intervals.
         */
        """
        pass

    def interrupt(self, const_CIntervalManager_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        interrupt(const CIntervalManager self)
        
        /**
         * Pauses or finishes (removes from the active queue) all intervals tagged
         * with auto_pause or auto_finish set to true.  These are intervals that
         * someone fired up but won't necessarily expect to clean up; they can be
         * interrupted at will when necessary.
         *
         * Returns the number of intervals affected.
         */
        """
        pass

    def output(self, CIntervalManager_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(CIntervalManager self, ostream out)
        
        /**
         *
         */
        """
        pass

    def removeCInterval(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_c_interval(const CIntervalManager self, int index)
        
        /**
         * Removes the indicated interval from the queue immediately.  It will not be
         * returned from get_next_removal(), and none of its pending events, if any,
         * will be returned by get_next_event().
         */
        """
        pass

    def remove_c_interval(self, const_CIntervalManager_self, int_index): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_c_interval(const CIntervalManager self, int index)
        
        /**
         * Removes the indicated interval from the queue immediately.  It will not be
         * returned from get_next_removal(), and none of its pending events, if any,
         * will be returned by get_next_event().
         */
        """
        pass

    def setEventQueue(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_event_queue(const CIntervalManager self, EventQueue event_queue)
        
        /**
         * Specifies a custom event queue to be used for throwing done events from
         * intervals as they finish.  If this is not specified, the global event queue
         * is used.
         *
         * The caller maintains ownership of the EventQueue object; it is the caller's
         * responsibility to ensure that the supplied EventQueue does not destruct
         * during the lifetime of the CIntervalManager.
         */
        """
        pass

    def set_event_queue(self, const_CIntervalManager_self, EventQueue_event_queue): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_event_queue(const CIntervalManager self, EventQueue event_queue)
        
        /**
         * Specifies a custom event queue to be used for throwing done events from
         * intervals as they finish.  If this is not specified, the global event queue
         * is used.
         *
         * The caller maintains ownership of the EventQueue object; it is the caller's
         * responsibility to ensure that the supplied EventQueue does not destruct
         * during the lifetime of the CIntervalManager.
         */
        """
        pass

    def step(self, const_CIntervalManager_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        step(const CIntervalManager self)
        
        /**
         * This should be called every frame to do the processing for all the active
         * intervals.  It will call step_play() for each interval that has been added
         * and that has not yet been removed.
         *
         * After each call to step(), the scripting language should call
         * get_next_event() and get_next_removal() repeatedly to process all the high-
         * level (e.g.  Python-interval-based) events and to manage the high-level
         * list of intervals.
         */
        """
        pass

    def write(self, CIntervalManager_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(CIntervalManager self, ostream out)
        
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
        '__doc__': '/**\n * This object holds a number of currently-playing intervals and is\n * responsible for advancing them each frame as needed.\n *\n * There is normally only one IntervalManager object in the world, and it is\n * the responsibility of the scripting language to call step() on this object\n * once each frame, and to then process the events indicated by\n * get_next_event().\n *\n * It is also possible to create multiple IntervalManager objects for special\n * needs.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.direct.CIntervalManager' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDC68E5540>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.direct.CIntervalManager' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.direct.CIntervalManager' objects>"
        'addCInterval': None, # (!) real value is "<method 'addCInterval' of 'panda3d.direct.CIntervalManager' objects>"
        'add_c_interval': None, # (!) real value is "<method 'add_c_interval' of 'panda3d.direct.CIntervalManager' objects>"
        'findCInterval': None, # (!) real value is "<method 'findCInterval' of 'panda3d.direct.CIntervalManager' objects>"
        'find_c_interval': None, # (!) real value is "<method 'find_c_interval' of 'panda3d.direct.CIntervalManager' objects>"
        'getCInterval': None, # (!) real value is "<method 'getCInterval' of 'panda3d.direct.CIntervalManager' objects>"
        'getEventQueue': None, # (!) real value is "<method 'getEventQueue' of 'panda3d.direct.CIntervalManager' objects>"
        'getGlobalPtr': None, # (!) real value is '<staticmethod(<built-in method getGlobalPtr of type object at 0x00007FFDC68E5540>)>'
        'getMaxIndex': None, # (!) real value is "<method 'getMaxIndex' of 'panda3d.direct.CIntervalManager' objects>"
        'getNextEvent': None, # (!) real value is "<method 'getNextEvent' of 'panda3d.direct.CIntervalManager' objects>"
        'getNextRemoval': None, # (!) real value is "<method 'getNextRemoval' of 'panda3d.direct.CIntervalManager' objects>"
        'getNumIntervals': None, # (!) real value is "<method 'getNumIntervals' of 'panda3d.direct.CIntervalManager' objects>"
        'get_c_interval': None, # (!) real value is "<method 'get_c_interval' of 'panda3d.direct.CIntervalManager' objects>"
        'get_event_queue': None, # (!) real value is "<method 'get_event_queue' of 'panda3d.direct.CIntervalManager' objects>"
        'get_global_ptr': None, # (!) real value is '<staticmethod(<built-in method get_global_ptr of type object at 0x00007FFDC68E5540>)>'
        'get_max_index': None, # (!) real value is "<method 'get_max_index' of 'panda3d.direct.CIntervalManager' objects>"
        'get_next_event': None, # (!) real value is "<method 'get_next_event' of 'panda3d.direct.CIntervalManager' objects>"
        'get_next_removal': None, # (!) real value is "<method 'get_next_removal' of 'panda3d.direct.CIntervalManager' objects>"
        'get_num_intervals': None, # (!) real value is "<method 'get_num_intervals' of 'panda3d.direct.CIntervalManager' objects>"
        'interrupt': None, # (!) real value is "<method 'interrupt' of 'panda3d.direct.CIntervalManager' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.direct.CIntervalManager' objects>"
        'removeCInterval': None, # (!) real value is "<method 'removeCInterval' of 'panda3d.direct.CIntervalManager' objects>"
        'remove_c_interval': None, # (!) real value is "<method 'remove_c_interval' of 'panda3d.direct.CIntervalManager' objects>"
        'setEventQueue': None, # (!) real value is "<method 'setEventQueue' of 'panda3d.direct.CIntervalManager' objects>"
        'set_event_queue': None, # (!) real value is "<method 'set_event_queue' of 'panda3d.direct.CIntervalManager' objects>"
        'step': None, # (!) real value is "<method 'step' of 'panda3d.direct.CIntervalManager' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.direct.CIntervalManager' objects>"
    }


