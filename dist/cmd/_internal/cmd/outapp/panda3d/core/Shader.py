# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .TypedWritableReferenceCount import TypedWritableReferenceCount

class Shader(TypedWritableReferenceCount):
    """
    /**
    
     */
    """
    def getCacheCompiledShader(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_cache_compiled_shader(Shader self)
        
        /**
         * Returns the setting of the cache_compiled_shader flag.  See
         * set_cache_compiled_shader().
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getErrorFlag(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_error_flag(Shader self)
        
        /**
         * Returns true if the shader contains a compile-time error.  This doesn't
         * tell you whether or not the shader is supported on the current video card.
         */
        """
        pass

    def getFilename(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_filename(Shader self, int type)
        
        /**
         * Return the Shader's filename for the given shader type.
         */
        """
        pass

    def getFullpath(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_fullpath(Shader self)
        
        /**
         * Returns the fullpath that has been set.  This is the full path to the file
         * as it was found along the model-path.
         */
        """
        pass

    def getLanguage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_language(Shader self)
        
        /**
         * Returns the shader language in which this shader was written.
         */
        """
        pass

    def getText(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_text(Shader self, int type)
        
        /**
         * Return the Shader's text for the given shader type.
         */
        """
        pass

    def get_cache_compiled_shader(self, Shader_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_cache_compiled_shader(Shader self)
        
        /**
         * Returns the setting of the cache_compiled_shader flag.  See
         * set_cache_compiled_shader().
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_error_flag(self, Shader_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_error_flag(Shader self)
        
        /**
         * Returns true if the shader contains a compile-time error.  This doesn't
         * tell you whether or not the shader is supported on the current video card.
         */
        """
        pass

    def get_filename(self, Shader_self, int_type): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_filename(Shader self, int type)
        
        /**
         * Return the Shader's filename for the given shader type.
         */
        """
        pass

    def get_fullpath(self, Shader_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_fullpath(Shader self)
        
        /**
         * Returns the fullpath that has been set.  This is the full path to the file
         * as it was found along the model-path.
         */
        """
        pass

    def get_language(self, Shader_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_language(Shader self)
        
        /**
         * Returns the shader language in which this shader was written.
         */
        """
        pass

    def get_text(self, Shader_self, int_type): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_text(Shader self, int type)
        
        /**
         * Return the Shader's text for the given shader type.
         */
        """
        pass

    def hasFullpath(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_fullpath(Shader self)
        
        /**
         * Returns true if the fullpath has been set and is available.  See
         * set_fullpath().
         */
        """
        pass

    def has_fullpath(self, Shader_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_fullpath(Shader self)
        
        /**
         * Returns true if the fullpath has been set and is available.  See
         * set_fullpath().
         */
        """
        pass

    def isPrepared(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_prepared(Shader self, PreparedGraphicsObjects prepared_objects)
        
        /**
         * Returns true if the shader has already been prepared or enqueued for
         * preparation on the indicated GSG, false otherwise.
         */
        """
        pass

    def is_prepared(self, Shader_self, PreparedGraphicsObjects_prepared_objects): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_prepared(Shader self, PreparedGraphicsObjects prepared_objects)
        
        /**
         * Returns true if the shader has already been prepared or enqueued for
         * preparation on the indicated GSG, false otherwise.
         */
        """
        pass

    def load(self, const_Filename_file): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        load(const Filename file)
        load(const Filename file, int lang)
        load(int lang, const Filename vertex, const Filename fragment, const Filename geometry, const Filename tess_control, const Filename tess_evaluation)
        
        /**
         * Loads the shader from the given string(s). Returns a boolean indicating
         * success or failure.
         */
        
        /**
         * Loads the shader with the given filename.
         */
        
        /**
         * This variant of Shader::load loads all shader programs separately.
         */
        """
        pass

    def loadCompute(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        load_compute(int lang, const Filename fn)
        
        /**
         * Loads a compute shader.
         */
        """
        pass

    def load_compute(self, int_lang, const_Filename_fn): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        load_compute(int lang, const Filename fn)
        
        /**
         * Loads a compute shader.
         */
        """
        pass

    def make(self, str_body): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make(str body)
        make(str body, int lang)
        make(int lang, str vertex, str fragment, str geometry, str tess_control, str tess_evaluation)
        
        /**
         * Loads the shader, using the string as shader body.
         */
        
        /**
         * Loads the shader, using the strings as shader bodies.
         */
        """
        pass

    def makeCompute(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_compute(int lang, str body)
        
        /**
         * Loads the compute shader from the given string.
         */
        """
        pass

    def make_compute(self, int_lang, str_body): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_compute(int lang, str body)
        
        /**
         * Loads the compute shader from the given string.
         */
        """
        pass

    def prepare(self, const_Shader_self, PreparedGraphicsObjects_prepared_objects): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        prepare(const Shader self, PreparedGraphicsObjects prepared_objects)
        
        /**
         * Indicates that the shader should be enqueued to be prepared in the
         * indicated prepared_objects at the beginning of the next frame.  This will
         * ensure the texture is already loaded into texture memory if it is expected
         * to be rendered soon.
         *
         * Use this function instead of prepare_now() to preload textures from a user
         * interface standpoint.
         */
        """
        pass

    def prepareNow(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        prepare_now(const Shader self, PreparedGraphicsObjects prepared_objects, GraphicsStateGuardianBase gsg)
        
        /**
         * Creates a context for the shader on the particular GSG, if it does not
         * already exist.  Returns the new (or old) ShaderContext.  This assumes that
         * the GraphicsStateGuardian is the currently active rendering context and
         * that it is ready to accept new textures.  If this is not necessarily the
         * case, you should use prepare() instead.
         *
         * Normally, this is not called directly except by the GraphicsStateGuardian;
         * a shader does not need to be explicitly prepared by the user before it may
         * be rendered.
         */
        """
        pass

    def prepare_now(self, const_Shader_self, PreparedGraphicsObjects_prepared_objects, GraphicsStateGuardianBase_gsg): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        prepare_now(const Shader self, PreparedGraphicsObjects prepared_objects, GraphicsStateGuardianBase gsg)
        
        /**
         * Creates a context for the shader on the particular GSG, if it does not
         * already exist.  Returns the new (or old) ShaderContext.  This assumes that
         * the GraphicsStateGuardian is the currently active rendering context and
         * that it is ready to accept new textures.  If this is not necessarily the
         * case, you should use prepare() instead.
         *
         * Normally, this is not called directly except by the GraphicsStateGuardian;
         * a shader does not need to be explicitly prepared by the user before it may
         * be rendered.
         */
        """
        pass

    def release(self, const_Shader_self, PreparedGraphicsObjects_prepared_objects): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        release(const Shader self, PreparedGraphicsObjects prepared_objects)
        
        /**
         * Frees the texture context only on the indicated object, if it exists there.
         * Returns true if it was released, false if it had not been prepared.
         */
        """
        pass

    def releaseAll(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        release_all(const Shader self)
        
        /**
         * Frees the context allocated on all objects for which the texture has been
         * declared.  Returns the number of contexts which have been freed.
         */
        """
        pass

    def release_all(self, const_Shader_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        release_all(const Shader self)
        
        /**
         * Frees the context allocated on all objects for which the texture has been
         * declared.  Returns the number of contexts which have been freed.
         */
        """
        pass

    def setCacheCompiledShader(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_cache_compiled_shader(const Shader self, bool flag)
        
        /**
         * Sets the cache_compiled_shader flag.  When this is set, the next time the
         * Shader is loaded on a GSG, it will automatically extract the compiled
         * shader from the GSG and save it to the global BamCache.
         *
         * This is used to store compiled shaders in the BamCache.  This flag should
         * not be set explicitly; it is set automatically by the ShaderPool when
         * model-cache-compiled-shaders is set true.
         */
        """
        pass

    def setFilename(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_filename(const Shader self, int type, const Filename filename)
        
        /**
         * Sets the Shader's filename for the given shader type.  Useful for
         * associating a shader created with Shader.make with a name for diagnostics.
         */
        """
        pass

    def set_cache_compiled_shader(self, const_Shader_self, bool_flag): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_cache_compiled_shader(const Shader self, bool flag)
        
        /**
         * Sets the cache_compiled_shader flag.  When this is set, the next time the
         * Shader is loaded on a GSG, it will automatically extract the compiled
         * shader from the GSG and save it to the global BamCache.
         *
         * This is used to store compiled shaders in the BamCache.  This flag should
         * not be set explicitly; it is set automatically by the ShaderPool when
         * model-cache-compiled-shaders is set true.
         */
        """
        pass

    def set_filename(self, const_Shader_self, int_type, const_Filename_filename): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_filename(const Shader self, int type, const Filename filename)
        
        /**
         * Sets the Shader's filename for the given shader type.  Useful for
         * associating a shader created with Shader.make with a name for diagnostics.
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

    ASGloss = 4
    ASGlow = 2
    ASNormal = 1
    ASRamp = 8
    ASShadow = 16
    AS_gloss = 4
    AS_glow = 2
    AS_normal = 1
    AS_ramp = 8
    AS_shadow = 16
    BitAutoShaderGloss = 2
    BitAutoShaderGlow = 1
    BitAutoShaderNormal = 0
    BitAutoShaderRamp = 3
    BitAutoShaderShadow = 4
    bit_AutoShaderGloss = 2
    bit_AutoShaderGlow = 1
    bit_AutoShaderNormal = 0
    bit_AutoShaderRamp = 3
    bit_AutoShaderShadow = 4
    DtoolClassDict = {
        'ASGloss': 4,
        'ASGlow': 2,
        'ASNormal': 1,
        'ASRamp': 8,
        'ASShadow': 16,
        'AS_gloss': 4,
        'AS_glow': 2,
        'AS_normal': 1,
        'AS_ramp': 8,
        'AS_shadow': 16,
        'BitAutoShaderGloss': 2,
        'BitAutoShaderGlow': 1,
        'BitAutoShaderNormal': 0,
        'BitAutoShaderRamp': 3,
        'BitAutoShaderShadow': 4,
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        'SLCg': 1,
        'SLGLSL': 2,
        'SLHLSL': 3,
        'SLNone': 0,
        'SLSPIRV': 4,
        'SL_Cg': 1,
        'SL_GLSL': 2,
        'SL_HLSL': 3,
        'SL_SPIR_V': 4,
        'SL_none': 0,
        'STCOUNT': 7,
        'STCompute': 6,
        'STFragment': 2,
        'STGeometry': 3,
        'STNone': 0,
        'STTessControl': 4,
        'STTessEvaluation': 5,
        'STVertex': 1,
        'ST_COUNT': 7,
        'ST_compute': 6,
        'ST_fragment': 2,
        'ST_geometry': 3,
        'ST_none': 0,
        'ST_tess_control': 4,
        'ST_tess_evaluation': 5,
        'ST_vertex': 1,
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.Shader' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.Shader' objects>"
        '__doc__': '/**\n\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.Shader' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2FEF10>'
        'bit_AutoShaderGloss': 2,
        'bit_AutoShaderGlow': 1,
        'bit_AutoShaderNormal': 0,
        'bit_AutoShaderRamp': 3,
        'bit_AutoShaderShadow': 4,
        'getCacheCompiledShader': None, # (!) real value is "<method 'getCacheCompiledShader' of 'panda3d.core.Shader' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2FEF10>)>'
        'getErrorFlag': None, # (!) real value is "<method 'getErrorFlag' of 'panda3d.core.Shader' objects>"
        'getFilename': None, # (!) real value is "<method 'getFilename' of 'panda3d.core.Shader' objects>"
        'getFullpath': None, # (!) real value is "<method 'getFullpath' of 'panda3d.core.Shader' objects>"
        'getLanguage': None, # (!) real value is "<method 'getLanguage' of 'panda3d.core.Shader' objects>"
        'getText': None, # (!) real value is "<method 'getText' of 'panda3d.core.Shader' objects>"
        'get_cache_compiled_shader': None, # (!) real value is "<method 'get_cache_compiled_shader' of 'panda3d.core.Shader' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2FEF10>)>'
        'get_error_flag': None, # (!) real value is "<method 'get_error_flag' of 'panda3d.core.Shader' objects>"
        'get_filename': None, # (!) real value is "<method 'get_filename' of 'panda3d.core.Shader' objects>"
        'get_fullpath': None, # (!) real value is "<method 'get_fullpath' of 'panda3d.core.Shader' objects>"
        'get_language': None, # (!) real value is "<method 'get_language' of 'panda3d.core.Shader' objects>"
        'get_text': None, # (!) real value is "<method 'get_text' of 'panda3d.core.Shader' objects>"
        'hasFullpath': None, # (!) real value is "<method 'hasFullpath' of 'panda3d.core.Shader' objects>"
        'has_fullpath': None, # (!) real value is "<method 'has_fullpath' of 'panda3d.core.Shader' objects>"
        'isPrepared': None, # (!) real value is "<method 'isPrepared' of 'panda3d.core.Shader' objects>"
        'is_prepared': None, # (!) real value is "<method 'is_prepared' of 'panda3d.core.Shader' objects>"
        'load': None, # (!) real value is '<staticmethod(<built-in method load of type object at 0x00007FFCFE2FEF10>)>'
        'loadCompute': None, # (!) real value is '<staticmethod(<built-in method loadCompute of type object at 0x00007FFCFE2FEF10>)>'
        'load_compute': None, # (!) real value is '<staticmethod(<built-in method load_compute of type object at 0x00007FFCFE2FEF10>)>'
        'make': None, # (!) real value is '<staticmethod(<built-in method make of type object at 0x00007FFCFE2FEF10>)>'
        'makeCompute': None, # (!) real value is '<staticmethod(<built-in method makeCompute of type object at 0x00007FFCFE2FEF10>)>'
        'make_compute': None, # (!) real value is '<staticmethod(<built-in method make_compute of type object at 0x00007FFCFE2FEF10>)>'
        'prepare': None, # (!) real value is "<method 'prepare' of 'panda3d.core.Shader' objects>"
        'prepareNow': None, # (!) real value is "<method 'prepareNow' of 'panda3d.core.Shader' objects>"
        'prepare_now': None, # (!) real value is "<method 'prepare_now' of 'panda3d.core.Shader' objects>"
        'release': None, # (!) real value is "<method 'release' of 'panda3d.core.Shader' objects>"
        'releaseAll': None, # (!) real value is "<method 'releaseAll' of 'panda3d.core.Shader' objects>"
        'release_all': None, # (!) real value is "<method 'release_all' of 'panda3d.core.Shader' objects>"
        'setCacheCompiledShader': None, # (!) real value is "<method 'setCacheCompiledShader' of 'panda3d.core.Shader' objects>"
        'setFilename': None, # (!) real value is "<method 'setFilename' of 'panda3d.core.Shader' objects>"
        'set_cache_compiled_shader': None, # (!) real value is "<method 'set_cache_compiled_shader' of 'panda3d.core.Shader' objects>"
        'set_filename': None, # (!) real value is "<method 'set_filename' of 'panda3d.core.Shader' objects>"
    }
    SLCg = 1
    SLGLSL = 2
    SLHLSL = 3
    SLNone = 0
    SLSPIRV = 4
    SL_Cg = 1
    SL_GLSL = 2
    SL_HLSL = 3
    SL_none = 0
    SL_SPIR_V = 4
    STCompute = 6
    STCOUNT = 7
    STFragment = 2
    STGeometry = 3
    STNone = 0
    STTessControl = 4
    STTessEvaluation = 5
    STVertex = 1
    ST_compute = 6
    ST_COUNT = 7
    ST_fragment = 2
    ST_geometry = 3
    ST_none = 0
    ST_tess_control = 4
    ST_tess_evaluation = 5
    ST_vertex = 1


