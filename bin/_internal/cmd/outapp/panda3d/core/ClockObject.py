# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .ReferenceCount import ReferenceCount

class ClockObject(ReferenceCount):
    """
    /**
     * A ClockObject keeps track of elapsed real time and discrete time.  In
     * normal mode, get_frame_time() returns the time as of the last time tick()
     * was called.  This is the "discrete" time, and is usually used to get the
     * time as of, for instance, the beginning of the current frame.
     *
     * In other modes, as set by set_mode() or the clock-mode config variable,
     * get_frame_time() may return other values to simulate different timing
     * effects, for instance to perform non-real-time animation.  See set_mode().
     *
     * In all modes, get_real_time() always returns the elapsed real time in
     * seconds since the ClockObject was constructed, or since it was last reset.
     *
     * You can create your own ClockObject whenever you want to have your own
     * local timer.  There is also a default, global ClockObject intended to
     * represent global time for the application; this is normally set up to tick
     * every frame so that its get_frame_time() will return the time for the
     * current frame.
     */
    """
    def calcFrameRateDeviation(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        calc_frame_rate_deviation(ClockObject self, Thread current_thread)
        
        /**
         * Returns the standard deviation of the frame times of the frames rendered
         * over the past get_average_frame_rate_interval() seconds.  This number gives
         * an estimate of the chugginess of the frame rate; if it is large, there is a
         * large variation in the frame rate; if is small, all of the frames are
         * consistent in length.
         *
         * A large value might also represent just a recent change in frame rate, for
         * instance, because the camera has just rotated from looking at a simple
         * scene to looking at a more complex scene.
         */
        """
        pass

    def calc_frame_rate_deviation(self, ClockObject_self, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        calc_frame_rate_deviation(ClockObject self, Thread current_thread)
        
        /**
         * Returns the standard deviation of the frame times of the frames rendered
         * over the past get_average_frame_rate_interval() seconds.  This number gives
         * an estimate of the chugginess of the frame rate; if it is large, there is a
         * large variation in the frame rate; if is small, all of the frames are
         * consistent in length.
         *
         * A large value might also represent just a recent change in frame rate, for
         * instance, because the camera has just rotated from looking at a simple
         * scene to looking at a more complex scene.
         */
        """
        pass

    def checkErrors(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        check_errors(const ClockObject self, Thread current_thread)
        
        /**
         * Returns true if a clock error was detected since the last time
         * check_errors() was called.  A clock error means that something happened, an
         * OS or BIOS bug, for instance, that makes the current value of the clock
         * somewhat suspect, and an application may wish to resynchronize with any
         * external clocks.
         */
        """
        pass

    def check_errors(self, const_ClockObject_self, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        check_errors(const ClockObject self, Thread current_thread)
        
        /**
         * Returns true if a clock error was detected since the last time
         * check_errors() was called.  A clock error means that something happened, an
         * OS or BIOS bug, for instance, that makes the current value of the clock
         * somewhat suspect, and an application may wish to resynchronize with any
         * external clocks.
         */
        """
        pass

    def getAverageFrameRate(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_average_frame_rate(ClockObject self, Thread current_thread)
        
        /**
         * Returns the average frame rate in number of frames per second over the last
         * get_average_frame_rate_interval() seconds.  This measures the virtual frame
         * rate if the clock is in M_non_real_time mode.
         */
        """
        pass

    def getAverageFrameRateInterval(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_average_frame_rate_interval(ClockObject self)
        
        /**
         * Returns the interval of time (in seconds) over which
         * get_average_frame_rate() averages the number of frames per second to
         * compute the frame rate.
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getDegradeFactor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_degrade_factor(ClockObject self)
        
        /**
         * In degrade mode, returns the ratio by which the performance is degraded.  A
         * value of 2.0 causes the clock to be slowed down by a factor of two
         * (reducing performance to 1/2 what would be otherwise).
         *
         * This has no effect if mode is not M_degrade.
         */
        """
        pass

    def getDt(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_dt(ClockObject self, Thread current_thread)
        
        /**
         * Returns the elapsed time for the previous frame: the number of seconds
         * elapsed between the last two calls to tick().
         */
        """
        pass

    def getFrameCount(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_frame_count(ClockObject self, Thread current_thread)
        
        /**
         * Returns the number of times tick() has been called since the ClockObject
         * was created, or since it was last reset.  This is generally the number of
         * frames that have been rendered.
         */
        """
        pass

    def getFrameTime(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_frame_time(ClockObject self, Thread current_thread)
        
        /**
         * Returns the time in seconds as of the last time tick() was called
         * (typically, this will be as of the start of the current frame).
         *
         * This is generally the kind of time you want to ask for in most rendering
         * and animation contexts, since it's important that all of the animation for
         * a given frame remains in sync with each other.
         */
        """
        pass

    def getGlobalClock(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_global_clock()
        
        /**
         * Returns a pointer to the global ClockObject.  This is the ClockObject that
         * most code should use for handling scene graph rendering and animation.
         */
        """
        pass

    def getLongTime(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_long_time(ClockObject self)
        
        /**
         * Returns the actual number of seconds elapsed since the ClockObject was
         * created, or since it was last reset.
         *
         * This is similar to get_real_time(), except that it uses the most accurate
         * counter we have over a long period of time, and so it is less likely to
         * drift.  However, it may not be very precise for measuring short intervals.
         * On Windows, for instace, this is only accurate to within about 55
         * milliseconds.
         */
        """
        pass

    def getMaxDt(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_max_dt(ClockObject self)
        
        /**
         * Returns the current maximum allowable time elapsed between any two frames.
         * See set_max_dt().
         */
        """
        pass

    def getMaxFrameDuration(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_max_frame_duration(ClockObject self, Thread current_thread)
        
        /**
         * Returns the maximum frame duration over the last
         * get_average_frame_rate_interval() seconds.
         */
        """
        pass

    def getMode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_mode(ClockObject self)
        
        /**
         * Returns the current mode of the clock.  See set_mode().
         */
        """
        pass

    def getNetFrameRate(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_net_frame_rate(ClockObject self, Thread current_thread)
        
        /**
         * Returns the average frame rate since the last reset.  This is simply the
         * total number of frames divided by the total elapsed time.  This reports the
         * virtual frame rate if the clock is in (or has been in) M_non_real_time
         * mode.
         */
        """
        pass

    def getRealTime(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_real_time(ClockObject self)
        
        /**
         * Returns the actual number of seconds elapsed since the ClockObject was
         * created, or since it was last reset.  This is useful for doing real timing
         * measurements, e.g.  for performance statistics.
         *
         * This returns the most precise timer we have for short time intervals, but
         * it may tend to drift over the long haul.  If more accurate timekeeping is
         * needed over a long period of time, use get_long_time() instead.
         */
        """
        pass

    def get_average_frame_rate(self, ClockObject_self, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_average_frame_rate(ClockObject self, Thread current_thread)
        
        /**
         * Returns the average frame rate in number of frames per second over the last
         * get_average_frame_rate_interval() seconds.  This measures the virtual frame
         * rate if the clock is in M_non_real_time mode.
         */
        """
        pass

    def get_average_frame_rate_interval(self, ClockObject_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_average_frame_rate_interval(ClockObject self)
        
        /**
         * Returns the interval of time (in seconds) over which
         * get_average_frame_rate() averages the number of frames per second to
         * compute the frame rate.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_degrade_factor(self, ClockObject_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_degrade_factor(ClockObject self)
        
        /**
         * In degrade mode, returns the ratio by which the performance is degraded.  A
         * value of 2.0 causes the clock to be slowed down by a factor of two
         * (reducing performance to 1/2 what would be otherwise).
         *
         * This has no effect if mode is not M_degrade.
         */
        """
        pass

    def get_dt(self, ClockObject_self, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_dt(ClockObject self, Thread current_thread)
        
        /**
         * Returns the elapsed time for the previous frame: the number of seconds
         * elapsed between the last two calls to tick().
         */
        """
        pass

    def get_frame_count(self, ClockObject_self, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_frame_count(ClockObject self, Thread current_thread)
        
        /**
         * Returns the number of times tick() has been called since the ClockObject
         * was created, or since it was last reset.  This is generally the number of
         * frames that have been rendered.
         */
        """
        pass

    def get_frame_time(self, ClockObject_self, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_frame_time(ClockObject self, Thread current_thread)
        
        /**
         * Returns the time in seconds as of the last time tick() was called
         * (typically, this will be as of the start of the current frame).
         *
         * This is generally the kind of time you want to ask for in most rendering
         * and animation contexts, since it's important that all of the animation for
         * a given frame remains in sync with each other.
         */
        """
        pass

    def get_global_clock(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_global_clock()
        
        /**
         * Returns a pointer to the global ClockObject.  This is the ClockObject that
         * most code should use for handling scene graph rendering and animation.
         */
        """
        pass

    def get_long_time(self, ClockObject_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_long_time(ClockObject self)
        
        /**
         * Returns the actual number of seconds elapsed since the ClockObject was
         * created, or since it was last reset.
         *
         * This is similar to get_real_time(), except that it uses the most accurate
         * counter we have over a long period of time, and so it is less likely to
         * drift.  However, it may not be very precise for measuring short intervals.
         * On Windows, for instace, this is only accurate to within about 55
         * milliseconds.
         */
        """
        pass

    def get_max_dt(self, ClockObject_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_max_dt(ClockObject self)
        
        /**
         * Returns the current maximum allowable time elapsed between any two frames.
         * See set_max_dt().
         */
        """
        pass

    def get_max_frame_duration(self, ClockObject_self, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_max_frame_duration(ClockObject self, Thread current_thread)
        
        /**
         * Returns the maximum frame duration over the last
         * get_average_frame_rate_interval() seconds.
         */
        """
        pass

    def get_mode(self, ClockObject_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_mode(ClockObject self)
        
        /**
         * Returns the current mode of the clock.  See set_mode().
         */
        """
        pass

    def get_net_frame_rate(self, ClockObject_self, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_net_frame_rate(ClockObject self, Thread current_thread)
        
        /**
         * Returns the average frame rate since the last reset.  This is simply the
         * total number of frames divided by the total elapsed time.  This reports the
         * virtual frame rate if the clock is in (or has been in) M_non_real_time
         * mode.
         */
        """
        pass

    def get_real_time(self, ClockObject_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_real_time(ClockObject self)
        
        /**
         * Returns the actual number of seconds elapsed since the ClockObject was
         * created, or since it was last reset.  This is useful for doing real timing
         * measurements, e.g.  for performance statistics.
         *
         * This returns the most precise timer we have for short time intervals, but
         * it may tend to drift over the long haul.  If more accurate timekeeping is
         * needed over a long period of time, use get_long_time() instead.
         */
        """
        pass

    def reset(self, const_ClockObject_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        reset(const ClockObject self)
        
        /**
         * Simultaneously resets both the time and the frame count to zero.
         */
        """
        pass

    def setAverageFrameRateInterval(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_average_frame_rate_interval(const ClockObject self, double time)
        
        /**
         * Specifies the interval of time (in seconds) over which
         * get_average_frame_rate() averages the number of frames per second to
         * compute the frame rate.  Changing this does not necessarily immediately
         * change the result of get_average_frame_rate(), until this interval of time
         * has elapsed again.
         *
         * Setting this to zero disables the computation of get_average_frame_rate().
         */
        """
        pass

    def setDegradeFactor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_degrade_factor(const ClockObject self, double degrade_factor)
        
        /**
         * In degrade mode, sets the ratio by which the performance is degraded.  A
         * value of 2.0 causes the clock to be slowed down by a factor of two
         * (reducing performance to 1/2 what would be otherwise).
         *
         * This has no effect if mode is not M_degrade.
         */
        """
        pass

    def setDt(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_dt(const ClockObject self, double dt)
        
        /**
         * In non-real-time mode, sets the number of seconds that should appear to
         * elapse between frames.  In forced mode or limited mode, sets our target dt.
         * In normal mode, this has no effect.
         *
         * Also see set_frame_rate(), which is a different way to specify the same
         * quantity.
         */
        """
        pass

    def setFrameCount(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_frame_count(const ClockObject self, int frame_count, Thread current_thread)
        
        /**
         * Resets the number of frames counted to the indicated number.  Also see
         * reset(), set_real_time(), and set_frame_time().
         */
        """
        pass

    def setFrameRate(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_frame_rate(const ClockObject self, double frame_rate)
        
        /**
         * In non-real-time mode, sets the number of frames per second that we should
         * appear to be running.  In forced mode or limited mode, sets our target
         * frame rate.  In normal mode, this has no effect.
         *
         * Also see set_dt(), which is a different way to specify the same quantity.
         */
        """
        pass

    def setFrameTime(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_frame_time(const ClockObject self, double time, Thread current_thread)
        
        /**
         * Changes the time as reported for the current frame to the indicated time.
         * Normally, the way to adjust the frame time is via tick(); this function is
         * provided only for occasional special adjustments.
         */
        """
        pass

    def setMaxDt(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_max_dt(const ClockObject self, double max_dt)
        
        /**
         * Sets a limit on the value returned by get_dt().  If this value is less than
         * zero, no limit is imposed; otherwise, this is the maximum value that will
         * ever be returned by get_dt(), regardless of how much time has actually
         * elapsed between frames.
         *
         * This limit is only imposed in real-time mode; in non-real-time mode, the dt
         * is fixed anyway and max_dt is ignored.
         *
         * This is generally used to guarantee reasonable behavior even in the
         * presence of a very slow or chuggy frame rame.
         */
        """
        pass

    def setMode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_mode(const ClockObject self, int mode)
        
        /**
         * Changes the mode of the clock.  Normally, the clock is in mode M_normal.
         * In this mode, each call to tick() will set the value returned by
         * get_frame_time() to the current real time; thus, the clock simply reports
         * time advancing.
         *
         * Other possible modes:
         *
         * M_non_real_time - the clock ignores real time completely; at each call to
         * tick(), it pretends that exactly dt seconds have elapsed since the last
         * call to tick().  You may set the value of dt with set_dt() or
         * set_frame_rate().
         *
         * M_limited - the clock will run as fast as it can, as in M_normal, but will
         * not run faster than the rate specified by set_frame_rate().  If the
         * application would run faster than this rate, the clock will slow down the
         * application.
         *
         * M_integer - the clock will run as fast as it can, but the rate will be
         * constrained to be an integer multiple or divisor of the rate specified by
         * set_frame_rate().  The clock will slow down the application a bit to
         * guarantee this.
         *
         * M_integer_limited - a combination of M_limited and M_integer; the clock
         * will not run faster than set_frame_rate(), and if it runs slower, it will
         * run at a integer divisor of that rate.
         *
         * M_forced - the clock forces the application to run at the rate specified by
         * set_frame_rate().  If the application would run faster than this rate, the
         * clock will slow down the application; if the application would run slower
         * than this rate, the clock slows down time so that the application believes
         * it is running at the given rate.
         *
         * M_degrade - the clock runs at real time, but the application is slowed down
         * by a set factor of its frame rate, specified by set_degrade_factor().
         *
         * M_slave - the clock does not advance, but relies on the user to call
         * set_frame_time() and/or set_frame_count() each frame.
         */
        """
        pass

    def setRealTime(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_real_time(const ClockObject self, double time)
        
        /**
         * Resets the clock to the indicated time.  This changes only the real time of
         * the clock as reported by get_real_time(), but does not immediately change
         * the time reported by get_frame_time()--that will change after the next call
         * to tick().  Also see reset(), set_frame_time(), and set_frame_count().
         */
        """
        pass

    def set_average_frame_rate_interval(self, const_ClockObject_self, double_time): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_average_frame_rate_interval(const ClockObject self, double time)
        
        /**
         * Specifies the interval of time (in seconds) over which
         * get_average_frame_rate() averages the number of frames per second to
         * compute the frame rate.  Changing this does not necessarily immediately
         * change the result of get_average_frame_rate(), until this interval of time
         * has elapsed again.
         *
         * Setting this to zero disables the computation of get_average_frame_rate().
         */
        """
        pass

    def set_degrade_factor(self, const_ClockObject_self, double_degrade_factor): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_degrade_factor(const ClockObject self, double degrade_factor)
        
        /**
         * In degrade mode, sets the ratio by which the performance is degraded.  A
         * value of 2.0 causes the clock to be slowed down by a factor of two
         * (reducing performance to 1/2 what would be otherwise).
         *
         * This has no effect if mode is not M_degrade.
         */
        """
        pass

    def set_dt(self, const_ClockObject_self, double_dt): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_dt(const ClockObject self, double dt)
        
        /**
         * In non-real-time mode, sets the number of seconds that should appear to
         * elapse between frames.  In forced mode or limited mode, sets our target dt.
         * In normal mode, this has no effect.
         *
         * Also see set_frame_rate(), which is a different way to specify the same
         * quantity.
         */
        """
        pass

    def set_frame_count(self, const_ClockObject_self, int_frame_count, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_frame_count(const ClockObject self, int frame_count, Thread current_thread)
        
        /**
         * Resets the number of frames counted to the indicated number.  Also see
         * reset(), set_real_time(), and set_frame_time().
         */
        """
        pass

    def set_frame_rate(self, const_ClockObject_self, double_frame_rate): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_frame_rate(const ClockObject self, double frame_rate)
        
        /**
         * In non-real-time mode, sets the number of frames per second that we should
         * appear to be running.  In forced mode or limited mode, sets our target
         * frame rate.  In normal mode, this has no effect.
         *
         * Also see set_dt(), which is a different way to specify the same quantity.
         */
        """
        pass

    def set_frame_time(self, const_ClockObject_self, double_time, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_frame_time(const ClockObject self, double time, Thread current_thread)
        
        /**
         * Changes the time as reported for the current frame to the indicated time.
         * Normally, the way to adjust the frame time is via tick(); this function is
         * provided only for occasional special adjustments.
         */
        """
        pass

    def set_max_dt(self, const_ClockObject_self, double_max_dt): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_max_dt(const ClockObject self, double max_dt)
        
        /**
         * Sets a limit on the value returned by get_dt().  If this value is less than
         * zero, no limit is imposed; otherwise, this is the maximum value that will
         * ever be returned by get_dt(), regardless of how much time has actually
         * elapsed between frames.
         *
         * This limit is only imposed in real-time mode; in non-real-time mode, the dt
         * is fixed anyway and max_dt is ignored.
         *
         * This is generally used to guarantee reasonable behavior even in the
         * presence of a very slow or chuggy frame rame.
         */
        """
        pass

    def set_mode(self, const_ClockObject_self, int_mode): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_mode(const ClockObject self, int mode)
        
        /**
         * Changes the mode of the clock.  Normally, the clock is in mode M_normal.
         * In this mode, each call to tick() will set the value returned by
         * get_frame_time() to the current real time; thus, the clock simply reports
         * time advancing.
         *
         * Other possible modes:
         *
         * M_non_real_time - the clock ignores real time completely; at each call to
         * tick(), it pretends that exactly dt seconds have elapsed since the last
         * call to tick().  You may set the value of dt with set_dt() or
         * set_frame_rate().
         *
         * M_limited - the clock will run as fast as it can, as in M_normal, but will
         * not run faster than the rate specified by set_frame_rate().  If the
         * application would run faster than this rate, the clock will slow down the
         * application.
         *
         * M_integer - the clock will run as fast as it can, but the rate will be
         * constrained to be an integer multiple or divisor of the rate specified by
         * set_frame_rate().  The clock will slow down the application a bit to
         * guarantee this.
         *
         * M_integer_limited - a combination of M_limited and M_integer; the clock
         * will not run faster than set_frame_rate(), and if it runs slower, it will
         * run at a integer divisor of that rate.
         *
         * M_forced - the clock forces the application to run at the rate specified by
         * set_frame_rate().  If the application would run faster than this rate, the
         * clock will slow down the application; if the application would run slower
         * than this rate, the clock slows down time so that the application believes
         * it is running at the given rate.
         *
         * M_degrade - the clock runs at real time, but the application is slowed down
         * by a set factor of its frame rate, specified by set_degrade_factor().
         *
         * M_slave - the clock does not advance, but relies on the user to call
         * set_frame_time() and/or set_frame_count() each frame.
         */
        """
        pass

    def set_real_time(self, const_ClockObject_self, double_time): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_real_time(const ClockObject self, double time)
        
        /**
         * Resets the clock to the indicated time.  This changes only the real time of
         * the clock as reported by get_real_time(), but does not immediately change
         * the time reported by get_frame_time()--that will change after the next call
         * to tick().  Also see reset(), set_frame_time(), and set_frame_count().
         */
        """
        pass

    def syncFrameTime(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        sync_frame_time(const ClockObject self, Thread current_thread)
        
        /**
         * Resets the frame time to the current real time.  This is similar to tick(),
         * except that it does not advance the frame counter and does not affect dt.
         * This is intended to be used in the middle of a particularly long frame to
         * compensate for the time that has already elapsed.
         *
         * In non-real-time mode, this function has no effect (because in this mode
         * all frames take the same length of time).
         */
        """
        pass

    def sync_frame_time(self, const_ClockObject_self, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        sync_frame_time(const ClockObject self, Thread current_thread)
        
        /**
         * Resets the frame time to the current real time.  This is similar to tick(),
         * except that it does not advance the frame counter and does not affect dt.
         * This is intended to be used in the middle of a particularly long frame to
         * compensate for the time that has already elapsed.
         *
         * In non-real-time mode, this function has no effect (because in this mode
         * all frames take the same length of time).
         */
        """
        pass

    def tick(self, const_ClockObject_self, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        tick(const ClockObject self, Thread current_thread)
        
        /**
         * Instructs the clock that a new frame has just begun.  In normal, real-time
         * mode, get_frame_time() will henceforth report the time as of this instant
         * as the current start-of-frame time.  In non-real-time mode,
         * get_frame_time() will be incremented by the value of dt.
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

    average_frame_rate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    average_frame_rate_interval = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    degrade_factor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dt = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    frame_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    frame_time = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    long_time = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    max_dt = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    max_frame_duration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    real_time = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        'MDegrade': 3,
        'MForced': 2,
        'MInteger': 6,
        'MIntegerLimited': 7,
        'MLimited': 5,
        'MNonRealTime': 1,
        'MNormal': 0,
        'MSlave': 4,
        'M_degrade': 3,
        'M_forced': 2,
        'M_integer': 6,
        'M_integer_limited': 7,
        'M_limited': 5,
        'M_non_real_time': 1,
        'M_normal': 0,
        'M_slave': 4,
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.ClockObject' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.ClockObject' objects>"
        '__doc__': '/**\n * A ClockObject keeps track of elapsed real time and discrete time.  In\n * normal mode, get_frame_time() returns the time as of the last time tick()\n * was called.  This is the "discrete" time, and is usually used to get the\n * time as of, for instance, the beginning of the current frame.\n *\n * In other modes, as set by set_mode() or the clock-mode config variable,\n * get_frame_time() may return other values to simulate different timing\n * effects, for instance to perform non-real-time animation.  See set_mode().\n *\n * In all modes, get_real_time() always returns the elapsed real time in\n * seconds since the ClockObject was constructed, or since it was last reset.\n *\n * You can create your own ClockObject whenever you want to have your own\n * local timer.  There is also a default, global ClockObject intended to\n * represent global time for the application; this is normally set up to tick\n * every frame so that its get_frame_time() will return the time for the\n * current frame.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.ClockObject' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE371970>'
        'average_frame_rate': None, # (!) real value is "<attribute 'average_frame_rate' of 'panda3d.core.ClockObject' objects>"
        'average_frame_rate_interval': None, # (!) real value is "<attribute 'average_frame_rate_interval' of 'panda3d.core.ClockObject' objects>"
        'calcFrameRateDeviation': None, # (!) real value is "<method 'calcFrameRateDeviation' of 'panda3d.core.ClockObject' objects>"
        'calc_frame_rate_deviation': None, # (!) real value is "<method 'calc_frame_rate_deviation' of 'panda3d.core.ClockObject' objects>"
        'checkErrors': None, # (!) real value is "<method 'checkErrors' of 'panda3d.core.ClockObject' objects>"
        'check_errors': None, # (!) real value is "<method 'check_errors' of 'panda3d.core.ClockObject' objects>"
        'degrade_factor': None, # (!) real value is "<attribute 'degrade_factor' of 'panda3d.core.ClockObject' objects>"
        'dt': None, # (!) real value is "<attribute 'dt' of 'panda3d.core.ClockObject' objects>"
        'frame_count': None, # (!) real value is "<attribute 'frame_count' of 'panda3d.core.ClockObject' objects>"
        'frame_time': None, # (!) real value is "<attribute 'frame_time' of 'panda3d.core.ClockObject' objects>"
        'getAverageFrameRate': None, # (!) real value is "<method 'getAverageFrameRate' of 'panda3d.core.ClockObject' objects>"
        'getAverageFrameRateInterval': None, # (!) real value is "<method 'getAverageFrameRateInterval' of 'panda3d.core.ClockObject' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE371970>)>'
        'getDegradeFactor': None, # (!) real value is "<method 'getDegradeFactor' of 'panda3d.core.ClockObject' objects>"
        'getDt': None, # (!) real value is "<method 'getDt' of 'panda3d.core.ClockObject' objects>"
        'getFrameCount': None, # (!) real value is "<method 'getFrameCount' of 'panda3d.core.ClockObject' objects>"
        'getFrameTime': None, # (!) real value is "<method 'getFrameTime' of 'panda3d.core.ClockObject' objects>"
        'getGlobalClock': None, # (!) real value is '<staticmethod(<built-in method getGlobalClock of type object at 0x00007FFCFE371970>)>'
        'getLongTime': None, # (!) real value is "<method 'getLongTime' of 'panda3d.core.ClockObject' objects>"
        'getMaxDt': None, # (!) real value is "<method 'getMaxDt' of 'panda3d.core.ClockObject' objects>"
        'getMaxFrameDuration': None, # (!) real value is "<method 'getMaxFrameDuration' of 'panda3d.core.ClockObject' objects>"
        'getMode': None, # (!) real value is "<method 'getMode' of 'panda3d.core.ClockObject' objects>"
        'getNetFrameRate': None, # (!) real value is "<method 'getNetFrameRate' of 'panda3d.core.ClockObject' objects>"
        'getRealTime': None, # (!) real value is "<method 'getRealTime' of 'panda3d.core.ClockObject' objects>"
        'get_average_frame_rate': None, # (!) real value is "<method 'get_average_frame_rate' of 'panda3d.core.ClockObject' objects>"
        'get_average_frame_rate_interval': None, # (!) real value is "<method 'get_average_frame_rate_interval' of 'panda3d.core.ClockObject' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE371970>)>'
        'get_degrade_factor': None, # (!) real value is "<method 'get_degrade_factor' of 'panda3d.core.ClockObject' objects>"
        'get_dt': None, # (!) real value is "<method 'get_dt' of 'panda3d.core.ClockObject' objects>"
        'get_frame_count': None, # (!) real value is "<method 'get_frame_count' of 'panda3d.core.ClockObject' objects>"
        'get_frame_time': None, # (!) real value is "<method 'get_frame_time' of 'panda3d.core.ClockObject' objects>"
        'get_global_clock': None, # (!) real value is '<staticmethod(<built-in method get_global_clock of type object at 0x00007FFCFE371970>)>'
        'get_long_time': None, # (!) real value is "<method 'get_long_time' of 'panda3d.core.ClockObject' objects>"
        'get_max_dt': None, # (!) real value is "<method 'get_max_dt' of 'panda3d.core.ClockObject' objects>"
        'get_max_frame_duration': None, # (!) real value is "<method 'get_max_frame_duration' of 'panda3d.core.ClockObject' objects>"
        'get_mode': None, # (!) real value is "<method 'get_mode' of 'panda3d.core.ClockObject' objects>"
        'get_net_frame_rate': None, # (!) real value is "<method 'get_net_frame_rate' of 'panda3d.core.ClockObject' objects>"
        'get_real_time': None, # (!) real value is "<method 'get_real_time' of 'panda3d.core.ClockObject' objects>"
        'long_time': None, # (!) real value is "<attribute 'long_time' of 'panda3d.core.ClockObject' objects>"
        'max_dt': None, # (!) real value is "<attribute 'max_dt' of 'panda3d.core.ClockObject' objects>"
        'max_frame_duration': None, # (!) real value is "<attribute 'max_frame_duration' of 'panda3d.core.ClockObject' objects>"
        'mode': None, # (!) real value is "<attribute 'mode' of 'panda3d.core.ClockObject' objects>"
        'real_time': None, # (!) real value is "<attribute 'real_time' of 'panda3d.core.ClockObject' objects>"
        'reset': None, # (!) real value is "<method 'reset' of 'panda3d.core.ClockObject' objects>"
        'setAverageFrameRateInterval': None, # (!) real value is "<method 'setAverageFrameRateInterval' of 'panda3d.core.ClockObject' objects>"
        'setDegradeFactor': None, # (!) real value is "<method 'setDegradeFactor' of 'panda3d.core.ClockObject' objects>"
        'setDt': None, # (!) real value is "<method 'setDt' of 'panda3d.core.ClockObject' objects>"
        'setFrameCount': None, # (!) real value is "<method 'setFrameCount' of 'panda3d.core.ClockObject' objects>"
        'setFrameRate': None, # (!) real value is "<method 'setFrameRate' of 'panda3d.core.ClockObject' objects>"
        'setFrameTime': None, # (!) real value is "<method 'setFrameTime' of 'panda3d.core.ClockObject' objects>"
        'setMaxDt': None, # (!) real value is "<method 'setMaxDt' of 'panda3d.core.ClockObject' objects>"
        'setMode': None, # (!) real value is "<method 'setMode' of 'panda3d.core.ClockObject' objects>"
        'setRealTime': None, # (!) real value is "<method 'setRealTime' of 'panda3d.core.ClockObject' objects>"
        'set_average_frame_rate_interval': None, # (!) real value is "<method 'set_average_frame_rate_interval' of 'panda3d.core.ClockObject' objects>"
        'set_degrade_factor': None, # (!) real value is "<method 'set_degrade_factor' of 'panda3d.core.ClockObject' objects>"
        'set_dt': None, # (!) real value is "<method 'set_dt' of 'panda3d.core.ClockObject' objects>"
        'set_frame_count': None, # (!) real value is "<method 'set_frame_count' of 'panda3d.core.ClockObject' objects>"
        'set_frame_rate': None, # (!) real value is "<method 'set_frame_rate' of 'panda3d.core.ClockObject' objects>"
        'set_frame_time': None, # (!) real value is "<method 'set_frame_time' of 'panda3d.core.ClockObject' objects>"
        'set_max_dt': None, # (!) real value is "<method 'set_max_dt' of 'panda3d.core.ClockObject' objects>"
        'set_mode': None, # (!) real value is "<method 'set_mode' of 'panda3d.core.ClockObject' objects>"
        'set_real_time': None, # (!) real value is "<method 'set_real_time' of 'panda3d.core.ClockObject' objects>"
        'syncFrameTime': None, # (!) real value is "<method 'syncFrameTime' of 'panda3d.core.ClockObject' objects>"
        'sync_frame_time': None, # (!) real value is "<method 'sync_frame_time' of 'panda3d.core.ClockObject' objects>"
        'tick': None, # (!) real value is "<method 'tick' of 'panda3d.core.ClockObject' objects>"
    }
    MDegrade = 3
    MForced = 2
    MInteger = 6
    MIntegerLimited = 7
    MLimited = 5
    MNonRealTime = 1
    MNormal = 0
    MSlave = 4
    M_degrade = 3
    M_forced = 2
    M_integer = 6
    M_integer_limited = 7
    M_limited = 5
    M_non_real_time = 1
    M_normal = 0
    M_slave = 4


