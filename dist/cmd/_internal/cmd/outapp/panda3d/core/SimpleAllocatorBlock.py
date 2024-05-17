# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class SimpleAllocatorBlock(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * A single block as returned from SimpleAllocator::alloc().
     */
    """
    def free(self, const_SimpleAllocatorBlock_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        free(const SimpleAllocatorBlock self)
        
        /**
         * Releases the allocated space.
         */
        """
        pass

    def getAllocator(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_allocator(SimpleAllocatorBlock self)
        
        /**
         * Returns the SimpleAllocator object that owns this block.  Returns NULL if
         * the block has been freed.
         */
        """
        pass

    def getMaxSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_max_size(SimpleAllocatorBlock self)
        
        /**
         * Returns the maximum size this block can be reallocated to, as limited by
         * the following block.
         */
        """
        pass

    def getNextBlock(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_next_block(SimpleAllocatorBlock self)
        
        /**
         * Returns a pointer to the next allocated block in the chain, or NULL if
         * there are no more allocated blocks.
         */
        """
        pass

    def getSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_size(SimpleAllocatorBlock self)
        
        /**
         * Returns the size of this block.  It is an error to call this if the block
         * has been freed.
         */
        """
        pass

    def getStart(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_start(SimpleAllocatorBlock self)
        
        /**
         * Returns the starting point of this block.  It is an error to call this if
         * the block has been freed.
         */
        """
        pass

    def get_allocator(self, SimpleAllocatorBlock_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_allocator(SimpleAllocatorBlock self)
        
        /**
         * Returns the SimpleAllocator object that owns this block.  Returns NULL if
         * the block has been freed.
         */
        """
        pass

    def get_max_size(self, SimpleAllocatorBlock_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_max_size(SimpleAllocatorBlock self)
        
        /**
         * Returns the maximum size this block can be reallocated to, as limited by
         * the following block.
         */
        """
        pass

    def get_next_block(self, SimpleAllocatorBlock_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_next_block(SimpleAllocatorBlock self)
        
        /**
         * Returns a pointer to the next allocated block in the chain, or NULL if
         * there are no more allocated blocks.
         */
        """
        pass

    def get_size(self, SimpleAllocatorBlock_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_size(SimpleAllocatorBlock self)
        
        /**
         * Returns the size of this block.  It is an error to call this if the block
         * has been freed.
         */
        """
        pass

    def get_start(self, SimpleAllocatorBlock_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_start(SimpleAllocatorBlock self)
        
        /**
         * Returns the starting point of this block.  It is an error to call this if
         * the block has been freed.
         */
        """
        pass

    def isFree(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_free(SimpleAllocatorBlock self)
        
        /**
         * Returns true if the block has been freed, false if it is still valid.
         */
        """
        pass

    def is_free(self, SimpleAllocatorBlock_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_free(SimpleAllocatorBlock self)
        
        /**
         * Returns true if the block has been freed, false if it is still valid.
         */
        """
        pass

    def output(self, SimpleAllocatorBlock_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(SimpleAllocatorBlock self, ostream out)
        
        /**
         *
         */
        """
        pass

    def realloc(self, const_SimpleAllocatorBlock_self, int_size): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        realloc(const SimpleAllocatorBlock self, int size)
        
        /**
         * Changes the size of this block to the specified size.  Returns true if the
         * change is accepted, false if there was not enough room.
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
        '__doc__': '/**\n * A single block as returned from SimpleAllocator::alloc().\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.SimpleAllocatorBlock' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2FAA30>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.SimpleAllocatorBlock' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.SimpleAllocatorBlock' objects>"
        'free': None, # (!) real value is "<method 'free' of 'panda3d.core.SimpleAllocatorBlock' objects>"
        'getAllocator': None, # (!) real value is "<method 'getAllocator' of 'panda3d.core.SimpleAllocatorBlock' objects>"
        'getMaxSize': None, # (!) real value is "<method 'getMaxSize' of 'panda3d.core.SimpleAllocatorBlock' objects>"
        'getNextBlock': None, # (!) real value is "<method 'getNextBlock' of 'panda3d.core.SimpleAllocatorBlock' objects>"
        'getSize': None, # (!) real value is "<method 'getSize' of 'panda3d.core.SimpleAllocatorBlock' objects>"
        'getStart': None, # (!) real value is "<method 'getStart' of 'panda3d.core.SimpleAllocatorBlock' objects>"
        'get_allocator': None, # (!) real value is "<method 'get_allocator' of 'panda3d.core.SimpleAllocatorBlock' objects>"
        'get_max_size': None, # (!) real value is "<method 'get_max_size' of 'panda3d.core.SimpleAllocatorBlock' objects>"
        'get_next_block': None, # (!) real value is "<method 'get_next_block' of 'panda3d.core.SimpleAllocatorBlock' objects>"
        'get_size': None, # (!) real value is "<method 'get_size' of 'panda3d.core.SimpleAllocatorBlock' objects>"
        'get_start': None, # (!) real value is "<method 'get_start' of 'panda3d.core.SimpleAllocatorBlock' objects>"
        'isFree': None, # (!) real value is "<method 'isFree' of 'panda3d.core.SimpleAllocatorBlock' objects>"
        'is_free': None, # (!) real value is "<method 'is_free' of 'panda3d.core.SimpleAllocatorBlock' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.SimpleAllocatorBlock' objects>"
        'realloc': None, # (!) real value is "<method 'realloc' of 'panda3d.core.SimpleAllocatorBlock' objects>"
    }


