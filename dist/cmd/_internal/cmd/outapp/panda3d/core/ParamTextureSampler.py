# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .ParamValueBase import ParamValueBase

class ParamTextureSampler(ParamValueBase):
    """
    /**
     * A class object for storing a pointer to a Texture along with a sampler
     * state that indicates how to to sample the given texture.
     */
    """
    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getSampler(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_sampler(ParamTextureSampler self)
        
        /**
         * Retrieves the sampler state stored in the parameter.
         */
        """
        pass

    def getTexture(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_texture(ParamTextureSampler self)
        
        /**
         * Retrieves the texture stored in the parameter.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_sampler(self, ParamTextureSampler_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_sampler(ParamTextureSampler self)
        
        /**
         * Retrieves the sampler state stored in the parameter.
         */
        """
        pass

    def get_texture(self, ParamTextureSampler_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_texture(ParamTextureSampler self)
        
        /**
         * Retrieves the texture stored in the parameter.
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    sampler = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    texture = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * A class object for storing a pointer to a Texture along with a sampler\n * state that indicates how to to sample the given texture.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.ParamTextureSampler' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2FFF60>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2FFF60>)>'
        'getSampler': None, # (!) real value is "<method 'getSampler' of 'panda3d.core.ParamTextureSampler' objects>"
        'getTexture': None, # (!) real value is "<method 'getTexture' of 'panda3d.core.ParamTextureSampler' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2FFF60>)>'
        'get_sampler': None, # (!) real value is "<method 'get_sampler' of 'panda3d.core.ParamTextureSampler' objects>"
        'get_texture': None, # (!) real value is "<method 'get_texture' of 'panda3d.core.ParamTextureSampler' objects>"
        'sampler': None, # (!) real value is "<attribute 'sampler' of 'panda3d.core.ParamTextureSampler' objects>"
        'texture': None, # (!) real value is "<attribute 'texture' of 'panda3d.core.ParamTextureSampler' objects>"
    }


