# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class StreamWrapperBase(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * The base class for both IStreamWrapper and OStreamWrapper, this provides
     * the common locking interface.
     */
    """
    def acquire(self, const_StreamWrapperBase_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        acquire(const StreamWrapperBase self)
        
        /**
         * Acquires the internal lock.
         *
         * User code should call this to take temporary possession of the stream and
         * perform direct I/O operations on it, for instance to make several
         * sequential atomic reads.  You may not call any of the StreamWrapper methods
         * while the lock is held, other than release().
         *
         * Use with extreme caution!  This is a very low-level, non-recursive lock.
         * You must call acquire() only once, and you must later call release()
         * exactly once.  Failing to do so may result in a hard deadlock with no
         * available debugging features.
         */
        """
        pass

    def release(self, const_StreamWrapperBase_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        release(const StreamWrapperBase self)
        
        /**
         * Releases the internal lock.  Must be called exactly once following a call
         * to acquire().  See the cautions with acquire().
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * The base class for both IStreamWrapper and OStreamWrapper, this provides\n * the common locking interface.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.StreamWrapperBase' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE264890>'
        'acquire': None, # (!) real value is "<method 'acquire' of 'panda3d.core.StreamWrapperBase' objects>"
        'release': None, # (!) real value is "<method 'release' of 'panda3d.core.StreamWrapperBase' objects>"
    }


