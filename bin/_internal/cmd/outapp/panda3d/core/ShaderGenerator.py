# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .TypedReferenceCount import TypedReferenceCount

class ShaderGenerator(TypedReferenceCount):
    """
    /**
     * The ShaderGenerator is a device that effectively replaces the classic fixed
     * function pipeline with a 'next-gen' fixed function pipeline.  The next-gen
     * fixed function pipeline supports features like normal mapping, gloss
     * mapping, cartoon lighting, and so forth.  It works by automatically
     * generating a shader from a given RenderState.
     *
     * Currently, there is one ShaderGenerator object per GraphicsStateGuardian.
     * It is our intent that in time, people will write classes that derive from
     * ShaderGenerator but which yield slightly different results.
     *
     * The ShaderGenerator owes its existence to the 'Bamboo Team' at Carnegie
     * Mellon's Entertainment Technology Center.  This is a group of students who,
     * as a semester project, decided that next-gen graphics should be accessible
     * to everyone, even if they don't know shader programming.  The group
     * consisted of:
     *
     * Aaron Lo, Programmer Heegun Lee, Programmer Erin Fernandez, Artist/Tester
     * Joe Grubb, Artist/Tester Ivan Ortega, Technical Artist/Tester
     *
     * Thanks to them!
     *
     */
    """
    def clearGeneratedShaders(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_generated_shaders(const ShaderGenerator self)
        
        /**
         * Removes all previously generated shaders, requiring all shaders to be
         * regenerated.  Does not clear cache of compiled shaders.
         *
         * @since 1.10.0
         */
        """
        pass

    def clear_generated_shaders(self, const_ShaderGenerator_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_generated_shaders(const ShaderGenerator self)
        
        /**
         * Removes all previously generated shaders, requiring all shaders to be
         * regenerated.  Does not clear cache of compiled shaders.
         *
         * @since 1.10.0
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def rehashGeneratedShaders(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        rehash_generated_shaders(const ShaderGenerator self)
        
        /**
         * Rehashes all the states with generated shaders, removing the ones that are
         * no longer fresh.
         *
         * Call this if certain state has changed in such a way as to require a rerun
         * of the shader generator.  This should be rare because in most cases, the
         * shader generator will automatically regenerate shaders as necessary.
         *
         * @since 1.10.0
         */
        """
        pass

    def rehash_generated_shaders(self, const_ShaderGenerator_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        rehash_generated_shaders(const ShaderGenerator self)
        
        /**
         * Rehashes all the states with generated shaders, removing the ones that are
         * no longer fresh.
         *
         * Call this if certain state has changed in such a way as to require a rerun
         * of the shader generator.  This should be rare because in most cases, the
         * shader generator will automatically regenerate shaders as necessary.
         *
         * @since 1.10.0
         */
        """
        pass

    def synthesizeShader(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        synthesize_shader(const ShaderGenerator self, const RenderState rs, const GeomVertexAnimationSpec anim)
        
        /**
         * This is the routine that implements the next-gen fixed function pipeline by
         * synthesizing a shader.  It also takes care of setting up any buffers needed
         * to produce the requested effects.
         *
         * Currently supports:
         * - flat colors
         * - vertex colors
         * - lighting
         * - normal maps, even multiple
         * - gloss maps, but not multiple
         * - glow maps, but not multiple
         * - materials, but not updates to materials
         * - 2D textures
         * - all texture stage modes, including combine modes
         * - color scale attrib
         * - light ramps (for cartoon shading)
         * - shadow mapping
         * - most texgen modes
         * - texmatrix
         * - 1D/2D/3D textures, cube textures, 2D tex arrays
         * - linear/exp/exp2 fog
         * - animation
         *
         * Potential optimizations
         * - omit attenuation calculations if attenuation off
         *
         */
        """
        pass

    def synthesize_shader(self, const_ShaderGenerator_self, const_RenderState_rs, const_GeomVertexAnimationSpec_anim): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        synthesize_shader(const ShaderGenerator self, const RenderState rs, const GeomVertexAnimationSpec anim)
        
        /**
         * This is the routine that implements the next-gen fixed function pipeline by
         * synthesizing a shader.  It also takes care of setting up any buffers needed
         * to produce the requested effects.
         *
         * Currently supports:
         * - flat colors
         * - vertex colors
         * - lighting
         * - normal maps, even multiple
         * - gloss maps, but not multiple
         * - glow maps, but not multiple
         * - materials, but not updates to materials
         * - 2D textures
         * - all texture stage modes, including combine modes
         * - color scale attrib
         * - light ramps (for cartoon shading)
         * - shadow mapping
         * - most texgen modes
         * - texmatrix
         * - 1D/2D/3D textures, cube textures, 2D tex arrays
         * - linear/exp/exp2 fog
         * - animation
         *
         * Potential optimizations
         * - omit attenuation calculations if attenuation off
         *
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

    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.ShaderGenerator' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.ShaderGenerator' objects>"
        '__doc__': "/**\n * The ShaderGenerator is a device that effectively replaces the classic fixed\n * function pipeline with a 'next-gen' fixed function pipeline.  The next-gen\n * fixed function pipeline supports features like normal mapping, gloss\n * mapping, cartoon lighting, and so forth.  It works by automatically\n * generating a shader from a given RenderState.\n *\n * Currently, there is one ShaderGenerator object per GraphicsStateGuardian.\n * It is our intent that in time, people will write classes that derive from\n * ShaderGenerator but which yield slightly different results.\n *\n * The ShaderGenerator owes its existence to the 'Bamboo Team' at Carnegie\n * Mellon's Entertainment Technology Center.  This is a group of students who,\n * as a semester project, decided that next-gen graphics should be accessible\n * to everyone, even if they don't know shader programming.  The group\n * consisted of:\n *\n * Aaron Lo, Programmer Heegun Lee, Programmer Erin Fernandez, Artist/Tester\n * Joe Grubb, Artist/Tester Ivan Ortega, Technical Artist/Tester\n *\n * Thanks to them!\n *\n */",
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.ShaderGenerator' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE288580>'
        'clearGeneratedShaders': None, # (!) real value is "<method 'clearGeneratedShaders' of 'panda3d.core.ShaderGenerator' objects>"
        'clear_generated_shaders': None, # (!) real value is "<method 'clear_generated_shaders' of 'panda3d.core.ShaderGenerator' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE288580>)>'
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE288580>)>'
        'rehashGeneratedShaders': None, # (!) real value is "<method 'rehashGeneratedShaders' of 'panda3d.core.ShaderGenerator' objects>"
        'rehash_generated_shaders': None, # (!) real value is "<method 'rehash_generated_shaders' of 'panda3d.core.ShaderGenerator' objects>"
        'synthesizeShader': None, # (!) real value is "<method 'synthesizeShader' of 'panda3d.core.ShaderGenerator' objects>"
        'synthesize_shader': None, # (!) real value is "<method 'synthesize_shader' of 'panda3d.core.ShaderGenerator' objects>"
    }


