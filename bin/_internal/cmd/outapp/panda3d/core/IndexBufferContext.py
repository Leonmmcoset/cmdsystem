# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .BufferContext import BufferContext

from .AdaptiveLruPage import AdaptiveLruPage

class IndexBufferContext(BufferContext, AdaptiveLruPage):
    """
    /**
     * This is a special class object that holds all the information returned by a
     * particular GSG to indicate the vertex data array's internal context
     * identifier.
     *
     * This allows the GSG to cache the vertex data array in whatever way makes
     * sense.  For instance, DirectX can allocate a vertex buffer for the array.
     * OpenGL can create a buffer object.
     */
    """
    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getData(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_data(IndexBufferContext self)
        
        /**
         * Returns the pointer to the client-side array data object.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_data(self, IndexBufferContext_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_data(IndexBufferContext self)
        
        /**
         * Returns the pointer to the client-side array data object.
         */
        """
        pass

    def upcastToAdaptiveLruPage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_AdaptiveLruPage(const IndexBufferContext self)
        
        upcast from IndexBufferContext to AdaptiveLruPage
        """
        pass

    def upcastToBufferContext(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_BufferContext(const IndexBufferContext self)
        
        upcast from IndexBufferContext to BufferContext
        """
        pass

    def upcast_to_AdaptiveLruPage(self, const_IndexBufferContext_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_AdaptiveLruPage(const IndexBufferContext self)
        
        upcast from IndexBufferContext to AdaptiveLruPage
        """
        pass

    def upcast_to_BufferContext(self, const_IndexBufferContext_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_BufferContext(const IndexBufferContext self)
        
        upcast from IndexBufferContext to BufferContext
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
        '__doc__': "/**\n * This is a special class object that holds all the information returned by a\n * particular GSG to indicate the vertex data array's internal context\n * identifier.\n *\n * This allows the GSG to cache the vertex data array in whatever way makes\n * sense.  For instance, DirectX can allocate a vertex buffer for the array.\n * OpenGL can create a buffer object.\n */",
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.IndexBufferContext' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2FF480>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2FF480>)>'
        'getData': None, # (!) real value is "<method 'getData' of 'panda3d.core.IndexBufferContext' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2FF480>)>'
        'get_data': None, # (!) real value is "<method 'get_data' of 'panda3d.core.IndexBufferContext' objects>"
        'upcastToAdaptiveLruPage': None, # (!) real value is "<method 'upcastToAdaptiveLruPage' of 'panda3d.core.IndexBufferContext' objects>"
        'upcastToBufferContext': None, # (!) real value is "<method 'upcastToBufferContext' of 'panda3d.core.IndexBufferContext' objects>"
        'upcast_to_AdaptiveLruPage': None, # (!) real value is "<method 'upcast_to_AdaptiveLruPage' of 'panda3d.core.IndexBufferContext' objects>"
        'upcast_to_BufferContext': None, # (!) real value is "<method 'upcast_to_BufferContext' of 'panda3d.core.IndexBufferContext' objects>"
    }


