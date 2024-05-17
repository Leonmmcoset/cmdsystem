# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .SimpleAllocator import SimpleAllocator

from .SimpleLruPage import SimpleLruPage

class VertexDataPage(SimpleAllocator, SimpleLruPage):
    """
    /**
     * A block of bytes that holds one or more VertexDataBlocks.  The entire page
     * may be paged out, in the form of in-memory compression or to an on-disk
     * cache file, if necessary.
     */
    """
    def alloc(self, const_VertexDataPage_self, int_size): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        alloc(const VertexDataPage self, int size)
        
        /**
         * Allocates a new block.  Returns NULL if a block of the requested size
         * cannot be allocated.
         *
         * To free the allocated block, call block->free(), or simply delete the block
         * pointer.
         */
        """
        pass

    def flushThreads(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        flush_threads()
        
        /**
         * Waits for all of the pending thread tasks to finish before returning.
         */
        """
        pass

    def flush_threads(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        flush_threads()
        
        /**
         * Waits for all of the pending thread tasks to finish before returning.
         */
        """
        pass

    def getBook(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_book(VertexDataPage self)
        
        /**
         * Returns a pointer to the book that owns this page.
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getFirstBlock(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_first_block(VertexDataPage self)
        
        /**
         * Returns a pointer to the first allocated block, or NULL if there are no
         * allocated blocks.
         */
        """
        pass

    def getGlobalLru(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_global_lru(int rclass)
        
        /**
         * Returns a pointer to the global LRU object that manages the
         * VertexDataPage's with the indicated RamClass.
         */
        """
        pass

    def getNumPendingReads(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_pending_reads()
        
        /**
         * Returns the number of read requests that are waiting to be serviced by a
         * thread.
         */
        """
        pass

    def getNumPendingWrites(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_pending_writes()
        
        /**
         * Returns the number of write requests that are waiting to be serviced by a
         * thread.
         */
        """
        pass

    def getNumThreads(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_threads()
        
        /**
         * Returns the number of threads that have been spawned to service vertex
         * paging requests, or 0 if no threads have been spawned (which may mean
         * either that all paging requests will be handled by the main thread, or
         * simply that no paging requests have yet been issued).
         */
        """
        pass

    def getPendingLru(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_pending_lru()
        
        /**
         * Returns a pointer to the global LRU object that manages the
         * VertexDataPage's that are pending processing by the thread.
         */
        """
        pass

    def getPendingRamClass(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_pending_ram_class(VertexDataPage self)
        
        /**
         * Returns the pending ram class of the array.  If this is different from
         * get_ram_class(), this page has been queued to be processed by the thread.
         * Eventually the page will be set to this ram class.
         */
        """
        pass

    def getRamClass(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_ram_class(VertexDataPage self)
        
        /**
         * Returns the current ram class of the array.  If this is other than
         * RC_resident, the array data is not resident in memory.
         */
        """
        pass

    def getSaveFile(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_save_file()
        
        /**
         * Returns the global VertexDataSaveFile that will be used to save vertex data
         * buffers to disk when necessary.
         */
        """
        pass

    def get_book(self, VertexDataPage_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_book(VertexDataPage self)
        
        /**
         * Returns a pointer to the book that owns this page.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_first_block(self, VertexDataPage_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_first_block(VertexDataPage self)
        
        /**
         * Returns a pointer to the first allocated block, or NULL if there are no
         * allocated blocks.
         */
        """
        pass

    def get_global_lru(self, int_rclass): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_global_lru(int rclass)
        
        /**
         * Returns a pointer to the global LRU object that manages the
         * VertexDataPage's with the indicated RamClass.
         */
        """
        pass

    def get_num_pending_reads(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_pending_reads()
        
        /**
         * Returns the number of read requests that are waiting to be serviced by a
         * thread.
         */
        """
        pass

    def get_num_pending_writes(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_pending_writes()
        
        /**
         * Returns the number of write requests that are waiting to be serviced by a
         * thread.
         */
        """
        pass

    def get_num_threads(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_threads()
        
        /**
         * Returns the number of threads that have been spawned to service vertex
         * paging requests, or 0 if no threads have been spawned (which may mean
         * either that all paging requests will be handled by the main thread, or
         * simply that no paging requests have yet been issued).
         */
        """
        pass

    def get_pending_lru(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_pending_lru()
        
        /**
         * Returns a pointer to the global LRU object that manages the
         * VertexDataPage's that are pending processing by the thread.
         */
        """
        pass

    def get_pending_ram_class(self, VertexDataPage_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_pending_ram_class(VertexDataPage self)
        
        /**
         * Returns the pending ram class of the array.  If this is different from
         * get_ram_class(), this page has been queued to be processed by the thread.
         * Eventually the page will be set to this ram class.
         */
        """
        pass

    def get_ram_class(self, VertexDataPage_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_ram_class(VertexDataPage self)
        
        /**
         * Returns the current ram class of the array.  If this is other than
         * RC_resident, the array data is not resident in memory.
         */
        """
        pass

    def get_save_file(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_save_file()
        
        /**
         * Returns the global VertexDataSaveFile that will be used to save vertex data
         * buffers to disk when necessary.
         */
        """
        pass

    def output(self, VertexDataPage_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(VertexDataPage self, ostream out)
        
        /**
         *
         */
        """
        pass

    def requestResident(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        request_resident(const VertexDataPage self)
        
        /**
         * Ensures that the page will become resident soon.  Future calls to
         * get_page_data() will eventually return non-NULL.
         */
        """
        pass

    def request_resident(self, const_VertexDataPage_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        request_resident(const VertexDataPage self)
        
        /**
         * Ensures that the page will become resident soon.  Future calls to
         * get_page_data() will eventually return non-NULL.
         */
        """
        pass

    def saveToDisk(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        save_to_disk(const VertexDataPage self)
        
        /**
         * Writes the page to disk, but does not evict it from memory or affect its
         * LRU status.  If it gets evicted later without having been modified, it will
         * not need to write itself to disk again.
         */
        """
        pass

    def save_to_disk(self, const_VertexDataPage_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        save_to_disk(const VertexDataPage self)
        
        /**
         * Writes the page to disk, but does not evict it from memory or affect its
         * LRU status.  If it gets evicted later without having been modified, it will
         * not need to write itself to disk again.
         */
        """
        pass

    def stopThreads(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        stop_threads()
        
        /**
         * Call this to stop the paging threads, if they were started.  This may block
         * until all of the pending tasks have been completed.
         */
        """
        pass

    def stop_threads(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        stop_threads()
        
        /**
         * Call this to stop the paging threads, if they were started.  This may block
         * until all of the pending tasks have been completed.
         */
        """
        pass

    def upcastToSimpleAllocator(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_SimpleAllocator(const VertexDataPage self)
        
        upcast from VertexDataPage to SimpleAllocator
        """
        pass

    def upcastToSimpleLruPage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_SimpleLruPage(const VertexDataPage self)
        
        upcast from VertexDataPage to SimpleLruPage
        """
        pass

    def upcast_to_SimpleAllocator(self, const_VertexDataPage_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_SimpleAllocator(const VertexDataPage self)
        
        upcast from VertexDataPage to SimpleAllocator
        """
        pass

    def upcast_to_SimpleLruPage(self, const_VertexDataPage_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_SimpleLruPage(const VertexDataPage self)
        
        upcast from VertexDataPage to SimpleLruPage
        """
        pass

    def write(self, VertexDataPage_self, ostream_out, int_indent_level): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(VertexDataPage self, ostream out, int indent_level)
        
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
        'RCCompressed': 1,
        'RCDisk': 2,
        'RCEndOfList': 3,
        'RCResident': 0,
        'RC_compressed': 1,
        'RC_disk': 2,
        'RC_end_of_list': 3,
        'RC_resident': 0,
        '__doc__': '/**\n * A block of bytes that holds one or more VertexDataBlocks.  The entire page\n * may be paged out, in the form of in-memory compression or to an on-disk\n * cache file, if necessary.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.VertexDataPage' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2FADD0>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.VertexDataPage' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.VertexDataPage' objects>"
        'alloc': None, # (!) real value is "<method 'alloc' of 'panda3d.core.VertexDataPage' objects>"
        'flushThreads': None, # (!) real value is '<staticmethod(<built-in method flushThreads of type object at 0x00007FFCFE2FADD0>)>'
        'flush_threads': None, # (!) real value is '<staticmethod(<built-in method flush_threads of type object at 0x00007FFCFE2FADD0>)>'
        'getBook': None, # (!) real value is "<method 'getBook' of 'panda3d.core.VertexDataPage' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2FADD0>)>'
        'getFirstBlock': None, # (!) real value is "<method 'getFirstBlock' of 'panda3d.core.VertexDataPage' objects>"
        'getGlobalLru': None, # (!) real value is '<staticmethod(<built-in method getGlobalLru of type object at 0x00007FFCFE2FADD0>)>'
        'getNumPendingReads': None, # (!) real value is '<staticmethod(<built-in method getNumPendingReads of type object at 0x00007FFCFE2FADD0>)>'
        'getNumPendingWrites': None, # (!) real value is '<staticmethod(<built-in method getNumPendingWrites of type object at 0x00007FFCFE2FADD0>)>'
        'getNumThreads': None, # (!) real value is '<staticmethod(<built-in method getNumThreads of type object at 0x00007FFCFE2FADD0>)>'
        'getPendingLru': None, # (!) real value is '<staticmethod(<built-in method getPendingLru of type object at 0x00007FFCFE2FADD0>)>'
        'getPendingRamClass': None, # (!) real value is "<method 'getPendingRamClass' of 'panda3d.core.VertexDataPage' objects>"
        'getRamClass': None, # (!) real value is "<method 'getRamClass' of 'panda3d.core.VertexDataPage' objects>"
        'getSaveFile': None, # (!) real value is '<staticmethod(<built-in method getSaveFile of type object at 0x00007FFCFE2FADD0>)>'
        'get_book': None, # (!) real value is "<method 'get_book' of 'panda3d.core.VertexDataPage' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2FADD0>)>'
        'get_first_block': None, # (!) real value is "<method 'get_first_block' of 'panda3d.core.VertexDataPage' objects>"
        'get_global_lru': None, # (!) real value is '<staticmethod(<built-in method get_global_lru of type object at 0x00007FFCFE2FADD0>)>'
        'get_num_pending_reads': None, # (!) real value is '<staticmethod(<built-in method get_num_pending_reads of type object at 0x00007FFCFE2FADD0>)>'
        'get_num_pending_writes': None, # (!) real value is '<staticmethod(<built-in method get_num_pending_writes of type object at 0x00007FFCFE2FADD0>)>'
        'get_num_threads': None, # (!) real value is '<staticmethod(<built-in method get_num_threads of type object at 0x00007FFCFE2FADD0>)>'
        'get_pending_lru': None, # (!) real value is '<staticmethod(<built-in method get_pending_lru of type object at 0x00007FFCFE2FADD0>)>'
        'get_pending_ram_class': None, # (!) real value is "<method 'get_pending_ram_class' of 'panda3d.core.VertexDataPage' objects>"
        'get_ram_class': None, # (!) real value is "<method 'get_ram_class' of 'panda3d.core.VertexDataPage' objects>"
        'get_save_file': None, # (!) real value is '<staticmethod(<built-in method get_save_file of type object at 0x00007FFCFE2FADD0>)>'
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.VertexDataPage' objects>"
        'requestResident': None, # (!) real value is "<method 'requestResident' of 'panda3d.core.VertexDataPage' objects>"
        'request_resident': None, # (!) real value is "<method 'request_resident' of 'panda3d.core.VertexDataPage' objects>"
        'saveToDisk': None, # (!) real value is "<method 'saveToDisk' of 'panda3d.core.VertexDataPage' objects>"
        'save_file': None, # (!) real value is "<attribute 'save_file' of 'panda3d.core.VertexDataPage'>"
        'save_to_disk': None, # (!) real value is "<method 'save_to_disk' of 'panda3d.core.VertexDataPage' objects>"
        'stopThreads': None, # (!) real value is '<staticmethod(<built-in method stopThreads of type object at 0x00007FFCFE2FADD0>)>'
        'stop_threads': None, # (!) real value is '<staticmethod(<built-in method stop_threads of type object at 0x00007FFCFE2FADD0>)>'
        'upcastToSimpleAllocator': None, # (!) real value is "<method 'upcastToSimpleAllocator' of 'panda3d.core.VertexDataPage' objects>"
        'upcastToSimpleLruPage': None, # (!) real value is "<method 'upcastToSimpleLruPage' of 'panda3d.core.VertexDataPage' objects>"
        'upcast_to_SimpleAllocator': None, # (!) real value is "<method 'upcast_to_SimpleAllocator' of 'panda3d.core.VertexDataPage' objects>"
        'upcast_to_SimpleLruPage': None, # (!) real value is "<method 'upcast_to_SimpleLruPage' of 'panda3d.core.VertexDataPage' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.core.VertexDataPage' objects>"
    }
    RCCompressed = 1
    RCDisk = 2
    RCEndOfList = 3
    RCResident = 0
    RC_compressed = 1
    RC_disk = 2
    RC_end_of_list = 3
    RC_resident = 0
    save_file = None # (!) real value is 'SimpleAllocator, 0 of 18446744073709551615 allocated'


