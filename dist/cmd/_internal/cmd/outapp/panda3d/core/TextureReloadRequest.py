# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .AsyncTask import AsyncTask

class TextureReloadRequest(AsyncTask):
    """
    /**
     * This loader request will call Texture::get_ram_image() in a sub-thread, to
     * force the texture's image to be re-read from disk.  It is used by
     * GraphicsStateGuardian::async_reload_texture(), when get_incomplete_render()
     * is true.
     */
    """
    def getAllowCompressed(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_allow_compressed(TextureReloadRequest self)
        
        /**
         * Returns the "allow compressed" flag associated with this asynchronous
         * TextureReloadRequest.
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getPreparedGraphicsObjects(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_prepared_graphics_objects(TextureReloadRequest self)
        
        /**
         * Returns the PreparedGraphicsObjects object associated with this
         * asynchronous TextureReloadRequest.
         */
        """
        pass

    def getTexture(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_texture(TextureReloadRequest self)
        
        /**
         * Returns the Texture object associated with this asynchronous
         * TextureReloadRequest.
         */
        """
        pass

    def get_allow_compressed(self, TextureReloadRequest_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_allow_compressed(TextureReloadRequest self)
        
        /**
         * Returns the "allow compressed" flag associated with this asynchronous
         * TextureReloadRequest.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_prepared_graphics_objects(self, TextureReloadRequest_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_prepared_graphics_objects(TextureReloadRequest self)
        
        /**
         * Returns the PreparedGraphicsObjects object associated with this
         * asynchronous TextureReloadRequest.
         */
        """
        pass

    def get_texture(self, TextureReloadRequest_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_texture(TextureReloadRequest self)
        
        /**
         * Returns the Texture object associated with this asynchronous
         * TextureReloadRequest.
         */
        """
        pass

    def isReady(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_ready(TextureReloadRequest self)
        
        /**
         * Returns true if this request has completed, false if it is still pending.
         * Equivalent to `req.done() and not req.cancelled()`.
         * @see done()
         */
        """
        pass

    def is_ready(self, TextureReloadRequest_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_ready(TextureReloadRequest self)
        
        /**
         * Returns true if this request has completed, false if it is still pending.
         * Equivalent to `req.done() and not req.cancelled()`.
         * @see done()
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

    texture = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.TextureReloadRequest' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.TextureReloadRequest' objects>"
        '__doc__': "/**\n * This loader request will call Texture::get_ram_image() in a sub-thread, to\n * force the texture's image to be re-read from disk.  It is used by\n * GraphicsStateGuardian::async_reload_texture(), when get_incomplete_render()\n * is true.\n */",
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.TextureReloadRequest' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE3004D0>'
        'getAllowCompressed': None, # (!) real value is "<method 'getAllowCompressed' of 'panda3d.core.TextureReloadRequest' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE3004D0>)>'
        'getPreparedGraphicsObjects': None, # (!) real value is "<method 'getPreparedGraphicsObjects' of 'panda3d.core.TextureReloadRequest' objects>"
        'getTexture': None, # (!) real value is "<method 'getTexture' of 'panda3d.core.TextureReloadRequest' objects>"
        'get_allow_compressed': None, # (!) real value is "<method 'get_allow_compressed' of 'panda3d.core.TextureReloadRequest' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE3004D0>)>'
        'get_prepared_graphics_objects': None, # (!) real value is "<method 'get_prepared_graphics_objects' of 'panda3d.core.TextureReloadRequest' objects>"
        'get_texture': None, # (!) real value is "<method 'get_texture' of 'panda3d.core.TextureReloadRequest' objects>"
        'isReady': None, # (!) real value is "<method 'isReady' of 'panda3d.core.TextureReloadRequest' objects>"
        'is_ready': None, # (!) real value is "<method 'is_ready' of 'panda3d.core.TextureReloadRequest' objects>"
        'texture': None, # (!) real value is "<attribute 'texture' of 'panda3d.core.TextureReloadRequest' objects>"
    }


