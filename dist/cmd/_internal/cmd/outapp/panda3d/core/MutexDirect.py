# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class MutexDirect(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * This class implements a standard mutex by making direct calls to the
     * underlying implementation layer.  It doesn't perform any debugging
     * operations.
     */
    """
    def acquire(self, MutexDirect_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        acquire(MutexDirect self)
        
        /**
         * Grabs the mutex if it is available.  If it is not available, blocks until
         * it becomes available, then grabs it.  In either case, the function does not
         * return until the mutex is held; you should then call unlock().
         *
         * This method is considered const so that you can lock and unlock const
         * mutexes, mainly to allow thread-safe access to otherwise const data.
         *
         * Also see MutexHolder.
         */
        """
        pass

    def clearName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_name(const MutexDirect self)
        
        /**
         * The mutex name is only defined when compiling in DEBUG_THREADS mode.
         */
        """
        pass

    def clear_name(self, const_MutexDirect_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_name(const MutexDirect self)
        
        /**
         * The mutex name is only defined when compiling in DEBUG_THREADS mode.
         */
        """
        pass

    def debugIsLocked(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        debug_is_locked(MutexDirect self)
        
        /**
         * Returns true if the current thread has locked the Mutex, false otherwise.
         * This method is only intended for use in debugging, hence the method name;
         * in the MutexDirect case, it always returns true, since there's not a
         * reliable way to determine this otherwise.
         */
        """
        pass

    def debug_is_locked(self, MutexDirect_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        debug_is_locked(MutexDirect self)
        
        /**
         * Returns true if the current thread has locked the Mutex, false otherwise.
         * This method is only intended for use in debugging, hence the method name;
         * in the MutexDirect case, it always returns true, since there's not a
         * reliable way to determine this otherwise.
         */
        """
        pass

    def getName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_name(MutexDirect self)
        
        /**
         * The mutex name is only defined when compiling in DEBUG_THREADS mode.
         */
        """
        pass

    def get_name(self, MutexDirect_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_name(MutexDirect self)
        
        /**
         * The mutex name is only defined when compiling in DEBUG_THREADS mode.
         */
        """
        pass

    def hasName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_name(MutexDirect self)
        
        /**
         * The mutex name is only defined when compiling in DEBUG_THREADS mode.
         */
        """
        pass

    def has_name(self, MutexDirect_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_name(MutexDirect self)
        
        /**
         * The mutex name is only defined when compiling in DEBUG_THREADS mode.
         */
        """
        pass

    def output(self, MutexDirect_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(MutexDirect self, ostream out)
        
        /**
         * This method is declared virtual in MutexDebug, but non-virtual in
         * MutexDirect.
         */
        """
        pass

    def release(self, MutexDirect_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        release(MutexDirect self)
        
        /**
         * Releases the mutex.  It is an error to call this if the mutex was not
         * already locked.
         *
         * This method is considered const so that you can lock and unlock const
         * mutexes, mainly to allow thread-safe access to otherwise const data.
         */
        """
        pass

    def setName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_name(const MutexDirect self, str name)
        
        /**
         * The mutex name is only defined when compiling in DEBUG_THREADS mode.
         */
        """
        pass

    def set_name(self, const_MutexDirect_self, str_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_name(const MutexDirect self, str name)
        
        /**
         * The mutex name is only defined when compiling in DEBUG_THREADS mode.
         */
        """
        pass

    def tryAcquire(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        try_acquire(MutexDirect self)
        
        /**
         * Returns immediately, with a true value indicating the mutex has been
         * acquired, and false indicating it has not.
         */
        """
        pass

    def try_acquire(self, MutexDirect_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        try_acquire(MutexDirect self)
        
        /**
         * Returns immediately, with a true value indicating the mutex has been
         * acquired, and false indicating it has not.
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
        '__doc__': "/**\n * This class implements a standard mutex by making direct calls to the\n * underlying implementation layer.  It doesn't perform any debugging\n * operations.\n */",
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.MutexDirect' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2EB330>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.MutexDirect' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.MutexDirect' objects>"
        'acquire': None, # (!) real value is "<method 'acquire' of 'panda3d.core.MutexDirect' objects>"
        'clearName': None, # (!) real value is "<method 'clearName' of 'panda3d.core.MutexDirect' objects>"
        'clear_name': None, # (!) real value is "<method 'clear_name' of 'panda3d.core.MutexDirect' objects>"
        'debugIsLocked': None, # (!) real value is "<method 'debugIsLocked' of 'panda3d.core.MutexDirect' objects>"
        'debug_is_locked': None, # (!) real value is "<method 'debug_is_locked' of 'panda3d.core.MutexDirect' objects>"
        'getName': None, # (!) real value is "<method 'getName' of 'panda3d.core.MutexDirect' objects>"
        'get_name': None, # (!) real value is "<method 'get_name' of 'panda3d.core.MutexDirect' objects>"
        'hasName': None, # (!) real value is "<method 'hasName' of 'panda3d.core.MutexDirect' objects>"
        'has_name': None, # (!) real value is "<method 'has_name' of 'panda3d.core.MutexDirect' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.MutexDirect' objects>"
        'release': None, # (!) real value is "<method 'release' of 'panda3d.core.MutexDirect' objects>"
        'setName': None, # (!) real value is "<method 'setName' of 'panda3d.core.MutexDirect' objects>"
        'set_name': None, # (!) real value is "<method 'set_name' of 'panda3d.core.MutexDirect' objects>"
        'tryAcquire': None, # (!) real value is "<method 'tryAcquire' of 'panda3d.core.MutexDirect' objects>"
        'try_acquire': None, # (!) real value is "<method 'try_acquire' of 'panda3d.core.MutexDirect' objects>"
    }


