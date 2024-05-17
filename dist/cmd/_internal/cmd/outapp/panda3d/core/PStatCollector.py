# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class PStatCollector(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * A lightweight class that represents a single element that may be timed
     * and/or counted via stats.
     *
     * Collectors can be used to measure two different kinds of values: elapsed
     * time, and "other".
     *
     * To measure elapsed time, call start() and stop() as appropriate to bracket
     * the section of code you want to time (or use a PStatTimer to do this
     * automatically).
     *
     * To measure anything else, call set_level() and/or add_level() to set the
     * "level" value associated with this collector.  The meaning of the value set
     * for the "level" is entirely up to the user; it may represent the number of
     * triangles rendered or the kilobytes of texture memory consumed, for
     * instance.  The level set will remain fixed across multiple frames until it
     * is reset via another set_level() or adjusted via a call to add_level().  It
     * may also be completely removed via clear_level().
     */
    """
    def addLevel(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_level(const PStatCollector self, double increment)
        add_level(const PStatCollector self, const PStatThread thread, double increment)
        
        /**
         * Adds the indicated increment (which may be negative) to the level setting
         * associated with this collector for the main thread.  If the collector did
         * not already have a level setting for the main thread, it is initialized to
         * 0.
         *
         * As an optimization, the data is not immediately set to the PStatClient.  It
         * will be sent the next time flush_level() is called.
         */
        
        /**
         * Adds the indicated increment (which may be negative) to the level setting
         * associated with this collector for the indicated thread.  If the collector
         * did not already have a level setting for this thread, it is initialized to
         * 0.
         */
        """
        pass

    def addLevelNow(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_level_now(const PStatCollector self, double increment)
        
        /**
         * Calls add_level() and immediately calls flush_level().
         */
        """
        pass

    def addThreadLevel(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_thread_level(const PStatCollector self, double increment)
        
        /**
         * Adds the indicated increment (which may be negative) to the level setting
         * associated with this collector for the current thread.  If the collector
         * did not already have a level setting for the current thread, it is
         * initialized to 0.
         */
        """
        pass

    def add_level(self, const_PStatCollector_self, double_increment): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_level(const PStatCollector self, double increment)
        add_level(const PStatCollector self, const PStatThread thread, double increment)
        
        /**
         * Adds the indicated increment (which may be negative) to the level setting
         * associated with this collector for the main thread.  If the collector did
         * not already have a level setting for the main thread, it is initialized to
         * 0.
         *
         * As an optimization, the data is not immediately set to the PStatClient.  It
         * will be sent the next time flush_level() is called.
         */
        
        /**
         * Adds the indicated increment (which may be negative) to the level setting
         * associated with this collector for the indicated thread.  If the collector
         * did not already have a level setting for this thread, it is initialized to
         * 0.
         */
        """
        pass

    def add_level_now(self, const_PStatCollector_self, double_increment): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_level_now(const PStatCollector self, double increment)
        
        /**
         * Calls add_level() and immediately calls flush_level().
         */
        """
        pass

    def add_thread_level(self, const_PStatCollector_self, double_increment): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_thread_level(const PStatCollector self, double increment)
        
        /**
         * Adds the indicated increment (which may be negative) to the level setting
         * associated with this collector for the current thread.  If the collector
         * did not already have a level setting for the current thread, it is
         * initialized to 0.
         */
        """
        pass

    def assign(self, const_PStatCollector_self, const_PStatCollector_copy): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        assign(const PStatCollector self, const PStatCollector copy)
        """
        pass

    def clearLevel(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_level(const PStatCollector self)
        clear_level(const PStatCollector self, const PStatThread thread)
        
        /**
         * Removes the level setting associated with this collector for the main
         * thread.  The collector will no longer show up on any level graphs in the
         * main thread.  This implicitly calls flush_level().
         */
        
        /**
         * Removes the level setting associated with this collector for the indicated
         * thread.  The collector will no longer show up on any level graphs in this
         * thread.
         */
        """
        pass

    def clearThreadLevel(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_thread_level(const PStatCollector self)
        
        /**
         * Removes the level setting associated with this collector for the current
         * thread.  The collector will no longer show up on any level graphs in the
         * current thread.
         */
        """
        pass

    def clear_level(self, const_PStatCollector_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_level(const PStatCollector self)
        clear_level(const PStatCollector self, const PStatThread thread)
        
        /**
         * Removes the level setting associated with this collector for the main
         * thread.  The collector will no longer show up on any level graphs in the
         * main thread.  This implicitly calls flush_level().
         */
        
        /**
         * Removes the level setting associated with this collector for the indicated
         * thread.  The collector will no longer show up on any level graphs in this
         * thread.
         */
        """
        pass

    def clear_thread_level(self, const_PStatCollector_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_thread_level(const PStatCollector self)
        
        /**
         * Removes the level setting associated with this collector for the current
         * thread.  The collector will no longer show up on any level graphs in the
         * current thread.
         */
        """
        pass

    def flushLevel(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        flush_level(const PStatCollector self)
        
        /**
         * Updates the PStatClient with the recent results from add_level() and
         * sub_level().
         */
        """
        pass

    def flush_level(self, const_PStatCollector_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        flush_level(const PStatCollector self)
        
        /**
         * Updates the PStatClient with the recent results from add_level() and
         * sub_level().
         */
        """
        pass

    def getFullname(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_fullname(PStatCollector self)
        
        /**
         * Returns the full name of this collector.  This includes the names of all
         * the collector's parents, concatenated together with colons.
         */
        """
        pass

    def getIndex(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_index(PStatCollector self)
        
        /**
         * Returns the index number of this particular collector within the
         * PStatClient.
         */
        """
        pass

    def getLevel(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_level(const PStatCollector self)
        get_level(const PStatCollector self, const PStatThread thread)
        
        /**
         * Returns the current level value of the given collector in the main thread.
         * This implicitly calls flush_level().
         */
        
        /**
         * Returns the current level value of the given collector.
         */
        """
        pass

    def getName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_name(PStatCollector self)
        
        /**
         * Returns the local name of this collector.  This is the rightmost part of
         * the fullname, after the rightmost colon.
         */
        """
        pass

    def getThreadLevel(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_thread_level(const PStatCollector self)
        
        /**
         * Returns the current level value of the given collector in the current
         * thread.
         */
        """
        pass

    def get_fullname(self, PStatCollector_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_fullname(PStatCollector self)
        
        /**
         * Returns the full name of this collector.  This includes the names of all
         * the collector's parents, concatenated together with colons.
         */
        """
        pass

    def get_index(self, PStatCollector_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_index(PStatCollector self)
        
        /**
         * Returns the index number of this particular collector within the
         * PStatClient.
         */
        """
        pass

    def get_level(self, const_PStatCollector_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_level(const PStatCollector self)
        get_level(const PStatCollector self, const PStatThread thread)
        
        /**
         * Returns the current level value of the given collector in the main thread.
         * This implicitly calls flush_level().
         */
        
        /**
         * Returns the current level value of the given collector.
         */
        """
        pass

    def get_name(self, PStatCollector_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_name(PStatCollector self)
        
        /**
         * Returns the local name of this collector.  This is the rightmost part of
         * the fullname, after the rightmost colon.
         */
        """
        pass

    def get_thread_level(self, const_PStatCollector_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_thread_level(const PStatCollector self)
        
        /**
         * Returns the current level value of the given collector in the current
         * thread.
         */
        """
        pass

    def isActive(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_active(const PStatCollector self)
        is_active(const PStatCollector self, const PStatThread thread)
        
        /**
         * Returns true if this particular collector is active on the default thread,
         * and we are currently transmitting PStats data.
         */
        
        /**
         * Returns true if this particular collector is active on the indicated
         * thread, and we are currently transmitting PStats data.
         */
        """
        pass

    def isStarted(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_started(const PStatCollector self)
        is_started(const PStatCollector self, const PStatThread thread)
        
        /**
         * Returns true if this particular collector has been started on the default
         * thread, or false otherwise.
         */
        
        /**
         * Returns true if this particular collector has been started on the indicated
         * thread, or false otherwise.
         */
        """
        pass

    def isValid(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_valid(PStatCollector self)
        
        /**
         * Returns true if collector is valid and may be used, or false if it was
         * constructed with the default constructor (in which case any attempt to use
         * it will crash).
         */
        """
        pass

    def is_active(self, const_PStatCollector_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_active(const PStatCollector self)
        is_active(const PStatCollector self, const PStatThread thread)
        
        /**
         * Returns true if this particular collector is active on the default thread,
         * and we are currently transmitting PStats data.
         */
        
        /**
         * Returns true if this particular collector is active on the indicated
         * thread, and we are currently transmitting PStats data.
         */
        """
        pass

    def is_started(self, const_PStatCollector_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_started(const PStatCollector self)
        is_started(const PStatCollector self, const PStatThread thread)
        
        /**
         * Returns true if this particular collector has been started on the default
         * thread, or false otherwise.
         */
        
        /**
         * Returns true if this particular collector has been started on the indicated
         * thread, or false otherwise.
         */
        """
        pass

    def is_valid(self, PStatCollector_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_valid(PStatCollector self)
        
        /**
         * Returns true if collector is valid and may be used, or false if it was
         * constructed with the default constructor (in which case any attempt to use
         * it will crash).
         */
        """
        pass

    def output(self, PStatCollector_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(PStatCollector self, ostream out)
        
        /**
         *
         */
        """
        pass

    def setLevel(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_level(const PStatCollector self, double level)
        set_level(const PStatCollector self, const PStatThread thread, double level)
        
        /**
         * Sets the level setting associated with this collector for the main thread
         * to the indicated value.  This implicitly calls flush_level().
         */
        
        /**
         * Sets the level setting associated with this collector for the indicated
         * thread to the indicated value.
         */
        """
        pass

    def setThreadLevel(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_thread_level(const PStatCollector self, double level)
        
        /**
         * Sets the level setting associated with this collector for the current
         * thread to the indicated value.
         */
        """
        pass

    def set_level(self, const_PStatCollector_self, double_level): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_level(const PStatCollector self, double level)
        set_level(const PStatCollector self, const PStatThread thread, double level)
        
        /**
         * Sets the level setting associated with this collector for the main thread
         * to the indicated value.  This implicitly calls flush_level().
         */
        
        /**
         * Sets the level setting associated with this collector for the indicated
         * thread to the indicated value.
         */
        """
        pass

    def set_thread_level(self, const_PStatCollector_self, double_level): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_thread_level(const PStatCollector self, double level)
        
        /**
         * Sets the level setting associated with this collector for the current
         * thread to the indicated value.
         */
        """
        pass

    def start(self, const_PStatCollector_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        start(const PStatCollector self)
        start(const PStatCollector self, const PStatThread thread)
        start(const PStatCollector self, const PStatThread thread, double as_of)
        
        /**
         * Starts this particular timer ticking.  This should be called before the
         * code you want to measure.
         */
        
        /**
         * Starts this timer ticking within a particular thread.
         */
        
        /**
         * Marks that the timer should have been started as of the indicated time.
         * This must be a time based on the PStatClient's clock (see
         * PStatClient::get_clock()), and care should be taken that all such calls
         * exhibit a monotonically increasing series of time values.
         */
        """
        pass

    def stop(self, const_PStatCollector_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        stop(const PStatCollector self)
        stop(const PStatCollector self, const PStatThread thread)
        stop(const PStatCollector self, const PStatThread thread, double as_of)
        
        /**
         * Stops this timer.  This should be called after the code you want to
         * measure.
         */
        
        /**
         * Stops this timer within a particular thread.
         */
        
        /**
         * Marks that the timer should have been stopped as of the indicated time.
         * This must be a time based on the PStatClient's clock (see
         * PStatClient::get_clock()), and care should be taken that all such calls
         * exhibit a monotonically increasing series of time values.
         */
        """
        pass

    def subLevel(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        sub_level(const PStatCollector self, double decrement)
        sub_level(const PStatCollector self, const PStatThread thread, double decrement)
        
        /**
         * Subtracts the indicated decrement (which may be negative) to the level
         * setting associated with this collector for the main thread.  If the
         * collector did not already have a level setting for the main thread, it is
         * initialized to 0.
         *
         * As an optimization, the data is not immediately set to the PStatClient.  It
         * will be sent the next time flush_level() is called.
         */
        
        /**
         * Subtracts the indicated decrement (which may be negative) to the level
         * setting associated with this collector for the indicated thread.  If the
         * collector did not already have a level setting for this thread, it is
         * initialized to 0.
         */
        """
        pass

    def subLevelNow(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        sub_level_now(const PStatCollector self, double decrement)
        
        /**
         * Calls sub_level() and immediately calls flush_level().
         */
        """
        pass

    def subThreadLevel(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        sub_thread_level(const PStatCollector self, double decrement)
        
        /**
         * Subtracts the indicated decrement (which may be negative) to the level
         * setting associated with this collector for the current thread.  If the
         * collector did not already have a level setting for the current thread, it
         * is initialized to 0.
         */
        """
        pass

    def sub_level(self, const_PStatCollector_self, double_decrement): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        sub_level(const PStatCollector self, double decrement)
        sub_level(const PStatCollector self, const PStatThread thread, double decrement)
        
        /**
         * Subtracts the indicated decrement (which may be negative) to the level
         * setting associated with this collector for the main thread.  If the
         * collector did not already have a level setting for the main thread, it is
         * initialized to 0.
         *
         * As an optimization, the data is not immediately set to the PStatClient.  It
         * will be sent the next time flush_level() is called.
         */
        
        /**
         * Subtracts the indicated decrement (which may be negative) to the level
         * setting associated with this collector for the indicated thread.  If the
         * collector did not already have a level setting for this thread, it is
         * initialized to 0.
         */
        """
        pass

    def sub_level_now(self, const_PStatCollector_self, double_decrement): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        sub_level_now(const PStatCollector self, double decrement)
        
        /**
         * Calls sub_level() and immediately calls flush_level().
         */
        """
        pass

    def sub_thread_level(self, const_PStatCollector_self, double_decrement): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        sub_thread_level(const PStatCollector self, double decrement)
        
        /**
         * Subtracts the indicated decrement (which may be negative) to the level
         * setting associated with this collector for the current thread.  If the
         * collector did not already have a level setting for the current thread, it
         * is initialized to 0.
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

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.PStatCollector' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.PStatCollector' objects>"
        '__doc__': '/**\n * A lightweight class that represents a single element that may be timed\n * and/or counted via stats.\n *\n * Collectors can be used to measure two different kinds of values: elapsed\n * time, and "other".\n *\n * To measure elapsed time, call start() and stop() as appropriate to bracket\n * the section of code you want to time (or use a PStatTimer to do this\n * automatically).\n *\n * To measure anything else, call set_level() and/or add_level() to set the\n * "level" value associated with this collector.  The meaning of the value set\n * for the "level" is entirely up to the user; it may represent the number of\n * triangles rendered or the kilobytes of texture memory consumed, for\n * instance.  The level set will remain fixed across multiple frames until it\n * is reset via another set_level() or adjusted via a call to add_level().  It\n * may also be completely removed via clear_level().\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.PStatCollector' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2C9570>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.PStatCollector' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.PStatCollector' objects>"
        'addLevel': None, # (!) real value is "<method 'addLevel' of 'panda3d.core.PStatCollector' objects>"
        'addLevelNow': None, # (!) real value is "<method 'addLevelNow' of 'panda3d.core.PStatCollector' objects>"
        'addThreadLevel': None, # (!) real value is "<method 'addThreadLevel' of 'panda3d.core.PStatCollector' objects>"
        'add_level': None, # (!) real value is "<method 'add_level' of 'panda3d.core.PStatCollector' objects>"
        'add_level_now': None, # (!) real value is "<method 'add_level_now' of 'panda3d.core.PStatCollector' objects>"
        'add_thread_level': None, # (!) real value is "<method 'add_thread_level' of 'panda3d.core.PStatCollector' objects>"
        'assign': None, # (!) real value is "<method 'assign' of 'panda3d.core.PStatCollector' objects>"
        'clearLevel': None, # (!) real value is "<method 'clearLevel' of 'panda3d.core.PStatCollector' objects>"
        'clearThreadLevel': None, # (!) real value is "<method 'clearThreadLevel' of 'panda3d.core.PStatCollector' objects>"
        'clear_level': None, # (!) real value is "<method 'clear_level' of 'panda3d.core.PStatCollector' objects>"
        'clear_thread_level': None, # (!) real value is "<method 'clear_thread_level' of 'panda3d.core.PStatCollector' objects>"
        'flushLevel': None, # (!) real value is "<method 'flushLevel' of 'panda3d.core.PStatCollector' objects>"
        'flush_level': None, # (!) real value is "<method 'flush_level' of 'panda3d.core.PStatCollector' objects>"
        'getFullname': None, # (!) real value is "<method 'getFullname' of 'panda3d.core.PStatCollector' objects>"
        'getIndex': None, # (!) real value is "<method 'getIndex' of 'panda3d.core.PStatCollector' objects>"
        'getLevel': None, # (!) real value is "<method 'getLevel' of 'panda3d.core.PStatCollector' objects>"
        'getName': None, # (!) real value is "<method 'getName' of 'panda3d.core.PStatCollector' objects>"
        'getThreadLevel': None, # (!) real value is "<method 'getThreadLevel' of 'panda3d.core.PStatCollector' objects>"
        'get_fullname': None, # (!) real value is "<method 'get_fullname' of 'panda3d.core.PStatCollector' objects>"
        'get_index': None, # (!) real value is "<method 'get_index' of 'panda3d.core.PStatCollector' objects>"
        'get_level': None, # (!) real value is "<method 'get_level' of 'panda3d.core.PStatCollector' objects>"
        'get_name': None, # (!) real value is "<method 'get_name' of 'panda3d.core.PStatCollector' objects>"
        'get_thread_level': None, # (!) real value is "<method 'get_thread_level' of 'panda3d.core.PStatCollector' objects>"
        'isActive': None, # (!) real value is "<method 'isActive' of 'panda3d.core.PStatCollector' objects>"
        'isStarted': None, # (!) real value is "<method 'isStarted' of 'panda3d.core.PStatCollector' objects>"
        'isValid': None, # (!) real value is "<method 'isValid' of 'panda3d.core.PStatCollector' objects>"
        'is_active': None, # (!) real value is "<method 'is_active' of 'panda3d.core.PStatCollector' objects>"
        'is_started': None, # (!) real value is "<method 'is_started' of 'panda3d.core.PStatCollector' objects>"
        'is_valid': None, # (!) real value is "<method 'is_valid' of 'panda3d.core.PStatCollector' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.PStatCollector' objects>"
        'setLevel': None, # (!) real value is "<method 'setLevel' of 'panda3d.core.PStatCollector' objects>"
        'setThreadLevel': None, # (!) real value is "<method 'setThreadLevel' of 'panda3d.core.PStatCollector' objects>"
        'set_level': None, # (!) real value is "<method 'set_level' of 'panda3d.core.PStatCollector' objects>"
        'set_thread_level': None, # (!) real value is "<method 'set_thread_level' of 'panda3d.core.PStatCollector' objects>"
        'start': None, # (!) real value is "<method 'start' of 'panda3d.core.PStatCollector' objects>"
        'stop': None, # (!) real value is "<method 'stop' of 'panda3d.core.PStatCollector' objects>"
        'subLevel': None, # (!) real value is "<method 'subLevel' of 'panda3d.core.PStatCollector' objects>"
        'subLevelNow': None, # (!) real value is "<method 'subLevelNow' of 'panda3d.core.PStatCollector' objects>"
        'subThreadLevel': None, # (!) real value is "<method 'subThreadLevel' of 'panda3d.core.PStatCollector' objects>"
        'sub_level': None, # (!) real value is "<method 'sub_level' of 'panda3d.core.PStatCollector' objects>"
        'sub_level_now': None, # (!) real value is "<method 'sub_level_now' of 'panda3d.core.PStatCollector' objects>"
        'sub_thread_level': None, # (!) real value is "<method 'sub_thread_level' of 'panda3d.core.PStatCollector' objects>"
    }


