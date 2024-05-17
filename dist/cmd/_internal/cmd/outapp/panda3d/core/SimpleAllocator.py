# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class SimpleAllocator(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * An implementation of a very simple block allocator.  This class can
     * allocate ranges of nonnegative integers within a specified upper limit; it
     * uses a simple first-fit algorithm to find the next available space.
     */
    """
    def alloc(self, const_SimpleAllocator_self, int_size, int_alignment): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        alloc(const SimpleAllocator self, int size, int alignment)
        
        /**
         * Allocates a new block.  Returns NULL if a block of the requested size
         * cannot be allocated.
         *
         * To free the allocated block, call block->free(), or simply delete the block
         * pointer.
         */
        """
        pass

    def getContiguous(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_contiguous(SimpleAllocator self)
        
        /**
         * Returns an upper-bound estimate of the size of the largest contiguous block
         * that may be allocated.  It is guaranteed that an attempt to allocate a
         * block larger than this will fail, though it is not guaranteed that an
         * attempt to allocate a block this size or smaller will succeed.
         */
        """
        pass

    def getFirstBlock(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_first_block(SimpleAllocator self)
        
        /**
         * Returns a pointer to the first allocated block, or NULL if there are no
         * allocated blocks.
         */
        """
        pass

    def getMaxSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_max_size(SimpleAllocator self)
        
        /**
         * Returns the available space for allocated objects.
         */
        """
        pass

    def getTotalSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_total_size(SimpleAllocator self)
        
        /**
         * Returns the total size of allocated objects.
         */
        """
        pass

    def get_contiguous(self, SimpleAllocator_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_contiguous(SimpleAllocator self)
        
        /**
         * Returns an upper-bound estimate of the size of the largest contiguous block
         * that may be allocated.  It is guaranteed that an attempt to allocate a
         * block larger than this will fail, though it is not guaranteed that an
         * attempt to allocate a block this size or smaller will succeed.
         */
        """
        pass

    def get_first_block(self, SimpleAllocator_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_first_block(SimpleAllocator self)
        
        /**
         * Returns a pointer to the first allocated block, or NULL if there are no
         * allocated blocks.
         */
        """
        pass

    def get_max_size(self, SimpleAllocator_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_max_size(SimpleAllocator self)
        
        /**
         * Returns the available space for allocated objects.
         */
        """
        pass

    def get_total_size(self, SimpleAllocator_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_total_size(SimpleAllocator self)
        
        /**
         * Returns the total size of allocated objects.
         */
        """
        pass

    def isEmpty(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_empty(SimpleAllocator self)
        
        /**
         * Returns true if there are no blocks allocated on this page, or false if
         * there is at least one.
         */
        """
        pass

    def is_empty(self, SimpleAllocator_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_empty(SimpleAllocator self)
        
        /**
         * Returns true if there are no blocks allocated on this page, or false if
         * there is at least one.
         */
        """
        pass

    def output(self, SimpleAllocator_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(SimpleAllocator self, ostream out)
        
        /**
         *
         */
        """
        pass

    def setMaxSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_max_size(const SimpleAllocator self, int max_size)
        
        /**
         * Changes the available space for allocated objects.  This will not affect
         * any already-allocated objects, but will have an effect on future calls to
         * alloc().
         */
        """
        pass

    def set_max_size(self, const_SimpleAllocator_self, int_max_size): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_max_size(const SimpleAllocator self, int max_size)
        
        /**
         * Changes the available space for allocated objects.  This will not affect
         * any already-allocated objects, but will have an effect on future calls to
         * alloc().
         */
        """
        pass

    def write(self, SimpleAllocator_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(SimpleAllocator self, ostream out)
        
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
        '__doc__': '/**\n * An implementation of a very simple block allocator.  This class can\n * allocate ranges of nonnegative integers within a specified upper limit; it\n * uses a simple first-fit algorithm to find the next available space.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.SimpleAllocator' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2FA860>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.SimpleAllocator' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.SimpleAllocator' objects>"
        'alloc': None, # (!) real value is "<method 'alloc' of 'panda3d.core.SimpleAllocator' objects>"
        'getContiguous': None, # (!) real value is "<method 'getContiguous' of 'panda3d.core.SimpleAllocator' objects>"
        'getFirstBlock': None, # (!) real value is "<method 'getFirstBlock' of 'panda3d.core.SimpleAllocator' objects>"
        'getMaxSize': None, # (!) real value is "<method 'getMaxSize' of 'panda3d.core.SimpleAllocator' objects>"
        'getTotalSize': None, # (!) real value is "<method 'getTotalSize' of 'panda3d.core.SimpleAllocator' objects>"
        'get_contiguous': None, # (!) real value is "<method 'get_contiguous' of 'panda3d.core.SimpleAllocator' objects>"
        'get_first_block': None, # (!) real value is "<method 'get_first_block' of 'panda3d.core.SimpleAllocator' objects>"
        'get_max_size': None, # (!) real value is "<method 'get_max_size' of 'panda3d.core.SimpleAllocator' objects>"
        'get_total_size': None, # (!) real value is "<method 'get_total_size' of 'panda3d.core.SimpleAllocator' objects>"
        'isEmpty': None, # (!) real value is "<method 'isEmpty' of 'panda3d.core.SimpleAllocator' objects>"
        'is_empty': None, # (!) real value is "<method 'is_empty' of 'panda3d.core.SimpleAllocator' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.SimpleAllocator' objects>"
        'setMaxSize': None, # (!) real value is "<method 'setMaxSize' of 'panda3d.core.SimpleAllocator' objects>"
        'set_max_size': None, # (!) real value is "<method 'set_max_size' of 'panda3d.core.SimpleAllocator' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.core.SimpleAllocator' objects>"
    }


