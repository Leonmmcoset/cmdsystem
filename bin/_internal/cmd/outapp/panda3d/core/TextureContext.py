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

class TextureContext(BufferContext, AdaptiveLruPage):
    """
    /**
     * This is a special class object that holds all the information returned by a
     * particular GSG to indicate the texture's internal context identifier.
     *
     * Textures typically have an immediate-mode and a retained-mode operation.
     * When using textures in retained-mode (in response to Texture::prepare()),
     * the GSG will create some internal handle for the texture and store it here.
     * The texture stores all of these handles internally.
     */
    """
    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getImageModified(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_image_modified(TextureContext self)
        
        /**
         * Returns a sequence number which is guaranteed to change at least every time
         * the texture image data (including mipmap levels) are modified.
         */
        """
        pass

    def getNativeBufferId(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_native_buffer_id(TextureContext self)
        
        /**
         * Similar to get_native_id, but some implementations use a separate
         * identifier for the buffer object associated with buffer textures.
         * Returns 0 if the underlying implementation does not support this, or
         * if this is not a buffer texture.
         */
        """
        pass

    def getNativeId(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_native_id(TextureContext self)
        
        /**
         * Returns an implementation-defined handle or pointer that can be used
         * to interface directly with the underlying API.
         * Returns 0 if the underlying implementation does not support this.
         */
        """
        pass

    def getPropertiesModified(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_properties_modified(TextureContext self)
        
        /**
         * Returns a sequence number which is guaranteed to change at least every time
         * the texture properties (unrelated to the image) are modified.
         */
        """
        pass

    def getSimpleImageModified(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_simple_image_modified(TextureContext self)
        
        /**
         * Returns a sequence number which is guaranteed to change at least every time
         * the texture's "simple" image data is modified.
         */
        """
        pass

    def getTexture(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_texture(TextureContext self)
        
        /**
         * Returns the pointer to the associated Texture object.
         */
        """
        pass

    def getView(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_view(TextureContext self)
        
        /**
         * Returns the specific view of a multiview texture this context represents.
         * In the usual case, with a non-multiview texture, this will be 0.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_image_modified(self, TextureContext_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_image_modified(TextureContext self)
        
        /**
         * Returns a sequence number which is guaranteed to change at least every time
         * the texture image data (including mipmap levels) are modified.
         */
        """
        pass

    def get_native_buffer_id(self, TextureContext_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_native_buffer_id(TextureContext self)
        
        /**
         * Similar to get_native_id, but some implementations use a separate
         * identifier for the buffer object associated with buffer textures.
         * Returns 0 if the underlying implementation does not support this, or
         * if this is not a buffer texture.
         */
        """
        pass

    def get_native_id(self, TextureContext_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_native_id(TextureContext self)
        
        /**
         * Returns an implementation-defined handle or pointer that can be used
         * to interface directly with the underlying API.
         * Returns 0 if the underlying implementation does not support this.
         */
        """
        pass

    def get_properties_modified(self, TextureContext_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_properties_modified(TextureContext self)
        
        /**
         * Returns a sequence number which is guaranteed to change at least every time
         * the texture properties (unrelated to the image) are modified.
         */
        """
        pass

    def get_simple_image_modified(self, TextureContext_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_simple_image_modified(TextureContext self)
        
        /**
         * Returns a sequence number which is guaranteed to change at least every time
         * the texture's "simple" image data is modified.
         */
        """
        pass

    def get_texture(self, TextureContext_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_texture(TextureContext self)
        
        /**
         * Returns the pointer to the associated Texture object.
         */
        """
        pass

    def get_view(self, TextureContext_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_view(TextureContext self)
        
        /**
         * Returns the specific view of a multiview texture this context represents.
         * In the usual case, with a non-multiview texture, this will be 0.
         */
        """
        pass

    def upcastToAdaptiveLruPage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_AdaptiveLruPage(const TextureContext self)
        
        upcast from TextureContext to AdaptiveLruPage
        """
        pass

    def upcastToBufferContext(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_BufferContext(const TextureContext self)
        
        upcast from TextureContext to BufferContext
        """
        pass

    def upcast_to_AdaptiveLruPage(self, const_TextureContext_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_AdaptiveLruPage(const TextureContext self)
        
        upcast from TextureContext to AdaptiveLruPage
        """
        pass

    def upcast_to_BufferContext(self, const_TextureContext_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_BufferContext(const TextureContext self)
        
        upcast from TextureContext to BufferContext
        """
        pass

    def wasImageModified(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        was_image_modified(TextureContext self)
        
        /**
         * Returns true if the texture image has been modified since the last time
         * mark_loaded() was called.
         */
        """
        pass

    def wasModified(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        was_modified(TextureContext self)
        
        /**
         * Returns true if the texture properties or image have been modified since
         * the last time mark_loaded() was called.
         */
        """
        pass

    def wasPropertiesModified(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        was_properties_modified(TextureContext self)
        
        /**
         * Returns true if the texture properties (unrelated to the image) have been
         * modified since the last time mark_loaded() was called.
         */
        """
        pass

    def wasSimpleImageModified(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        was_simple_image_modified(TextureContext self)
        
        /**
         * Returns true if the texture's "simple" image has been modified since the
         * last time mark_simple_loaded() was called.
         */
        """
        pass

    def was_image_modified(self, TextureContext_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        was_image_modified(TextureContext self)
        
        /**
         * Returns true if the texture image has been modified since the last time
         * mark_loaded() was called.
         */
        """
        pass

    def was_modified(self, TextureContext_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        was_modified(TextureContext self)
        
        /**
         * Returns true if the texture properties or image have been modified since
         * the last time mark_loaded() was called.
         */
        """
        pass

    def was_properties_modified(self, TextureContext_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        was_properties_modified(TextureContext self)
        
        /**
         * Returns true if the texture properties (unrelated to the image) have been
         * modified since the last time mark_loaded() was called.
         */
        """
        pass

    def was_simple_image_modified(self, TextureContext_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        was_simple_image_modified(TextureContext self)
        
        /**
         * Returns true if the texture's "simple" image has been modified since the
         * last time mark_simple_loaded() was called.
         */
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
        '__doc__': "/**\n * This is a special class object that holds all the information returned by a\n * particular GSG to indicate the texture's internal context identifier.\n *\n * Textures typically have an immediate-mode and a retained-mode operation.\n * When using textures in retained-mode (in response to Texture::prepare()),\n * the GSG will create some internal handle for the texture and store it here.\n * The texture stores all of these handles internally.\n */",
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.TextureContext' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE3006A0>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE3006A0>)>'
        'getImageModified': None, # (!) real value is "<method 'getImageModified' of 'panda3d.core.TextureContext' objects>"
        'getNativeBufferId': None, # (!) real value is "<method 'getNativeBufferId' of 'panda3d.core.TextureContext' objects>"
        'getNativeId': None, # (!) real value is "<method 'getNativeId' of 'panda3d.core.TextureContext' objects>"
        'getPropertiesModified': None, # (!) real value is "<method 'getPropertiesModified' of 'panda3d.core.TextureContext' objects>"
        'getSimpleImageModified': None, # (!) real value is "<method 'getSimpleImageModified' of 'panda3d.core.TextureContext' objects>"
        'getTexture': None, # (!) real value is "<method 'getTexture' of 'panda3d.core.TextureContext' objects>"
        'getView': None, # (!) real value is "<method 'getView' of 'panda3d.core.TextureContext' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE3006A0>)>'
        'get_image_modified': None, # (!) real value is "<method 'get_image_modified' of 'panda3d.core.TextureContext' objects>"
        'get_native_buffer_id': None, # (!) real value is "<method 'get_native_buffer_id' of 'panda3d.core.TextureContext' objects>"
        'get_native_id': None, # (!) real value is "<method 'get_native_id' of 'panda3d.core.TextureContext' objects>"
        'get_properties_modified': None, # (!) real value is "<method 'get_properties_modified' of 'panda3d.core.TextureContext' objects>"
        'get_simple_image_modified': None, # (!) real value is "<method 'get_simple_image_modified' of 'panda3d.core.TextureContext' objects>"
        'get_texture': None, # (!) real value is "<method 'get_texture' of 'panda3d.core.TextureContext' objects>"
        'get_view': None, # (!) real value is "<method 'get_view' of 'panda3d.core.TextureContext' objects>"
        'upcastToAdaptiveLruPage': None, # (!) real value is "<method 'upcastToAdaptiveLruPage' of 'panda3d.core.TextureContext' objects>"
        'upcastToBufferContext': None, # (!) real value is "<method 'upcastToBufferContext' of 'panda3d.core.TextureContext' objects>"
        'upcast_to_AdaptiveLruPage': None, # (!) real value is "<method 'upcast_to_AdaptiveLruPage' of 'panda3d.core.TextureContext' objects>"
        'upcast_to_BufferContext': None, # (!) real value is "<method 'upcast_to_BufferContext' of 'panda3d.core.TextureContext' objects>"
        'wasImageModified': None, # (!) real value is "<method 'wasImageModified' of 'panda3d.core.TextureContext' objects>"
        'wasModified': None, # (!) real value is "<method 'wasModified' of 'panda3d.core.TextureContext' objects>"
        'wasPropertiesModified': None, # (!) real value is "<method 'wasPropertiesModified' of 'panda3d.core.TextureContext' objects>"
        'wasSimpleImageModified': None, # (!) real value is "<method 'wasSimpleImageModified' of 'panda3d.core.TextureContext' objects>"
        'was_image_modified': None, # (!) real value is "<method 'was_image_modified' of 'panda3d.core.TextureContext' objects>"
        'was_modified': None, # (!) real value is "<method 'was_modified' of 'panda3d.core.TextureContext' objects>"
        'was_properties_modified': None, # (!) real value is "<method 'was_properties_modified' of 'panda3d.core.TextureContext' objects>"
        'was_simple_image_modified': None, # (!) real value is "<method 'was_simple_image_modified' of 'panda3d.core.TextureContext' objects>"
    }


