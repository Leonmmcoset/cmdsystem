# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .Namable import Namable

class SimpleLru(Namable):
    """
    /**
     * An implementation of a very simple LRU algorithm.  Also see AdaptiveLru.
     */
    """
    def beginEpoch(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        begin_epoch(const SimpleLru self)
        
        /**
         * Marks the end of the previous epoch and the beginning of the next one.
         * This will evict any objects that are pending eviction, and also update any
         * internal bookkeeping.
         */
        """
        pass

    def begin_epoch(self, const_SimpleLru_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        begin_epoch(const SimpleLru self)
        
        /**
         * Marks the end of the previous epoch and the beginning of the next one.
         * This will evict any objects that are pending eviction, and also update any
         * internal bookkeeping.
         */
        """
        pass

    def considerEvict(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        consider_evict(const SimpleLru self)
        
        /**
         * Evicts a sequence of objects if the queue is full.
         */
        """
        pass

    def consider_evict(self, const_SimpleLru_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        consider_evict(const SimpleLru self)
        
        /**
         * Evicts a sequence of objects if the queue is full.
         */
        """
        pass

    def countActiveSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        count_active_size(SimpleLru self)
        
        /**
         * Returns the total size of the pages that were enqueued since the last call
         * to begin_epoch().
         */
        """
        pass

    def count_active_size(self, SimpleLru_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        count_active_size(SimpleLru self)
        
        /**
         * Returns the total size of the pages that were enqueued since the last call
         * to begin_epoch().
         */
        """
        pass

    def evictTo(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        evict_to(const SimpleLru self, int target_size)
        
        /**
         * Evicts a sequence of objects until the queue fits within the indicated
         * target size, regardless of its normal max size.
         */
        """
        pass

    def evict_to(self, const_SimpleLru_self, int_target_size): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        evict_to(const SimpleLru self, int target_size)
        
        /**
         * Evicts a sequence of objects until the queue fits within the indicated
         * target size, regardless of its normal max size.
         */
        """
        pass

    def getMaxSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_max_size(SimpleLru self)
        
        /**
         * Returns the max size of all objects that are allowed to be active on the
         * LRU.
         */
        """
        pass

    def getTotalSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_total_size(SimpleLru self)
        
        /**
         * Returns the total size of all objects currently active on the LRU.
         */
        """
        pass

    def get_max_size(self, SimpleLru_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_max_size(SimpleLru self)
        
        /**
         * Returns the max size of all objects that are allowed to be active on the
         * LRU.
         */
        """
        pass

    def get_total_size(self, SimpleLru_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_total_size(SimpleLru self)
        
        /**
         * Returns the total size of all objects currently active on the LRU.
         */
        """
        pass

    def output(self, SimpleLru_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(SimpleLru self, ostream out)
        
        /**
         *
         */
        """
        pass

    def setMaxSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_max_size(const SimpleLru self, int max_size)
        
        /**
         * Changes the max size of all objects that are allowed to be active on the
         * LRU.
         *
         * If the size is (size_t)-1, there is no limit.
         */
        """
        pass

    def set_max_size(self, const_SimpleLru_self, int_max_size): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_max_size(const SimpleLru self, int max_size)
        
        /**
         * Changes the max size of all objects that are allowed to be active on the
         * LRU.
         *
         * If the size is (size_t)-1, there is no limit.
         */
        """
        pass

    def upcastToNamable(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_Namable(const SimpleLru self)
        
        upcast from SimpleLru to Namable
        """
        pass

    def upcast_to_Namable(self, const_SimpleLru_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_Namable(const SimpleLru self)
        
        upcast from SimpleLru to Namable
        """
        pass

    def validate(self, const_SimpleLru_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        validate(const SimpleLru self)
        
        /**
         * Checks that the LRU is internally self-consistent.  Returns true if
         * successful, false if there is some problem.
         */
        """
        pass

    def write(self, SimpleLru_self, ostream_out, int_indent_level): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(SimpleLru self, ostream out, int indent_level)
        
        /**
         *
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
        '__doc__': '/**\n * An implementation of a very simple LRU algorithm.  Also see AdaptiveLru.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.SimpleLru' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2FA4C0>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.SimpleLru' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.SimpleLru' objects>"
        'beginEpoch': None, # (!) real value is "<method 'beginEpoch' of 'panda3d.core.SimpleLru' objects>"
        'begin_epoch': None, # (!) real value is "<method 'begin_epoch' of 'panda3d.core.SimpleLru' objects>"
        'considerEvict': None, # (!) real value is "<method 'considerEvict' of 'panda3d.core.SimpleLru' objects>"
        'consider_evict': None, # (!) real value is "<method 'consider_evict' of 'panda3d.core.SimpleLru' objects>"
        'countActiveSize': None, # (!) real value is "<method 'countActiveSize' of 'panda3d.core.SimpleLru' objects>"
        'count_active_size': None, # (!) real value is "<method 'count_active_size' of 'panda3d.core.SimpleLru' objects>"
        'evictTo': None, # (!) real value is "<method 'evictTo' of 'panda3d.core.SimpleLru' objects>"
        'evict_to': None, # (!) real value is "<method 'evict_to' of 'panda3d.core.SimpleLru' objects>"
        'getMaxSize': None, # (!) real value is "<method 'getMaxSize' of 'panda3d.core.SimpleLru' objects>"
        'getTotalSize': None, # (!) real value is "<method 'getTotalSize' of 'panda3d.core.SimpleLru' objects>"
        'get_max_size': None, # (!) real value is "<method 'get_max_size' of 'panda3d.core.SimpleLru' objects>"
        'get_total_size': None, # (!) real value is "<method 'get_total_size' of 'panda3d.core.SimpleLru' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.SimpleLru' objects>"
        'setMaxSize': None, # (!) real value is "<method 'setMaxSize' of 'panda3d.core.SimpleLru' objects>"
        'set_max_size': None, # (!) real value is "<method 'set_max_size' of 'panda3d.core.SimpleLru' objects>"
        'upcastToNamable': None, # (!) real value is "<method 'upcastToNamable' of 'panda3d.core.SimpleLru' objects>"
        'upcast_to_Namable': None, # (!) real value is "<method 'upcast_to_Namable' of 'panda3d.core.SimpleLru' objects>"
        'validate': None, # (!) real value is "<method 'validate' of 'panda3d.core.SimpleLru' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.core.SimpleLru' objects>"
    }


