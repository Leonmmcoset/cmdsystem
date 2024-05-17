# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .SavedContext import SavedContext

class BufferContext(SavedContext):
    """
    /**
     * This is a base class for those kinds of SavedContexts that occupy an
     * easily-measured (and substantial) number of bytes in the video card's frame
     * buffer memory or AGP memory.  At the present, this includes most of the
     * SavedContext types: VertexBufferContext and IndexBufferContext, as well as
     * TextureContext.
     *
     * This class provides methods for tracking the video memory utilization, as
     * well as residency of each object, via PStats.
     */
    """
    def getActive(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_active(BufferContext self)
        
        /**
         * Returns the active flag associated with this object.  An object is
         * considered "active" if it was rendered in the current frame.
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getDataSizeBytes(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_data_size_bytes(BufferContext self)
        
        /**
         * Returns the number of bytes previously reported for the data object.  This
         * is used to track changes in the data object's allocated size; if it changes
         * from this, we need to create a new buffer.  This is also used to track
         * memory utilization in PStats.
         */
        """
        pass

    def getModified(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_modified(BufferContext self)
        
        /**
         * Returns the UpdateSeq that was recorded the last time mark_loaded() was
         * called.
         */
        """
        pass

    def getResident(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_resident(BufferContext self)
        
        /**
         * Returns the resident flag associated with this object.  An object is
         * considered "resident" if it appears to be resident in texture memory.
         */
        """
        pass

    def get_active(self, BufferContext_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_active(BufferContext self)
        
        /**
         * Returns the active flag associated with this object.  An object is
         * considered "active" if it was rendered in the current frame.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_data_size_bytes(self, BufferContext_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_data_size_bytes(BufferContext self)
        
        /**
         * Returns the number of bytes previously reported for the data object.  This
         * is used to track changes in the data object's allocated size; if it changes
         * from this, we need to create a new buffer.  This is also used to track
         * memory utilization in PStats.
         */
        """
        pass

    def get_modified(self, BufferContext_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_modified(BufferContext self)
        
        /**
         * Returns the UpdateSeq that was recorded the last time mark_loaded() was
         * called.
         */
        """
        pass

    def get_resident(self, BufferContext_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_resident(BufferContext self)
        
        /**
         * Returns the resident flag associated with this object.  An object is
         * considered "resident" if it appears to be resident in texture memory.
         */
        """
        pass

    def upcastToSavedContext(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_SavedContext(const BufferContext self)
        
        upcast from BufferContext to SavedContext
        """
        pass

    def upcast_to_SavedContext(self, const_BufferContext_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_SavedContext(const BufferContext self)
        
        upcast from BufferContext to SavedContext
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    active = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    data_size_bytes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    modified = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    object = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    resident = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': "/**\n * This is a base class for those kinds of SavedContexts that occupy an\n * easily-measured (and substantial) number of bytes in the video card's frame\n * buffer memory or AGP memory.  At the present, this includes most of the\n * SavedContext types: VertexBufferContext and IndexBufferContext, as well as\n * TextureContext.\n *\n * This class provides methods for tracking the video memory utilization, as\n * well as residency of each object, via PStats.\n */",
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.BufferContext' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2FC900>'
        'active': None, # (!) real value is "<attribute 'active' of 'panda3d.core.BufferContext' objects>"
        'data_size_bytes': None, # (!) real value is "<attribute 'data_size_bytes' of 'panda3d.core.BufferContext' objects>"
        'getActive': None, # (!) real value is "<method 'getActive' of 'panda3d.core.BufferContext' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2FC900>)>'
        'getDataSizeBytes': None, # (!) real value is "<method 'getDataSizeBytes' of 'panda3d.core.BufferContext' objects>"
        'getModified': None, # (!) real value is "<method 'getModified' of 'panda3d.core.BufferContext' objects>"
        'getResident': None, # (!) real value is "<method 'getResident' of 'panda3d.core.BufferContext' objects>"
        'get_active': None, # (!) real value is "<method 'get_active' of 'panda3d.core.BufferContext' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2FC900>)>'
        'get_data_size_bytes': None, # (!) real value is "<method 'get_data_size_bytes' of 'panda3d.core.BufferContext' objects>"
        'get_modified': None, # (!) real value is "<method 'get_modified' of 'panda3d.core.BufferContext' objects>"
        'get_resident': None, # (!) real value is "<method 'get_resident' of 'panda3d.core.BufferContext' objects>"
        'modified': None, # (!) real value is "<attribute 'modified' of 'panda3d.core.BufferContext' objects>"
        'object': None, # (!) real value is "<attribute 'object' of 'panda3d.core.BufferContext' objects>"
        'resident': None, # (!) real value is "<attribute 'resident' of 'panda3d.core.BufferContext' objects>"
        'upcastToSavedContext': None, # (!) real value is "<method 'upcastToSavedContext' of 'panda3d.core.BufferContext' objects>"
        'upcast_to_SavedContext': None, # (!) real value is "<method 'upcast_to_SavedContext' of 'panda3d.core.BufferContext' objects>"
    }


