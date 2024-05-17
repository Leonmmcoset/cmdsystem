# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .ParamValueBase import ParamValueBase

class ParamTextureImage(ParamValueBase):
    """
    /**
     * A class object for storing a pointer to a Texture along with a set of
     * properties that indicates which image to bind to a shader input.
     *
     * This class is useful for binding texture images to a shader, which is a
     * fairly esoteric feature.
     */
    """
    def getBindLayer(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_bind_layer(ParamTextureImage self)
        
        /**
         * Returns the image layer that should be bound.  This is undefined if
         * get_bind_layered() returns false.
         */
        """
        pass

    def getBindLayered(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_bind_layered(ParamTextureImage self)
        
        /**
         * Returns true if all layers of this image should be bound simultaneously.
         */
        """
        pass

    def getBindLevel(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_bind_level(ParamTextureImage self)
        
        /**
         * Returns the image level that should be bound.
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getTexture(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_texture(ParamTextureImage self)
        
        /**
         * Retrieves the texture stored in the parameter.
         */
        """
        pass

    def get_bind_layer(self, ParamTextureImage_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_bind_layer(ParamTextureImage self)
        
        /**
         * Returns the image layer that should be bound.  This is undefined if
         * get_bind_layered() returns false.
         */
        """
        pass

    def get_bind_layered(self, ParamTextureImage_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_bind_layered(ParamTextureImage self)
        
        /**
         * Returns true if all layers of this image should be bound simultaneously.
         */
        """
        pass

    def get_bind_level(self, ParamTextureImage_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_bind_level(ParamTextureImage self)
        
        /**
         * Returns the image level that should be bound.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_texture(self, ParamTextureImage_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_texture(ParamTextureImage self)
        
        /**
         * Retrieves the texture stored in the parameter.
         */
        """
        pass

    def hasReadAccess(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_read_access(ParamTextureImage self)
        
        /**
         * Returns true if this image should be bound with read access enabled.
         */
        """
        pass

    def hasWriteAccess(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_write_access(ParamTextureImage self)
        
        /**
         * Returns true if this image should be bound with write access enabled.
         */
        """
        pass

    def has_read_access(self, ParamTextureImage_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_read_access(ParamTextureImage self)
        
        /**
         * Returns true if this image should be bound with read access enabled.
         */
        """
        pass

    def has_write_access(self, ParamTextureImage_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_write_access(ParamTextureImage self)
        
        /**
         * Returns true if this image should be bound with write access enabled.
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    bind_layer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    bind_level = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    read_access = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    texture = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    write_access = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * A class object for storing a pointer to a Texture along with a set of\n * properties that indicates which image to bind to a shader input.\n *\n * This class is useful for binding texture images to a shader, which is a\n * fairly esoteric feature.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.ParamTextureImage' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE300130>'
        'bind_layer': None, # (!) real value is "<attribute 'bind_layer' of 'panda3d.core.ParamTextureImage' objects>"
        'bind_level': None, # (!) real value is "<attribute 'bind_level' of 'panda3d.core.ParamTextureImage' objects>"
        'getBindLayer': None, # (!) real value is "<method 'getBindLayer' of 'panda3d.core.ParamTextureImage' objects>"
        'getBindLayered': None, # (!) real value is "<method 'getBindLayered' of 'panda3d.core.ParamTextureImage' objects>"
        'getBindLevel': None, # (!) real value is "<method 'getBindLevel' of 'panda3d.core.ParamTextureImage' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE300130>)>'
        'getTexture': None, # (!) real value is "<method 'getTexture' of 'panda3d.core.ParamTextureImage' objects>"
        'get_bind_layer': None, # (!) real value is "<method 'get_bind_layer' of 'panda3d.core.ParamTextureImage' objects>"
        'get_bind_layered': None, # (!) real value is "<method 'get_bind_layered' of 'panda3d.core.ParamTextureImage' objects>"
        'get_bind_level': None, # (!) real value is "<method 'get_bind_level' of 'panda3d.core.ParamTextureImage' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE300130>)>'
        'get_texture': None, # (!) real value is "<method 'get_texture' of 'panda3d.core.ParamTextureImage' objects>"
        'hasReadAccess': None, # (!) real value is "<method 'hasReadAccess' of 'panda3d.core.ParamTextureImage' objects>"
        'hasWriteAccess': None, # (!) real value is "<method 'hasWriteAccess' of 'panda3d.core.ParamTextureImage' objects>"
        'has_read_access': None, # (!) real value is "<method 'has_read_access' of 'panda3d.core.ParamTextureImage' objects>"
        'has_write_access': None, # (!) real value is "<method 'has_write_access' of 'panda3d.core.ParamTextureImage' objects>"
        'read_access': None, # (!) real value is "<attribute 'read_access' of 'panda3d.core.ParamTextureImage' objects>"
        'texture': None, # (!) real value is "<attribute 'texture' of 'panda3d.core.ParamTextureImage' objects>"
        'write_access': None, # (!) real value is "<attribute 'write_access' of 'panda3d.core.ParamTextureImage' objects>"
    }


