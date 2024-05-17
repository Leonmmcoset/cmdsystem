# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class Semaphore(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * A classic semaphore synchronization primitive.
     *
     * A semaphore manages an internal counter which is decremented by each
     * acquire() call and incremented by each release() call.  The counter can
     * never go below zero; when acquire() finds that it is zero, it blocks,
     * waiting until some other thread calls release().
     */
    """
    def acquire(self, const_Semaphore_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        acquire(const Semaphore self)
        
        /**
         * Decrements the internal count.  If the count was already at zero, blocks
         * until the count is nonzero, then decrements it.
         */
        """
        pass

    def getCount(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_count(Semaphore self)
        
        /**
         * Returns the current semaphore count.  Note that this call is not thread-
         * safe (the count may change at any time).
         */
        """
        pass

    def get_count(self, Semaphore_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_count(Semaphore self)
        
        /**
         * Returns the current semaphore count.  Note that this call is not thread-
         * safe (the count may change at any time).
         */
        """
        pass

    def output(self, Semaphore_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(Semaphore self, ostream out)
        
        /**
         *
         */
        """
        pass

    def release(self, const_Semaphore_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        release(const Semaphore self)
        
        /**
         * Increments the semaphore's internal count.  This may wake up another thread
         * blocked on acquire().
         *
         * Returns the count of the semaphore upon release.
         */
        """
        pass

    def tryAcquire(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        try_acquire(const Semaphore self)
        
        /**
         * If the semaphore can be acquired without blocking, does so and returns
         * true.  Otherwise, returns false.
         */
        """
        pass

    def try_acquire(self, const_Semaphore_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        try_acquire(const Semaphore self)
        
        /**
         * If the semaphore can be acquired without blocking, does so and returns
         * true.  Otherwise, returns false.
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
        '__doc__': '/**\n * A classic semaphore synchronization primitive.\n *\n * A semaphore manages an internal counter which is decremented by each\n * acquire() call and incremented by each release() call.  The counter can\n * never go below zero; when acquire() finds that it is zero, it blocks,\n * waiting until some other thread calls release().\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.Semaphore' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2ECC90>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.Semaphore' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.Semaphore' objects>"
        'acquire': None, # (!) real value is "<method 'acquire' of 'panda3d.core.Semaphore' objects>"
        'getCount': None, # (!) real value is "<method 'getCount' of 'panda3d.core.Semaphore' objects>"
        'get_count': None, # (!) real value is "<method 'get_count' of 'panda3d.core.Semaphore' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.Semaphore' objects>"
        'release': None, # (!) real value is "<method 'release' of 'panda3d.core.Semaphore' objects>"
        'tryAcquire': None, # (!) real value is "<method 'tryAcquire' of 'panda3d.core.Semaphore' objects>"
        'try_acquire': None, # (!) real value is "<method 'try_acquire' of 'panda3d.core.Semaphore' objects>"
    }


