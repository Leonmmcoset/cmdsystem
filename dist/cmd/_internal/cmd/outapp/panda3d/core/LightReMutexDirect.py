# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class LightReMutexDirect(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * This class implements a standard lightReMutex by making direct calls to the
     * underlying implementation layer.  It doesn't perform any debugging
     * operations.
     */
    """
    def acquire(self, LightReMutexDirect_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        acquire(LightReMutexDirect self)
        acquire(LightReMutexDirect self, Thread current_thread)
        
        /**
         * Grabs the lightReMutex if it is available.  If it is not available, blocks
         * until it becomes available, then grabs it.  In either case, the function
         * does not return until the lightReMutex is held; you should then call
         * unlock().
         *
         * This method is considered const so that you can lock and unlock const
         * lightReMutexes, mainly to allow thread-safe access to otherwise const data.
         *
         * Also see LightReMutexHolder.
         */
        
        /**
         * This variant on acquire() accepts the current thread as a parameter, if it
         * is already known, as an optimization.
         */
        """
        pass

    def clearName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_name(const LightReMutexDirect self)
        
        /**
         * The mutex name is only defined when compiling in DEBUG_THREADS mode.
         */
        """
        pass

    def clear_name(self, const_LightReMutexDirect_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_name(const LightReMutexDirect self)
        
        /**
         * The mutex name is only defined when compiling in DEBUG_THREADS mode.
         */
        """
        pass

    def debugIsLocked(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        debug_is_locked(LightReMutexDirect self)
        
        /**
         * Returns true if the current thread has locked the LightReMutex, false
         * otherwise.  This method is only intended for use in debugging, hence the
         * method name; in the LightReMutexDirect case, it always returns true, since
         * there's not a reliable way to determine this otherwise.
         */
        """
        pass

    def debug_is_locked(self, LightReMutexDirect_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        debug_is_locked(LightReMutexDirect self)
        
        /**
         * Returns true if the current thread has locked the LightReMutex, false
         * otherwise.  This method is only intended for use in debugging, hence the
         * method name; in the LightReMutexDirect case, it always returns true, since
         * there's not a reliable way to determine this otherwise.
         */
        """
        pass

    def elevateLock(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        elevate_lock(LightReMutexDirect self)
        
        /**
         * This method increments the lock count, assuming the calling thread already
         * holds the lock.  After this call, release() will need to be called one
         * additional time to release the lock.
         *
         * This method really performs the same function as acquire(), but it offers a
         * potential (slight) performance benefit when the calling thread knows that
         * it already holds the lock.  It is an error to call this when the calling
         * thread does not hold the lock.
         */
        """
        pass

    def elevate_lock(self, LightReMutexDirect_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        elevate_lock(LightReMutexDirect self)
        
        /**
         * This method increments the lock count, assuming the calling thread already
         * holds the lock.  After this call, release() will need to be called one
         * additional time to release the lock.
         *
         * This method really performs the same function as acquire(), but it offers a
         * potential (slight) performance benefit when the calling thread knows that
         * it already holds the lock.  It is an error to call this when the calling
         * thread does not hold the lock.
         */
        """
        pass

    def getName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_name(LightReMutexDirect self)
        
        /**
         * The mutex name is only defined when compiling in DEBUG_THREADS mode.
         */
        """
        pass

    def get_name(self, LightReMutexDirect_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_name(LightReMutexDirect self)
        
        /**
         * The mutex name is only defined when compiling in DEBUG_THREADS mode.
         */
        """
        pass

    def hasName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_name(LightReMutexDirect self)
        
        /**
         * The mutex name is only defined when compiling in DEBUG_THREADS mode.
         */
        """
        pass

    def has_name(self, LightReMutexDirect_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_name(LightReMutexDirect self)
        
        /**
         * The mutex name is only defined when compiling in DEBUG_THREADS mode.
         */
        """
        pass

    def output(self, LightReMutexDirect_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(LightReMutexDirect self, ostream out)
        
        /**
         * This method is declared virtual in MutexDebug, but non-virtual in
         * LightReMutexDirect.
         */
        """
        pass

    def release(self, LightReMutexDirect_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        release(LightReMutexDirect self)
        
        /**
         * Releases the lightReMutex.  It is an error to call this if the lightReMutex
         * was not already locked.
         *
         * This method is considered const so that you can lock and unlock const
         * lightReMutexes, mainly to allow thread-safe access to otherwise const data.
         */
        """
        pass

    def setName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_name(const LightReMutexDirect self, str name)
        
        /**
         * The mutex name is only defined when compiling in DEBUG_THREADS mode.
         */
        """
        pass

    def set_name(self, const_LightReMutexDirect_self, str_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_name(const LightReMutexDirect self, str name)
        
        /**
         * The mutex name is only defined when compiling in DEBUG_THREADS mode.
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
        '__doc__': "/**\n * This class implements a standard lightReMutex by making direct calls to the\n * underlying implementation layer.  It doesn't perform any debugging\n * operations.\n */",
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.LightReMutexDirect' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2EC720>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.LightReMutexDirect' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.LightReMutexDirect' objects>"
        'acquire': None, # (!) real value is "<method 'acquire' of 'panda3d.core.LightReMutexDirect' objects>"
        'clearName': None, # (!) real value is "<method 'clearName' of 'panda3d.core.LightReMutexDirect' objects>"
        'clear_name': None, # (!) real value is "<method 'clear_name' of 'panda3d.core.LightReMutexDirect' objects>"
        'debugIsLocked': None, # (!) real value is "<method 'debugIsLocked' of 'panda3d.core.LightReMutexDirect' objects>"
        'debug_is_locked': None, # (!) real value is "<method 'debug_is_locked' of 'panda3d.core.LightReMutexDirect' objects>"
        'elevateLock': None, # (!) real value is "<method 'elevateLock' of 'panda3d.core.LightReMutexDirect' objects>"
        'elevate_lock': None, # (!) real value is "<method 'elevate_lock' of 'panda3d.core.LightReMutexDirect' objects>"
        'getName': None, # (!) real value is "<method 'getName' of 'panda3d.core.LightReMutexDirect' objects>"
        'get_name': None, # (!) real value is "<method 'get_name' of 'panda3d.core.LightReMutexDirect' objects>"
        'hasName': None, # (!) real value is "<method 'hasName' of 'panda3d.core.LightReMutexDirect' objects>"
        'has_name': None, # (!) real value is "<method 'has_name' of 'panda3d.core.LightReMutexDirect' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.LightReMutexDirect' objects>"
        'release': None, # (!) real value is "<method 'release' of 'panda3d.core.LightReMutexDirect' objects>"
        'setName': None, # (!) real value is "<method 'setName' of 'panda3d.core.LightReMutexDirect' objects>"
        'set_name': None, # (!) real value is "<method 'set_name' of 'panda3d.core.LightReMutexDirect' objects>"
    }


