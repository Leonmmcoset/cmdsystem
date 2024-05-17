# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class LightMutexDirect(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * This class implements a lightweight Mutex by making direct calls to the
     * underlying implementation layer.  It doesn't perform any debugging
     * operations.
     */
    """
    def acquire(self, LightMutexDirect_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        acquire(LightMutexDirect self)
        
        /**
         * Grabs the lightMutex if it is available.  If it is not available, blocks
         * until it becomes available, then grabs it.  In either case, the function
         * does not return until the lightMutex is held; you should then call
         * unlock().
         *
         * This method is considered const so that you can lock and unlock const
         * lightMutexes, mainly to allow thread-safe access to otherwise const data.
         *
         * Also see LightMutexHolder.
         */
        """
        pass

    def clearName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_name(const LightMutexDirect self)
        
        /**
         * The lightMutex name is only defined when compiling in DEBUG_THREADS mode.
         */
        """
        pass

    def clear_name(self, const_LightMutexDirect_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_name(const LightMutexDirect self)
        
        /**
         * The lightMutex name is only defined when compiling in DEBUG_THREADS mode.
         */
        """
        pass

    def debugIsLocked(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        debug_is_locked(LightMutexDirect self)
        
        /**
         * Returns true if the current thread has locked the LightMutex, false
         * otherwise.  This method is only intended for use in debugging, hence the
         * method name; in the LightMutexDirect case, it always returns true, since
         * there's not a reliable way to determine this otherwise.
         */
        """
        pass

    def debug_is_locked(self, LightMutexDirect_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        debug_is_locked(LightMutexDirect self)
        
        /**
         * Returns true if the current thread has locked the LightMutex, false
         * otherwise.  This method is only intended for use in debugging, hence the
         * method name; in the LightMutexDirect case, it always returns true, since
         * there's not a reliable way to determine this otherwise.
         */
        """
        pass

    def getName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_name(LightMutexDirect self)
        
        /**
         * The lightMutex name is only defined when compiling in DEBUG_THREADS mode.
         */
        """
        pass

    def get_name(self, LightMutexDirect_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_name(LightMutexDirect self)
        
        /**
         * The lightMutex name is only defined when compiling in DEBUG_THREADS mode.
         */
        """
        pass

    def hasName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_name(LightMutexDirect self)
        
        /**
         * The lightMutex name is only defined when compiling in DEBUG_THREADS mode.
         */
        """
        pass

    def has_name(self, LightMutexDirect_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_name(LightMutexDirect self)
        
        /**
         * The lightMutex name is only defined when compiling in DEBUG_THREADS mode.
         */
        """
        pass

    def output(self, LightMutexDirect_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(LightMutexDirect self, ostream out)
        
        /**
         * This method is declared virtual in LightMutexDebug, but non-virtual in
         * LightMutexDirect.
         */
        """
        pass

    def release(self, LightMutexDirect_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        release(LightMutexDirect self)
        
        /**
         * Releases the lightMutex.  It is an error to call this if the lightMutex was
         * not already locked.
         *
         * This method is considered const so that you can lock and unlock const
         * lightMutexes, mainly to allow thread-safe access to otherwise const data.
         */
        """
        pass

    def setName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_name(const LightMutexDirect self, str name)
        
        /**
         * The lightMutex name is only defined when compiling in DEBUG_THREADS mode.
         */
        """
        pass

    def set_name(self, const_LightMutexDirect_self, str_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_name(const LightMutexDirect self, str name)
        
        /**
         * The lightMutex name is only defined when compiling in DEBUG_THREADS mode.
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
        '__doc__': "/**\n * This class implements a lightweight Mutex by making direct calls to the\n * underlying implementation layer.  It doesn't perform any debugging\n * operations.\n */",
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.LightMutexDirect' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2EC380>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.LightMutexDirect' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.LightMutexDirect' objects>"
        'acquire': None, # (!) real value is "<method 'acquire' of 'panda3d.core.LightMutexDirect' objects>"
        'clearName': None, # (!) real value is "<method 'clearName' of 'panda3d.core.LightMutexDirect' objects>"
        'clear_name': None, # (!) real value is "<method 'clear_name' of 'panda3d.core.LightMutexDirect' objects>"
        'debugIsLocked': None, # (!) real value is "<method 'debugIsLocked' of 'panda3d.core.LightMutexDirect' objects>"
        'debug_is_locked': None, # (!) real value is "<method 'debug_is_locked' of 'panda3d.core.LightMutexDirect' objects>"
        'getName': None, # (!) real value is "<method 'getName' of 'panda3d.core.LightMutexDirect' objects>"
        'get_name': None, # (!) real value is "<method 'get_name' of 'panda3d.core.LightMutexDirect' objects>"
        'hasName': None, # (!) real value is "<method 'hasName' of 'panda3d.core.LightMutexDirect' objects>"
        'has_name': None, # (!) real value is "<method 'has_name' of 'panda3d.core.LightMutexDirect' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.LightMutexDirect' objects>"
        'release': None, # (!) real value is "<method 'release' of 'panda3d.core.LightMutexDirect' objects>"
        'setName': None, # (!) real value is "<method 'setName' of 'panda3d.core.LightMutexDirect' objects>"
        'set_name': None, # (!) real value is "<method 'set_name' of 'panda3d.core.LightMutexDirect' objects>"
    }


