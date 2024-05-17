# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .SimpleAllocatorBlock import SimpleAllocatorBlock

from .ReferenceCount import ReferenceCount

class VertexDataBlock(SimpleAllocatorBlock, ReferenceCount):
    """
    /**
     * A block of bytes that stores the actual raw vertex data referenced by a
     * GeomVertexArrayData object.
     */
    """
    def getNextBlock(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_next_block(VertexDataBlock self)
        
        /**
         * Returns a pointer to the next allocated block in the chain, or NULL if
         * there are no more allocated blocks.
         */
        """
        pass

    def getPage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_page(VertexDataBlock self)
        
        /**
         * Returns the page from which this buffer was allocated.
         */
        """
        pass

    def get_next_block(self, VertexDataBlock_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_next_block(VertexDataBlock self)
        
        /**
         * Returns a pointer to the next allocated block in the chain, or NULL if
         * there are no more allocated blocks.
         */
        """
        pass

    def get_page(self, VertexDataBlock_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_page(VertexDataBlock self)
        
        /**
         * Returns the page from which this buffer was allocated.
         */
        """
        pass

    def upcastToReferenceCount(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_ReferenceCount(const VertexDataBlock self)
        
        upcast from VertexDataBlock to ReferenceCount
        """
        pass

    def upcastToSimpleAllocatorBlock(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_SimpleAllocatorBlock(const VertexDataBlock self)
        
        upcast from VertexDataBlock to SimpleAllocatorBlock
        """
        pass

    def upcast_to_ReferenceCount(self, const_VertexDataBlock_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_ReferenceCount(const VertexDataBlock self)
        
        upcast from VertexDataBlock to ReferenceCount
        """
        pass

    def upcast_to_SimpleAllocatorBlock(self, const_VertexDataBlock_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_SimpleAllocatorBlock(const VertexDataBlock self)
        
        upcast from VertexDataBlock to SimpleAllocatorBlock
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
        '__doc__': '/**\n * A block of bytes that stores the actual raw vertex data referenced by a\n * GeomVertexArrayData object.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.VertexDataBlock' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2FB170>'
        'getNextBlock': None, # (!) real value is "<method 'getNextBlock' of 'panda3d.core.VertexDataBlock' objects>"
        'getPage': None, # (!) real value is "<method 'getPage' of 'panda3d.core.VertexDataBlock' objects>"
        'get_next_block': None, # (!) real value is "<method 'get_next_block' of 'panda3d.core.VertexDataBlock' objects>"
        'get_page': None, # (!) real value is "<method 'get_page' of 'panda3d.core.VertexDataBlock' objects>"
        'upcastToReferenceCount': None, # (!) real value is "<method 'upcastToReferenceCount' of 'panda3d.core.VertexDataBlock' objects>"
        'upcastToSimpleAllocatorBlock': None, # (!) real value is "<method 'upcastToSimpleAllocatorBlock' of 'panda3d.core.VertexDataBlock' objects>"
        'upcast_to_ReferenceCount': None, # (!) real value is "<method 'upcast_to_ReferenceCount' of 'panda3d.core.VertexDataBlock' objects>"
        'upcast_to_SimpleAllocatorBlock': None, # (!) real value is "<method 'upcast_to_SimpleAllocatorBlock' of 'panda3d.core.VertexDataBlock' objects>"
    }


