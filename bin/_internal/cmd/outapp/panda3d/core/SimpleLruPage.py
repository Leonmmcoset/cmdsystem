# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class SimpleLruPage(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * One atomic piece that may be managed by a SimpleLru chain.  To use this
     * class, inherit from it and override evict_lru().
     */
    """
    def assign(self, const_SimpleLruPage_self, const_SimpleLruPage_copy): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        assign(const SimpleLruPage self, const SimpleLruPage copy)
        """
        pass

    def dequeueLru(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        dequeue_lru(const SimpleLruPage self)
        
        /**
         * Removes the page from its SimpleLru.
         */
        """
        pass

    def dequeue_lru(self, const_SimpleLruPage_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        dequeue_lru(const SimpleLruPage self)
        
        /**
         * Removes the page from its SimpleLru.
         */
        """
        pass

    def enqueueLru(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        enqueue_lru(const SimpleLruPage self, SimpleLru lru)
        
        /**
         * Adds the page to the LRU for the first time, or marks it recently-accessed
         * if it has already been added.
         *
         * If lru is NULL, it means to remove this page from its LRU.
         */
        """
        pass

    def enqueue_lru(self, const_SimpleLruPage_self, SimpleLru_lru): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        enqueue_lru(const SimpleLruPage self, SimpleLru lru)
        
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
        evict_lru(const SimpleLruPage self)
        
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

    def evict_lru(self, const_SimpleLruPage_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        evict_lru(const SimpleLruPage self)
        
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
        get_lru(SimpleLruPage self)
        
        /**
         * Returns the LRU that manages this page, or NULL if it is not currently
         * managed by any LRU.
         */
        """
        pass

    def getLruSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_lru_size(SimpleLruPage self)
        
        /**
         * Returns the size of this page as reported to the LRU, presumably in bytes.
         */
        """
        pass

    def get_lru(self, SimpleLruPage_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_lru(SimpleLruPage self)
        
        /**
         * Returns the LRU that manages this page, or NULL if it is not currently
         * managed by any LRU.
         */
        """
        pass

    def get_lru_size(self, SimpleLruPage_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_lru_size(SimpleLruPage self)
        
        /**
         * Returns the size of this page as reported to the LRU, presumably in bytes.
         */
        """
        pass

    def markUsedLru(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        mark_used_lru(SimpleLruPage self)
        mark_used_lru(const SimpleLruPage self, SimpleLru lru)
        
        /**
         * To be called when the page is used; this will move it to the tail of the
         * SimpleLru queue it is already on.
         *
         * This method is const because it's not technically modifying the contents of
         * the page itself.
         */
        
        /**
         * To be called when the page is used; this will move it to the tail of the
         * specified SimpleLru queue.
         */
        """
        pass

    def mark_used_lru(self, SimpleLruPage_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        mark_used_lru(SimpleLruPage self)
        mark_used_lru(const SimpleLruPage self, SimpleLru lru)
        
        /**
         * To be called when the page is used; this will move it to the tail of the
         * SimpleLru queue it is already on.
         *
         * This method is const because it's not technically modifying the contents of
         * the page itself.
         */
        
        /**
         * To be called when the page is used; this will move it to the tail of the
         * specified SimpleLru queue.
         */
        """
        pass

    def output(self, SimpleLruPage_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(SimpleLruPage self, ostream out)
        
        /**
         *
         */
        """
        pass

    def setLruSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_lru_size(const SimpleLruPage self, int lru_size)
        
        /**
         * Specifies the size of this page, presumably in bytes, although any unit is
         * possible.
         */
        """
        pass

    def set_lru_size(self, const_SimpleLruPage_self, int_lru_size): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_lru_size(const SimpleLruPage self, int lru_size)
        
        /**
         * Specifies the size of this page, presumably in bytes, although any unit is
         * possible.
         */
        """
        pass

    def write(self, SimpleLruPage_self, ostream_out, int_indent_level): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(SimpleLruPage self, ostream out, int indent_level)
        
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
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.SimpleLruPage' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.SimpleLruPage' objects>"
        '__doc__': '/**\n * One atomic piece that may be managed by a SimpleLru chain.  To use this\n * class, inherit from it and override evict_lru().\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.SimpleLruPage' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2FA690>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.SimpleLruPage' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.SimpleLruPage' objects>"
        'assign': None, # (!) real value is "<method 'assign' of 'panda3d.core.SimpleLruPage' objects>"
        'dequeueLru': None, # (!) real value is "<method 'dequeueLru' of 'panda3d.core.SimpleLruPage' objects>"
        'dequeue_lru': None, # (!) real value is "<method 'dequeue_lru' of 'panda3d.core.SimpleLruPage' objects>"
        'enqueueLru': None, # (!) real value is "<method 'enqueueLru' of 'panda3d.core.SimpleLruPage' objects>"
        'enqueue_lru': None, # (!) real value is "<method 'enqueue_lru' of 'panda3d.core.SimpleLruPage' objects>"
        'evictLru': None, # (!) real value is "<method 'evictLru' of 'panda3d.core.SimpleLruPage' objects>"
        'evict_lru': None, # (!) real value is "<method 'evict_lru' of 'panda3d.core.SimpleLruPage' objects>"
        'getLru': None, # (!) real value is "<method 'getLru' of 'panda3d.core.SimpleLruPage' objects>"
        'getLruSize': None, # (!) real value is "<method 'getLruSize' of 'panda3d.core.SimpleLruPage' objects>"
        'get_lru': None, # (!) real value is "<method 'get_lru' of 'panda3d.core.SimpleLruPage' objects>"
        'get_lru_size': None, # (!) real value is "<method 'get_lru_size' of 'panda3d.core.SimpleLruPage' objects>"
        'markUsedLru': None, # (!) real value is "<method 'markUsedLru' of 'panda3d.core.SimpleLruPage' objects>"
        'mark_used_lru': None, # (!) real value is "<method 'mark_used_lru' of 'panda3d.core.SimpleLruPage' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.SimpleLruPage' objects>"
        'setLruSize': None, # (!) real value is "<method 'setLruSize' of 'panda3d.core.SimpleLruPage' objects>"
        'set_lru_size': None, # (!) real value is "<method 'set_lru_size' of 'panda3d.core.SimpleLruPage' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.core.SimpleLruPage' objects>"
    }


