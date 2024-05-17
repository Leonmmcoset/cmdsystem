# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .TypedWritableReferenceCount import TypedWritableReferenceCount

from .Namable import Namable

class Texture(TypedWritableReferenceCount, Namable):
    """
    /**
     * Represents a texture object, which is typically a single 2-d image but may
     * also represent a 1-d or 3-d texture image, or the six 2-d faces of a cube
     * map texture.
     *
     * A texture's image data might be stored in system RAM (see get_ram_image())
     * or its image may be represented in texture memory on one or more
     * GraphicsStateGuardians (see prepare()), or both.  The typical usage pattern
     * is that a texture is loaded from an image file on disk, which copies its
     * image data into system RAM; then the first time the texture is rendered its
     * image data is copied to texture memory (actually, to the graphics API), and
     * the system RAM image is automatically freed.
     */
    """
    def clear(self, const_Texture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear(const Texture self)
        
        /**
         * Reinitializes the texture to its default, empty state (except for the
         * name).
         */
        """
        pass

    def clearAlphaFilename(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_alpha_filename(const Texture self)
        
        /**
         * Removes the alpha filename, if it was previously set.  See
         * set_alpha_filename().
         */
        """
        pass

    def clearAlphaFullpath(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_alpha_fullpath(const Texture self)
        
        /**
         * Removes the alpha fullpath, if it was previously set.  See
         * set_alpha_fullpath().
         */
        """
        pass

    def clearAuxData(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_aux_data(const Texture self, str key)
        
        /**
         * Removes a record previously recorded via set_aux_data().
         */
        """
        pass

    def clearClearColor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_clear_color(const Texture self)
        
        /**
         * The opposite of set_clear_color.  If the image is cleared after setting
         * this, its contents may be undefined (or may in fact not be cleared at all).
         */
        """
        pass

    def clearFilename(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_filename(const Texture self)
        
        /**
         * Removes the alpha filename, if it was previously set.  See set_filename().
         */
        """
        pass

    def clearFullpath(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_fullpath(const Texture self)
        
        /**
         * Removes the alpha fullpath, if it was previously set.  See set_fullpath().
         */
        """
        pass

    def clearImage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_image(const Texture self)
        
        /**
         * Clears the texture data without changing its format or resolution.  The
         * texture is cleared on both the graphics hardware and from RAM, unlike
         * clear_ram_image, which only removes the data from RAM.
         *
         * If a clear color has been specified using set_clear_color, the texture will
         * be cleared using a solid color.
         *
         * The texture data will be cleared the first time in which the texture is
         * used after this method is called.
         */
        """
        pass

    def clearRamImage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_ram_image(const Texture self)
        
        /**
         * Discards the current system-RAM image.
         */
        """
        pass

    def clearRamMipmapImage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_ram_mipmap_image(const Texture self, int n)
        
        /**
         * Discards the current system-RAM image for the nth mipmap level.
         */
        """
        pass

    def clearRamMipmapImages(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_ram_mipmap_images(const Texture self)
        
        /**
         * Discards the current system-RAM image for all mipmap levels, except level 0
         * (the base image).
         */
        """
        pass

    def clearSimpleRamImage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_simple_ram_image(const Texture self)
        
        /**
         * Discards the current "simple" image.
         */
        """
        pass

    def clear_alpha_filename(self, const_Texture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_alpha_filename(const Texture self)
        
        /**
         * Removes the alpha filename, if it was previously set.  See
         * set_alpha_filename().
         */
        """
        pass

    def clear_alpha_fullpath(self, const_Texture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_alpha_fullpath(const Texture self)
        
        /**
         * Removes the alpha fullpath, if it was previously set.  See
         * set_alpha_fullpath().
         */
        """
        pass

    def clear_aux_data(self, const_Texture_self, str_key): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_aux_data(const Texture self, str key)
        
        /**
         * Removes a record previously recorded via set_aux_data().
         */
        """
        pass

    def clear_clear_color(self, const_Texture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_clear_color(const Texture self)
        
        /**
         * The opposite of set_clear_color.  If the image is cleared after setting
         * this, its contents may be undefined (or may in fact not be cleared at all).
         */
        """
        pass

    def clear_filename(self, const_Texture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_filename(const Texture self)
        
        /**
         * Removes the alpha filename, if it was previously set.  See set_filename().
         */
        """
        pass

    def clear_fullpath(self, const_Texture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_fullpath(const Texture self)
        
        /**
         * Removes the alpha fullpath, if it was previously set.  See set_fullpath().
         */
        """
        pass

    def clear_image(self, const_Texture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_image(const Texture self)
        
        /**
         * Clears the texture data without changing its format or resolution.  The
         * texture is cleared on both the graphics hardware and from RAM, unlike
         * clear_ram_image, which only removes the data from RAM.
         *
         * If a clear color has been specified using set_clear_color, the texture will
         * be cleared using a solid color.
         *
         * The texture data will be cleared the first time in which the texture is
         * used after this method is called.
         */
        """
        pass

    def clear_ram_image(self, const_Texture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_ram_image(const Texture self)
        
        /**
         * Discards the current system-RAM image.
         */
        """
        pass

    def clear_ram_mipmap_image(self, const_Texture_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_ram_mipmap_image(const Texture self, int n)
        
        /**
         * Discards the current system-RAM image for the nth mipmap level.
         */
        """
        pass

    def clear_ram_mipmap_images(self, const_Texture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_ram_mipmap_images(const Texture self)
        
        /**
         * Discards the current system-RAM image for all mipmap levels, except level 0
         * (the base image).
         */
        """
        pass

    def clear_simple_ram_image(self, const_Texture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_simple_ram_image(const Texture self)
        
        /**
         * Discards the current "simple" image.
         */
        """
        pass

    def compressRamImage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        compress_ram_image(const Texture self, int compression, int quality_level, GraphicsStateGuardianBase gsg)
        
        /**
         * Attempts to compress the texture's RAM image internally, to a format
         * supported by the indicated GSG.  In order for this to work, the squish
         * library must have been compiled into Panda.
         *
         * If compression is CM_on, then an appropriate compression method that is
         * supported by the indicated GSG is automatically chosen.  If the GSG pointer
         * is NULL, any of the standard DXT1/3/5 compression methods will be used,
         * regardless of whether it is supported.
         *
         * If compression is any specific compression method, that method is used
         * regardless of whether the GSG supports it.
         *
         * quality_level determines the speed/quality tradeoff of the compression.  If
         * it is QL_default, the texture's own quality_level parameter is used.
         *
         * Returns true if successful, false otherwise.
         */
        """
        pass

    def compress_ram_image(self, const_Texture_self, int_compression, int_quality_level, GraphicsStateGuardianBase_gsg): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        compress_ram_image(const Texture self, int compression, int quality_level, GraphicsStateGuardianBase gsg)
        
        /**
         * Attempts to compress the texture's RAM image internally, to a format
         * supported by the indicated GSG.  In order for this to work, the squish
         * library must have been compiled into Panda.
         *
         * If compression is CM_on, then an appropriate compression method that is
         * supported by the indicated GSG is automatically chosen.  If the GSG pointer
         * is NULL, any of the standard DXT1/3/5 compression methods will be used,
         * regardless of whether it is supported.
         *
         * If compression is any specific compression method, that method is used
         * regardless of whether the GSG supports it.
         *
         * quality_level determines the speed/quality tradeoff of the compression.  If
         * it is QL_default, the texture's own quality_level parameter is used.
         *
         * Returns true if successful, false otherwise.
         */
        """
        pass

    def considerRescale(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        consider_rescale(const Texture self, PNMImage pnmimage)
        consider_rescale(PNMImage pnmimage, str name, int auto_texture_scale)
        
        /**
         * Asks the PNMImage to change its scale when it reads the image, according to
         * the whims of the Config.prc file.
         *
         * For most efficient results, this method should be called after
         * pnmimage.read_header() has been called, but before pnmimage.read().  This
         * method may also be called after pnmimage.read(), i.e.  when the pnmimage is
         * already loaded; in this case it will rescale the image on the spot.  Also
         * see rescale_texture().
         */
        
        /**
         * Asks the PNMImage to change its scale when it reads the image, according to
         * the whims of the Config.prc file.
         *
         * For most efficient results, this method should be called after
         * pnmimage.read_header() has been called, but before pnmimage.read().  This
         * method may also be called after pnmimage.read(), i.e.  when the pnmimage is
         * already loaded; in this case it will rescale the image on the spot.  Also
         * see rescale_texture().
         */
        """
        pass

    def consider_rescale(self, const_Texture_self, PNMImage_pnmimage): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        consider_rescale(const Texture self, PNMImage pnmimage)
        consider_rescale(PNMImage pnmimage, str name, int auto_texture_scale)
        
        /**
         * Asks the PNMImage to change its scale when it reads the image, according to
         * the whims of the Config.prc file.
         *
         * For most efficient results, this method should be called after
         * pnmimage.read_header() has been called, but before pnmimage.read().  This
         * method may also be called after pnmimage.read(), i.e.  when the pnmimage is
         * already loaded; in this case it will rescale the image on the spot.  Also
         * see rescale_texture().
         */
        
        /**
         * Asks the PNMImage to change its scale when it reads the image, according to
         * the whims of the Config.prc file.
         *
         * For most efficient results, this method should be called after
         * pnmimage.read_header() has been called, but before pnmimage.read().  This
         * method may also be called after pnmimage.read(), i.e.  when the pnmimage is
         * already loaded; in this case it will rescale the image on the spot.  Also
         * see rescale_texture().
         */
        """
        pass

    def downToPower2(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        down_to_power_2(int value)
        
        /**
         * Returns the largest power of 2 less than or equal to value.
         */
        """
        pass

    def down_to_power_2(self, int_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        down_to_power_2(int value)
        
        /**
         * Returns the largest power of 2 less than or equal to value.
         */
        """
        pass

    def estimateTextureMemory(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        estimate_texture_memory(Texture self)
        
        /**
         * Estimates the amount of texture memory that will be consumed by loading
         * this texture.  This returns a value that is not specific to any particular
         * graphics card or driver; it tries to make a reasonable assumption about how
         * a driver will load the texture.  It does not account for texture
         * compression or anything fancy.  This is mainly useful for debugging and
         * reporting purposes.
         *
         * Returns a value in bytes.
         */
        """
        pass

    def estimate_texture_memory(self, Texture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        estimate_texture_memory(Texture self)
        
        /**
         * Estimates the amount of texture memory that will be consumed by loading
         * this texture.  This returns a value that is not specific to any particular
         * graphics card or driver; it tries to make a reasonable assumption about how
         * a driver will load the texture.  It does not account for texture
         * compression or anything fancy.  This is mainly useful for debugging and
         * reporting purposes.
         *
         * Returns a value in bytes.
         */
        """
        pass

    def formatComponentType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        format_component_type(int ct)
        
        /**
         * Returns the indicated ComponentType converted to a string word.
         */
        """
        pass

    def formatCompressionMode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        format_compression_mode(int cm)
        
        /**
         * Returns the indicated CompressionMode converted to a string word.
         */
        """
        pass

    def formatFormat(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        format_format(int f)
        
        /**
         * Returns the indicated Format converted to a string word.
         */
        """
        pass

    def formatQualityLevel(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        format_quality_level(int tql)
        
        /**
         * Returns the indicated QualityLevel converted to a string word.
         */
        """
        pass

    def formatTextureType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        format_texture_type(int tt)
        
        /**
         * Returns the indicated TextureType converted to a string word.
         */
        """
        pass

    def format_component_type(self, int_ct): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        format_component_type(int ct)
        
        /**
         * Returns the indicated ComponentType converted to a string word.
         */
        """
        pass

    def format_compression_mode(self, int_cm): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        format_compression_mode(int cm)
        
        /**
         * Returns the indicated CompressionMode converted to a string word.
         */
        """
        pass

    def format_format(self, int_f): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        format_format(int f)
        
        /**
         * Returns the indicated Format converted to a string word.
         */
        """
        pass

    def format_quality_level(self, int_tql): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        format_quality_level(int tql)
        
        /**
         * Returns the indicated QualityLevel converted to a string word.
         */
        """
        pass

    def format_texture_type(self, int_tt): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        format_texture_type(int tt)
        
        /**
         * Returns the indicated TextureType converted to a string word.
         */
        """
        pass

    def generateAlphaScaleMap(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        generate_alpha_scale_map(const Texture self)
        
        /**
         * Generates a special 256x1 1-d texture that can be used to apply an
         * arbitrary alpha scale to objects by judicious use of texture matrix.  The
         * texture is a gradient, with an alpha of 0 on the left (U = 0), and 255 on
         * the right (U = 1).
         */
        """
        pass

    def generateNormalizationCubeMap(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        generate_normalization_cube_map(const Texture self, int size)
        
        /**
         * Generates a special cube map image in the texture that can be used to apply
         * bump mapping effects: for each texel in the cube map that is indexed by the
         * 3-d texture coordinates (x, y, z), the resulting value is the normalized
         * vector (x, y, z) (compressed from -1..1 into 0..1).
         */
        """
        pass

    def generateRamMipmapImages(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        generate_ram_mipmap_images(const Texture self)
        
        /**
         * Automatically fills in the n mipmap levels of the Texture, based on the
         * texture's source image.  This requires the texture's uncompressed ram image
         * to be available in system memory.  If it is not already, it will be fetched
         * if possible.
         *
         * This call is not normally necessary, since the mipmap levels will be
         * generated automatically if needed.  But there may be certain cases in which
         * you would like to call this explicitly.
         */
        """
        pass

    def generateSimpleRamImage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        generate_simple_ram_image(const Texture self)
        
        /**
         * Computes the "simple" ram image by loading the main RAM image, if it is not
         * already available, and reducing it to 16x16 or smaller.  This may be an
         * expensive operation.
         */
        """
        pass

    def generate_alpha_scale_map(self, const_Texture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        generate_alpha_scale_map(const Texture self)
        
        /**
         * Generates a special 256x1 1-d texture that can be used to apply an
         * arbitrary alpha scale to objects by judicious use of texture matrix.  The
         * texture is a gradient, with an alpha of 0 on the left (U = 0), and 255 on
         * the right (U = 1).
         */
        """
        pass

    def generate_normalization_cube_map(self, const_Texture_self, int_size): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        generate_normalization_cube_map(const Texture self, int size)
        
        /**
         * Generates a special cube map image in the texture that can be used to apply
         * bump mapping effects: for each texel in the cube map that is indexed by the
         * 3-d texture coordinates (x, y, z), the resulting value is the normalized
         * vector (x, y, z) (compressed from -1..1 into 0..1).
         */
        """
        pass

    def generate_ram_mipmap_images(self, const_Texture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        generate_ram_mipmap_images(const Texture self)
        
        /**
         * Automatically fills in the n mipmap levels of the Texture, based on the
         * texture's source image.  This requires the texture's uncompressed ram image
         * to be available in system memory.  If it is not already, it will be fetched
         * if possible.
         *
         * This call is not normally necessary, since the mipmap levels will be
         * generated automatically if needed.  But there may be certain cases in which
         * you would like to call this explicitly.
         */
        """
        pass

    def generate_simple_ram_image(self, const_Texture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        generate_simple_ram_image(const Texture self)
        
        /**
         * Computes the "simple" ram image by loading the main RAM image, if it is not
         * already available, and reducing it to 16x16 or smaller.  This may be an
         * expensive operation.
         */
        """
        pass

    def getActive(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_active(Texture self, PreparedGraphicsObjects prepared_objects)
        
        /**
         * Returns true if this Texture was rendered in the most recent frame within
         * the indicated GSG.
         */
        """
        pass

    def getAlphaFilename(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_alpha_filename(Texture self)
        
        /**
         * Returns the alpha_filename that has been set.  If this is set, it
         * represents the name of the alpha component, which is stored in a separate
         * file.  See also get_filename(), and get_alpha_fullpath().
         */
        """
        pass

    def getAlphaFullpath(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_alpha_fullpath(Texture self)
        
        /**
         *
         * Returns the alpha_fullpath that has been set.  This is the full path to the
         * alpha part of the image file as it was found along the texture search path.
         */
        """
        pass

    def getAnisotropicDegree(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_anisotropic_degree(Texture self)
        
        /**
         * Returns the degree of anisotropic filtering that should be applied to the
         * texture.  This value may return 0, indicating the default value; see also
         * get_effective_anisotropic_degree.
         *
         * This returns the default sampler state for this texture; it may still be
         * overridden by a sampler state specified at a higher level.
         */
        """
        pass

    def getAutoTextureScale(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_auto_texture_scale(Texture self)
        
        /**
         * Returns the power-of-2 texture-scaling mode that will be applied to this
         * particular texture when it is next loaded from disk.  See
         * set_textures_power_2().
         */
        """
        pass

    def getAuxData(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_aux_data(Texture self, str key)
        
        /**
         * Returns a record previously recorded via set_aux_data().  Returns NULL if
         * there was no record associated with the indicated key.
         */
        """
        pass

    def getBorderColor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_border_color(Texture self)
        
        /**
         * Returns the solid color of the texture's border.  Some OpenGL
         * implementations use a border for tiling textures; in Panda, it is only used
         * for specifying the clamp color.
         *
         * This returns the default sampler state for this texture; it may still be
         * overridden by a sampler state specified at a higher level.
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getClearColor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_clear_color(Texture self)
        
        /**
         * Returns the color that was previously set using set_clear_color.
         */
        """
        pass

    def getClearData(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_clear_data(Texture self)
        
        /**
         * Returns the raw image data for a single pixel if it were set to the clear
         * color.
         */
        """
        pass

    def getComponentType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_component_type(Texture self)
        
        /**
         * Returns the numeric interpretation of each component of the texture.
         */
        """
        pass

    def getComponentWidth(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_component_width(Texture self)
        
        /**
         * Returns the number of bytes stored for each color component of a texel.
         * Typically this is 1, but it may be 2 for 16-bit texels.
         */
        """
        pass

    def getCompression(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_compression(Texture self)
        
        /**
         * Returns the compression mode requested for this particular texture, or
         * CM_off if the texture is not to be compressed.
         *
         * If a value other than CM_off is returned, this is not a guarantee that the
         * texture is actually successfully compressed on the GSG.  It may be that the
         * GSG does not support the requested compression mode, in which case the
         * texture may actually be stored uncompressed in texture memory.
         */
        """
        pass

    def getDataSizeBytes(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_data_size_bytes(Texture self, PreparedGraphicsObjects prepared_objects)
        
        /**
         * Returns the number of bytes which the texture is reported to consume within
         * graphics memory, for the indicated GSG.  This may return a nonzero value
         * even if the texture is not currently resident; you should also check
         * get_resident() if you want to know how much space the texture is actually
         * consuming right now.
         */
        """
        pass

    def getDefaultSampler(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_default_sampler(Texture self)
        
        /**
         * This returns the default sampler state for this texture, containing the
         * wrap and filter properties specified on the texture level; it may still be
         * overridden by a sampler state specified at a higher level.
         */
        """
        pass

    def getEffectiveAnisotropicDegree(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_effective_anisotropic_degree(Texture self)
        
        /**
         * Returns the degree of anisotropic filtering that should be applied to the
         * texture.  This value will normally not return 0, unless there is an error
         * in the config file.
         *
         * This returns the default sampler state for this texture; it may still be
         * overridden by a sampler state specified at a higher level.
         */
        """
        pass

    def getEffectiveMagfilter(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_effective_magfilter(Texture self)
        
        /**
         * Returns the filter mode of the texture for magnification, with special
         * treatment for FT_default.  This will normally not return FT_default, unless
         * there is an error in the config file.
         *
         * This returns the default sampler state for this texture; it may still be
         * overridden by a sampler state specified at a higher level.
         */
        """
        pass

    def getEffectiveMinfilter(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_effective_minfilter(Texture self)
        
        /**
         * Returns the filter mode of the texture for minification, with special
         * treatment for FT_default.  This will normally not return FT_default, unless
         * there is an error in the config file.
         *
         * This returns the default sampler state for this texture; it may still be
         * overridden by a sampler state specified at a higher level.
         */
        """
        pass

    def getEffectiveQualityLevel(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_effective_quality_level(Texture self)
        
        /**
         * Returns the current quality_level hint, or the global default quality_level
         * if this texture doesn't specify a quality level.  This value will not
         * normally return QL_default (unless there is an error in the config file)
         */
        """
        pass

    def getExpectedMipmapNumPages(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_expected_mipmap_num_pages(Texture self, int n)
        
        /**
         * Returns the total number of pages that the nth mipmap level should have,
         * based on the texture's size.  This is usually the same as
         * get_expected_mipmap_z_size(), except for a multiview texture, in which case
         * it is get_expected_mipmap_z_size() * get_num_views().
         */
        """
        pass

    def getExpectedMipmapXSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_expected_mipmap_x_size(Texture self, int n)
        
        /**
         * Returns the x_size that the nth mipmap level should have, based on the
         * texture's size.
         */
        """
        pass

    def getExpectedMipmapYSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_expected_mipmap_y_size(Texture self, int n)
        
        /**
         * Returns the y_size that the nth mipmap level should have, based on the
         * texture's size.
         */
        """
        pass

    def getExpectedMipmapZSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_expected_mipmap_z_size(Texture self, int n)
        
        /**
         * Returns the z_size that the nth mipmap level should have, based on the
         * texture's size.
         */
        """
        pass

    def getExpectedNumMipmapLevels(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_expected_num_mipmap_levels(Texture self)
        
        /**
         * Returns the number of mipmap levels that should be defined for this
         * texture, given the texture's size.
         *
         * Note that this returns a number appropriate for mipmapping, even if the
         * texture does not currently have mipmapping enabled.
         */
        """
        pass

    def getExpectedRamImageSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_expected_ram_image_size(Texture self)
        
        /**
         * Returns the number of bytes that *ought* to be used by the in-memory image,
         * based on the texture parameters.
         */
        """
        pass

    def getExpectedRamMipmapImageSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_expected_ram_mipmap_image_size(Texture self, int n)
        
        /**
         * Returns the number of bytes that *ought* to be used by the in-memory image
         * for mipmap level n, based on the texture parameters.
         */
        """
        pass

    def getExpectedRamMipmapPageSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_expected_ram_mipmap_page_size(Texture self, int n)
        
        /**
         * Returns the number of bytes that should be used per each Z page of the 3-d
         * texture, for mipmap level n.  For a 2-d or 1-d texture, this is the same as
         * get_expected_ram_mipmap_view_size(n).
         */
        """
        pass

    def getExpectedRamMipmapViewSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_expected_ram_mipmap_view_size(Texture self, int n)
        
        /**
         * Returns the number of bytes that *ought* to be used by each view of the in-
         * memory image for mipmap level n, based on the texture parameters.  For a
         * normal, non-multiview texture, this is the same as
         * get_expected_ram_mipmap_image_size(n).
         */
        """
        pass

    def getExpectedRamPageSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_expected_ram_page_size(Texture self)
        
        /**
         * Returns the number of bytes that should be used per each Z page of the 3-d
         * texture.  For a 2-d or 1-d texture, this is the same as
         * get_expected_ram_image_size().
         */
        """
        pass

    def getFilename(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_filename(Texture self)
        
        /**
         * Returns the filename that has been set.  This is the name of the file as it
         * was requested.  Also see get_fullpath().
         */
        """
        pass

    def getFormat(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_format(Texture self)
        
        /**
         * Returns the format of the texture, which represents both the semantic
         * meaning of the texels and, to some extent, their storage information.
         */
        """
        pass

    def getFullpath(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_fullpath(Texture self)
        
        /**
         * Returns the fullpath that has been set.  This is the full path to the file
         * as it was found along the texture search path.
         */
        """
        pass

    def getImageModified(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_image_modified(Texture self)
        
        /**
         * Returns a sequence number which is guaranteed to change at least every time
         * the texture image data (including mipmap levels) are modified.
         */
        """
        pass

    def getKeepRamImage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_keep_ram_image(Texture self)
        
        /**
         * Returns the flag that indicates whether this Texture is eligible to have
         * its main RAM copy of the texture memory dumped when the texture is prepared
         * for rendering.  See set_keep_ram_image().
         */
        """
        pass

    def getLoadedFromImage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_loaded_from_image(Texture self)
        
        /**
         * Returns the flag that indicates the texture has been loaded from a disk
         * file or PNMImage.  See set_loaded_from_image().
         */
        """
        pass

    def getLoadedFromTxo(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_loaded_from_txo(Texture self)
        
        /**
         * Returns the flag that indicates the texture has been loaded from a txo
         * file.
         */
        """
        pass

    def getMagfilter(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_magfilter(Texture self)
        
        /**
         * Returns the filter mode of the texture for magnification.  The mipmap
         * constants are invalid here.  This may return FT_default; see also
         * get_effective_minfilter().
         *
         * This returns the default sampler state for this texture; it may still be
         * overridden by a sampler state specified at a higher level.
         */
        """
        pass

    def getMatchFramebufferFormat(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_match_framebuffer_format(Texture self)
        
        /**
         * Returns true if the special flag was set that indicates to the GSG that the
         * Texture's format should be chosen to exactly match the framebuffer's
         * format, presumably because the application intends to copy image data from
         * the framebuffer into the Texture (or vice-versa).
         */
        """
        pass

    def getMinfilter(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_minfilter(Texture self)
        
        /**
         * Returns the filter mode of the texture for minification.  If this is one of
         * the mipmap constants, then the texture requires mipmaps.  This may return
         * FT_default; see also get_effective_minfilter().
         *
         * This returns the default sampler state for this texture; it may still be
         * overridden by a sampler state specified at a higher level.
         */
        """
        pass

    def getNumComponents(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_components(Texture self)
        
        /**
         * Returns the number of color components for each texel of the texture image.
         * This is 3 for an rgb texture or 4 for an rgba texture; it may also be 1 or
         * 2 for a grayscale texture.
         */
        """
        pass

    def getNumLoadableRamMipmapImages(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_loadable_ram_mipmap_images(Texture self)
        
        /**
         * Returns the number of contiguous mipmap levels that exist in RAM, up until
         * the first gap in the sequence.  It is guaranteed that at least mipmap
         * levels [0, get_num_ram_mipmap_images()) exist.
         *
         * The number returned will never exceed the number of required mipmap images
         * based on the size of the texture and its filter mode.
         *
         * This method is different from get_num_ram_mipmap_images() in that it
         * returns only the number of mipmap levels that can actually be usefully
         * loaded, regardless of the actual number that may be stored.
         */
        """
        pass

    def getNumPages(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_pages(Texture self)
        
        /**
         * Returns the total number of pages in the texture.  Each "page" is a 2-d
         * texture image within the larger image--a face of a cube map, or a level of
         * a 3-d texture.  Normally, get_num_pages() is the same as get_z_size().
         * However, in a multiview texture, this returns get_z_size() *
         * get_num_views().
         */
        """
        pass

    def getNumRamMipmapImages(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_ram_mipmap_images(Texture self)
        
        /**
         * Returns the maximum number of mipmap level images available in system
         * memory.  The actual number may be less than this (that is, there might be
         * gaps in the sequence); use has_ram_mipmap_image() to verify each level.
         *
         * Also see get_num_loadable_ram_mipmap_images().
         */
        """
        pass

    def getNumViews(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_views(Texture self)
        
        /**
         * Returns the number of "views" in the texture.  A view is a completely
         * separate image stored within the Texture object.  Most textures have only
         * one view, but a stereo texture, for instance, may have two views, a left
         * and a right image.  Other uses for multiple views are not yet defined.
         *
         * If this value is greater than one, the additional views are accessed as
         * additional pages beyond get_z_size().
         */
        """
        pass

    def getOrigFileXSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_orig_file_x_size(Texture self)
        
        /**
         * Returns the X size of the original disk image that this Texture was loaded
         * from (if it came from a disk file), before any automatic rescaling by
         * Panda.
         */
        """
        pass

    def getOrigFileYSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_orig_file_y_size(Texture self)
        
        /**
         * Returns the Y size of the original disk image that this Texture was loaded
         * from (if it came from a disk file), before any automatic rescaling by
         * Panda.
         */
        """
        pass

    def getOrigFileZSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_orig_file_z_size(Texture self)
        
        /**
         * Returns the Z size of the original disk image that this Texture was loaded
         * from (if it came from a disk file), before any automatic rescaling by
         * Panda.
         */
        """
        pass

    def getPadXSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_pad_x_size(Texture self)
        
        /**
         * Returns size of the pad region.  See set_pad_size.
         */
        """
        pass

    def getPadYSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_pad_y_size(Texture self)
        
        /**
         * Returns size of the pad region.  See set_pad_size.
         */
        """
        pass

    def getPadZSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_pad_z_size(Texture self)
        
        /**
         * Returns size of the pad region.  See set_pad_size.
         */
        """
        pass

    def getPostLoadStoreCache(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_post_load_store_cache(Texture self)
        
        /**
         * Returns the setting of the post_load_store_cache flag.  See
         * set_post_load_store_cache().
         */
        """
        pass

    def getPropertiesModified(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_properties_modified(Texture self)
        
        /**
         * Returns a sequence number which is guaranteed to change at least every time
         * the texture properties (unrelated to the image) are modified.
         */
        """
        pass

    def getQualityLevel(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_quality_level(Texture self)
        
        /**
         * Returns the current quality_level hint.  See set_quality_level().  This
         * value may return QL_default; see get_effective_quality_level().
         */
        """
        pass

    def getRamImage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_ram_image(const Texture self)
        
        /**
         * Returns the system-RAM image data associated with the texture.  If the
         * texture does not currently have an associated RAM image, and the texture
         * was generated by loading an image from a disk file (the most common case),
         * this forces the reload of the same texture.  This can happen if
         * keep_texture_ram is configured to false, and we have previously prepared
         * this texture with a GSG.
         *
         * Note that it is not correct to call has_ram_image() first to test whether
         * this function will fail.  A false return value from has_ram_image()
         * indicates only that get_ram_image() may need to reload the texture from
         * disk, which it will do automatically.  However, you can call
         * might_have_ram_image(), which will return true if the ram image exists, or
         * there is a reasonable reason to believe it can be loaded.
         *
         * On the other hand, it is possible that the texture cannot be found on disk
         * or is otherwise unavailable.  If that happens, this function will return
         * NULL. There is no way to predict with 100% accuracy whether get_ram_image()
         * will return NULL without calling it first; might_have_ram_image() is the
         * closest.
         */
        """
        pass

    def getRamImageAs(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_ram_image_as(const Texture self, str requested_format)
        
        /**
         * Returns the uncompressed system-RAM image data associated with the texture.
         * Rather than just returning a pointer to the data, like
         * get_uncompressed_ram_image, this function first processes the data and
         * reorders the components using the specified format string, and places these
         * into a new char array.
         *
         * The 'format' argument should specify in which order the components of the
         * texture must be.  For example, valid format strings are "RGBA", "GA",
         * "ABRG" or "AAA".  A component can also be written as "0" or "1", which
         * means an empty/black or a full/white channel, respectively.
         *
         * This function is particularly useful to copy an image in-memory to a
         * different library (for example, PIL or wxWidgets) that require a different
         * component order than Panda's internal format, BGRA. Note, however, that
         * this conversion can still be too slow if you want to do it every frame, and
         * should thus be avoided for that purpose.
         *
         * The only requirement for the reordering is that an uncompressed image must
         * be available.  If the RAM image is compressed, it will attempt to re-load
         * the texture from disk, if it doesn't find an uncompressed image there, it
         * will return NULL.
         */
        """
        pass

    def getRamImageCompression(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_ram_image_compression(Texture self)
        
        /**
         * Returns the compression mode in which the ram image is already stored pre-
         * compressed.  If this is other than CM_off, you cannot rely on the contents
         * of the ram image to be anything predicatable (it will not be an array of x
         * by y pixels, and it probably won't have the same length as
         * get_expected_ram_image_size()).
         */
        """
        pass

    def getRamImageSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_ram_image_size(Texture self)
        
        /**
         * Returns the total number of bytes used by the in-memory image, across all
         * pages and views, or 0 if there is no in-memory image.
         */
        """
        pass

    def getRamMipmapImage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_ram_mipmap_image(Texture self, int n)
        
        /**
         * Returns the system-RAM image data associated with the nth mipmap level, if
         * present.  Returns NULL if the nth mipmap level is not present.
         */
        """
        pass

    def getRamMipmapImageSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_ram_mipmap_image_size(Texture self, int n)
        
        /**
         * Returns the number of bytes used by the in-memory image for mipmap level n,
         * or 0 if there is no in-memory image for this mipmap level.
         */
        """
        pass

    def getRamMipmapPageSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_ram_mipmap_page_size(Texture self, int n)
        
        /**
         * Returns the number of bytes used by the in-memory image per page for mipmap
         * level n, or 0 if there is no in-memory image for this mipmap level.
         *
         * For a non-compressed texture, this is the same as
         * get_expected_ram_mipmap_page_size().  For a compressed texture, this may be
         * a smaller value.  (We do assume that all pages will be the same size on a
         * compressed texture).
         */
        """
        pass

    def getRamMipmapViewSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_ram_mipmap_view_size(Texture self, int n)
        
        /**
         * Returns the number of bytes used by the in-memory image per view for mipmap
         * level n, or 0 if there is no in-memory image for this mipmap level.
         *
         * A "view" is a collection of z_size pages for each mipmap level.  Most
         * textures have only one view, except for multiview or stereo textures.
         *
         * For a non-compressed texture, this is the same as
         * get_expected_ram_mipmap_view_size().  For a compressed texture, this may be
         * a smaller value.  (We do assume that all pages will be the same size on a
         * compressed texture).
         */
        """
        pass

    def getRamPageSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_ram_page_size(Texture self)
        
        /**
         * Returns the number of bytes used by the in-memory image per page, or 0 if
         * there is no in-memory image.
         *
         * For a non-compressed texture, this is the same as
         * get_expected_ram_page_size().  For a compressed texture, this may be a
         * smaller value.  (We do assume that all pages will be the same size on a
         * compressed texture).
         */
        """
        pass

    def getRamViewSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_ram_view_size(Texture self)
        
        /**
         * Returns the number of bytes used by the in-memory image per view, or 0 if
         * there is no in-memory image.  Since each view is a stack of z_size pages,
         * this is get_z_size() * get_ram_page_size().
         */
        """
        pass

    def getRenderToTexture(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_render_to_texture(Texture self)
        
        /**
         * Returns a flag on the texture that indicates whether the texture is
         * intended to be used as a direct-render target, by binding a framebuffer to
         * a texture and rendering directly into the texture.
         *
         * Normally, a user should not need to set this flag directly; it is set
         * automatically by the low-level display code when a texture is bound to a
         * framebuffer.
         */
        """
        pass

    def getResident(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_resident(Texture self, PreparedGraphicsObjects prepared_objects)
        
        /**
         * Returns true if this Texture is reported to be resident within graphics
         * memory for the indicated GSG.
         */
        """
        pass

    def getSimpleImageModified(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_simple_image_modified(Texture self)
        
        /**
         * Returns a sequence number which is guaranteed to change at least every time
         * the texture's "simple" image data is modified.
         */
        """
        pass

    def getSimpleRamImage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_simple_ram_image(Texture self)
        
        /**
         * Returns the image data associated with the "simple" texture image.  This is
         * provided for some textures as an option to display while the main texture
         * image is being loaded from disk.
         *
         * Unlike get_ram_image(), this function will always return immediately.
         * Either the simple image is available, or it is not.
         *
         * The "simple" image is always 4 components, 1 byte each, regardless of the
         * parameters of the full texture.  The simple image is only supported for
         * ordinary 2-d textures.
         */
        """
        pass

    def getSimpleRamImageSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_simple_ram_image_size(Texture self)
        
        /**
         * Returns the number of bytes used by the "simple" image, or 0 if there is no
         * simple image.
         */
        """
        pass

    def getSimpleXSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_simple_x_size(Texture self)
        
        /**
         * Returns the width of the "simple" image in texels.
         */
        """
        pass

    def getSimpleYSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_simple_y_size(Texture self)
        
        /**
         * Returns the height of the "simple" image in texels.
         */
        """
        pass

    def getTexScale(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_tex_scale(Texture self)
        
        /**
         * Returns a scale pair that is suitable for applying to geometry via
         * NodePath::set_tex_scale(), which will convert texture coordinates on the
         * geometry from the range 0..1 into the appropriate range to render the video
         * part of the texture.
         *
         * This is necessary only if a padding size has been set via set_pad_size()
         * (or implicitly via something like "textures-power-2 pad" in the config.prc
         * file).  In this case, this is a convenient way to generate UV's that
         * reflect the built-in padding size.
         */
        """
        pass

    def getTexturesPower2(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_textures_power_2()
        
        /**
         * This flag returns ATS_none, ATS_up, or ATS_down and controls the scaling of
         * textures in general.  It is initialized from the config variable of the
         * same name, but it can be subsequently adjusted.  See also
         * get_auto_texture_scale().
         */
        """
        pass

    def getTextureType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_texture_type(Texture self)
        
        /**
         * Returns the overall interpretation of the texture.
         */
        """
        pass

    def getUncompressedRamImage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_uncompressed_ram_image(const Texture self)
        
        /**
         * Returns the system-RAM image associated with the texture, in an
         * uncompressed form if at all possible.
         *
         * If get_ram_image_compression() is CM_off, then the system-RAM image is
         * already uncompressed, and this returns the same thing as get_ram_image().
         *
         * If get_ram_image_compression() is anything else, then the system-RAM image
         * is compressed.  In this case, the image will be reloaded from the
         * *original* file (not from the cache), in the hopes that an uncompressed
         * image will be found there.
         *
         * If an uncompressed image cannot be found, returns NULL.
         */
        """
        pass

    def getUsageHint(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_usage_hint(Texture self)
        
        /**
         * Returns the usage hint specified for buffer textures, or UH_unspecified for
         * all other texture types.
         */
        """
        pass

    def getWrapU(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_wrap_u(Texture self)
        
        /**
         * Returns the wrap mode of the texture in the U direction.
         *
         * This returns the default sampler state for this texture; it may still be
         * overridden by a sampler state specified at a higher level.
         */
        """
        pass

    def getWrapV(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_wrap_v(Texture self)
        
        /**
         * Returns the wrap mode of the texture in the V direction.
         *
         * This returns the default sampler state for this texture; it may still be
         * overridden by a sampler state specified at a higher level.
         */
        """
        pass

    def getWrapW(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_wrap_w(Texture self)
        
        /**
         * Returns the wrap mode of the texture in the W direction.  This is the depth
         * direction of 3-d textures.
         *
         * This returns the default sampler state for this texture; it may still be
         * overridden by a sampler state specified at a higher level.
         */
        """
        pass

    def getXSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_x_size(Texture self)
        
        /**
         * Returns the width of the texture image in texels.
         */
        """
        pass

    def getYSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_y_size(Texture self)
        
        /**
         * Returns the height of the texture image in texels.  For a 1-d texture, this
         * will be 1.
         */
        """
        pass

    def getZSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_z_size(Texture self)
        
        /**
         * Returns the depth of the texture image in texels.  For a 1-d texture or 2-d
         * texture, this will be 1. For a cube map texture, this will be 6.
         */
        """
        pass

    def get_active(self, Texture_self, PreparedGraphicsObjects_prepared_objects): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_active(Texture self, PreparedGraphicsObjects prepared_objects)
        
        /**
         * Returns true if this Texture was rendered in the most recent frame within
         * the indicated GSG.
         */
        """
        pass

    def get_alpha_filename(self, Texture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_alpha_filename(Texture self)
        
        /**
         * Returns the alpha_filename that has been set.  If this is set, it
         * represents the name of the alpha component, which is stored in a separate
         * file.  See also get_filename(), and get_alpha_fullpath().
         */
        """
        pass

    def get_alpha_fullpath(self, Texture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_alpha_fullpath(Texture self)
        
        /**
         *
         * Returns the alpha_fullpath that has been set.  This is the full path to the
         * alpha part of the image file as it was found along the texture search path.
         */
        """
        pass

    def get_anisotropic_degree(self, Texture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_anisotropic_degree(Texture self)
        
        /**
         * Returns the degree of anisotropic filtering that should be applied to the
         * texture.  This value may return 0, indicating the default value; see also
         * get_effective_anisotropic_degree.
         *
         * This returns the default sampler state for this texture; it may still be
         * overridden by a sampler state specified at a higher level.
         */
        """
        pass

    def get_auto_texture_scale(self, Texture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_auto_texture_scale(Texture self)
        
        /**
         * Returns the power-of-2 texture-scaling mode that will be applied to this
         * particular texture when it is next loaded from disk.  See
         * set_textures_power_2().
         */
        """
        pass

    def get_aux_data(self, Texture_self, str_key): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_aux_data(Texture self, str key)
        
        /**
         * Returns a record previously recorded via set_aux_data().  Returns NULL if
         * there was no record associated with the indicated key.
         */
        """
        pass

    def get_border_color(self, Texture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_border_color(Texture self)
        
        /**
         * Returns the solid color of the texture's border.  Some OpenGL
         * implementations use a border for tiling textures; in Panda, it is only used
         * for specifying the clamp color.
         *
         * This returns the default sampler state for this texture; it may still be
         * overridden by a sampler state specified at a higher level.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_clear_color(self, Texture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_clear_color(Texture self)
        
        /**
         * Returns the color that was previously set using set_clear_color.
         */
        """
        pass

    def get_clear_data(self, Texture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_clear_data(Texture self)
        
        /**
         * Returns the raw image data for a single pixel if it were set to the clear
         * color.
         */
        """
        pass

    def get_component_type(self, Texture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_component_type(Texture self)
        
        /**
         * Returns the numeric interpretation of each component of the texture.
         */
        """
        pass

    def get_component_width(self, Texture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_component_width(Texture self)
        
        /**
         * Returns the number of bytes stored for each color component of a texel.
         * Typically this is 1, but it may be 2 for 16-bit texels.
         */
        """
        pass

    def get_compression(self, Texture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_compression(Texture self)
        
        /**
         * Returns the compression mode requested for this particular texture, or
         * CM_off if the texture is not to be compressed.
         *
         * If a value other than CM_off is returned, this is not a guarantee that the
         * texture is actually successfully compressed on the GSG.  It may be that the
         * GSG does not support the requested compression mode, in which case the
         * texture may actually be stored uncompressed in texture memory.
         */
        """
        pass

    def get_data_size_bytes(self, Texture_self, PreparedGraphicsObjects_prepared_objects): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_data_size_bytes(Texture self, PreparedGraphicsObjects prepared_objects)
        
        /**
         * Returns the number of bytes which the texture is reported to consume within
         * graphics memory, for the indicated GSG.  This may return a nonzero value
         * even if the texture is not currently resident; you should also check
         * get_resident() if you want to know how much space the texture is actually
         * consuming right now.
         */
        """
        pass

    def get_default_sampler(self, Texture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_default_sampler(Texture self)
        
        /**
         * This returns the default sampler state for this texture, containing the
         * wrap and filter properties specified on the texture level; it may still be
         * overridden by a sampler state specified at a higher level.
         */
        """
        pass

    def get_effective_anisotropic_degree(self, Texture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_effective_anisotropic_degree(Texture self)
        
        /**
         * Returns the degree of anisotropic filtering that should be applied to the
         * texture.  This value will normally not return 0, unless there is an error
         * in the config file.
         *
         * This returns the default sampler state for this texture; it may still be
         * overridden by a sampler state specified at a higher level.
         */
        """
        pass

    def get_effective_magfilter(self, Texture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_effective_magfilter(Texture self)
        
        /**
         * Returns the filter mode of the texture for magnification, with special
         * treatment for FT_default.  This will normally not return FT_default, unless
         * there is an error in the config file.
         *
         * This returns the default sampler state for this texture; it may still be
         * overridden by a sampler state specified at a higher level.
         */
        """
        pass

    def get_effective_minfilter(self, Texture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_effective_minfilter(Texture self)
        
        /**
         * Returns the filter mode of the texture for minification, with special
         * treatment for FT_default.  This will normally not return FT_default, unless
         * there is an error in the config file.
         *
         * This returns the default sampler state for this texture; it may still be
         * overridden by a sampler state specified at a higher level.
         */
        """
        pass

    def get_effective_quality_level(self, Texture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_effective_quality_level(Texture self)
        
        /**
         * Returns the current quality_level hint, or the global default quality_level
         * if this texture doesn't specify a quality level.  This value will not
         * normally return QL_default (unless there is an error in the config file)
         */
        """
        pass

    def get_expected_mipmap_num_pages(self, Texture_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_expected_mipmap_num_pages(Texture self, int n)
        
        /**
         * Returns the total number of pages that the nth mipmap level should have,
         * based on the texture's size.  This is usually the same as
         * get_expected_mipmap_z_size(), except for a multiview texture, in which case
         * it is get_expected_mipmap_z_size() * get_num_views().
         */
        """
        pass

    def get_expected_mipmap_x_size(self, Texture_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_expected_mipmap_x_size(Texture self, int n)
        
        /**
         * Returns the x_size that the nth mipmap level should have, based on the
         * texture's size.
         */
        """
        pass

    def get_expected_mipmap_y_size(self, Texture_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_expected_mipmap_y_size(Texture self, int n)
        
        /**
         * Returns the y_size that the nth mipmap level should have, based on the
         * texture's size.
         */
        """
        pass

    def get_expected_mipmap_z_size(self, Texture_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_expected_mipmap_z_size(Texture self, int n)
        
        /**
         * Returns the z_size that the nth mipmap level should have, based on the
         * texture's size.
         */
        """
        pass

    def get_expected_num_mipmap_levels(self, Texture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_expected_num_mipmap_levels(Texture self)
        
        /**
         * Returns the number of mipmap levels that should be defined for this
         * texture, given the texture's size.
         *
         * Note that this returns a number appropriate for mipmapping, even if the
         * texture does not currently have mipmapping enabled.
         */
        """
        pass

    def get_expected_ram_image_size(self, Texture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_expected_ram_image_size(Texture self)
        
        /**
         * Returns the number of bytes that *ought* to be used by the in-memory image,
         * based on the texture parameters.
         */
        """
        pass

    def get_expected_ram_mipmap_image_size(self, Texture_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_expected_ram_mipmap_image_size(Texture self, int n)
        
        /**
         * Returns the number of bytes that *ought* to be used by the in-memory image
         * for mipmap level n, based on the texture parameters.
         */
        """
        pass

    def get_expected_ram_mipmap_page_size(self, Texture_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_expected_ram_mipmap_page_size(Texture self, int n)
        
        /**
         * Returns the number of bytes that should be used per each Z page of the 3-d
         * texture, for mipmap level n.  For a 2-d or 1-d texture, this is the same as
         * get_expected_ram_mipmap_view_size(n).
         */
        """
        pass

    def get_expected_ram_mipmap_view_size(self, Texture_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_expected_ram_mipmap_view_size(Texture self, int n)
        
        /**
         * Returns the number of bytes that *ought* to be used by each view of the in-
         * memory image for mipmap level n, based on the texture parameters.  For a
         * normal, non-multiview texture, this is the same as
         * get_expected_ram_mipmap_image_size(n).
         */
        """
        pass

    def get_expected_ram_page_size(self, Texture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_expected_ram_page_size(Texture self)
        
        /**
         * Returns the number of bytes that should be used per each Z page of the 3-d
         * texture.  For a 2-d or 1-d texture, this is the same as
         * get_expected_ram_image_size().
         */
        """
        pass

    def get_filename(self, Texture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_filename(Texture self)
        
        /**
         * Returns the filename that has been set.  This is the name of the file as it
         * was requested.  Also see get_fullpath().
         */
        """
        pass

    def get_format(self, Texture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_format(Texture self)
        
        /**
         * Returns the format of the texture, which represents both the semantic
         * meaning of the texels and, to some extent, their storage information.
         */
        """
        pass

    def get_fullpath(self, Texture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_fullpath(Texture self)
        
        /**
         * Returns the fullpath that has been set.  This is the full path to the file
         * as it was found along the texture search path.
         */
        """
        pass

    def get_image_modified(self, Texture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_image_modified(Texture self)
        
        /**
         * Returns a sequence number which is guaranteed to change at least every time
         * the texture image data (including mipmap levels) are modified.
         */
        """
        pass

    def get_keep_ram_image(self, Texture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_keep_ram_image(Texture self)
        
        /**
         * Returns the flag that indicates whether this Texture is eligible to have
         * its main RAM copy of the texture memory dumped when the texture is prepared
         * for rendering.  See set_keep_ram_image().
         */
        """
        pass

    def get_loaded_from_image(self, Texture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_loaded_from_image(Texture self)
        
        /**
         * Returns the flag that indicates the texture has been loaded from a disk
         * file or PNMImage.  See set_loaded_from_image().
         */
        """
        pass

    def get_loaded_from_txo(self, Texture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_loaded_from_txo(Texture self)
        
        /**
         * Returns the flag that indicates the texture has been loaded from a txo
         * file.
         */
        """
        pass

    def get_magfilter(self, Texture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_magfilter(Texture self)
        
        /**
         * Returns the filter mode of the texture for magnification.  The mipmap
         * constants are invalid here.  This may return FT_default; see also
         * get_effective_minfilter().
         *
         * This returns the default sampler state for this texture; it may still be
         * overridden by a sampler state specified at a higher level.
         */
        """
        pass

    def get_match_framebuffer_format(self, Texture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_match_framebuffer_format(Texture self)
        
        /**
         * Returns true if the special flag was set that indicates to the GSG that the
         * Texture's format should be chosen to exactly match the framebuffer's
         * format, presumably because the application intends to copy image data from
         * the framebuffer into the Texture (or vice-versa).
         */
        """
        pass

    def get_minfilter(self, Texture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_minfilter(Texture self)
        
        /**
         * Returns the filter mode of the texture for minification.  If this is one of
         * the mipmap constants, then the texture requires mipmaps.  This may return
         * FT_default; see also get_effective_minfilter().
         *
         * This returns the default sampler state for this texture; it may still be
         * overridden by a sampler state specified at a higher level.
         */
        """
        pass

    def get_num_components(self, Texture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_components(Texture self)
        
        /**
         * Returns the number of color components for each texel of the texture image.
         * This is 3 for an rgb texture or 4 for an rgba texture; it may also be 1 or
         * 2 for a grayscale texture.
         */
        """
        pass

    def get_num_loadable_ram_mipmap_images(self, Texture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_loadable_ram_mipmap_images(Texture self)
        
        /**
         * Returns the number of contiguous mipmap levels that exist in RAM, up until
         * the first gap in the sequence.  It is guaranteed that at least mipmap
         * levels [0, get_num_ram_mipmap_images()) exist.
         *
         * The number returned will never exceed the number of required mipmap images
         * based on the size of the texture and its filter mode.
         *
         * This method is different from get_num_ram_mipmap_images() in that it
         * returns only the number of mipmap levels that can actually be usefully
         * loaded, regardless of the actual number that may be stored.
         */
        """
        pass

    def get_num_pages(self, Texture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_pages(Texture self)
        
        /**
         * Returns the total number of pages in the texture.  Each "page" is a 2-d
         * texture image within the larger image--a face of a cube map, or a level of
         * a 3-d texture.  Normally, get_num_pages() is the same as get_z_size().
         * However, in a multiview texture, this returns get_z_size() *
         * get_num_views().
         */
        """
        pass

    def get_num_ram_mipmap_images(self, Texture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_ram_mipmap_images(Texture self)
        
        /**
         * Returns the maximum number of mipmap level images available in system
         * memory.  The actual number may be less than this (that is, there might be
         * gaps in the sequence); use has_ram_mipmap_image() to verify each level.
         *
         * Also see get_num_loadable_ram_mipmap_images().
         */
        """
        pass

    def get_num_views(self, Texture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_views(Texture self)
        
        /**
         * Returns the number of "views" in the texture.  A view is a completely
         * separate image stored within the Texture object.  Most textures have only
         * one view, but a stereo texture, for instance, may have two views, a left
         * and a right image.  Other uses for multiple views are not yet defined.
         *
         * If this value is greater than one, the additional views are accessed as
         * additional pages beyond get_z_size().
         */
        """
        pass

    def get_orig_file_x_size(self, Texture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_orig_file_x_size(Texture self)
        
        /**
         * Returns the X size of the original disk image that this Texture was loaded
         * from (if it came from a disk file), before any automatic rescaling by
         * Panda.
         */
        """
        pass

    def get_orig_file_y_size(self, Texture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_orig_file_y_size(Texture self)
        
        /**
         * Returns the Y size of the original disk image that this Texture was loaded
         * from (if it came from a disk file), before any automatic rescaling by
         * Panda.
         */
        """
        pass

    def get_orig_file_z_size(self, Texture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_orig_file_z_size(Texture self)
        
        /**
         * Returns the Z size of the original disk image that this Texture was loaded
         * from (if it came from a disk file), before any automatic rescaling by
         * Panda.
         */
        """
        pass

    def get_pad_x_size(self, Texture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_pad_x_size(Texture self)
        
        /**
         * Returns size of the pad region.  See set_pad_size.
         */
        """
        pass

    def get_pad_y_size(self, Texture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_pad_y_size(Texture self)
        
        /**
         * Returns size of the pad region.  See set_pad_size.
         */
        """
        pass

    def get_pad_z_size(self, Texture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_pad_z_size(Texture self)
        
        /**
         * Returns size of the pad region.  See set_pad_size.
         */
        """
        pass

    def get_post_load_store_cache(self, Texture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_post_load_store_cache(Texture self)
        
        /**
         * Returns the setting of the post_load_store_cache flag.  See
         * set_post_load_store_cache().
         */
        """
        pass

    def get_properties_modified(self, Texture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_properties_modified(Texture self)
        
        /**
         * Returns a sequence number which is guaranteed to change at least every time
         * the texture properties (unrelated to the image) are modified.
         */
        """
        pass

    def get_quality_level(self, Texture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_quality_level(Texture self)
        
        /**
         * Returns the current quality_level hint.  See set_quality_level().  This
         * value may return QL_default; see get_effective_quality_level().
         */
        """
        pass

    def get_ram_image(self, const_Texture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_ram_image(const Texture self)
        
        /**
         * Returns the system-RAM image data associated with the texture.  If the
         * texture does not currently have an associated RAM image, and the texture
         * was generated by loading an image from a disk file (the most common case),
         * this forces the reload of the same texture.  This can happen if
         * keep_texture_ram is configured to false, and we have previously prepared
         * this texture with a GSG.
         *
         * Note that it is not correct to call has_ram_image() first to test whether
         * this function will fail.  A false return value from has_ram_image()
         * indicates only that get_ram_image() may need to reload the texture from
         * disk, which it will do automatically.  However, you can call
         * might_have_ram_image(), which will return true if the ram image exists, or
         * there is a reasonable reason to believe it can be loaded.
         *
         * On the other hand, it is possible that the texture cannot be found on disk
         * or is otherwise unavailable.  If that happens, this function will return
         * NULL. There is no way to predict with 100% accuracy whether get_ram_image()
         * will return NULL without calling it first; might_have_ram_image() is the
         * closest.
         */
        """
        pass

    def get_ram_image_as(self, const_Texture_self, str_requested_format): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_ram_image_as(const Texture self, str requested_format)
        
        /**
         * Returns the uncompressed system-RAM image data associated with the texture.
         * Rather than just returning a pointer to the data, like
         * get_uncompressed_ram_image, this function first processes the data and
         * reorders the components using the specified format string, and places these
         * into a new char array.
         *
         * The 'format' argument should specify in which order the components of the
         * texture must be.  For example, valid format strings are "RGBA", "GA",
         * "ABRG" or "AAA".  A component can also be written as "0" or "1", which
         * means an empty/black or a full/white channel, respectively.
         *
         * This function is particularly useful to copy an image in-memory to a
         * different library (for example, PIL or wxWidgets) that require a different
         * component order than Panda's internal format, BGRA. Note, however, that
         * this conversion can still be too slow if you want to do it every frame, and
         * should thus be avoided for that purpose.
         *
         * The only requirement for the reordering is that an uncompressed image must
         * be available.  If the RAM image is compressed, it will attempt to re-load
         * the texture from disk, if it doesn't find an uncompressed image there, it
         * will return NULL.
         */
        """
        pass

    def get_ram_image_compression(self, Texture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_ram_image_compression(Texture self)
        
        /**
         * Returns the compression mode in which the ram image is already stored pre-
         * compressed.  If this is other than CM_off, you cannot rely on the contents
         * of the ram image to be anything predicatable (it will not be an array of x
         * by y pixels, and it probably won't have the same length as
         * get_expected_ram_image_size()).
         */
        """
        pass

    def get_ram_image_size(self, Texture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_ram_image_size(Texture self)
        
        /**
         * Returns the total number of bytes used by the in-memory image, across all
         * pages and views, or 0 if there is no in-memory image.
         */
        """
        pass

    def get_ram_mipmap_image(self, Texture_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_ram_mipmap_image(Texture self, int n)
        
        /**
         * Returns the system-RAM image data associated with the nth mipmap level, if
         * present.  Returns NULL if the nth mipmap level is not present.
         */
        """
        pass

    def get_ram_mipmap_image_size(self, Texture_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_ram_mipmap_image_size(Texture self, int n)
        
        /**
         * Returns the number of bytes used by the in-memory image for mipmap level n,
         * or 0 if there is no in-memory image for this mipmap level.
         */
        """
        pass

    def get_ram_mipmap_page_size(self, Texture_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_ram_mipmap_page_size(Texture self, int n)
        
        /**
         * Returns the number of bytes used by the in-memory image per page for mipmap
         * level n, or 0 if there is no in-memory image for this mipmap level.
         *
         * For a non-compressed texture, this is the same as
         * get_expected_ram_mipmap_page_size().  For a compressed texture, this may be
         * a smaller value.  (We do assume that all pages will be the same size on a
         * compressed texture).
         */
        """
        pass

    def get_ram_mipmap_view_size(self, Texture_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_ram_mipmap_view_size(Texture self, int n)
        
        /**
         * Returns the number of bytes used by the in-memory image per view for mipmap
         * level n, or 0 if there is no in-memory image for this mipmap level.
         *
         * A "view" is a collection of z_size pages for each mipmap level.  Most
         * textures have only one view, except for multiview or stereo textures.
         *
         * For a non-compressed texture, this is the same as
         * get_expected_ram_mipmap_view_size().  For a compressed texture, this may be
         * a smaller value.  (We do assume that all pages will be the same size on a
         * compressed texture).
         */
        """
        pass

    def get_ram_page_size(self, Texture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_ram_page_size(Texture self)
        
        /**
         * Returns the number of bytes used by the in-memory image per page, or 0 if
         * there is no in-memory image.
         *
         * For a non-compressed texture, this is the same as
         * get_expected_ram_page_size().  For a compressed texture, this may be a
         * smaller value.  (We do assume that all pages will be the same size on a
         * compressed texture).
         */
        """
        pass

    def get_ram_view_size(self, Texture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_ram_view_size(Texture self)
        
        /**
         * Returns the number of bytes used by the in-memory image per view, or 0 if
         * there is no in-memory image.  Since each view is a stack of z_size pages,
         * this is get_z_size() * get_ram_page_size().
         */
        """
        pass

    def get_render_to_texture(self, Texture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_render_to_texture(Texture self)
        
        /**
         * Returns a flag on the texture that indicates whether the texture is
         * intended to be used as a direct-render target, by binding a framebuffer to
         * a texture and rendering directly into the texture.
         *
         * Normally, a user should not need to set this flag directly; it is set
         * automatically by the low-level display code when a texture is bound to a
         * framebuffer.
         */
        """
        pass

    def get_resident(self, Texture_self, PreparedGraphicsObjects_prepared_objects): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_resident(Texture self, PreparedGraphicsObjects prepared_objects)
        
        /**
         * Returns true if this Texture is reported to be resident within graphics
         * memory for the indicated GSG.
         */
        """
        pass

    def get_simple_image_modified(self, Texture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_simple_image_modified(Texture self)
        
        /**
         * Returns a sequence number which is guaranteed to change at least every time
         * the texture's "simple" image data is modified.
         */
        """
        pass

    def get_simple_ram_image(self, Texture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_simple_ram_image(Texture self)
        
        /**
         * Returns the image data associated with the "simple" texture image.  This is
         * provided for some textures as an option to display while the main texture
         * image is being loaded from disk.
         *
         * Unlike get_ram_image(), this function will always return immediately.
         * Either the simple image is available, or it is not.
         *
         * The "simple" image is always 4 components, 1 byte each, regardless of the
         * parameters of the full texture.  The simple image is only supported for
         * ordinary 2-d textures.
         */
        """
        pass

    def get_simple_ram_image_size(self, Texture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_simple_ram_image_size(Texture self)
        
        /**
         * Returns the number of bytes used by the "simple" image, or 0 if there is no
         * simple image.
         */
        """
        pass

    def get_simple_x_size(self, Texture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_simple_x_size(Texture self)
        
        /**
         * Returns the width of the "simple" image in texels.
         */
        """
        pass

    def get_simple_y_size(self, Texture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_simple_y_size(Texture self)
        
        /**
         * Returns the height of the "simple" image in texels.
         */
        """
        pass

    def get_textures_power_2(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_textures_power_2()
        
        /**
         * This flag returns ATS_none, ATS_up, or ATS_down and controls the scaling of
         * textures in general.  It is initialized from the config variable of the
         * same name, but it can be subsequently adjusted.  See also
         * get_auto_texture_scale().
         */
        """
        pass

    def get_texture_type(self, Texture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_texture_type(Texture self)
        
        /**
         * Returns the overall interpretation of the texture.
         */
        """
        pass

    def get_tex_scale(self, Texture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_tex_scale(Texture self)
        
        /**
         * Returns a scale pair that is suitable for applying to geometry via
         * NodePath::set_tex_scale(), which will convert texture coordinates on the
         * geometry from the range 0..1 into the appropriate range to render the video
         * part of the texture.
         *
         * This is necessary only if a padding size has been set via set_pad_size()
         * (or implicitly via something like "textures-power-2 pad" in the config.prc
         * file).  In this case, this is a convenient way to generate UV's that
         * reflect the built-in padding size.
         */
        """
        pass

    def get_uncompressed_ram_image(self, const_Texture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_uncompressed_ram_image(const Texture self)
        
        /**
         * Returns the system-RAM image associated with the texture, in an
         * uncompressed form if at all possible.
         *
         * If get_ram_image_compression() is CM_off, then the system-RAM image is
         * already uncompressed, and this returns the same thing as get_ram_image().
         *
         * If get_ram_image_compression() is anything else, then the system-RAM image
         * is compressed.  In this case, the image will be reloaded from the
         * *original* file (not from the cache), in the hopes that an uncompressed
         * image will be found there.
         *
         * If an uncompressed image cannot be found, returns NULL.
         */
        """
        pass

    def get_usage_hint(self, Texture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_usage_hint(Texture self)
        
        /**
         * Returns the usage hint specified for buffer textures, or UH_unspecified for
         * all other texture types.
         */
        """
        pass

    def get_wrap_u(self, Texture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_wrap_u(Texture self)
        
        /**
         * Returns the wrap mode of the texture in the U direction.
         *
         * This returns the default sampler state for this texture; it may still be
         * overridden by a sampler state specified at a higher level.
         */
        """
        pass

    def get_wrap_v(self, Texture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_wrap_v(Texture self)
        
        /**
         * Returns the wrap mode of the texture in the V direction.
         *
         * This returns the default sampler state for this texture; it may still be
         * overridden by a sampler state specified at a higher level.
         */
        """
        pass

    def get_wrap_w(self, Texture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_wrap_w(Texture self)
        
        /**
         * Returns the wrap mode of the texture in the W direction.  This is the depth
         * direction of 3-d textures.
         *
         * This returns the default sampler state for this texture; it may still be
         * overridden by a sampler state specified at a higher level.
         */
        """
        pass

    def get_x_size(self, Texture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_x_size(Texture self)
        
        /**
         * Returns the width of the texture image in texels.
         */
        """
        pass

    def get_y_size(self, Texture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_y_size(Texture self)
        
        /**
         * Returns the height of the texture image in texels.  For a 1-d texture, this
         * will be 1.
         */
        """
        pass

    def get_z_size(self, Texture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_z_size(Texture self)
        
        /**
         * Returns the depth of the texture image in texels.  For a 1-d texture or 2-d
         * texture, this will be 1. For a cube map texture, this will be 6.
         */
        """
        pass

    def hasAllRamMipmapImages(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_all_ram_mipmap_images(Texture self)
        
        /**
         * Returns true if all expected mipmap levels have been defined and exist in
         * the system RAM, or false if even one mipmap level is missing.
         */
        """
        pass

    def hasAlphaFilename(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_alpha_filename(Texture self)
        
        /**
         * Returns true if the alpha_filename has been set and is available.  See
         * set_alpha_filename().
         */
        """
        pass

    def hasAlphaFullpath(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_alpha_fullpath(Texture self)
        
        /**
         * Returns true if the alpha_fullpath has been set and is available.  See
         * set_alpha_fullpath().
         */
        """
        pass

    def hasAutoTextureScale(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_auto_texture_scale(Texture self)
        
        /**
         * Returns true if set_auto_texture_scale() has been set to something other
         * than ATS_unspecified for this particular texture.
         */
        """
        pass

    def hasClearColor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_clear_color(Texture self)
        
        /**
         * Returns true if a color was previously set using set_clear_color.
         */
        """
        pass

    def hasCompression(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_compression(Texture self)
        
        /**
         * Returns true if the texture indicates it wants to be compressed, either
         * with CM_on or higher, or CM_default and compressed-textures is true.
         *
         * If true returned, this is not a guarantee that the texture is actually
         * successfully compressed on the GSG.  It may be that the GSG does not
         * support the requested compression mode, in which case the texture may
         * actually be stored uncompressed in texture memory.
         */
        """
        pass

    def hasFilename(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_filename(Texture self)
        
        /**
         * Returns true if the filename has been set and is available.  See
         * set_filename().
         */
        """
        pass

    def hasFullpath(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_fullpath(Texture self)
        
        /**
         * Returns true if the fullpath has been set and is available.  See
         * set_fullpath().
         */
        """
        pass

    def hasRamImage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_ram_image(Texture self)
        
        /**
         * Returns true if the Texture has its image contents available in main RAM,
         * false if it exists only in texture memory or in the prepared GSG context.
         *
         * Note that this has nothing to do with whether get_ram_image() will fail or
         * not.  Even if has_ram_image() returns false, get_ram_image() may still
         * return a valid RAM image, because get_ram_image() will automatically load
         * the texture from disk if necessary.  The only thing has_ram_image() tells
         * you is whether the texture is available right now without hitting the disk
         * first.
         *
         * Note also that if an application uses only one GSG, it may appear that
         * has_ram_image() returns true if the texture has not yet been loaded by the
         * GSG, but this correlation is not true in general and should not be depended
         * on.  Specifically, if an application ever uses multiple GSG's in its
         * lifetime (for instance, by opening more than one window, or by closing its
         * window and opening another one later), then has_ram_image() may well return
         * false on textures that have never been loaded on the current GSG.
         */
        """
        pass

    def hasRamMipmapImage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_ram_mipmap_image(Texture self, int n)
        
        /**
         * Returns true if the Texture has the nth mipmap level available in system
         * memory, false otherwise.  If the texture's minfilter mode requires
         * mipmapping (see uses_mipmaps()), and all the texture's mipmap levels are
         * not available when the texture is rendered, they will be generated
         * automatically.
         */
        """
        pass

    def hasSimpleRamImage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_simple_ram_image(Texture self)
        
        /**
         * Returns true if the Texture has a "simple" image available in main RAM.
         */
        """
        pass

    def hasTexturesPower2(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_textures_power_2()
        
        /**
         * If true, then get_textures_power_2 has been set using set_textures_power_2.
         * If false, then get_textures_power_2 simply returns the config variable of
         * the same name.
         */
        """
        pass

    def hasUncompressedRamImage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_uncompressed_ram_image(Texture self)
        
        /**
         * Returns true if the Texture has its image contents available in main RAM
         * and is uncompressed, false otherwise.  See has_ram_image().
         */
        """
        pass

    def has_all_ram_mipmap_images(self, Texture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_all_ram_mipmap_images(Texture self)
        
        /**
         * Returns true if all expected mipmap levels have been defined and exist in
         * the system RAM, or false if even one mipmap level is missing.
         */
        """
        pass

    def has_alpha_filename(self, Texture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_alpha_filename(Texture self)
        
        /**
         * Returns true if the alpha_filename has been set and is available.  See
         * set_alpha_filename().
         */
        """
        pass

    def has_alpha_fullpath(self, Texture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_alpha_fullpath(Texture self)
        
        /**
         * Returns true if the alpha_fullpath has been set and is available.  See
         * set_alpha_fullpath().
         */
        """
        pass

    def has_auto_texture_scale(self, Texture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_auto_texture_scale(Texture self)
        
        /**
         * Returns true if set_auto_texture_scale() has been set to something other
         * than ATS_unspecified for this particular texture.
         */
        """
        pass

    def has_clear_color(self, Texture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_clear_color(Texture self)
        
        /**
         * Returns true if a color was previously set using set_clear_color.
         */
        """
        pass

    def has_compression(self, Texture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_compression(Texture self)
        
        /**
         * Returns true if the texture indicates it wants to be compressed, either
         * with CM_on or higher, or CM_default and compressed-textures is true.
         *
         * If true returned, this is not a guarantee that the texture is actually
         * successfully compressed on the GSG.  It may be that the GSG does not
         * support the requested compression mode, in which case the texture may
         * actually be stored uncompressed in texture memory.
         */
        """
        pass

    def has_filename(self, Texture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_filename(Texture self)
        
        /**
         * Returns true if the filename has been set and is available.  See
         * set_filename().
         */
        """
        pass

    def has_fullpath(self, Texture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_fullpath(Texture self)
        
        /**
         * Returns true if the fullpath has been set and is available.  See
         * set_fullpath().
         */
        """
        pass

    def has_ram_image(self, Texture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_ram_image(Texture self)
        
        /**
         * Returns true if the Texture has its image contents available in main RAM,
         * false if it exists only in texture memory or in the prepared GSG context.
         *
         * Note that this has nothing to do with whether get_ram_image() will fail or
         * not.  Even if has_ram_image() returns false, get_ram_image() may still
         * return a valid RAM image, because get_ram_image() will automatically load
         * the texture from disk if necessary.  The only thing has_ram_image() tells
         * you is whether the texture is available right now without hitting the disk
         * first.
         *
         * Note also that if an application uses only one GSG, it may appear that
         * has_ram_image() returns true if the texture has not yet been loaded by the
         * GSG, but this correlation is not true in general and should not be depended
         * on.  Specifically, if an application ever uses multiple GSG's in its
         * lifetime (for instance, by opening more than one window, or by closing its
         * window and opening another one later), then has_ram_image() may well return
         * false on textures that have never been loaded on the current GSG.
         */
        """
        pass

    def has_ram_mipmap_image(self, Texture_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_ram_mipmap_image(Texture self, int n)
        
        /**
         * Returns true if the Texture has the nth mipmap level available in system
         * memory, false otherwise.  If the texture's minfilter mode requires
         * mipmapping (see uses_mipmaps()), and all the texture's mipmap levels are
         * not available when the texture is rendered, they will be generated
         * automatically.
         */
        """
        pass

    def has_simple_ram_image(self, Texture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_simple_ram_image(Texture self)
        
        /**
         * Returns true if the Texture has a "simple" image available in main RAM.
         */
        """
        pass

    def has_textures_power_2(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_textures_power_2()
        
        /**
         * If true, then get_textures_power_2 has been set using set_textures_power_2.
         * If false, then get_textures_power_2 simply returns the config variable of
         * the same name.
         */
        """
        pass

    def has_uncompressed_ram_image(self, Texture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_uncompressed_ram_image(Texture self)
        
        /**
         * Returns true if the Texture has its image contents available in main RAM
         * and is uncompressed, false otherwise.  See has_ram_image().
         */
        """
        pass

    def isCacheable(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_cacheable(Texture self)
        
        /**
         * Returns true if there is enough information in this Texture object to write
         * it to the bam cache successfully, false otherwise.  For most textures, this
         * is the same as has_ram_image().
         */
        """
        pass

    def isPrepared(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_prepared(Texture self, PreparedGraphicsObjects prepared_objects)
        
        /**
         * Returns true if the texture has already been prepared or enqueued for
         * preparation on the indicated GSG, false otherwise.
         */
        """
        pass

    def is_cacheable(self, Texture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_cacheable(Texture self)
        
        /**
         * Returns true if there is enough information in this Texture object to write
         * it to the bam cache successfully, false otherwise.  For most textures, this
         * is the same as has_ram_image().
         */
        """
        pass

    def is_prepared(self, Texture_self, PreparedGraphicsObjects_prepared_objects): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_prepared(Texture self, PreparedGraphicsObjects prepared_objects)
        
        /**
         * Returns true if the texture has already been prepared or enqueued for
         * preparation on the indicated GSG, false otherwise.
         */
        """
        pass

    def load(self, const_Texture_self, const_PNMImage_pnmimage): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        load(const Texture self, const PNMImage pnmimage)
        load(const Texture self, const PfmFile pfm)
        load(const Texture self, const PNMImage pnmimage, const LoaderOptions options)
        load(const Texture self, const PfmFile pfm, const LoaderOptions options)
        load(const Texture self, const PNMImage pnmimage, int z, int n, const LoaderOptions options)
        load(const Texture self, const PfmFile pfm, int z, int n, const LoaderOptions options)
        
        /**
         * Replaces the texture with the indicated image.
         */
        
        /**
         * Stores the indicated image in the given page and mipmap level.  See read().
         */
        
        /**
         * Replaces the texture with the indicated image.
         */
        
        /**
         * Stores the indicated image in the given page and mipmap level.  See read().
         */
        """
        pass

    def loadRelated(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        load_related(Texture self, const InternalName suffix)
        
        /**
         * Loads a texture whose filename is derived by concatenating a suffix to the
         * filename of this texture.  May return NULL, for example, if this texture
         * doesn't have a filename.
         */
        """
        pass

    def loadSubImage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        load_sub_image(const Texture self, const PNMImage pnmimage, int x, int y, int z, int n)
        
        /**
         * Stores the indicated image in a region of the texture.  The texture
         * properties remain unchanged.  This can be more efficient than updating an
         * entire texture, but has a few restrictions: for one, you must ensure that
         * the texture is still in RAM (eg.  using set_keep_ram_image) and it may not
         * be compressed.
         */
        """
        pass

    def load_related(self, Texture_self, const_InternalName_suffix): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        load_related(Texture self, const InternalName suffix)
        
        /**
         * Loads a texture whose filename is derived by concatenating a suffix to the
         * filename of this texture.  May return NULL, for example, if this texture
         * doesn't have a filename.
         */
        """
        pass

    def load_sub_image(self, const_Texture_self, const_PNMImage_pnmimage, int_x, int_y, int_z, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        load_sub_image(const Texture self, const PNMImage pnmimage, int x, int y, int z, int n)
        
        /**
         * Stores the indicated image in a region of the texture.  The texture
         * properties remain unchanged.  This can be more efficient than updating an
         * entire texture, but has a few restrictions: for one, you must ensure that
         * the texture is still in RAM (eg.  using set_keep_ram_image) and it may not
         * be compressed.
         */
        """
        pass

    def makeCopy(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_copy(Texture self)
        
        /**
         * Returns a new copy of the same Texture.  This copy, if applied to geometry,
         * will be copied into texture as a separate texture from the original, so it
         * will be duplicated in texture memory (and may be independently modified if
         * desired).
         *
         * If the Texture is a VideoTexture, the resulting duplicate may be animated
         * independently of the original.
         */
        """
        pass

    def makeFromTxo(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_from_txo(istream in, str filename)
        
        /**
         * Constructs a new Texture object from the txo file.  This is similar to
         * Texture::read_txo(), but it constructs and returns a new object, which
         * allows it to return a subclass of Texture (for instance, a movie texture).
         *
         * Pass a real filename if it is available, or empty string if it is not.
         */
        """
        pass

    def makeRamImage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_ram_image(const Texture self)
        
        /**
         * Discards the current system-RAM image for the texture, if any, and
         * allocates a new buffer of the appropriate size.  Returns the new buffer.
         *
         * This does *not* affect keep_ram_image.
         */
        """
        pass

    def makeRamMipmapImage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_ram_mipmap_image(const Texture self, int n)
        
        /**
         * Discards the current system-RAM image for the nth mipmap level, if any, and
         * allocates a new buffer of the appropriate size.  Returns the new buffer.
         *
         * This does *not* affect keep_ram_image.
         */
        """
        pass

    def make_copy(self, Texture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_copy(Texture self)
        
        /**
         * Returns a new copy of the same Texture.  This copy, if applied to geometry,
         * will be copied into texture as a separate texture from the original, so it
         * will be duplicated in texture memory (and may be independently modified if
         * desired).
         *
         * If the Texture is a VideoTexture, the resulting duplicate may be animated
         * independently of the original.
         */
        """
        pass

    def make_from_txo(self, istream_in, str_filename): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_from_txo(istream in, str filename)
        
        /**
         * Constructs a new Texture object from the txo file.  This is similar to
         * Texture::read_txo(), but it constructs and returns a new object, which
         * allows it to return a subclass of Texture (for instance, a movie texture).
         *
         * Pass a real filename if it is available, or empty string if it is not.
         */
        """
        pass

    def make_ram_image(self, const_Texture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_ram_image(const Texture self)
        
        /**
         * Discards the current system-RAM image for the texture, if any, and
         * allocates a new buffer of the appropriate size.  Returns the new buffer.
         *
         * This does *not* affect keep_ram_image.
         */
        """
        pass

    def make_ram_mipmap_image(self, const_Texture_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_ram_mipmap_image(const Texture self, int n)
        
        /**
         * Discards the current system-RAM image for the nth mipmap level, if any, and
         * allocates a new buffer of the appropriate size.  Returns the new buffer.
         *
         * This does *not* affect keep_ram_image.
         */
        """
        pass

    def mightHaveRamImage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        might_have_ram_image(Texture self)
        
        /**
         * Returns true if the texture's image contents are currently available in
         * main RAM, or there is reason to believe it can be loaded on demand.  That
         * is, this function returns a "best guess" as to whether get_ram_image() will
         * succeed without actually calling it first.
         */
        """
        pass

    def might_have_ram_image(self, Texture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        might_have_ram_image(Texture self)
        
        /**
         * Returns true if the texture's image contents are currently available in
         * main RAM, or there is reason to believe it can be loaded on demand.  That
         * is, this function returns a "best guess" as to whether get_ram_image() will
         * succeed without actually calling it first.
         */
        """
        pass

    def modifyRamImage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        modify_ram_image(const Texture self)
        
        /**
         * Returns a modifiable pointer to the system-RAM image.  This assumes the RAM
         * image should be uncompressed.  If the RAM image has been dumped, or is
         * stored compressed, creates a new one.
         *
         * This does *not* affect keep_ram_image.
         */
        """
        pass

    def modifyRamMipmapImage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        modify_ram_mipmap_image(const Texture self, int n)
        
        /**
         * Returns a modifiable pointer to the system-RAM image for the nth mipmap
         * level.  This assumes the RAM image is uncompressed; if this is not the
         * case, raises an assertion.
         *
         * This does *not* affect keep_ram_image.
         */
        """
        pass

    def modifySimpleRamImage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        modify_simple_ram_image(const Texture self)
        
        /**
         * Returns a modifiable pointer to the internal "simple" texture image.  See
         * set_simple_ram_image().
         */
        """
        pass

    def modify_ram_image(self, const_Texture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        modify_ram_image(const Texture self)
        
        /**
         * Returns a modifiable pointer to the system-RAM image.  This assumes the RAM
         * image should be uncompressed.  If the RAM image has been dumped, or is
         * stored compressed, creates a new one.
         *
         * This does *not* affect keep_ram_image.
         */
        """
        pass

    def modify_ram_mipmap_image(self, const_Texture_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        modify_ram_mipmap_image(const Texture self, int n)
        
        /**
         * Returns a modifiable pointer to the system-RAM image for the nth mipmap
         * level.  This assumes the RAM image is uncompressed; if this is not the
         * case, raises an assertion.
         *
         * This does *not* affect keep_ram_image.
         */
        """
        pass

    def modify_simple_ram_image(self, const_Texture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        modify_simple_ram_image(const Texture self)
        
        /**
         * Returns a modifiable pointer to the internal "simple" texture image.  See
         * set_simple_ram_image().
         */
        """
        pass

    def newSimpleRamImage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        new_simple_ram_image(const Texture self, int x_size, int y_size)
        
        /**
         * Creates an empty array for the simple ram image of the indicated size, and
         * returns a modifiable pointer to the new array.  See set_simple_ram_image().
         */
        """
        pass

    def new_simple_ram_image(self, const_Texture_self, int_x_size, int_y_size): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        new_simple_ram_image(const Texture self, int x_size, int y_size)
        
        /**
         * Creates an empty array for the simple ram image of the indicated size, and
         * returns a modifiable pointer to the new array.  See set_simple_ram_image().
         */
        """
        pass

    def peek(self, const_Texture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        peek(const Texture self)
        
        /**
         * Returns a TexturePeeker object that can be used to examine the individual
         * texels stored within this Texture by (u, v) coordinate.
         *
         * If the texture has a ram image resident, that image is used.  If it does
         * not have a full ram image but does have a simple_ram_image resident, that
         * image is used instead.  If neither image is resident the full image is
         * reloaded.
         *
         * Returns NULL if the texture cannot find an image to load, or the texture
         * format is incompatible.
         */
        """
        pass

    def prepare(self, const_Texture_self, PreparedGraphicsObjects_prepared_objects): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        prepare(const Texture self, PreparedGraphicsObjects prepared_objects)
        
        /**
         * Indicates that the texture should be enqueued to be prepared in the
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
        prepare_now(const Texture self, int view, PreparedGraphicsObjects prepared_objects, GraphicsStateGuardianBase gsg)
        
        /**
         * Creates a context for the texture on the particular GSG, if it does not
         * already exist.  Returns the new (or old) TextureContext.  This assumes that
         * the GraphicsStateGuardian is the currently active rendering context and
         * that it is ready to accept new textures.  If this is not necessarily the
         * case, you should use prepare() instead.
         *
         * Normally, this is not called directly except by the GraphicsStateGuardian;
         * a texture does not need to be explicitly prepared by the user before it may
         * be rendered.
         */
        """
        pass

    def prepare_now(self, const_Texture_self, int_view, PreparedGraphicsObjects_prepared_objects, GraphicsStateGuardianBase_gsg): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        prepare_now(const Texture self, int view, PreparedGraphicsObjects prepared_objects, GraphicsStateGuardianBase gsg)
        
        /**
         * Creates a context for the texture on the particular GSG, if it does not
         * already exist.  Returns the new (or old) TextureContext.  This assumes that
         * the GraphicsStateGuardian is the currently active rendering context and
         * that it is ready to accept new textures.  If this is not necessarily the
         * case, you should use prepare() instead.
         *
         * Normally, this is not called directly except by the GraphicsStateGuardian;
         * a texture does not need to be explicitly prepared by the user before it may
         * be rendered.
         */
        """
        pass

    def read(self, const_Texture_self, const_Filename_fullpath): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        read(const Texture self, const Filename fullpath)
        read(const Texture self, const Filename fullpath, const LoaderOptions options)
        read(const Texture self, const Filename fullpath, const Filename alpha_fullpath, int primary_file_num_channels, int alpha_file_channel)
        read(const Texture self, const Filename fullpath, int z, int n, bool read_pages, bool read_mipmaps)
        read(const Texture self, const Filename fullpath, const Filename alpha_fullpath, int primary_file_num_channels, int alpha_file_channel, const LoaderOptions options)
        read(const Texture self, const Filename fullpath, int z, int n, bool read_pages, bool read_mipmaps, const LoaderOptions options)
        read(const Texture self, const Filename fullpath, const Filename alpha_fullpath, int primary_file_num_channels, int alpha_file_channel, int z, int n, bool read_pages, bool read_mipmaps, BamCacheRecord record, const LoaderOptions options)
        
        /**
         * Reads the named filename into the texture.
         */
        
        /**
         * Combine a 3-component image with a grayscale image to get a 4-component
         * image.
         *
         * See the description of the full-parameter read() method for the meaning of
         * the primary_file_num_channels and alpha_file_channel parameters.
         */
        
        /**
         * Reads a single file into a single page or mipmap level, or automatically
         * reads a series of files into a series of pages and/or mipmap levels.
         *
         * See the description of the full-parameter read() method for the meaning of
         * the various parameters.
         */
        
        /**
         * Reads the texture from the indicated filename.  If
         * primary_file_num_channels is not 0, it specifies the number of components
         * to downgrade the image to if it is greater than this number.
         *
         * If the filename has the extension .txo, this implicitly reads a texture
         * object instead of a filename (which replaces all of the texture
         * properties).  In this case, all the rest of the parameters are ignored, and
         * the filename should not contain any hash marks; just the one named file
         * will be read, since a single .txo file can contain all pages and mipmaps
         * necessary to define a texture.
         *
         * If alpha_fullpath is not empty, it specifies the name of a file from which
         * to retrieve the alpha.  In this case, alpha_file_channel represents the
         * numeric channel of this image file to use as the resulting texture's alpha
         * channel; usually, this is 0 to indicate the grayscale combination of r, g,
         * b; or it may be a one-based channel number, e.g.  1 for the red channel, 2
         * for the green channel, and so on.
         *
         * If read pages is false, then z indicates the page number into which this
         * image will be assigned.  Normally this is 0 for the first (or only) page of
         * the texture.  3-D textures have one page for each level of depth, and cube
         * map textures always have six pages.
         *
         * If read_pages is true, multiple images will be read at once, one for each
         * page of a cube map or a 3-D texture.  In this case, the filename should
         * contain a sequence of one or more hash marks ("#") which will be filled in
         * with the z value of each page, zero-based.  In this case, the z parameter
         * indicates the maximum z value that will be loaded, or 0 to load all
         * filenames that exist.
         *
         * If read_mipmaps is false, then n indicates the mipmap level to which this
         * image will be assigned.  Normally this is 0 for the base texture image, but
         * it is possible to load custom mipmap levels into the later images.  After
         * the base texture image is loaded (thus defining the size of the texture),
         * you can call get_expected_num_mipmap_levels() to determine the maximum
         * sensible value for n.
         *
         * If read_mipmaps is true, multiple images will be read as above, but this
         * time the images represent the different mipmap levels of the texture image.
         * In this case, the n parameter indicates the maximum n value that will be
         * loaded, or 0 to load all filenames that exist (up to the expected number of
         * mipmap levels).
         *
         * If both read_pages and read_mipmaps is true, then both sequences will be
         * read; the filename should contain two sequences of hash marks, separated by
         * some character such as a hyphen, underscore, or dot.  The first hash mark
         * sequence will be filled in with the mipmap level, while the second hash
         * mark sequence will be the page index.
         *
         * This method implicitly sets keep_ram_image to false.
         */
        """
        pass

    def readDds(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        read_dds(const Texture self, istream in, str filename, bool header_only)
        
        /**
         * Reads the texture from a DDS file object.  This is a Microsoft-defined file
         * format; it is similar in principle to a txo object, in that it is designed
         * to contain the texture image in a form as similar as possible to its
         * runtime image, and it can contain mipmaps, pre-compressed textures, and so
         * on.
         *
         * As with read_txo, the filename is just for reference.
         */
        """
        pass

    def readKtx(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        read_ktx(const Texture self, istream in, str filename, bool header_only)
        
        /**
         * Reads the texture from a KTX file object.  This is a Khronos-defined file
         * format; it is similar in principle to a dds object, in that it is designed
         * to contain the texture image in a form as similar as possible to its
         * runtime image, and it can contain mipmaps, pre-compressed textures, and so
         * on.
         *
         * As with read_dds, the filename is just for reference.
         */
        """
        pass

    def readTxo(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        read_txo(const Texture self, istream in, str filename)
        
        /**
         * Reads the texture from a Panda texture object.  This defines the complete
         * Texture specification, including the image data as well as all texture
         * properties.  This only works if the txo file contains a static Texture
         * image, as opposed to a subclass of Texture such as a movie texture.
         *
         * Pass a real filename if it is available, or empty string if it is not.
         */
        """
        pass

    def read_dds(self, const_Texture_self, istream_in, str_filename, bool_header_only): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        read_dds(const Texture self, istream in, str filename, bool header_only)
        
        /**
         * Reads the texture from a DDS file object.  This is a Microsoft-defined file
         * format; it is similar in principle to a txo object, in that it is designed
         * to contain the texture image in a form as similar as possible to its
         * runtime image, and it can contain mipmaps, pre-compressed textures, and so
         * on.
         *
         * As with read_txo, the filename is just for reference.
         */
        """
        pass

    def read_ktx(self, const_Texture_self, istream_in, str_filename, bool_header_only): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        read_ktx(const Texture self, istream in, str filename, bool header_only)
        
        /**
         * Reads the texture from a KTX file object.  This is a Khronos-defined file
         * format; it is similar in principle to a dds object, in that it is designed
         * to contain the texture image in a form as similar as possible to its
         * runtime image, and it can contain mipmaps, pre-compressed textures, and so
         * on.
         *
         * As with read_dds, the filename is just for reference.
         */
        """
        pass

    def read_txo(self, const_Texture_self, istream_in, str_filename): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        read_txo(const Texture self, istream in, str filename)
        
        /**
         * Reads the texture from a Panda texture object.  This defines the complete
         * Texture specification, including the image data as well as all texture
         * properties.  This only works if the txo file contains a static Texture
         * image, as opposed to a subclass of Texture such as a movie texture.
         *
         * Pass a real filename if it is available, or empty string if it is not.
         */
        """
        pass

    def release(self, const_Texture_self, PreparedGraphicsObjects_prepared_objects): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        release(const Texture self, PreparedGraphicsObjects prepared_objects)
        
        /**
         * Frees the texture context only on the indicated object, if it exists there.
         * Returns true if it was released, false if it had not been prepared.
         */
        """
        pass

    def releaseAll(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        release_all(const Texture self)
        
        /**
         * Frees the context allocated on all objects for which the texture has been
         * declared.  Returns the number of contexts which have been freed.
         */
        """
        pass

    def release_all(self, const_Texture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        release_all(const Texture self)
        
        /**
         * Frees the context allocated on all objects for which the texture has been
         * declared.  Returns the number of contexts which have been freed.
         */
        """
        pass

    def reload(self, const_Texture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        reload(const Texture self)
        
        /**
         * Re-reads the Texture from its disk file.  Useful when you know the image on
         * disk has recently changed, and you want to update the Texture image.
         *
         * Returns true on success, false on failure (in which case, the Texture may
         * or may not still be valid).
         */
        """
        pass

    def rescaleTexture(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        rescale_texture(const Texture self)
        
        /**
         * This method is similar to consider_rescale(), but instead of scaling a
         * separate PNMImage, it will ask the Texture to rescale its own internal
         * image to a power of 2, according to the config file requirements.  This may
         * be useful after loading a Texture image by hand, instead of reading it from
         * a disk file.  Returns true if the texture is changed, false if it was not.
         */
        """
        pass

    def rescale_texture(self, const_Texture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        rescale_texture(const Texture self)
        
        /**
         * This method is similar to consider_rescale(), but instead of scaling a
         * separate PNMImage, it will ask the Texture to rescale its own internal
         * image to a power of 2, according to the config file requirements.  This may
         * be useful after loading a Texture image by hand, instead of reading it from
         * a disk file.  Returns true if the texture is changed, false if it was not.
         */
        """
        pass

    def setAlphaFilename(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_alpha_filename(const Texture self, const Filename alpha_filename)
        
        /**
         * Sets the name of the file that contains the image's alpha channel contents.
         * Normally, this is set automatically when the image is loaded, for instance
         * via Texture::read().
         *
         * The Texture's get_filename() function returns the name of the image file
         * that was loaded into the buffer.  In the case where a texture specified two
         * separate files to load, a 1- or 3-channel color image and a 1-channel alpha
         * image, this Filename is update to contain the name of the image file that
         * was loaded into the buffer's alpha channel.
         */
        """
        pass

    def setAlphaFullpath(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_alpha_fullpath(const Texture self, const Filename alpha_fullpath)
        
        /**
         * Sets the full pathname to the file that contains the image's alpha channel
         * contents, as found along the search path.  Normally, this is set
         * automatically when the image is loaded, for instance via Texture::read().
         */
        """
        pass

    def setAnisotropicDegree(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_anisotropic_degree(const Texture self, int anisotropic_degree)
        
        /**
         * Specifies the level of anisotropic filtering to apply to the texture.  Set
         * this 0 to indicate the default value, which is specified in the texture-
         * anisotropic-degree config variable.
         *
         * To explicitly disable anisotropic filtering, set this value to 1.  To
         * explicitly enable anisotropic filtering, set it to a value higher than 1;
         * larger numbers indicate greater degrees of filtering.
         *
         * This sets the default sampler state for this texture; it may still be
         * overridden by a sampler state specified at a higher level.
         */
        """
        pass

    def setAutoTextureScale(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_auto_texture_scale(const Texture self, int scale)
        
        /**
         * Specifies the power-of-2 texture-scaling mode that will be applied to this
         * particular texture when it is next loaded from disk.  See
         * set_textures_power_2().
         */
        """
        pass

    def setAuxData(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_aux_data(const Texture self, str key, TypedReferenceCount aux_data)
        
        /**
         * Records an arbitrary object in the Texture, associated with a specified
         * key.  The object may later be retrieved by calling get_aux_data() with the
         * same key.
         *
         * These data objects are not recorded to a bam or txo file.
         */
        """
        pass

    def setBorderColor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_border_color(const Texture self, const LVecBase4f color)
        
        /**
         * Specifies the solid color of the texture's border.  Some OpenGL
         * implementations use a border for tiling textures; in Panda, it is only used
         * for specifying the clamp color.
         *
         * This sets the default sampler state for this texture; it may still be
         * overridden by a sampler state specified at a higher level.
         */
        """
        pass

    def setClearColor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_clear_color(const Texture self, const LVecBase4f color)
        
        /**
         * Sets the color that will be used to fill the texture image in absence of
         * any image data.  It is used when any of the setup_texture functions or
         * clear_image is called and image data is not provided using read() or
         * modify_ram_image().
         *
         * This does not affect a texture that has already been cleared; call
         * clear_image to clear it again.
         */
        """
        pass

    def setComponentType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_component_type(const Texture self, int component_type)
        
        /**
         * Changes the data value for the texture components.  This implicitly sets
         * component_width as well.
         */
        """
        pass

    def setCompression(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_compression(const Texture self, int compression)
        
        /**
         * Requests that this particular Texture be compressed when it is loaded into
         * texture memory.
         *
         * This refers to the internal compression of the texture image within texture
         * memory; it is not related to jpeg or png compression, which are disk file
         * compression formats.  The actual disk file that generated this texture may
         * be stored in a compressed or uncompressed format supported by Panda; it
         * will be decompressed on load, and then recompressed by the graphics API if
         * this parameter is not CM_off.
         *
         * If the GSG does not support this texture compression mode, the texture will
         * silently be loaded uncompressed.
         */
        """
        pass

    def setDefaultSampler(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_default_sampler(const Texture self, const SamplerState sampler)
        
        /**
         * This sets the default sampler state for this texture, containing the wrap
         * and filter properties specified on the texture level; it may still be
         * overridden by a sampler state specified at a higher level.  This
         * encompasses the settings for get_wrap_u, get_minfilter,
         * get_anisotropic_degree, etc.
         *
         * This makes a copy of the SamplerState object, so future modifications of
         * the same SamplerState will have no effect on this texture unless you call
         * set_default_sampler again.
         */
        """
        pass

    def setFilename(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_filename(const Texture self, const Filename filename)
        
        /**
         * Sets the name of the file that contains the image's contents.  Normally,
         * this is set automatically when the image is loaded, for instance via
         * Texture::read().
         *
         * The Texture's get_name() function used to return the filename, but now
         * returns just the basename (without the extension), which is a more useful
         * name for identifying an image in show code.
         */
        """
        pass

    def setFormat(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_format(const Texture self, int format)
        
        /**
         * Changes the format value for the texture components.  This implicitly sets
         * num_components as well.
         */
        """
        pass

    def setFullpath(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_fullpath(const Texture self, const Filename fullpath)
        
        /**
         * Sets the full pathname to the file that contains the image's contents, as
         * found along the search path.  Normally, this is set automatically when the
         * image is loaded, for instance via Texture::read().
         */
        """
        pass

    def setKeepRamImage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_keep_ram_image(const Texture self, bool keep_ram_image)
        
        /**
         * Sets the flag that indicates whether this Texture is eligible to have its
         * main RAM copy of the texture memory dumped when the texture is prepared for
         * rendering.
         *
         * This will be false for most textures, which can reload their images if
         * needed by rereading the input file.  However, textures that were generated
         * dynamically and cannot be easily reloaded will want to set this flag to
         * true, so that the texture will always keep its image copy around.
         */
        """
        pass

    def setLoadedFromImage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_loaded_from_image(const Texture self, bool flag)
        
        /**
         * Sets the flag that indicates the texture has been loaded from a disk file
         * or PNMImage.  You should also ensure the filename has been set correctly.
         * When this flag is true, the texture may be automatically reloaded when its
         * ram image needs to be replaced.
         */
        """
        pass

    def setLoadedFromTxo(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_loaded_from_txo(const Texture self, bool flag)
        
        /**
         * Sets the flag that indicates the texture has been loaded from a txo file.
         * You probably shouldn't be setting this directly; it is set automatically
         * when a Texture is loaded.
         */
        """
        pass

    def setMagfilter(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_magfilter(const Texture self, int filter)
        
        /**
         * Sets the filtering method that should be used when viewing the texture up
         * close.
         *
         * This sets the default sampler state for this texture; it may still be
         * overridden by a sampler state specified at a higher level.
         */
        """
        pass

    def setMatchFramebufferFormat(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_match_framebuffer_format(const Texture self, bool flag)
        
        /**
         * Sets the special flag that, if true, indicates to the GSG that the
         * Texture's format should be chosen to exactly match the framebuffer's
         * format, presumably because the application intends to copy image data from
         * the framebuffer into the Texture (or vice-versa).
         *
         * This sets only the graphics card's idea of the texture format; it is not
         * related to the system-memory format.
         */
        """
        pass

    def setMinfilter(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_minfilter(const Texture self, int filter)
        
        /**
         * Sets the filtering method that should be used when viewing the texture from
         * a distance.
         *
         * This sets the default sampler state for this texture; it may still be
         * overridden by a sampler state specified at a higher level.
         */
        """
        pass

    def setNumViews(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_num_views(const Texture self, int num_views)
        
        /**
         * Sets the number of "views" within a texture.  A view is a completely
         * separate image stored within the Texture object.  Most textures have only
         * one view, but a stereo texture, for instance, may have two views, a left
         * and a right image.  Other uses for multiple views are not yet defined.
         *
         * If this value is greater than one, the additional views are accessed as
         * additional pages beyond get_z_size().
         *
         * This also implicitly unloads the texture if it has already been loaded.
         */
        """
        pass

    def setOrigFileSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_orig_file_size(const Texture self, int x, int y, int z)
        
        /**
         * Specifies the size of the texture as it exists in its original disk file,
         * before any Panda scaling.
         */
        """
        pass

    def setPadSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_pad_size(const Texture self, int x, int y, int z)
        
        /**
         * Sets the size of the pad region.
         *
         * Sometimes, when a video card demands power-of-two textures, it is necessary
         * to create a big texture and then only use a portion of it.  The pad region
         * indicates which portion of the texture is not really in use.  All
         * operations use the texture as a whole, including the pad region, unless
         * they explicitly state that they use only the non-pad region.
         *
         * Changing the texture's size clears the pad region.
         */
        """
        pass

    def setPostLoadStoreCache(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_post_load_store_cache(const Texture self, bool flag)
        
        /**
         * Sets the post_load_store_cache flag.  When this is set, the next time the
         * texture is loaded on a GSG, it will automatically extract its RAM image
         * from the GSG and save it to the global BamCache.
         *
         * This is used to store compressed RAM images in the BamCache.  This flag
         * should not be set explicitly; it is set automatically by the TexturePool
         * when model-cache-compressed-textures is set true.
         */
        """
        pass

    def setQualityLevel(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_quality_level(const Texture self, int quality_level)
        
        /**
         * Sets a hint to the renderer about the desired performance / quality
         * tradeoff for this particular texture.  This is most useful for the
         * tinydisplay software renderer; for normal, hardware-accelerated renderers,
         * this may have little or no effect.
         */
        """
        pass

    def setRamImage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_ram_image(const Texture self, object image, int compression, int page_size)
        
        /**
         * Replaces the current system-RAM image with the new data.  If compression is
         * not CM_off, it indicates that the new data is already pre-compressed in the
         * indicated format.
         *
         * This does *not* affect keep_ram_image.
         */
        """
        pass

    def setRamImageAs(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_ram_image_as(const Texture self, object image, str provided_format)
        
        /**
         * Replaces the current system-RAM image with the new data, converting it
         * first if necessary from the indicated component-order format.  See
         * get_ram_image_as() for specifications about the format.  This method cannot
         * support compressed image data or sub-pages; use set_ram_image() for that.
         */
        """
        pass

    def setRamMipmapImage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_ram_mipmap_image(const Texture self, int n, ConstPointerToArray image, int page_size)
        
        /**
         * Replaces the current system-RAM image for the indicated mipmap level with
         * the new data.  If compression is not CM_off, it indicates that the new data
         * is already pre-compressed in the indicated format.
         *
         * This does *not* affect keep_ram_image.
         */
        """
        pass

    def setRamMipmapPointerFromInt(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_ram_mipmap_pointer_from_int(const Texture self, long pointer, int n, int page_size)
        
        /**
         * Accepts a raw pointer cast as an int, which is then passed to
         * set_ram_mipmap_pointer(); see the documentation for that method.
         *
         * This variant is particularly useful to set an external pointer from a
         * language like Python, which doesn't support void pointers directly.
         */
        """
        pass

    def setRenderToTexture(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_render_to_texture(const Texture self, bool render_to_texture)
        
        /**
         * Sets a flag on the texture that indicates whether the texture is intended
         * to be used as a direct-render target, by binding a framebuffer to a texture
         * and rendering directly into the texture.
         *
         * This controls some low-level choices made about the texture object itself.
         * For instance, compressed textures are disallowed when this flag is set
         * true.
         *
         * Normally, a user should not need to set this flag directly; it is set
         * automatically by the low-level display code when a texture is bound to a
         * framebuffer.
         */
        """
        pass

    def setSimpleRamImage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_simple_ram_image(const Texture self, ConstPointerToArray image, int x_size, int y_size)
        
        /**
         * Replaces the internal "simple" texture image.  This can be used as an
         * option to display while the main texture image is being loaded from disk.
         * It is normally a very small image, 16x16 or smaller (and maybe even 1x1),
         * that is designed to give just enough sense of color to serve as a
         * placeholder until the full texture is available.
         *
         * The "simple" image is always 4 components, 1 byte each, regardless of the
         * parameters of the full texture.  The simple image is only supported for
         * ordinary 2-d textures.
         *
         * Also see generate_simple_ram_image(), modify_simple_ram_image(), and
         * new_simple_ram_image().
         */
        """
        pass

    def setSizePadded(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_size_padded(const Texture self, int x, int y, int z)
        
        /**
         * Changes the size of the texture, padding if necessary, and setting the pad
         * region as well.
         */
        """
        pass

    def setTexturesPower2(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_textures_power_2(int scale)
        
        /**
         * Set this flag to ATS_none, ATS_up, ATS_down, or ATS_pad to control the
         * scaling of textures in general, if a particular texture does not override
         * this.  See also set_auto_texture_scale() for the per-texture override.
         */
        """
        pass

    def setup1dTexture(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        setup_1d_texture(const Texture self)
        setup_1d_texture(const Texture self, int x_size, int component_type, int format)
        
        /**
         * Sets the texture as an empty 1-d texture with no dimensions.  Follow up
         * with read() or load() to fill the texture properties and image data, or use
         * set_clear_color to let the texture be cleared to a solid color.
         */
        
        /**
         * Sets the texture as an empty 1-d texture with the specified dimensions and
         * properties.  Follow up with set_ram_image() or modify_ram_image() to fill
         * the image data, or use set_clear_color to let the texture be cleared to a
         * solid color.
         */
        """
        pass

    def setup2dTexture(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        setup_2d_texture(const Texture self)
        setup_2d_texture(const Texture self, int x_size, int y_size, int component_type, int format)
        
        /**
         * Sets the texture as an empty 2-d texture with no dimensions.  Follow up
         * with read() or load() to fill the texture properties and image data, or use
         * set_clear_color to let the texture be cleared to a solid color.
         */
        
        /**
         * Sets the texture as an empty 2-d texture with the specified dimensions and
         * properties.  Follow up with set_ram_image() or modify_ram_image() to fill
         * the image data, or use set_clear_color to let the texture be cleared to a
         * solid color.
         */
        """
        pass

    def setup2dTextureArray(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        setup_2d_texture_array(const Texture self)
        setup_2d_texture_array(const Texture self, int z_size)
        setup_2d_texture_array(const Texture self, int x_size, int y_size, int z_size, int component_type, int format)
        
        /**
         * Sets the texture as an empty 2-d texture array with no dimensions (though
         * if you know the depth ahead of time, it saves a bit of reallocation later).
         * Follow up with read() or load() to fill the texture properties and image
         * data, or use set_clear_color to let the texture be cleared to a solid
         * color.
         */
        
        /**
         * Sets the texture as an empty 2-d texture array with the specified
         * dimensions and properties.  Follow up with set_ram_image() or
         * modify_ram_image() to fill the image data, or use set_clear_color to let
         * the texture be cleared to a solid color.
         */
        """
        pass

    def setup3dTexture(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        setup_3d_texture(const Texture self)
        setup_3d_texture(const Texture self, int z_size)
        setup_3d_texture(const Texture self, int x_size, int y_size, int z_size, int component_type, int format)
        
        /**
         * Sets the texture as an empty 3-d texture with no dimensions (though if you
         * know the depth ahead of time, it saves a bit of reallocation later). Follow
         * up with read() or load() to fill the texture properties and image data, or
         * use set_clear_color to let the texture be cleared to a solid color.
         */
        
        /**
         * Sets the texture as an empty 3-d texture with the specified dimensions and
         * properties.  Follow up with set_ram_image() or modify_ram_image() to fill
         * the image data.
         */
        """
        pass

    def setupBufferTexture(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        setup_buffer_texture(const Texture self, int size, int component_type, int format, int usage)
        
        /**
         * Sets the texture as an empty buffer texture with the specified size and
         * properties.  Follow up with set_ram_image() or modify_ram_image() to fill
         * the image data, or use set_clear_color to let the texture be cleared to a
         * solid color.
         *
         * Note that a buffer texture's format needs to match the component type.
         */
        """
        pass

    def setupCubeMap(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        setup_cube_map(const Texture self)
        setup_cube_map(const Texture self, int size, int component_type, int format)
        
        /**
         * Sets the texture as an empty cube map texture with no dimensions.  Follow
         * up with read() or load() to fill the texture properties and image data, or
         * use set_clear_color to let the texture be cleared to a solid color.
         */
        
        /**
         * Sets the texture as an empty cube map texture with the specified dimensions
         * and properties.  Follow up with set_ram_image() or modify_ram_image() to
         * fill the image data, or use set_clear_color to let the texture be cleared
         * to a solid color.
         *
         * Note that a cube map should always consist of six square images, so x_size
         * and y_size will be the same, and z_size is always 6.
         */
        """
        pass

    def setupCubeMapArray(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        setup_cube_map_array(const Texture self, int num_cube_maps)
        setup_cube_map_array(const Texture self, int size, int num_cube_maps, int component_type, int format)
        
        /**
         * Sets the texture as cube map array with N cube maps.  Note that this number
         * is not the same as the z_size.  Follow up with read() or load() to fill the
         * texture properties and image data, or use set_clear_color to let the
         * texture be cleared to a solid color.
         *
         * @since 1.10.0
         */
        
        /**
         * Sets the texture as cube map array with N cube maps with the specified
         * dimensions and format.  Follow up with set_ram_image() or
         * modify_ram_image() to fill the image data, or use set_clear_color to let
         * the texture be cleared to a solid color.
         *
         * The num_cube_maps given here is multiplied by six to become the z_size of
         * the image.
         *
         * @since 1.10.0
         */
        """
        pass

    def setupTexture(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        setup_texture(const Texture self, int texture_type, int x_size, int y_size, int z_size, int component_type, int format)
        
        /**
         * Sets the texture to the indicated type and dimensions, presumably in
         * preparation for calling read() or load(), or set_ram_image() or
         * modify_ram_image(), or use set_clear_color to let the texture be cleared to
         * a solid color.
         */
        """
        pass

    def setup_1d_texture(self, const_Texture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        setup_1d_texture(const Texture self)
        setup_1d_texture(const Texture self, int x_size, int component_type, int format)
        
        /**
         * Sets the texture as an empty 1-d texture with no dimensions.  Follow up
         * with read() or load() to fill the texture properties and image data, or use
         * set_clear_color to let the texture be cleared to a solid color.
         */
        
        /**
         * Sets the texture as an empty 1-d texture with the specified dimensions and
         * properties.  Follow up with set_ram_image() or modify_ram_image() to fill
         * the image data, or use set_clear_color to let the texture be cleared to a
         * solid color.
         */
        """
        pass

    def setup_2d_texture(self, const_Texture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        setup_2d_texture(const Texture self)
        setup_2d_texture(const Texture self, int x_size, int y_size, int component_type, int format)
        
        /**
         * Sets the texture as an empty 2-d texture with no dimensions.  Follow up
         * with read() or load() to fill the texture properties and image data, or use
         * set_clear_color to let the texture be cleared to a solid color.
         */
        
        /**
         * Sets the texture as an empty 2-d texture with the specified dimensions and
         * properties.  Follow up with set_ram_image() or modify_ram_image() to fill
         * the image data, or use set_clear_color to let the texture be cleared to a
         * solid color.
         */
        """
        pass

    def setup_2d_texture_array(self, const_Texture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        setup_2d_texture_array(const Texture self)
        setup_2d_texture_array(const Texture self, int z_size)
        setup_2d_texture_array(const Texture self, int x_size, int y_size, int z_size, int component_type, int format)
        
        /**
         * Sets the texture as an empty 2-d texture array with no dimensions (though
         * if you know the depth ahead of time, it saves a bit of reallocation later).
         * Follow up with read() or load() to fill the texture properties and image
         * data, or use set_clear_color to let the texture be cleared to a solid
         * color.
         */
        
        /**
         * Sets the texture as an empty 2-d texture array with the specified
         * dimensions and properties.  Follow up with set_ram_image() or
         * modify_ram_image() to fill the image data, or use set_clear_color to let
         * the texture be cleared to a solid color.
         */
        """
        pass

    def setup_3d_texture(self, const_Texture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        setup_3d_texture(const Texture self)
        setup_3d_texture(const Texture self, int z_size)
        setup_3d_texture(const Texture self, int x_size, int y_size, int z_size, int component_type, int format)
        
        /**
         * Sets the texture as an empty 3-d texture with no dimensions (though if you
         * know the depth ahead of time, it saves a bit of reallocation later). Follow
         * up with read() or load() to fill the texture properties and image data, or
         * use set_clear_color to let the texture be cleared to a solid color.
         */
        
        /**
         * Sets the texture as an empty 3-d texture with the specified dimensions and
         * properties.  Follow up with set_ram_image() or modify_ram_image() to fill
         * the image data.
         */
        """
        pass

    def setup_buffer_texture(self, const_Texture_self, int_size, int_component_type, int_format, int_usage): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        setup_buffer_texture(const Texture self, int size, int component_type, int format, int usage)
        
        /**
         * Sets the texture as an empty buffer texture with the specified size and
         * properties.  Follow up with set_ram_image() or modify_ram_image() to fill
         * the image data, or use set_clear_color to let the texture be cleared to a
         * solid color.
         *
         * Note that a buffer texture's format needs to match the component type.
         */
        """
        pass

    def setup_cube_map(self, const_Texture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        setup_cube_map(const Texture self)
        setup_cube_map(const Texture self, int size, int component_type, int format)
        
        /**
         * Sets the texture as an empty cube map texture with no dimensions.  Follow
         * up with read() or load() to fill the texture properties and image data, or
         * use set_clear_color to let the texture be cleared to a solid color.
         */
        
        /**
         * Sets the texture as an empty cube map texture with the specified dimensions
         * and properties.  Follow up with set_ram_image() or modify_ram_image() to
         * fill the image data, or use set_clear_color to let the texture be cleared
         * to a solid color.
         *
         * Note that a cube map should always consist of six square images, so x_size
         * and y_size will be the same, and z_size is always 6.
         */
        """
        pass

    def setup_cube_map_array(self, const_Texture_self, int_num_cube_maps): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        setup_cube_map_array(const Texture self, int num_cube_maps)
        setup_cube_map_array(const Texture self, int size, int num_cube_maps, int component_type, int format)
        
        /**
         * Sets the texture as cube map array with N cube maps.  Note that this number
         * is not the same as the z_size.  Follow up with read() or load() to fill the
         * texture properties and image data, or use set_clear_color to let the
         * texture be cleared to a solid color.
         *
         * @since 1.10.0
         */
        
        /**
         * Sets the texture as cube map array with N cube maps with the specified
         * dimensions and format.  Follow up with set_ram_image() or
         * modify_ram_image() to fill the image data, or use set_clear_color to let
         * the texture be cleared to a solid color.
         *
         * The num_cube_maps given here is multiplied by six to become the z_size of
         * the image.
         *
         * @since 1.10.0
         */
        """
        pass

    def setup_texture(self, const_Texture_self, int_texture_type, int_x_size, int_y_size, int_z_size, int_component_type, int_format): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        setup_texture(const Texture self, int texture_type, int x_size, int y_size, int z_size, int component_type, int format)
        
        /**
         * Sets the texture to the indicated type and dimensions, presumably in
         * preparation for calling read() or load(), or set_ram_image() or
         * modify_ram_image(), or use set_clear_color to let the texture be cleared to
         * a solid color.
         */
        """
        pass

    def setWrapU(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_wrap_u(const Texture self, int wrap)
        
        /**
         * This setting determines what happens when the texture is sampled with a U
         * value outside the range 0.0-1.0.  The default is WM_repeat, which indicates
         * that the texture should repeat indefinitely.
         *
         * This sets the default sampler state for this texture; it may still be
         * overridden by a sampler state specified at a higher level.
         */
        """
        pass

    def setWrapV(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_wrap_v(const Texture self, int wrap)
        
        /**
         * This setting determines what happens when the texture is sampled with a V
         * value outside the range 0.0-1.0.  The default is WM_repeat, which indicates
         * that the texture should repeat indefinitely.
         *
         * This sets the default sampler state for this texture; it may still be
         * overridden by a sampler state specified at a higher level.
         */
        """
        pass

    def setWrapW(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_wrap_w(const Texture self, int wrap)
        
        /**
         * The W wrap direction is only used for 3-d textures.
         *
         * This sets the default sampler state for this texture; it may still be
         * overridden by a sampler state specified at a higher level.
         */
        """
        pass

    def setXSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_x_size(const Texture self, int x_size)
        
        /**
         * Changes the x size indicated for the texture.  This also implicitly unloads
         * the texture if it has already been loaded.
         */
        """
        pass

    def setYSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_y_size(const Texture self, int y_size)
        
        /**
         * Changes the y size indicated for the texture.  This also implicitly unloads
         * the texture if it has already been loaded.
         */
        """
        pass

    def setZSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_z_size(const Texture self, int z_size)
        
        /**
         * Changes the z size indicated for the texture.  This also implicitly unloads
         * the texture if it has already been loaded.
         */
        """
        pass

    def set_alpha_filename(self, const_Texture_self, const_Filename_alpha_filename): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_alpha_filename(const Texture self, const Filename alpha_filename)
        
        /**
         * Sets the name of the file that contains the image's alpha channel contents.
         * Normally, this is set automatically when the image is loaded, for instance
         * via Texture::read().
         *
         * The Texture's get_filename() function returns the name of the image file
         * that was loaded into the buffer.  In the case where a texture specified two
         * separate files to load, a 1- or 3-channel color image and a 1-channel alpha
         * image, this Filename is update to contain the name of the image file that
         * was loaded into the buffer's alpha channel.
         */
        """
        pass

    def set_alpha_fullpath(self, const_Texture_self, const_Filename_alpha_fullpath): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_alpha_fullpath(const Texture self, const Filename alpha_fullpath)
        
        /**
         * Sets the full pathname to the file that contains the image's alpha channel
         * contents, as found along the search path.  Normally, this is set
         * automatically when the image is loaded, for instance via Texture::read().
         */
        """
        pass

    def set_anisotropic_degree(self, const_Texture_self, int_anisotropic_degree): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_anisotropic_degree(const Texture self, int anisotropic_degree)
        
        /**
         * Specifies the level of anisotropic filtering to apply to the texture.  Set
         * this 0 to indicate the default value, which is specified in the texture-
         * anisotropic-degree config variable.
         *
         * To explicitly disable anisotropic filtering, set this value to 1.  To
         * explicitly enable anisotropic filtering, set it to a value higher than 1;
         * larger numbers indicate greater degrees of filtering.
         *
         * This sets the default sampler state for this texture; it may still be
         * overridden by a sampler state specified at a higher level.
         */
        """
        pass

    def set_auto_texture_scale(self, const_Texture_self, int_scale): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_auto_texture_scale(const Texture self, int scale)
        
        /**
         * Specifies the power-of-2 texture-scaling mode that will be applied to this
         * particular texture when it is next loaded from disk.  See
         * set_textures_power_2().
         */
        """
        pass

    def set_aux_data(self, const_Texture_self, str_key, TypedReferenceCount_aux_data): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_aux_data(const Texture self, str key, TypedReferenceCount aux_data)
        
        /**
         * Records an arbitrary object in the Texture, associated with a specified
         * key.  The object may later be retrieved by calling get_aux_data() with the
         * same key.
         *
         * These data objects are not recorded to a bam or txo file.
         */
        """
        pass

    def set_border_color(self, const_Texture_self, const_LVecBase4f_color): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_border_color(const Texture self, const LVecBase4f color)
        
        /**
         * Specifies the solid color of the texture's border.  Some OpenGL
         * implementations use a border for tiling textures; in Panda, it is only used
         * for specifying the clamp color.
         *
         * This sets the default sampler state for this texture; it may still be
         * overridden by a sampler state specified at a higher level.
         */
        """
        pass

    def set_clear_color(self, const_Texture_self, const_LVecBase4f_color): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_clear_color(const Texture self, const LVecBase4f color)
        
        /**
         * Sets the color that will be used to fill the texture image in absence of
         * any image data.  It is used when any of the setup_texture functions or
         * clear_image is called and image data is not provided using read() or
         * modify_ram_image().
         *
         * This does not affect a texture that has already been cleared; call
         * clear_image to clear it again.
         */
        """
        pass

    def set_component_type(self, const_Texture_self, int_component_type): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_component_type(const Texture self, int component_type)
        
        /**
         * Changes the data value for the texture components.  This implicitly sets
         * component_width as well.
         */
        """
        pass

    def set_compression(self, const_Texture_self, int_compression): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_compression(const Texture self, int compression)
        
        /**
         * Requests that this particular Texture be compressed when it is loaded into
         * texture memory.
         *
         * This refers to the internal compression of the texture image within texture
         * memory; it is not related to jpeg or png compression, which are disk file
         * compression formats.  The actual disk file that generated this texture may
         * be stored in a compressed or uncompressed format supported by Panda; it
         * will be decompressed on load, and then recompressed by the graphics API if
         * this parameter is not CM_off.
         *
         * If the GSG does not support this texture compression mode, the texture will
         * silently be loaded uncompressed.
         */
        """
        pass

    def set_default_sampler(self, const_Texture_self, const_SamplerState_sampler): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_default_sampler(const Texture self, const SamplerState sampler)
        
        /**
         * This sets the default sampler state for this texture, containing the wrap
         * and filter properties specified on the texture level; it may still be
         * overridden by a sampler state specified at a higher level.  This
         * encompasses the settings for get_wrap_u, get_minfilter,
         * get_anisotropic_degree, etc.
         *
         * This makes a copy of the SamplerState object, so future modifications of
         * the same SamplerState will have no effect on this texture unless you call
         * set_default_sampler again.
         */
        """
        pass

    def set_filename(self, const_Texture_self, const_Filename_filename): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_filename(const Texture self, const Filename filename)
        
        /**
         * Sets the name of the file that contains the image's contents.  Normally,
         * this is set automatically when the image is loaded, for instance via
         * Texture::read().
         *
         * The Texture's get_name() function used to return the filename, but now
         * returns just the basename (without the extension), which is a more useful
         * name for identifying an image in show code.
         */
        """
        pass

    def set_format(self, const_Texture_self, int_format): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_format(const Texture self, int format)
        
        /**
         * Changes the format value for the texture components.  This implicitly sets
         * num_components as well.
         */
        """
        pass

    def set_fullpath(self, const_Texture_self, const_Filename_fullpath): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_fullpath(const Texture self, const Filename fullpath)
        
        /**
         * Sets the full pathname to the file that contains the image's contents, as
         * found along the search path.  Normally, this is set automatically when the
         * image is loaded, for instance via Texture::read().
         */
        """
        pass

    def set_keep_ram_image(self, const_Texture_self, bool_keep_ram_image): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_keep_ram_image(const Texture self, bool keep_ram_image)
        
        /**
         * Sets the flag that indicates whether this Texture is eligible to have its
         * main RAM copy of the texture memory dumped when the texture is prepared for
         * rendering.
         *
         * This will be false for most textures, which can reload their images if
         * needed by rereading the input file.  However, textures that were generated
         * dynamically and cannot be easily reloaded will want to set this flag to
         * true, so that the texture will always keep its image copy around.
         */
        """
        pass

    def set_loaded_from_image(self, const_Texture_self, bool_flag): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_loaded_from_image(const Texture self, bool flag)
        
        /**
         * Sets the flag that indicates the texture has been loaded from a disk file
         * or PNMImage.  You should also ensure the filename has been set correctly.
         * When this flag is true, the texture may be automatically reloaded when its
         * ram image needs to be replaced.
         */
        """
        pass

    def set_loaded_from_txo(self, const_Texture_self, bool_flag): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_loaded_from_txo(const Texture self, bool flag)
        
        /**
         * Sets the flag that indicates the texture has been loaded from a txo file.
         * You probably shouldn't be setting this directly; it is set automatically
         * when a Texture is loaded.
         */
        """
        pass

    def set_magfilter(self, const_Texture_self, int_filter): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_magfilter(const Texture self, int filter)
        
        /**
         * Sets the filtering method that should be used when viewing the texture up
         * close.
         *
         * This sets the default sampler state for this texture; it may still be
         * overridden by a sampler state specified at a higher level.
         */
        """
        pass

    def set_match_framebuffer_format(self, const_Texture_self, bool_flag): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_match_framebuffer_format(const Texture self, bool flag)
        
        /**
         * Sets the special flag that, if true, indicates to the GSG that the
         * Texture's format should be chosen to exactly match the framebuffer's
         * format, presumably because the application intends to copy image data from
         * the framebuffer into the Texture (or vice-versa).
         *
         * This sets only the graphics card's idea of the texture format; it is not
         * related to the system-memory format.
         */
        """
        pass

    def set_minfilter(self, const_Texture_self, int_filter): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_minfilter(const Texture self, int filter)
        
        /**
         * Sets the filtering method that should be used when viewing the texture from
         * a distance.
         *
         * This sets the default sampler state for this texture; it may still be
         * overridden by a sampler state specified at a higher level.
         */
        """
        pass

    def set_num_views(self, const_Texture_self, int_num_views): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_num_views(const Texture self, int num_views)
        
        /**
         * Sets the number of "views" within a texture.  A view is a completely
         * separate image stored within the Texture object.  Most textures have only
         * one view, but a stereo texture, for instance, may have two views, a left
         * and a right image.  Other uses for multiple views are not yet defined.
         *
         * If this value is greater than one, the additional views are accessed as
         * additional pages beyond get_z_size().
         *
         * This also implicitly unloads the texture if it has already been loaded.
         */
        """
        pass

    def set_orig_file_size(self, const_Texture_self, int_x, int_y, int_z): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_orig_file_size(const Texture self, int x, int y, int z)
        
        /**
         * Specifies the size of the texture as it exists in its original disk file,
         * before any Panda scaling.
         */
        """
        pass

    def set_pad_size(self, const_Texture_self, int_x, int_y, int_z): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_pad_size(const Texture self, int x, int y, int z)
        
        /**
         * Sets the size of the pad region.
         *
         * Sometimes, when a video card demands power-of-two textures, it is necessary
         * to create a big texture and then only use a portion of it.  The pad region
         * indicates which portion of the texture is not really in use.  All
         * operations use the texture as a whole, including the pad region, unless
         * they explicitly state that they use only the non-pad region.
         *
         * Changing the texture's size clears the pad region.
         */
        """
        pass

    def set_post_load_store_cache(self, const_Texture_self, bool_flag): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_post_load_store_cache(const Texture self, bool flag)
        
        /**
         * Sets the post_load_store_cache flag.  When this is set, the next time the
         * texture is loaded on a GSG, it will automatically extract its RAM image
         * from the GSG and save it to the global BamCache.
         *
         * This is used to store compressed RAM images in the BamCache.  This flag
         * should not be set explicitly; it is set automatically by the TexturePool
         * when model-cache-compressed-textures is set true.
         */
        """
        pass

    def set_quality_level(self, const_Texture_self, int_quality_level): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_quality_level(const Texture self, int quality_level)
        
        /**
         * Sets a hint to the renderer about the desired performance / quality
         * tradeoff for this particular texture.  This is most useful for the
         * tinydisplay software renderer; for normal, hardware-accelerated renderers,
         * this may have little or no effect.
         */
        """
        pass

    def set_ram_image(self, const_Texture_self, object_image, int_compression, int_page_size): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_ram_image(const Texture self, object image, int compression, int page_size)
        
        /**
         * Replaces the current system-RAM image with the new data.  If compression is
         * not CM_off, it indicates that the new data is already pre-compressed in the
         * indicated format.
         *
         * This does *not* affect keep_ram_image.
         */
        """
        pass

    def set_ram_image_as(self, const_Texture_self, object_image, str_provided_format): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_ram_image_as(const Texture self, object image, str provided_format)
        
        /**
         * Replaces the current system-RAM image with the new data, converting it
         * first if necessary from the indicated component-order format.  See
         * get_ram_image_as() for specifications about the format.  This method cannot
         * support compressed image data or sub-pages; use set_ram_image() for that.
         */
        """
        pass

    def set_ram_mipmap_image(self, const_Texture_self, int_n, ConstPointerToArray_image, int_page_size): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_ram_mipmap_image(const Texture self, int n, ConstPointerToArray image, int page_size)
        
        /**
         * Replaces the current system-RAM image for the indicated mipmap level with
         * the new data.  If compression is not CM_off, it indicates that the new data
         * is already pre-compressed in the indicated format.
         *
         * This does *not* affect keep_ram_image.
         */
        """
        pass

    def set_ram_mipmap_pointer_from_int(self, const_Texture_self, long_pointer, int_n, int_page_size): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_ram_mipmap_pointer_from_int(const Texture self, long pointer, int n, int page_size)
        
        /**
         * Accepts a raw pointer cast as an int, which is then passed to
         * set_ram_mipmap_pointer(); see the documentation for that method.
         *
         * This variant is particularly useful to set an external pointer from a
         * language like Python, which doesn't support void pointers directly.
         */
        """
        pass

    def set_render_to_texture(self, const_Texture_self, bool_render_to_texture): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_render_to_texture(const Texture self, bool render_to_texture)
        
        /**
         * Sets a flag on the texture that indicates whether the texture is intended
         * to be used as a direct-render target, by binding a framebuffer to a texture
         * and rendering directly into the texture.
         *
         * This controls some low-level choices made about the texture object itself.
         * For instance, compressed textures are disallowed when this flag is set
         * true.
         *
         * Normally, a user should not need to set this flag directly; it is set
         * automatically by the low-level display code when a texture is bound to a
         * framebuffer.
         */
        """
        pass

    def set_simple_ram_image(self, const_Texture_self, ConstPointerToArray_image, int_x_size, int_y_size): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_simple_ram_image(const Texture self, ConstPointerToArray image, int x_size, int y_size)
        
        /**
         * Replaces the internal "simple" texture image.  This can be used as an
         * option to display while the main texture image is being loaded from disk.
         * It is normally a very small image, 16x16 or smaller (and maybe even 1x1),
         * that is designed to give just enough sense of color to serve as a
         * placeholder until the full texture is available.
         *
         * The "simple" image is always 4 components, 1 byte each, regardless of the
         * parameters of the full texture.  The simple image is only supported for
         * ordinary 2-d textures.
         *
         * Also see generate_simple_ram_image(), modify_simple_ram_image(), and
         * new_simple_ram_image().
         */
        """
        pass

    def set_size_padded(self, const_Texture_self, int_x, int_y, int_z): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_size_padded(const Texture self, int x, int y, int z)
        
        /**
         * Changes the size of the texture, padding if necessary, and setting the pad
         * region as well.
         */
        """
        pass

    def set_textures_power_2(self, int_scale): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_textures_power_2(int scale)
        
        /**
         * Set this flag to ATS_none, ATS_up, ATS_down, or ATS_pad to control the
         * scaling of textures in general, if a particular texture does not override
         * this.  See also set_auto_texture_scale() for the per-texture override.
         */
        """
        pass

    def set_wrap_u(self, const_Texture_self, int_wrap): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_wrap_u(const Texture self, int wrap)
        
        /**
         * This setting determines what happens when the texture is sampled with a U
         * value outside the range 0.0-1.0.  The default is WM_repeat, which indicates
         * that the texture should repeat indefinitely.
         *
         * This sets the default sampler state for this texture; it may still be
         * overridden by a sampler state specified at a higher level.
         */
        """
        pass

    def set_wrap_v(self, const_Texture_self, int_wrap): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_wrap_v(const Texture self, int wrap)
        
        /**
         * This setting determines what happens when the texture is sampled with a V
         * value outside the range 0.0-1.0.  The default is WM_repeat, which indicates
         * that the texture should repeat indefinitely.
         *
         * This sets the default sampler state for this texture; it may still be
         * overridden by a sampler state specified at a higher level.
         */
        """
        pass

    def set_wrap_w(self, const_Texture_self, int_wrap): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_wrap_w(const Texture self, int wrap)
        
        /**
         * The W wrap direction is only used for 3-d textures.
         *
         * This sets the default sampler state for this texture; it may still be
         * overridden by a sampler state specified at a higher level.
         */
        """
        pass

    def set_x_size(self, const_Texture_self, int_x_size): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_x_size(const Texture self, int x_size)
        
        /**
         * Changes the x size indicated for the texture.  This also implicitly unloads
         * the texture if it has already been loaded.
         */
        """
        pass

    def set_y_size(self, const_Texture_self, int_y_size): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_y_size(const Texture self, int y_size)
        
        /**
         * Changes the y size indicated for the texture.  This also implicitly unloads
         * the texture if it has already been loaded.
         */
        """
        pass

    def set_z_size(self, const_Texture_self, int_z_size): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_z_size(const Texture self, int z_size)
        
        /**
         * Changes the z size indicated for the texture.  This also implicitly unloads
         * the texture if it has already been loaded.
         */
        """
        pass

    def store(self, Texture_self, PNMImage_pnmimage): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        store(Texture self, PNMImage pnmimage)
        store(Texture self, PfmFile pfm)
        store(Texture self, PNMImage pnmimage, int z, int n)
        store(Texture self, PfmFile pfm, int z, int n)
        
        /**
         * Saves the texture to the indicated PNMImage, but does not write it to disk.
         */
        
        /**
         * Saves the indicated page and mipmap level of the texture to the PNMImage.
         */
        
        /**
         * Saves the texture to the indicated PfmFile, but does not write it to disk.
         */
        
        /**
         * Saves the indicated page and mipmap level of the texture to the PfmFile.
         */
        """
        pass

    def stringComponentType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        string_component_type(str str)
        
        /**
         * Returns the ComponentType corresponding to the indicated string word.
         */
        """
        pass

    def stringCompressionMode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        string_compression_mode(str str)
        
        /**
         * Returns the CompressionMode value associated with the given string
         * representation.
         */
        """
        pass

    def stringFormat(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        string_format(str str)
        
        /**
         * Returns the Format corresponding to the indicated string word.
         */
        """
        pass

    def stringQualityLevel(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        string_quality_level(str str)
        
        /**
         * Returns the QualityLevel value associated with the given string
         * representation.
         */
        """
        pass

    def stringTextureType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        string_texture_type(str str)
        
        /**
         * Returns the TextureType corresponding to the indicated string word.
         */
        """
        pass

    def string_component_type(self, str_str): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        string_component_type(str str)
        
        /**
         * Returns the ComponentType corresponding to the indicated string word.
         */
        """
        pass

    def string_compression_mode(self, str_str): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        string_compression_mode(str str)
        
        /**
         * Returns the CompressionMode value associated with the given string
         * representation.
         */
        """
        pass

    def string_format(self, str_str): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        string_format(str str)
        
        /**
         * Returns the Format corresponding to the indicated string word.
         */
        """
        pass

    def string_quality_level(self, str_str): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        string_quality_level(str str)
        
        /**
         * Returns the QualityLevel value associated with the given string
         * representation.
         */
        """
        pass

    def string_texture_type(self, str_str): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        string_texture_type(str str)
        
        /**
         * Returns the TextureType corresponding to the indicated string word.
         */
        """
        pass

    def uncompressRamImage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        uncompress_ram_image(const Texture self)
        
        /**
         * Attempts to uncompress the texture's RAM image internally.  In order for
         * this to work, the squish library must have been compiled into Panda, and
         * the ram image must be compressed in a format supported by squish.
         *
         * Returns true if successful, false otherwise.
         */
        """
        pass

    def uncompress_ram_image(self, const_Texture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        uncompress_ram_image(const Texture self)
        
        /**
         * Attempts to uncompress the texture's RAM image internally.  In order for
         * this to work, the squish library must have been compiled into Panda, and
         * the ram image must be compressed in a format supported by squish.
         *
         * Returns true if successful, false otherwise.
         */
        """
        pass

    def upcastToNamable(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_Namable(const Texture self)
        
        upcast from Texture to Namable
        """
        pass

    def upcastToTypedWritableReferenceCount(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_TypedWritableReferenceCount(const Texture self)
        
        upcast from Texture to TypedWritableReferenceCount
        """
        pass

    def upcast_to_Namable(self, const_Texture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_Namable(const Texture self)
        
        upcast from Texture to Namable
        """
        pass

    def upcast_to_TypedWritableReferenceCount(self, const_Texture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_TypedWritableReferenceCount(const Texture self)
        
        upcast from Texture to TypedWritableReferenceCount
        """
        pass

    def upToPower2(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        up_to_power_2(int value)
        
        /**
         * Returns the smallest power of 2 greater than or equal to value.
         */
        """
        pass

    def up_to_power_2(self, int_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        up_to_power_2(int value)
        
        /**
         * Returns the smallest power of 2 greater than or equal to value.
         */
        """
        pass

    def usesMipmaps(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        uses_mipmaps(Texture self)
        
        /**
         * Returns true if the minfilter settings on this texture indicate the use of
         * mipmapping, false otherwise.
         */
        """
        pass

    def uses_mipmaps(self, Texture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        uses_mipmaps(Texture self)
        
        /**
         * Returns true if the minfilter settings on this texture indicate the use of
         * mipmapping, false otherwise.
         */
        """
        pass

    def wasImageModified(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        was_image_modified(Texture self, PreparedGraphicsObjects prepared_objects)
        
        /**
         * Returns true if the texture needs to be re-loaded onto the indicated GSG,
         * either because its image data is out-of-date, or because it's not fully
         * prepared now.
         */
        """
        pass

    def was_image_modified(self, Texture_self, PreparedGraphicsObjects_prepared_objects): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        was_image_modified(Texture self, PreparedGraphicsObjects prepared_objects)
        
        /**
         * Returns true if the texture needs to be re-loaded onto the indicated GSG,
         * either because its image data is out-of-date, or because it's not fully
         * prepared now.
         */
        """
        pass

    def write(self, const_Texture_self, const_Filename_fullpath): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(const Texture self, const Filename fullpath)
        write(Texture self, ostream out, int indent_level)
        write(const Texture self, const Filename fullpath, int z, int n, bool write_pages, bool write_mipmaps)
        
        /**
         * Writes the texture to the named filename.
         */
        
        /**
         * Writes a single page or mipmap level to a single file, or automatically
         * writes a series of pages and/or mipmap levels to a numbered series of
         * files.
         *
         * If the filename ends in the extension .txo, this implicitly writes a Panda
         * texture object (.txo) instead of an image file.  In this case, the
         * remaining parameters are ignored, and only one file is written, which will
         * contain all of the pages and resident mipmap levels in the texture.
         *
         * If write_pages is false, then z indicates the page number to write.  3-D
         * textures have one page number for each level of depth; cube maps have six
         * pages number 0 through 5.  Other kinds of textures have only one page,
         * numbered 0.  If there are multiple views, the range of z is increased; the
         * total range is [0, get_num_pages()).
         *
         * If write_pages is true, then all pages of the texture will be written.  In
         * this case z is ignored, and the filename should contain a sequence of hash
         * marks ("#") which will be filled in with the page index number.
         *
         * If write_mipmaps is false, then n indicates the mipmap level number to
         * write.  Normally, this is 0, for the base texture image.  Normally, the
         * mipmap levels of a texture are not available in RAM (they are generated
         * automatically by the graphics card). However, if you have the mipmap levels
         * available, for instance because you called generate_ram_mipmap_images() to
         * generate them internally, or you called
         * GraphicsEngine::extract_texture_data() to retrieve them from the graphics
         * card, then you may write out each mipmap level with this parameter.
         *
         * If write_mipmaps is true, then all mipmap levels of the texture will be
         * written.  In this case n is ignored, and the filename should contain a
         * sequence of hash marks ("#") which will be filled in with the mipmap level
         * number.
         *
         * If both write_pages and write_mipmaps is true, then all pages and all
         * mipmap levels will be written.  In this case, the filename should contain
         * two different sequences of hash marks, separated by a character such as a
         * hyphen, underscore, or dot.  The first hash mark sequence will be filled in
         * with the mipmap level, while the second hash mark sequence will be the page
         * index.
         */
        
        /**
         * Not to be confused with write(Filename), this method simply describes the
         * texture properties.
         */
        """
        pass

    def writeTxo(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        write_txo(Texture self, ostream out, str filename)
        
        /**
         * Writes the texture to a Panda texture object.  This defines the complete
         * Texture specification, including the image data as well as all texture
         * properties.
         *
         * The filename is just for reference.
         */
        """
        pass

    def write_txo(self, Texture_self, ostream_out, str_filename): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write_txo(Texture self, ostream out, str filename)
        
        /**
         * Writes the texture to a Panda texture object.  This defines the complete
         * Texture specification, including the image data as well as all texture
         * properties.
         *
         * The filename is just for reference.
         */
        """
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __deepcopy__(self, Texture_self, object_memo): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        __deepcopy__(Texture self, object memo)
        """
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

    alpha_fullpath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    anisotropic_degree = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    auto_texture_scale = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    aux_data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    border_color = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    cacheable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    clear_color = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    component_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    component_width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    compression = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """// Could maybe use has_compression here, too"""

    default_sampler = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    effective_anisotropic_degree = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    effective_magfilter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    effective_minfilter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    effective_quality_level = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    expected_num_mipmap_levels = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    expected_ram_image_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    expected_ram_page_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    filename = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    format = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    fullpath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    image_modified = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    keep_ram_image = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    loaded_from_image = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    loaded_from_txo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    magfilter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    match_framebuffer_format = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    minfilter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    num_components = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    num_loadable_ram_mipmap_images = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    num_pages = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    num_ram_mipmap_images = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    num_views = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    orig_file_x_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    orig_file_y_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    orig_file_z_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    post_load_store_cache = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    properties_modified = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    quality_level = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ram_image_compression = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ram_image_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ram_page_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ram_view_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    render_to_texture = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    simple_image_modified = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    simple_ram_image = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    simple_x_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    simple_y_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    texture_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    usage_hint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    wrap_u = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    wrap_v = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    wrap_w = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    x_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    y_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    z_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    CMDefault = 0
    CMDxt1 = 4
    CMDxt2 = 5
    CMDxt3 = 6
    CMDxt4 = 7
    CMDxt5 = 8
    CMEac = 14
    CMEtc1 = 12
    CMEtc2 = 13
    CMFxt1 = 3
    CMOff = 1
    CMOn = 2
    CMPvr12bpp = 9
    CMPvr14bpp = 10
    CMRgtc = 11
    CM_default = 0
    CM_dxt1 = 4
    CM_dxt2 = 5
    CM_dxt3 = 6
    CM_dxt4 = 7
    CM_dxt5 = 8
    CM_eac = 14
    CM_etc1 = 12
    CM_etc2 = 13
    CM_fxt1 = 3
    CM_off = 1
    CM_on = 2
    CM_pvr1_2bpp = 9
    CM_pvr1_4bpp = 10
    CM_rgtc = 11
    DtoolClassDict = {
        'CMDefault': 0,
        'CMDxt1': 4,
        'CMDxt2': 5,
        'CMDxt3': 6,
        'CMDxt4': 7,
        'CMDxt5': 8,
        'CMEac': 14,
        'CMEtc1': 12,
        'CMEtc2': 13,
        'CMFxt1': 3,
        'CMOff': 1,
        'CMOn': 2,
        'CMPvr12bpp': 9,
        'CMPvr14bpp': 10,
        'CMRgtc': 11,
        'CM_default': 0,
        'CM_dxt1': 4,
        'CM_dxt2': 5,
        'CM_dxt3': 6,
        'CM_dxt4': 7,
        'CM_dxt5': 8,
        'CM_eac': 14,
        'CM_etc1': 12,
        'CM_etc2': 13,
        'CM_fxt1': 3,
        'CM_off': 1,
        'CM_on': 2,
        'CM_pvr1_2bpp': 9,
        'CM_pvr1_4bpp': 10,
        'CM_rgtc': 11,
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        'FAlpha': 6,
        'FBlue': 5,
        'FColorIndex': 2,
        'FDepthComponent': 23,
        'FDepthComponent16': 24,
        'FDepthComponent24': 25,
        'FDepthComponent32': 26,
        'FDepthStencil': 1,
        'FGreen': 4,
        'FLuminance': 18,
        'FLuminanceAlpha': 19,
        'FLuminanceAlphamask': 20,
        'FR11G11B10': 42,
        'FR16': 27,
        'FR16i': 46,
        'FR32': 35,
        'FR32i': 34,
        'FR8i': 38,
        'FRed': 3,
        'FRg': 45,
        'FRg16': 28,
        'FRg16i': 47,
        'FRg32': 36,
        'FRg32i': 50,
        'FRg8i': 39,
        'FRgb': 7,
        'FRgb10A2': 44,
        'FRgb12': 10,
        'FRgb16': 29,
        'FRgb16i': 48,
        'FRgb32': 37,
        'FRgb32i': 51,
        'FRgb332': 11,
        'FRgb5': 8,
        'FRgb8': 9,
        'FRgb8i': 40,
        'FRgb9E5': 43,
        'FRgba': 12,
        'FRgba12': 17,
        'FRgba16': 21,
        'FRgba16i': 49,
        'FRgba32': 22,
        'FRgba32i': 52,
        'FRgba4': 14,
        'FRgba5': 15,
        'FRgba8': 16,
        'FRgba8i': 41,
        'FRgbm': 13,
        'FSluminance': 32,
        'FSluminanceAlpha': 33,
        'FSrgb': 30,
        'FSrgbAlpha': 31,
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
        'F_alpha': 6,
        'F_blue': 5,
        'F_color_index': 2,
        'F_depth_component': 23,
        'F_depth_component16': 24,
        'F_depth_component24': 25,
        'F_depth_component32': 26,
        'F_depth_stencil': 1,
        'F_green': 4,
        'F_luminance': 18,
        'F_luminance_alpha': 19,
        'F_luminance_alphamask': 20,
        'F_r11_g11_b10': 42,
        'F_r16': 27,
        'F_r16i': 46,
        'F_r32': 35,
        'F_r32i': 34,
        'F_r8i': 38,
        'F_red': 3,
        'F_rg': 45,
        'F_rg16': 28,
        'F_rg16i': 47,
        'F_rg32': 36,
        'F_rg32i': 50,
        'F_rg8i': 39,
        'F_rgb': 7,
        'F_rgb10_a2': 44,
        'F_rgb12': 10,
        'F_rgb16': 29,
        'F_rgb16i': 48,
        'F_rgb32': 37,
        'F_rgb32i': 51,
        'F_rgb332': 11,
        'F_rgb5': 8,
        'F_rgb8': 9,
        'F_rgb8i': 40,
        'F_rgb9_e5': 43,
        'F_rgba': 12,
        'F_rgba12': 17,
        'F_rgba16': 21,
        'F_rgba16i': 49,
        'F_rgba32': 22,
        'F_rgba32i': 52,
        'F_rgba4': 14,
        'F_rgba5': 15,
        'F_rgba8': 16,
        'F_rgba8i': 41,
        'F_rgbm': 13,
        'F_sluminance': 32,
        'F_sluminance_alpha': 33,
        'F_srgb': 30,
        'F_srgb_alpha': 31,
        'QLBest': 3,
        'QLDefault': 0,
        'QLFastest': 1,
        'QLNormal': 2,
        'QL_best': 3,
        'QL_default': 0,
        'QL_fastest': 1,
        'QL_normal': 2,
        'TByte': 5,
        'TFloat': 2,
        'THalfFloat': 7,
        'TInt': 4,
        'TShort': 6,
        'TT1dTexture': 0,
        'TT1dTextureArray': 7,
        'TT2dTexture': 1,
        'TT2dTextureArray': 3,
        'TT3dTexture': 2,
        'TTBufferTexture': 5,
        'TTCubeMap': 4,
        'TTCubeMapArray': 6,
        'TT_1d_texture': 0,
        'TT_1d_texture_array': 7,
        'TT_2d_texture': 1,
        'TT_2d_texture_array': 3,
        'TT_3d_texture': 2,
        'TT_buffer_texture': 5,
        'TT_cube_map': 4,
        'TT_cube_map_array': 6,
        'TUnsignedByte': 0,
        'TUnsignedInt': 8,
        'TUnsignedInt248': 3,
        'TUnsignedShort': 1,
        'T_byte': 5,
        'T_float': 2,
        'T_half_float': 7,
        'T_int': 4,
        'T_short': 6,
        'T_unsigned_byte': 0,
        'T_unsigned_int': 8,
        'T_unsigned_int_24_8': 3,
        'T_unsigned_short': 1,
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
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.Texture' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.Texture' objects>"
        '__doc__': "/**\n * Represents a texture object, which is typically a single 2-d image but may\n * also represent a 1-d or 3-d texture image, or the six 2-d faces of a cube\n * map texture.\n *\n * A texture's image data might be stored in system RAM (see get_ram_image())\n * or its image may be represented in texture memory on one or more\n * GraphicsStateGuardians (see prepare()), or both.  The typical usage pattern\n * is that a texture is loaded from an image file on disk, which copies its\n * image data into system RAM; then the first time the texture is rendered its\n * image data is copied to texture memory (actually, to the graphics API), and\n * the system RAM image is automatically freed.\n */",
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.Texture' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2FED40>'
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.Texture' objects>"
        'alpha_filename': None, # (!) real value is "<attribute 'alpha_filename' of 'panda3d.core.Texture' objects>"
        'alpha_fullpath': None, # (!) real value is "<attribute 'alpha_fullpath' of 'panda3d.core.Texture' objects>"
        'anisotropic_degree': None, # (!) real value is "<attribute 'anisotropic_degree' of 'panda3d.core.Texture' objects>"
        'auto_texture_scale': None, # (!) real value is "<attribute 'auto_texture_scale' of 'panda3d.core.Texture' objects>"
        'aux_data': None, # (!) real value is "<attribute 'aux_data' of 'panda3d.core.Texture' objects>"
        'border_color': None, # (!) real value is "<attribute 'border_color' of 'panda3d.core.Texture' objects>"
        'cacheable': None, # (!) real value is "<attribute 'cacheable' of 'panda3d.core.Texture' objects>"
        'clear': None, # (!) real value is "<method 'clear' of 'panda3d.core.Texture' objects>"
        'clearAlphaFilename': None, # (!) real value is "<method 'clearAlphaFilename' of 'panda3d.core.Texture' objects>"
        'clearAlphaFullpath': None, # (!) real value is "<method 'clearAlphaFullpath' of 'panda3d.core.Texture' objects>"
        'clearAuxData': None, # (!) real value is "<method 'clearAuxData' of 'panda3d.core.Texture' objects>"
        'clearClearColor': None, # (!) real value is "<method 'clearClearColor' of 'panda3d.core.Texture' objects>"
        'clearFilename': None, # (!) real value is "<method 'clearFilename' of 'panda3d.core.Texture' objects>"
        'clearFullpath': None, # (!) real value is "<method 'clearFullpath' of 'panda3d.core.Texture' objects>"
        'clearImage': None, # (!) real value is "<method 'clearImage' of 'panda3d.core.Texture' objects>"
        'clearRamImage': None, # (!) real value is "<method 'clearRamImage' of 'panda3d.core.Texture' objects>"
        'clearRamMipmapImage': None, # (!) real value is "<method 'clearRamMipmapImage' of 'panda3d.core.Texture' objects>"
        'clearRamMipmapImages': None, # (!) real value is "<method 'clearRamMipmapImages' of 'panda3d.core.Texture' objects>"
        'clearSimpleRamImage': None, # (!) real value is "<method 'clearSimpleRamImage' of 'panda3d.core.Texture' objects>"
        'clear_alpha_filename': None, # (!) real value is "<method 'clear_alpha_filename' of 'panda3d.core.Texture' objects>"
        'clear_alpha_fullpath': None, # (!) real value is "<method 'clear_alpha_fullpath' of 'panda3d.core.Texture' objects>"
        'clear_aux_data': None, # (!) real value is "<method 'clear_aux_data' of 'panda3d.core.Texture' objects>"
        'clear_clear_color': None, # (!) real value is "<method 'clear_clear_color' of 'panda3d.core.Texture' objects>"
        'clear_color': None, # (!) real value is "<attribute 'clear_color' of 'panda3d.core.Texture' objects>"
        'clear_filename': None, # (!) real value is "<method 'clear_filename' of 'panda3d.core.Texture' objects>"
        'clear_fullpath': None, # (!) real value is "<method 'clear_fullpath' of 'panda3d.core.Texture' objects>"
        'clear_image': None, # (!) real value is "<method 'clear_image' of 'panda3d.core.Texture' objects>"
        'clear_ram_image': None, # (!) real value is "<method 'clear_ram_image' of 'panda3d.core.Texture' objects>"
        'clear_ram_mipmap_image': None, # (!) real value is "<method 'clear_ram_mipmap_image' of 'panda3d.core.Texture' objects>"
        'clear_ram_mipmap_images': None, # (!) real value is "<method 'clear_ram_mipmap_images' of 'panda3d.core.Texture' objects>"
        'clear_simple_ram_image': None, # (!) real value is "<method 'clear_simple_ram_image' of 'panda3d.core.Texture' objects>"
        'component_type': None, # (!) real value is "<attribute 'component_type' of 'panda3d.core.Texture' objects>"
        'component_width': None, # (!) real value is "<attribute 'component_width' of 'panda3d.core.Texture' objects>"
        'compressRamImage': None, # (!) real value is "<method 'compressRamImage' of 'panda3d.core.Texture' objects>"
        'compress_ram_image': None, # (!) real value is "<method 'compress_ram_image' of 'panda3d.core.Texture' objects>"
        'compression': None, # (!) real value is "<attribute 'compression' of 'panda3d.core.Texture' objects>"
        'considerRescale': None, # (!) real value is "<method 'considerRescale' of 'panda3d.core.Texture' objects>"
        'consider_rescale': None, # (!) real value is "<method 'consider_rescale' of 'panda3d.core.Texture' objects>"
        'default_sampler': None, # (!) real value is "<attribute 'default_sampler' of 'panda3d.core.Texture' objects>"
        'downToPower2': None, # (!) real value is '<staticmethod(<built-in method downToPower2 of type object at 0x00007FFCFE2FED40>)>'
        'down_to_power_2': None, # (!) real value is '<staticmethod(<built-in method down_to_power_2 of type object at 0x00007FFCFE2FED40>)>'
        'effective_anisotropic_degree': None, # (!) real value is "<attribute 'effective_anisotropic_degree' of 'panda3d.core.Texture' objects>"
        'effective_magfilter': None, # (!) real value is "<attribute 'effective_magfilter' of 'panda3d.core.Texture' objects>"
        'effective_minfilter': None, # (!) real value is "<attribute 'effective_minfilter' of 'panda3d.core.Texture' objects>"
        'effective_quality_level': None, # (!) real value is "<attribute 'effective_quality_level' of 'panda3d.core.Texture' objects>"
        'estimateTextureMemory': None, # (!) real value is "<method 'estimateTextureMemory' of 'panda3d.core.Texture' objects>"
        'estimate_texture_memory': None, # (!) real value is "<method 'estimate_texture_memory' of 'panda3d.core.Texture' objects>"
        'expected_num_mipmap_levels': None, # (!) real value is "<attribute 'expected_num_mipmap_levels' of 'panda3d.core.Texture' objects>"
        'expected_ram_image_size': None, # (!) real value is "<attribute 'expected_ram_image_size' of 'panda3d.core.Texture' objects>"
        'expected_ram_page_size': None, # (!) real value is "<attribute 'expected_ram_page_size' of 'panda3d.core.Texture' objects>"
        'filename': None, # (!) real value is "<attribute 'filename' of 'panda3d.core.Texture' objects>"
        'format': None, # (!) real value is "<attribute 'format' of 'panda3d.core.Texture' objects>"
        'formatComponentType': None, # (!) real value is '<staticmethod(<built-in method formatComponentType of type object at 0x00007FFCFE2FED40>)>'
        'formatCompressionMode': None, # (!) real value is '<staticmethod(<built-in method formatCompressionMode of type object at 0x00007FFCFE2FED40>)>'
        'formatFormat': None, # (!) real value is '<staticmethod(<built-in method formatFormat of type object at 0x00007FFCFE2FED40>)>'
        'formatQualityLevel': None, # (!) real value is '<staticmethod(<built-in method formatQualityLevel of type object at 0x00007FFCFE2FED40>)>'
        'formatTextureType': None, # (!) real value is '<staticmethod(<built-in method formatTextureType of type object at 0x00007FFCFE2FED40>)>'
        'format_component_type': None, # (!) real value is '<staticmethod(<built-in method format_component_type of type object at 0x00007FFCFE2FED40>)>'
        'format_compression_mode': None, # (!) real value is '<staticmethod(<built-in method format_compression_mode of type object at 0x00007FFCFE2FED40>)>'
        'format_format': None, # (!) real value is '<staticmethod(<built-in method format_format of type object at 0x00007FFCFE2FED40>)>'
        'format_quality_level': None, # (!) real value is '<staticmethod(<built-in method format_quality_level of type object at 0x00007FFCFE2FED40>)>'
        'format_texture_type': None, # (!) real value is '<staticmethod(<built-in method format_texture_type of type object at 0x00007FFCFE2FED40>)>'
        'fullpath': None, # (!) real value is "<attribute 'fullpath' of 'panda3d.core.Texture' objects>"
        'generateAlphaScaleMap': None, # (!) real value is "<method 'generateAlphaScaleMap' of 'panda3d.core.Texture' objects>"
        'generateNormalizationCubeMap': None, # (!) real value is "<method 'generateNormalizationCubeMap' of 'panda3d.core.Texture' objects>"
        'generateRamMipmapImages': None, # (!) real value is "<method 'generateRamMipmapImages' of 'panda3d.core.Texture' objects>"
        'generateSimpleRamImage': None, # (!) real value is "<method 'generateSimpleRamImage' of 'panda3d.core.Texture' objects>"
        'generate_alpha_scale_map': None, # (!) real value is "<method 'generate_alpha_scale_map' of 'panda3d.core.Texture' objects>"
        'generate_normalization_cube_map': None, # (!) real value is "<method 'generate_normalization_cube_map' of 'panda3d.core.Texture' objects>"
        'generate_ram_mipmap_images': None, # (!) real value is "<method 'generate_ram_mipmap_images' of 'panda3d.core.Texture' objects>"
        'generate_simple_ram_image': None, # (!) real value is "<method 'generate_simple_ram_image' of 'panda3d.core.Texture' objects>"
        'getActive': None, # (!) real value is "<method 'getActive' of 'panda3d.core.Texture' objects>"
        'getAlphaFilename': None, # (!) real value is "<method 'getAlphaFilename' of 'panda3d.core.Texture' objects>"
        'getAlphaFullpath': None, # (!) real value is "<method 'getAlphaFullpath' of 'panda3d.core.Texture' objects>"
        'getAnisotropicDegree': None, # (!) real value is "<method 'getAnisotropicDegree' of 'panda3d.core.Texture' objects>"
        'getAutoTextureScale': None, # (!) real value is "<method 'getAutoTextureScale' of 'panda3d.core.Texture' objects>"
        'getAuxData': None, # (!) real value is "<method 'getAuxData' of 'panda3d.core.Texture' objects>"
        'getBorderColor': None, # (!) real value is "<method 'getBorderColor' of 'panda3d.core.Texture' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2FED40>)>'
        'getClearColor': None, # (!) real value is "<method 'getClearColor' of 'panda3d.core.Texture' objects>"
        'getClearData': None, # (!) real value is "<method 'getClearData' of 'panda3d.core.Texture' objects>"
        'getComponentType': None, # (!) real value is "<method 'getComponentType' of 'panda3d.core.Texture' objects>"
        'getComponentWidth': None, # (!) real value is "<method 'getComponentWidth' of 'panda3d.core.Texture' objects>"
        'getCompression': None, # (!) real value is "<method 'getCompression' of 'panda3d.core.Texture' objects>"
        'getDataSizeBytes': None, # (!) real value is "<method 'getDataSizeBytes' of 'panda3d.core.Texture' objects>"
        'getDefaultSampler': None, # (!) real value is "<method 'getDefaultSampler' of 'panda3d.core.Texture' objects>"
        'getEffectiveAnisotropicDegree': None, # (!) real value is "<method 'getEffectiveAnisotropicDegree' of 'panda3d.core.Texture' objects>"
        'getEffectiveMagfilter': None, # (!) real value is "<method 'getEffectiveMagfilter' of 'panda3d.core.Texture' objects>"
        'getEffectiveMinfilter': None, # (!) real value is "<method 'getEffectiveMinfilter' of 'panda3d.core.Texture' objects>"
        'getEffectiveQualityLevel': None, # (!) real value is "<method 'getEffectiveQualityLevel' of 'panda3d.core.Texture' objects>"
        'getExpectedMipmapNumPages': None, # (!) real value is "<method 'getExpectedMipmapNumPages' of 'panda3d.core.Texture' objects>"
        'getExpectedMipmapXSize': None, # (!) real value is "<method 'getExpectedMipmapXSize' of 'panda3d.core.Texture' objects>"
        'getExpectedMipmapYSize': None, # (!) real value is "<method 'getExpectedMipmapYSize' of 'panda3d.core.Texture' objects>"
        'getExpectedMipmapZSize': None, # (!) real value is "<method 'getExpectedMipmapZSize' of 'panda3d.core.Texture' objects>"
        'getExpectedNumMipmapLevels': None, # (!) real value is "<method 'getExpectedNumMipmapLevels' of 'panda3d.core.Texture' objects>"
        'getExpectedRamImageSize': None, # (!) real value is "<method 'getExpectedRamImageSize' of 'panda3d.core.Texture' objects>"
        'getExpectedRamMipmapImageSize': None, # (!) real value is "<method 'getExpectedRamMipmapImageSize' of 'panda3d.core.Texture' objects>"
        'getExpectedRamMipmapPageSize': None, # (!) real value is "<method 'getExpectedRamMipmapPageSize' of 'panda3d.core.Texture' objects>"
        'getExpectedRamMipmapViewSize': None, # (!) real value is "<method 'getExpectedRamMipmapViewSize' of 'panda3d.core.Texture' objects>"
        'getExpectedRamPageSize': None, # (!) real value is "<method 'getExpectedRamPageSize' of 'panda3d.core.Texture' objects>"
        'getFilename': None, # (!) real value is "<method 'getFilename' of 'panda3d.core.Texture' objects>"
        'getFormat': None, # (!) real value is "<method 'getFormat' of 'panda3d.core.Texture' objects>"
        'getFullpath': None, # (!) real value is "<method 'getFullpath' of 'panda3d.core.Texture' objects>"
        'getImageModified': None, # (!) real value is "<method 'getImageModified' of 'panda3d.core.Texture' objects>"
        'getKeepRamImage': None, # (!) real value is "<method 'getKeepRamImage' of 'panda3d.core.Texture' objects>"
        'getLoadedFromImage': None, # (!) real value is "<method 'getLoadedFromImage' of 'panda3d.core.Texture' objects>"
        'getLoadedFromTxo': None, # (!) real value is "<method 'getLoadedFromTxo' of 'panda3d.core.Texture' objects>"
        'getMagfilter': None, # (!) real value is "<method 'getMagfilter' of 'panda3d.core.Texture' objects>"
        'getMatchFramebufferFormat': None, # (!) real value is "<method 'getMatchFramebufferFormat' of 'panda3d.core.Texture' objects>"
        'getMinfilter': None, # (!) real value is "<method 'getMinfilter' of 'panda3d.core.Texture' objects>"
        'getNumComponents': None, # (!) real value is "<method 'getNumComponents' of 'panda3d.core.Texture' objects>"
        'getNumLoadableRamMipmapImages': None, # (!) real value is "<method 'getNumLoadableRamMipmapImages' of 'panda3d.core.Texture' objects>"
        'getNumPages': None, # (!) real value is "<method 'getNumPages' of 'panda3d.core.Texture' objects>"
        'getNumRamMipmapImages': None, # (!) real value is "<method 'getNumRamMipmapImages' of 'panda3d.core.Texture' objects>"
        'getNumViews': None, # (!) real value is "<method 'getNumViews' of 'panda3d.core.Texture' objects>"
        'getOrigFileXSize': None, # (!) real value is "<method 'getOrigFileXSize' of 'panda3d.core.Texture' objects>"
        'getOrigFileYSize': None, # (!) real value is "<method 'getOrigFileYSize' of 'panda3d.core.Texture' objects>"
        'getOrigFileZSize': None, # (!) real value is "<method 'getOrigFileZSize' of 'panda3d.core.Texture' objects>"
        'getPadXSize': None, # (!) real value is "<method 'getPadXSize' of 'panda3d.core.Texture' objects>"
        'getPadYSize': None, # (!) real value is "<method 'getPadYSize' of 'panda3d.core.Texture' objects>"
        'getPadZSize': None, # (!) real value is "<method 'getPadZSize' of 'panda3d.core.Texture' objects>"
        'getPostLoadStoreCache': None, # (!) real value is "<method 'getPostLoadStoreCache' of 'panda3d.core.Texture' objects>"
        'getPropertiesModified': None, # (!) real value is "<method 'getPropertiesModified' of 'panda3d.core.Texture' objects>"
        'getQualityLevel': None, # (!) real value is "<method 'getQualityLevel' of 'panda3d.core.Texture' objects>"
        'getRamImage': None, # (!) real value is "<method 'getRamImage' of 'panda3d.core.Texture' objects>"
        'getRamImageAs': None, # (!) real value is "<method 'getRamImageAs' of 'panda3d.core.Texture' objects>"
        'getRamImageCompression': None, # (!) real value is "<method 'getRamImageCompression' of 'panda3d.core.Texture' objects>"
        'getRamImageSize': None, # (!) real value is "<method 'getRamImageSize' of 'panda3d.core.Texture' objects>"
        'getRamMipmapImage': None, # (!) real value is "<method 'getRamMipmapImage' of 'panda3d.core.Texture' objects>"
        'getRamMipmapImageSize': None, # (!) real value is "<method 'getRamMipmapImageSize' of 'panda3d.core.Texture' objects>"
        'getRamMipmapPageSize': None, # (!) real value is "<method 'getRamMipmapPageSize' of 'panda3d.core.Texture' objects>"
        'getRamMipmapViewSize': None, # (!) real value is "<method 'getRamMipmapViewSize' of 'panda3d.core.Texture' objects>"
        'getRamPageSize': None, # (!) real value is "<method 'getRamPageSize' of 'panda3d.core.Texture' objects>"
        'getRamViewSize': None, # (!) real value is "<method 'getRamViewSize' of 'panda3d.core.Texture' objects>"
        'getRenderToTexture': None, # (!) real value is "<method 'getRenderToTexture' of 'panda3d.core.Texture' objects>"
        'getResident': None, # (!) real value is "<method 'getResident' of 'panda3d.core.Texture' objects>"
        'getSimpleImageModified': None, # (!) real value is "<method 'getSimpleImageModified' of 'panda3d.core.Texture' objects>"
        'getSimpleRamImage': None, # (!) real value is "<method 'getSimpleRamImage' of 'panda3d.core.Texture' objects>"
        'getSimpleRamImageSize': None, # (!) real value is "<method 'getSimpleRamImageSize' of 'panda3d.core.Texture' objects>"
        'getSimpleXSize': None, # (!) real value is "<method 'getSimpleXSize' of 'panda3d.core.Texture' objects>"
        'getSimpleYSize': None, # (!) real value is "<method 'getSimpleYSize' of 'panda3d.core.Texture' objects>"
        'getTexScale': None, # (!) real value is "<method 'getTexScale' of 'panda3d.core.Texture' objects>"
        'getTextureType': None, # (!) real value is "<method 'getTextureType' of 'panda3d.core.Texture' objects>"
        'getTexturesPower2': None, # (!) real value is '<staticmethod(<built-in method getTexturesPower2 of type object at 0x00007FFCFE2FED40>)>'
        'getUncompressedRamImage': None, # (!) real value is "<method 'getUncompressedRamImage' of 'panda3d.core.Texture' objects>"
        'getUsageHint': None, # (!) real value is "<method 'getUsageHint' of 'panda3d.core.Texture' objects>"
        'getWrapU': None, # (!) real value is "<method 'getWrapU' of 'panda3d.core.Texture' objects>"
        'getWrapV': None, # (!) real value is "<method 'getWrapV' of 'panda3d.core.Texture' objects>"
        'getWrapW': None, # (!) real value is "<method 'getWrapW' of 'panda3d.core.Texture' objects>"
        'getXSize': None, # (!) real value is "<method 'getXSize' of 'panda3d.core.Texture' objects>"
        'getYSize': None, # (!) real value is "<method 'getYSize' of 'panda3d.core.Texture' objects>"
        'getZSize': None, # (!) real value is "<method 'getZSize' of 'panda3d.core.Texture' objects>"
        'get_active': None, # (!) real value is "<method 'get_active' of 'panda3d.core.Texture' objects>"
        'get_alpha_filename': None, # (!) real value is "<method 'get_alpha_filename' of 'panda3d.core.Texture' objects>"
        'get_alpha_fullpath': None, # (!) real value is "<method 'get_alpha_fullpath' of 'panda3d.core.Texture' objects>"
        'get_anisotropic_degree': None, # (!) real value is "<method 'get_anisotropic_degree' of 'panda3d.core.Texture' objects>"
        'get_auto_texture_scale': None, # (!) real value is "<method 'get_auto_texture_scale' of 'panda3d.core.Texture' objects>"
        'get_aux_data': None, # (!) real value is "<method 'get_aux_data' of 'panda3d.core.Texture' objects>"
        'get_border_color': None, # (!) real value is "<method 'get_border_color' of 'panda3d.core.Texture' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2FED40>)>'
        'get_clear_color': None, # (!) real value is "<method 'get_clear_color' of 'panda3d.core.Texture' objects>"
        'get_clear_data': None, # (!) real value is "<method 'get_clear_data' of 'panda3d.core.Texture' objects>"
        'get_component_type': None, # (!) real value is "<method 'get_component_type' of 'panda3d.core.Texture' objects>"
        'get_component_width': None, # (!) real value is "<method 'get_component_width' of 'panda3d.core.Texture' objects>"
        'get_compression': None, # (!) real value is "<method 'get_compression' of 'panda3d.core.Texture' objects>"
        'get_data_size_bytes': None, # (!) real value is "<method 'get_data_size_bytes' of 'panda3d.core.Texture' objects>"
        'get_default_sampler': None, # (!) real value is "<method 'get_default_sampler' of 'panda3d.core.Texture' objects>"
        'get_effective_anisotropic_degree': None, # (!) real value is "<method 'get_effective_anisotropic_degree' of 'panda3d.core.Texture' objects>"
        'get_effective_magfilter': None, # (!) real value is "<method 'get_effective_magfilter' of 'panda3d.core.Texture' objects>"
        'get_effective_minfilter': None, # (!) real value is "<method 'get_effective_minfilter' of 'panda3d.core.Texture' objects>"
        'get_effective_quality_level': None, # (!) real value is "<method 'get_effective_quality_level' of 'panda3d.core.Texture' objects>"
        'get_expected_mipmap_num_pages': None, # (!) real value is "<method 'get_expected_mipmap_num_pages' of 'panda3d.core.Texture' objects>"
        'get_expected_mipmap_x_size': None, # (!) real value is "<method 'get_expected_mipmap_x_size' of 'panda3d.core.Texture' objects>"
        'get_expected_mipmap_y_size': None, # (!) real value is "<method 'get_expected_mipmap_y_size' of 'panda3d.core.Texture' objects>"
        'get_expected_mipmap_z_size': None, # (!) real value is "<method 'get_expected_mipmap_z_size' of 'panda3d.core.Texture' objects>"
        'get_expected_num_mipmap_levels': None, # (!) real value is "<method 'get_expected_num_mipmap_levels' of 'panda3d.core.Texture' objects>"
        'get_expected_ram_image_size': None, # (!) real value is "<method 'get_expected_ram_image_size' of 'panda3d.core.Texture' objects>"
        'get_expected_ram_mipmap_image_size': None, # (!) real value is "<method 'get_expected_ram_mipmap_image_size' of 'panda3d.core.Texture' objects>"
        'get_expected_ram_mipmap_page_size': None, # (!) real value is "<method 'get_expected_ram_mipmap_page_size' of 'panda3d.core.Texture' objects>"
        'get_expected_ram_mipmap_view_size': None, # (!) real value is "<method 'get_expected_ram_mipmap_view_size' of 'panda3d.core.Texture' objects>"
        'get_expected_ram_page_size': None, # (!) real value is "<method 'get_expected_ram_page_size' of 'panda3d.core.Texture' objects>"
        'get_filename': None, # (!) real value is "<method 'get_filename' of 'panda3d.core.Texture' objects>"
        'get_format': None, # (!) real value is "<method 'get_format' of 'panda3d.core.Texture' objects>"
        'get_fullpath': None, # (!) real value is "<method 'get_fullpath' of 'panda3d.core.Texture' objects>"
        'get_image_modified': None, # (!) real value is "<method 'get_image_modified' of 'panda3d.core.Texture' objects>"
        'get_keep_ram_image': None, # (!) real value is "<method 'get_keep_ram_image' of 'panda3d.core.Texture' objects>"
        'get_loaded_from_image': None, # (!) real value is "<method 'get_loaded_from_image' of 'panda3d.core.Texture' objects>"
        'get_loaded_from_txo': None, # (!) real value is "<method 'get_loaded_from_txo' of 'panda3d.core.Texture' objects>"
        'get_magfilter': None, # (!) real value is "<method 'get_magfilter' of 'panda3d.core.Texture' objects>"
        'get_match_framebuffer_format': None, # (!) real value is "<method 'get_match_framebuffer_format' of 'panda3d.core.Texture' objects>"
        'get_minfilter': None, # (!) real value is "<method 'get_minfilter' of 'panda3d.core.Texture' objects>"
        'get_num_components': None, # (!) real value is "<method 'get_num_components' of 'panda3d.core.Texture' objects>"
        'get_num_loadable_ram_mipmap_images': None, # (!) real value is "<method 'get_num_loadable_ram_mipmap_images' of 'panda3d.core.Texture' objects>"
        'get_num_pages': None, # (!) real value is "<method 'get_num_pages' of 'panda3d.core.Texture' objects>"
        'get_num_ram_mipmap_images': None, # (!) real value is "<method 'get_num_ram_mipmap_images' of 'panda3d.core.Texture' objects>"
        'get_num_views': None, # (!) real value is "<method 'get_num_views' of 'panda3d.core.Texture' objects>"
        'get_orig_file_x_size': None, # (!) real value is "<method 'get_orig_file_x_size' of 'panda3d.core.Texture' objects>"
        'get_orig_file_y_size': None, # (!) real value is "<method 'get_orig_file_y_size' of 'panda3d.core.Texture' objects>"
        'get_orig_file_z_size': None, # (!) real value is "<method 'get_orig_file_z_size' of 'panda3d.core.Texture' objects>"
        'get_pad_x_size': None, # (!) real value is "<method 'get_pad_x_size' of 'panda3d.core.Texture' objects>"
        'get_pad_y_size': None, # (!) real value is "<method 'get_pad_y_size' of 'panda3d.core.Texture' objects>"
        'get_pad_z_size': None, # (!) real value is "<method 'get_pad_z_size' of 'panda3d.core.Texture' objects>"
        'get_post_load_store_cache': None, # (!) real value is "<method 'get_post_load_store_cache' of 'panda3d.core.Texture' objects>"
        'get_properties_modified': None, # (!) real value is "<method 'get_properties_modified' of 'panda3d.core.Texture' objects>"
        'get_quality_level': None, # (!) real value is "<method 'get_quality_level' of 'panda3d.core.Texture' objects>"
        'get_ram_image': None, # (!) real value is "<method 'get_ram_image' of 'panda3d.core.Texture' objects>"
        'get_ram_image_as': None, # (!) real value is "<method 'get_ram_image_as' of 'panda3d.core.Texture' objects>"
        'get_ram_image_compression': None, # (!) real value is "<method 'get_ram_image_compression' of 'panda3d.core.Texture' objects>"
        'get_ram_image_size': None, # (!) real value is "<method 'get_ram_image_size' of 'panda3d.core.Texture' objects>"
        'get_ram_mipmap_image': None, # (!) real value is "<method 'get_ram_mipmap_image' of 'panda3d.core.Texture' objects>"
        'get_ram_mipmap_image_size': None, # (!) real value is "<method 'get_ram_mipmap_image_size' of 'panda3d.core.Texture' objects>"
        'get_ram_mipmap_page_size': None, # (!) real value is "<method 'get_ram_mipmap_page_size' of 'panda3d.core.Texture' objects>"
        'get_ram_mipmap_view_size': None, # (!) real value is "<method 'get_ram_mipmap_view_size' of 'panda3d.core.Texture' objects>"
        'get_ram_page_size': None, # (!) real value is "<method 'get_ram_page_size' of 'panda3d.core.Texture' objects>"
        'get_ram_view_size': None, # (!) real value is "<method 'get_ram_view_size' of 'panda3d.core.Texture' objects>"
        'get_render_to_texture': None, # (!) real value is "<method 'get_render_to_texture' of 'panda3d.core.Texture' objects>"
        'get_resident': None, # (!) real value is "<method 'get_resident' of 'panda3d.core.Texture' objects>"
        'get_simple_image_modified': None, # (!) real value is "<method 'get_simple_image_modified' of 'panda3d.core.Texture' objects>"
        'get_simple_ram_image': None, # (!) real value is "<method 'get_simple_ram_image' of 'panda3d.core.Texture' objects>"
        'get_simple_ram_image_size': None, # (!) real value is "<method 'get_simple_ram_image_size' of 'panda3d.core.Texture' objects>"
        'get_simple_x_size': None, # (!) real value is "<method 'get_simple_x_size' of 'panda3d.core.Texture' objects>"
        'get_simple_y_size': None, # (!) real value is "<method 'get_simple_y_size' of 'panda3d.core.Texture' objects>"
        'get_tex_scale': None, # (!) real value is "<method 'get_tex_scale' of 'panda3d.core.Texture' objects>"
        'get_texture_type': None, # (!) real value is "<method 'get_texture_type' of 'panda3d.core.Texture' objects>"
        'get_textures_power_2': None, # (!) real value is '<staticmethod(<built-in method get_textures_power_2 of type object at 0x00007FFCFE2FED40>)>'
        'get_uncompressed_ram_image': None, # (!) real value is "<method 'get_uncompressed_ram_image' of 'panda3d.core.Texture' objects>"
        'get_usage_hint': None, # (!) real value is "<method 'get_usage_hint' of 'panda3d.core.Texture' objects>"
        'get_wrap_u': None, # (!) real value is "<method 'get_wrap_u' of 'panda3d.core.Texture' objects>"
        'get_wrap_v': None, # (!) real value is "<method 'get_wrap_v' of 'panda3d.core.Texture' objects>"
        'get_wrap_w': None, # (!) real value is "<method 'get_wrap_w' of 'panda3d.core.Texture' objects>"
        'get_x_size': None, # (!) real value is "<method 'get_x_size' of 'panda3d.core.Texture' objects>"
        'get_y_size': None, # (!) real value is "<method 'get_y_size' of 'panda3d.core.Texture' objects>"
        'get_z_size': None, # (!) real value is "<method 'get_z_size' of 'panda3d.core.Texture' objects>"
        'hasAllRamMipmapImages': None, # (!) real value is "<method 'hasAllRamMipmapImages' of 'panda3d.core.Texture' objects>"
        'hasAlphaFilename': None, # (!) real value is "<method 'hasAlphaFilename' of 'panda3d.core.Texture' objects>"
        'hasAlphaFullpath': None, # (!) real value is "<method 'hasAlphaFullpath' of 'panda3d.core.Texture' objects>"
        'hasAutoTextureScale': None, # (!) real value is "<method 'hasAutoTextureScale' of 'panda3d.core.Texture' objects>"
        'hasClearColor': None, # (!) real value is "<method 'hasClearColor' of 'panda3d.core.Texture' objects>"
        'hasCompression': None, # (!) real value is "<method 'hasCompression' of 'panda3d.core.Texture' objects>"
        'hasFilename': None, # (!) real value is "<method 'hasFilename' of 'panda3d.core.Texture' objects>"
        'hasFullpath': None, # (!) real value is "<method 'hasFullpath' of 'panda3d.core.Texture' objects>"
        'hasRamImage': None, # (!) real value is "<method 'hasRamImage' of 'panda3d.core.Texture' objects>"
        'hasRamMipmapImage': None, # (!) real value is "<method 'hasRamMipmapImage' of 'panda3d.core.Texture' objects>"
        'hasSimpleRamImage': None, # (!) real value is "<method 'hasSimpleRamImage' of 'panda3d.core.Texture' objects>"
        'hasTexturesPower2': None, # (!) real value is '<staticmethod(<built-in method hasTexturesPower2 of type object at 0x00007FFCFE2FED40>)>'
        'hasUncompressedRamImage': None, # (!) real value is "<method 'hasUncompressedRamImage' of 'panda3d.core.Texture' objects>"
        'has_all_ram_mipmap_images': None, # (!) real value is "<method 'has_all_ram_mipmap_images' of 'panda3d.core.Texture' objects>"
        'has_alpha_filename': None, # (!) real value is "<method 'has_alpha_filename' of 'panda3d.core.Texture' objects>"
        'has_alpha_fullpath': None, # (!) real value is "<method 'has_alpha_fullpath' of 'panda3d.core.Texture' objects>"
        'has_auto_texture_scale': None, # (!) real value is "<method 'has_auto_texture_scale' of 'panda3d.core.Texture' objects>"
        'has_clear_color': None, # (!) real value is "<method 'has_clear_color' of 'panda3d.core.Texture' objects>"
        'has_compression': None, # (!) real value is "<method 'has_compression' of 'panda3d.core.Texture' objects>"
        'has_filename': None, # (!) real value is "<method 'has_filename' of 'panda3d.core.Texture' objects>"
        'has_fullpath': None, # (!) real value is "<method 'has_fullpath' of 'panda3d.core.Texture' objects>"
        'has_ram_image': None, # (!) real value is "<method 'has_ram_image' of 'panda3d.core.Texture' objects>"
        'has_ram_mipmap_image': None, # (!) real value is "<method 'has_ram_mipmap_image' of 'panda3d.core.Texture' objects>"
        'has_simple_ram_image': None, # (!) real value is "<method 'has_simple_ram_image' of 'panda3d.core.Texture' objects>"
        'has_textures_power_2': None, # (!) real value is '<staticmethod(<built-in method has_textures_power_2 of type object at 0x00007FFCFE2FED40>)>'
        'has_uncompressed_ram_image': None, # (!) real value is "<method 'has_uncompressed_ram_image' of 'panda3d.core.Texture' objects>"
        'image_modified': None, # (!) real value is "<attribute 'image_modified' of 'panda3d.core.Texture' objects>"
        'isCacheable': None, # (!) real value is "<method 'isCacheable' of 'panda3d.core.Texture' objects>"
        'isPrepared': None, # (!) real value is "<method 'isPrepared' of 'panda3d.core.Texture' objects>"
        'is_cacheable': None, # (!) real value is "<method 'is_cacheable' of 'panda3d.core.Texture' objects>"
        'is_prepared': None, # (!) real value is "<method 'is_prepared' of 'panda3d.core.Texture' objects>"
        'keep_ram_image': None, # (!) real value is "<attribute 'keep_ram_image' of 'panda3d.core.Texture' objects>"
        'load': None, # (!) real value is "<method 'load' of 'panda3d.core.Texture' objects>"
        'loadRelated': None, # (!) real value is "<method 'loadRelated' of 'panda3d.core.Texture' objects>"
        'loadSubImage': None, # (!) real value is "<method 'loadSubImage' of 'panda3d.core.Texture' objects>"
        'load_related': None, # (!) real value is "<method 'load_related' of 'panda3d.core.Texture' objects>"
        'load_sub_image': None, # (!) real value is "<method 'load_sub_image' of 'panda3d.core.Texture' objects>"
        'loaded_from_image': None, # (!) real value is "<attribute 'loaded_from_image' of 'panda3d.core.Texture' objects>"
        'loaded_from_txo': None, # (!) real value is "<attribute 'loaded_from_txo' of 'panda3d.core.Texture' objects>"
        'magfilter': None, # (!) real value is "<attribute 'magfilter' of 'panda3d.core.Texture' objects>"
        'makeCopy': None, # (!) real value is "<method 'makeCopy' of 'panda3d.core.Texture' objects>"
        'makeFromTxo': None, # (!) real value is '<staticmethod(<built-in method makeFromTxo of type object at 0x00007FFCFE2FED40>)>'
        'makeRamImage': None, # (!) real value is "<method 'makeRamImage' of 'panda3d.core.Texture' objects>"
        'makeRamMipmapImage': None, # (!) real value is "<method 'makeRamMipmapImage' of 'panda3d.core.Texture' objects>"
        'make_copy': None, # (!) real value is "<method 'make_copy' of 'panda3d.core.Texture' objects>"
        'make_from_txo': None, # (!) real value is '<staticmethod(<built-in method make_from_txo of type object at 0x00007FFCFE2FED40>)>'
        'make_ram_image': None, # (!) real value is "<method 'make_ram_image' of 'panda3d.core.Texture' objects>"
        'make_ram_mipmap_image': None, # (!) real value is "<method 'make_ram_mipmap_image' of 'panda3d.core.Texture' objects>"
        'match_framebuffer_format': None, # (!) real value is "<attribute 'match_framebuffer_format' of 'panda3d.core.Texture' objects>"
        'mightHaveRamImage': None, # (!) real value is "<method 'mightHaveRamImage' of 'panda3d.core.Texture' objects>"
        'might_have_ram_image': None, # (!) real value is "<method 'might_have_ram_image' of 'panda3d.core.Texture' objects>"
        'minfilter': None, # (!) real value is "<attribute 'minfilter' of 'panda3d.core.Texture' objects>"
        'modifyRamImage': None, # (!) real value is "<method 'modifyRamImage' of 'panda3d.core.Texture' objects>"
        'modifyRamMipmapImage': None, # (!) real value is "<method 'modifyRamMipmapImage' of 'panda3d.core.Texture' objects>"
        'modifySimpleRamImage': None, # (!) real value is "<method 'modifySimpleRamImage' of 'panda3d.core.Texture' objects>"
        'modify_ram_image': None, # (!) real value is "<method 'modify_ram_image' of 'panda3d.core.Texture' objects>"
        'modify_ram_mipmap_image': None, # (!) real value is "<method 'modify_ram_mipmap_image' of 'panda3d.core.Texture' objects>"
        'modify_simple_ram_image': None, # (!) real value is "<method 'modify_simple_ram_image' of 'panda3d.core.Texture' objects>"
        'newSimpleRamImage': None, # (!) real value is "<method 'newSimpleRamImage' of 'panda3d.core.Texture' objects>"
        'new_simple_ram_image': None, # (!) real value is "<method 'new_simple_ram_image' of 'panda3d.core.Texture' objects>"
        'num_components': None, # (!) real value is "<attribute 'num_components' of 'panda3d.core.Texture' objects>"
        'num_loadable_ram_mipmap_images': None, # (!) real value is "<attribute 'num_loadable_ram_mipmap_images' of 'panda3d.core.Texture' objects>"
        'num_pages': None, # (!) real value is "<attribute 'num_pages' of 'panda3d.core.Texture' objects>"
        'num_ram_mipmap_images': None, # (!) real value is "<attribute 'num_ram_mipmap_images' of 'panda3d.core.Texture' objects>"
        'num_views': None, # (!) real value is "<attribute 'num_views' of 'panda3d.core.Texture' objects>"
        'orig_file_x_size': None, # (!) real value is "<attribute 'orig_file_x_size' of 'panda3d.core.Texture' objects>"
        'orig_file_y_size': None, # (!) real value is "<attribute 'orig_file_y_size' of 'panda3d.core.Texture' objects>"
        'orig_file_z_size': None, # (!) real value is "<attribute 'orig_file_z_size' of 'panda3d.core.Texture' objects>"
        'peek': None, # (!) real value is "<method 'peek' of 'panda3d.core.Texture' objects>"
        'post_load_store_cache': None, # (!) real value is "<attribute 'post_load_store_cache' of 'panda3d.core.Texture' objects>"
        'prepare': None, # (!) real value is "<method 'prepare' of 'panda3d.core.Texture' objects>"
        'prepareNow': None, # (!) real value is "<method 'prepareNow' of 'panda3d.core.Texture' objects>"
        'prepare_now': None, # (!) real value is "<method 'prepare_now' of 'panda3d.core.Texture' objects>"
        'properties_modified': None, # (!) real value is "<attribute 'properties_modified' of 'panda3d.core.Texture' objects>"
        'quality_level': None, # (!) real value is "<attribute 'quality_level' of 'panda3d.core.Texture' objects>"
        'ram_image_compression': None, # (!) real value is "<attribute 'ram_image_compression' of 'panda3d.core.Texture' objects>"
        'ram_image_size': None, # (!) real value is "<attribute 'ram_image_size' of 'panda3d.core.Texture' objects>"
        'ram_page_size': None, # (!) real value is "<attribute 'ram_page_size' of 'panda3d.core.Texture' objects>"
        'ram_view_size': None, # (!) real value is "<attribute 'ram_view_size' of 'panda3d.core.Texture' objects>"
        'read': None, # (!) real value is "<method 'read' of 'panda3d.core.Texture' objects>"
        'readDds': None, # (!) real value is "<method 'readDds' of 'panda3d.core.Texture' objects>"
        'readKtx': None, # (!) real value is "<method 'readKtx' of 'panda3d.core.Texture' objects>"
        'readTxo': None, # (!) real value is "<method 'readTxo' of 'panda3d.core.Texture' objects>"
        'read_dds': None, # (!) real value is "<method 'read_dds' of 'panda3d.core.Texture' objects>"
        'read_ktx': None, # (!) real value is "<method 'read_ktx' of 'panda3d.core.Texture' objects>"
        'read_txo': None, # (!) real value is "<method 'read_txo' of 'panda3d.core.Texture' objects>"
        'release': None, # (!) real value is "<method 'release' of 'panda3d.core.Texture' objects>"
        'releaseAll': None, # (!) real value is "<method 'releaseAll' of 'panda3d.core.Texture' objects>"
        'release_all': None, # (!) real value is "<method 'release_all' of 'panda3d.core.Texture' objects>"
        'reload': None, # (!) real value is "<method 'reload' of 'panda3d.core.Texture' objects>"
        'render_to_texture': None, # (!) real value is "<attribute 'render_to_texture' of 'panda3d.core.Texture' objects>"
        'rescaleTexture': None, # (!) real value is "<method 'rescaleTexture' of 'panda3d.core.Texture' objects>"
        'rescale_texture': None, # (!) real value is "<method 'rescale_texture' of 'panda3d.core.Texture' objects>"
        'setAlphaFilename': None, # (!) real value is "<method 'setAlphaFilename' of 'panda3d.core.Texture' objects>"
        'setAlphaFullpath': None, # (!) real value is "<method 'setAlphaFullpath' of 'panda3d.core.Texture' objects>"
        'setAnisotropicDegree': None, # (!) real value is "<method 'setAnisotropicDegree' of 'panda3d.core.Texture' objects>"
        'setAutoTextureScale': None, # (!) real value is "<method 'setAutoTextureScale' of 'panda3d.core.Texture' objects>"
        'setAuxData': None, # (!) real value is "<method 'setAuxData' of 'panda3d.core.Texture' objects>"
        'setBorderColor': None, # (!) real value is "<method 'setBorderColor' of 'panda3d.core.Texture' objects>"
        'setClearColor': None, # (!) real value is "<method 'setClearColor' of 'panda3d.core.Texture' objects>"
        'setComponentType': None, # (!) real value is "<method 'setComponentType' of 'panda3d.core.Texture' objects>"
        'setCompression': None, # (!) real value is "<method 'setCompression' of 'panda3d.core.Texture' objects>"
        'setDefaultSampler': None, # (!) real value is "<method 'setDefaultSampler' of 'panda3d.core.Texture' objects>"
        'setFilename': None, # (!) real value is "<method 'setFilename' of 'panda3d.core.Texture' objects>"
        'setFormat': None, # (!) real value is "<method 'setFormat' of 'panda3d.core.Texture' objects>"
        'setFullpath': None, # (!) real value is "<method 'setFullpath' of 'panda3d.core.Texture' objects>"
        'setKeepRamImage': None, # (!) real value is "<method 'setKeepRamImage' of 'panda3d.core.Texture' objects>"
        'setLoadedFromImage': None, # (!) real value is "<method 'setLoadedFromImage' of 'panda3d.core.Texture' objects>"
        'setLoadedFromTxo': None, # (!) real value is "<method 'setLoadedFromTxo' of 'panda3d.core.Texture' objects>"
        'setMagfilter': None, # (!) real value is "<method 'setMagfilter' of 'panda3d.core.Texture' objects>"
        'setMatchFramebufferFormat': None, # (!) real value is "<method 'setMatchFramebufferFormat' of 'panda3d.core.Texture' objects>"
        'setMinfilter': None, # (!) real value is "<method 'setMinfilter' of 'panda3d.core.Texture' objects>"
        'setNumViews': None, # (!) real value is "<method 'setNumViews' of 'panda3d.core.Texture' objects>"
        'setOrigFileSize': None, # (!) real value is "<method 'setOrigFileSize' of 'panda3d.core.Texture' objects>"
        'setPadSize': None, # (!) real value is "<method 'setPadSize' of 'panda3d.core.Texture' objects>"
        'setPostLoadStoreCache': None, # (!) real value is "<method 'setPostLoadStoreCache' of 'panda3d.core.Texture' objects>"
        'setQualityLevel': None, # (!) real value is "<method 'setQualityLevel' of 'panda3d.core.Texture' objects>"
        'setRamImage': None, # (!) real value is "<method 'setRamImage' of 'panda3d.core.Texture' objects>"
        'setRamImageAs': None, # (!) real value is "<method 'setRamImageAs' of 'panda3d.core.Texture' objects>"
        'setRamMipmapImage': None, # (!) real value is "<method 'setRamMipmapImage' of 'panda3d.core.Texture' objects>"
        'setRamMipmapPointerFromInt': None, # (!) real value is "<method 'setRamMipmapPointerFromInt' of 'panda3d.core.Texture' objects>"
        'setRenderToTexture': None, # (!) real value is "<method 'setRenderToTexture' of 'panda3d.core.Texture' objects>"
        'setSimpleRamImage': None, # (!) real value is "<method 'setSimpleRamImage' of 'panda3d.core.Texture' objects>"
        'setSizePadded': None, # (!) real value is "<method 'setSizePadded' of 'panda3d.core.Texture' objects>"
        'setTexturesPower2': None, # (!) real value is '<staticmethod(<built-in method setTexturesPower2 of type object at 0x00007FFCFE2FED40>)>'
        'setWrapU': None, # (!) real value is "<method 'setWrapU' of 'panda3d.core.Texture' objects>"
        'setWrapV': None, # (!) real value is "<method 'setWrapV' of 'panda3d.core.Texture' objects>"
        'setWrapW': None, # (!) real value is "<method 'setWrapW' of 'panda3d.core.Texture' objects>"
        'setXSize': None, # (!) real value is "<method 'setXSize' of 'panda3d.core.Texture' objects>"
        'setYSize': None, # (!) real value is "<method 'setYSize' of 'panda3d.core.Texture' objects>"
        'setZSize': None, # (!) real value is "<method 'setZSize' of 'panda3d.core.Texture' objects>"
        'set_alpha_filename': None, # (!) real value is "<method 'set_alpha_filename' of 'panda3d.core.Texture' objects>"
        'set_alpha_fullpath': None, # (!) real value is "<method 'set_alpha_fullpath' of 'panda3d.core.Texture' objects>"
        'set_anisotropic_degree': None, # (!) real value is "<method 'set_anisotropic_degree' of 'panda3d.core.Texture' objects>"
        'set_auto_texture_scale': None, # (!) real value is "<method 'set_auto_texture_scale' of 'panda3d.core.Texture' objects>"
        'set_aux_data': None, # (!) real value is "<method 'set_aux_data' of 'panda3d.core.Texture' objects>"
        'set_border_color': None, # (!) real value is "<method 'set_border_color' of 'panda3d.core.Texture' objects>"
        'set_clear_color': None, # (!) real value is "<method 'set_clear_color' of 'panda3d.core.Texture' objects>"
        'set_component_type': None, # (!) real value is "<method 'set_component_type' of 'panda3d.core.Texture' objects>"
        'set_compression': None, # (!) real value is "<method 'set_compression' of 'panda3d.core.Texture' objects>"
        'set_default_sampler': None, # (!) real value is "<method 'set_default_sampler' of 'panda3d.core.Texture' objects>"
        'set_filename': None, # (!) real value is "<method 'set_filename' of 'panda3d.core.Texture' objects>"
        'set_format': None, # (!) real value is "<method 'set_format' of 'panda3d.core.Texture' objects>"
        'set_fullpath': None, # (!) real value is "<method 'set_fullpath' of 'panda3d.core.Texture' objects>"
        'set_keep_ram_image': None, # (!) real value is "<method 'set_keep_ram_image' of 'panda3d.core.Texture' objects>"
        'set_loaded_from_image': None, # (!) real value is "<method 'set_loaded_from_image' of 'panda3d.core.Texture' objects>"
        'set_loaded_from_txo': None, # (!) real value is "<method 'set_loaded_from_txo' of 'panda3d.core.Texture' objects>"
        'set_magfilter': None, # (!) real value is "<method 'set_magfilter' of 'panda3d.core.Texture' objects>"
        'set_match_framebuffer_format': None, # (!) real value is "<method 'set_match_framebuffer_format' of 'panda3d.core.Texture' objects>"
        'set_minfilter': None, # (!) real value is "<method 'set_minfilter' of 'panda3d.core.Texture' objects>"
        'set_num_views': None, # (!) real value is "<method 'set_num_views' of 'panda3d.core.Texture' objects>"
        'set_orig_file_size': None, # (!) real value is "<method 'set_orig_file_size' of 'panda3d.core.Texture' objects>"
        'set_pad_size': None, # (!) real value is "<method 'set_pad_size' of 'panda3d.core.Texture' objects>"
        'set_post_load_store_cache': None, # (!) real value is "<method 'set_post_load_store_cache' of 'panda3d.core.Texture' objects>"
        'set_quality_level': None, # (!) real value is "<method 'set_quality_level' of 'panda3d.core.Texture' objects>"
        'set_ram_image': None, # (!) real value is "<method 'set_ram_image' of 'panda3d.core.Texture' objects>"
        'set_ram_image_as': None, # (!) real value is "<method 'set_ram_image_as' of 'panda3d.core.Texture' objects>"
        'set_ram_mipmap_image': None, # (!) real value is "<method 'set_ram_mipmap_image' of 'panda3d.core.Texture' objects>"
        'set_ram_mipmap_pointer_from_int': None, # (!) real value is "<method 'set_ram_mipmap_pointer_from_int' of 'panda3d.core.Texture' objects>"
        'set_render_to_texture': None, # (!) real value is "<method 'set_render_to_texture' of 'panda3d.core.Texture' objects>"
        'set_simple_ram_image': None, # (!) real value is "<method 'set_simple_ram_image' of 'panda3d.core.Texture' objects>"
        'set_size_padded': None, # (!) real value is "<method 'set_size_padded' of 'panda3d.core.Texture' objects>"
        'set_textures_power_2': None, # (!) real value is '<staticmethod(<built-in method set_textures_power_2 of type object at 0x00007FFCFE2FED40>)>'
        'set_wrap_u': None, # (!) real value is "<method 'set_wrap_u' of 'panda3d.core.Texture' objects>"
        'set_wrap_v': None, # (!) real value is "<method 'set_wrap_v' of 'panda3d.core.Texture' objects>"
        'set_wrap_w': None, # (!) real value is "<method 'set_wrap_w' of 'panda3d.core.Texture' objects>"
        'set_x_size': None, # (!) real value is "<method 'set_x_size' of 'panda3d.core.Texture' objects>"
        'set_y_size': None, # (!) real value is "<method 'set_y_size' of 'panda3d.core.Texture' objects>"
        'set_z_size': None, # (!) real value is "<method 'set_z_size' of 'panda3d.core.Texture' objects>"
        'setup1dTexture': None, # (!) real value is "<method 'setup1dTexture' of 'panda3d.core.Texture' objects>"
        'setup2dTexture': None, # (!) real value is "<method 'setup2dTexture' of 'panda3d.core.Texture' objects>"
        'setup2dTextureArray': None, # (!) real value is "<method 'setup2dTextureArray' of 'panda3d.core.Texture' objects>"
        'setup3dTexture': None, # (!) real value is "<method 'setup3dTexture' of 'panda3d.core.Texture' objects>"
        'setupBufferTexture': None, # (!) real value is "<method 'setupBufferTexture' of 'panda3d.core.Texture' objects>"
        'setupCubeMap': None, # (!) real value is "<method 'setupCubeMap' of 'panda3d.core.Texture' objects>"
        'setupCubeMapArray': None, # (!) real value is "<method 'setupCubeMapArray' of 'panda3d.core.Texture' objects>"
        'setupTexture': None, # (!) real value is "<method 'setupTexture' of 'panda3d.core.Texture' objects>"
        'setup_1d_texture': None, # (!) real value is "<method 'setup_1d_texture' of 'panda3d.core.Texture' objects>"
        'setup_2d_texture': None, # (!) real value is "<method 'setup_2d_texture' of 'panda3d.core.Texture' objects>"
        'setup_2d_texture_array': None, # (!) real value is "<method 'setup_2d_texture_array' of 'panda3d.core.Texture' objects>"
        'setup_3d_texture': None, # (!) real value is "<method 'setup_3d_texture' of 'panda3d.core.Texture' objects>"
        'setup_buffer_texture': None, # (!) real value is "<method 'setup_buffer_texture' of 'panda3d.core.Texture' objects>"
        'setup_cube_map': None, # (!) real value is "<method 'setup_cube_map' of 'panda3d.core.Texture' objects>"
        'setup_cube_map_array': None, # (!) real value is "<method 'setup_cube_map_array' of 'panda3d.core.Texture' objects>"
        'setup_texture': None, # (!) real value is "<method 'setup_texture' of 'panda3d.core.Texture' objects>"
        'simple_image_modified': None, # (!) real value is "<attribute 'simple_image_modified' of 'panda3d.core.Texture' objects>"
        'simple_ram_image': None, # (!) real value is "<attribute 'simple_ram_image' of 'panda3d.core.Texture' objects>"
        'simple_x_size': None, # (!) real value is "<attribute 'simple_x_size' of 'panda3d.core.Texture' objects>"
        'simple_y_size': None, # (!) real value is "<attribute 'simple_y_size' of 'panda3d.core.Texture' objects>"
        'store': None, # (!) real value is "<method 'store' of 'panda3d.core.Texture' objects>"
        'stringComponentType': None, # (!) real value is '<staticmethod(<built-in method stringComponentType of type object at 0x00007FFCFE2FED40>)>'
        'stringCompressionMode': None, # (!) real value is '<staticmethod(<built-in method stringCompressionMode of type object at 0x00007FFCFE2FED40>)>'
        'stringFormat': None, # (!) real value is '<staticmethod(<built-in method stringFormat of type object at 0x00007FFCFE2FED40>)>'
        'stringQualityLevel': None, # (!) real value is '<staticmethod(<built-in method stringQualityLevel of type object at 0x00007FFCFE2FED40>)>'
        'stringTextureType': None, # (!) real value is '<staticmethod(<built-in method stringTextureType of type object at 0x00007FFCFE2FED40>)>'
        'string_component_type': None, # (!) real value is '<staticmethod(<built-in method string_component_type of type object at 0x00007FFCFE2FED40>)>'
        'string_compression_mode': None, # (!) real value is '<staticmethod(<built-in method string_compression_mode of type object at 0x00007FFCFE2FED40>)>'
        'string_format': None, # (!) real value is '<staticmethod(<built-in method string_format of type object at 0x00007FFCFE2FED40>)>'
        'string_quality_level': None, # (!) real value is '<staticmethod(<built-in method string_quality_level of type object at 0x00007FFCFE2FED40>)>'
        'string_texture_type': None, # (!) real value is '<staticmethod(<built-in method string_texture_type of type object at 0x00007FFCFE2FED40>)>'
        'texture_type': None, # (!) real value is "<attribute 'texture_type' of 'panda3d.core.Texture' objects>"
        'uncompressRamImage': None, # (!) real value is "<method 'uncompressRamImage' of 'panda3d.core.Texture' objects>"
        'uncompress_ram_image': None, # (!) real value is "<method 'uncompress_ram_image' of 'panda3d.core.Texture' objects>"
        'upToPower2': None, # (!) real value is '<staticmethod(<built-in method upToPower2 of type object at 0x00007FFCFE2FED40>)>'
        'up_to_power_2': None, # (!) real value is '<staticmethod(<built-in method up_to_power_2 of type object at 0x00007FFCFE2FED40>)>'
        'upcastToNamable': None, # (!) real value is "<method 'upcastToNamable' of 'panda3d.core.Texture' objects>"
        'upcastToTypedWritableReferenceCount': None, # (!) real value is "<method 'upcastToTypedWritableReferenceCount' of 'panda3d.core.Texture' objects>"
        'upcast_to_Namable': None, # (!) real value is "<method 'upcast_to_Namable' of 'panda3d.core.Texture' objects>"
        'upcast_to_TypedWritableReferenceCount': None, # (!) real value is "<method 'upcast_to_TypedWritableReferenceCount' of 'panda3d.core.Texture' objects>"
        'usage_hint': None, # (!) real value is "<attribute 'usage_hint' of 'panda3d.core.Texture' objects>"
        'usesMipmaps': None, # (!) real value is "<method 'usesMipmaps' of 'panda3d.core.Texture' objects>"
        'uses_mipmaps': None, # (!) real value is "<method 'uses_mipmaps' of 'panda3d.core.Texture' objects>"
        'wasImageModified': None, # (!) real value is "<method 'wasImageModified' of 'panda3d.core.Texture' objects>"
        'was_image_modified': None, # (!) real value is "<method 'was_image_modified' of 'panda3d.core.Texture' objects>"
        'wrap_u': None, # (!) real value is "<attribute 'wrap_u' of 'panda3d.core.Texture' objects>"
        'wrap_v': None, # (!) real value is "<attribute 'wrap_v' of 'panda3d.core.Texture' objects>"
        'wrap_w': None, # (!) real value is "<attribute 'wrap_w' of 'panda3d.core.Texture' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.core.Texture' objects>"
        'writeTxo': None, # (!) real value is "<method 'writeTxo' of 'panda3d.core.Texture' objects>"
        'write_txo': None, # (!) real value is "<method 'write_txo' of 'panda3d.core.Texture' objects>"
        'x_size': None, # (!) real value is "<attribute 'x_size' of 'panda3d.core.Texture' objects>"
        'y_size': None, # (!) real value is "<attribute 'y_size' of 'panda3d.core.Texture' objects>"
        'z_size': None, # (!) real value is "<attribute 'z_size' of 'panda3d.core.Texture' objects>"
    }
    FAlpha = 6
    FBlue = 5
    FColorIndex = 2
    FDepthComponent = 23
    FDepthComponent16 = 24
    FDepthComponent24 = 25
    FDepthComponent32 = 26
    FDepthStencil = 1
    FGreen = 4
    FLuminance = 18
    FLuminanceAlpha = 19
    FLuminanceAlphamask = 20
    FR11G11B10 = 42
    FR16 = 27
    FR16i = 46
    FR32 = 35
    FR32i = 34
    FR8i = 38
    FRed = 3
    FRg = 45
    FRg16 = 28
    FRg16i = 47
    FRg32 = 36
    FRg32i = 50
    FRg8i = 39
    FRgb = 7
    FRgb10A2 = 44
    FRgb12 = 10
    FRgb16 = 29
    FRgb16i = 48
    FRgb32 = 37
    FRgb32i = 51
    FRgb332 = 11
    FRgb5 = 8
    FRgb8 = 9
    FRgb8i = 40
    FRgb9E5 = 43
    FRgba = 12
    FRgba12 = 17
    FRgba16 = 21
    FRgba16i = 49
    FRgba32 = 22
    FRgba32i = 52
    FRgba4 = 14
    FRgba5 = 15
    FRgba8 = 16
    FRgba8i = 41
    FRgbm = 13
    FSluminance = 32
    FSluminanceAlpha = 33
    FSrgb = 30
    FSrgbAlpha = 31
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
    F_alpha = 6
    F_blue = 5
    F_color_index = 2
    F_depth_component = 23
    F_depth_component16 = 24
    F_depth_component24 = 25
    F_depth_component32 = 26
    F_depth_stencil = 1
    F_green = 4
    F_luminance = 18
    F_luminance_alpha = 19
    F_luminance_alphamask = 20
    F_r11_g11_b10 = 42
    F_r16 = 27
    F_r16i = 46
    F_r32 = 35
    F_r32i = 34
    F_r8i = 38
    F_red = 3
    F_rg = 45
    F_rg16 = 28
    F_rg16i = 47
    F_rg32 = 36
    F_rg32i = 50
    F_rg8i = 39
    F_rgb = 7
    F_rgb10_a2 = 44
    F_rgb12 = 10
    F_rgb16 = 29
    F_rgb16i = 48
    F_rgb32 = 37
    F_rgb32i = 51
    F_rgb332 = 11
    F_rgb5 = 8
    F_rgb8 = 9
    F_rgb8i = 40
    F_rgb9_e5 = 43
    F_rgba = 12
    F_rgba12 = 17
    F_rgba16 = 21
    F_rgba16i = 49
    F_rgba32 = 22
    F_rgba32i = 52
    F_rgba4 = 14
    F_rgba5 = 15
    F_rgba8 = 16
    F_rgba8i = 41
    F_rgbm = 13
    F_sluminance = 32
    F_sluminance_alpha = 33
    F_srgb = 30
    F_srgb_alpha = 31
    QLBest = 3
    QLDefault = 0
    QLFastest = 1
    QLNormal = 2
    QL_best = 3
    QL_default = 0
    QL_fastest = 1
    QL_normal = 2
    TByte = 5
    TFloat = 2
    THalfFloat = 7
    TInt = 4
    TShort = 6
    TT1dTexture = 0
    TT1dTextureArray = 7
    TT2dTexture = 1
    TT2dTextureArray = 3
    TT3dTexture = 2
    TTBufferTexture = 5
    TTCubeMap = 4
    TTCubeMapArray = 6
    TT_1d_texture = 0
    TT_1d_texture_array = 7
    TT_2d_texture = 1
    TT_2d_texture_array = 3
    TT_3d_texture = 2
    TT_buffer_texture = 5
    TT_cube_map = 4
    TT_cube_map_array = 6
    TUnsignedByte = 0
    TUnsignedInt = 8
    TUnsignedInt248 = 3
    TUnsignedShort = 1
    T_byte = 5
    T_float = 2
    T_half_float = 7
    T_int = 4
    T_short = 6
    T_unsigned_byte = 0
    T_unsigned_int = 8
    T_unsigned_int_24_8 = 3
    T_unsigned_short = 1
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


