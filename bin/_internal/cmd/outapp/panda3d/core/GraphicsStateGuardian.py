# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .GraphicsStateGuardianBase import GraphicsStateGuardianBase

class GraphicsStateGuardian(GraphicsStateGuardianBase):
    """
    /**
     * Encapsulates all the communication with a particular instance of a given
     * rendering backend.  Tries to guarantee that redundant state-change requests
     * are not issued (hence "state guardian").
     *
     * There will be one of these objects for each different graphics context
     * active in the system.
     */
    """
    def beginScene(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        begin_scene(const GraphicsStateGuardian self)
        """
        pass

    def begin_scene(self, const_GraphicsStateGuardian_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        begin_scene(const GraphicsStateGuardian self)
        """
        pass

    def clearFlashTexture(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_flash_texture(const GraphicsStateGuardian self)
        """
        pass

    def clear_flash_texture(self, const_GraphicsStateGuardian_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_flash_texture(const GraphicsStateGuardian self)
        """
        pass

    def endScene(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        end_scene(const GraphicsStateGuardian self)
        """
        pass

    def end_scene(self, const_GraphicsStateGuardian_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        end_scene(const GraphicsStateGuardian self)
        """
        pass

    def getAlphaScaleTextureStage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_alpha_scale_texture_stage()
        
        /**
         * Returns the TextureStage that will be used to apply an alpha scale, if
         * get_alpha_scale_via_texture() returns true.
         */
        """
        pass

    def getAlphaScaleViaTexture(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_alpha_scale_via_texture(GraphicsStateGuardian self)
        get_alpha_scale_via_texture(GraphicsStateGuardian self, const TextureAttrib tex_attrib)
        
        /**
         * Returns true if this particular GSG can implement (or would prefer to
         * implement) an alpha scale via an additional Texture layer, or false if we
         * need to actually munge the alpha.
         */
        
        /**
         * This variant of get_alpha_scale_via_texture() answers the question of
         * whether the GSG can implement an alpha scale via an additional Texture
         * layer, considering the current TextureAttrib that will be in effect.  This
         * considers whether there is at least one additional texture slot available
         * on the GSG.
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getColorScaleViaLighting(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_color_scale_via_lighting(GraphicsStateGuardian self)
        
        /**
         * Returns true if this particular GSG can implement (or would prefer to
         * implement) set color and/or color scale using materials and/or ambient
         * lights, or false if we need to actually munge the color.
         */
        """
        pass

    def getCoordinateSystem(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_coordinate_system(GraphicsStateGuardian self)
        
        /**
         * Returns the coordinate system in effect on this particular gsg.  Normally,
         * this will be the default coordinate system, but it might be set differently
         * at runtime.
         */
        """
        pass

    def getCopyTextureInverted(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_copy_texture_inverted(GraphicsStateGuardian self)
        
        /**
         * Returns true if this particular GSG has the property that any framebuffer-
         * to-texture copy results in a texture that is upside-down and backwards from
         * Panda's usual convention; that is, it copies into a texture from the bottom
         * up instead of from the top down.
         *
         * If this is true, then on offscreen GraphicsBuffer created for the purposes
         * of rendering into a texture should be created with the invert flag set
         * true, to compensate.  Panda will do this automatically if you create an
         * offscreen buffer using GraphicsOutput::make_texture_buffer().
         */
        """
        pass

    def getDriverRenderer(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_driver_renderer(const GraphicsStateGuardian self)
        """
        pass

    def getDriverShaderVersionMajor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_driver_shader_version_major(const GraphicsStateGuardian self)
        """
        pass

    def getDriverShaderVersionMinor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_driver_shader_version_minor(const GraphicsStateGuardian self)
        """
        pass

    def getDriverVendor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_driver_vendor(const GraphicsStateGuardian self)
        """
        pass

    def getDriverVersion(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_driver_version(const GraphicsStateGuardian self)
        """
        pass

    def getDriverVersionMajor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_driver_version_major(const GraphicsStateGuardian self)
        """
        pass

    def getDriverVersionMinor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_driver_version_minor(const GraphicsStateGuardian self)
        """
        pass

    def getEngine(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_engine(GraphicsStateGuardian self)
        """
        pass

    def getFlashTexture(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_flash_texture(GraphicsStateGuardian self)
        """
        pass

    def getGamma(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_gamma(GraphicsStateGuardian self)
        """
        pass

    def getInternalCoordinateSystem(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_internal_coordinate_system(GraphicsStateGuardian self)
        """
        pass

    def getLoader(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_loader(GraphicsStateGuardian self)
        
        /**
         * Returns the Loader object that will be used by this GSG to load textures
         * when necessary, if get_incomplete_render() is true.
         */
        """
        pass

    def getMax2dTextureArrayLayers(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_max_2d_texture_array_layers(GraphicsStateGuardian self)
        
        //z axis
        
        //z axis
        
        /**
         * Returns the largest possible number of pages, or -1 if there is no
         * particular limit.  Returns 0 if 2-d texture arrays not supported.
         *
         * The value returned may not be meaningful until after the graphics context
         * has been fully created (e.g.  the window has been opened).
         */
        """
        pass

    def getMax3dTextureDimension(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_max_3d_texture_dimension(GraphicsStateGuardian self)
        
        /**
         * Returns the largest possible texture size in any one dimension for a 3-d
         * texture, or -1 if there is no particular limit.  Returns 0 if 3-d textures
         * are not supported.
         *
         * The value returned may not be meaningful until after the graphics context
         * has been fully created (e.g.  the window has been opened).
         */
        """
        pass

    def getMaxBufferTextureSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_max_buffer_texture_size(GraphicsStateGuardian self)
        
        /**
         * Returns the largest possible buffer texture size, or -1 if there is no
         * particular limit.  Returns 0 if cube map textures are not supported.
         *
         * The value returned may not be meaningful until after the graphics context
         * has been fully created (e.g.  the window has been opened).
         */
        """
        pass

    def getMaxClipPlanes(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_max_clip_planes(GraphicsStateGuardian self)
        
        /**
         * Returns the maximum number of simultaneous clip planes that may be applied
         * to geometry, or -1 if there is no particular limit.
         *
         * The value returned may not be meaningful until after the graphics context
         * has been fully created (e.g.  the window has been opened).
         */
        """
        pass

    def getMaxColorTargets(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_max_color_targets(GraphicsStateGuardian self)
        
        /**
         * Returns the maximum number of simultaneous color textures that may be
         * attached for render-to-texture, as supported by this particular GSG.  If
         * you exceed this number, the lowest-priority render targets will not be
         * applied.  Use RenderTarget::set_priority() to adjust the relative
         * importance of the different render targets.
         *
         * The value returned may not be meaningful until after the graphics context
         * has been fully created (e.g.  the window has been opened).
         */
        """
        pass

    def getMaxCubeMapDimension(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_max_cube_map_dimension(GraphicsStateGuardian self)
        
        //z axis
        
        //z axis
        
        /**
         * Returns the largest possible texture size in any one dimension for a cube
         * map texture, or -1 if there is no particular limit.  Returns 0 if cube map
         * textures are not supported.
         *
         * The value returned may not be meaningful until after the graphics context
         * has been fully created (e.g.  the window has been opened).
         */
        """
        pass

    def getMaximumSimultaneousRenderTargets(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_maximum_simultaneous_render_targets(GraphicsStateGuardian self)
        
        /**
         * Deprecated.  Use get_max_color_targets() instead, which returns the exact
         * same value.
         */
        """
        pass

    def getMaxLights(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_max_lights(GraphicsStateGuardian self)
        
        /**
         * Returns the maximum number of simultaneous lights that may be rendered on
         * geometry, or -1 if there is no particular limit.
         *
         * The value returned may not be meaningful until after the graphics context
         * has been fully created (e.g.  the window has been opened).
         */
        """
        pass

    def getMaxTextureStages(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_max_texture_stages(GraphicsStateGuardian self)
        
        /**
         * Returns the maximum number of simultaneous textures that may be applied to
         * geometry with multitexturing, as supported by this particular GSG.  If you
         * exceed this number, the lowest-priority texture stages will not be applied.
         * Use TextureStage::set_priority() to adjust the relative importance of the
         * different texture stages.
         *
         * The value returned may not be meaningful until after the graphics context
         * has been fully created (e.g.  the window has been opened).
         */
        """
        pass

    def getMaxVertexTransformIndices(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_max_vertex_transform_indices(GraphicsStateGuardian self)
        
        /**
         * Returns the maximum number of transforms there may be in a single
         * TransformTable for this graphics hardware.  If this number is 0 (but
         * get_max_transforms() is nonzero), then the graphics hardware (or API)
         * doesn't support indexed transforms, but can support direct transform
         * references.
         *
         * The value returned may not be meaningful until after the graphics context
         * has been fully created (e.g.  the window has been opened).
         */
        """
        pass

    def getMaxVertexTransforms(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_max_vertex_transforms(GraphicsStateGuardian self)
        
        /**
         * Returns the maximum number of transform matrices that may be simultaneously
         * used to transform any one vertex by the graphics hardware.  If this number
         * is 0, then the hardware (or the graphics backend) doesn't support soft-
         * skinned vertices (in which case Panda will animate the vertices in
         * software).
         *
         * The value returned may not be meaningful until after the graphics context
         * has been fully created (e.g.  the window has been opened).
         */
        """
        pass

    def getPipe(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_pipe(GraphicsStateGuardian self)
        
        /**
         * Returns the graphics pipe on which this GSG was created.
         */
        """
        pass

    def getPreparedObjects(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_prepared_objects(const GraphicsStateGuardian self)
        """
        pass

    def getPreparedTextures(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_prepared_textures(GraphicsStateGuardian self)
        """
        pass

    def getRuntimeColorScale(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_runtime_color_scale(GraphicsStateGuardian self)
        
        /**
         * Returns true if this particular GSG can implement (or would prefer to
         * implement) set color and/or color scale directly, without requiring any
         * munging of vertices or tricks with lighting.
         */
        """
        pass

    def getScene(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_scene(GraphicsStateGuardian self)
        """
        pass

    def getShaderGenerator(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_shader_generator(GraphicsStateGuardian self)
        
        /**
         * Returns the ShaderGenerator object that will be used by this GSG to
         * generate shaders when necessary.
         */
        """
        pass

    def getShaderModel(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_shader_model(GraphicsStateGuardian self)
        
        /**
         * Returns the ShaderModel
         */
        """
        pass

    def getSupports2dTextureArray(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_supports_2d_texture_array(GraphicsStateGuardian self)
        
        /**
         * Returns true if this GSG can render 2-d textures array.
         */
        """
        pass

    def getSupports3dTexture(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_supports_3d_texture(GraphicsStateGuardian self)
        
        /**
         * Returns true if this GSG can render 3-d (volumetric) textures.
         */
        """
        pass

    def getSupportsBasicShaders(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_supports_basic_shaders(GraphicsStateGuardian self)
        
        /**
         * Returns true if this particular GSG supports arbfp1+arbvp1 or above.
         */
        """
        pass

    def getSupportsBufferTexture(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_supports_buffer_texture(GraphicsStateGuardian self)
        
        /**
         * Returns true if this GSG can render buffer textures.
         */
        """
        pass

    def getSupportsCgProfile(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_supports_cg_profile(GraphicsStateGuardian self, str name)
        """
        pass

    def getSupportsCompressedTexture(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_supports_compressed_texture(GraphicsStateGuardian self)
        
        /**
         * Returns true if this GSG can compress textures as it loads them into
         * texture memory, and/or accept pre-compressed textures for storing.
         */
        """
        pass

    def getSupportsComputeShaders(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_supports_compute_shaders(GraphicsStateGuardian self)
        
        /**
         * Returns true if this particular GSG supports compute shaders.
         */
        """
        pass

    def getSupportsCubeMap(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_supports_cube_map(GraphicsStateGuardian self)
        
        /**
         * Returns true if this GSG can render cube map textures.
         */
        """
        pass

    def getSupportsCubeMapArray(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_supports_cube_map_array(GraphicsStateGuardian self)
        
        /**
         * Returns true if this GSG can render cube map arrays.
         */
        """
        pass

    def getSupportsDepthStencil(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_supports_depth_stencil(GraphicsStateGuardian self)
        
        /**
         * Returns true if this particular GSG supports textures whose format is
         * F_depth_stencil.  This only returns true if the GSG supports the full
         * packed depth-stencil functionality.
         */
        """
        pass

    def getSupportsDepthTexture(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_supports_depth_texture(GraphicsStateGuardian self)
        
        /**
         * Returns true if this particular GSG supports textures whose format is
         * F_depth_stencil.  This returns true if the GSG supports GL_DEPTH_COMPONENT
         * textures, which are considered a limited but still valid case of
         * F_depth_stencil.
         */
        """
        pass

    def getSupportsDualSourceBlending(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_supports_dual_source_blending(GraphicsStateGuardian self)
        
        /**
         * Returns true if dual source (incoming1_color and incoming1_alpha) blend
         * operands are supported by this GSG.
         */
        """
        pass

    def getSupportsGenerateMipmap(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_supports_generate_mipmap(GraphicsStateGuardian self)
        
        /**
         * Returns true if this particular GSG can generate mipmaps for a texture
         * automatically, or if they must be generated in software.  If this is true,
         * then mipmaps can safely be enabled for rendered textures (e.g.  using the
         * MultitexReducer).
         */
        """
        pass

    def getSupportsGeometryInstancing(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_supports_geometry_instancing(GraphicsStateGuardian self)
        
        /**
         * Returns true if this particular GSG supports hardware geometry instancing:
         * the ability to render multiple copies of a model.  In OpenGL, this is done
         * using the EXT_draw_instanced extension.
         */
        """
        pass

    def getSupportsGeometryShaders(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_supports_geometry_shaders(GraphicsStateGuardian self)
        
        /**
         * Returns true if this particular GSG supports geometry shaders.
         */
        """
        pass

    def getSupportsGlsl(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_supports_glsl(GraphicsStateGuardian self)
        
        /**
         * Returns true if this particular GSG supports GLSL shaders.
         */
        """
        pass

    def getSupportsIndirectDraw(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_supports_indirect_draw(GraphicsStateGuardian self)
        
        /**
         * Returns true if this particular GSG supports draw calls for which the
         * information comes from a buffer.
         */
        """
        pass

    def getSupportsLuminanceTexture(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_supports_luminance_texture(GraphicsStateGuardian self)
        
        /**
         * Returns true if this particular GSG supports luminance textures.
         */
        """
        pass

    def getSupportsOcclusionQuery(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_supports_occlusion_query(GraphicsStateGuardian self)
        
        /**
         * Returns true if this GSG supports an occlusion query.  If this is true,
         * then begin_occlusion_query() and end_occlusion_query() may be called to
         * bracket a sequence of draw_triangles() (or whatever) calls to measure
         * pixels that pass the depth test.
         */
        """
        pass

    def getSupportsSamplerObjects(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_supports_sampler_objects(GraphicsStateGuardian self)
        
        /**
         * Returns true if this particular GSG supports the use of sampler objects to
         * record texture sampling parameters separately from the texture objects.
         * This doesn't really affect functionality, but if this is false, it may mean
         * that using the same texture with different SamplerState objects will result
         * in reduced performance.
         */
        """
        pass

    def getSupportsStencil(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_supports_stencil(GraphicsStateGuardian self)
        
        /**
         * Returns true if this particular GSG supports stencil buffers at all.
         */
        """
        pass

    def getSupportsTessellationShaders(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_supports_tessellation_shaders(GraphicsStateGuardian self)
        
        /**
         * Returns true if this particular GSG supports tesselation shaders.
         */
        """
        pass

    def getSupportsTexNonPow2(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_supports_tex_non_pow2(GraphicsStateGuardian self)
        
        /**
         * Returns true if this GSG can handle non power of two sized textures.
         */
        """
        pass

    def getSupportsTextureCombine(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_supports_texture_combine(GraphicsStateGuardian self)
        
        /**
         * Returns true if this particular GSG can use the TextureStage::M_combine
         * mode, which includes all of the texture blend modes specified by
         * set_combine_rgb() and/or set_combine_alpha().  If this is false, you must
         * limit yourself to using the simpler blend modes.
         */
        """
        pass

    def getSupportsTextureDot3(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_supports_texture_dot3(GraphicsStateGuardian self)
        
        /**
         * Returns true if this GSG can use the TextureStage::CM_dot3_rgb or
         * CM_dot3_rgba combine modes.
         */
        """
        pass

    def getSupportsTextureSavedResult(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_supports_texture_saved_result(GraphicsStateGuardian self)
        
        /**
         * Returns true if this GSG can use the TextureStage::CS_last_saved_result
         * source, which allows you to save the result of a TextureStage and re-use it
         * for multiple inputs.
         */
        """
        pass

    def getSupportsTimerQuery(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_supports_timer_query(GraphicsStateGuardian self)
        
        /**
         * Returns true if this GSG supports a timer query.
         */
        """
        pass

    def getSupportsTwoSidedStencil(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_supports_two_sided_stencil(GraphicsStateGuardian self)
        
        /**
         * Returns true if this particular GSG supports two sided stencil: different
         * stencil settings for the front and back side of the same polygon.
         */
        """
        pass

    def getTextureQualityOverride(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_texture_quality_override(GraphicsStateGuardian self)
        
        /**
         * Returns the global quality_level override specified by
         * set_texture_quality_override.
         *
         * This is mainly useful for the tinydisplay software renderer.  See
         * Texture::set_quality_level().
         */
        """
        pass

    def getThreadingModel(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_threading_model(GraphicsStateGuardian self)
        
        /**
         * Returns the threading model that was used to create this GSG.
         */
        """
        pass

    def getTimerQueriesActive(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_timer_queries_active(GraphicsStateGuardian self)
        
        /**
         * Returns true if timer queries are currently enabled on this GSG.
         */
        """
        pass

    def get_alpha_scale_texture_stage(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_alpha_scale_texture_stage()
        
        /**
         * Returns the TextureStage that will be used to apply an alpha scale, if
         * get_alpha_scale_via_texture() returns true.
         */
        """
        pass

    def get_alpha_scale_via_texture(self, GraphicsStateGuardian_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_alpha_scale_via_texture(GraphicsStateGuardian self)
        get_alpha_scale_via_texture(GraphicsStateGuardian self, const TextureAttrib tex_attrib)
        
        /**
         * Returns true if this particular GSG can implement (or would prefer to
         * implement) an alpha scale via an additional Texture layer, or false if we
         * need to actually munge the alpha.
         */
        
        /**
         * This variant of get_alpha_scale_via_texture() answers the question of
         * whether the GSG can implement an alpha scale via an additional Texture
         * layer, considering the current TextureAttrib that will be in effect.  This
         * considers whether there is at least one additional texture slot available
         * on the GSG.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_color_scale_via_lighting(self, GraphicsStateGuardian_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_color_scale_via_lighting(GraphicsStateGuardian self)
        
        /**
         * Returns true if this particular GSG can implement (or would prefer to
         * implement) set color and/or color scale using materials and/or ambient
         * lights, or false if we need to actually munge the color.
         */
        """
        pass

    def get_coordinate_system(self, GraphicsStateGuardian_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_coordinate_system(GraphicsStateGuardian self)
        
        /**
         * Returns the coordinate system in effect on this particular gsg.  Normally,
         * this will be the default coordinate system, but it might be set differently
         * at runtime.
         */
        """
        pass

    def get_copy_texture_inverted(self, GraphicsStateGuardian_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_copy_texture_inverted(GraphicsStateGuardian self)
        
        /**
         * Returns true if this particular GSG has the property that any framebuffer-
         * to-texture copy results in a texture that is upside-down and backwards from
         * Panda's usual convention; that is, it copies into a texture from the bottom
         * up instead of from the top down.
         *
         * If this is true, then on offscreen GraphicsBuffer created for the purposes
         * of rendering into a texture should be created with the invert flag set
         * true, to compensate.  Panda will do this automatically if you create an
         * offscreen buffer using GraphicsOutput::make_texture_buffer().
         */
        """
        pass

    def get_driver_renderer(self, const_GraphicsStateGuardian_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_driver_renderer(const GraphicsStateGuardian self)
        """
        pass

    def get_driver_shader_version_major(self, const_GraphicsStateGuardian_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_driver_shader_version_major(const GraphicsStateGuardian self)
        """
        pass

    def get_driver_shader_version_minor(self, const_GraphicsStateGuardian_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_driver_shader_version_minor(const GraphicsStateGuardian self)
        """
        pass

    def get_driver_vendor(self, const_GraphicsStateGuardian_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_driver_vendor(const GraphicsStateGuardian self)
        """
        pass

    def get_driver_version(self, const_GraphicsStateGuardian_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_driver_version(const GraphicsStateGuardian self)
        """
        pass

    def get_driver_version_major(self, const_GraphicsStateGuardian_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_driver_version_major(const GraphicsStateGuardian self)
        """
        pass

    def get_driver_version_minor(self, const_GraphicsStateGuardian_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_driver_version_minor(const GraphicsStateGuardian self)
        """
        pass

    def get_engine(self, GraphicsStateGuardian_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_engine(GraphicsStateGuardian self)
        """
        pass

    def get_flash_texture(self, GraphicsStateGuardian_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_flash_texture(GraphicsStateGuardian self)
        """
        pass

    def get_gamma(self, GraphicsStateGuardian_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_gamma(GraphicsStateGuardian self)
        """
        pass

    def get_internal_coordinate_system(self, GraphicsStateGuardian_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_internal_coordinate_system(GraphicsStateGuardian self)
        """
        pass

    def get_loader(self, GraphicsStateGuardian_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_loader(GraphicsStateGuardian self)
        
        /**
         * Returns the Loader object that will be used by this GSG to load textures
         * when necessary, if get_incomplete_render() is true.
         */
        """
        pass

    def get_maximum_simultaneous_render_targets(self, GraphicsStateGuardian_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_maximum_simultaneous_render_targets(GraphicsStateGuardian self)
        
        /**
         * Deprecated.  Use get_max_color_targets() instead, which returns the exact
         * same value.
         */
        """
        pass

    def get_max_2d_texture_array_layers(self, GraphicsStateGuardian_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_max_2d_texture_array_layers(GraphicsStateGuardian self)
        
        //z axis
        
        //z axis
        
        /**
         * Returns the largest possible number of pages, or -1 if there is no
         * particular limit.  Returns 0 if 2-d texture arrays not supported.
         *
         * The value returned may not be meaningful until after the graphics context
         * has been fully created (e.g.  the window has been opened).
         */
        """
        pass

    def get_max_3d_texture_dimension(self, GraphicsStateGuardian_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_max_3d_texture_dimension(GraphicsStateGuardian self)
        
        /**
         * Returns the largest possible texture size in any one dimension for a 3-d
         * texture, or -1 if there is no particular limit.  Returns 0 if 3-d textures
         * are not supported.
         *
         * The value returned may not be meaningful until after the graphics context
         * has been fully created (e.g.  the window has been opened).
         */
        """
        pass

    def get_max_buffer_texture_size(self, GraphicsStateGuardian_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_max_buffer_texture_size(GraphicsStateGuardian self)
        
        /**
         * Returns the largest possible buffer texture size, or -1 if there is no
         * particular limit.  Returns 0 if cube map textures are not supported.
         *
         * The value returned may not be meaningful until after the graphics context
         * has been fully created (e.g.  the window has been opened).
         */
        """
        pass

    def get_max_clip_planes(self, GraphicsStateGuardian_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_max_clip_planes(GraphicsStateGuardian self)
        
        /**
         * Returns the maximum number of simultaneous clip planes that may be applied
         * to geometry, or -1 if there is no particular limit.
         *
         * The value returned may not be meaningful until after the graphics context
         * has been fully created (e.g.  the window has been opened).
         */
        """
        pass

    def get_max_color_targets(self, GraphicsStateGuardian_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_max_color_targets(GraphicsStateGuardian self)
        
        /**
         * Returns the maximum number of simultaneous color textures that may be
         * attached for render-to-texture, as supported by this particular GSG.  If
         * you exceed this number, the lowest-priority render targets will not be
         * applied.  Use RenderTarget::set_priority() to adjust the relative
         * importance of the different render targets.
         *
         * The value returned may not be meaningful until after the graphics context
         * has been fully created (e.g.  the window has been opened).
         */
        """
        pass

    def get_max_cube_map_dimension(self, GraphicsStateGuardian_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_max_cube_map_dimension(GraphicsStateGuardian self)
        
        //z axis
        
        //z axis
        
        /**
         * Returns the largest possible texture size in any one dimension for a cube
         * map texture, or -1 if there is no particular limit.  Returns 0 if cube map
         * textures are not supported.
         *
         * The value returned may not be meaningful until after the graphics context
         * has been fully created (e.g.  the window has been opened).
         */
        """
        pass

    def get_max_lights(self, GraphicsStateGuardian_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_max_lights(GraphicsStateGuardian self)
        
        /**
         * Returns the maximum number of simultaneous lights that may be rendered on
         * geometry, or -1 if there is no particular limit.
         *
         * The value returned may not be meaningful until after the graphics context
         * has been fully created (e.g.  the window has been opened).
         */
        """
        pass

    def get_max_texture_stages(self, GraphicsStateGuardian_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_max_texture_stages(GraphicsStateGuardian self)
        
        /**
         * Returns the maximum number of simultaneous textures that may be applied to
         * geometry with multitexturing, as supported by this particular GSG.  If you
         * exceed this number, the lowest-priority texture stages will not be applied.
         * Use TextureStage::set_priority() to adjust the relative importance of the
         * different texture stages.
         *
         * The value returned may not be meaningful until after the graphics context
         * has been fully created (e.g.  the window has been opened).
         */
        """
        pass

    def get_max_vertex_transforms(self, GraphicsStateGuardian_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_max_vertex_transforms(GraphicsStateGuardian self)
        
        /**
         * Returns the maximum number of transform matrices that may be simultaneously
         * used to transform any one vertex by the graphics hardware.  If this number
         * is 0, then the hardware (or the graphics backend) doesn't support soft-
         * skinned vertices (in which case Panda will animate the vertices in
         * software).
         *
         * The value returned may not be meaningful until after the graphics context
         * has been fully created (e.g.  the window has been opened).
         */
        """
        pass

    def get_max_vertex_transform_indices(self, GraphicsStateGuardian_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_max_vertex_transform_indices(GraphicsStateGuardian self)
        
        /**
         * Returns the maximum number of transforms there may be in a single
         * TransformTable for this graphics hardware.  If this number is 0 (but
         * get_max_transforms() is nonzero), then the graphics hardware (or API)
         * doesn't support indexed transforms, but can support direct transform
         * references.
         *
         * The value returned may not be meaningful until after the graphics context
         * has been fully created (e.g.  the window has been opened).
         */
        """
        pass

    def get_pipe(self, GraphicsStateGuardian_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_pipe(GraphicsStateGuardian self)
        
        /**
         * Returns the graphics pipe on which this GSG was created.
         */
        """
        pass

    def get_prepared_objects(self, const_GraphicsStateGuardian_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_prepared_objects(const GraphicsStateGuardian self)
        """
        pass

    def get_prepared_textures(self, GraphicsStateGuardian_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_prepared_textures(GraphicsStateGuardian self)
        """
        pass

    def get_runtime_color_scale(self, GraphicsStateGuardian_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_runtime_color_scale(GraphicsStateGuardian self)
        
        /**
         * Returns true if this particular GSG can implement (or would prefer to
         * implement) set color and/or color scale directly, without requiring any
         * munging of vertices or tricks with lighting.
         */
        """
        pass

    def get_scene(self, GraphicsStateGuardian_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_scene(GraphicsStateGuardian self)
        """
        pass

    def get_shader_generator(self, GraphicsStateGuardian_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_shader_generator(GraphicsStateGuardian self)
        
        /**
         * Returns the ShaderGenerator object that will be used by this GSG to
         * generate shaders when necessary.
         */
        """
        pass

    def get_shader_model(self, GraphicsStateGuardian_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_shader_model(GraphicsStateGuardian self)
        
        /**
         * Returns the ShaderModel
         */
        """
        pass

    def get_supports_2d_texture_array(self, GraphicsStateGuardian_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_supports_2d_texture_array(GraphicsStateGuardian self)
        
        /**
         * Returns true if this GSG can render 2-d textures array.
         */
        """
        pass

    def get_supports_3d_texture(self, GraphicsStateGuardian_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_supports_3d_texture(GraphicsStateGuardian self)
        
        /**
         * Returns true if this GSG can render 3-d (volumetric) textures.
         */
        """
        pass

    def get_supports_basic_shaders(self, GraphicsStateGuardian_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_supports_basic_shaders(GraphicsStateGuardian self)
        
        /**
         * Returns true if this particular GSG supports arbfp1+arbvp1 or above.
         */
        """
        pass

    def get_supports_buffer_texture(self, GraphicsStateGuardian_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_supports_buffer_texture(GraphicsStateGuardian self)
        
        /**
         * Returns true if this GSG can render buffer textures.
         */
        """
        pass

    def get_supports_cg_profile(self, GraphicsStateGuardian_self, str_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_supports_cg_profile(GraphicsStateGuardian self, str name)
        """
        pass

    def get_supports_compressed_texture(self, GraphicsStateGuardian_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_supports_compressed_texture(GraphicsStateGuardian self)
        
        /**
         * Returns true if this GSG can compress textures as it loads them into
         * texture memory, and/or accept pre-compressed textures for storing.
         */
        """
        pass

    def get_supports_compute_shaders(self, GraphicsStateGuardian_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_supports_compute_shaders(GraphicsStateGuardian self)
        
        /**
         * Returns true if this particular GSG supports compute shaders.
         */
        """
        pass

    def get_supports_cube_map(self, GraphicsStateGuardian_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_supports_cube_map(GraphicsStateGuardian self)
        
        /**
         * Returns true if this GSG can render cube map textures.
         */
        """
        pass

    def get_supports_cube_map_array(self, GraphicsStateGuardian_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_supports_cube_map_array(GraphicsStateGuardian self)
        
        /**
         * Returns true if this GSG can render cube map arrays.
         */
        """
        pass

    def get_supports_depth_stencil(self, GraphicsStateGuardian_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_supports_depth_stencil(GraphicsStateGuardian self)
        
        /**
         * Returns true if this particular GSG supports textures whose format is
         * F_depth_stencil.  This only returns true if the GSG supports the full
         * packed depth-stencil functionality.
         */
        """
        pass

    def get_supports_depth_texture(self, GraphicsStateGuardian_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_supports_depth_texture(GraphicsStateGuardian self)
        
        /**
         * Returns true if this particular GSG supports textures whose format is
         * F_depth_stencil.  This returns true if the GSG supports GL_DEPTH_COMPONENT
         * textures, which are considered a limited but still valid case of
         * F_depth_stencil.
         */
        """
        pass

    def get_supports_dual_source_blending(self, GraphicsStateGuardian_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_supports_dual_source_blending(GraphicsStateGuardian self)
        
        /**
         * Returns true if dual source (incoming1_color and incoming1_alpha) blend
         * operands are supported by this GSG.
         */
        """
        pass

    def get_supports_generate_mipmap(self, GraphicsStateGuardian_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_supports_generate_mipmap(GraphicsStateGuardian self)
        
        /**
         * Returns true if this particular GSG can generate mipmaps for a texture
         * automatically, or if they must be generated in software.  If this is true,
         * then mipmaps can safely be enabled for rendered textures (e.g.  using the
         * MultitexReducer).
         */
        """
        pass

    def get_supports_geometry_instancing(self, GraphicsStateGuardian_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_supports_geometry_instancing(GraphicsStateGuardian self)
        
        /**
         * Returns true if this particular GSG supports hardware geometry instancing:
         * the ability to render multiple copies of a model.  In OpenGL, this is done
         * using the EXT_draw_instanced extension.
         */
        """
        pass

    def get_supports_geometry_shaders(self, GraphicsStateGuardian_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_supports_geometry_shaders(GraphicsStateGuardian self)
        
        /**
         * Returns true if this particular GSG supports geometry shaders.
         */
        """
        pass

    def get_supports_glsl(self, GraphicsStateGuardian_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_supports_glsl(GraphicsStateGuardian self)
        
        /**
         * Returns true if this particular GSG supports GLSL shaders.
         */
        """
        pass

    def get_supports_indirect_draw(self, GraphicsStateGuardian_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_supports_indirect_draw(GraphicsStateGuardian self)
        
        /**
         * Returns true if this particular GSG supports draw calls for which the
         * information comes from a buffer.
         */
        """
        pass

    def get_supports_luminance_texture(self, GraphicsStateGuardian_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_supports_luminance_texture(GraphicsStateGuardian self)
        
        /**
         * Returns true if this particular GSG supports luminance textures.
         */
        """
        pass

    def get_supports_occlusion_query(self, GraphicsStateGuardian_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_supports_occlusion_query(GraphicsStateGuardian self)
        
        /**
         * Returns true if this GSG supports an occlusion query.  If this is true,
         * then begin_occlusion_query() and end_occlusion_query() may be called to
         * bracket a sequence of draw_triangles() (or whatever) calls to measure
         * pixels that pass the depth test.
         */
        """
        pass

    def get_supports_sampler_objects(self, GraphicsStateGuardian_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_supports_sampler_objects(GraphicsStateGuardian self)
        
        /**
         * Returns true if this particular GSG supports the use of sampler objects to
         * record texture sampling parameters separately from the texture objects.
         * This doesn't really affect functionality, but if this is false, it may mean
         * that using the same texture with different SamplerState objects will result
         * in reduced performance.
         */
        """
        pass

    def get_supports_stencil(self, GraphicsStateGuardian_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_supports_stencil(GraphicsStateGuardian self)
        
        /**
         * Returns true if this particular GSG supports stencil buffers at all.
         */
        """
        pass

    def get_supports_tessellation_shaders(self, GraphicsStateGuardian_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_supports_tessellation_shaders(GraphicsStateGuardian self)
        
        /**
         * Returns true if this particular GSG supports tesselation shaders.
         */
        """
        pass

    def get_supports_texture_combine(self, GraphicsStateGuardian_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_supports_texture_combine(GraphicsStateGuardian self)
        
        /**
         * Returns true if this particular GSG can use the TextureStage::M_combine
         * mode, which includes all of the texture blend modes specified by
         * set_combine_rgb() and/or set_combine_alpha().  If this is false, you must
         * limit yourself to using the simpler blend modes.
         */
        """
        pass

    def get_supports_texture_dot3(self, GraphicsStateGuardian_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_supports_texture_dot3(GraphicsStateGuardian self)
        
        /**
         * Returns true if this GSG can use the TextureStage::CM_dot3_rgb or
         * CM_dot3_rgba combine modes.
         */
        """
        pass

    def get_supports_texture_saved_result(self, GraphicsStateGuardian_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_supports_texture_saved_result(GraphicsStateGuardian self)
        
        /**
         * Returns true if this GSG can use the TextureStage::CS_last_saved_result
         * source, which allows you to save the result of a TextureStage and re-use it
         * for multiple inputs.
         */
        """
        pass

    def get_supports_tex_non_pow2(self, GraphicsStateGuardian_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_supports_tex_non_pow2(GraphicsStateGuardian self)
        
        /**
         * Returns true if this GSG can handle non power of two sized textures.
         */
        """
        pass

    def get_supports_timer_query(self, GraphicsStateGuardian_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_supports_timer_query(GraphicsStateGuardian self)
        
        /**
         * Returns true if this GSG supports a timer query.
         */
        """
        pass

    def get_supports_two_sided_stencil(self, GraphicsStateGuardian_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_supports_two_sided_stencil(GraphicsStateGuardian self)
        
        /**
         * Returns true if this particular GSG supports two sided stencil: different
         * stencil settings for the front and back side of the same polygon.
         */
        """
        pass

    def get_texture_quality_override(self, GraphicsStateGuardian_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_texture_quality_override(GraphicsStateGuardian self)
        
        /**
         * Returns the global quality_level override specified by
         * set_texture_quality_override.
         *
         * This is mainly useful for the tinydisplay software renderer.  See
         * Texture::set_quality_level().
         */
        """
        pass

    def get_threading_model(self, GraphicsStateGuardian_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_threading_model(GraphicsStateGuardian self)
        
        /**
         * Returns the threading model that was used to create this GSG.
         */
        """
        pass

    def get_timer_queries_active(self, GraphicsStateGuardian_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_timer_queries_active(GraphicsStateGuardian self)
        
        /**
         * Returns true if timer queries are currently enabled on this GSG.
         */
        """
        pass

    def hasExtension(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_extension(GraphicsStateGuardian self, str extension)
        """
        pass

    def has_extension(self, GraphicsStateGuardian_self, str_extension): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_extension(GraphicsStateGuardian self, str extension)
        """
        pass

    def isActive(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_active(GraphicsStateGuardian self)
        
        /**
         * Returns the active flag associated with the GraphicsStateGuardian.
         */
        """
        pass

    def isHardware(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_hardware(GraphicsStateGuardian self)
        
        /**
         * Returns true if this GSG appears to be hardware-accelerated, or false if it
         * is known to be software only.
         */
        """
        pass

    def isValid(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_valid(GraphicsStateGuardian self)
        
        /**
         * Returns true if the GSG has been correctly initialized within a graphics
         * context, false if there has been some problem or it hasn't been initialized
         * yet.
         */
        """
        pass

    def is_active(self, GraphicsStateGuardian_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_active(GraphicsStateGuardian self)
        
        /**
         * Returns the active flag associated with the GraphicsStateGuardian.
         */
        """
        pass

    def is_hardware(self, GraphicsStateGuardian_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_hardware(GraphicsStateGuardian self)
        
        /**
         * Returns true if this GSG appears to be hardware-accelerated, or false if it
         * is known to be software only.
         */
        """
        pass

    def is_valid(self, GraphicsStateGuardian_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_valid(GraphicsStateGuardian self)
        
        /**
         * Returns true if the GSG has been correctly initialized within a graphics
         * context, false if there has been some problem or it hasn't been initialized
         * yet.
         */
        """
        pass

    def needsReset(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        needs_reset(GraphicsStateGuardian self)
        
        /**
         * Returns true if the gsg is marked as needing a reset.
         */
        """
        pass

    def needs_reset(self, GraphicsStateGuardian_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        needs_reset(GraphicsStateGuardian self)
        
        /**
         * Returns true if the gsg is marked as needing a reset.
         */
        """
        pass

    def releaseAll(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        release_all(const GraphicsStateGuardian self)
        
        /**
         * Releases all prepared objects.
         */
        """
        pass

    def releaseAllGeoms(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        release_all_geoms(const GraphicsStateGuardian self)
        
        /**
         * Frees the resources for all geoms associated with this GSG.
         */
        """
        pass

    def releaseAllIndexBuffers(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        release_all_index_buffers(const GraphicsStateGuardian self)
        
        /**
         * Frees the resources for all index buffers associated with this GSG.
         */
        """
        pass

    def releaseAllSamplers(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        release_all_samplers(const GraphicsStateGuardian self)
        
        /**
         * Frees the resources for all samplers associated with this GSG.
         */
        """
        pass

    def releaseAllShaderBuffers(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        release_all_shader_buffers(const GraphicsStateGuardian self)
        
        /**
         * Frees the resources for all index buffers associated with this GSG.
         */
        """
        pass

    def releaseAllTextures(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        release_all_textures(const GraphicsStateGuardian self)
        
        /**
         * Frees the resources for all textures associated with this GSG.
         */
        """
        pass

    def releaseAllVertexBuffers(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        release_all_vertex_buffers(const GraphicsStateGuardian self)
        
        /**
         * Frees the resources for all vertex buffers associated with this GSG.
         */
        """
        pass

    def release_all(self, const_GraphicsStateGuardian_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        release_all(const GraphicsStateGuardian self)
        
        /**
         * Releases all prepared objects.
         */
        """
        pass

    def release_all_geoms(self, const_GraphicsStateGuardian_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        release_all_geoms(const GraphicsStateGuardian self)
        
        /**
         * Frees the resources for all geoms associated with this GSG.
         */
        """
        pass

    def release_all_index_buffers(self, const_GraphicsStateGuardian_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        release_all_index_buffers(const GraphicsStateGuardian self)
        
        /**
         * Frees the resources for all index buffers associated with this GSG.
         */
        """
        pass

    def release_all_samplers(self, const_GraphicsStateGuardian_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        release_all_samplers(const GraphicsStateGuardian self)
        
        /**
         * Frees the resources for all samplers associated with this GSG.
         */
        """
        pass

    def release_all_shader_buffers(self, const_GraphicsStateGuardian_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        release_all_shader_buffers(const GraphicsStateGuardian self)
        
        /**
         * Frees the resources for all index buffers associated with this GSG.
         */
        """
        pass

    def release_all_textures(self, const_GraphicsStateGuardian_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        release_all_textures(const GraphicsStateGuardian self)
        
        /**
         * Frees the resources for all textures associated with this GSG.
         */
        """
        pass

    def release_all_vertex_buffers(self, const_GraphicsStateGuardian_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        release_all_vertex_buffers(const GraphicsStateGuardian self)
        
        /**
         * Frees the resources for all vertex buffers associated with this GSG.
         */
        """
        pass

    def restoreGamma(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        restore_gamma(const GraphicsStateGuardian self)
        """
        pass

    def restore_gamma(self, const_GraphicsStateGuardian_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        restore_gamma(const GraphicsStateGuardian self)
        """
        pass

    def setActive(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_active(const GraphicsStateGuardian self, bool active)
        
        /**
         * Sets the active flag associated with the GraphicsStateGuardian.  If the
         * GraphicsStateGuardian is marked inactive, nothing is rendered.  This is not
         * normally turned off unless there is a problem with the rendering detected
         * at a low level.
         */
        """
        pass

    def setCoordinateSystem(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_coordinate_system(const GraphicsStateGuardian self, int cs)
        """
        pass

    def setFlashTexture(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_flash_texture(const GraphicsStateGuardian self, Texture tex)
        """
        pass

    def setGamma(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_gamma(const GraphicsStateGuardian self, float gamma)
        """
        pass

    def setIncompleteRender(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_incomplete_render(const GraphicsStateGuardian self, bool incomplete_render)
        
        /**
         * Sets the incomplete_render flag.  When this is true, the frame will be
         * rendered even if some of the geometry or textures in the scene are not
         * available (e.g.  they have been temporarily paged out).  When this is
         * false, the frame will be held up while this data is reloaded.
         *
         * Setting this true allows for a smoother frame rate, but occasionally parts
         * of the frame will be invisible or missing (they will generally come in
         * within a second or two).  Setting this false guarantees that every frame
         * will be complete, but may cause more chugs as things are loaded up at
         * runtime.
         *
         * You may want to set this false during loading screens, to guarantee that
         * all of your assets are available by the time you take the loading screen
         * down.
         *
         * This flag may also be set individually on each DisplayRegion.  It will be
         * considered true for a given DisplayRegion only if it is true on both the
         * GSG and on the DisplayRegion.
         */
        """
        pass

    def setLoader(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_loader(const GraphicsStateGuardian self, Loader loader)
        
        /**
         * Sets the Loader object that will be used by this GSG to load textures when
         * necessary, if get_incomplete_render() is true.
         */
        """
        pass

    def setScene(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_scene(const GraphicsStateGuardian self, SceneSetup scene_setup)
        """
        pass

    def setShaderGenerator(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_shader_generator(const GraphicsStateGuardian self, ShaderGenerator shader_generator)
        
        /**
         * Sets the ShaderGenerator object that will be used by this GSG to generate
         * shaders when necessary.
         */
        """
        pass

    def setShaderModel(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_shader_model(const GraphicsStateGuardian self, int shader_model)
        
        /**
         * Sets the ShaderModel.  This will override the auto- detected shader model
         * during GSG reset.  Useful for testing lower-end shaders.
         */
        """
        pass

    def setTextureQualityOverride(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_texture_quality_override(const GraphicsStateGuardian self, int quality_level)
        
        /**
         * Specifies the global quality_level to be imposed for all Textures rendered
         * by this GSG.  This overrides the value set on individual textures via
         * Texture::set_quality_level().  Set this to Texture::QL_default in order to
         * allow the individual texture quality levels to be respected.
         *
         * This is mainly useful for the tinydisplay software renderer.  See
         * Texture::set_quality_level().
         */
        """
        pass

    def set_active(self, const_GraphicsStateGuardian_self, bool_active): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_active(const GraphicsStateGuardian self, bool active)
        
        /**
         * Sets the active flag associated with the GraphicsStateGuardian.  If the
         * GraphicsStateGuardian is marked inactive, nothing is rendered.  This is not
         * normally turned off unless there is a problem with the rendering detected
         * at a low level.
         */
        """
        pass

    def set_coordinate_system(self, const_GraphicsStateGuardian_self, int_cs): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_coordinate_system(const GraphicsStateGuardian self, int cs)
        """
        pass

    def set_flash_texture(self, const_GraphicsStateGuardian_self, Texture_tex): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_flash_texture(const GraphicsStateGuardian self, Texture tex)
        """
        pass

    def set_gamma(self, const_GraphicsStateGuardian_self, float_gamma): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_gamma(const GraphicsStateGuardian self, float gamma)
        """
        pass

    def set_incomplete_render(self, const_GraphicsStateGuardian_self, bool_incomplete_render): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_incomplete_render(const GraphicsStateGuardian self, bool incomplete_render)
        
        /**
         * Sets the incomplete_render flag.  When this is true, the frame will be
         * rendered even if some of the geometry or textures in the scene are not
         * available (e.g.  they have been temporarily paged out).  When this is
         * false, the frame will be held up while this data is reloaded.
         *
         * Setting this true allows for a smoother frame rate, but occasionally parts
         * of the frame will be invisible or missing (they will generally come in
         * within a second or two).  Setting this false guarantees that every frame
         * will be complete, but may cause more chugs as things are loaded up at
         * runtime.
         *
         * You may want to set this false during loading screens, to guarantee that
         * all of your assets are available by the time you take the loading screen
         * down.
         *
         * This flag may also be set individually on each DisplayRegion.  It will be
         * considered true for a given DisplayRegion only if it is true on both the
         * GSG and on the DisplayRegion.
         */
        """
        pass

    def set_loader(self, const_GraphicsStateGuardian_self, Loader_loader): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_loader(const GraphicsStateGuardian self, Loader loader)
        
        /**
         * Sets the Loader object that will be used by this GSG to load textures when
         * necessary, if get_incomplete_render() is true.
         */
        """
        pass

    def set_scene(self, const_GraphicsStateGuardian_self, SceneSetup_scene_setup): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_scene(const GraphicsStateGuardian self, SceneSetup scene_setup)
        """
        pass

    def set_shader_generator(self, const_GraphicsStateGuardian_self, ShaderGenerator_shader_generator): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_shader_generator(const GraphicsStateGuardian self, ShaderGenerator shader_generator)
        
        /**
         * Sets the ShaderGenerator object that will be used by this GSG to generate
         * shaders when necessary.
         */
        """
        pass

    def set_shader_model(self, const_GraphicsStateGuardian_self, int_shader_model): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_shader_model(const GraphicsStateGuardian self, int shader_model)
        
        /**
         * Sets the ShaderModel.  This will override the auto- detected shader model
         * during GSG reset.  Useful for testing lower-end shaders.
         */
        """
        pass

    def set_texture_quality_override(self, const_GraphicsStateGuardian_self, int_quality_level): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_texture_quality_override(const GraphicsStateGuardian self, int quality_level)
        
        /**
         * Specifies the global quality_level to be imposed for all Textures rendered
         * by this GSG.  This overrides the value set on individual textures via
         * Texture::set_quality_level().  Set this to Texture::QL_default in order to
         * allow the individual texture quality levels to be respected.
         *
         * This is mainly useful for the tinydisplay software renderer.  See
         * Texture::set_quality_level().
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    active = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    coordinate_system = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    copy_texture_inverted = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    driver_renderer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    driver_shader_version_major = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    driver_shader_version_minor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    driver_vendor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    driver_version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    driver_version_major = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    driver_version_minor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    effective_incomplete_render = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    flash_texture = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    gamma = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    incomplete_render = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    loader = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    max_2d_texture_array_layers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """//z axis"""

    max_3d_texture_dimension = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    max_buffer_texture_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    max_clip_planes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    max_color_targets = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    max_cube_map_dimension = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """//z axis"""

    max_lights = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    max_texture_dimension = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    max_texture_stages = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    max_vertex_transforms = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    max_vertex_transform_indices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    max_vertices_per_array = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    max_vertices_per_primitive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pipe = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    prepared_objects = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    scene = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    shader_generator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    shader_model = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    supports_2d_texture_array = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    supports_3d_texture = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    supports_basic_shaders = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    supports_buffer_texture = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    supports_compressed_texture = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    supports_compute_shaders = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    supports_cube_map = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    supports_cube_map_array = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    supports_depth_stencil = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    supports_depth_texture = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    supports_dual_source_blending = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    supports_generate_mipmap = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    supports_geometry_instancing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    supports_geometry_shaders = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    supports_glsl = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    supports_hlsl = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    supports_indirect_draw = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    supports_luminance_texture = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    supports_multisample = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    supports_occlusion_query = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    supports_sampler_objects = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    supports_shadow_filter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    supports_stencil = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    supports_tessellation_shaders = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    supports_texture_combine = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    supports_texture_dot3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    supports_texture_saved_result = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    supports_texture_srgb = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    supports_tex_non_pow2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    supports_timer_query = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    supports_two_sided_stencil = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    texture_quality_override = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    timer_queries_active = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    valid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        'SM00': 0,
        'SM11': 1,
        'SM20': 2,
        'SM2X': 3,
        'SM30': 4,
        'SM40': 5,
        'SM50': 6,
        'SM51': 7,
        'SM_00': 0,
        'SM_11': 1,
        'SM_20': 2,
        'SM_2X': 3,
        'SM_30': 4,
        'SM_40': 5,
        'SM_50': 6,
        'SM_51': 7,
        '__doc__': '/**\n * Encapsulates all the communication with a particular instance of a given\n * rendering backend.  Tries to guarantee that redundant state-change requests\n * are not issued (hence "state guardian").\n *\n * There will be one of these objects for each different graphics context\n * active in the system.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.GraphicsStateGuardian' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2DD8D0>'
        'active': None, # (!) real value is "<attribute 'active' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'beginScene': None, # (!) real value is "<method 'beginScene' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'begin_scene': None, # (!) real value is "<method 'begin_scene' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'clearFlashTexture': None, # (!) real value is "<method 'clearFlashTexture' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'clear_flash_texture': None, # (!) real value is "<method 'clear_flash_texture' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'coordinate_system': None, # (!) real value is "<attribute 'coordinate_system' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'copy_texture_inverted': None, # (!) real value is "<attribute 'copy_texture_inverted' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'driver_renderer': None, # (!) real value is "<attribute 'driver_renderer' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'driver_shader_version_major': None, # (!) real value is "<attribute 'driver_shader_version_major' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'driver_shader_version_minor': None, # (!) real value is "<attribute 'driver_shader_version_minor' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'driver_vendor': None, # (!) real value is "<attribute 'driver_vendor' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'driver_version': None, # (!) real value is "<attribute 'driver_version' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'driver_version_major': None, # (!) real value is "<attribute 'driver_version_major' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'driver_version_minor': None, # (!) real value is "<attribute 'driver_version_minor' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'effective_incomplete_render': None, # (!) real value is "<attribute 'effective_incomplete_render' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'endScene': None, # (!) real value is "<method 'endScene' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'end_scene': None, # (!) real value is "<method 'end_scene' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'flash_texture': None, # (!) real value is "<attribute 'flash_texture' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'gamma': None, # (!) real value is "<attribute 'gamma' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'getAlphaScaleTextureStage': None, # (!) real value is '<staticmethod(<built-in method getAlphaScaleTextureStage of type object at 0x00007FFCFE2DD8D0>)>'
        'getAlphaScaleViaTexture': None, # (!) real value is "<method 'getAlphaScaleViaTexture' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2DD8D0>)>'
        'getColorScaleViaLighting': None, # (!) real value is "<method 'getColorScaleViaLighting' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'getCoordinateSystem': None, # (!) real value is "<method 'getCoordinateSystem' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'getCopyTextureInverted': None, # (!) real value is "<method 'getCopyTextureInverted' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'getDriverRenderer': None, # (!) real value is "<method 'getDriverRenderer' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'getDriverShaderVersionMajor': None, # (!) real value is "<method 'getDriverShaderVersionMajor' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'getDriverShaderVersionMinor': None, # (!) real value is "<method 'getDriverShaderVersionMinor' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'getDriverVendor': None, # (!) real value is "<method 'getDriverVendor' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'getDriverVersion': None, # (!) real value is "<method 'getDriverVersion' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'getDriverVersionMajor': None, # (!) real value is "<method 'getDriverVersionMajor' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'getDriverVersionMinor': None, # (!) real value is "<method 'getDriverVersionMinor' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'getEngine': None, # (!) real value is "<method 'getEngine' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'getFlashTexture': None, # (!) real value is "<method 'getFlashTexture' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'getGamma': None, # (!) real value is "<method 'getGamma' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'getInternalCoordinateSystem': None, # (!) real value is "<method 'getInternalCoordinateSystem' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'getLoader': None, # (!) real value is "<method 'getLoader' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'getMax2dTextureArrayLayers': None, # (!) real value is "<method 'getMax2dTextureArrayLayers' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'getMax3dTextureDimension': None, # (!) real value is "<method 'getMax3dTextureDimension' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'getMaxBufferTextureSize': None, # (!) real value is "<method 'getMaxBufferTextureSize' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'getMaxClipPlanes': None, # (!) real value is "<method 'getMaxClipPlanes' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'getMaxColorTargets': None, # (!) real value is "<method 'getMaxColorTargets' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'getMaxCubeMapDimension': None, # (!) real value is "<method 'getMaxCubeMapDimension' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'getMaxLights': None, # (!) real value is "<method 'getMaxLights' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'getMaxTextureStages': None, # (!) real value is "<method 'getMaxTextureStages' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'getMaxVertexTransformIndices': None, # (!) real value is "<method 'getMaxVertexTransformIndices' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'getMaxVertexTransforms': None, # (!) real value is "<method 'getMaxVertexTransforms' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'getMaximumSimultaneousRenderTargets': None, # (!) real value is "<method 'getMaximumSimultaneousRenderTargets' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'getPipe': None, # (!) real value is "<method 'getPipe' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'getPreparedObjects': None, # (!) real value is "<method 'getPreparedObjects' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'getPreparedTextures': None, # (!) real value is "<method 'getPreparedTextures' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'getRuntimeColorScale': None, # (!) real value is "<method 'getRuntimeColorScale' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'getScene': None, # (!) real value is "<method 'getScene' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'getShaderGenerator': None, # (!) real value is "<method 'getShaderGenerator' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'getShaderModel': None, # (!) real value is "<method 'getShaderModel' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'getSupports2dTextureArray': None, # (!) real value is "<method 'getSupports2dTextureArray' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'getSupports3dTexture': None, # (!) real value is "<method 'getSupports3dTexture' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'getSupportsBasicShaders': None, # (!) real value is "<method 'getSupportsBasicShaders' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'getSupportsBufferTexture': None, # (!) real value is "<method 'getSupportsBufferTexture' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'getSupportsCgProfile': None, # (!) real value is "<method 'getSupportsCgProfile' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'getSupportsCompressedTexture': None, # (!) real value is "<method 'getSupportsCompressedTexture' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'getSupportsComputeShaders': None, # (!) real value is "<method 'getSupportsComputeShaders' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'getSupportsCubeMap': None, # (!) real value is "<method 'getSupportsCubeMap' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'getSupportsCubeMapArray': None, # (!) real value is "<method 'getSupportsCubeMapArray' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'getSupportsDepthStencil': None, # (!) real value is "<method 'getSupportsDepthStencil' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'getSupportsDepthTexture': None, # (!) real value is "<method 'getSupportsDepthTexture' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'getSupportsDualSourceBlending': None, # (!) real value is "<method 'getSupportsDualSourceBlending' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'getSupportsGenerateMipmap': None, # (!) real value is "<method 'getSupportsGenerateMipmap' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'getSupportsGeometryInstancing': None, # (!) real value is "<method 'getSupportsGeometryInstancing' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'getSupportsGeometryShaders': None, # (!) real value is "<method 'getSupportsGeometryShaders' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'getSupportsGlsl': None, # (!) real value is "<method 'getSupportsGlsl' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'getSupportsIndirectDraw': None, # (!) real value is "<method 'getSupportsIndirectDraw' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'getSupportsLuminanceTexture': None, # (!) real value is "<method 'getSupportsLuminanceTexture' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'getSupportsOcclusionQuery': None, # (!) real value is "<method 'getSupportsOcclusionQuery' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'getSupportsSamplerObjects': None, # (!) real value is "<method 'getSupportsSamplerObjects' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'getSupportsStencil': None, # (!) real value is "<method 'getSupportsStencil' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'getSupportsTessellationShaders': None, # (!) real value is "<method 'getSupportsTessellationShaders' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'getSupportsTexNonPow2': None, # (!) real value is "<method 'getSupportsTexNonPow2' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'getSupportsTextureCombine': None, # (!) real value is "<method 'getSupportsTextureCombine' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'getSupportsTextureDot3': None, # (!) real value is "<method 'getSupportsTextureDot3' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'getSupportsTextureSavedResult': None, # (!) real value is "<method 'getSupportsTextureSavedResult' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'getSupportsTimerQuery': None, # (!) real value is "<method 'getSupportsTimerQuery' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'getSupportsTwoSidedStencil': None, # (!) real value is "<method 'getSupportsTwoSidedStencil' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'getTextureQualityOverride': None, # (!) real value is "<method 'getTextureQualityOverride' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'getThreadingModel': None, # (!) real value is "<method 'getThreadingModel' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'getTimerQueriesActive': None, # (!) real value is "<method 'getTimerQueriesActive' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'get_alpha_scale_texture_stage': None, # (!) real value is '<staticmethod(<built-in method get_alpha_scale_texture_stage of type object at 0x00007FFCFE2DD8D0>)>'
        'get_alpha_scale_via_texture': None, # (!) real value is "<method 'get_alpha_scale_via_texture' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2DD8D0>)>'
        'get_color_scale_via_lighting': None, # (!) real value is "<method 'get_color_scale_via_lighting' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'get_coordinate_system': None, # (!) real value is "<method 'get_coordinate_system' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'get_copy_texture_inverted': None, # (!) real value is "<method 'get_copy_texture_inverted' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'get_driver_renderer': None, # (!) real value is "<method 'get_driver_renderer' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'get_driver_shader_version_major': None, # (!) real value is "<method 'get_driver_shader_version_major' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'get_driver_shader_version_minor': None, # (!) real value is "<method 'get_driver_shader_version_minor' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'get_driver_vendor': None, # (!) real value is "<method 'get_driver_vendor' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'get_driver_version': None, # (!) real value is "<method 'get_driver_version' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'get_driver_version_major': None, # (!) real value is "<method 'get_driver_version_major' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'get_driver_version_minor': None, # (!) real value is "<method 'get_driver_version_minor' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'get_engine': None, # (!) real value is "<method 'get_engine' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'get_flash_texture': None, # (!) real value is "<method 'get_flash_texture' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'get_gamma': None, # (!) real value is "<method 'get_gamma' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'get_internal_coordinate_system': None, # (!) real value is "<method 'get_internal_coordinate_system' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'get_loader': None, # (!) real value is "<method 'get_loader' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'get_max_2d_texture_array_layers': None, # (!) real value is "<method 'get_max_2d_texture_array_layers' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'get_max_3d_texture_dimension': None, # (!) real value is "<method 'get_max_3d_texture_dimension' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'get_max_buffer_texture_size': None, # (!) real value is "<method 'get_max_buffer_texture_size' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'get_max_clip_planes': None, # (!) real value is "<method 'get_max_clip_planes' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'get_max_color_targets': None, # (!) real value is "<method 'get_max_color_targets' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'get_max_cube_map_dimension': None, # (!) real value is "<method 'get_max_cube_map_dimension' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'get_max_lights': None, # (!) real value is "<method 'get_max_lights' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'get_max_texture_stages': None, # (!) real value is "<method 'get_max_texture_stages' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'get_max_vertex_transform_indices': None, # (!) real value is "<method 'get_max_vertex_transform_indices' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'get_max_vertex_transforms': None, # (!) real value is "<method 'get_max_vertex_transforms' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'get_maximum_simultaneous_render_targets': None, # (!) real value is "<method 'get_maximum_simultaneous_render_targets' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'get_pipe': None, # (!) real value is "<method 'get_pipe' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'get_prepared_objects': None, # (!) real value is "<method 'get_prepared_objects' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'get_prepared_textures': None, # (!) real value is "<method 'get_prepared_textures' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'get_runtime_color_scale': None, # (!) real value is "<method 'get_runtime_color_scale' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'get_scene': None, # (!) real value is "<method 'get_scene' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'get_shader_generator': None, # (!) real value is "<method 'get_shader_generator' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'get_shader_model': None, # (!) real value is "<method 'get_shader_model' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'get_supports_2d_texture_array': None, # (!) real value is "<method 'get_supports_2d_texture_array' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'get_supports_3d_texture': None, # (!) real value is "<method 'get_supports_3d_texture' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'get_supports_basic_shaders': None, # (!) real value is "<method 'get_supports_basic_shaders' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'get_supports_buffer_texture': None, # (!) real value is "<method 'get_supports_buffer_texture' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'get_supports_cg_profile': None, # (!) real value is "<method 'get_supports_cg_profile' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'get_supports_compressed_texture': None, # (!) real value is "<method 'get_supports_compressed_texture' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'get_supports_compute_shaders': None, # (!) real value is "<method 'get_supports_compute_shaders' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'get_supports_cube_map': None, # (!) real value is "<method 'get_supports_cube_map' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'get_supports_cube_map_array': None, # (!) real value is "<method 'get_supports_cube_map_array' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'get_supports_depth_stencil': None, # (!) real value is "<method 'get_supports_depth_stencil' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'get_supports_depth_texture': None, # (!) real value is "<method 'get_supports_depth_texture' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'get_supports_dual_source_blending': None, # (!) real value is "<method 'get_supports_dual_source_blending' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'get_supports_generate_mipmap': None, # (!) real value is "<method 'get_supports_generate_mipmap' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'get_supports_geometry_instancing': None, # (!) real value is "<method 'get_supports_geometry_instancing' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'get_supports_geometry_shaders': None, # (!) real value is "<method 'get_supports_geometry_shaders' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'get_supports_glsl': None, # (!) real value is "<method 'get_supports_glsl' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'get_supports_indirect_draw': None, # (!) real value is "<method 'get_supports_indirect_draw' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'get_supports_luminance_texture': None, # (!) real value is "<method 'get_supports_luminance_texture' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'get_supports_occlusion_query': None, # (!) real value is "<method 'get_supports_occlusion_query' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'get_supports_sampler_objects': None, # (!) real value is "<method 'get_supports_sampler_objects' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'get_supports_stencil': None, # (!) real value is "<method 'get_supports_stencil' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'get_supports_tessellation_shaders': None, # (!) real value is "<method 'get_supports_tessellation_shaders' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'get_supports_tex_non_pow2': None, # (!) real value is "<method 'get_supports_tex_non_pow2' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'get_supports_texture_combine': None, # (!) real value is "<method 'get_supports_texture_combine' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'get_supports_texture_dot3': None, # (!) real value is "<method 'get_supports_texture_dot3' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'get_supports_texture_saved_result': None, # (!) real value is "<method 'get_supports_texture_saved_result' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'get_supports_timer_query': None, # (!) real value is "<method 'get_supports_timer_query' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'get_supports_two_sided_stencil': None, # (!) real value is "<method 'get_supports_two_sided_stencil' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'get_texture_quality_override': None, # (!) real value is "<method 'get_texture_quality_override' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'get_threading_model': None, # (!) real value is "<method 'get_threading_model' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'get_timer_queries_active': None, # (!) real value is "<method 'get_timer_queries_active' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'hasExtension': None, # (!) real value is "<method 'hasExtension' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'has_extension': None, # (!) real value is "<method 'has_extension' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'incomplete_render': None, # (!) real value is "<attribute 'incomplete_render' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'isActive': None, # (!) real value is "<method 'isActive' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'isHardware': None, # (!) real value is "<method 'isHardware' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'isValid': None, # (!) real value is "<method 'isValid' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'is_active': None, # (!) real value is "<method 'is_active' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'is_hardware': None, # (!) real value is "<method 'is_hardware' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'is_valid': None, # (!) real value is "<method 'is_valid' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'loader': None, # (!) real value is "<attribute 'loader' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'max_2d_texture_array_layers': None, # (!) real value is "<attribute 'max_2d_texture_array_layers' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'max_3d_texture_dimension': None, # (!) real value is "<attribute 'max_3d_texture_dimension' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'max_buffer_texture_size': None, # (!) real value is "<attribute 'max_buffer_texture_size' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'max_clip_planes': None, # (!) real value is "<attribute 'max_clip_planes' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'max_color_targets': None, # (!) real value is "<attribute 'max_color_targets' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'max_cube_map_dimension': None, # (!) real value is "<attribute 'max_cube_map_dimension' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'max_lights': None, # (!) real value is "<attribute 'max_lights' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'max_texture_dimension': None, # (!) real value is "<attribute 'max_texture_dimension' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'max_texture_stages': None, # (!) real value is "<attribute 'max_texture_stages' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'max_vertex_transform_indices': None, # (!) real value is "<attribute 'max_vertex_transform_indices' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'max_vertex_transforms': None, # (!) real value is "<attribute 'max_vertex_transforms' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'max_vertices_per_array': None, # (!) real value is "<attribute 'max_vertices_per_array' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'max_vertices_per_primitive': None, # (!) real value is "<attribute 'max_vertices_per_primitive' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'needsReset': None, # (!) real value is "<method 'needsReset' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'needs_reset': None, # (!) real value is "<method 'needs_reset' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'pipe': None, # (!) real value is "<attribute 'pipe' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'prepared_objects': None, # (!) real value is "<attribute 'prepared_objects' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'releaseAll': None, # (!) real value is "<method 'releaseAll' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'releaseAllGeoms': None, # (!) real value is "<method 'releaseAllGeoms' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'releaseAllIndexBuffers': None, # (!) real value is "<method 'releaseAllIndexBuffers' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'releaseAllSamplers': None, # (!) real value is "<method 'releaseAllSamplers' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'releaseAllShaderBuffers': None, # (!) real value is "<method 'releaseAllShaderBuffers' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'releaseAllTextures': None, # (!) real value is "<method 'releaseAllTextures' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'releaseAllVertexBuffers': None, # (!) real value is "<method 'releaseAllVertexBuffers' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'release_all': None, # (!) real value is "<method 'release_all' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'release_all_geoms': None, # (!) real value is "<method 'release_all_geoms' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'release_all_index_buffers': None, # (!) real value is "<method 'release_all_index_buffers' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'release_all_samplers': None, # (!) real value is "<method 'release_all_samplers' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'release_all_shader_buffers': None, # (!) real value is "<method 'release_all_shader_buffers' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'release_all_textures': None, # (!) real value is "<method 'release_all_textures' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'release_all_vertex_buffers': None, # (!) real value is "<method 'release_all_vertex_buffers' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'restoreGamma': None, # (!) real value is "<method 'restoreGamma' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'restore_gamma': None, # (!) real value is "<method 'restore_gamma' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'scene': None, # (!) real value is "<attribute 'scene' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'setActive': None, # (!) real value is "<method 'setActive' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'setCoordinateSystem': None, # (!) real value is "<method 'setCoordinateSystem' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'setFlashTexture': None, # (!) real value is "<method 'setFlashTexture' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'setGamma': None, # (!) real value is "<method 'setGamma' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'setIncompleteRender': None, # (!) real value is "<method 'setIncompleteRender' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'setLoader': None, # (!) real value is "<method 'setLoader' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'setScene': None, # (!) real value is "<method 'setScene' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'setShaderGenerator': None, # (!) real value is "<method 'setShaderGenerator' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'setShaderModel': None, # (!) real value is "<method 'setShaderModel' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'setTextureQualityOverride': None, # (!) real value is "<method 'setTextureQualityOverride' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'set_active': None, # (!) real value is "<method 'set_active' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'set_coordinate_system': None, # (!) real value is "<method 'set_coordinate_system' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'set_flash_texture': None, # (!) real value is "<method 'set_flash_texture' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'set_gamma': None, # (!) real value is "<method 'set_gamma' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'set_incomplete_render': None, # (!) real value is "<method 'set_incomplete_render' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'set_loader': None, # (!) real value is "<method 'set_loader' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'set_scene': None, # (!) real value is "<method 'set_scene' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'set_shader_generator': None, # (!) real value is "<method 'set_shader_generator' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'set_shader_model': None, # (!) real value is "<method 'set_shader_model' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'set_texture_quality_override': None, # (!) real value is "<method 'set_texture_quality_override' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'shader_generator': None, # (!) real value is "<attribute 'shader_generator' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'shader_model': None, # (!) real value is "<attribute 'shader_model' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'supports_2d_texture_array': None, # (!) real value is "<attribute 'supports_2d_texture_array' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'supports_3d_texture': None, # (!) real value is "<attribute 'supports_3d_texture' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'supports_basic_shaders': None, # (!) real value is "<attribute 'supports_basic_shaders' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'supports_buffer_texture': None, # (!) real value is "<attribute 'supports_buffer_texture' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'supports_compressed_texture': None, # (!) real value is "<attribute 'supports_compressed_texture' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'supports_compute_shaders': None, # (!) real value is "<attribute 'supports_compute_shaders' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'supports_cube_map': None, # (!) real value is "<attribute 'supports_cube_map' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'supports_cube_map_array': None, # (!) real value is "<attribute 'supports_cube_map_array' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'supports_depth_stencil': None, # (!) real value is "<attribute 'supports_depth_stencil' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'supports_depth_texture': None, # (!) real value is "<attribute 'supports_depth_texture' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'supports_dual_source_blending': None, # (!) real value is "<attribute 'supports_dual_source_blending' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'supports_generate_mipmap': None, # (!) real value is "<attribute 'supports_generate_mipmap' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'supports_geometry_instancing': None, # (!) real value is "<attribute 'supports_geometry_instancing' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'supports_geometry_shaders': None, # (!) real value is "<attribute 'supports_geometry_shaders' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'supports_glsl': None, # (!) real value is "<attribute 'supports_glsl' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'supports_hlsl': None, # (!) real value is "<attribute 'supports_hlsl' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'supports_indirect_draw': None, # (!) real value is "<attribute 'supports_indirect_draw' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'supports_luminance_texture': None, # (!) real value is "<attribute 'supports_luminance_texture' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'supports_multisample': None, # (!) real value is "<attribute 'supports_multisample' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'supports_occlusion_query': None, # (!) real value is "<attribute 'supports_occlusion_query' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'supports_sampler_objects': None, # (!) real value is "<attribute 'supports_sampler_objects' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'supports_shadow_filter': None, # (!) real value is "<attribute 'supports_shadow_filter' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'supports_stencil': None, # (!) real value is "<attribute 'supports_stencil' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'supports_tessellation_shaders': None, # (!) real value is "<attribute 'supports_tessellation_shaders' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'supports_tex_non_pow2': None, # (!) real value is "<attribute 'supports_tex_non_pow2' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'supports_texture_combine': None, # (!) real value is "<attribute 'supports_texture_combine' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'supports_texture_dot3': None, # (!) real value is "<attribute 'supports_texture_dot3' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'supports_texture_saved_result': None, # (!) real value is "<attribute 'supports_texture_saved_result' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'supports_texture_srgb': None, # (!) real value is "<attribute 'supports_texture_srgb' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'supports_timer_query': None, # (!) real value is "<attribute 'supports_timer_query' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'supports_two_sided_stencil': None, # (!) real value is "<attribute 'supports_two_sided_stencil' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'texture_quality_override': None, # (!) real value is "<attribute 'texture_quality_override' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'timer_queries_active': None, # (!) real value is "<attribute 'timer_queries_active' of 'panda3d.core.GraphicsStateGuardian' objects>"
        'valid': None, # (!) real value is "<attribute 'valid' of 'panda3d.core.GraphicsStateGuardian' objects>"
    }
    SM00 = 0
    SM11 = 1
    SM20 = 2
    SM2X = 3
    SM30 = 4
    SM40 = 5
    SM50 = 6
    SM51 = 7
    SM_00 = 0
    SM_11 = 1
    SM_20 = 2
    SM_2X = 3
    SM_30 = 4
    SM_40 = 5
    SM_50 = 6
    SM_51 = 7


