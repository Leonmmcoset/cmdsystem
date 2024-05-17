# encoding: utf-8
# module panda3d.direct
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\direct.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import panda3d.core as __panda3d_core


from .CInterval import CInterval

class CMetaInterval(CInterval):
    """
    /**
     * This interval contains a list of nested intervals, each of which has its
     * own begin and end times.  Some of them may overlap and some of them may
     * not.
     */
    """
    def addCInterval(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_c_interval(const CMetaInterval self, CInterval c_interval, double rel_time, int rel_to)
        
        /**
         * Adds a new CInterval to the list.  The interval will be played when the
         * indicated time (relative to the given point) has been reached.
         *
         * The return value is the index of the def entry representing the new
         * interval.
         */
        """
        pass

    def addExtIndex(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_ext_index(const CMetaInterval self, int ext_index, str name, double duration, bool open_ended, double rel_time, int rel_to)
        
        /**
         * Adds a new external interval to the list.  This represents some object in
         * the external scripting language that has properties similar to a CInterval
         * (for instance, a Python Interval object).
         *
         * The CMetaInterval object cannot play this external interval directly, but
         * it records a placeholder for it and will ask the scripting language to play
         * it when it is time, via is_event_ready() and related methods.
         *
         * The ext_index number itself is simply a handle that the scripting language
         * makes up and associates with its interval object somehow.  The
         * CMetaInterval object does not attempt to interpret this value.
         *
         * The return value is the index of the def entry representing the new
         * interval.
         */
        """
        pass

    def add_c_interval(self, const_CMetaInterval_self, CInterval_c_interval, double_rel_time, int_rel_to): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_c_interval(const CMetaInterval self, CInterval c_interval, double rel_time, int rel_to)
        
        /**
         * Adds a new CInterval to the list.  The interval will be played when the
         * indicated time (relative to the given point) has been reached.
         *
         * The return value is the index of the def entry representing the new
         * interval.
         */
        """
        pass

    def add_ext_index(self, const_CMetaInterval_self, int_ext_index, str_name, double_duration, bool_open_ended, double_rel_time, int_rel_to): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_ext_index(const CMetaInterval self, int ext_index, str name, double duration, bool open_ended, double rel_time, int rel_to)
        
        /**
         * Adds a new external interval to the list.  This represents some object in
         * the external scripting language that has properties similar to a CInterval
         * (for instance, a Python Interval object).
         *
         * The CMetaInterval object cannot play this external interval directly, but
         * it records a placeholder for it and will ask the scripting language to play
         * it when it is time, via is_event_ready() and related methods.
         *
         * The ext_index number itself is simply a handle that the scripting language
         * makes up and associates with its interval object somehow.  The
         * CMetaInterval object does not attempt to interpret this value.
         *
         * The return value is the index of the def entry representing the new
         * interval.
         */
        """
        pass

    def clearIntervals(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_intervals(const CMetaInterval self)
        
        /**
         * Resets the list of intervals and prepares for receiving a new list.
         */
        """
        pass

    def clear_intervals(self, const_CMetaInterval_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_intervals(const CMetaInterval self)
        
        /**
         * Resets the list of intervals and prepares for receiving a new list.
         */
        """
        pass

    def getCInterval(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_c_interval(CMetaInterval self, int n)
        
        /**
         * Return the CInterval pointer associated with the nth interval definition.
         * It is only valid to call this if get_def_type(n) returns DT_c_interval.
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getDefType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_def_type(CMetaInterval self, int n)
        
        /**
         * Returns the type of the nth interval definition that has been added.
         */
        """
        pass

    def getEventIndex(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_event_index(CMetaInterval self)
        
        /**
         * If a previous call to is_event_ready() returned true, this returns the
         * index number (added via add_event_index()) of the external interval that
         * needs to be played.
         */
        """
        pass

    def getEventT(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_event_t(CMetaInterval self)
        
        /**
         * If a previous call to is_event_ready() returned true, this returns the t
         * value that should be fed to the given interval.
         */
        """
        pass

    def getEventType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_event_type(CMetaInterval self)
        
        /**
         * If a previous call to is_event_ready() returned true, this returns the type
         * of the event (initialize, step, finalize, etc.) for the given interval.
         */
        """
        pass

    def getExtIndex(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_ext_index(CMetaInterval self, int n)
        
        /**
         * Return the external interval index number associated with the nth interval
         * definition.  It is only valid to call this if get_def_type(n) returns
         * DT_ext_index.
         */
        """
        pass

    def getIntervalEndTime(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_interval_end_time(CMetaInterval self, str name)
        
        /**
         * Returns the actual end time, relative to the beginning of the interval, of
         * the child interval with the given name, if found, or -1 if the interval is
         * not found.
         */
        """
        pass

    def getIntervalStartTime(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_interval_start_time(CMetaInterval self, str name)
        
        /**
         * Returns the actual start time, relative to the beginning of the interval,
         * of the child interval with the given name, if found, or -1 if the interval
         * is not found.
         */
        """
        pass

    def getNumDefs(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_defs(CMetaInterval self)
        
        /**
         * Returns the number of interval and push/pop definitions that have been
         * added to the meta interval.
         */
        """
        pass

    def getPrecision(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_precision(CMetaInterval self)
        
        /**
         * Returns the precision with which time measurements are compared.  See
         * set_precision().
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_c_interval(self, CMetaInterval_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_c_interval(CMetaInterval self, int n)
        
        /**
         * Return the CInterval pointer associated with the nth interval definition.
         * It is only valid to call this if get_def_type(n) returns DT_c_interval.
         */
        """
        pass

    def get_def_type(self, CMetaInterval_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_def_type(CMetaInterval self, int n)
        
        /**
         * Returns the type of the nth interval definition that has been added.
         */
        """
        pass

    def get_event_index(self, CMetaInterval_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_event_index(CMetaInterval self)
        
        /**
         * If a previous call to is_event_ready() returned true, this returns the
         * index number (added via add_event_index()) of the external interval that
         * needs to be played.
         */
        """
        pass

    def get_event_t(self, CMetaInterval_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_event_t(CMetaInterval self)
        
        /**
         * If a previous call to is_event_ready() returned true, this returns the t
         * value that should be fed to the given interval.
         */
        """
        pass

    def get_event_type(self, CMetaInterval_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_event_type(CMetaInterval self)
        
        /**
         * If a previous call to is_event_ready() returned true, this returns the type
         * of the event (initialize, step, finalize, etc.) for the given interval.
         */
        """
        pass

    def get_ext_index(self, CMetaInterval_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_ext_index(CMetaInterval self, int n)
        
        /**
         * Return the external interval index number associated with the nth interval
         * definition.  It is only valid to call this if get_def_type(n) returns
         * DT_ext_index.
         */
        """
        pass

    def get_interval_end_time(self, CMetaInterval_self, str_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_interval_end_time(CMetaInterval self, str name)
        
        /**
         * Returns the actual end time, relative to the beginning of the interval, of
         * the child interval with the given name, if found, or -1 if the interval is
         * not found.
         */
        """
        pass

    def get_interval_start_time(self, CMetaInterval_self, str_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_interval_start_time(CMetaInterval self, str name)
        
        /**
         * Returns the actual start time, relative to the beginning of the interval,
         * of the child interval with the given name, if found, or -1 if the interval
         * is not found.
         */
        """
        pass

    def get_num_defs(self, CMetaInterval_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_defs(CMetaInterval self)
        
        /**
         * Returns the number of interval and push/pop definitions that have been
         * added to the meta interval.
         */
        """
        pass

    def get_precision(self, CMetaInterval_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_precision(CMetaInterval self)
        
        /**
         * Returns the precision with which time measurements are compared.  See
         * set_precision().
         */
        """
        pass

    def isEventReady(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_event_ready(const CMetaInterval self)
        
        /**
         * Returns true if a recent call to priv_initialize(), priv_step(), or
         * priv_finalize() has left some external intervals ready to play.  If this
         * returns true, call get_event_index(), get_event_t(), and pop_event() to
         * retrieve the relevant information.
         */
        """
        pass

    def is_event_ready(self, const_CMetaInterval_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_event_ready(const CMetaInterval self)
        
        /**
         * Returns true if a recent call to priv_initialize(), priv_step(), or
         * priv_finalize() has left some external intervals ready to play.  If this
         * returns true, call get_event_index(), get_event_t(), and pop_event() to
         * retrieve the relevant information.
         */
        """
        pass

    def popEvent(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        pop_event(const CMetaInterval self)
        
        /**
         * Acknowledges that the external interval on the top of the queue has been
         * extracted, and is about to be serviced by the scripting language.  This
         * prepares the interval so the next call to is_event_ready() will return
         * information about the next external interval on the queue, if any.
         */
        """
        pass

    def popLevel(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        pop_level(const CMetaInterval self, double duration)
        
        /**
         * Finishes a level marked by a previous call to push_level(), and returns to
         * the previous level.
         *
         * If the duration is not negative, it represents a phony duration to assign
         * to the level, for the purposes of sequencing later intervals.  Otherwise,
         * the level's duration is computed based on the intervals within the level.
         */
        """
        pass

    def pop_event(self, const_CMetaInterval_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        pop_event(const CMetaInterval self)
        
        /**
         * Acknowledges that the external interval on the top of the queue has been
         * extracted, and is about to be serviced by the scripting language.  This
         * prepares the interval so the next call to is_event_ready() will return
         * information about the next external interval on the queue, if any.
         */
        """
        pass

    def pop_level(self, const_CMetaInterval_self, double_duration): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        pop_level(const CMetaInterval self, double duration)
        
        /**
         * Finishes a level marked by a previous call to push_level(), and returns to
         * the previous level.
         *
         * If the duration is not negative, it represents a phony duration to assign
         * to the level, for the purposes of sequencing later intervals.  Otherwise,
         * the level's duration is computed based on the intervals within the level.
         */
        """
        pass

    def pushLevel(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        push_level(const CMetaInterval self, str name, double rel_time, int rel_to)
        
        /**
         * Marks the beginning of a nested level of child intervals.  Within the
         * nested level, a RelativeStart time of RS_level_begin refers to the start of
         * the level, and the first interval added within the level is always relative
         * to the start of the level.
         *
         * The return value is the index of the def entry created by this push.
         */
        """
        pass

    def push_level(self, const_CMetaInterval_self, str_name, double_rel_time, int_rel_to): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        push_level(const CMetaInterval self, str name, double rel_time, int rel_to)
        
        /**
         * Marks the beginning of a nested level of child intervals.  Within the
         * nested level, a RelativeStart time of RS_level_begin refers to the start of
         * the level, and the first interval added within the level is always relative
         * to the start of the level.
         *
         * The return value is the index of the def entry created by this push.
         */
        """
        pass

    def setIntervalStartTime(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_interval_start_time(const CMetaInterval self, str name, double rel_time, int rel_to)
        
        /**
         * Adjusts the start time of the child interval with the given name, if found.
         * This may be either a C++ interval added via add_c_interval(), or an
         * external interval added via add_ext_index(); the name must match exactly.
         *
         * If the interval is found, its start time is adjusted, and all subsequent
         * intervals are adjusting accordingly, and true is returned.  If a matching
         * interval is not found, nothing is changed and false is returned.
         */
        """
        pass

    def setPrecision(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_precision(const CMetaInterval self, double precision)
        
        /**
         * Indicates the precision with which time measurements are compared.  For
         * numerical accuracy, all floating-point time values are converted to integer
         * values internally by scaling by the precision factor.  The larger the
         * number given here, the smaller the delta of time that can be
         * differentiated; the limit is the maximum integer that can be represented in
         * the system.
         */
        """
        pass

    def set_interval_start_time(self, const_CMetaInterval_self, str_name, double_rel_time, int_rel_to): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_interval_start_time(const CMetaInterval self, str name, double rel_time, int rel_to)
        
        /**
         * Adjusts the start time of the child interval with the given name, if found.
         * This may be either a C++ interval added via add_c_interval(), or an
         * external interval added via add_ext_index(); the name must match exactly.
         *
         * If the interval is found, its start time is adjusted, and all subsequent
         * intervals are adjusting accordingly, and true is returned.  If a matching
         * interval is not found, nothing is changed and false is returned.
         */
        """
        pass

    def set_precision(self, const_CMetaInterval_self, double_precision): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_precision(const CMetaInterval self, double precision)
        
        /**
         * Indicates the precision with which time measurements are compared.  For
         * numerical accuracy, all floating-point time values are converted to integer
         * values internally by scaling by the precision factor.  The larger the
         * number given here, the smaller the delta of time that can be
         * differentiated; the limit is the maximum integer that can be represented in
         * the system.
         */
        """
        pass

    def timeline(self, CMetaInterval_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        timeline(CMetaInterval self, ostream out)
        
        /**
         * Outputs a list of all events in the order in which they occur.
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

    DTCInterval = 0
    DTExtIndex = 1
    DtoolClassDict = {
        'DTCInterval': 0,
        'DTExtIndex': 1,
        'DTPopLevel': 3,
        'DTPushLevel': 2,
        'DT_c_interval': 0,
        'DT_ext_index': 1,
        'DT_pop_level': 3,
        'DT_push_level': 2,
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        'RSLevelBegin': 2,
        'RSPreviousBegin': 1,
        'RSPreviousEnd': 0,
        'RS_level_begin': 2,
        'RS_previous_begin': 1,
        'RS_previous_end': 0,
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.direct.CMetaInterval' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.direct.CMetaInterval' objects>"
        '__doc__': '/**\n * This interval contains a list of nested intervals, each of which has its\n * own begin and end times.  Some of them may overlap and some of them may\n * not.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.direct.CMetaInterval' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDC68E6590>'
        'addCInterval': None, # (!) real value is "<method 'addCInterval' of 'panda3d.direct.CMetaInterval' objects>"
        'addExtIndex': None, # (!) real value is "<method 'addExtIndex' of 'panda3d.direct.CMetaInterval' objects>"
        'add_c_interval': None, # (!) real value is "<method 'add_c_interval' of 'panda3d.direct.CMetaInterval' objects>"
        'add_ext_index': None, # (!) real value is "<method 'add_ext_index' of 'panda3d.direct.CMetaInterval' objects>"
        'clearIntervals': None, # (!) real value is "<method 'clearIntervals' of 'panda3d.direct.CMetaInterval' objects>"
        'clear_intervals': None, # (!) real value is "<method 'clear_intervals' of 'panda3d.direct.CMetaInterval' objects>"
        'getCInterval': None, # (!) real value is "<method 'getCInterval' of 'panda3d.direct.CMetaInterval' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFDC68E6590>)>'
        'getDefType': None, # (!) real value is "<method 'getDefType' of 'panda3d.direct.CMetaInterval' objects>"
        'getEventIndex': None, # (!) real value is "<method 'getEventIndex' of 'panda3d.direct.CMetaInterval' objects>"
        'getEventT': None, # (!) real value is "<method 'getEventT' of 'panda3d.direct.CMetaInterval' objects>"
        'getEventType': None, # (!) real value is "<method 'getEventType' of 'panda3d.direct.CMetaInterval' objects>"
        'getExtIndex': None, # (!) real value is "<method 'getExtIndex' of 'panda3d.direct.CMetaInterval' objects>"
        'getIntervalEndTime': None, # (!) real value is "<method 'getIntervalEndTime' of 'panda3d.direct.CMetaInterval' objects>"
        'getIntervalStartTime': None, # (!) real value is "<method 'getIntervalStartTime' of 'panda3d.direct.CMetaInterval' objects>"
        'getNumDefs': None, # (!) real value is "<method 'getNumDefs' of 'panda3d.direct.CMetaInterval' objects>"
        'getPrecision': None, # (!) real value is "<method 'getPrecision' of 'panda3d.direct.CMetaInterval' objects>"
        'get_c_interval': None, # (!) real value is "<method 'get_c_interval' of 'panda3d.direct.CMetaInterval' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFDC68E6590>)>'
        'get_def_type': None, # (!) real value is "<method 'get_def_type' of 'panda3d.direct.CMetaInterval' objects>"
        'get_event_index': None, # (!) real value is "<method 'get_event_index' of 'panda3d.direct.CMetaInterval' objects>"
        'get_event_t': None, # (!) real value is "<method 'get_event_t' of 'panda3d.direct.CMetaInterval' objects>"
        'get_event_type': None, # (!) real value is "<method 'get_event_type' of 'panda3d.direct.CMetaInterval' objects>"
        'get_ext_index': None, # (!) real value is "<method 'get_ext_index' of 'panda3d.direct.CMetaInterval' objects>"
        'get_interval_end_time': None, # (!) real value is "<method 'get_interval_end_time' of 'panda3d.direct.CMetaInterval' objects>"
        'get_interval_start_time': None, # (!) real value is "<method 'get_interval_start_time' of 'panda3d.direct.CMetaInterval' objects>"
        'get_num_defs': None, # (!) real value is "<method 'get_num_defs' of 'panda3d.direct.CMetaInterval' objects>"
        'get_precision': None, # (!) real value is "<method 'get_precision' of 'panda3d.direct.CMetaInterval' objects>"
        'isEventReady': None, # (!) real value is "<method 'isEventReady' of 'panda3d.direct.CMetaInterval' objects>"
        'is_event_ready': None, # (!) real value is "<method 'is_event_ready' of 'panda3d.direct.CMetaInterval' objects>"
        'popEvent': None, # (!) real value is "<method 'popEvent' of 'panda3d.direct.CMetaInterval' objects>"
        'popLevel': None, # (!) real value is "<method 'popLevel' of 'panda3d.direct.CMetaInterval' objects>"
        'pop_event': None, # (!) real value is "<method 'pop_event' of 'panda3d.direct.CMetaInterval' objects>"
        'pop_level': None, # (!) real value is "<method 'pop_level' of 'panda3d.direct.CMetaInterval' objects>"
        'pushLevel': None, # (!) real value is "<method 'pushLevel' of 'panda3d.direct.CMetaInterval' objects>"
        'push_level': None, # (!) real value is "<method 'push_level' of 'panda3d.direct.CMetaInterval' objects>"
        'setIntervalStartTime': None, # (!) real value is "<method 'setIntervalStartTime' of 'panda3d.direct.CMetaInterval' objects>"
        'setPrecision': None, # (!) real value is "<method 'setPrecision' of 'panda3d.direct.CMetaInterval' objects>"
        'set_interval_start_time': None, # (!) real value is "<method 'set_interval_start_time' of 'panda3d.direct.CMetaInterval' objects>"
        'set_precision': None, # (!) real value is "<method 'set_precision' of 'panda3d.direct.CMetaInterval' objects>"
        'timeline': None, # (!) real value is "<method 'timeline' of 'panda3d.direct.CMetaInterval' objects>"
    }
    DTPopLevel = 3
    DTPushLevel = 2
    DT_c_interval = 0
    DT_ext_index = 1
    DT_pop_level = 3
    DT_push_level = 2
    RSLevelBegin = 2
    RSPreviousBegin = 1
    RSPreviousEnd = 0
    RS_level_begin = 2
    RS_previous_begin = 1
    RS_previous_end = 0


