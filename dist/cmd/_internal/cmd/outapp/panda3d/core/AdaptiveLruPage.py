# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class AdaptiveLruPage(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * One atomic piece that may be managed by a AdaptiveLru chain.  To use this
     * class, inherit from it and override evict_lru().
     *
     * This class multiply inherits from two classes which in turn both inherit
     * from LinkedListNode.  This is just a sneaky C++ trick to allow this class
     * to inherit from LinkedListNode twice, so that pages can be stored on two
     * different linked lists simultaneously.  The AdaptiveLru class depends on
     * this; it maintains its pages in two different lists, one grouped by
     * priority, and one in order by next partial update needs.
     */
    """
    def assign(self, const_AdaptiveLruPage_self, const_AdaptiveLruPage_copy): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        assign(const AdaptiveLruPage self, const AdaptiveLruPage copy)
        """
        pass

    def dequeueLru(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        dequeue_lru(const AdaptiveLruPage self)
        
        /**
         * Removes the page from its AdaptiveLru.
         */
        """
        pass

    def dequeue_lru(self, const_AdaptiveLruPage_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        dequeue_lru(const AdaptiveLruPage self)
        
        /**
         * Removes the page from its AdaptiveLru.
         */
        """
        pass

    def enqueueLru(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        enqueue_lru(const AdaptiveLruPage self, AdaptiveLru lru)
        
        /**
         * Adds the page to the LRU for the first time, or marks it recently-accessed
         * if it has already been added.
         *
         * If lru is NULL, it means to remove this page from its LRU.
         */
        """
        pass

    def enqueue_lru(self, const_AdaptiveLruPage_self, AdaptiveLru_lru): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        enqueue_lru(const AdaptiveLruPage self, AdaptiveLru lru)
        
        /**
         * Adds the page to the LRU for the first time, or marks it recently-accessed
         * if it has already been added.
         *
         * If lru is NULL, it means to remove this page from its LRU.
         */
        """
        pass

    def evictLru(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        evict_lru(const AdaptiveLruPage self)
        
        /**
         * Evicts the page from the LRU.  Called internally when the LRU determines
         * that it is full.  May also be called externally when necessary to
         * explicitly evict the page.
         *
         * It is legal for this method to either evict the page as requested, do
         * nothing (in which case the eviction will be requested again at the next
         * epoch), or requeue itself on the tail of the queue (in which case the
         * eviction will be requested again much later).
         */
        """
        pass

    def evict_lru(self, const_AdaptiveLruPage_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        evict_lru(const AdaptiveLruPage self)
        
        /**
         * Evicts the page from the LRU.  Called internally when the LRU determines
         * that it is full.  May also be called externally when necessary to
         * explicitly evict the page.
         *
         * It is legal for this method to either evict the page as requested, do
         * nothing (in which case the eviction will be requested again at the next
         * epoch), or requeue itself on the tail of the queue (in which case the
         * eviction will be requested again much later).
         */
        """
        pass

    def getLru(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_lru(AdaptiveLruPage self)
        
        /**
         * Returns the LRU that manages this page, or NULL if it is not currently
         * managed by any LRU.
         */
        """
        pass

    def getLruSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_lru_size(AdaptiveLruPage self)
        
        /**
         * Returns the size of this page as reported to the LRU, presumably in bytes.
         */
        """
        pass

    def getNumFrames(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_frames(AdaptiveLruPage self)
        
        // Not defined in SimpleLruPage.
        
        /**
         * Returns the number of frames since the page was first added to its LRU.
         * Returns 0 if it does not have an LRU.
         */
        """
        pass

    def getNumInactiveFrames(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_inactive_frames(AdaptiveLruPage self)
        
        /**
         * Returns the number of frames since the page was last accessed on its LRU.
         * Returns 0 if it does not have an LRU.
         */
        """
        pass

    def get_lru(self, AdaptiveLruPage_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_lru(AdaptiveLruPage self)
        
        /**
         * Returns the LRU that manages this page, or NULL if it is not currently
         * managed by any LRU.
         */
        """
        pass

    def get_lru_size(self, AdaptiveLruPage_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_lru_size(AdaptiveLruPage self)
        
        /**
         * Returns the size of this page as reported to the LRU, presumably in bytes.
         */
        """
        pass

    def get_num_frames(self, AdaptiveLruPage_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_frames(AdaptiveLruPage self)
        
        // Not defined in SimpleLruPage.
        
        /**
         * Returns the number of frames since the page was first added to its LRU.
         * Returns 0 if it does not have an LRU.
         */
        """
        pass

    def get_num_inactive_frames(self, AdaptiveLruPage_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_inactive_frames(AdaptiveLruPage self)
        
        /**
         * Returns the number of frames since the page was last accessed on its LRU.
         * Returns 0 if it does not have an LRU.
         */
        """
        pass

    def markUsedLru(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        mark_used_lru(AdaptiveLruPage self)
        mark_used_lru(const AdaptiveLruPage self, AdaptiveLru lru)
        
        /**
         * To be called when the page is used; this will move it to the tail of the
         * AdaptiveLru queue it is already on.
         *
         * This method is const because it's not technically modifying the contents of
         * the page itself.
         */
        
        /**
         * To be called when the page is used; this will move it to the tail of the
         * specified AdaptiveLru queue.
         */
        """
        pass

    def mark_used_lru(self, AdaptiveLruPage_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        mark_used_lru(AdaptiveLruPage self)
        mark_used_lru(const AdaptiveLruPage self, AdaptiveLru lru)
        
        /**
         * To be called when the page is used; this will move it to the tail of the
         * AdaptiveLru queue it is already on.
         *
         * This method is const because it's not technically modifying the contents of
         * the page itself.
         */
        
        /**
         * To be called when the page is used; this will move it to the tail of the
         * specified AdaptiveLru queue.
         */
        """
        pass

    def output(self, AdaptiveLruPage_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(AdaptiveLruPage self, ostream out)
        
        /**
         *
         */
        """
        pass

    def setLruSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_lru_size(const AdaptiveLruPage self, int lru_size)
        
        /**
         * Specifies the size of this page, presumably in bytes, although any unit is
         * possible.
         */
        """
        pass

    def set_lru_size(self, const_AdaptiveLruPage_self, int_lru_size): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_lru_size(const AdaptiveLruPage self, int lru_size)
        
        /**
         * Specifies the size of this page, presumably in bytes, although any unit is
         * possible.
         */
        """
        pass

    def write(self, AdaptiveLruPage_self, ostream_out, int_indent_level): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(AdaptiveLruPage self, ostream out, int indent_level)
        
        /**
         *
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

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.AdaptiveLruPage' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.AdaptiveLruPage' objects>"
        '__doc__': '/**\n * One atomic piece that may be managed by a AdaptiveLru chain.  To use this\n * class, inherit from it and override evict_lru().\n *\n * This class multiply inherits from two classes which in turn both inherit\n * from LinkedListNode.  This is just a sneaky C++ trick to allow this class\n * to inherit from LinkedListNode twice, so that pages can be stored on two\n * different linked lists simultaneously.  The AdaptiveLru class depends on\n * this; it maintains its pages in two different lists, one grouped by\n * priority, and one in order by next partial update needs.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.AdaptiveLruPage' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2F9810>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.AdaptiveLruPage' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.AdaptiveLruPage' objects>"
        'assign': None, # (!) real value is "<method 'assign' of 'panda3d.core.AdaptiveLruPage' objects>"
        'dequeueLru': None, # (!) real value is "<method 'dequeueLru' of 'panda3d.core.AdaptiveLruPage' objects>"
        'dequeue_lru': None, # (!) real value is "<method 'dequeue_lru' of 'panda3d.core.AdaptiveLruPage' objects>"
        'enqueueLru': None, # (!) real value is "<method 'enqueueLru' of 'panda3d.core.AdaptiveLruPage' objects>"
        'enqueue_lru': None, # (!) real value is "<method 'enqueue_lru' of 'panda3d.core.AdaptiveLruPage' objects>"
        'evictLru': None, # (!) real value is "<method 'evictLru' of 'panda3d.core.AdaptiveLruPage' objects>"
        'evict_lru': None, # (!) real value is "<method 'evict_lru' of 'panda3d.core.AdaptiveLruPage' objects>"
        'getLru': None, # (!) real value is "<method 'getLru' of 'panda3d.core.AdaptiveLruPage' objects>"
        'getLruSize': None, # (!) real value is "<method 'getLruSize' of 'panda3d.core.AdaptiveLruPage' objects>"
        'getNumFrames': None, # (!) real value is "<method 'getNumFrames' of 'panda3d.core.AdaptiveLruPage' objects>"
        'getNumInactiveFrames': None, # (!) real value is "<method 'getNumInactiveFrames' of 'panda3d.core.AdaptiveLruPage' objects>"
        'get_lru': None, # (!) real value is "<method 'get_lru' of 'panda3d.core.AdaptiveLruPage' objects>"
        'get_lru_size': None, # (!) real value is "<method 'get_lru_size' of 'panda3d.core.AdaptiveLruPage' objects>"
        'get_num_frames': None, # (!) real value is "<method 'get_num_frames' of 'panda3d.core.AdaptiveLruPage' objects>"
        'get_num_inactive_frames': None, # (!) real value is "<method 'get_num_inactive_frames' of 'panda3d.core.AdaptiveLruPage' objects>"
        'markUsedLru': None, # (!) real value is "<method 'markUsedLru' of 'panda3d.core.AdaptiveLruPage' objects>"
        'mark_used_lru': None, # (!) real value is "<method 'mark_used_lru' of 'panda3d.core.AdaptiveLruPage' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.AdaptiveLruPage' objects>"
        'setLruSize': None, # (!) real value is "<method 'setLruSize' of 'panda3d.core.AdaptiveLruPage' objects>"
        'set_lru_size': None, # (!) real value is "<method 'set_lru_size' of 'panda3d.core.AdaptiveLruPage' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.core.AdaptiveLruPage' objects>"
    }


