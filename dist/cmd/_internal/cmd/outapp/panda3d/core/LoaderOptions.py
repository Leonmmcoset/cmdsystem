# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class LoaderOptions(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * Specifies parameters that may be passed to the loader.
     */
    """
    def getAutoTextureScale(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_auto_texture_scale(LoaderOptions self)
        
        /**
         * See set_auto_texture_scale().
         */
        """
        pass

    def getFlags(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_flags(LoaderOptions self)
        
        /**
         *
         */
        """
        pass

    def getTextureFlags(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_texture_flags(LoaderOptions self)
        
        /**
         *
         */
        """
        pass

    def getTextureNumViews(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_texture_num_views(LoaderOptions self)
        
        /**
         * See set_texture_num_views().
         */
        """
        pass

    def get_auto_texture_scale(self, LoaderOptions_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_auto_texture_scale(LoaderOptions self)
        
        /**
         * See set_auto_texture_scale().
         */
        """
        pass

    def get_flags(self, LoaderOptions_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_flags(LoaderOptions self)
        
        /**
         *
         */
        """
        pass

    def get_texture_flags(self, LoaderOptions_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_texture_flags(LoaderOptions self)
        
        /**
         *
         */
        """
        pass

    def get_texture_num_views(self, LoaderOptions_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_texture_num_views(LoaderOptions self)
        
        /**
         * See set_texture_num_views().
         */
        """
        pass

    def output(self, LoaderOptions_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(LoaderOptions self, ostream out)
        
        /**
         *
         */
        """
        pass

    def setAutoTextureScale(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_auto_texture_scale(const LoaderOptions self, int scale)
        
        /**
         * Set this flag to ATS_none, ATS_up, ATS_down, or ATS_pad to control how a
         * texture is scaled from disk when it is subsequently loaded.  Set it to
         * ATS_unspecified to restore the default behavior.
         */
        """
        pass

    def setFlags(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_flags(const LoaderOptions self, int flags)
        
        /**
         *
         */
        """
        pass

    def setTextureFlags(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_texture_flags(const LoaderOptions self, int flags)
        
        /**
         *
         */
        """
        pass

    def setTextureNumViews(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_texture_num_views(const LoaderOptions self, int num_views)
        
        /**
         * Specifies the expected number of views to load for the texture.  This is
         * ignored unless TF_multiview is included in texture_flags.  This must be
         * specified when loading a 3-d multiview texture or 2-d texture array, in
         * which case it is used to differentiate z levels from separate views; it
         * may be zero in the case of 2-d textures or cube maps, in which case the
         * number of views can be inferred from the number of images found on disk.
         */
        """
        pass

    def set_auto_texture_scale(self, const_LoaderOptions_self, int_scale): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_auto_texture_scale(const LoaderOptions self, int scale)
        
        /**
         * Set this flag to ATS_none, ATS_up, ATS_down, or ATS_pad to control how a
         * texture is scaled from disk when it is subsequently loaded.  Set it to
         * ATS_unspecified to restore the default behavior.
         */
        """
        pass

    def set_flags(self, const_LoaderOptions_self, int_flags): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_flags(const LoaderOptions self, int flags)
        
        /**
         *
         */
        """
        pass

    def set_texture_flags(self, const_LoaderOptions_self, int_flags): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_texture_flags(const LoaderOptions self, int flags)
        
        /**
         *
         */
        """
        pass

    def set_texture_num_views(self, const_LoaderOptions_self, int_num_views): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_texture_num_views(const LoaderOptions self, int num_views)
        
        /**
         * Specifies the expected number of views to load for the texture.  This is
         * ignored unless TF_multiview is included in texture_flags.  This must be
         * specified when loading a 3-d multiview texture or 2-d texture array, in
         * which case it is used to differentiate z levels from separate views; it
         * may be zero in the case of 2-d textures or cube maps, in which case the
         * number of views can be inferred from the number of images found on disk.
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

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    auto_texture_scale = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    texture_flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    texture_num_views = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        'LFAllowInstance': 128,
        'LFCacheOnly': 64,
        'LFConvertAnim': 12,
        'LFConvertChannels': 8,
        'LFConvertSkeleton': 4,
        'LFNoCache': 48,
        'LFNoDiskCache': 16,
        'LFNoRamCache': 32,
        'LFReportErrors': 2,
        'LFSearch': 1,
        'LF_allow_instance': 128,
        'LF_cache_only': 64,
        'LF_convert_anim': 12,
        'LF_convert_channels': 8,
        'LF_convert_skeleton': 4,
        'LF_no_cache': 48,
        'LF_no_disk_cache': 16,
        'LF_no_ram_cache': 32,
        'LF_report_errors': 2,
        'LF_search': 1,
        'TFAllow1d': 16,
        'TFAllowCompression': 512,
        'TFFloat': 256,
        'TFGenerateMipmaps': 32,
        'TFInteger': 128,
        'TFMultiview': 64,
        'TFPreload': 4,
        'TFPreloadSimple': 8,
        'TF_allow_1d': 16,
        'TF_allow_compression': 512,
        'TF_float': 256,
        'TF_generate_mipmaps': 32,
        'TF_integer': 128,
        'TF_multiview': 64,
        'TF_preload': 4,
        'TF_preload_simple': 8,
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.LoaderOptions' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.LoaderOptions' objects>"
        '__doc__': '/**\n * Specifies parameters that may be passed to the loader.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.LoaderOptions' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE36FE40>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.LoaderOptions' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.LoaderOptions' objects>"
        'auto_texture_scale': None, # (!) real value is "<attribute 'auto_texture_scale' of 'panda3d.core.LoaderOptions' objects>"
        'flags': None, # (!) real value is "<attribute 'flags' of 'panda3d.core.LoaderOptions' objects>"
        'getAutoTextureScale': None, # (!) real value is "<method 'getAutoTextureScale' of 'panda3d.core.LoaderOptions' objects>"
        'getFlags': None, # (!) real value is "<method 'getFlags' of 'panda3d.core.LoaderOptions' objects>"
        'getTextureFlags': None, # (!) real value is "<method 'getTextureFlags' of 'panda3d.core.LoaderOptions' objects>"
        'getTextureNumViews': None, # (!) real value is "<method 'getTextureNumViews' of 'panda3d.core.LoaderOptions' objects>"
        'get_auto_texture_scale': None, # (!) real value is "<method 'get_auto_texture_scale' of 'panda3d.core.LoaderOptions' objects>"
        'get_flags': None, # (!) real value is "<method 'get_flags' of 'panda3d.core.LoaderOptions' objects>"
        'get_texture_flags': None, # (!) real value is "<method 'get_texture_flags' of 'panda3d.core.LoaderOptions' objects>"
        'get_texture_num_views': None, # (!) real value is "<method 'get_texture_num_views' of 'panda3d.core.LoaderOptions' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.LoaderOptions' objects>"
        'setAutoTextureScale': None, # (!) real value is "<method 'setAutoTextureScale' of 'panda3d.core.LoaderOptions' objects>"
        'setFlags': None, # (!) real value is "<method 'setFlags' of 'panda3d.core.LoaderOptions' objects>"
        'setTextureFlags': None, # (!) real value is "<method 'setTextureFlags' of 'panda3d.core.LoaderOptions' objects>"
        'setTextureNumViews': None, # (!) real value is "<method 'setTextureNumViews' of 'panda3d.core.LoaderOptions' objects>"
        'set_auto_texture_scale': None, # (!) real value is "<method 'set_auto_texture_scale' of 'panda3d.core.LoaderOptions' objects>"
        'set_flags': None, # (!) real value is "<method 'set_flags' of 'panda3d.core.LoaderOptions' objects>"
        'set_texture_flags': None, # (!) real value is "<method 'set_texture_flags' of 'panda3d.core.LoaderOptions' objects>"
        'set_texture_num_views': None, # (!) real value is "<method 'set_texture_num_views' of 'panda3d.core.LoaderOptions' objects>"
        'texture_flags': None, # (!) real value is "<attribute 'texture_flags' of 'panda3d.core.LoaderOptions' objects>"
        'texture_num_views': None, # (!) real value is "<attribute 'texture_num_views' of 'panda3d.core.LoaderOptions' objects>"
    }
    LFAllowInstance = 128
    LFCacheOnly = 64
    LFConvertAnim = 12
    LFConvertChannels = 8
    LFConvertSkeleton = 4
    LFNoCache = 48
    LFNoDiskCache = 16
    LFNoRamCache = 32
    LFReportErrors = 2
    LFSearch = 1
    LF_allow_instance = 128
    LF_cache_only = 64
    LF_convert_anim = 12
    LF_convert_channels = 8
    LF_convert_skeleton = 4
    LF_no_cache = 48
    LF_no_disk_cache = 16
    LF_no_ram_cache = 32
    LF_report_errors = 2
    LF_search = 1
    TFAllow1d = 16
    TFAllowCompression = 512
    TFFloat = 256
    TFGenerateMipmaps = 32
    TFInteger = 128
    TFMultiview = 64
    TFPreload = 4
    TFPreloadSimple = 8
    TF_allow_1d = 16
    TF_allow_compression = 512
    TF_float = 256
    TF_generate_mipmaps = 32
    TF_integer = 128
    TF_multiview = 64
    TF_preload = 4
    TF_preload_simple = 8


