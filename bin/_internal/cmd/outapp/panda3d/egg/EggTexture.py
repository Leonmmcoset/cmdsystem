# encoding: utf-8
# module panda3d.egg
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\egg.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import panda3d.core as __panda3d_core


from .EggFilenameNode import EggFilenameNode

from .EggRenderMode import EggRenderMode

from .EggTransform import EggTransform

class EggTexture(EggFilenameNode, EggRenderMode, EggTransform):
    """
    /**
     * Defines a texture map that may be applied to geometry.
     */
    """
    def affectsPolygonAlpha(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        affects_polygon_alpha(EggTexture self)
        
        /**
         * Returns true if this texture's environment type or combine mode allows the
         * texture to have an effect on the polygon's alpha values, false otherwise.
         */
        """
        pass

    def affects_polygon_alpha(self, EggTexture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        affects_polygon_alpha(EggTexture self)
        
        /**
         * Returns true if this texture's environment type or combine mode allows the
         * texture to have an effect on the polygon's alpha values, false otherwise.
         */
        """
        pass

    def assign(self, const_EggTexture_self, const_EggTexture_copy): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        assign(const EggTexture self, const EggTexture copy)
        
        /**
         *
         */
        """
        pass

    def clearAlphaFileChannel(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_alpha_file_channel(const EggTexture self)
        
        /**
         * Removes the specification of a particular channel to use from the alpha-
         * file image.
         */
        """
        pass

    def clearAlphaFilename(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_alpha_filename(const EggTexture self)
        
        /**
         *
         */
        """
        pass

    def clearAlphaScale(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_alpha_scale(const EggTexture self)
        
        /**
         * Removes the alpha_scale from the texture and restores it to the default
         * value of 1.
         */
        """
        pass

    def clearAnisotropicDegree(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_anisotropic_degree(const EggTexture self)
        
        /**
         * Removes the specification of anisotropic filtering from the texture.
         */
        """
        pass

    def clearBorderColor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_border_color(const EggTexture self)
        
        /**
         *
         */
        """
        pass

    def clearColor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_color(const EggTexture self)
        
        /**
         *
         */
        """
        pass

    def clearLodBias(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_lod_bias(const EggTexture self)
        
        /**
         * Removes the specification of a maximum mipmap level from the texture.
         */
        """
        pass

    def clearMaxLod(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_max_lod(const EggTexture self)
        
        /**
         * Removes the specification of a maximum mipmap level from the texture.
         */
        """
        pass

    def clearMinLod(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_min_lod(const EggTexture self)
        
        /**
         * Removes the specification of a minimum mipmap level from the texture.
         */
        """
        pass

    def clearMultitexture(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_multitexture(const EggTexture self)
        
        /**
         * Resets the multitexture flags set by multitexture_over().  After this call,
         * get_multitexture() will return false, and get_multitexture_sort() will
         * return 0.
         */
        """
        pass

    def clearNumViews(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_num_views(const EggTexture self)
        
        /**
         * Removes the specification of the number of views for a 3-D multiview
         * texture.
         */
        """
        pass

    def clearPriority(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_priority(const EggTexture self)
        
        /**
         * Removes the specification of multitexture priority from the texture.  The
         * default priority value is 0.
         */
        """
        pass

    def clearRgbScale(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_rgb_scale(const EggTexture self)
        
        /**
         * Removes the rgb_scale from the texture and restores it to the default value
         * of 1.
         */
        """
        pass

    def clearStageName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_stage_name(const EggTexture self)
        
        /**
         * Removes the named TextureStage specification.
         */
        """
        pass

    def clearUvName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_uv_name(const EggTexture self)
        
        /**
         * Removes the restriction to a particular named set of texture coordinates
         * and restores the texture to using the default texture coordinates.
         */
        """
        pass

    def clear_alpha_filename(self, const_EggTexture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_alpha_filename(const EggTexture self)
        
        /**
         *
         */
        """
        pass

    def clear_alpha_file_channel(self, const_EggTexture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_alpha_file_channel(const EggTexture self)
        
        /**
         * Removes the specification of a particular channel to use from the alpha-
         * file image.
         */
        """
        pass

    def clear_alpha_scale(self, const_EggTexture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_alpha_scale(const EggTexture self)
        
        /**
         * Removes the alpha_scale from the texture and restores it to the default
         * value of 1.
         */
        """
        pass

    def clear_anisotropic_degree(self, const_EggTexture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_anisotropic_degree(const EggTexture self)
        
        /**
         * Removes the specification of anisotropic filtering from the texture.
         */
        """
        pass

    def clear_border_color(self, const_EggTexture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_border_color(const EggTexture self)
        
        /**
         *
         */
        """
        pass

    def clear_color(self, const_EggTexture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_color(const EggTexture self)
        
        /**
         *
         */
        """
        pass

    def clear_lod_bias(self, const_EggTexture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_lod_bias(const EggTexture self)
        
        /**
         * Removes the specification of a maximum mipmap level from the texture.
         */
        """
        pass

    def clear_max_lod(self, const_EggTexture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_max_lod(const EggTexture self)
        
        /**
         * Removes the specification of a maximum mipmap level from the texture.
         */
        """
        pass

    def clear_min_lod(self, const_EggTexture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_min_lod(const EggTexture self)
        
        /**
         * Removes the specification of a minimum mipmap level from the texture.
         */
        """
        pass

    def clear_multitexture(self, const_EggTexture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_multitexture(const EggTexture self)
        
        /**
         * Resets the multitexture flags set by multitexture_over().  After this call,
         * get_multitexture() will return false, and get_multitexture_sort() will
         * return 0.
         */
        """
        pass

    def clear_num_views(self, const_EggTexture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_num_views(const EggTexture self)
        
        /**
         * Removes the specification of the number of views for a 3-D multiview
         * texture.
         */
        """
        pass

    def clear_priority(self, const_EggTexture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_priority(const EggTexture self)
        
        /**
         * Removes the specification of multitexture priority from the texture.  The
         * default priority value is 0.
         */
        """
        pass

    def clear_rgb_scale(self, const_EggTexture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_rgb_scale(const EggTexture self)
        
        /**
         * Removes the rgb_scale from the texture and restores it to the default value
         * of 1.
         */
        """
        pass

    def clear_stage_name(self, const_EggTexture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_stage_name(const EggTexture self)
        
        /**
         * Removes the named TextureStage specification.
         */
        """
        pass

    def clear_uv_name(self, const_EggTexture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_uv_name(const EggTexture self)
        
        /**
         * Removes the restriction to a particular named set of texture coordinates
         * and restores the texture to using the default texture coordinates.
         */
        """
        pass

    def determineWrapU(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        determine_wrap_u(EggTexture self)
        
        /**
         * Determines the appropriate wrap in the U direction.  This is different from
         * get_wrap_u() in that if the U wrap is unspecified, it returns the overall
         * wrap value.
         */
        """
        pass

    def determineWrapV(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        determine_wrap_v(EggTexture self)
        
        /**
         * Determines the appropriate wrap in the V direction.  This is different from
         * get_wrap_v() in that if the V wrap is unspecified, it returns the overall
         * wrap value.
         */
        """
        pass

    def determineWrapW(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        determine_wrap_w(EggTexture self)
        
        /**
         * Determines the appropriate wrap in the W direction.  This is different from
         * get_wrap_w() in that if the W wrap is unspecified, it returns the overall
         * wrap value.
         */
        """
        pass

    def determine_wrap_u(self, EggTexture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        determine_wrap_u(EggTexture self)
        
        /**
         * Determines the appropriate wrap in the U direction.  This is different from
         * get_wrap_u() in that if the U wrap is unspecified, it returns the overall
         * wrap value.
         */
        """
        pass

    def determine_wrap_v(self, EggTexture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        determine_wrap_v(EggTexture self)
        
        /**
         * Determines the appropriate wrap in the V direction.  This is different from
         * get_wrap_v() in that if the V wrap is unspecified, it returns the overall
         * wrap value.
         */
        """
        pass

    def determine_wrap_w(self, EggTexture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        determine_wrap_w(EggTexture self)
        
        /**
         * Determines the appropriate wrap in the W direction.  This is different from
         * get_wrap_w() in that if the W wrap is unspecified, it returns the overall
         * wrap value.
         */
        """
        pass

    def getAlphaFileChannel(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_alpha_file_channel(EggTexture self)
        
        /**
         * Returns the particular channel that has been specified for the alpha-file
         * image, or 0 if no channel has been specified.  See
         * set_alpha_file_channel().
         */
        """
        pass

    def getAlphaFilename(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_alpha_filename(EggTexture self)
        
        /**
         * Returns the separate file assigned for the alpha channel.  It is an error
         * to call this unless has_alpha_filename() returns true.  See
         * set_alpha_filename().
         */
        """
        pass

    def getAlphaFullpath(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_alpha_fullpath(EggTexture self)
        
        /**
         * Returns the full pathname to the alpha file, if it is known; otherwise,
         * returns the same thing as get_alpha_filename().
         *
         * This function simply returns whatever was set by the last call to
         * set_alpha_fullpath().  This string is not written to the egg file; its main
         * purpose is to record the full path to the alpha filename if it is known,
         * for egg structures that are generated in-memory and then immediately
         * converted to a scene graph.
         */
        """
        pass

    def getAlphaScale(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_alpha_scale(EggTexture self)
        
        /**
         * Returns the alpha_scale value that has been specified for the texture, or 1
         * if no alpha_scale value has been specified.
         */
        """
        pass

    def getAnisotropicDegree(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_anisotropic_degree(EggTexture self)
        
        /**
         * Returns the anisotropic filtering degree that has been specified for this
         * texture, or 0 if nothing has been specified.
         */
        """
        pass

    def getBorderColor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_border_color(EggTexture self)
        
        /**
         * Returns the border color if one has been specified, or (0, 0, 0, 1)
         * otherwise.
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getColor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_color(EggTexture self)
        
        /**
         * Returns the blend color if one has been specified, or (0, 0, 0, 1)
         * otherwise.
         */
        """
        pass

    def getCombineMode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_combine_mode(EggTexture self, int channel)
        
        /**
         *
         */
        """
        pass

    def getCombineOperand(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_combine_operand(EggTexture self, int channel, int n)
        
        /**
         *
         */
        """
        pass

    def getCombineSource(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_combine_source(EggTexture self, int channel, int n)
        
        /**
         *
         */
        """
        pass

    def getCompressionMode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_compression_mode(EggTexture self)
        
        /**
         *
         */
        """
        pass

    def getEnvType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_env_type(EggTexture self)
        
        /**
         *
         */
        """
        pass

    def getFormat(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_format(EggTexture self)
        
        /**
         *
         */
        """
        pass

    def getLodBias(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_lod_bias(EggTexture self)
        
        /**
         * Returns the maximum mipmap level that has been specified for this texture.
         */
        """
        pass

    def getMagfilter(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_magfilter(EggTexture self)
        
        /**
         *
         */
        """
        pass

    def getMaxLod(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_max_lod(EggTexture self)
        
        /**
         * Returns the maximum mipmap level that has been specified for this texture.
         */
        """
        pass

    def getMinfilter(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_minfilter(EggTexture self)
        
        /**
         *
         */
        """
        pass

    def getMinLod(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_min_lod(EggTexture self)
        
        /**
         * Returns the minimum mipmap level that has been specified for this texture.
         */
        """
        pass

    def getMultitextureSort(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_multitexture_sort(EggTexture self)
        
        /**
         * Returns an integer that represents the depth to which this texture is
         * layered on all other textures in the egg file.  In general, if texture A is
         * layered over texture B, then sort(A) > sort(B).  If texture A is never
         * layered over any other texture, then sort(A) == 0.  More than that is
         * difficult to guarantee.
         */
        """
        pass

    def getMultiview(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_multiview(EggTexture self)
        
        /**
         * Returns the current setting of the multiview flag.  See set_multiview().
         */
        """
        pass

    def getNumViews(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_views(EggTexture self)
        
        /**
         * Returns the specified number of views specified for the 3-D multiview
         * texture.  See set_num_views().
         */
        """
        pass

    def getPriority(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_priority(EggTexture self)
        
        /**
         * Returns the multitexture importance value that has been specified for the
         * texture, or 0 if no priority value has been specified.
         */
        """
        pass

    def getQualityLevel(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_quality_level(EggTexture self)
        
        /**
         *
         */
        """
        pass

    def getReadMipmaps(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_read_mipmaps(EggTexture self)
        
        /**
         * Returns the current setting of the read_mipmaps flag.  See
         * set_read_mipmaps().
         */
        """
        pass

    def getRgbScale(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_rgb_scale(EggTexture self)
        
        /**
         * Returns the rgb_scale value that has been specified for the texture, or 1
         * if no rgb_scale value has been specified.
         */
        """
        pass

    def getSavedResult(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_saved_result(EggTexture self)
        
        /**
         * Returns the current setting of the saved_result flag.  See
         * set_saved_result().
         */
        """
        pass

    def getStageName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_stage_name(EggTexture self)
        
        /**
         * Returns the stage name that has been specified for this texture, or the
         * tref name if no texture stage has explicitly been specified.
         */
        """
        pass

    def getTexGen(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_tex_gen(EggTexture self)
        
        /**
         *
         */
        """
        pass

    def getTextureType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_texture_type(EggTexture self)
        
        /**
         *
         */
        """
        pass

    def getUvName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_uv_name(EggTexture self)
        
        /**
         * Returns the texcoord name that has been specified for this texture, or the
         * empty string if no texcoord name has explicitly been specified.
         */
        """
        pass

    def getWrapMode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_wrap_mode(EggTexture self)
        
        /**
         *
         */
        """
        pass

    def getWrapU(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_wrap_u(EggTexture self)
        
        /**
         * Returns the amount specified for U wrap.  This may be unspecified, even if
         * there is an overall wrap value.
         */
        """
        pass

    def getWrapV(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_wrap_v(EggTexture self)
        
        /**
         * Returns the amount specified for V wrap.  This may be unspecified, even if
         * there is an overall wrap value.
         */
        """
        pass

    def getWrapW(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_wrap_w(EggTexture self)
        
        /**
         * Returns the amount specified for W wrap.  This may be unspecified, even if
         * there is an overall wrap value.
         */
        """
        pass

    def get_alpha_filename(self, EggTexture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_alpha_filename(EggTexture self)
        
        /**
         * Returns the separate file assigned for the alpha channel.  It is an error
         * to call this unless has_alpha_filename() returns true.  See
         * set_alpha_filename().
         */
        """
        pass

    def get_alpha_file_channel(self, EggTexture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_alpha_file_channel(EggTexture self)
        
        /**
         * Returns the particular channel that has been specified for the alpha-file
         * image, or 0 if no channel has been specified.  See
         * set_alpha_file_channel().
         */
        """
        pass

    def get_alpha_fullpath(self, EggTexture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_alpha_fullpath(EggTexture self)
        
        /**
         * Returns the full pathname to the alpha file, if it is known; otherwise,
         * returns the same thing as get_alpha_filename().
         *
         * This function simply returns whatever was set by the last call to
         * set_alpha_fullpath().  This string is not written to the egg file; its main
         * purpose is to record the full path to the alpha filename if it is known,
         * for egg structures that are generated in-memory and then immediately
         * converted to a scene graph.
         */
        """
        pass

    def get_alpha_scale(self, EggTexture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_alpha_scale(EggTexture self)
        
        /**
         * Returns the alpha_scale value that has been specified for the texture, or 1
         * if no alpha_scale value has been specified.
         */
        """
        pass

    def get_anisotropic_degree(self, EggTexture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_anisotropic_degree(EggTexture self)
        
        /**
         * Returns the anisotropic filtering degree that has been specified for this
         * texture, or 0 if nothing has been specified.
         */
        """
        pass

    def get_border_color(self, EggTexture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_border_color(EggTexture self)
        
        /**
         * Returns the border color if one has been specified, or (0, 0, 0, 1)
         * otherwise.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_color(self, EggTexture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_color(EggTexture self)
        
        /**
         * Returns the blend color if one has been specified, or (0, 0, 0, 1)
         * otherwise.
         */
        """
        pass

    def get_combine_mode(self, EggTexture_self, int_channel): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_combine_mode(EggTexture self, int channel)
        
        /**
         *
         */
        """
        pass

    def get_combine_operand(self, EggTexture_self, int_channel, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_combine_operand(EggTexture self, int channel, int n)
        
        /**
         *
         */
        """
        pass

    def get_combine_source(self, EggTexture_self, int_channel, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_combine_source(EggTexture self, int channel, int n)
        
        /**
         *
         */
        """
        pass

    def get_compression_mode(self, EggTexture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_compression_mode(EggTexture self)
        
        /**
         *
         */
        """
        pass

    def get_env_type(self, EggTexture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_env_type(EggTexture self)
        
        /**
         *
         */
        """
        pass

    def get_format(self, EggTexture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_format(EggTexture self)
        
        /**
         *
         */
        """
        pass

    def get_lod_bias(self, EggTexture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_lod_bias(EggTexture self)
        
        /**
         * Returns the maximum mipmap level that has been specified for this texture.
         */
        """
        pass

    def get_magfilter(self, EggTexture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_magfilter(EggTexture self)
        
        /**
         *
         */
        """
        pass

    def get_max_lod(self, EggTexture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_max_lod(EggTexture self)
        
        /**
         * Returns the maximum mipmap level that has been specified for this texture.
         */
        """
        pass

    def get_minfilter(self, EggTexture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_minfilter(EggTexture self)
        
        /**
         *
         */
        """
        pass

    def get_min_lod(self, EggTexture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_min_lod(EggTexture self)
        
        /**
         * Returns the minimum mipmap level that has been specified for this texture.
         */
        """
        pass

    def get_multitexture_sort(self, EggTexture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_multitexture_sort(EggTexture self)
        
        /**
         * Returns an integer that represents the depth to which this texture is
         * layered on all other textures in the egg file.  In general, if texture A is
         * layered over texture B, then sort(A) > sort(B).  If texture A is never
         * layered over any other texture, then sort(A) == 0.  More than that is
         * difficult to guarantee.
         */
        """
        pass

    def get_multiview(self, EggTexture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_multiview(EggTexture self)
        
        /**
         * Returns the current setting of the multiview flag.  See set_multiview().
         */
        """
        pass

    def get_num_views(self, EggTexture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_views(EggTexture self)
        
        /**
         * Returns the specified number of views specified for the 3-D multiview
         * texture.  See set_num_views().
         */
        """
        pass

    def get_priority(self, EggTexture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_priority(EggTexture self)
        
        /**
         * Returns the multitexture importance value that has been specified for the
         * texture, or 0 if no priority value has been specified.
         */
        """
        pass

    def get_quality_level(self, EggTexture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_quality_level(EggTexture self)
        
        /**
         *
         */
        """
        pass

    def get_read_mipmaps(self, EggTexture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_read_mipmaps(EggTexture self)
        
        /**
         * Returns the current setting of the read_mipmaps flag.  See
         * set_read_mipmaps().
         */
        """
        pass

    def get_rgb_scale(self, EggTexture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_rgb_scale(EggTexture self)
        
        /**
         * Returns the rgb_scale value that has been specified for the texture, or 1
         * if no rgb_scale value has been specified.
         */
        """
        pass

    def get_saved_result(self, EggTexture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_saved_result(EggTexture self)
        
        /**
         * Returns the current setting of the saved_result flag.  See
         * set_saved_result().
         */
        """
        pass

    def get_stage_name(self, EggTexture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_stage_name(EggTexture self)
        
        /**
         * Returns the stage name that has been specified for this texture, or the
         * tref name if no texture stage has explicitly been specified.
         */
        """
        pass

    def get_texture_type(self, EggTexture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_texture_type(EggTexture self)
        
        /**
         *
         */
        """
        pass

    def get_tex_gen(self, EggTexture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_tex_gen(EggTexture self)
        
        /**
         *
         */
        """
        pass

    def get_uv_name(self, EggTexture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_uv_name(EggTexture self)
        
        /**
         * Returns the texcoord name that has been specified for this texture, or the
         * empty string if no texcoord name has explicitly been specified.
         */
        """
        pass

    def get_wrap_mode(self, EggTexture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_wrap_mode(EggTexture self)
        
        /**
         *
         */
        """
        pass

    def get_wrap_u(self, EggTexture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_wrap_u(EggTexture self)
        
        /**
         * Returns the amount specified for U wrap.  This may be unspecified, even if
         * there is an overall wrap value.
         */
        """
        pass

    def get_wrap_v(self, EggTexture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_wrap_v(EggTexture self)
        
        /**
         * Returns the amount specified for V wrap.  This may be unspecified, even if
         * there is an overall wrap value.
         */
        """
        pass

    def get_wrap_w(self, EggTexture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_wrap_w(EggTexture self)
        
        /**
         * Returns the amount specified for W wrap.  This may be unspecified, even if
         * there is an overall wrap value.
         */
        """
        pass

    def hasAlphaChannel(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_alpha_channel(EggTexture self, int num_components)
        
        /**
         * Given the number of color components (channels) in the image file as
         * actually read from the disk, return true if this texture seems to have an
         * alpha channel or not.  This depends on the EggTexture's format as well as
         * the number of channels.
         */
        """
        pass

    def hasAlphaFileChannel(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_alpha_file_channel(EggTexture self)
        
        /**
         * Returns true if a particular channel has been specified for the alpha-file
         * image, false otherwise.
         */
        """
        pass

    def hasAlphaFilename(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_alpha_filename(EggTexture self)
        
        /**
         * Returns true if a separate file for the alpha component has been applied,
         * false otherwise.  See set_alpha_filename().
         */
        """
        pass

    def hasAlphaScale(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_alpha_scale(EggTexture self)
        
        /**
         * Returns true if an alpha_scale has been specified for the texture, false
         * otherwise.
         */
        """
        pass

    def hasAnisotropicDegree(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_anisotropic_degree(EggTexture self)
        
        /**
         * Returns true if a value for the anisotropic filtering degree has been
         * specified for this texture, false otherwise.
         */
        """
        pass

    def hasBorderColor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_border_color(EggTexture self)
        
        /**
         * Returns true if a border color has been specified for the texture.
         */
        """
        pass

    def hasColor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_color(EggTexture self)
        
        /**
         * Returns true if a blend color has been specified for the texture.
         */
        """
        pass

    def hasLodBias(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_lod_bias(EggTexture self)
        
        /**
         * Returns true if a value for the maximum mipmap level has been specified for
         * this texture, false otherwise.
         */
        """
        pass

    def hasMaxLod(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_max_lod(EggTexture self)
        
        /**
         * Returns true if a value for the maximum mipmap level has been specified for
         * this texture, false otherwise.
         */
        """
        pass

    def hasMinLod(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_min_lod(EggTexture self)
        
        /**
         * Returns true if a value for the minimum mipmap level has been specified for
         * this texture, false otherwise.
         */
        """
        pass

    def hasNumViews(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_num_views(EggTexture self)
        
        /**
         * Returns true if the number of views has been specified for the 3-D
         * multiview texture, false otherwise.
         */
        """
        pass

    def hasPriority(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_priority(EggTexture self)
        
        /**
         * Returns true if a priority value for multitexture importance has been
         * specified for the texture, false otherwise.
         */
        """
        pass

    def hasRgbScale(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_rgb_scale(EggTexture self)
        
        /**
         * Returns true if an rgb_scale has been specified for the texture, false
         * otherwise.
         */
        """
        pass

    def hasStageName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_stage_name(EggTexture self)
        
        /**
         * Returns true if a stage name has been explicitly specified for this
         * texture, false otherwise.
         */
        """
        pass

    def hasUvName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_uv_name(EggTexture self)
        
        /**
         * Returns true if a texcoord name has been explicitly specified for this
         * texture, false otherwise.
         */
        """
        pass

    def has_alpha_channel(self, EggTexture_self, int_num_components): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_alpha_channel(EggTexture self, int num_components)
        
        /**
         * Given the number of color components (channels) in the image file as
         * actually read from the disk, return true if this texture seems to have an
         * alpha channel or not.  This depends on the EggTexture's format as well as
         * the number of channels.
         */
        """
        pass

    def has_alpha_filename(self, EggTexture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_alpha_filename(EggTexture self)
        
        /**
         * Returns true if a separate file for the alpha component has been applied,
         * false otherwise.  See set_alpha_filename().
         */
        """
        pass

    def has_alpha_file_channel(self, EggTexture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_alpha_file_channel(EggTexture self)
        
        /**
         * Returns true if a particular channel has been specified for the alpha-file
         * image, false otherwise.
         */
        """
        pass

    def has_alpha_scale(self, EggTexture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_alpha_scale(EggTexture self)
        
        /**
         * Returns true if an alpha_scale has been specified for the texture, false
         * otherwise.
         */
        """
        pass

    def has_anisotropic_degree(self, EggTexture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_anisotropic_degree(EggTexture self)
        
        /**
         * Returns true if a value for the anisotropic filtering degree has been
         * specified for this texture, false otherwise.
         */
        """
        pass

    def has_border_color(self, EggTexture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_border_color(EggTexture self)
        
        /**
         * Returns true if a border color has been specified for the texture.
         */
        """
        pass

    def has_color(self, EggTexture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_color(EggTexture self)
        
        /**
         * Returns true if a blend color has been specified for the texture.
         */
        """
        pass

    def has_lod_bias(self, EggTexture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_lod_bias(EggTexture self)
        
        /**
         * Returns true if a value for the maximum mipmap level has been specified for
         * this texture, false otherwise.
         */
        """
        pass

    def has_max_lod(self, EggTexture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_max_lod(EggTexture self)
        
        /**
         * Returns true if a value for the maximum mipmap level has been specified for
         * this texture, false otherwise.
         */
        """
        pass

    def has_min_lod(self, EggTexture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_min_lod(EggTexture self)
        
        /**
         * Returns true if a value for the minimum mipmap level has been specified for
         * this texture, false otherwise.
         */
        """
        pass

    def has_num_views(self, EggTexture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_num_views(EggTexture self)
        
        /**
         * Returns true if the number of views has been specified for the 3-D
         * multiview texture, false otherwise.
         */
        """
        pass

    def has_priority(self, EggTexture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_priority(EggTexture self)
        
        /**
         * Returns true if a priority value for multitexture importance has been
         * specified for the texture, false otherwise.
         */
        """
        pass

    def has_rgb_scale(self, EggTexture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_rgb_scale(EggTexture self)
        
        /**
         * Returns true if an rgb_scale has been specified for the texture, false
         * otherwise.
         */
        """
        pass

    def has_stage_name(self, EggTexture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_stage_name(EggTexture self)
        
        /**
         * Returns true if a stage name has been explicitly specified for this
         * texture, false otherwise.
         */
        """
        pass

    def has_uv_name(self, EggTexture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_uv_name(EggTexture self)
        
        /**
         * Returns true if a texcoord name has been explicitly specified for this
         * texture, false otherwise.
         */
        """
        pass

    def isEquivalentTo(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_equivalent_to(EggTexture self, const EggTexture other, int eq)
        
        /**
         * Returns true if the two textures are equivalent in all relevant properties
         * (according to eq), false otherwise.
         *
         * The Equivalence parameter, eq, should be set to the bitwise OR of the
         * following properties, according to what you consider relevant:
         *
         * EggTexture::E_basename: The basename part of the texture filename, without
         * the directory prefix *or* the filename extension.
         *
         * EggTexture::E_extension: The extension part of the texture filename.
         *
         * EggTexture::E_dirname: The directory prefix of the texture filename.
         *
         * EggTexture::E_complete_filename: The union of the above three; that is, the
         * complete filename, with directory, basename, and extension.
         *
         * EggTexture::E_transform: The texture matrix.
         *
         * EggTexture::E_attributes: All remaining texture attributes (mode, mipmap,
         * etc.) except TRef name.
         *
         * EggTexture::E_tref_name: The TRef name.
         */
        """
        pass

    def is_equivalent_to(self, EggTexture_self, const_EggTexture_other, int_eq): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_equivalent_to(EggTexture self, const EggTexture other, int eq)
        
        /**
         * Returns true if the two textures are equivalent in all relevant properties
         * (according to eq), false otherwise.
         *
         * The Equivalence parameter, eq, should be set to the bitwise OR of the
         * following properties, according to what you consider relevant:
         *
         * EggTexture::E_basename: The basename part of the texture filename, without
         * the directory prefix *or* the filename extension.
         *
         * EggTexture::E_extension: The extension part of the texture filename.
         *
         * EggTexture::E_dirname: The directory prefix of the texture filename.
         *
         * EggTexture::E_complete_filename: The union of the above three; that is, the
         * complete filename, with directory, basename, and extension.
         *
         * EggTexture::E_transform: The texture matrix.
         *
         * EggTexture::E_attributes: All remaining texture attributes (mode, mipmap,
         * etc.) except TRef name.
         *
         * EggTexture::E_tref_name: The TRef name.
         */
        """
        pass

    def multitextureOver(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        multitexture_over(const EggTexture self, EggTexture other)
        
        /**
         * Indicates that this texture should be layered on top of the other texture.
         * This will guarantee that this->get_multitexture_sort() >
         * other->get_multitexture_sort(), at least until clear_multitexture() is
         * called on either one.
         *
         * The return value is true if successful, or false if there is a failure
         * because the other texture was already layered on top of this one (or there
         * is a three- or more-way cycle).
         */
        """
        pass

    def multitexture_over(self, const_EggTexture_self, EggTexture_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        multitexture_over(const EggTexture self, EggTexture other)
        
        /**
         * Indicates that this texture should be layered on top of the other texture.
         * This will guarantee that this->get_multitexture_sort() >
         * other->get_multitexture_sort(), at least until clear_multitexture() is
         * called on either one.
         *
         * The return value is true if successful, or false if there is a failure
         * because the other texture was already layered on top of this one (or there
         * is a three- or more-way cycle).
         */
        """
        pass

    def setAlphaFileChannel(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_alpha_file_channel(const EggTexture self, int alpha_file_channel)
        
        /**
         * If a separate alpha-file is specified, this indicates which channel number
         * should be extracted from this file to derive the alpha channel for the
         * final image.  The default is 0, which means the grayscale combination of r,
         * g, b.  Otherwise, this should be the 1-based channel number, for instance
         * 1, 2, or 3 for r, g, or b, respectively, or 4 for the alpha channel of a
         * four-component image.
         */
        """
        pass

    def setAlphaFilename(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_alpha_filename(const EggTexture self, const Filename filename)
        
        /**
         * Specifies a separate file that will be loaded in with the 1- or 3-component
         * texture and applied as the alpha channel.  This is useful when loading
         * textures from file formats that do not support alpha, for instance jpg.
         */
        """
        pass

    def setAlphaFullpath(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_alpha_fullpath(const EggTexture self, const Filename fullpath)
        
        /**
         * Records the full pathname to the file, for the benefit of
         * get_alpha_fullpath().
         */
        """
        pass

    def setAlphaScale(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_alpha_scale(const EggTexture self, int alpha_scale)
        
        /**
         * Sets an additional factor that will scale the alpha component after the
         * texture has been applied.  This is used only when a combine mode is in
         * effect.
         *
         * The only legal values are 1, 2, or 4.
         */
        """
        pass

    def setAnisotropicDegree(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_anisotropic_degree(const EggTexture self, int anisotropic_degree)
        
        /**
         * Sets the degree of anisotropic filtering for this texture.  1 is off;
         * higher levels indicate filtering in effect.
         */
        """
        pass

    def setBorderColor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_border_color(const EggTexture self, const LVecBase4f border_color)
        
        /**
         *
         */
        """
        pass

    def setColor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_color(const EggTexture self, const LVecBase4f color)
        
        /**
         *
         */
        """
        pass

    def setCombineMode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_combine_mode(const EggTexture self, int channel, int cm)
        
        /**
         *
         */
        """
        pass

    def setCombineOperand(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_combine_operand(const EggTexture self, int channel, int n, int co)
        
        /**
         *
         */
        """
        pass

    def setCombineSource(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_combine_source(const EggTexture self, int channel, int n, int cs)
        
        /**
         *
         */
        """
        pass

    def setCompressionMode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_compression_mode(const EggTexture self, int mode)
        
        /**
         *
         */
        """
        pass

    def setEnvType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_env_type(const EggTexture self, int type)
        
        /**
         *
         */
        """
        pass

    def setFormat(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_format(const EggTexture self, int format)
        
        /**
         *
         */
        """
        pass

    def setLodBias(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_lod_bias(const EggTexture self, double lod_bias)
        
        /**
         * Sets the mipmap level bias that is added to the mipmap level to be sampled.
         */
        """
        pass

    def setMagfilter(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_magfilter(const EggTexture self, int type)
        
        /**
         *
         */
        """
        pass

    def setMaxLod(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_max_lod(const EggTexture self, double max_lod)
        
        /**
         * Sets the maximum mipmap level that may be sampled.
         */
        """
        pass

    def setMinfilter(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_minfilter(const EggTexture self, int type)
        
        /**
         *
         */
        """
        pass

    def setMinLod(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_min_lod(const EggTexture self, double min_lod)
        
        /**
         * Sets the minimum mipmap level that may be sampled.
         */
        """
        pass

    def setMultiview(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_multiview(const EggTexture self, bool multiview)
        
        /**
         * Sets the multiview flag.
         *
         * If multiview is true, the filename should contain a hash mark ('#'), which
         * will be filled in with the view number; and a multiview texture will be
         * defined with a series of images, one for each view.
         *
         * A multiview texture is most often used for stereo textures, but other uses
         * are also possible, such as for texture animation.
         */
        """
        pass

    def setNumViews(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_num_views(const EggTexture self, int num_views)
        
        /**
         * When loading a 3-D multiview texture, this parameter is necessary to
         * specify how many views will be expected.  The z size is determined
         * implicitly from the number of images loaded.
         */
        """
        pass

    def setPriority(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_priority(const EggTexture self, int priority)
        
        /**
         * Sets the importance of this texture with respect to other textures also
         * applied on the same geometry.  This is only meaningful in the presence of
         * multitexturing.
         */
        """
        pass

    def setQualityLevel(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_quality_level(const EggTexture self, int quality_level)
        
        /**
         *
         */
        """
        pass

    def setReadMipmaps(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_read_mipmaps(const EggTexture self, bool read_mipmaps)
        
        /**
         * Sets the read_mipmaps flag.
         *
         * If read_mipmaps is true, the filename should contain a hash mark ('#'),
         * which will be filled in with the mipmap level number; and the texture will
         * be defined with a series of images, one for each mipmap level.
         *
         * If the filename is of a type that already requires a hash mark, such as a
         * cube map or a 3-d texture, then the filename should now require two hash
         * marks, and the first one indicates the mipmap level number, while the
         * second indicates the face number or 3-d level number.
         */
        """
        pass

    def setRgbScale(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_rgb_scale(const EggTexture self, int rgb_scale)
        
        /**
         * Sets an additional factor that will scale all three r, g, b components
         * after the texture has been applied.  This is used only when a combine mode
         * is in effect.
         *
         * The only legal values are 1, 2, or 4.
         */
        """
        pass

    def setSavedResult(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_saved_result(const EggTexture self, bool saved_result)
        
        /**
         * Sets the saved_result flag.  When this is true, the output of this stage is
         * not part of the normal pipeline--that is, it will not be supplied as the
         * "previous" source for the next texture stage--but it will instead be
         * supplied as the "last_saved_result" source for any future stages, until the
         * next TextureStage with a saved_result set true is encountered.
         *
         * This can be used to reuse the results of this texture stage as input to
         * more than one stage later in the pipeline.
         *
         * The last texture in the pipeline (the one with the highest sort value)
         * should not have this flag set.
         */
        """
        pass

    def setStageName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_stage_name(const EggTexture self, str stage_name)
        
        /**
         * Specifies the particular TextureStage this texture will be rendered on by
         * name.  If this is omitted, the texture will be rendered on the default
         * TextureStage, unless some other stage-specific property is specificied, in
         * which case the texture will be rendered on a TextureStage with the same
         * name as the tref.  This is in support of multitexturing.
         *
         * Each different TextureStage in the world must be uniquely named.
         */
        """
        pass

    def setTexGen(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_tex_gen(const EggTexture self, int tex_gen)
        
        /**
         *
         */
        """
        pass

    def setTextureType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_texture_type(const EggTexture self, int texture_type)
        
        /**
         *
         */
        """
        pass

    def setUvName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_uv_name(const EggTexture self, str uv_name)
        
        /**
         * Specifies the named set of texture coordinates that this texture will use
         * when it is applied to geometry.  Geometry may have multiple sets of texture
         * coordinates defined, by name.
         *
         * If this is not specified for a particular texture, the default set of
         * texture coordinates will be used.
         */
        """
        pass

    def setWrapMode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_wrap_mode(const EggTexture self, int mode)
        
        /**
         *
         */
        """
        pass

    def setWrapU(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_wrap_u(const EggTexture self, int mode)
        
        /**
         *
         */
        """
        pass

    def setWrapV(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_wrap_v(const EggTexture self, int mode)
        
        /**
         *
         */
        """
        pass

    def setWrapW(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_wrap_w(const EggTexture self, int mode)
        
        /**
         *
         */
        """
        pass

    def set_alpha_filename(self, const_EggTexture_self, const_Filename_filename): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_alpha_filename(const EggTexture self, const Filename filename)
        
        /**
         * Specifies a separate file that will be loaded in with the 1- or 3-component
         * texture and applied as the alpha channel.  This is useful when loading
         * textures from file formats that do not support alpha, for instance jpg.
         */
        """
        pass

    def set_alpha_file_channel(self, const_EggTexture_self, int_alpha_file_channel): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_alpha_file_channel(const EggTexture self, int alpha_file_channel)
        
        /**
         * If a separate alpha-file is specified, this indicates which channel number
         * should be extracted from this file to derive the alpha channel for the
         * final image.  The default is 0, which means the grayscale combination of r,
         * g, b.  Otherwise, this should be the 1-based channel number, for instance
         * 1, 2, or 3 for r, g, or b, respectively, or 4 for the alpha channel of a
         * four-component image.
         */
        """
        pass

    def set_alpha_fullpath(self, const_EggTexture_self, const_Filename_fullpath): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_alpha_fullpath(const EggTexture self, const Filename fullpath)
        
        /**
         * Records the full pathname to the file, for the benefit of
         * get_alpha_fullpath().
         */
        """
        pass

    def set_alpha_scale(self, const_EggTexture_self, int_alpha_scale): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_alpha_scale(const EggTexture self, int alpha_scale)
        
        /**
         * Sets an additional factor that will scale the alpha component after the
         * texture has been applied.  This is used only when a combine mode is in
         * effect.
         *
         * The only legal values are 1, 2, or 4.
         */
        """
        pass

    def set_anisotropic_degree(self, const_EggTexture_self, int_anisotropic_degree): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_anisotropic_degree(const EggTexture self, int anisotropic_degree)
        
        /**
         * Sets the degree of anisotropic filtering for this texture.  1 is off;
         * higher levels indicate filtering in effect.
         */
        """
        pass

    def set_border_color(self, const_EggTexture_self, const_LVecBase4f_border_color): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_border_color(const EggTexture self, const LVecBase4f border_color)
        
        /**
         *
         */
        """
        pass

    def set_color(self, const_EggTexture_self, const_LVecBase4f_color): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_color(const EggTexture self, const LVecBase4f color)
        
        /**
         *
         */
        """
        pass

    def set_combine_mode(self, const_EggTexture_self, int_channel, int_cm): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_combine_mode(const EggTexture self, int channel, int cm)
        
        /**
         *
         */
        """
        pass

    def set_combine_operand(self, const_EggTexture_self, int_channel, int_n, int_co): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_combine_operand(const EggTexture self, int channel, int n, int co)
        
        /**
         *
         */
        """
        pass

    def set_combine_source(self, const_EggTexture_self, int_channel, int_n, int_cs): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_combine_source(const EggTexture self, int channel, int n, int cs)
        
        /**
         *
         */
        """
        pass

    def set_compression_mode(self, const_EggTexture_self, int_mode): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_compression_mode(const EggTexture self, int mode)
        
        /**
         *
         */
        """
        pass

    def set_env_type(self, const_EggTexture_self, int_type): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_env_type(const EggTexture self, int type)
        
        /**
         *
         */
        """
        pass

    def set_format(self, const_EggTexture_self, int_format): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_format(const EggTexture self, int format)
        
        /**
         *
         */
        """
        pass

    def set_lod_bias(self, const_EggTexture_self, double_lod_bias): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_lod_bias(const EggTexture self, double lod_bias)
        
        /**
         * Sets the mipmap level bias that is added to the mipmap level to be sampled.
         */
        """
        pass

    def set_magfilter(self, const_EggTexture_self, int_type): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_magfilter(const EggTexture self, int type)
        
        /**
         *
         */
        """
        pass

    def set_max_lod(self, const_EggTexture_self, double_max_lod): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_max_lod(const EggTexture self, double max_lod)
        
        /**
         * Sets the maximum mipmap level that may be sampled.
         */
        """
        pass

    def set_minfilter(self, const_EggTexture_self, int_type): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_minfilter(const EggTexture self, int type)
        
        /**
         *
         */
        """
        pass

    def set_min_lod(self, const_EggTexture_self, double_min_lod): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_min_lod(const EggTexture self, double min_lod)
        
        /**
         * Sets the minimum mipmap level that may be sampled.
         */
        """
        pass

    def set_multiview(self, const_EggTexture_self, bool_multiview): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_multiview(const EggTexture self, bool multiview)
        
        /**
         * Sets the multiview flag.
         *
         * If multiview is true, the filename should contain a hash mark ('#'), which
         * will be filled in with the view number; and a multiview texture will be
         * defined with a series of images, one for each view.
         *
         * A multiview texture is most often used for stereo textures, but other uses
         * are also possible, such as for texture animation.
         */
        """
        pass

    def set_num_views(self, const_EggTexture_self, int_num_views): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_num_views(const EggTexture self, int num_views)
        
        /**
         * When loading a 3-D multiview texture, this parameter is necessary to
         * specify how many views will be expected.  The z size is determined
         * implicitly from the number of images loaded.
         */
        """
        pass

    def set_priority(self, const_EggTexture_self, int_priority): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_priority(const EggTexture self, int priority)
        
        /**
         * Sets the importance of this texture with respect to other textures also
         * applied on the same geometry.  This is only meaningful in the presence of
         * multitexturing.
         */
        """
        pass

    def set_quality_level(self, const_EggTexture_self, int_quality_level): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_quality_level(const EggTexture self, int quality_level)
        
        /**
         *
         */
        """
        pass

    def set_read_mipmaps(self, const_EggTexture_self, bool_read_mipmaps): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_read_mipmaps(const EggTexture self, bool read_mipmaps)
        
        /**
         * Sets the read_mipmaps flag.
         *
         * If read_mipmaps is true, the filename should contain a hash mark ('#'),
         * which will be filled in with the mipmap level number; and the texture will
         * be defined with a series of images, one for each mipmap level.
         *
         * If the filename is of a type that already requires a hash mark, such as a
         * cube map or a 3-d texture, then the filename should now require two hash
         * marks, and the first one indicates the mipmap level number, while the
         * second indicates the face number or 3-d level number.
         */
        """
        pass

    def set_rgb_scale(self, const_EggTexture_self, int_rgb_scale): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_rgb_scale(const EggTexture self, int rgb_scale)
        
        /**
         * Sets an additional factor that will scale all three r, g, b components
         * after the texture has been applied.  This is used only when a combine mode
         * is in effect.
         *
         * The only legal values are 1, 2, or 4.
         */
        """
        pass

    def set_saved_result(self, const_EggTexture_self, bool_saved_result): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_saved_result(const EggTexture self, bool saved_result)
        
        /**
         * Sets the saved_result flag.  When this is true, the output of this stage is
         * not part of the normal pipeline--that is, it will not be supplied as the
         * "previous" source for the next texture stage--but it will instead be
         * supplied as the "last_saved_result" source for any future stages, until the
         * next TextureStage with a saved_result set true is encountered.
         *
         * This can be used to reuse the results of this texture stage as input to
         * more than one stage later in the pipeline.
         *
         * The last texture in the pipeline (the one with the highest sort value)
         * should not have this flag set.
         */
        """
        pass

    def set_stage_name(self, const_EggTexture_self, str_stage_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_stage_name(const EggTexture self, str stage_name)
        
        /**
         * Specifies the particular TextureStage this texture will be rendered on by
         * name.  If this is omitted, the texture will be rendered on the default
         * TextureStage, unless some other stage-specific property is specificied, in
         * which case the texture will be rendered on a TextureStage with the same
         * name as the tref.  This is in support of multitexturing.
         *
         * Each different TextureStage in the world must be uniquely named.
         */
        """
        pass

    def set_texture_type(self, const_EggTexture_self, int_texture_type): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_texture_type(const EggTexture self, int texture_type)
        
        /**
         *
         */
        """
        pass

    def set_tex_gen(self, const_EggTexture_self, int_tex_gen): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_tex_gen(const EggTexture self, int tex_gen)
        
        /**
         *
         */
        """
        pass

    def set_uv_name(self, const_EggTexture_self, str_uv_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_uv_name(const EggTexture self, str uv_name)
        
        /**
         * Specifies the named set of texture coordinates that this texture will use
         * when it is applied to geometry.  Geometry may have multiple sets of texture
         * coordinates defined, by name.
         *
         * If this is not specified for a particular texture, the default set of
         * texture coordinates will be used.
         */
        """
        pass

    def set_wrap_mode(self, const_EggTexture_self, int_mode): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_wrap_mode(const EggTexture self, int mode)
        
        /**
         *
         */
        """
        pass

    def set_wrap_u(self, const_EggTexture_self, int_mode): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_wrap_u(const EggTexture self, int mode)
        
        /**
         *
         */
        """
        pass

    def set_wrap_v(self, const_EggTexture_self, int_mode): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_wrap_v(const EggTexture self, int mode)
        
        /**
         *
         */
        """
        pass

    def set_wrap_w(self, const_EggTexture_self, int_mode): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_wrap_w(const EggTexture self, int mode)
        
        /**
         *
         */
        """
        pass

    def sortsLessThan(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        sorts_less_than(EggTexture self, const EggTexture other, int eq)
        
        /**
         * An ordering operator to compare two textures for sorting order.  This
         * imposes an arbitrary ordering useful to identify unique textures, according
         * to the indicated Equivalence factor.  See is_equivalent_to().
         */
        """
        pass

    def sorts_less_than(self, EggTexture_self, const_EggTexture_other, int_eq): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        sorts_less_than(EggTexture self, const EggTexture other, int eq)
        
        /**
         * An ordering operator to compare two textures for sorting order.  This
         * imposes an arbitrary ordering useful to identify unique textures, according
         * to the indicated Equivalence factor.  See is_equivalent_to().
         */
        """
        pass

    def stringCombineMode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        string_combine_mode(str string)
        
        /**
         * Returns the CombineMode value associated with the given string
         * representation, or CM_unspecified if the string does not match any known
         * CombineMode value.
         */
        """
        pass

    def stringCombineOperand(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        string_combine_operand(str string)
        
        /**
         * Returns the CombineOperand value associated with the given string
         * representation, or CO_unspecified if the string does not match any known
         * CombineOperand value.
         */
        """
        pass

    def stringCombineSource(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        string_combine_source(str string)
        
        /**
         * Returns the CombineSource value associated with the given string
         * representation, or CS_unspecified if the string does not match any known
         * CombineSource value.
         */
        """
        pass

    def stringCompressionMode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        string_compression_mode(str string)
        
        /**
         * Returns the CompressionMode value associated with the given string
         * representation, or CM_default if the string does not match any known
         * CompressionMode value.
         */
        """
        pass

    def stringEnvType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        string_env_type(str string)
        
        /**
         * Returns the EnvType value associated with the given string representation,
         * or ET_unspecified if the string does not match any known EnvType value.
         */
        """
        pass

    def stringFilterType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        string_filter_type(str string)
        
        /**
         * Returns the FilterType value associated with the given string
         * representation, or FT_unspecified if the string does not match any known
         * FilterType value.
         */
        """
        pass

    def stringFormat(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        string_format(str string)
        
        /**
         * Returns the Format value associated with the given string representation,
         * or F_unspecified if the string does not match any known Format value.
         */
        """
        pass

    def stringQualityLevel(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        string_quality_level(str string)
        
        /**
         * Returns the TexGen value associated with the given string representation,
         * or ET_unspecified if the string does not match any known TexGen value.
         */
        """
        pass

    def stringTexGen(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        string_tex_gen(str string)
        
        /**
         * Returns the TexGen value associated with the given string representation,
         * or ET_unspecified if the string does not match any known TexGen value.
         */
        """
        pass

    def stringTextureType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        string_texture_type(str string)
        
        /**
         * Returns the Texture_ype value associated with the given string
         * representation, or TT_unspecified if the string does not match any known
         * TextureType value.
         */
        """
        pass

    def stringWrapMode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        string_wrap_mode(str string)
        
        /**
         * Returns the WrapMode value associated with the given string representation,
         * or WM_unspecified if the string does not match any known WrapMode value.
         */
        """
        pass

    def string_combine_mode(self, str_string): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        string_combine_mode(str string)
        
        /**
         * Returns the CombineMode value associated with the given string
         * representation, or CM_unspecified if the string does not match any known
         * CombineMode value.
         */
        """
        pass

    def string_combine_operand(self, str_string): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        string_combine_operand(str string)
        
        /**
         * Returns the CombineOperand value associated with the given string
         * representation, or CO_unspecified if the string does not match any known
         * CombineOperand value.
         */
        """
        pass

    def string_combine_source(self, str_string): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        string_combine_source(str string)
        
        /**
         * Returns the CombineSource value associated with the given string
         * representation, or CS_unspecified if the string does not match any known
         * CombineSource value.
         */
        """
        pass

    def string_compression_mode(self, str_string): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        string_compression_mode(str string)
        
        /**
         * Returns the CompressionMode value associated with the given string
         * representation, or CM_default if the string does not match any known
         * CompressionMode value.
         */
        """
        pass

    def string_env_type(self, str_string): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        string_env_type(str string)
        
        /**
         * Returns the EnvType value associated with the given string representation,
         * or ET_unspecified if the string does not match any known EnvType value.
         */
        """
        pass

    def string_filter_type(self, str_string): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        string_filter_type(str string)
        
        /**
         * Returns the FilterType value associated with the given string
         * representation, or FT_unspecified if the string does not match any known
         * FilterType value.
         */
        """
        pass

    def string_format(self, str_string): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        string_format(str string)
        
        /**
         * Returns the Format value associated with the given string representation,
         * or F_unspecified if the string does not match any known Format value.
         */
        """
        pass

    def string_quality_level(self, str_string): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        string_quality_level(str string)
        
        /**
         * Returns the TexGen value associated with the given string representation,
         * or ET_unspecified if the string does not match any known TexGen value.
         */
        """
        pass

    def string_texture_type(self, str_string): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        string_texture_type(str string)
        
        /**
         * Returns the Texture_ype value associated with the given string
         * representation, or TT_unspecified if the string does not match any known
         * TextureType value.
         */
        """
        pass

    def string_tex_gen(self, str_string): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        string_tex_gen(str string)
        
        /**
         * Returns the TexGen value associated with the given string representation,
         * or ET_unspecified if the string does not match any known TexGen value.
         */
        """
        pass

    def string_wrap_mode(self, str_string): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        string_wrap_mode(str string)
        
        /**
         * Returns the WrapMode value associated with the given string representation,
         * or WM_unspecified if the string does not match any known WrapMode value.
         */
        """
        pass

    def upcastToEggFilenameNode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_EggFilenameNode(const EggTexture self)
        
        upcast from EggTexture to EggFilenameNode
        """
        pass

    def upcastToEggRenderMode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_EggRenderMode(const EggTexture self)
        
        upcast from EggTexture to EggRenderMode
        """
        pass

    def upcastToEggTransform(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_EggTransform(const EggTexture self)
        
        upcast from EggTexture to EggTransform
        """
        pass

    def upcast_to_EggFilenameNode(self, const_EggTexture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_EggFilenameNode(const EggTexture self)
        
        upcast from EggTexture to EggFilenameNode
        """
        pass

    def upcast_to_EggRenderMode(self, const_EggTexture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_EggRenderMode(const EggTexture self)
        
        upcast from EggTexture to EggRenderMode
        """
        pass

    def upcast_to_EggTransform(self, const_EggTexture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_EggTransform(const EggTexture self)
        
        upcast from EggTexture to EggTransform
        """
        pass

    def write(self, EggTexture_self, ostream_out, int_indent_level): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(EggTexture self, ostream out, int indent_level)
        
        /**
         * Writes the texture definition to the indicated output stream in Egg format.
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

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    alpha_filename = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    alpha_file_channel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    alpha_fullpath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    alpha_scale = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    anisotropic_degree = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    border_color = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    color = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    compression_mode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    env_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    format = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    lod_bias = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    magfilter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    max_lod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    minfilter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    min_lod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    multitexture_sort = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    multiview = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    num_views = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priority = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    quality_level = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    read_mipmaps = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    rgb_scale = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    saved_result = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    stage_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    texture_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tex_gen = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    uv_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    wrap_mode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    wrap_u = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    wrap_v = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    wrap_w = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    CCAlpha = 1
    CCNumChannels = 2
    CCRgb = 0
    CC_alpha = 1
    CC_num_channels = 2
    CC_rgb = 0
    CINumIndices = 3
    CI_num_indices = 3
    CMAdd = 3
    CMAddSigned = 4
    CMDefault = 0
    CMDot3Rgb = 7
    CMDot3Rgba = 8
    CMDxt1 = 4
    CMDxt2 = 5
    CMDxt3 = 6
    CMDxt4 = 7
    CMDxt5 = 8
    CMFxt1 = 3
    CMInterpolate = 5
    CMModulate = 2
    CMOff = 1
    CMOn = 2
    CMReplace = 1
    CMSubtract = 6
    CMUnspecified = 0
    CM_add = 3
    CM_add_signed = 4
    CM_default = 0
    CM_dot3_rgb = 7
    CM_dot3_rgba = 8
    CM_dxt1 = 4
    CM_dxt2 = 5
    CM_dxt3 = 6
    CM_dxt4 = 7
    CM_dxt5 = 8
    CM_fxt1 = 3
    CM_interpolate = 5
    CM_modulate = 2
    CM_off = 1
    CM_on = 2
    CM_replace = 1
    CM_subtract = 6
    CM_unspecified = 0
    COOneMinusSrcAlpha = 4
    COOneMinusSrcColor = 2
    COSrcAlpha = 3
    COSrcColor = 1
    COUnspecified = 0
    CO_one_minus_src_alpha = 4
    CO_one_minus_src_color = 2
    CO_src_alpha = 3
    CO_src_color = 1
    CO_unspecified = 0
    CSConstant = 2
    CSConstantColorScale = 5
    CSLastSavedResult = 6
    CSPrevious = 4
    CSPrimaryColor = 3
    CSTexture = 1
    CSUnspecified = 0
    CS_constant = 2
    CS_constant_color_scale = 5
    CS_last_saved_result = 6
    CS_previous = 4
    CS_primary_color = 3
    CS_texture = 1
    CS_unspecified = 0
    DtoolClassDict = {
        'CCAlpha': 1,
        'CCNumChannels': 2,
        'CCRgb': 0,
        'CC_alpha': 1,
        'CC_num_channels': 2,
        'CC_rgb': 0,
        'CINumIndices': 3,
        'CI_num_indices': 3,
        'CMAdd': 3,
        'CMAddSigned': 4,
        'CMDefault': 0,
        'CMDot3Rgb': 7,
        'CMDot3Rgba': 8,
        'CMDxt1': 4,
        'CMDxt2': 5,
        'CMDxt3': 6,
        'CMDxt4': 7,
        'CMDxt5': 8,
        'CMFxt1': 3,
        'CMInterpolate': 5,
        'CMModulate': 2,
        'CMOff': 1,
        'CMOn': 2,
        'CMReplace': 1,
        'CMSubtract': 6,
        'CMUnspecified': 0,
        'CM_add': 3,
        'CM_add_signed': 4,
        'CM_default': 0,
        'CM_dot3_rgb': 7,
        'CM_dot3_rgba': 8,
        'CM_dxt1': 4,
        'CM_dxt2': 5,
        'CM_dxt3': 6,
        'CM_dxt4': 7,
        'CM_dxt5': 8,
        'CM_fxt1': 3,
        'CM_interpolate': 5,
        'CM_modulate': 2,
        'CM_off': 1,
        'CM_on': 2,
        'CM_replace': 1,
        'CM_subtract': 6,
        'CM_unspecified': 0,
        'COOneMinusSrcAlpha': 4,
        'COOneMinusSrcColor': 2,
        'COSrcAlpha': 3,
        'COSrcColor': 1,
        'COUnspecified': 0,
        'CO_one_minus_src_alpha': 4,
        'CO_one_minus_src_color': 2,
        'CO_src_alpha': 3,
        'CO_src_color': 1,
        'CO_unspecified': 0,
        'CSConstant': 2,
        'CSConstantColorScale': 5,
        'CSLastSavedResult': 6,
        'CSPrevious': 4,
        'CSPrimaryColor': 3,
        'CSTexture': 1,
        'CSUnspecified': 0,
        'CS_constant': 2,
        'CS_constant_color_scale': 5,
        'CS_last_saved_result': 6,
        'CS_previous': 4,
        'CS_primary_color': 3,
        'CS_texture': 1,
        'CS_unspecified': 0,
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        'EAttributes': 16,
        'EBasename': 1,
        'ECompleteFilename': 7,
        'EDirname': 4,
        'EExtension': 2,
        'ETAdd': 5,
        'ETBlend': 3,
        'ETBlendColorScale': 6,
        'ETDecal': 2,
        'ETEmission': 16,
        'ETGloss': 12,
        'ETGlow': 11,
        'ETHeight': 13,
        'ETModulate': 1,
        'ETModulateGloss': 8,
        'ETModulateGlow': 7,
        'ETNormal': 9,
        'ETNormalGloss': 15,
        'ETNormalHeight': 10,
        'ETReplace': 4,
        'ETSelector': 14,
        'ETUnspecified': 0,
        'ET_add': 5,
        'ET_blend': 3,
        'ET_blend_color_scale': 6,
        'ET_decal': 2,
        'ET_emission': 16,
        'ET_gloss': 12,
        'ET_glow': 11,
        'ET_height': 13,
        'ET_modulate': 1,
        'ET_modulate_gloss': 8,
        'ET_modulate_glow': 7,
        'ET_normal': 9,
        'ET_normal_gloss': 15,
        'ET_normal_height': 10,
        'ET_replace': 4,
        'ET_selector': 14,
        'ET_unspecified': 0,
        'ETransform': 8,
        'ETrefName': 32,
        'E_attributes': 16,
        'E_basename': 1,
        'E_complete_filename': 7,
        'E_dirname': 4,
        'E_extension': 2,
        'E_transform': 8,
        'E_tref_name': 32,
        'FAlpha': 15,
        'FBlue': 14,
        'FGreen': 13,
        'FLuminance': 16,
        'FLuminanceAlpha': 17,
        'FLuminanceAlphamask': 18,
        'FRed': 12,
        'FRgb': 7,
        'FRgb12': 8,
        'FRgb332': 11,
        'FRgb5': 10,
        'FRgb8': 9,
        'FRgba': 1,
        'FRgba12': 3,
        'FRgba4': 5,
        'FRgba5': 6,
        'FRgba8': 4,
        'FRgbm': 2,
        'FSrgb': 19,
        'FSrgbAlpha': 20,
        'FTLinear': 2,
        'FTLinearMipmapLinear': 6,
        'FTLinearMipmapNearest': 4,
        'FTNearest': 1,
        'FTNearestMipmapLinear': 5,
        'FTNearestMipmapNearest': 3,
        'FTUnspecified': 0,
        'FT_linear': 2,
        'FT_linear_mipmap_linear': 6,
        'FT_linear_mipmap_nearest': 4,
        'FT_nearest': 1,
        'FT_nearest_mipmap_linear': 5,
        'FT_nearest_mipmap_nearest': 3,
        'FT_unspecified': 0,
        'FUnspecified': 0,
        'F_alpha': 15,
        'F_blue': 14,
        'F_green': 13,
        'F_luminance': 16,
        'F_luminance_alpha': 17,
        'F_luminance_alphamask': 18,
        'F_red': 12,
        'F_rgb': 7,
        'F_rgb12': 8,
        'F_rgb332': 11,
        'F_rgb5': 10,
        'F_rgb8': 9,
        'F_rgba': 1,
        'F_rgba12': 3,
        'F_rgba4': 5,
        'F_rgba5': 6,
        'F_rgba8': 4,
        'F_rgbm': 2,
        'F_srgb': 19,
        'F_srgb_alpha': 20,
        'F_unspecified': 0,
        'QLBest': 4,
        'QLDefault': 1,
        'QLFastest': 2,
        'QLNormal': 3,
        'QLUnspecified': 0,
        'QL_best': 4,
        'QL_default': 1,
        'QL_fastest': 2,
        'QL_normal': 3,
        'QL_unspecified': 0,
        'TGEyeCubeMap': 3,
        'TGEyeNormal': 5,
        'TGEyePosition': 7,
        'TGEyeSphereMap': 1,
        'TGPointSprite': 8,
        'TGUnspecified': 0,
        'TGWorldCubeMap': 2,
        'TGWorldNormal': 4,
        'TGWorldPosition': 6,
        'TG_eye_cube_map': 3,
        'TG_eye_normal': 5,
        'TG_eye_position': 7,
        'TG_eye_sphere_map': 1,
        'TG_point_sprite': 8,
        'TG_unspecified': 0,
        'TG_world_cube_map': 2,
        'TG_world_normal': 4,
        'TG_world_position': 6,
        'TT1dTexture': 1,
        'TT2dTexture': 2,
        'TT3dTexture': 3,
        'TTCubeMap': 4,
        'TTUnspecified': 0,
        'TT_1d_texture': 1,
        'TT_2d_texture': 2,
        'TT_3d_texture': 3,
        'TT_cube_map': 4,
        'TT_unspecified': 0,
        'WMBorderColor': 5,
        'WMClamp': 1,
        'WMMirror': 3,
        'WMMirrorOnce': 4,
        'WMRepeat': 2,
        'WMUnspecified': 0,
        'WM_border_color': 5,
        'WM_clamp': 1,
        'WM_mirror': 3,
        'WM_mirror_once': 4,
        'WM_repeat': 2,
        'WM_unspecified': 0,
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.egg.EggTexture' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.egg.EggTexture' objects>"
        '__doc__': '/**\n * Defines a texture map that may be applied to geometry.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.egg.EggTexture' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDC68CEBC0>'
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.egg.EggTexture' objects>"
        'affectsPolygonAlpha': None, # (!) real value is "<method 'affectsPolygonAlpha' of 'panda3d.egg.EggTexture' objects>"
        'affects_polygon_alpha': None, # (!) real value is "<method 'affects_polygon_alpha' of 'panda3d.egg.EggTexture' objects>"
        'alpha_file_channel': None, # (!) real value is "<attribute 'alpha_file_channel' of 'panda3d.egg.EggTexture' objects>"
        'alpha_filename': None, # (!) real value is "<attribute 'alpha_filename' of 'panda3d.egg.EggTexture' objects>"
        'alpha_fullpath': None, # (!) real value is "<attribute 'alpha_fullpath' of 'panda3d.egg.EggTexture' objects>"
        'alpha_scale': None, # (!) real value is "<attribute 'alpha_scale' of 'panda3d.egg.EggTexture' objects>"
        'anisotropic_degree': None, # (!) real value is "<attribute 'anisotropic_degree' of 'panda3d.egg.EggTexture' objects>"
        'assign': None, # (!) real value is "<method 'assign' of 'panda3d.egg.EggTexture' objects>"
        'border_color': None, # (!) real value is "<attribute 'border_color' of 'panda3d.egg.EggTexture' objects>"
        'clearAlphaFileChannel': None, # (!) real value is "<method 'clearAlphaFileChannel' of 'panda3d.egg.EggTexture' objects>"
        'clearAlphaFilename': None, # (!) real value is "<method 'clearAlphaFilename' of 'panda3d.egg.EggTexture' objects>"
        'clearAlphaScale': None, # (!) real value is "<method 'clearAlphaScale' of 'panda3d.egg.EggTexture' objects>"
        'clearAnisotropicDegree': None, # (!) real value is "<method 'clearAnisotropicDegree' of 'panda3d.egg.EggTexture' objects>"
        'clearBorderColor': None, # (!) real value is "<method 'clearBorderColor' of 'panda3d.egg.EggTexture' objects>"
        'clearColor': None, # (!) real value is "<method 'clearColor' of 'panda3d.egg.EggTexture' objects>"
        'clearLodBias': None, # (!) real value is "<method 'clearLodBias' of 'panda3d.egg.EggTexture' objects>"
        'clearMaxLod': None, # (!) real value is "<method 'clearMaxLod' of 'panda3d.egg.EggTexture' objects>"
        'clearMinLod': None, # (!) real value is "<method 'clearMinLod' of 'panda3d.egg.EggTexture' objects>"
        'clearMultitexture': None, # (!) real value is "<method 'clearMultitexture' of 'panda3d.egg.EggTexture' objects>"
        'clearNumViews': None, # (!) real value is "<method 'clearNumViews' of 'panda3d.egg.EggTexture' objects>"
        'clearPriority': None, # (!) real value is "<method 'clearPriority' of 'panda3d.egg.EggTexture' objects>"
        'clearRgbScale': None, # (!) real value is "<method 'clearRgbScale' of 'panda3d.egg.EggTexture' objects>"
        'clearStageName': None, # (!) real value is "<method 'clearStageName' of 'panda3d.egg.EggTexture' objects>"
        'clearUvName': None, # (!) real value is "<method 'clearUvName' of 'panda3d.egg.EggTexture' objects>"
        'clear_alpha_file_channel': None, # (!) real value is "<method 'clear_alpha_file_channel' of 'panda3d.egg.EggTexture' objects>"
        'clear_alpha_filename': None, # (!) real value is "<method 'clear_alpha_filename' of 'panda3d.egg.EggTexture' objects>"
        'clear_alpha_scale': None, # (!) real value is "<method 'clear_alpha_scale' of 'panda3d.egg.EggTexture' objects>"
        'clear_anisotropic_degree': None, # (!) real value is "<method 'clear_anisotropic_degree' of 'panda3d.egg.EggTexture' objects>"
        'clear_border_color': None, # (!) real value is "<method 'clear_border_color' of 'panda3d.egg.EggTexture' objects>"
        'clear_color': None, # (!) real value is "<method 'clear_color' of 'panda3d.egg.EggTexture' objects>"
        'clear_lod_bias': None, # (!) real value is "<method 'clear_lod_bias' of 'panda3d.egg.EggTexture' objects>"
        'clear_max_lod': None, # (!) real value is "<method 'clear_max_lod' of 'panda3d.egg.EggTexture' objects>"
        'clear_min_lod': None, # (!) real value is "<method 'clear_min_lod' of 'panda3d.egg.EggTexture' objects>"
        'clear_multitexture': None, # (!) real value is "<method 'clear_multitexture' of 'panda3d.egg.EggTexture' objects>"
        'clear_num_views': None, # (!) real value is "<method 'clear_num_views' of 'panda3d.egg.EggTexture' objects>"
        'clear_priority': None, # (!) real value is "<method 'clear_priority' of 'panda3d.egg.EggTexture' objects>"
        'clear_rgb_scale': None, # (!) real value is "<method 'clear_rgb_scale' of 'panda3d.egg.EggTexture' objects>"
        'clear_stage_name': None, # (!) real value is "<method 'clear_stage_name' of 'panda3d.egg.EggTexture' objects>"
        'clear_uv_name': None, # (!) real value is "<method 'clear_uv_name' of 'panda3d.egg.EggTexture' objects>"
        'color': None, # (!) real value is "<attribute 'color' of 'panda3d.egg.EggTexture' objects>"
        'compression_mode': None, # (!) real value is "<attribute 'compression_mode' of 'panda3d.egg.EggTexture' objects>"
        'determineWrapU': None, # (!) real value is "<method 'determineWrapU' of 'panda3d.egg.EggTexture' objects>"
        'determineWrapV': None, # (!) real value is "<method 'determineWrapV' of 'panda3d.egg.EggTexture' objects>"
        'determineWrapW': None, # (!) real value is "<method 'determineWrapW' of 'panda3d.egg.EggTexture' objects>"
        'determine_wrap_u': None, # (!) real value is "<method 'determine_wrap_u' of 'panda3d.egg.EggTexture' objects>"
        'determine_wrap_v': None, # (!) real value is "<method 'determine_wrap_v' of 'panda3d.egg.EggTexture' objects>"
        'determine_wrap_w': None, # (!) real value is "<method 'determine_wrap_w' of 'panda3d.egg.EggTexture' objects>"
        'env_type': None, # (!) real value is "<attribute 'env_type' of 'panda3d.egg.EggTexture' objects>"
        'format': None, # (!) real value is "<attribute 'format' of 'panda3d.egg.EggTexture' objects>"
        'getAlphaFileChannel': None, # (!) real value is "<method 'getAlphaFileChannel' of 'panda3d.egg.EggTexture' objects>"
        'getAlphaFilename': None, # (!) real value is "<method 'getAlphaFilename' of 'panda3d.egg.EggTexture' objects>"
        'getAlphaFullpath': None, # (!) real value is "<method 'getAlphaFullpath' of 'panda3d.egg.EggTexture' objects>"
        'getAlphaScale': None, # (!) real value is "<method 'getAlphaScale' of 'panda3d.egg.EggTexture' objects>"
        'getAnisotropicDegree': None, # (!) real value is "<method 'getAnisotropicDegree' of 'panda3d.egg.EggTexture' objects>"
        'getBorderColor': None, # (!) real value is "<method 'getBorderColor' of 'panda3d.egg.EggTexture' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFDC68CEBC0>)>'
        'getColor': None, # (!) real value is "<method 'getColor' of 'panda3d.egg.EggTexture' objects>"
        'getCombineMode': None, # (!) real value is "<method 'getCombineMode' of 'panda3d.egg.EggTexture' objects>"
        'getCombineOperand': None, # (!) real value is "<method 'getCombineOperand' of 'panda3d.egg.EggTexture' objects>"
        'getCombineSource': None, # (!) real value is "<method 'getCombineSource' of 'panda3d.egg.EggTexture' objects>"
        'getCompressionMode': None, # (!) real value is "<method 'getCompressionMode' of 'panda3d.egg.EggTexture' objects>"
        'getEnvType': None, # (!) real value is "<method 'getEnvType' of 'panda3d.egg.EggTexture' objects>"
        'getFormat': None, # (!) real value is "<method 'getFormat' of 'panda3d.egg.EggTexture' objects>"
        'getLodBias': None, # (!) real value is "<method 'getLodBias' of 'panda3d.egg.EggTexture' objects>"
        'getMagfilter': None, # (!) real value is "<method 'getMagfilter' of 'panda3d.egg.EggTexture' objects>"
        'getMaxLod': None, # (!) real value is "<method 'getMaxLod' of 'panda3d.egg.EggTexture' objects>"
        'getMinLod': None, # (!) real value is "<method 'getMinLod' of 'panda3d.egg.EggTexture' objects>"
        'getMinfilter': None, # (!) real value is "<method 'getMinfilter' of 'panda3d.egg.EggTexture' objects>"
        'getMultitextureSort': None, # (!) real value is "<method 'getMultitextureSort' of 'panda3d.egg.EggTexture' objects>"
        'getMultiview': None, # (!) real value is "<method 'getMultiview' of 'panda3d.egg.EggTexture' objects>"
        'getNumViews': None, # (!) real value is "<method 'getNumViews' of 'panda3d.egg.EggTexture' objects>"
        'getPriority': None, # (!) real value is "<method 'getPriority' of 'panda3d.egg.EggTexture' objects>"
        'getQualityLevel': None, # (!) real value is "<method 'getQualityLevel' of 'panda3d.egg.EggTexture' objects>"
        'getReadMipmaps': None, # (!) real value is "<method 'getReadMipmaps' of 'panda3d.egg.EggTexture' objects>"
        'getRgbScale': None, # (!) real value is "<method 'getRgbScale' of 'panda3d.egg.EggTexture' objects>"
        'getSavedResult': None, # (!) real value is "<method 'getSavedResult' of 'panda3d.egg.EggTexture' objects>"
        'getStageName': None, # (!) real value is "<method 'getStageName' of 'panda3d.egg.EggTexture' objects>"
        'getTexGen': None, # (!) real value is "<method 'getTexGen' of 'panda3d.egg.EggTexture' objects>"
        'getTextureType': None, # (!) real value is "<method 'getTextureType' of 'panda3d.egg.EggTexture' objects>"
        'getUvName': None, # (!) real value is "<method 'getUvName' of 'panda3d.egg.EggTexture' objects>"
        'getWrapMode': None, # (!) real value is "<method 'getWrapMode' of 'panda3d.egg.EggTexture' objects>"
        'getWrapU': None, # (!) real value is "<method 'getWrapU' of 'panda3d.egg.EggTexture' objects>"
        'getWrapV': None, # (!) real value is "<method 'getWrapV' of 'panda3d.egg.EggTexture' objects>"
        'getWrapW': None, # (!) real value is "<method 'getWrapW' of 'panda3d.egg.EggTexture' objects>"
        'get_alpha_file_channel': None, # (!) real value is "<method 'get_alpha_file_channel' of 'panda3d.egg.EggTexture' objects>"
        'get_alpha_filename': None, # (!) real value is "<method 'get_alpha_filename' of 'panda3d.egg.EggTexture' objects>"
        'get_alpha_fullpath': None, # (!) real value is "<method 'get_alpha_fullpath' of 'panda3d.egg.EggTexture' objects>"
        'get_alpha_scale': None, # (!) real value is "<method 'get_alpha_scale' of 'panda3d.egg.EggTexture' objects>"
        'get_anisotropic_degree': None, # (!) real value is "<method 'get_anisotropic_degree' of 'panda3d.egg.EggTexture' objects>"
        'get_border_color': None, # (!) real value is "<method 'get_border_color' of 'panda3d.egg.EggTexture' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFDC68CEBC0>)>'
        'get_color': None, # (!) real value is "<method 'get_color' of 'panda3d.egg.EggTexture' objects>"
        'get_combine_mode': None, # (!) real value is "<method 'get_combine_mode' of 'panda3d.egg.EggTexture' objects>"
        'get_combine_operand': None, # (!) real value is "<method 'get_combine_operand' of 'panda3d.egg.EggTexture' objects>"
        'get_combine_source': None, # (!) real value is "<method 'get_combine_source' of 'panda3d.egg.EggTexture' objects>"
        'get_compression_mode': None, # (!) real value is "<method 'get_compression_mode' of 'panda3d.egg.EggTexture' objects>"
        'get_env_type': None, # (!) real value is "<method 'get_env_type' of 'panda3d.egg.EggTexture' objects>"
        'get_format': None, # (!) real value is "<method 'get_format' of 'panda3d.egg.EggTexture' objects>"
        'get_lod_bias': None, # (!) real value is "<method 'get_lod_bias' of 'panda3d.egg.EggTexture' objects>"
        'get_magfilter': None, # (!) real value is "<method 'get_magfilter' of 'panda3d.egg.EggTexture' objects>"
        'get_max_lod': None, # (!) real value is "<method 'get_max_lod' of 'panda3d.egg.EggTexture' objects>"
        'get_min_lod': None, # (!) real value is "<method 'get_min_lod' of 'panda3d.egg.EggTexture' objects>"
        'get_minfilter': None, # (!) real value is "<method 'get_minfilter' of 'panda3d.egg.EggTexture' objects>"
        'get_multitexture_sort': None, # (!) real value is "<method 'get_multitexture_sort' of 'panda3d.egg.EggTexture' objects>"
        'get_multiview': None, # (!) real value is "<method 'get_multiview' of 'panda3d.egg.EggTexture' objects>"
        'get_num_views': None, # (!) real value is "<method 'get_num_views' of 'panda3d.egg.EggTexture' objects>"
        'get_priority': None, # (!) real value is "<method 'get_priority' of 'panda3d.egg.EggTexture' objects>"
        'get_quality_level': None, # (!) real value is "<method 'get_quality_level' of 'panda3d.egg.EggTexture' objects>"
        'get_read_mipmaps': None, # (!) real value is "<method 'get_read_mipmaps' of 'panda3d.egg.EggTexture' objects>"
        'get_rgb_scale': None, # (!) real value is "<method 'get_rgb_scale' of 'panda3d.egg.EggTexture' objects>"
        'get_saved_result': None, # (!) real value is "<method 'get_saved_result' of 'panda3d.egg.EggTexture' objects>"
        'get_stage_name': None, # (!) real value is "<method 'get_stage_name' of 'panda3d.egg.EggTexture' objects>"
        'get_tex_gen': None, # (!) real value is "<method 'get_tex_gen' of 'panda3d.egg.EggTexture' objects>"
        'get_texture_type': None, # (!) real value is "<method 'get_texture_type' of 'panda3d.egg.EggTexture' objects>"
        'get_uv_name': None, # (!) real value is "<method 'get_uv_name' of 'panda3d.egg.EggTexture' objects>"
        'get_wrap_mode': None, # (!) real value is "<method 'get_wrap_mode' of 'panda3d.egg.EggTexture' objects>"
        'get_wrap_u': None, # (!) real value is "<method 'get_wrap_u' of 'panda3d.egg.EggTexture' objects>"
        'get_wrap_v': None, # (!) real value is "<method 'get_wrap_v' of 'panda3d.egg.EggTexture' objects>"
        'get_wrap_w': None, # (!) real value is "<method 'get_wrap_w' of 'panda3d.egg.EggTexture' objects>"
        'hasAlphaChannel': None, # (!) real value is "<method 'hasAlphaChannel' of 'panda3d.egg.EggTexture' objects>"
        'hasAlphaFileChannel': None, # (!) real value is "<method 'hasAlphaFileChannel' of 'panda3d.egg.EggTexture' objects>"
        'hasAlphaFilename': None, # (!) real value is "<method 'hasAlphaFilename' of 'panda3d.egg.EggTexture' objects>"
        'hasAlphaScale': None, # (!) real value is "<method 'hasAlphaScale' of 'panda3d.egg.EggTexture' objects>"
        'hasAnisotropicDegree': None, # (!) real value is "<method 'hasAnisotropicDegree' of 'panda3d.egg.EggTexture' objects>"
        'hasBorderColor': None, # (!) real value is "<method 'hasBorderColor' of 'panda3d.egg.EggTexture' objects>"
        'hasColor': None, # (!) real value is "<method 'hasColor' of 'panda3d.egg.EggTexture' objects>"
        'hasLodBias': None, # (!) real value is "<method 'hasLodBias' of 'panda3d.egg.EggTexture' objects>"
        'hasMaxLod': None, # (!) real value is "<method 'hasMaxLod' of 'panda3d.egg.EggTexture' objects>"
        'hasMinLod': None, # (!) real value is "<method 'hasMinLod' of 'panda3d.egg.EggTexture' objects>"
        'hasNumViews': None, # (!) real value is "<method 'hasNumViews' of 'panda3d.egg.EggTexture' objects>"
        'hasPriority': None, # (!) real value is "<method 'hasPriority' of 'panda3d.egg.EggTexture' objects>"
        'hasRgbScale': None, # (!) real value is "<method 'hasRgbScale' of 'panda3d.egg.EggTexture' objects>"
        'hasStageName': None, # (!) real value is "<method 'hasStageName' of 'panda3d.egg.EggTexture' objects>"
        'hasUvName': None, # (!) real value is "<method 'hasUvName' of 'panda3d.egg.EggTexture' objects>"
        'has_alpha_channel': None, # (!) real value is "<method 'has_alpha_channel' of 'panda3d.egg.EggTexture' objects>"
        'has_alpha_file_channel': None, # (!) real value is "<method 'has_alpha_file_channel' of 'panda3d.egg.EggTexture' objects>"
        'has_alpha_filename': None, # (!) real value is "<method 'has_alpha_filename' of 'panda3d.egg.EggTexture' objects>"
        'has_alpha_scale': None, # (!) real value is "<method 'has_alpha_scale' of 'panda3d.egg.EggTexture' objects>"
        'has_anisotropic_degree': None, # (!) real value is "<method 'has_anisotropic_degree' of 'panda3d.egg.EggTexture' objects>"
        'has_border_color': None, # (!) real value is "<method 'has_border_color' of 'panda3d.egg.EggTexture' objects>"
        'has_color': None, # (!) real value is "<method 'has_color' of 'panda3d.egg.EggTexture' objects>"
        'has_lod_bias': None, # (!) real value is "<method 'has_lod_bias' of 'panda3d.egg.EggTexture' objects>"
        'has_max_lod': None, # (!) real value is "<method 'has_max_lod' of 'panda3d.egg.EggTexture' objects>"
        'has_min_lod': None, # (!) real value is "<method 'has_min_lod' of 'panda3d.egg.EggTexture' objects>"
        'has_num_views': None, # (!) real value is "<method 'has_num_views' of 'panda3d.egg.EggTexture' objects>"
        'has_priority': None, # (!) real value is "<method 'has_priority' of 'panda3d.egg.EggTexture' objects>"
        'has_rgb_scale': None, # (!) real value is "<method 'has_rgb_scale' of 'panda3d.egg.EggTexture' objects>"
        'has_stage_name': None, # (!) real value is "<method 'has_stage_name' of 'panda3d.egg.EggTexture' objects>"
        'has_uv_name': None, # (!) real value is "<method 'has_uv_name' of 'panda3d.egg.EggTexture' objects>"
        'isEquivalentTo': None, # (!) real value is "<method 'isEquivalentTo' of 'panda3d.egg.EggTexture' objects>"
        'is_equivalent_to': None, # (!) real value is "<method 'is_equivalent_to' of 'panda3d.egg.EggTexture' objects>"
        'lod_bias': None, # (!) real value is "<attribute 'lod_bias' of 'panda3d.egg.EggTexture' objects>"
        'magfilter': None, # (!) real value is "<attribute 'magfilter' of 'panda3d.egg.EggTexture' objects>"
        'max_lod': None, # (!) real value is "<attribute 'max_lod' of 'panda3d.egg.EggTexture' objects>"
        'min_lod': None, # (!) real value is "<attribute 'min_lod' of 'panda3d.egg.EggTexture' objects>"
        'minfilter': None, # (!) real value is "<attribute 'minfilter' of 'panda3d.egg.EggTexture' objects>"
        'multitextureOver': None, # (!) real value is "<method 'multitextureOver' of 'panda3d.egg.EggTexture' objects>"
        'multitexture_over': None, # (!) real value is "<method 'multitexture_over' of 'panda3d.egg.EggTexture' objects>"
        'multitexture_sort': None, # (!) real value is "<attribute 'multitexture_sort' of 'panda3d.egg.EggTexture' objects>"
        'multiview': None, # (!) real value is "<attribute 'multiview' of 'panda3d.egg.EggTexture' objects>"
        'num_views': None, # (!) real value is "<attribute 'num_views' of 'panda3d.egg.EggTexture' objects>"
        'priority': None, # (!) real value is "<attribute 'priority' of 'panda3d.egg.EggTexture' objects>"
        'quality_level': None, # (!) real value is "<attribute 'quality_level' of 'panda3d.egg.EggTexture' objects>"
        'read_mipmaps': None, # (!) real value is "<attribute 'read_mipmaps' of 'panda3d.egg.EggTexture' objects>"
        'rgb_scale': None, # (!) real value is "<attribute 'rgb_scale' of 'panda3d.egg.EggTexture' objects>"
        'saved_result': None, # (!) real value is "<attribute 'saved_result' of 'panda3d.egg.EggTexture' objects>"
        'setAlphaFileChannel': None, # (!) real value is "<method 'setAlphaFileChannel' of 'panda3d.egg.EggTexture' objects>"
        'setAlphaFilename': None, # (!) real value is "<method 'setAlphaFilename' of 'panda3d.egg.EggTexture' objects>"
        'setAlphaFullpath': None, # (!) real value is "<method 'setAlphaFullpath' of 'panda3d.egg.EggTexture' objects>"
        'setAlphaScale': None, # (!) real value is "<method 'setAlphaScale' of 'panda3d.egg.EggTexture' objects>"
        'setAnisotropicDegree': None, # (!) real value is "<method 'setAnisotropicDegree' of 'panda3d.egg.EggTexture' objects>"
        'setBorderColor': None, # (!) real value is "<method 'setBorderColor' of 'panda3d.egg.EggTexture' objects>"
        'setColor': None, # (!) real value is "<method 'setColor' of 'panda3d.egg.EggTexture' objects>"
        'setCombineMode': None, # (!) real value is "<method 'setCombineMode' of 'panda3d.egg.EggTexture' objects>"
        'setCombineOperand': None, # (!) real value is "<method 'setCombineOperand' of 'panda3d.egg.EggTexture' objects>"
        'setCombineSource': None, # (!) real value is "<method 'setCombineSource' of 'panda3d.egg.EggTexture' objects>"
        'setCompressionMode': None, # (!) real value is "<method 'setCompressionMode' of 'panda3d.egg.EggTexture' objects>"
        'setEnvType': None, # (!) real value is "<method 'setEnvType' of 'panda3d.egg.EggTexture' objects>"
        'setFormat': None, # (!) real value is "<method 'setFormat' of 'panda3d.egg.EggTexture' objects>"
        'setLodBias': None, # (!) real value is "<method 'setLodBias' of 'panda3d.egg.EggTexture' objects>"
        'setMagfilter': None, # (!) real value is "<method 'setMagfilter' of 'panda3d.egg.EggTexture' objects>"
        'setMaxLod': None, # (!) real value is "<method 'setMaxLod' of 'panda3d.egg.EggTexture' objects>"
        'setMinLod': None, # (!) real value is "<method 'setMinLod' of 'panda3d.egg.EggTexture' objects>"
        'setMinfilter': None, # (!) real value is "<method 'setMinfilter' of 'panda3d.egg.EggTexture' objects>"
        'setMultiview': None, # (!) real value is "<method 'setMultiview' of 'panda3d.egg.EggTexture' objects>"
        'setNumViews': None, # (!) real value is "<method 'setNumViews' of 'panda3d.egg.EggTexture' objects>"
        'setPriority': None, # (!) real value is "<method 'setPriority' of 'panda3d.egg.EggTexture' objects>"
        'setQualityLevel': None, # (!) real value is "<method 'setQualityLevel' of 'panda3d.egg.EggTexture' objects>"
        'setReadMipmaps': None, # (!) real value is "<method 'setReadMipmaps' of 'panda3d.egg.EggTexture' objects>"
        'setRgbScale': None, # (!) real value is "<method 'setRgbScale' of 'panda3d.egg.EggTexture' objects>"
        'setSavedResult': None, # (!) real value is "<method 'setSavedResult' of 'panda3d.egg.EggTexture' objects>"
        'setStageName': None, # (!) real value is "<method 'setStageName' of 'panda3d.egg.EggTexture' objects>"
        'setTexGen': None, # (!) real value is "<method 'setTexGen' of 'panda3d.egg.EggTexture' objects>"
        'setTextureType': None, # (!) real value is "<method 'setTextureType' of 'panda3d.egg.EggTexture' objects>"
        'setUvName': None, # (!) real value is "<method 'setUvName' of 'panda3d.egg.EggTexture' objects>"
        'setWrapMode': None, # (!) real value is "<method 'setWrapMode' of 'panda3d.egg.EggTexture' objects>"
        'setWrapU': None, # (!) real value is "<method 'setWrapU' of 'panda3d.egg.EggTexture' objects>"
        'setWrapV': None, # (!) real value is "<method 'setWrapV' of 'panda3d.egg.EggTexture' objects>"
        'setWrapW': None, # (!) real value is "<method 'setWrapW' of 'panda3d.egg.EggTexture' objects>"
        'set_alpha_file_channel': None, # (!) real value is "<method 'set_alpha_file_channel' of 'panda3d.egg.EggTexture' objects>"
        'set_alpha_filename': None, # (!) real value is "<method 'set_alpha_filename' of 'panda3d.egg.EggTexture' objects>"
        'set_alpha_fullpath': None, # (!) real value is "<method 'set_alpha_fullpath' of 'panda3d.egg.EggTexture' objects>"
        'set_alpha_scale': None, # (!) real value is "<method 'set_alpha_scale' of 'panda3d.egg.EggTexture' objects>"
        'set_anisotropic_degree': None, # (!) real value is "<method 'set_anisotropic_degree' of 'panda3d.egg.EggTexture' objects>"
        'set_border_color': None, # (!) real value is "<method 'set_border_color' of 'panda3d.egg.EggTexture' objects>"
        'set_color': None, # (!) real value is "<method 'set_color' of 'panda3d.egg.EggTexture' objects>"
        'set_combine_mode': None, # (!) real value is "<method 'set_combine_mode' of 'panda3d.egg.EggTexture' objects>"
        'set_combine_operand': None, # (!) real value is "<method 'set_combine_operand' of 'panda3d.egg.EggTexture' objects>"
        'set_combine_source': None, # (!) real value is "<method 'set_combine_source' of 'panda3d.egg.EggTexture' objects>"
        'set_compression_mode': None, # (!) real value is "<method 'set_compression_mode' of 'panda3d.egg.EggTexture' objects>"
        'set_env_type': None, # (!) real value is "<method 'set_env_type' of 'panda3d.egg.EggTexture' objects>"
        'set_format': None, # (!) real value is "<method 'set_format' of 'panda3d.egg.EggTexture' objects>"
        'set_lod_bias': None, # (!) real value is "<method 'set_lod_bias' of 'panda3d.egg.EggTexture' objects>"
        'set_magfilter': None, # (!) real value is "<method 'set_magfilter' of 'panda3d.egg.EggTexture' objects>"
        'set_max_lod': None, # (!) real value is "<method 'set_max_lod' of 'panda3d.egg.EggTexture' objects>"
        'set_min_lod': None, # (!) real value is "<method 'set_min_lod' of 'panda3d.egg.EggTexture' objects>"
        'set_minfilter': None, # (!) real value is "<method 'set_minfilter' of 'panda3d.egg.EggTexture' objects>"
        'set_multiview': None, # (!) real value is "<method 'set_multiview' of 'panda3d.egg.EggTexture' objects>"
        'set_num_views': None, # (!) real value is "<method 'set_num_views' of 'panda3d.egg.EggTexture' objects>"
        'set_priority': None, # (!) real value is "<method 'set_priority' of 'panda3d.egg.EggTexture' objects>"
        'set_quality_level': None, # (!) real value is "<method 'set_quality_level' of 'panda3d.egg.EggTexture' objects>"
        'set_read_mipmaps': None, # (!) real value is "<method 'set_read_mipmaps' of 'panda3d.egg.EggTexture' objects>"
        'set_rgb_scale': None, # (!) real value is "<method 'set_rgb_scale' of 'panda3d.egg.EggTexture' objects>"
        'set_saved_result': None, # (!) real value is "<method 'set_saved_result' of 'panda3d.egg.EggTexture' objects>"
        'set_stage_name': None, # (!) real value is "<method 'set_stage_name' of 'panda3d.egg.EggTexture' objects>"
        'set_tex_gen': None, # (!) real value is "<method 'set_tex_gen' of 'panda3d.egg.EggTexture' objects>"
        'set_texture_type': None, # (!) real value is "<method 'set_texture_type' of 'panda3d.egg.EggTexture' objects>"
        'set_uv_name': None, # (!) real value is "<method 'set_uv_name' of 'panda3d.egg.EggTexture' objects>"
        'set_wrap_mode': None, # (!) real value is "<method 'set_wrap_mode' of 'panda3d.egg.EggTexture' objects>"
        'set_wrap_u': None, # (!) real value is "<method 'set_wrap_u' of 'panda3d.egg.EggTexture' objects>"
        'set_wrap_v': None, # (!) real value is "<method 'set_wrap_v' of 'panda3d.egg.EggTexture' objects>"
        'set_wrap_w': None, # (!) real value is "<method 'set_wrap_w' of 'panda3d.egg.EggTexture' objects>"
        'sortsLessThan': None, # (!) real value is "<method 'sortsLessThan' of 'panda3d.egg.EggTexture' objects>"
        'sorts_less_than': None, # (!) real value is "<method 'sorts_less_than' of 'panda3d.egg.EggTexture' objects>"
        'stage_name': None, # (!) real value is "<attribute 'stage_name' of 'panda3d.egg.EggTexture' objects>"
        'stringCombineMode': None, # (!) real value is '<staticmethod(<built-in method stringCombineMode of type object at 0x00007FFDC68CEBC0>)>'
        'stringCombineOperand': None, # (!) real value is '<staticmethod(<built-in method stringCombineOperand of type object at 0x00007FFDC68CEBC0>)>'
        'stringCombineSource': None, # (!) real value is '<staticmethod(<built-in method stringCombineSource of type object at 0x00007FFDC68CEBC0>)>'
        'stringCompressionMode': None, # (!) real value is '<staticmethod(<built-in method stringCompressionMode of type object at 0x00007FFDC68CEBC0>)>'
        'stringEnvType': None, # (!) real value is '<staticmethod(<built-in method stringEnvType of type object at 0x00007FFDC68CEBC0>)>'
        'stringFilterType': None, # (!) real value is '<staticmethod(<built-in method stringFilterType of type object at 0x00007FFDC68CEBC0>)>'
        'stringFormat': None, # (!) real value is '<staticmethod(<built-in method stringFormat of type object at 0x00007FFDC68CEBC0>)>'
        'stringQualityLevel': None, # (!) real value is '<staticmethod(<built-in method stringQualityLevel of type object at 0x00007FFDC68CEBC0>)>'
        'stringTexGen': None, # (!) real value is '<staticmethod(<built-in method stringTexGen of type object at 0x00007FFDC68CEBC0>)>'
        'stringTextureType': None, # (!) real value is '<staticmethod(<built-in method stringTextureType of type object at 0x00007FFDC68CEBC0>)>'
        'stringWrapMode': None, # (!) real value is '<staticmethod(<built-in method stringWrapMode of type object at 0x00007FFDC68CEBC0>)>'
        'string_combine_mode': None, # (!) real value is '<staticmethod(<built-in method string_combine_mode of type object at 0x00007FFDC68CEBC0>)>'
        'string_combine_operand': None, # (!) real value is '<staticmethod(<built-in method string_combine_operand of type object at 0x00007FFDC68CEBC0>)>'
        'string_combine_source': None, # (!) real value is '<staticmethod(<built-in method string_combine_source of type object at 0x00007FFDC68CEBC0>)>'
        'string_compression_mode': None, # (!) real value is '<staticmethod(<built-in method string_compression_mode of type object at 0x00007FFDC68CEBC0>)>'
        'string_env_type': None, # (!) real value is '<staticmethod(<built-in method string_env_type of type object at 0x00007FFDC68CEBC0>)>'
        'string_filter_type': None, # (!) real value is '<staticmethod(<built-in method string_filter_type of type object at 0x00007FFDC68CEBC0>)>'
        'string_format': None, # (!) real value is '<staticmethod(<built-in method string_format of type object at 0x00007FFDC68CEBC0>)>'
        'string_quality_level': None, # (!) real value is '<staticmethod(<built-in method string_quality_level of type object at 0x00007FFDC68CEBC0>)>'
        'string_tex_gen': None, # (!) real value is '<staticmethod(<built-in method string_tex_gen of type object at 0x00007FFDC68CEBC0>)>'
        'string_texture_type': None, # (!) real value is '<staticmethod(<built-in method string_texture_type of type object at 0x00007FFDC68CEBC0>)>'
        'string_wrap_mode': None, # (!) real value is '<staticmethod(<built-in method string_wrap_mode of type object at 0x00007FFDC68CEBC0>)>'
        'tex_gen': None, # (!) real value is "<attribute 'tex_gen' of 'panda3d.egg.EggTexture' objects>"
        'texture_type': None, # (!) real value is "<attribute 'texture_type' of 'panda3d.egg.EggTexture' objects>"
        'upcastToEggFilenameNode': None, # (!) real value is "<method 'upcastToEggFilenameNode' of 'panda3d.egg.EggTexture' objects>"
        'upcastToEggRenderMode': None, # (!) real value is "<method 'upcastToEggRenderMode' of 'panda3d.egg.EggTexture' objects>"
        'upcastToEggTransform': None, # (!) real value is "<method 'upcastToEggTransform' of 'panda3d.egg.EggTexture' objects>"
        'upcast_to_EggFilenameNode': None, # (!) real value is "<method 'upcast_to_EggFilenameNode' of 'panda3d.egg.EggTexture' objects>"
        'upcast_to_EggRenderMode': None, # (!) real value is "<method 'upcast_to_EggRenderMode' of 'panda3d.egg.EggTexture' objects>"
        'upcast_to_EggTransform': None, # (!) real value is "<method 'upcast_to_EggTransform' of 'panda3d.egg.EggTexture' objects>"
        'uv_name': None, # (!) real value is "<attribute 'uv_name' of 'panda3d.egg.EggTexture' objects>"
        'wrap_mode': None, # (!) real value is "<attribute 'wrap_mode' of 'panda3d.egg.EggTexture' objects>"
        'wrap_u': None, # (!) real value is "<attribute 'wrap_u' of 'panda3d.egg.EggTexture' objects>"
        'wrap_v': None, # (!) real value is "<attribute 'wrap_v' of 'panda3d.egg.EggTexture' objects>"
        'wrap_w': None, # (!) real value is "<attribute 'wrap_w' of 'panda3d.egg.EggTexture' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.egg.EggTexture' objects>"
    }
    EAttributes = 16
    EBasename = 1
    ECompleteFilename = 7
    EDirname = 4
    EExtension = 2
    ETAdd = 5
    ETBlend = 3
    ETBlendColorScale = 6
    ETDecal = 2
    ETEmission = 16
    ETGloss = 12
    ETGlow = 11
    ETHeight = 13
    ETModulate = 1
    ETModulateGloss = 8
    ETModulateGlow = 7
    ETNormal = 9
    ETNormalGloss = 15
    ETNormalHeight = 10
    ETransform = 8
    ETrefName = 32
    ETReplace = 4
    ETSelector = 14
    ETUnspecified = 0
    ET_add = 5
    ET_blend = 3
    ET_blend_color_scale = 6
    ET_decal = 2
    ET_emission = 16
    ET_gloss = 12
    ET_glow = 11
    ET_height = 13
    ET_modulate = 1
    ET_modulate_gloss = 8
    ET_modulate_glow = 7
    ET_normal = 9
    ET_normal_gloss = 15
    ET_normal_height = 10
    ET_replace = 4
    ET_selector = 14
    ET_unspecified = 0
    E_attributes = 16
    E_basename = 1
    E_complete_filename = 7
    E_dirname = 4
    E_extension = 2
    E_transform = 8
    E_tref_name = 32
    FAlpha = 15
    FBlue = 14
    FGreen = 13
    FLuminance = 16
    FLuminanceAlpha = 17
    FLuminanceAlphamask = 18
    FRed = 12
    FRgb = 7
    FRgb12 = 8
    FRgb332 = 11
    FRgb5 = 10
    FRgb8 = 9
    FRgba = 1
    FRgba12 = 3
    FRgba4 = 5
    FRgba5 = 6
    FRgba8 = 4
    FRgbm = 2
    FSrgb = 19
    FSrgbAlpha = 20
    FTLinear = 2
    FTLinearMipmapLinear = 6
    FTLinearMipmapNearest = 4
    FTNearest = 1
    FTNearestMipmapLinear = 5
    FTNearestMipmapNearest = 3
    FTUnspecified = 0
    FT_linear = 2
    FT_linear_mipmap_linear = 6
    FT_linear_mipmap_nearest = 4
    FT_nearest = 1
    FT_nearest_mipmap_linear = 5
    FT_nearest_mipmap_nearest = 3
    FT_unspecified = 0
    FUnspecified = 0
    F_alpha = 15
    F_blue = 14
    F_green = 13
    F_luminance = 16
    F_luminance_alpha = 17
    F_luminance_alphamask = 18
    F_red = 12
    F_rgb = 7
    F_rgb12 = 8
    F_rgb332 = 11
    F_rgb5 = 10
    F_rgb8 = 9
    F_rgba = 1
    F_rgba12 = 3
    F_rgba4 = 5
    F_rgba5 = 6
    F_rgba8 = 4
    F_rgbm = 2
    F_srgb = 19
    F_srgb_alpha = 20
    F_unspecified = 0
    QLBest = 4
    QLDefault = 1
    QLFastest = 2
    QLNormal = 3
    QLUnspecified = 0
    QL_best = 4
    QL_default = 1
    QL_fastest = 2
    QL_normal = 3
    QL_unspecified = 0
    TGEyeCubeMap = 3
    TGEyeNormal = 5
    TGEyePosition = 7
    TGEyeSphereMap = 1
    TGPointSprite = 8
    TGUnspecified = 0
    TGWorldCubeMap = 2
    TGWorldNormal = 4
    TGWorldPosition = 6
    TG_eye_cube_map = 3
    TG_eye_normal = 5
    TG_eye_position = 7
    TG_eye_sphere_map = 1
    TG_point_sprite = 8
    TG_unspecified = 0
    TG_world_cube_map = 2
    TG_world_normal = 4
    TG_world_position = 6
    TT1dTexture = 1
    TT2dTexture = 2
    TT3dTexture = 3
    TTCubeMap = 4
    TTUnspecified = 0
    TT_1d_texture = 1
    TT_2d_texture = 2
    TT_3d_texture = 3
    TT_cube_map = 4
    TT_unspecified = 0
    WMBorderColor = 5
    WMClamp = 1
    WMMirror = 3
    WMMirrorOnce = 4
    WMRepeat = 2
    WMUnspecified = 0
    WM_border_color = 5
    WM_clamp = 1
    WM_mirror = 3
    WM_mirror_once = 4
    WM_repeat = 2
    WM_unspecified = 0


