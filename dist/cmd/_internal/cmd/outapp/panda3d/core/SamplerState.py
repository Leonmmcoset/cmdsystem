# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class SamplerState(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * Represents a set of settings that indicate how a texture is sampled.  This
     * can be used to sample the same texture using different settings in
     * different places.
     */
    """
    def formatFilterType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        format_filter_type(int ft)
        
        /**
         * Returns the indicated FilterType converted to a string word.
         */
        """
        pass

    def formatWrapMode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        format_wrap_mode(int wm)
        
        /**
         * Returns the indicated WrapMode converted to a string word.
         */
        """
        pass

    def format_filter_type(self, int_ft): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        format_filter_type(int ft)
        
        /**
         * Returns the indicated FilterType converted to a string word.
         */
        """
        pass

    def format_wrap_mode(self, int_wm): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        format_wrap_mode(int wm)
        
        /**
         * Returns the indicated WrapMode converted to a string word.
         */
        """
        pass

    def getAnisotropicDegree(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_anisotropic_degree(SamplerState self)
        
        /**
         * Returns the degree of anisotropic filtering that should be applied to the
         * texture.  This value may return 0, indicating the default value; see also
         * get_effective_anisotropic_degree.
         */
        """
        pass

    def getBorderColor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_border_color(SamplerState self)
        
        /**
         * Returns the solid color of the texture's border.  Some OpenGL
         * implementations use a border for tiling textures; in Panda, it is only used
         * for specifying the clamp color.
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getDefault(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_default()
        
        /**
         * Returns a reference to the global default immutable SamplerState object.
         */
        """
        pass

    def getEffectiveAnisotropicDegree(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_effective_anisotropic_degree(SamplerState self)
        
        /**
         * Returns the degree of anisotropic filtering that should be applied to the
         * texture.  This value will normally not return 0, unless there is an error
         * in the config file.
         */
        """
        pass

    def getEffectiveMagfilter(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_effective_magfilter(SamplerState self)
        
        /**
         * Returns the filter mode of the texture for magnification, with special
         * treatment for FT_default.  This will normally not return FT_default, unless
         * there is an error in the config file.
         */
        """
        pass

    def getEffectiveMinfilter(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_effective_minfilter(SamplerState self)
        
        /**
         * Returns the filter mode of the texture for minification, with special
         * treatment for FT_default.  This will normally not return FT_default, unless
         * there is an error in the config file.
         */
        """
        pass

    def getLodBias(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_lod_bias(SamplerState self)
        
        /**
         * Returns the bias that will be added to the texture level of detail when
         * sampling this texture.
         */
        """
        pass

    def getMagfilter(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_magfilter(SamplerState self)
        
        /**
         * Returns the filter mode of the texture for magnification.  The mipmap
         * constants are invalid here.  This may return FT_default; see also
         * get_effective_minfilter().
         */
        """
        pass

    def getMaxLod(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_max_lod(SamplerState self)
        
        /**
         * Returns the maximum level of detail that will be observed when sampling
         * this texture.
         */
        """
        pass

    def getMinfilter(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_minfilter(SamplerState self)
        
        /**
         * Returns the filter mode of the texture for minification.  If this is one of
         * the mipmap constants, then the texture requires mipmaps.  This may return
         * FT_default; see also get_effective_minfilter().
         */
        """
        pass

    def getMinLod(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_min_lod(SamplerState self)
        
        /**
         * Returns the minimum level of detail that will be observed when sampling
         * this texture.
         */
        """
        pass

    def getWrapU(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_wrap_u(SamplerState self)
        
        /**
         * Returns the wrap mode of the texture in the U direction.
         */
        """
        pass

    def getWrapV(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_wrap_v(SamplerState self)
        
        /**
         * Returns the wrap mode of the texture in the V direction.
         */
        """
        pass

    def getWrapW(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_wrap_w(SamplerState self)
        
        /**
         * Returns the wrap mode of the texture in the W direction.  This is the depth
         * direction of 3-d textures.
         */
        """
        pass

    def get_anisotropic_degree(self, SamplerState_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_anisotropic_degree(SamplerState self)
        
        /**
         * Returns the degree of anisotropic filtering that should be applied to the
         * texture.  This value may return 0, indicating the default value; see also
         * get_effective_anisotropic_degree.
         */
        """
        pass

    def get_border_color(self, SamplerState_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_border_color(SamplerState self)
        
        /**
         * Returns the solid color of the texture's border.  Some OpenGL
         * implementations use a border for tiling textures; in Panda, it is only used
         * for specifying the clamp color.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_default(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_default()
        
        /**
         * Returns a reference to the global default immutable SamplerState object.
         */
        """
        pass

    def get_effective_anisotropic_degree(self, SamplerState_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_effective_anisotropic_degree(SamplerState self)
        
        /**
         * Returns the degree of anisotropic filtering that should be applied to the
         * texture.  This value will normally not return 0, unless there is an error
         * in the config file.
         */
        """
        pass

    def get_effective_magfilter(self, SamplerState_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_effective_magfilter(SamplerState self)
        
        /**
         * Returns the filter mode of the texture for magnification, with special
         * treatment for FT_default.  This will normally not return FT_default, unless
         * there is an error in the config file.
         */
        """
        pass

    def get_effective_minfilter(self, SamplerState_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_effective_minfilter(SamplerState self)
        
        /**
         * Returns the filter mode of the texture for minification, with special
         * treatment for FT_default.  This will normally not return FT_default, unless
         * there is an error in the config file.
         */
        """
        pass

    def get_lod_bias(self, SamplerState_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_lod_bias(SamplerState self)
        
        /**
         * Returns the bias that will be added to the texture level of detail when
         * sampling this texture.
         */
        """
        pass

    def get_magfilter(self, SamplerState_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_magfilter(SamplerState self)
        
        /**
         * Returns the filter mode of the texture for magnification.  The mipmap
         * constants are invalid here.  This may return FT_default; see also
         * get_effective_minfilter().
         */
        """
        pass

    def get_max_lod(self, SamplerState_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_max_lod(SamplerState self)
        
        /**
         * Returns the maximum level of detail that will be observed when sampling
         * this texture.
         */
        """
        pass

    def get_minfilter(self, SamplerState_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_minfilter(SamplerState self)
        
        /**
         * Returns the filter mode of the texture for minification.  If this is one of
         * the mipmap constants, then the texture requires mipmaps.  This may return
         * FT_default; see also get_effective_minfilter().
         */
        """
        pass

    def get_min_lod(self, SamplerState_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_min_lod(SamplerState self)
        
        /**
         * Returns the minimum level of detail that will be observed when sampling
         * this texture.
         */
        """
        pass

    def get_wrap_u(self, SamplerState_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_wrap_u(SamplerState self)
        
        /**
         * Returns the wrap mode of the texture in the U direction.
         */
        """
        pass

    def get_wrap_v(self, SamplerState_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_wrap_v(SamplerState self)
        
        /**
         * Returns the wrap mode of the texture in the V direction.
         */
        """
        pass

    def get_wrap_w(self, SamplerState_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_wrap_w(SamplerState self)
        
        /**
         * Returns the wrap mode of the texture in the W direction.  This is the depth
         * direction of 3-d textures.
         */
        """
        pass

    def isMipmap(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_mipmap(int type)
        
        /**
         * Returns true if the indicated filter type requires the use of mipmaps, or
         * false if it does not.
         */
        """
        pass

    def isPrepared(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_prepared(SamplerState self, PreparedGraphicsObjects prepared_objects)
        
        /**
         * Returns true if the sampler has already been prepared or enqueued for
         * preparation on the indicated GSG, false otherwise.
         */
        """
        pass

    def is_mipmap(self, int_type): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_mipmap(int type)
        
        /**
         * Returns true if the indicated filter type requires the use of mipmaps, or
         * false if it does not.
         */
        """
        pass

    def is_prepared(self, SamplerState_self, PreparedGraphicsObjects_prepared_objects): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_prepared(SamplerState self, PreparedGraphicsObjects prepared_objects)
        
        /**
         * Returns true if the sampler has already been prepared or enqueued for
         * preparation on the indicated GSG, false otherwise.
         */
        """
        pass

    def prepare(self, SamplerState_self, PreparedGraphicsObjects_prepared_objects): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        prepare(SamplerState self, PreparedGraphicsObjects prepared_objects)
        
        /**
         * Indicates that the sampler should be enqueued to be prepared in the
         * indicated prepared_objects at the beginning of the next frame.
         *
         * Use this function instead of prepare_now() to preload samplers from a user
         * interface standpoint.
         */
        """
        pass

    def release(self, SamplerState_self, PreparedGraphicsObjects_prepared_objects): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        release(SamplerState self, PreparedGraphicsObjects prepared_objects)
        
        /**
         * Frees the texture context only on the indicated object, if it exists there.
         * Returns true if it was released, false if it had not been prepared.
         */
        """
        pass

    def setAnisotropicDegree(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_anisotropic_degree(const SamplerState self, int anisotropic_degree)
        
        /**
         * Specifies the level of anisotropic filtering to apply to the SamplerState.
         * Set this 0 to indicate the default value, which is specified in the
         * SamplerState-anisotropic-degree config variable.
         *
         * To explicitly disable anisotropic filtering, set this value to 1.  To
         * explicitly enable anisotropic filtering, set it to a value higher than 1;
         * larger numbers indicate greater degrees of filtering.
         */
        """
        pass

    def setBorderColor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_border_color(const SamplerState self, const LVecBase4f color)
        
        /**
         * Specifies the solid color of the SamplerState's border.  Some OpenGL
         * implementations use a border for tiling SamplerStates; in Panda, it is only
         * used for specifying the clamp color.
         */
        """
        pass

    def setLodBias(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_lod_bias(const SamplerState self, float lod_bias)
        
        /**
         * Sets the value that will be added to the level of detail when sampling the
         * texture.  This may be a negative value, although some graphics hardware may
         * not support the use of negative LOD values.
         */
        """
        pass

    def setMagfilter(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_magfilter(const SamplerState self, int filter)
        
        /**
         * Sets the filtering method that should be used when viewing the SamplerState
         * up close.
         */
        """
        pass

    def setMaxLod(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_max_lod(const SamplerState self, float max_lod)
        
        /**
         * Sets the maximum level of detail that will be used when sampling this
         * texture.  This may exceed the number of mipmap levels that the texture has.
         */
        """
        pass

    def setMinfilter(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_minfilter(const SamplerState self, int filter)
        
        /**
         * Sets the filtering method that should be used when viewing the SamplerState
         * from a distance.
         */
        """
        pass

    def setMinLod(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_min_lod(const SamplerState self, float min_lod)
        
        /**
         * Sets the minimum level of detail that will be used when sampling this
         * texture.  This may be a negative value.
         */
        """
        pass

    def setWrapU(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_wrap_u(const SamplerState self, int wrap)
        
        /**
         * This setting determines what happens when the SamplerState is sampled with
         * a U value outside the range 0.0-1.0.  The default is WM_repeat, which
         * indicates that the SamplerState should repeat indefinitely.
         */
        """
        pass

    def setWrapV(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_wrap_v(const SamplerState self, int wrap)
        
        /**
         * This setting determines what happens when the SamplerState is sampled with
         * a V value outside the range 0.0-1.0.  The default is WM_repeat, which
         * indicates that the SamplerState should repeat indefinitely.
         */
        """
        pass

    def setWrapW(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_wrap_w(const SamplerState self, int wrap)
        
        /**
         * The W wrap direction is only used for 3-d SamplerStates.
         */
        """
        pass

    def set_anisotropic_degree(self, const_SamplerState_self, int_anisotropic_degree): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_anisotropic_degree(const SamplerState self, int anisotropic_degree)
        
        /**
         * Specifies the level of anisotropic filtering to apply to the SamplerState.
         * Set this 0 to indicate the default value, which is specified in the
         * SamplerState-anisotropic-degree config variable.
         *
         * To explicitly disable anisotropic filtering, set this value to 1.  To
         * explicitly enable anisotropic filtering, set it to a value higher than 1;
         * larger numbers indicate greater degrees of filtering.
         */
        """
        pass

    def set_border_color(self, const_SamplerState_self, const_LVecBase4f_color): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_border_color(const SamplerState self, const LVecBase4f color)
        
        /**
         * Specifies the solid color of the SamplerState's border.  Some OpenGL
         * implementations use a border for tiling SamplerStates; in Panda, it is only
         * used for specifying the clamp color.
         */
        """
        pass

    def set_lod_bias(self, const_SamplerState_self, float_lod_bias): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_lod_bias(const SamplerState self, float lod_bias)
        
        /**
         * Sets the value that will be added to the level of detail when sampling the
         * texture.  This may be a negative value, although some graphics hardware may
         * not support the use of negative LOD values.
         */
        """
        pass

    def set_magfilter(self, const_SamplerState_self, int_filter): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_magfilter(const SamplerState self, int filter)
        
        /**
         * Sets the filtering method that should be used when viewing the SamplerState
         * up close.
         */
        """
        pass

    def set_max_lod(self, const_SamplerState_self, float_max_lod): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_max_lod(const SamplerState self, float max_lod)
        
        /**
         * Sets the maximum level of detail that will be used when sampling this
         * texture.  This may exceed the number of mipmap levels that the texture has.
         */
        """
        pass

    def set_minfilter(self, const_SamplerState_self, int_filter): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_minfilter(const SamplerState self, int filter)
        
        /**
         * Sets the filtering method that should be used when viewing the SamplerState
         * from a distance.
         */
        """
        pass

    def set_min_lod(self, const_SamplerState_self, float_min_lod): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_min_lod(const SamplerState self, float min_lod)
        
        /**
         * Sets the minimum level of detail that will be used when sampling this
         * texture.  This may be a negative value.
         */
        """
        pass

    def set_wrap_u(self, const_SamplerState_self, int_wrap): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_wrap_u(const SamplerState self, int wrap)
        
        /**
         * This setting determines what happens when the SamplerState is sampled with
         * a U value outside the range 0.0-1.0.  The default is WM_repeat, which
         * indicates that the SamplerState should repeat indefinitely.
         */
        """
        pass

    def set_wrap_v(self, const_SamplerState_self, int_wrap): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_wrap_v(const SamplerState self, int wrap)
        
        /**
         * This setting determines what happens when the SamplerState is sampled with
         * a V value outside the range 0.0-1.0.  The default is WM_repeat, which
         * indicates that the SamplerState should repeat indefinitely.
         */
        """
        pass

    def set_wrap_w(self, const_SamplerState_self, int_wrap): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_wrap_w(const SamplerState self, int wrap)
        
        /**
         * The W wrap direction is only used for 3-d SamplerStates.
         */
        """
        pass

    def stringFilterType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        string_filter_type(str str)
        
        /**
         * Returns the FilterType value associated with the given string
         * representation, or FT_invalid if the string does not match any known
         * FilterType value.
         */
        """
        pass

    def stringWrapMode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        string_wrap_mode(str str)
        
        /**
         * Returns the WrapMode value associated with the given string representation,
         * or WM_invalid if the string does not match any known WrapMode value.
         */
        """
        pass

    def string_filter_type(self, str_str): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        string_filter_type(str str)
        
        /**
         * Returns the FilterType value associated with the given string
         * representation, or FT_invalid if the string does not match any known
         * FilterType value.
         */
        """
        pass

    def string_wrap_mode(self, str_str): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        string_wrap_mode(str str)
        
        /**
         * Returns the WrapMode value associated with the given string representation,
         * or WM_invalid if the string does not match any known WrapMode value.
         */
        """
        pass

    def usesMipmaps(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        uses_mipmaps(SamplerState self)
        
        /**
         * Returns true if the minfilter settings on this sampler indicate the use of
         * mipmapping, false otherwise.
         */
        """
        pass

    def uses_mipmaps(self, SamplerState_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        uses_mipmaps(SamplerState self)
        
        /**
         * Returns true if the minfilter settings on this sampler indicate the use of
         * mipmapping, false otherwise.
         */
        """
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __deepcopy__(self, *args, **kwargs): # real signature unknown
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    anisotropic_degree = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    border_color = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    effective_anisotropic_degree = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    effective_magfilter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    effective_minfilter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    lod_bias = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    magfilter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    max_lod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    minfilter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    min_lod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    wrap_u = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    wrap_v = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    wrap_w = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        'FTDefault': 7,
        'FTInvalid': 8,
        'FTLinear': 1,
        'FTLinearMipmapLinear': 5,
        'FTLinearMipmapNearest': 3,
        'FTNearest': 0,
        'FTNearestMipmapLinear': 4,
        'FTNearestMipmapNearest': 2,
        'FTShadow': 6,
        'FT_default': 7,
        'FT_invalid': 8,
        'FT_linear': 1,
        'FT_linear_mipmap_linear': 5,
        'FT_linear_mipmap_nearest': 3,
        'FT_nearest': 0,
        'FT_nearest_mipmap_linear': 4,
        'FT_nearest_mipmap_nearest': 2,
        'FT_shadow': 6,
        'WMBorderColor': 4,
        'WMClamp': 0,
        'WMInvalid': 5,
        'WMMirror': 2,
        'WMMirrorOnce': 3,
        'WMRepeat': 1,
        'WM_border_color': 4,
        'WM_clamp': 0,
        'WM_invalid': 5,
        'WM_mirror': 2,
        'WM_mirror_once': 3,
        'WM_repeat': 1,
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.SamplerState' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.SamplerState' objects>"
        '__doc__': '/**\n * Represents a set of settings that indicate how a texture is sampled.  This\n * can be used to sample the same texture using different settings in\n * different places.\n */',
        '__eq__': None, # (!) real value is "<slot wrapper '__eq__' of 'panda3d.core.SamplerState' objects>"
        '__ge__': None, # (!) real value is "<slot wrapper '__ge__' of 'panda3d.core.SamplerState' objects>"
        '__gt__': None, # (!) real value is "<slot wrapper '__gt__' of 'panda3d.core.SamplerState' objects>"
        '__hash__': None, # (!) real value is "<slot wrapper '__hash__' of 'panda3d.core.SamplerState' objects>"
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.SamplerState' objects>"
        '__le__': None, # (!) real value is "<slot wrapper '__le__' of 'panda3d.core.SamplerState' objects>"
        '__lt__': None, # (!) real value is "<slot wrapper '__lt__' of 'panda3d.core.SamplerState' objects>"
        '__ne__': None, # (!) real value is "<slot wrapper '__ne__' of 'panda3d.core.SamplerState' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2FEB70>'
        'anisotropic_degree': None, # (!) real value is "<attribute 'anisotropic_degree' of 'panda3d.core.SamplerState' objects>"
        'border_color': None, # (!) real value is "<attribute 'border_color' of 'panda3d.core.SamplerState' objects>"
        'effective_anisotropic_degree': None, # (!) real value is "<attribute 'effective_anisotropic_degree' of 'panda3d.core.SamplerState' objects>"
        'effective_magfilter': None, # (!) real value is "<attribute 'effective_magfilter' of 'panda3d.core.SamplerState' objects>"
        'effective_minfilter': None, # (!) real value is "<attribute 'effective_minfilter' of 'panda3d.core.SamplerState' objects>"
        'formatFilterType': None, # (!) real value is '<staticmethod(<built-in method formatFilterType of type object at 0x00007FFCFE2FEB70>)>'
        'formatWrapMode': None, # (!) real value is '<staticmethod(<built-in method formatWrapMode of type object at 0x00007FFCFE2FEB70>)>'
        'format_filter_type': None, # (!) real value is '<staticmethod(<built-in method format_filter_type of type object at 0x00007FFCFE2FEB70>)>'
        'format_wrap_mode': None, # (!) real value is '<staticmethod(<built-in method format_wrap_mode of type object at 0x00007FFCFE2FEB70>)>'
        'getAnisotropicDegree': None, # (!) real value is "<method 'getAnisotropicDegree' of 'panda3d.core.SamplerState' objects>"
        'getBorderColor': None, # (!) real value is "<method 'getBorderColor' of 'panda3d.core.SamplerState' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2FEB70>)>'
        'getDefault': None, # (!) real value is '<staticmethod(<built-in method getDefault of type object at 0x00007FFCFE2FEB70>)>'
        'getEffectiveAnisotropicDegree': None, # (!) real value is "<method 'getEffectiveAnisotropicDegree' of 'panda3d.core.SamplerState' objects>"
        'getEffectiveMagfilter': None, # (!) real value is "<method 'getEffectiveMagfilter' of 'panda3d.core.SamplerState' objects>"
        'getEffectiveMinfilter': None, # (!) real value is "<method 'getEffectiveMinfilter' of 'panda3d.core.SamplerState' objects>"
        'getLodBias': None, # (!) real value is "<method 'getLodBias' of 'panda3d.core.SamplerState' objects>"
        'getMagfilter': None, # (!) real value is "<method 'getMagfilter' of 'panda3d.core.SamplerState' objects>"
        'getMaxLod': None, # (!) real value is "<method 'getMaxLod' of 'panda3d.core.SamplerState' objects>"
        'getMinLod': None, # (!) real value is "<method 'getMinLod' of 'panda3d.core.SamplerState' objects>"
        'getMinfilter': None, # (!) real value is "<method 'getMinfilter' of 'panda3d.core.SamplerState' objects>"
        'getWrapU': None, # (!) real value is "<method 'getWrapU' of 'panda3d.core.SamplerState' objects>"
        'getWrapV': None, # (!) real value is "<method 'getWrapV' of 'panda3d.core.SamplerState' objects>"
        'getWrapW': None, # (!) real value is "<method 'getWrapW' of 'panda3d.core.SamplerState' objects>"
        'get_anisotropic_degree': None, # (!) real value is "<method 'get_anisotropic_degree' of 'panda3d.core.SamplerState' objects>"
        'get_border_color': None, # (!) real value is "<method 'get_border_color' of 'panda3d.core.SamplerState' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2FEB70>)>'
        'get_default': None, # (!) real value is '<staticmethod(<built-in method get_default of type object at 0x00007FFCFE2FEB70>)>'
        'get_effective_anisotropic_degree': None, # (!) real value is "<method 'get_effective_anisotropic_degree' of 'panda3d.core.SamplerState' objects>"
        'get_effective_magfilter': None, # (!) real value is "<method 'get_effective_magfilter' of 'panda3d.core.SamplerState' objects>"
        'get_effective_minfilter': None, # (!) real value is "<method 'get_effective_minfilter' of 'panda3d.core.SamplerState' objects>"
        'get_lod_bias': None, # (!) real value is "<method 'get_lod_bias' of 'panda3d.core.SamplerState' objects>"
        'get_magfilter': None, # (!) real value is "<method 'get_magfilter' of 'panda3d.core.SamplerState' objects>"
        'get_max_lod': None, # (!) real value is "<method 'get_max_lod' of 'panda3d.core.SamplerState' objects>"
        'get_min_lod': None, # (!) real value is "<method 'get_min_lod' of 'panda3d.core.SamplerState' objects>"
        'get_minfilter': None, # (!) real value is "<method 'get_minfilter' of 'panda3d.core.SamplerState' objects>"
        'get_wrap_u': None, # (!) real value is "<method 'get_wrap_u' of 'panda3d.core.SamplerState' objects>"
        'get_wrap_v': None, # (!) real value is "<method 'get_wrap_v' of 'panda3d.core.SamplerState' objects>"
        'get_wrap_w': None, # (!) real value is "<method 'get_wrap_w' of 'panda3d.core.SamplerState' objects>"
        'isMipmap': None, # (!) real value is '<staticmethod(<built-in method isMipmap of type object at 0x00007FFCFE2FEB70>)>'
        'isPrepared': None, # (!) real value is "<method 'isPrepared' of 'panda3d.core.SamplerState' objects>"
        'is_mipmap': None, # (!) real value is '<staticmethod(<built-in method is_mipmap of type object at 0x00007FFCFE2FEB70>)>'
        'is_prepared': None, # (!) real value is "<method 'is_prepared' of 'panda3d.core.SamplerState' objects>"
        'lod_bias': None, # (!) real value is "<attribute 'lod_bias' of 'panda3d.core.SamplerState' objects>"
        'magfilter': None, # (!) real value is "<attribute 'magfilter' of 'panda3d.core.SamplerState' objects>"
        'max_lod': None, # (!) real value is "<attribute 'max_lod' of 'panda3d.core.SamplerState' objects>"
        'min_lod': None, # (!) real value is "<attribute 'min_lod' of 'panda3d.core.SamplerState' objects>"
        'minfilter': None, # (!) real value is "<attribute 'minfilter' of 'panda3d.core.SamplerState' objects>"
        'prepare': None, # (!) real value is "<method 'prepare' of 'panda3d.core.SamplerState' objects>"
        'release': None, # (!) real value is "<method 'release' of 'panda3d.core.SamplerState' objects>"
        'setAnisotropicDegree': None, # (!) real value is "<method 'setAnisotropicDegree' of 'panda3d.core.SamplerState' objects>"
        'setBorderColor': None, # (!) real value is "<method 'setBorderColor' of 'panda3d.core.SamplerState' objects>"
        'setLodBias': None, # (!) real value is "<method 'setLodBias' of 'panda3d.core.SamplerState' objects>"
        'setMagfilter': None, # (!) real value is "<method 'setMagfilter' of 'panda3d.core.SamplerState' objects>"
        'setMaxLod': None, # (!) real value is "<method 'setMaxLod' of 'panda3d.core.SamplerState' objects>"
        'setMinLod': None, # (!) real value is "<method 'setMinLod' of 'panda3d.core.SamplerState' objects>"
        'setMinfilter': None, # (!) real value is "<method 'setMinfilter' of 'panda3d.core.SamplerState' objects>"
        'setWrapU': None, # (!) real value is "<method 'setWrapU' of 'panda3d.core.SamplerState' objects>"
        'setWrapV': None, # (!) real value is "<method 'setWrapV' of 'panda3d.core.SamplerState' objects>"
        'setWrapW': None, # (!) real value is "<method 'setWrapW' of 'panda3d.core.SamplerState' objects>"
        'set_anisotropic_degree': None, # (!) real value is "<method 'set_anisotropic_degree' of 'panda3d.core.SamplerState' objects>"
        'set_border_color': None, # (!) real value is "<method 'set_border_color' of 'panda3d.core.SamplerState' objects>"
        'set_lod_bias': None, # (!) real value is "<method 'set_lod_bias' of 'panda3d.core.SamplerState' objects>"
        'set_magfilter': None, # (!) real value is "<method 'set_magfilter' of 'panda3d.core.SamplerState' objects>"
        'set_max_lod': None, # (!) real value is "<method 'set_max_lod' of 'panda3d.core.SamplerState' objects>"
        'set_min_lod': None, # (!) real value is "<method 'set_min_lod' of 'panda3d.core.SamplerState' objects>"
        'set_minfilter': None, # (!) real value is "<method 'set_minfilter' of 'panda3d.core.SamplerState' objects>"
        'set_wrap_u': None, # (!) real value is "<method 'set_wrap_u' of 'panda3d.core.SamplerState' objects>"
        'set_wrap_v': None, # (!) real value is "<method 'set_wrap_v' of 'panda3d.core.SamplerState' objects>"
        'set_wrap_w': None, # (!) real value is "<method 'set_wrap_w' of 'panda3d.core.SamplerState' objects>"
        'stringFilterType': None, # (!) real value is '<staticmethod(<built-in method stringFilterType of type object at 0x00007FFCFE2FEB70>)>'
        'stringWrapMode': None, # (!) real value is '<staticmethod(<built-in method stringWrapMode of type object at 0x00007FFCFE2FEB70>)>'
        'string_filter_type': None, # (!) real value is '<staticmethod(<built-in method string_filter_type of type object at 0x00007FFCFE2FEB70>)>'
        'string_wrap_mode': None, # (!) real value is '<staticmethod(<built-in method string_wrap_mode of type object at 0x00007FFCFE2FEB70>)>'
        'usesMipmaps': None, # (!) real value is "<method 'usesMipmaps' of 'panda3d.core.SamplerState' objects>"
        'uses_mipmaps': None, # (!) real value is "<method 'uses_mipmaps' of 'panda3d.core.SamplerState' objects>"
        'wrap_u': None, # (!) real value is "<attribute 'wrap_u' of 'panda3d.core.SamplerState' objects>"
        'wrap_v': None, # (!) real value is "<attribute 'wrap_v' of 'panda3d.core.SamplerState' objects>"
        'wrap_w': None, # (!) real value is "<attribute 'wrap_w' of 'panda3d.core.SamplerState' objects>"
    }
    FTDefault = 7
    FTInvalid = 8
    FTLinear = 1
    FTLinearMipmapLinear = 5
    FTLinearMipmapNearest = 3
    FTNearest = 0
    FTNearestMipmapLinear = 4
    FTNearestMipmapNearest = 2
    FTShadow = 6
    FT_default = 7
    FT_invalid = 8
    FT_linear = 1
    FT_linear_mipmap_linear = 5
    FT_linear_mipmap_nearest = 3
    FT_nearest = 0
    FT_nearest_mipmap_linear = 4
    FT_nearest_mipmap_nearest = 2
    FT_shadow = 6
    WMBorderColor = 4
    WMClamp = 0
    WMInvalid = 5
    WMMirror = 2
    WMMirrorOnce = 3
    WMRepeat = 1
    WM_border_color = 4
    WM_clamp = 0
    WM_invalid = 5
    WM_mirror = 2
    WM_mirror_once = 3
    WM_repeat = 1


