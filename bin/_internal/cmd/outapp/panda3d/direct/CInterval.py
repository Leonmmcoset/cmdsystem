# encoding: utf-8
# module panda3d.direct
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\direct.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import panda3d.core as __panda3d_core


class CInterval(__panda3d_core.TypedReferenceCount):
    """
    /**
     * The base class for timeline components.  A CInterval represents a single
     * action, event, or collection of nested intervals that will be performed at
     * some specific time or over a period of time.
     *
     * This is essentially similar to the Python "Interval" class, but it is
     * implemented in C++ (hence the name). Intervals that may be implemented in
     * C++ will inherit from this class; Intervals that must be implemented in
     * Python will inherit from the similar Python class.
     */
    """
    def clearToInitial(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_to_initial(const CInterval self)
        
        /**
         * Pauses the interval, if it is playing, and resets its state to its initial
         * state, abandoning any state changes already in progress in the middle of
         * the interval.  Calling this is like pausing the interval and discarding it,
         * creating a new one in its place.
         */
        """
        pass

    def clear_to_initial(self, const_CInterval_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_to_initial(const CInterval self)
        
        /**
         * Pauses the interval, if it is playing, and resets its state to its initial
         * state, abandoning any state changes already in progress in the middle of
         * the interval.  Calling this is like pausing the interval and discarding it,
         * creating a new one in its place.
         */
        """
        pass

    def finish(self, const_CInterval_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        finish(const CInterval self)
        
        /**
         * Stops the interval from playing and sets it to its final state.
         */
        """
        pass

    def getAutoFinish(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_auto_finish(CInterval self)
        
        /**
         * Returns the state of the 'auto_finish' flag.  See set_auto_finish().
         */
        """
        pass

    def getAutoPause(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_auto_pause(CInterval self)
        
        /**
         * Returns the state of the 'auto_pause' flag.  See set_auto_pause().
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getDoneEvent(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_done_event(CInterval self)
        
        /**
         * Returns the event that is generated whenever the interval reaches its final
         * state, whether it is explicitly finished or whether it gets there on its
         * own.
         */
        """
        pass

    def getDuration(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_duration(CInterval self)
        
        /**
         * Returns the duration of the interval in seconds.
         */
        """
        pass

    def getManager(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_manager(CInterval self)
        
        /**
         * Returns the CIntervalManager object which will be responsible for playing
         * this interval.  Note that this can only return a C++ object; if the
         * particular CIntervalManager object has been extended in the scripting
         * language, this will return the encapsulated C++ object, not the full
         * extended object.
         */
        """
        pass

    def getName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_name(CInterval self)
        
        /**
         * Returns the interval's name.
         */
        """
        pass

    def getOpenEnded(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_open_ended(CInterval self)
        
        /**
         * Returns the state of the "open_ended" flag.  This is primarily intended for
         * instantaneous intervals like FunctionIntervals; it indicates true if the
         * interval has some lasting effect that should be applied even if the
         * interval doesn't get started until after its finish time, or false if the
         * interval is a transitive thing that doesn't need to be called late.
         */
        """
        pass

    def getPlayRate(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_play_rate(CInterval self)
        
        /**
         * Returns the play rate as set by the last call to start(), loop(), or
         * set_play_rate().
         */
        """
        pass

    def getState(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_state(CInterval self)
        
        /**
         * Indicates the state the interval believes it is in: whether it has been
         * started, is currently in the middle, or has been finalized.
         */
        """
        pass

    def getT(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_t(CInterval self)
        
        /**
         * Returns the current time of the interval: the last value of t passed to
         * priv_initialize(), priv_step(), or priv_finalize().
         */
        """
        pass

    def getWantsTCallback(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_wants_t_callback(CInterval self)
        
        /**
         * Returns the state of the 'wants_t_callback' flag.  See
         * set_wants_t_callback().
         */
        """
        pass

    def get_auto_finish(self, CInterval_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_auto_finish(CInterval self)
        
        /**
         * Returns the state of the 'auto_finish' flag.  See set_auto_finish().
         */
        """
        pass

    def get_auto_pause(self, CInterval_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_auto_pause(CInterval self)
        
        /**
         * Returns the state of the 'auto_pause' flag.  See set_auto_pause().
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_done_event(self, CInterval_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_done_event(CInterval self)
        
        /**
         * Returns the event that is generated whenever the interval reaches its final
         * state, whether it is explicitly finished or whether it gets there on its
         * own.
         */
        """
        pass

    def get_duration(self, CInterval_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_duration(CInterval self)
        
        /**
         * Returns the duration of the interval in seconds.
         */
        """
        pass

    def get_manager(self, CInterval_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_manager(CInterval self)
        
        /**
         * Returns the CIntervalManager object which will be responsible for playing
         * this interval.  Note that this can only return a C++ object; if the
         * particular CIntervalManager object has been extended in the scripting
         * language, this will return the encapsulated C++ object, not the full
         * extended object.
         */
        """
        pass

    def get_name(self, CInterval_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_name(CInterval self)
        
        /**
         * Returns the interval's name.
         */
        """
        pass

    def get_open_ended(self, CInterval_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_open_ended(CInterval self)
        
        /**
         * Returns the state of the "open_ended" flag.  This is primarily intended for
         * instantaneous intervals like FunctionIntervals; it indicates true if the
         * interval has some lasting effect that should be applied even if the
         * interval doesn't get started until after its finish time, or false if the
         * interval is a transitive thing that doesn't need to be called late.
         */
        """
        pass

    def get_play_rate(self, CInterval_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_play_rate(CInterval self)
        
        /**
         * Returns the play rate as set by the last call to start(), loop(), or
         * set_play_rate().
         */
        """
        pass

    def get_state(self, CInterval_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_state(CInterval self)
        
        /**
         * Indicates the state the interval believes it is in: whether it has been
         * started, is currently in the middle, or has been finalized.
         */
        """
        pass

    def get_t(self, CInterval_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_t(CInterval self)
        
        /**
         * Returns the current time of the interval: the last value of t passed to
         * priv_initialize(), priv_step(), or priv_finalize().
         */
        """
        pass

    def get_wants_t_callback(self, CInterval_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_wants_t_callback(CInterval self)
        
        /**
         * Returns the state of the 'wants_t_callback' flag.  See
         * set_wants_t_callback().
         */
        """
        pass

    def isPlaying(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_playing(CInterval self)
        
        /**
         * Returns true if the interval is currently playing, false otherwise.
         */
        """
        pass

    def isStopped(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_stopped(CInterval self)
        
        /**
         * Returns true if the interval is in either its initial or final states (but
         * not in a running or paused state).
         */
        """
        pass

    def is_playing(self, CInterval_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_playing(CInterval self)
        
        /**
         * Returns true if the interval is currently playing, false otherwise.
         */
        """
        pass

    def is_stopped(self, CInterval_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_stopped(CInterval self)
        
        /**
         * Returns true if the interval is in either its initial or final states (but
         * not in a running or paused state).
         */
        """
        pass

    def loop(self, const_CInterval_self, double_start_t, double_end_t, double_play_rate): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        loop(const CInterval self, double start_t, double end_t, double play_rate)
        
        /**
         * Starts the interval playing by registering it with the current
         * CIntervalManager.  The interval will play until it is interrupted with
         * finish() or pause(), looping back to start_t when it reaches end_t.
         *
         * If end_t is less than zero, it indicates the end of the interval.
         */
        """
        pass

    def output(self, CInterval_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(CInterval self, ostream out)
        
        /**
         *
         */
        """
        pass

    def pause(self, const_CInterval_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        pause(const CInterval self)
        
        /**
         * Stops the interval from playing but leaves it in its current state.  It may
         * later be resumed from this point by calling resume().
         */
        """
        pass

    def privDoEvent(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        priv_do_event(const CInterval self, double t, int event)
        
        // These cannot be declared private because they must be accessible to
        // Python, but the method names are prefixed with priv_ to remind you that
        // you probably don't want to be using them directly.
        
        /**
         * Calls the appropriate event function indicated by the EventType.
         */
        """
        pass

    def privFinalize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        priv_finalize(const CInterval self)
        
        /**
         * This is called to stop an interval, forcing it to whatever state it would
         * be after it played all the way through.  It's generally invoked by
         * set_final_t().
         */
        """
        pass

    def privInitialize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        priv_initialize(const CInterval self, double t)
        
        /**
         * This replaces the first call to priv_step(), and indicates that the
         * interval has just begun.  This may be overridden by derived classes that
         * need to do some explicit initialization on the first call.
         */
        """
        pass

    def privInstant(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        priv_instant(const CInterval self)
        
        /**
         * This is called in lieu of priv_initialize() .. priv_step() ..
         * priv_finalize(), when everything is to happen within one frame.  The
         * interval should initialize itself, then leave itself in the final state.
         */
        """
        pass

    def privInterrupt(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        priv_interrupt(const CInterval self)
        
        /**
         * This is called while the interval is playing to indicate that it is about
         * to be interrupted; that is, priv_step() will not be called for a length of
         * time.  But the interval should remain in its current state in anticipation
         * of being eventually restarted when the calls to priv_step() eventually
         * resume.
         *
         * The purpose of this function is to allow self-running intervals like sound
         * intervals to stop the actual sound playback during the pause.
         */
        """
        pass

    def privReverseFinalize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        priv_reverse_finalize(const CInterval self)
        
        /**
         * Called generally following a priv_reverse_initialize(), this indicates the
         * interval should set itself to the initial state.
         */
        """
        pass

    def privReverseInitialize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        priv_reverse_initialize(const CInterval self, double t)
        
        /**
         * Similar to priv_initialize(), but this is called when the interval is being
         * played backwards; it indicates that the interval should start at the
         * finishing state and undo any intervening intervals.
         */
        """
        pass

    def privReverseInstant(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        priv_reverse_instant(const CInterval self)
        
        /**
         * This is called in lieu of priv_reverse_initialize() .. priv_step() ..
         * priv_reverse_finalize(), when everything is to happen within one frame.
         * The interval should initialize itself, then leave itself in the initial
         * state.
         */
        """
        pass

    def privStep(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        priv_step(const CInterval self, double t)
        
        /**
         * Advances the time on the interval.  The time may either increase (the
         * normal case) or decrease (e.g.  if the interval is being played by a
         * slider).
         */
        """
        pass

    def priv_do_event(self, const_CInterval_self, double_t, int_event): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        priv_do_event(const CInterval self, double t, int event)
        
        // These cannot be declared private because they must be accessible to
        // Python, but the method names are prefixed with priv_ to remind you that
        // you probably don't want to be using them directly.
        
        /**
         * Calls the appropriate event function indicated by the EventType.
         */
        """
        pass

    def priv_finalize(self, const_CInterval_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        priv_finalize(const CInterval self)
        
        /**
         * This is called to stop an interval, forcing it to whatever state it would
         * be after it played all the way through.  It's generally invoked by
         * set_final_t().
         */
        """
        pass

    def priv_initialize(self, const_CInterval_self, double_t): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        priv_initialize(const CInterval self, double t)
        
        /**
         * This replaces the first call to priv_step(), and indicates that the
         * interval has just begun.  This may be overridden by derived classes that
         * need to do some explicit initialization on the first call.
         */
        """
        pass

    def priv_instant(self, const_CInterval_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        priv_instant(const CInterval self)
        
        /**
         * This is called in lieu of priv_initialize() .. priv_step() ..
         * priv_finalize(), when everything is to happen within one frame.  The
         * interval should initialize itself, then leave itself in the final state.
         */
        """
        pass

    def priv_interrupt(self, const_CInterval_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        priv_interrupt(const CInterval self)
        
        /**
         * This is called while the interval is playing to indicate that it is about
         * to be interrupted; that is, priv_step() will not be called for a length of
         * time.  But the interval should remain in its current state in anticipation
         * of being eventually restarted when the calls to priv_step() eventually
         * resume.
         *
         * The purpose of this function is to allow self-running intervals like sound
         * intervals to stop the actual sound playback during the pause.
         */
        """
        pass

    def priv_reverse_finalize(self, const_CInterval_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        priv_reverse_finalize(const CInterval self)
        
        /**
         * Called generally following a priv_reverse_initialize(), this indicates the
         * interval should set itself to the initial state.
         */
        """
        pass

    def priv_reverse_initialize(self, const_CInterval_self, double_t): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        priv_reverse_initialize(const CInterval self, double t)
        
        /**
         * Similar to priv_initialize(), but this is called when the interval is being
         * played backwards; it indicates that the interval should start at the
         * finishing state and undo any intervening intervals.
         */
        """
        pass

    def priv_reverse_instant(self, const_CInterval_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        priv_reverse_instant(const CInterval self)
        
        /**
         * This is called in lieu of priv_reverse_initialize() .. priv_step() ..
         * priv_reverse_finalize(), when everything is to happen within one frame.
         * The interval should initialize itself, then leave itself in the initial
         * state.
         */
        """
        pass

    def priv_step(self, const_CInterval_self, double_t): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        priv_step(const CInterval self, double t)
        
        /**
         * Advances the time on the interval.  The time may either increase (the
         * normal case) or decrease (e.g.  if the interval is being played by a
         * slider).
         */
        """
        pass

    def resume(self, const_CInterval_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        resume(const CInterval self)
        resume(const CInterval self, double start_t)
        
        /**
         * Restarts the interval from its current point after a previous call to
         * pause().
         */
        
        /**
         * Restarts the interval from the indicated point after a previous call to
         * pause().
         */
        """
        pass

    def resumeUntil(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        resume_until(const CInterval self, double end_t)
        
        /**
         * Restarts the interval from the current point after a previous call to
         * pause() (or a previous play-to-point-and-stop), to play until the indicated
         * point and then stop.
         */
        """
        pass

    def resume_until(self, const_CInterval_self, double_end_t): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        resume_until(const CInterval self, double end_t)
        
        /**
         * Restarts the interval from the current point after a previous call to
         * pause() (or a previous play-to-point-and-stop), to play until the indicated
         * point and then stop.
         */
        """
        pass

    def setAutoFinish(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_auto_finish(const CInterval self, bool auto_finish)
        
        /**
         * Changes the state of the 'auto_finish' flag.  If this is true, the interval
         * may be arbitrarily finished when the system needs to reset due to some
         * external event by calling CIntervalManager::interrupt().  If this is false
         * (the default), the interval must always be explicitly finished or paused.
         */
        """
        pass

    def setAutoPause(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_auto_pause(const CInterval self, bool auto_pause)
        
        /**
         * Changes the state of the 'auto_pause' flag.  If this is true, the interval
         * may be arbitrarily interrupted when the system needs to reset due to some
         * external event by calling CIntervalManager::interrupt().  If this is false
         * (the default), the interval must always be explicitly finished or paused.
         */
        """
        pass

    def setDoneEvent(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_done_event(const CInterval self, str event)
        
        /**
         * Sets the event that is generated whenever the interval reaches its final
         * state, whether it is explicitly finished or whether it gets there on its
         * own.
         */
        """
        pass

    def setManager(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_manager(const CInterval self, CIntervalManager manager)
        
        /**
         * Indicates the CIntervalManager object which will be responsible for playing
         * this interval.  This defaults to the global CIntervalManager; you should
         * need to change this only if you have special requirements for playing this
         * interval.
         */
        """
        pass

    def setPlayRate(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_play_rate(const CInterval self, double play_rate)
        
        /**
         * Changes the play rate of the interval.  If the interval is already started,
         * this changes its speed on-the-fly.  Note that since play_rate is a
         * parameter to start() and loop(), the next call to start() or loop() will
         * reset this parameter.
         */
        """
        pass

    def setT(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_t(const CInterval self, double t)
        
        /**
         * Explicitly sets the time within the interval.  Normally, you would use
         * start() .. finish() to let the time play normally, but this may be used to
         * set the time to some particular value.
         */
        """
        pass

    def setupPlay(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        setup_play(const CInterval self, double start_time, double end_time, double play_rate, bool do_loop)
        
        /**
         * Called to prepare the interval for automatic timed playback, e.g.  via a
         * Python task.  The interval will be played from start_t to end_t, at a time
         * factor specified by play_rate.  start_t must always be less than end_t
         * (except for the exception for end_t == -1, below), but if play_rate is
         * negative the interval will be played backwards.
         *
         * Specify end_t of -1 to play the entire interval from start_t.
         *
         * Call step_play() repeatedly to execute the interval.
         */
        """
        pass

    def setupResume(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        setup_resume(const CInterval self)
        
        /**
         * Called to prepare the interval for restarting at the current point within
         * the interval after an interruption.
         */
        """
        pass

    def setupResumeUntil(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        setup_resume_until(const CInterval self, double end_t)
        
        /**
         * Called to prepare the interval for restarting from the current point after
         * a previous call to pause() (or a previous play-to-point-and-stop), to play
         * until the indicated point and then stop.
         */
        """
        pass

    def setup_play(self, const_CInterval_self, double_start_time, double_end_time, double_play_rate, bool_do_loop): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        setup_play(const CInterval self, double start_time, double end_time, double play_rate, bool do_loop)
        
        /**
         * Called to prepare the interval for automatic timed playback, e.g.  via a
         * Python task.  The interval will be played from start_t to end_t, at a time
         * factor specified by play_rate.  start_t must always be less than end_t
         * (except for the exception for end_t == -1, below), but if play_rate is
         * negative the interval will be played backwards.
         *
         * Specify end_t of -1 to play the entire interval from start_t.
         *
         * Call step_play() repeatedly to execute the interval.
         */
        """
        pass

    def setup_resume(self, const_CInterval_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        setup_resume(const CInterval self)
        
        /**
         * Called to prepare the interval for restarting at the current point within
         * the interval after an interruption.
         */
        """
        pass

    def setup_resume_until(self, const_CInterval_self, double_end_t): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        setup_resume_until(const CInterval self, double end_t)
        
        /**
         * Called to prepare the interval for restarting from the current point after
         * a previous call to pause() (or a previous play-to-point-and-stop), to play
         * until the indicated point and then stop.
         */
        """
        pass

    def setWantsTCallback(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_wants_t_callback(const CInterval self, bool wants_t_callback)
        
        /**
         * Changes the state of the 'wants_t_callback' flag.  If this is true, the
         * interval will be returned by CIntervalManager::get_event() each time the
         * interval's time value has been changed, regardless of whether it has any
         * external events.
         */
        """
        pass

    def set_auto_finish(self, const_CInterval_self, bool_auto_finish): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_auto_finish(const CInterval self, bool auto_finish)
        
        /**
         * Changes the state of the 'auto_finish' flag.  If this is true, the interval
         * may be arbitrarily finished when the system needs to reset due to some
         * external event by calling CIntervalManager::interrupt().  If this is false
         * (the default), the interval must always be explicitly finished or paused.
         */
        """
        pass

    def set_auto_pause(self, const_CInterval_self, bool_auto_pause): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_auto_pause(const CInterval self, bool auto_pause)
        
        /**
         * Changes the state of the 'auto_pause' flag.  If this is true, the interval
         * may be arbitrarily interrupted when the system needs to reset due to some
         * external event by calling CIntervalManager::interrupt().  If this is false
         * (the default), the interval must always be explicitly finished or paused.
         */
        """
        pass

    def set_done_event(self, const_CInterval_self, str_event): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_done_event(const CInterval self, str event)
        
        /**
         * Sets the event that is generated whenever the interval reaches its final
         * state, whether it is explicitly finished or whether it gets there on its
         * own.
         */
        """
        pass

    def set_manager(self, const_CInterval_self, CIntervalManager_manager): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_manager(const CInterval self, CIntervalManager manager)
        
        /**
         * Indicates the CIntervalManager object which will be responsible for playing
         * this interval.  This defaults to the global CIntervalManager; you should
         * need to change this only if you have special requirements for playing this
         * interval.
         */
        """
        pass

    def set_play_rate(self, const_CInterval_self, double_play_rate): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_play_rate(const CInterval self, double play_rate)
        
        /**
         * Changes the play rate of the interval.  If the interval is already started,
         * this changes its speed on-the-fly.  Note that since play_rate is a
         * parameter to start() and loop(), the next call to start() or loop() will
         * reset this parameter.
         */
        """
        pass

    def set_t(self, const_CInterval_self, double_t): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_t(const CInterval self, double t)
        
        /**
         * Explicitly sets the time within the interval.  Normally, you would use
         * start() .. finish() to let the time play normally, but this may be used to
         * set the time to some particular value.
         */
        """
        pass

    def set_wants_t_callback(self, const_CInterval_self, bool_wants_t_callback): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_wants_t_callback(const CInterval self, bool wants_t_callback)
        
        /**
         * Changes the state of the 'wants_t_callback' flag.  If this is true, the
         * interval will be returned by CIntervalManager::get_event() each time the
         * interval's time value has been changed, regardless of whether it has any
         * external events.
         */
        """
        pass

    def start(self, const_CInterval_self, double_start_t, double_end_t, double_play_rate): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        start(const CInterval self, double start_t, double end_t, double play_rate)
        
        /**
         * Starts the interval playing by registering it with the current
         * CIntervalManager.  The interval will play to the end and stop.
         *
         * If end_t is less than zero, it indicates the end of the interval.
         */
        """
        pass

    def stepPlay(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        step_play(const CInterval self)
        
        /**
         * Should be called once per frame to execute the automatic timed playback
         * begun with setup_play().
         *
         * Returns true if the interval should continue, false if it is done and
         * should stop.
         */
        """
        pass

    def step_play(self, const_CInterval_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        step_play(const CInterval self)
        
        /**
         * Should be called once per frame to execute the automatic timed playback
         * begun with setup_play().
         *
         * Returns true if the interval should continue, false if it is done and
         * should stop.
         */
        """
        pass

    def write(self, CInterval_self, ostream_out, int_indent_level): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(CInterval self, ostream out, int indent_level)
        
        /**
         *
         */
        """
        pass

    def __await__(self, *args, **kwargs): # real signature unknown
        """ Return an iterator to be used in await expression. """
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

    auto_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    auto_pause = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    done_event = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    duration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    manager = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    open_ended = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    playing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    play_rate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    stopped = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    t = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        'ETFinalize': 3,
        'ETInitialize': 0,
        'ETInstant': 1,
        'ETInterrupt': 7,
        'ETReverseFinalize': 6,
        'ETReverseInitialize': 4,
        'ETReverseInstant': 5,
        'ETStep': 2,
        'ET_finalize': 3,
        'ET_initialize': 0,
        'ET_instant': 1,
        'ET_interrupt': 7,
        'ET_reverse_finalize': 6,
        'ET_reverse_initialize': 4,
        'ET_reverse_instant': 5,
        'ET_step': 2,
        'SFinal': 3,
        'SInitial': 0,
        'SPaused': 2,
        'SStarted': 1,
        'S_final': 3,
        'S_initial': 0,
        'S_paused': 2,
        'S_started': 1,
        '__await__': None, # (!) real value is "<slot wrapper '__await__' of 'panda3d.direct.CInterval' objects>"
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.direct.CInterval' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.direct.CInterval' objects>"
        '__doc__': '/**\n * The base class for timeline components.  A CInterval represents a single\n * action, event, or collection of nested intervals that will be performed at\n * some specific time or over a period of time.\n *\n * This is essentially similar to the Python "Interval" class, but it is\n * implemented in C++ (hence the name). Intervals that may be implemented in\n * C++ will inherit from this class; Intervals that must be implemented in\n * Python will inherit from the similar Python class.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.direct.CInterval' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDC68E5360>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.direct.CInterval' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.direct.CInterval' objects>"
        'auto_finish': None, # (!) real value is "<attribute 'auto_finish' of 'panda3d.direct.CInterval' objects>"
        'auto_pause': None, # (!) real value is "<attribute 'auto_pause' of 'panda3d.direct.CInterval' objects>"
        'clearToInitial': None, # (!) real value is "<method 'clearToInitial' of 'panda3d.direct.CInterval' objects>"
        'clear_to_initial': None, # (!) real value is "<method 'clear_to_initial' of 'panda3d.direct.CInterval' objects>"
        'done_event': None, # (!) real value is "<attribute 'done_event' of 'panda3d.direct.CInterval' objects>"
        'duration': None, # (!) real value is "<attribute 'duration' of 'panda3d.direct.CInterval' objects>"
        'finish': None, # (!) real value is "<method 'finish' of 'panda3d.direct.CInterval' objects>"
        'getAutoFinish': None, # (!) real value is "<method 'getAutoFinish' of 'panda3d.direct.CInterval' objects>"
        'getAutoPause': None, # (!) real value is "<method 'getAutoPause' of 'panda3d.direct.CInterval' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFDC68E5360>)>'
        'getDoneEvent': None, # (!) real value is "<method 'getDoneEvent' of 'panda3d.direct.CInterval' objects>"
        'getDuration': None, # (!) real value is "<method 'getDuration' of 'panda3d.direct.CInterval' objects>"
        'getManager': None, # (!) real value is "<method 'getManager' of 'panda3d.direct.CInterval' objects>"
        'getName': None, # (!) real value is "<method 'getName' of 'panda3d.direct.CInterval' objects>"
        'getOpenEnded': None, # (!) real value is "<method 'getOpenEnded' of 'panda3d.direct.CInterval' objects>"
        'getPlayRate': None, # (!) real value is "<method 'getPlayRate' of 'panda3d.direct.CInterval' objects>"
        'getState': None, # (!) real value is "<method 'getState' of 'panda3d.direct.CInterval' objects>"
        'getT': None, # (!) real value is "<method 'getT' of 'panda3d.direct.CInterval' objects>"
        'getWantsTCallback': None, # (!) real value is "<method 'getWantsTCallback' of 'panda3d.direct.CInterval' objects>"
        'get_auto_finish': None, # (!) real value is "<method 'get_auto_finish' of 'panda3d.direct.CInterval' objects>"
        'get_auto_pause': None, # (!) real value is "<method 'get_auto_pause' of 'panda3d.direct.CInterval' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFDC68E5360>)>'
        'get_done_event': None, # (!) real value is "<method 'get_done_event' of 'panda3d.direct.CInterval' objects>"
        'get_duration': None, # (!) real value is "<method 'get_duration' of 'panda3d.direct.CInterval' objects>"
        'get_manager': None, # (!) real value is "<method 'get_manager' of 'panda3d.direct.CInterval' objects>"
        'get_name': None, # (!) real value is "<method 'get_name' of 'panda3d.direct.CInterval' objects>"
        'get_open_ended': None, # (!) real value is "<method 'get_open_ended' of 'panda3d.direct.CInterval' objects>"
        'get_play_rate': None, # (!) real value is "<method 'get_play_rate' of 'panda3d.direct.CInterval' objects>"
        'get_state': None, # (!) real value is "<method 'get_state' of 'panda3d.direct.CInterval' objects>"
        'get_t': None, # (!) real value is "<method 'get_t' of 'panda3d.direct.CInterval' objects>"
        'get_wants_t_callback': None, # (!) real value is "<method 'get_wants_t_callback' of 'panda3d.direct.CInterval' objects>"
        'isPlaying': None, # (!) real value is "<method 'isPlaying' of 'panda3d.direct.CInterval' objects>"
        'isStopped': None, # (!) real value is "<method 'isStopped' of 'panda3d.direct.CInterval' objects>"
        'is_playing': None, # (!) real value is "<method 'is_playing' of 'panda3d.direct.CInterval' objects>"
        'is_stopped': None, # (!) real value is "<method 'is_stopped' of 'panda3d.direct.CInterval' objects>"
        'loop': None, # (!) real value is "<method 'loop' of 'panda3d.direct.CInterval' objects>"
        'manager': None, # (!) real value is "<attribute 'manager' of 'panda3d.direct.CInterval' objects>"
        'name': None, # (!) real value is "<attribute 'name' of 'panda3d.direct.CInterval' objects>"
        'open_ended': None, # (!) real value is "<attribute 'open_ended' of 'panda3d.direct.CInterval' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.direct.CInterval' objects>"
        'pause': None, # (!) real value is "<method 'pause' of 'panda3d.direct.CInterval' objects>"
        'play_rate': None, # (!) real value is "<attribute 'play_rate' of 'panda3d.direct.CInterval' objects>"
        'playing': None, # (!) real value is "<attribute 'playing' of 'panda3d.direct.CInterval' objects>"
        'privDoEvent': None, # (!) real value is "<method 'privDoEvent' of 'panda3d.direct.CInterval' objects>"
        'privFinalize': None, # (!) real value is "<method 'privFinalize' of 'panda3d.direct.CInterval' objects>"
        'privInitialize': None, # (!) real value is "<method 'privInitialize' of 'panda3d.direct.CInterval' objects>"
        'privInstant': None, # (!) real value is "<method 'privInstant' of 'panda3d.direct.CInterval' objects>"
        'privInterrupt': None, # (!) real value is "<method 'privInterrupt' of 'panda3d.direct.CInterval' objects>"
        'privReverseFinalize': None, # (!) real value is "<method 'privReverseFinalize' of 'panda3d.direct.CInterval' objects>"
        'privReverseInitialize': None, # (!) real value is "<method 'privReverseInitialize' of 'panda3d.direct.CInterval' objects>"
        'privReverseInstant': None, # (!) real value is "<method 'privReverseInstant' of 'panda3d.direct.CInterval' objects>"
        'privStep': None, # (!) real value is "<method 'privStep' of 'panda3d.direct.CInterval' objects>"
        'priv_do_event': None, # (!) real value is "<method 'priv_do_event' of 'panda3d.direct.CInterval' objects>"
        'priv_finalize': None, # (!) real value is "<method 'priv_finalize' of 'panda3d.direct.CInterval' objects>"
        'priv_initialize': None, # (!) real value is "<method 'priv_initialize' of 'panda3d.direct.CInterval' objects>"
        'priv_instant': None, # (!) real value is "<method 'priv_instant' of 'panda3d.direct.CInterval' objects>"
        'priv_interrupt': None, # (!) real value is "<method 'priv_interrupt' of 'panda3d.direct.CInterval' objects>"
        'priv_reverse_finalize': None, # (!) real value is "<method 'priv_reverse_finalize' of 'panda3d.direct.CInterval' objects>"
        'priv_reverse_initialize': None, # (!) real value is "<method 'priv_reverse_initialize' of 'panda3d.direct.CInterval' objects>"
        'priv_reverse_instant': None, # (!) real value is "<method 'priv_reverse_instant' of 'panda3d.direct.CInterval' objects>"
        'priv_step': None, # (!) real value is "<method 'priv_step' of 'panda3d.direct.CInterval' objects>"
        'resume': None, # (!) real value is "<method 'resume' of 'panda3d.direct.CInterval' objects>"
        'resumeUntil': None, # (!) real value is "<method 'resumeUntil' of 'panda3d.direct.CInterval' objects>"
        'resume_until': None, # (!) real value is "<method 'resume_until' of 'panda3d.direct.CInterval' objects>"
        'setAutoFinish': None, # (!) real value is "<method 'setAutoFinish' of 'panda3d.direct.CInterval' objects>"
        'setAutoPause': None, # (!) real value is "<method 'setAutoPause' of 'panda3d.direct.CInterval' objects>"
        'setDoneEvent': None, # (!) real value is "<method 'setDoneEvent' of 'panda3d.direct.CInterval' objects>"
        'setManager': None, # (!) real value is "<method 'setManager' of 'panda3d.direct.CInterval' objects>"
        'setPlayRate': None, # (!) real value is "<method 'setPlayRate' of 'panda3d.direct.CInterval' objects>"
        'setT': None, # (!) real value is "<method 'setT' of 'panda3d.direct.CInterval' objects>"
        'setWantsTCallback': None, # (!) real value is "<method 'setWantsTCallback' of 'panda3d.direct.CInterval' objects>"
        'set_auto_finish': None, # (!) real value is "<method 'set_auto_finish' of 'panda3d.direct.CInterval' objects>"
        'set_auto_pause': None, # (!) real value is "<method 'set_auto_pause' of 'panda3d.direct.CInterval' objects>"
        'set_done_event': None, # (!) real value is "<method 'set_done_event' of 'panda3d.direct.CInterval' objects>"
        'set_manager': None, # (!) real value is "<method 'set_manager' of 'panda3d.direct.CInterval' objects>"
        'set_play_rate': None, # (!) real value is "<method 'set_play_rate' of 'panda3d.direct.CInterval' objects>"
        'set_t': None, # (!) real value is "<method 'set_t' of 'panda3d.direct.CInterval' objects>"
        'set_wants_t_callback': None, # (!) real value is "<method 'set_wants_t_callback' of 'panda3d.direct.CInterval' objects>"
        'setupPlay': None, # (!) real value is "<method 'setupPlay' of 'panda3d.direct.CInterval' objects>"
        'setupResume': None, # (!) real value is "<method 'setupResume' of 'panda3d.direct.CInterval' objects>"
        'setupResumeUntil': None, # (!) real value is "<method 'setupResumeUntil' of 'panda3d.direct.CInterval' objects>"
        'setup_play': None, # (!) real value is "<method 'setup_play' of 'panda3d.direct.CInterval' objects>"
        'setup_resume': None, # (!) real value is "<method 'setup_resume' of 'panda3d.direct.CInterval' objects>"
        'setup_resume_until': None, # (!) real value is "<method 'setup_resume_until' of 'panda3d.direct.CInterval' objects>"
        'start': None, # (!) real value is "<method 'start' of 'panda3d.direct.CInterval' objects>"
        'state': None, # (!) real value is "<attribute 'state' of 'panda3d.direct.CInterval' objects>"
        'stepPlay': None, # (!) real value is "<method 'stepPlay' of 'panda3d.direct.CInterval' objects>"
        'step_play': None, # (!) real value is "<method 'step_play' of 'panda3d.direct.CInterval' objects>"
        'stopped': None, # (!) real value is "<attribute 'stopped' of 'panda3d.direct.CInterval' objects>"
        't': None, # (!) real value is "<attribute 't' of 'panda3d.direct.CInterval' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.direct.CInterval' objects>"
    }
    ETFinalize = 3
    ETInitialize = 0
    ETInstant = 1
    ETInterrupt = 7
    ETReverseFinalize = 6
    ETReverseInitialize = 4
    ETReverseInstant = 5
    ETStep = 2
    ET_finalize = 3
    ET_initialize = 0
    ET_instant = 1
    ET_interrupt = 7
    ET_reverse_finalize = 6
    ET_reverse_initialize = 4
    ET_reverse_instant = 5
    ET_step = 2
    SFinal = 3
    SInitial = 0
    SPaused = 2
    SStarted = 1
    S_final = 3
    S_initial = 0
    S_paused = 2
    S_started = 1


