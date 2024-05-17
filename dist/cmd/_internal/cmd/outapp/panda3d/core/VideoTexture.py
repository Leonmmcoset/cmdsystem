# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .Texture import Texture

from .AnimInterface import AnimInterface

class VideoTexture(Texture, AnimInterface):
    """
    /**
     * The base class for a family of animated Textures that take their input from
     * a video source, such as a movie file.  These Textures may be stopped,
     * started, etc.  using the AnimInterface controls, similar to an animated
     * character.
     */
    """
    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getKeepRamImage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_keep_ram_image(VideoTexture self)
        
        /**
         * Returns the flag that indicates whether this Texture is eligible to have
         * its main RAM copy of the texture memory dumped when the texture is prepared
         * for rendering.  See set_keep_ram_image().
         */
        """
        pass

    def getVideoHeight(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_video_height(VideoTexture self)
        
        /**
         * Returns the height in texels of the source video stream.  This is not
         * necessarily the height of the actual texture, since the texture may have
         * been expanded to raise it to a power of 2.
         */
        """
        pass

    def getVideoWidth(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_video_width(VideoTexture self)
        
        /**
         * Returns the width in texels of the source video stream.  This is not
         * necessarily the width of the actual texture, since the texture may have
         * been expanded to raise it to a power of 2.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_keep_ram_image(self, VideoTexture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_keep_ram_image(VideoTexture self)
        
        /**
         * Returns the flag that indicates whether this Texture is eligible to have
         * its main RAM copy of the texture memory dumped when the texture is prepared
         * for rendering.  See set_keep_ram_image().
         */
        """
        pass

    def get_video_height(self, VideoTexture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_video_height(VideoTexture self)
        
        /**
         * Returns the height in texels of the source video stream.  This is not
         * necessarily the height of the actual texture, since the texture may have
         * been expanded to raise it to a power of 2.
         */
        """
        pass

    def get_video_width(self, VideoTexture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_video_width(VideoTexture self)
        
        /**
         * Returns the width in texels of the source video stream.  This is not
         * necessarily the width of the actual texture, since the texture may have
         * been expanded to raise it to a power of 2.
         */
        """
        pass

    def upcastToAnimInterface(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_AnimInterface(const VideoTexture self)
        
        upcast from VideoTexture to AnimInterface
        """
        pass

    def upcastToTexture(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_Texture(const VideoTexture self)
        
        upcast from VideoTexture to Texture
        """
        pass

    def upcast_to_AnimInterface(self, const_VideoTexture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_AnimInterface(const VideoTexture self)
        
        upcast from VideoTexture to AnimInterface
        """
        pass

    def upcast_to_Texture(self, const_VideoTexture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_Texture(const VideoTexture self)
        
        upcast from VideoTexture to Texture
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    video_height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    video_width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * The base class for a family of animated Textures that take their input from\n * a video source, such as a movie file.  These Textures may be stopped,\n * started, etc.  using the AnimInterface controls, similar to an animated\n * character.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.VideoTexture' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE300DE0>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE300DE0>)>'
        'getKeepRamImage': None, # (!) real value is "<method 'getKeepRamImage' of 'panda3d.core.VideoTexture' objects>"
        'getVideoHeight': None, # (!) real value is "<method 'getVideoHeight' of 'panda3d.core.VideoTexture' objects>"
        'getVideoWidth': None, # (!) real value is "<method 'getVideoWidth' of 'panda3d.core.VideoTexture' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE300DE0>)>'
        'get_keep_ram_image': None, # (!) real value is "<method 'get_keep_ram_image' of 'panda3d.core.VideoTexture' objects>"
        'get_video_height': None, # (!) real value is "<method 'get_video_height' of 'panda3d.core.VideoTexture' objects>"
        'get_video_width': None, # (!) real value is "<method 'get_video_width' of 'panda3d.core.VideoTexture' objects>"
        'upcastToAnimInterface': None, # (!) real value is "<method 'upcastToAnimInterface' of 'panda3d.core.VideoTexture' objects>"
        'upcastToTexture': None, # (!) real value is "<method 'upcastToTexture' of 'panda3d.core.VideoTexture' objects>"
        'upcast_to_AnimInterface': None, # (!) real value is "<method 'upcast_to_AnimInterface' of 'panda3d.core.VideoTexture' objects>"
        'upcast_to_Texture': None, # (!) real value is "<method 'upcast_to_Texture' of 'panda3d.core.VideoTexture' objects>"
        'video_height': None, # (!) real value is "<attribute 'video_height' of 'panda3d.core.VideoTexture' objects>"
        'video_width': None, # (!) real value is "<attribute 'video_width' of 'panda3d.core.VideoTexture' objects>"
    }


