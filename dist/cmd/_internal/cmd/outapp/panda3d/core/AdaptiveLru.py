# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .Namable import Namable

class AdaptiveLru(Namable):
    """
    /**
     * A basic LRU-type algorithm, except that it is adaptive and attempts to
     * avoid evicting pages that have been used more frequently (even if less
     * recently) than other pages.
     *
     * The interface is designed to be identical to that for SimpleLru, so that it
     * may be used as a drop-in replacement.
     */
    """
    def beginEpoch(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        begin_epoch(const AdaptiveLru self)
        
        /**
         * Marks the end of the previous epoch and the beginning of the next one.
         * This will evict any objects that are pending eviction, and also update any
         * internal bookkeeping.
         */
        """
        pass

    def begin_epoch(self, const_AdaptiveLru_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        begin_epoch(const AdaptiveLru self)
        
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
        consider_evict(const AdaptiveLru self)
        
        /**
         * Evicts a sequence of objects if the queue is full.
         */
        """
        pass

    def consider_evict(self, const_AdaptiveLru_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        consider_evict(const AdaptiveLru self)
        
        /**
         * Evicts a sequence of objects if the queue is full.
         */
        """
        pass

    def countActiveSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        count_active_size(AdaptiveLru self)
        
        /**
         * Returns the total size of the pages that were enqueued since the last call
         * to begin_epoch().
         */
        """
        pass

    def count_active_size(self, AdaptiveLru_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        count_active_size(AdaptiveLru self)
        
        /**
         * Returns the total size of the pages that were enqueued since the last call
         * to begin_epoch().
         */
        """
        pass

    def evictTo(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        evict_to(const AdaptiveLru self, int target_size)
        
        /**
         * Evicts a sequence of objects until the queue fits within the indicated
         * target size, regardless of its normal max size.
         */
        """
        pass

    def evict_to(self, const_AdaptiveLru_self, int_target_size): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        evict_to(const AdaptiveLru self, int target_size)
        
        /**
         * Evicts a sequence of objects until the queue fits within the indicated
         * target size, regardless of its normal max size.
         */
        """
        pass

    def getMaxSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_max_size(AdaptiveLru self)
        
        /**
         * Returns the max size of all objects that are allowed to be active on the
         * LRU.
         */
        """
        pass

    def getMaxUpdatesPerFrame(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_max_updates_per_frame(AdaptiveLru self)
        
        /**
         * Returns the maximum number of pages the AdaptiveLru will update each frame.
         */
        """
        pass

    def getTotalSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_total_size(AdaptiveLru self)
        
        /**
         * Returns the total size of all objects currently active on the LRU.
         */
        """
        pass

    def getWeight(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_weight(AdaptiveLru self)
        
        /**
         * Returns the weight value used to compute the exponential moving average.
         */
        """
        pass

    def get_max_size(self, AdaptiveLru_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_max_size(AdaptiveLru self)
        
        /**
         * Returns the max size of all objects that are allowed to be active on the
         * LRU.
         */
        """
        pass

    def get_max_updates_per_frame(self, AdaptiveLru_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_max_updates_per_frame(AdaptiveLru self)
        
        /**
         * Returns the maximum number of pages the AdaptiveLru will update each frame.
         */
        """
        pass

    def get_total_size(self, AdaptiveLru_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_total_size(AdaptiveLru self)
        
        /**
         * Returns the total size of all objects currently active on the LRU.
         */
        """
        pass

    def get_weight(self, AdaptiveLru_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_weight(AdaptiveLru self)
        
        /**
         * Returns the weight value used to compute the exponential moving average.
         */
        """
        pass

    def output(self, AdaptiveLru_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(AdaptiveLru self, ostream out)
        
        /**
         *
         */
        """
        pass

    def setMaxSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_max_size(const AdaptiveLru self, int max_size)
        
        /**
         * Changes the max size of all objects that are allowed to be active on the
         * LRU.
         *
         * If the size is (size_t)-1, there is no limit.
         */
        """
        pass

    def setMaxUpdatesPerFrame(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_max_updates_per_frame(const AdaptiveLru self, int max_updates_per_frame)
        
        /**
         * Specifies the maximum number of pages the AdaptiveLru will update each
         * frame.  This is a performance optimization: keeping this number low limits
         * the impact of the AdaptiveLru's adaptive algorithm.
         */
        """
        pass

    def setWeight(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_weight(const AdaptiveLru self, float weight)
        
        // The following methods are specific to AdaptiveLru, and do not exist in
        // the SimpleLru implementation.  In most cases, the defaults will be
        // sufficient, so you do not need to mess with them.
        
        /**
         * Specifies the weight value used to compute the exponential moving average.
         */
        """
        pass

    def set_max_size(self, const_AdaptiveLru_self, int_max_size): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_max_size(const AdaptiveLru self, int max_size)
        
        /**
         * Changes the max size of all objects that are allowed to be active on the
         * LRU.
         *
         * If the size is (size_t)-1, there is no limit.
         */
        """
        pass

    def set_max_updates_per_frame(self, const_AdaptiveLru_self, int_max_updates_per_frame): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_max_updates_per_frame(const AdaptiveLru self, int max_updates_per_frame)
        
        /**
         * Specifies the maximum number of pages the AdaptiveLru will update each
         * frame.  This is a performance optimization: keeping this number low limits
         * the impact of the AdaptiveLru's adaptive algorithm.
         */
        """
        pass

    def set_weight(self, const_AdaptiveLru_self, float_weight): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_weight(const AdaptiveLru self, float weight)
        
        // The following methods are specific to AdaptiveLru, and do not exist in
        // the SimpleLru implementation.  In most cases, the defaults will be
        // sufficient, so you do not need to mess with them.
        
        /**
         * Specifies the weight value used to compute the exponential moving average.
         */
        """
        pass

    def validate(self, const_AdaptiveLru_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        validate(const AdaptiveLru self)
        
        /**
         * Checks that the LRU is internally self-consistent.  Returns true if
         * successful, false if there is some problem.
         */
        """
        pass

    def write(self, AdaptiveLru_self, ostream_out, int_indent_level): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(AdaptiveLru self, ostream out, int indent_level)
        
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
        '__doc__': '/**\n * A basic LRU-type algorithm, except that it is adaptive and attempts to\n * avoid evicting pages that have been used more frequently (even if less\n * recently) than other pages.\n *\n * The interface is designed to be identical to that for SimpleLru, so that it\n * may be used as a drop-in replacement.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.AdaptiveLru' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2F9630>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.AdaptiveLru' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.AdaptiveLru' objects>"
        'beginEpoch': None, # (!) real value is "<method 'beginEpoch' of 'panda3d.core.AdaptiveLru' objects>"
        'begin_epoch': None, # (!) real value is "<method 'begin_epoch' of 'panda3d.core.AdaptiveLru' objects>"
        'considerEvict': None, # (!) real value is "<method 'considerEvict' of 'panda3d.core.AdaptiveLru' objects>"
        'consider_evict': None, # (!) real value is "<method 'consider_evict' of 'panda3d.core.AdaptiveLru' objects>"
        'countActiveSize': None, # (!) real value is "<method 'countActiveSize' of 'panda3d.core.AdaptiveLru' objects>"
        'count_active_size': None, # (!) real value is "<method 'count_active_size' of 'panda3d.core.AdaptiveLru' objects>"
        'evictTo': None, # (!) real value is "<method 'evictTo' of 'panda3d.core.AdaptiveLru' objects>"
        'evict_to': None, # (!) real value is "<method 'evict_to' of 'panda3d.core.AdaptiveLru' objects>"
        'getMaxSize': None, # (!) real value is "<method 'getMaxSize' of 'panda3d.core.AdaptiveLru' objects>"
        'getMaxUpdatesPerFrame': None, # (!) real value is "<method 'getMaxUpdatesPerFrame' of 'panda3d.core.AdaptiveLru' objects>"
        'getTotalSize': None, # (!) real value is "<method 'getTotalSize' of 'panda3d.core.AdaptiveLru' objects>"
        'getWeight': None, # (!) real value is "<method 'getWeight' of 'panda3d.core.AdaptiveLru' objects>"
        'get_max_size': None, # (!) real value is "<method 'get_max_size' of 'panda3d.core.AdaptiveLru' objects>"
        'get_max_updates_per_frame': None, # (!) real value is "<method 'get_max_updates_per_frame' of 'panda3d.core.AdaptiveLru' objects>"
        'get_total_size': None, # (!) real value is "<method 'get_total_size' of 'panda3d.core.AdaptiveLru' objects>"
        'get_weight': None, # (!) real value is "<method 'get_weight' of 'panda3d.core.AdaptiveLru' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.AdaptiveLru' objects>"
        'setMaxSize': None, # (!) real value is "<method 'setMaxSize' of 'panda3d.core.AdaptiveLru' objects>"
        'setMaxUpdatesPerFrame': None, # (!) real value is "<method 'setMaxUpdatesPerFrame' of 'panda3d.core.AdaptiveLru' objects>"
        'setWeight': None, # (!) real value is "<method 'setWeight' of 'panda3d.core.AdaptiveLru' objects>"
        'set_max_size': None, # (!) real value is "<method 'set_max_size' of 'panda3d.core.AdaptiveLru' objects>"
        'set_max_updates_per_frame': None, # (!) real value is "<method 'set_max_updates_per_frame' of 'panda3d.core.AdaptiveLru' objects>"
        'set_weight': None, # (!) real value is "<method 'set_weight' of 'panda3d.core.AdaptiveLru' objects>"
        'validate': None, # (!) real value is "<method 'validate' of 'panda3d.core.AdaptiveLru' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.core.AdaptiveLru' objects>"
    }


