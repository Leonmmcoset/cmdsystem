# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class TrueClock(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * An interface to whatever real-time clock we might have available in the
     * current environment.  There is only one TrueClock in existence, and it
     * constructs itself.
     *
     * The TrueClock returns elapsed real time in seconds since some undefined
     * epoch.  Since it is not defined at what time precisely the clock indicates
     * zero, this value can only be meaningfully used to measure elapsed time, by
     * sampling it at two different times and subtracting.
     */
    """
    def getErrorCount(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_error_count(TrueClock self)
        
        /**
         * Returns the number of clock errors that have been detected.  Each time a
         * clock error is detected, in which the value returned by either of the above
         * methods is suspect, the value returned by this method will be incremented.
         * Applications can monitor this value and react, for instance, by
         * resynchronizing their clocks each time this value changes.
         */
        """
        pass

    def getGlobalPtr(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_global_ptr()
        
        /**
         * Returns a pointer to the one TrueClock object in the world.
         */
        """
        pass

    def getLongTime(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_long_time(const TrueClock self)
        
        // get_long_time() returns the most accurate timer we have over a long
        // interval.  It may not be very precise for measuring short intervals, but
        // it should not drift substantially over the long haul.
        
        // get_long_time() returns the most accurate timer we have over a long
        // interval.  It may not be very precise for measuring short intervals, but
        // it should not drift substantially over the long haul.
        
        /**
         *
         */
        """
        pass

    def getShortRawTime(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_short_raw_time(const TrueClock self)
        
        // get_short_raw_time() is like get_short_time(), but does not apply any
        // corrections (e.g.  paranoid-clock) to the result returned by the OS.
        
        // get_short_raw_time() is like get_short_time(), but does not apply any
        // corrections (e.g.  paranoid-clock) to the result returned by the OS.
        
        /**
         *
         */
        """
        pass

    def getShortTime(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_short_time(const TrueClock self)
        
        // get_short_time() returns the most precise timer we have over a short
        // interval.  It may tend to drift over the long haul, but it should have
        // lots of digits to measure short intervals very precisely.
        
        // get_short_time() returns the most precise timer we have over a short
        // interval.  It may tend to drift over the long haul, but it should have
        // lots of digits to measure short intervals very precisely.
        
        /**
         *
         */
        """
        pass

    def get_error_count(self, TrueClock_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_error_count(TrueClock self)
        
        /**
         * Returns the number of clock errors that have been detected.  Each time a
         * clock error is detected, in which the value returned by either of the above
         * methods is suspect, the value returned by this method will be incremented.
         * Applications can monitor this value and react, for instance, by
         * resynchronizing their clocks each time this value changes.
         */
        """
        pass

    def get_global_ptr(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_global_ptr()
        
        /**
         * Returns a pointer to the one TrueClock object in the world.
         */
        """
        pass

    def get_long_time(self, const_TrueClock_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_long_time(const TrueClock self)
        
        // get_long_time() returns the most accurate timer we have over a long
        // interval.  It may not be very precise for measuring short intervals, but
        // it should not drift substantially over the long haul.
        
        // get_long_time() returns the most accurate timer we have over a long
        // interval.  It may not be very precise for measuring short intervals, but
        // it should not drift substantially over the long haul.
        
        /**
         *
         */
        """
        pass

    def get_short_raw_time(self, const_TrueClock_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_short_raw_time(const TrueClock self)
        
        // get_short_raw_time() is like get_short_time(), but does not apply any
        // corrections (e.g.  paranoid-clock) to the result returned by the OS.
        
        // get_short_raw_time() is like get_short_time(), but does not apply any
        // corrections (e.g.  paranoid-clock) to the result returned by the OS.
        
        /**
         *
         */
        """
        pass

    def get_short_time(self, const_TrueClock_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_short_time(const TrueClock self)
        
        // get_short_time() returns the most precise timer we have over a short
        // interval.  It may tend to drift over the long haul, but it should have
        // lots of digits to measure short intervals very precisely.
        
        // get_short_time() returns the most precise timer we have over a short
        // interval.  It may tend to drift over the long haul, but it should have
        // lots of digits to measure short intervals very precisely.
        
        /**
         *
         */
        """
        pass

    def setCpuAffinity(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_cpu_affinity(TrueClock self, int mask)
        """
        pass

    def set_cpu_affinity(self, TrueClock_self, int_mask): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_cpu_affinity(TrueClock self, int mask)
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    error_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    long_time = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """// get_long_time() returns the most accurate timer we have over a long
// interval.  It may not be very precise for measuring short intervals, but
// it should not drift substantially over the long haul."""

    short_raw_time = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """// get_short_raw_time() is like get_short_time(), but does not apply any
// corrections (e.g.  paranoid-clock) to the result returned by the OS."""

    short_time = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """// get_short_time() returns the most precise timer we have over a short
// interval.  It may tend to drift over the long haul, but it should have
// lots of digits to measure short intervals very precisely."""


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * An interface to whatever real-time clock we might have available in the\n * current environment.  There is only one TrueClock in existence, and it\n * constructs itself.\n *\n * The TrueClock returns elapsed real time in seconds since some undefined\n * epoch.  Since it is not defined at what time precisely the clock indicates\n * zero, this value can only be meaningfully used to measure elapsed time, by\n * sampling it at two different times and subtracting.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.TrueClock' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE27AFB0>'
        'error_count': None, # (!) real value is "<attribute 'error_count' of 'panda3d.core.TrueClock' objects>"
        'getErrorCount': None, # (!) real value is "<method 'getErrorCount' of 'panda3d.core.TrueClock' objects>"
        'getGlobalPtr': None, # (!) real value is '<staticmethod(<built-in method getGlobalPtr of type object at 0x00007FFCFE27AFB0>)>'
        'getLongTime': None, # (!) real value is "<method 'getLongTime' of 'panda3d.core.TrueClock' objects>"
        'getShortRawTime': None, # (!) real value is "<method 'getShortRawTime' of 'panda3d.core.TrueClock' objects>"
        'getShortTime': None, # (!) real value is "<method 'getShortTime' of 'panda3d.core.TrueClock' objects>"
        'get_error_count': None, # (!) real value is "<method 'get_error_count' of 'panda3d.core.TrueClock' objects>"
        'get_global_ptr': None, # (!) real value is '<staticmethod(<built-in method get_global_ptr of type object at 0x00007FFCFE27AFB0>)>'
        'get_long_time': None, # (!) real value is "<method 'get_long_time' of 'panda3d.core.TrueClock' objects>"
        'get_short_raw_time': None, # (!) real value is "<method 'get_short_raw_time' of 'panda3d.core.TrueClock' objects>"
        'get_short_time': None, # (!) real value is "<method 'get_short_time' of 'panda3d.core.TrueClock' objects>"
        'long_time': None, # (!) real value is "<attribute 'long_time' of 'panda3d.core.TrueClock' objects>"
        'setCpuAffinity': None, # (!) real value is "<method 'setCpuAffinity' of 'panda3d.core.TrueClock' objects>"
        'set_cpu_affinity': None, # (!) real value is "<method 'set_cpu_affinity' of 'panda3d.core.TrueClock' objects>"
        'short_raw_time': None, # (!) real value is "<attribute 'short_raw_time' of 'panda3d.core.TrueClock' objects>"
        'short_time': None, # (!) real value is "<attribute 'short_time' of 'panda3d.core.TrueClock' objects>"
    }


