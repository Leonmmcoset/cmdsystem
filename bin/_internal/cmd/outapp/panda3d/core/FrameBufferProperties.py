# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class FrameBufferProperties(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * A container for the various kinds of properties we might ask to have on a
     * graphics frameBuffer before we create a GSG.
     */
    """
    def addProperties(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_properties(const FrameBufferProperties self, const FrameBufferProperties other)
        
        /**
         * Sets any properties that are explicitly specified in other on this object.
         * Leaves other properties unchanged.
         */
        """
        pass

    def add_properties(self, const_FrameBufferProperties_self, const_FrameBufferProperties_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_properties(const FrameBufferProperties self, const FrameBufferProperties other)
        
        /**
         * Sets any properties that are explicitly specified in other on this object.
         * Leaves other properties unchanged.
         */
        """
        pass

    def clear(self, const_FrameBufferProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear(const FrameBufferProperties self)
        
        /**
         * Unsets all properties that have been specified so far, and resets the
         * FrameBufferProperties structure to its initial empty state.
         */
        """
        pass

    def getAccumBits(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_accum_bits(FrameBufferProperties self)
        
        /**
         *
         */
        """
        pass

    def getAlphaBits(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_alpha_bits(FrameBufferProperties self)
        
        /**
         *
         */
        """
        pass

    def getAuxFloat(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_aux_float(FrameBufferProperties self)
        
        /**
         *
         */
        """
        pass

    def getAuxHrgba(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_aux_hrgba(FrameBufferProperties self)
        
        /**
         *
         */
        """
        pass

    def getAuxMask(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_aux_mask(FrameBufferProperties self)
        
        /**
         * Converts the aux bitplanes of the framebuffer into a RenderBuffer::Type.
         */
        """
        pass

    def getAuxRgba(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_aux_rgba(FrameBufferProperties self)
        
        /**
         *
         */
        """
        pass

    def getBackBuffers(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_back_buffers(FrameBufferProperties self)
        
        /**
         *
         */
        """
        pass

    def getBlueBits(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_blue_bits(FrameBufferProperties self)
        
        /**
         *
         */
        """
        pass

    def getBufferMask(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_buffer_mask(FrameBufferProperties self)
        
        /**
         * Converts the non-aux bitplanes of the framebuffer into a
         * RenderBuffer::Type.
         */
        """
        pass

    def getColorBits(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_color_bits(FrameBufferProperties self)
        
        /**
         *
         */
        """
        pass

    def getCoverageSamples(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_coverage_samples(FrameBufferProperties self)
        
        /**
         * If coverage samples are specified, and there is hardware support, we use
         * coverage multisampling.
         */
        """
        pass

    def getDefault(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_default()
        
        /**
         * Returns a FrameBufferProperties structure with all of the default values
         * filled in according to the user's config file.
         */
        """
        pass

    def getDepthBits(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_depth_bits(FrameBufferProperties self)
        
        // Individual queries.
        
        // Individual queries.
        
        /**
         *
         */
        """
        pass

    def getFloatColor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_float_color(FrameBufferProperties self)
        
        /**
         *
         */
        """
        pass

    def getFloatDepth(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_float_depth(FrameBufferProperties self)
        
        /**
         *
         */
        """
        pass

    def getForceHardware(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_force_hardware(FrameBufferProperties self)
        
        /**
         *
         */
        """
        pass

    def getForceSoftware(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_force_software(FrameBufferProperties self)
        
        /**
         *
         */
        """
        pass

    def getGreenBits(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_green_bits(FrameBufferProperties self)
        
        /**
         *
         */
        """
        pass

    def getIndexedColor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_indexed_color(FrameBufferProperties self)
        
        /**
         *
         */
        """
        pass

    def getMultisamples(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_multisamples(FrameBufferProperties self)
        
        /**
         *
         */
        """
        pass

    def getQuality(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_quality(FrameBufferProperties self, const FrameBufferProperties reqs)
        
        /**
         * Assumes that these properties are a description of a window.
         *
         * Measures how well this window satisfies a specified set of requirements.  A
         * higher quality number means that more requirements were satisfied.  A
         * quality of zero means that the window is unsuitable.
         *
         * The routine deducts a lot if the window fails to provide a requested
         * feature.  It deducts less if the window provides a feature, but at a
         * degraded level of functionality (ie, the user asks for rgba8, color, but
         * the window only provides rgba4).  The routine also deducts a small amount
         * for unnecessary features.  For example, if the window has an accumulation
         * buffer when one is not requested will reduce quality slightly.  Maximum
         * quality is obtained when the window exactly matches the request.
         *
         * If you want to know whether the window satisfies all of the requirements,
         * use the "subsumes" function.
         */
        """
        pass

    def getRedBits(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_red_bits(FrameBufferProperties self)
        
        /**
         *
         */
        """
        pass

    def getRgbColor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_rgb_color(FrameBufferProperties self)
        
        /**
         *
         */
        """
        pass

    def getSrgbColor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_srgb_color(FrameBufferProperties self)
        
        /**
         *
         */
        """
        pass

    def getStencilBits(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_stencil_bits(FrameBufferProperties self)
        
        /**
         *
         */
        """
        pass

    def getStereo(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_stereo(FrameBufferProperties self)
        
        /**
         *
         */
        """
        pass

    def get_accum_bits(self, FrameBufferProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_accum_bits(FrameBufferProperties self)
        
        /**
         *
         */
        """
        pass

    def get_alpha_bits(self, FrameBufferProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_alpha_bits(FrameBufferProperties self)
        
        /**
         *
         */
        """
        pass

    def get_aux_float(self, FrameBufferProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_aux_float(FrameBufferProperties self)
        
        /**
         *
         */
        """
        pass

    def get_aux_hrgba(self, FrameBufferProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_aux_hrgba(FrameBufferProperties self)
        
        /**
         *
         */
        """
        pass

    def get_aux_mask(self, FrameBufferProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_aux_mask(FrameBufferProperties self)
        
        /**
         * Converts the aux bitplanes of the framebuffer into a RenderBuffer::Type.
         */
        """
        pass

    def get_aux_rgba(self, FrameBufferProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_aux_rgba(FrameBufferProperties self)
        
        /**
         *
         */
        """
        pass

    def get_back_buffers(self, FrameBufferProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_back_buffers(FrameBufferProperties self)
        
        /**
         *
         */
        """
        pass

    def get_blue_bits(self, FrameBufferProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_blue_bits(FrameBufferProperties self)
        
        /**
         *
         */
        """
        pass

    def get_buffer_mask(self, FrameBufferProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_buffer_mask(FrameBufferProperties self)
        
        /**
         * Converts the non-aux bitplanes of the framebuffer into a
         * RenderBuffer::Type.
         */
        """
        pass

    def get_color_bits(self, FrameBufferProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_color_bits(FrameBufferProperties self)
        
        /**
         *
         */
        """
        pass

    def get_coverage_samples(self, FrameBufferProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_coverage_samples(FrameBufferProperties self)
        
        /**
         * If coverage samples are specified, and there is hardware support, we use
         * coverage multisampling.
         */
        """
        pass

    def get_default(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_default()
        
        /**
         * Returns a FrameBufferProperties structure with all of the default values
         * filled in according to the user's config file.
         */
        """
        pass

    def get_depth_bits(self, FrameBufferProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_depth_bits(FrameBufferProperties self)
        
        // Individual queries.
        
        // Individual queries.
        
        /**
         *
         */
        """
        pass

    def get_float_color(self, FrameBufferProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_float_color(FrameBufferProperties self)
        
        /**
         *
         */
        """
        pass

    def get_float_depth(self, FrameBufferProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_float_depth(FrameBufferProperties self)
        
        /**
         *
         */
        """
        pass

    def get_force_hardware(self, FrameBufferProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_force_hardware(FrameBufferProperties self)
        
        /**
         *
         */
        """
        pass

    def get_force_software(self, FrameBufferProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_force_software(FrameBufferProperties self)
        
        /**
         *
         */
        """
        pass

    def get_green_bits(self, FrameBufferProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_green_bits(FrameBufferProperties self)
        
        /**
         *
         */
        """
        pass

    def get_indexed_color(self, FrameBufferProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_indexed_color(FrameBufferProperties self)
        
        /**
         *
         */
        """
        pass

    def get_multisamples(self, FrameBufferProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_multisamples(FrameBufferProperties self)
        
        /**
         *
         */
        """
        pass

    def get_quality(self, FrameBufferProperties_self, const_FrameBufferProperties_reqs): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_quality(FrameBufferProperties self, const FrameBufferProperties reqs)
        
        /**
         * Assumes that these properties are a description of a window.
         *
         * Measures how well this window satisfies a specified set of requirements.  A
         * higher quality number means that more requirements were satisfied.  A
         * quality of zero means that the window is unsuitable.
         *
         * The routine deducts a lot if the window fails to provide a requested
         * feature.  It deducts less if the window provides a feature, but at a
         * degraded level of functionality (ie, the user asks for rgba8, color, but
         * the window only provides rgba4).  The routine also deducts a small amount
         * for unnecessary features.  For example, if the window has an accumulation
         * buffer when one is not requested will reduce quality slightly.  Maximum
         * quality is obtained when the window exactly matches the request.
         *
         * If you want to know whether the window satisfies all of the requirements,
         * use the "subsumes" function.
         */
        """
        pass

    def get_red_bits(self, FrameBufferProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_red_bits(FrameBufferProperties self)
        
        /**
         *
         */
        """
        pass

    def get_rgb_color(self, FrameBufferProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_rgb_color(FrameBufferProperties self)
        
        /**
         *
         */
        """
        pass

    def get_srgb_color(self, FrameBufferProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_srgb_color(FrameBufferProperties self)
        
        /**
         *
         */
        """
        pass

    def get_stencil_bits(self, FrameBufferProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_stencil_bits(FrameBufferProperties self)
        
        /**
         *
         */
        """
        pass

    def get_stereo(self, FrameBufferProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_stereo(FrameBufferProperties self)
        
        /**
         *
         */
        """
        pass

    def isAnySpecified(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_any_specified(FrameBufferProperties self)
        
        /**
         * Returns true if any properties have been specified, false otherwise.
         */
        """
        pass

    def isBasic(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_basic(FrameBufferProperties self)
        
        /**
         * Returns true if the properties are extremely basic.  The following count as
         * basic: rgb or rgba, depth.  If anything else is specified, the properties
         * are non-basic.
         */
        """
        pass

    def isSingleBuffered(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_single_buffered(FrameBufferProperties self)
        
        /**
         *
         */
        """
        pass

    def isStereo(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_stereo(FrameBufferProperties self)
        
        /**
         *
         */
        """
        pass

    def is_any_specified(self, FrameBufferProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_any_specified(FrameBufferProperties self)
        
        /**
         * Returns true if any properties have been specified, false otherwise.
         */
        """
        pass

    def is_basic(self, FrameBufferProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_basic(FrameBufferProperties self)
        
        /**
         * Returns true if the properties are extremely basic.  The following count as
         * basic: rgb or rgba, depth.  If anything else is specified, the properties
         * are non-basic.
         */
        """
        pass

    def is_single_buffered(self, FrameBufferProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_single_buffered(FrameBufferProperties self)
        
        /**
         *
         */
        """
        pass

    def is_stereo(self, FrameBufferProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_stereo(FrameBufferProperties self)
        
        /**
         *
         */
        """
        pass

    def output(self, FrameBufferProperties_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(FrameBufferProperties self, ostream out)
        
        /**
         * Generates a string representation.
         */
        """
        pass

    def setAccumBits(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_accum_bits(const FrameBufferProperties self, int n)
        
        /**
         *
         */
        """
        pass

    def setAllSpecified(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_all_specified(const FrameBufferProperties self)
        
        /**
         * Marks all bits as having been specified.
         */
        """
        pass

    def setAlphaBits(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_alpha_bits(const FrameBufferProperties self, int n)
        
        /**
         *
         */
        """
        pass

    def setAuxFloat(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_aux_float(const FrameBufferProperties self, int n)
        
        /**
         *
         */
        """
        pass

    def setAuxHrgba(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_aux_hrgba(const FrameBufferProperties self, int n)
        
        /**
         *
         */
        """
        pass

    def setAuxRgba(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_aux_rgba(const FrameBufferProperties self, int n)
        
        /**
         *
         */
        """
        pass

    def setBackBuffers(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_back_buffers(const FrameBufferProperties self, int n)
        
        /**
         *
         */
        """
        pass

    def setBlueBits(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_blue_bits(const FrameBufferProperties self, int n)
        
        /**
         *
         */
        """
        pass

    def setColorBits(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_color_bits(const FrameBufferProperties self, int n)
        
        /**
         * Sets the number of requested color bits as a single number that represents
         * the sum of the individual numbers of red, green and blue bits.  Panda won't
         * care how the individual bits are divided up.
         *
         * See also set_rgba_bits, which allows you to specify requirements for the
         * individual components.
         */
        """
        pass

    def setCoverageSamples(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_coverage_samples(const FrameBufferProperties self, int n)
        
        /**
         * If coverage samples are specified, and there is hardware support, we use
         * coverage multisampling
         */
        """
        pass

    def setDepthBits(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_depth_bits(const FrameBufferProperties self, int n)
        
        // Individual assigners.
        
        // Individual assigners.
        
        /**
         *
         */
        """
        pass

    def setFloatColor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_float_color(const FrameBufferProperties self, bool n)
        
        /**
         *
         */
        """
        pass

    def setFloatDepth(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_float_depth(const FrameBufferProperties self, bool n)
        
        /**
         *
         */
        """
        pass

    def setForceHardware(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_force_hardware(const FrameBufferProperties self, bool n)
        
        /**
         *
         */
        """
        pass

    def setForceSoftware(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_force_software(const FrameBufferProperties self, bool n)
        
        /**
         *
         */
        """
        pass

    def setGreenBits(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_green_bits(const FrameBufferProperties self, int n)
        
        /**
         *
         */
        """
        pass

    def setIndexedColor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_indexed_color(const FrameBufferProperties self, bool n)
        
        /**
         *
         */
        """
        pass

    def setMultisamples(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_multisamples(const FrameBufferProperties self, int n)
        
        /**
         *
         */
        """
        pass

    def setOneBitPerChannel(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_one_bit_per_channel(const FrameBufferProperties self)
        
        /**
         * If any of the depth, color, alpha, accum, or stencil properties is set to
         * more than one, then they are reduced to one.
         */
        """
        pass

    def setRedBits(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_red_bits(const FrameBufferProperties self, int n)
        
        /**
         *
         */
        """
        pass

    def setRgbaBits(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_rgba_bits(const FrameBufferProperties self, int r, int g, int b, int a)
        
        /**
         * Convenience method for setting the red, green, blue and alpha bits in one
         * go.
         */
        """
        pass

    def setRgbColor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_rgb_color(const FrameBufferProperties self, bool n)
        
        /**
         *
         */
        """
        pass

    def setSrgbColor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_srgb_color(const FrameBufferProperties self, bool n)
        
        /**
         *
         */
        """
        pass

    def setStencilBits(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_stencil_bits(const FrameBufferProperties self, int n)
        
        /**
         *
         */
        """
        pass

    def setStereo(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_stereo(const FrameBufferProperties self, bool n)
        
        /**
         *
         */
        """
        pass

    def setupColorTexture(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        setup_color_texture(FrameBufferProperties self, Texture tex)
        
        /**
         * Sets the texture up for render-to-texture matching these framebuffer
         * properties.
         *
         * Returns true if there was a format that had enough bits, false otherwise.
         * Of course, this is no guarantee that a particular graphics back-end
         * supports rendering to textures of that format.
         */
        """
        pass

    def setupDepthTexture(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        setup_depth_texture(FrameBufferProperties self, Texture tex)
        
        /**
         * Sets the texture up for render-to-texture matching these framebuffer
         * properties.
         *
         * Returns true if there was a format that had enough bits, false otherwise.
         * Of course, this is no guarantee that a particular graphics back-end
         * supports rendering to textures of that format.
         */
        """
        pass

    def setup_color_texture(self, FrameBufferProperties_self, Texture_tex): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        setup_color_texture(FrameBufferProperties self, Texture tex)
        
        /**
         * Sets the texture up for render-to-texture matching these framebuffer
         * properties.
         *
         * Returns true if there was a format that had enough bits, false otherwise.
         * Of course, this is no guarantee that a particular graphics back-end
         * supports rendering to textures of that format.
         */
        """
        pass

    def setup_depth_texture(self, FrameBufferProperties_self, Texture_tex): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        setup_depth_texture(FrameBufferProperties self, Texture tex)
        
        /**
         * Sets the texture up for render-to-texture matching these framebuffer
         * properties.
         *
         * Returns true if there was a format that had enough bits, false otherwise.
         * Of course, this is no guarantee that a particular graphics back-end
         * supports rendering to textures of that format.
         */
        """
        pass

    def set_accum_bits(self, const_FrameBufferProperties_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_accum_bits(const FrameBufferProperties self, int n)
        
        /**
         *
         */
        """
        pass

    def set_all_specified(self, const_FrameBufferProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_all_specified(const FrameBufferProperties self)
        
        /**
         * Marks all bits as having been specified.
         */
        """
        pass

    def set_alpha_bits(self, const_FrameBufferProperties_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_alpha_bits(const FrameBufferProperties self, int n)
        
        /**
         *
         */
        """
        pass

    def set_aux_float(self, const_FrameBufferProperties_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_aux_float(const FrameBufferProperties self, int n)
        
        /**
         *
         */
        """
        pass

    def set_aux_hrgba(self, const_FrameBufferProperties_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_aux_hrgba(const FrameBufferProperties self, int n)
        
        /**
         *
         */
        """
        pass

    def set_aux_rgba(self, const_FrameBufferProperties_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_aux_rgba(const FrameBufferProperties self, int n)
        
        /**
         *
         */
        """
        pass

    def set_back_buffers(self, const_FrameBufferProperties_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_back_buffers(const FrameBufferProperties self, int n)
        
        /**
         *
         */
        """
        pass

    def set_blue_bits(self, const_FrameBufferProperties_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_blue_bits(const FrameBufferProperties self, int n)
        
        /**
         *
         */
        """
        pass

    def set_color_bits(self, const_FrameBufferProperties_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_color_bits(const FrameBufferProperties self, int n)
        
        /**
         * Sets the number of requested color bits as a single number that represents
         * the sum of the individual numbers of red, green and blue bits.  Panda won't
         * care how the individual bits are divided up.
         *
         * See also set_rgba_bits, which allows you to specify requirements for the
         * individual components.
         */
        """
        pass

    def set_coverage_samples(self, const_FrameBufferProperties_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_coverage_samples(const FrameBufferProperties self, int n)
        
        /**
         * If coverage samples are specified, and there is hardware support, we use
         * coverage multisampling
         */
        """
        pass

    def set_depth_bits(self, const_FrameBufferProperties_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_depth_bits(const FrameBufferProperties self, int n)
        
        // Individual assigners.
        
        // Individual assigners.
        
        /**
         *
         */
        """
        pass

    def set_float_color(self, const_FrameBufferProperties_self, bool_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_float_color(const FrameBufferProperties self, bool n)
        
        /**
         *
         */
        """
        pass

    def set_float_depth(self, const_FrameBufferProperties_self, bool_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_float_depth(const FrameBufferProperties self, bool n)
        
        /**
         *
         */
        """
        pass

    def set_force_hardware(self, const_FrameBufferProperties_self, bool_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_force_hardware(const FrameBufferProperties self, bool n)
        
        /**
         *
         */
        """
        pass

    def set_force_software(self, const_FrameBufferProperties_self, bool_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_force_software(const FrameBufferProperties self, bool n)
        
        /**
         *
         */
        """
        pass

    def set_green_bits(self, const_FrameBufferProperties_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_green_bits(const FrameBufferProperties self, int n)
        
        /**
         *
         */
        """
        pass

    def set_indexed_color(self, const_FrameBufferProperties_self, bool_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_indexed_color(const FrameBufferProperties self, bool n)
        
        /**
         *
         */
        """
        pass

    def set_multisamples(self, const_FrameBufferProperties_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_multisamples(const FrameBufferProperties self, int n)
        
        /**
         *
         */
        """
        pass

    def set_one_bit_per_channel(self, const_FrameBufferProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_one_bit_per_channel(const FrameBufferProperties self)
        
        /**
         * If any of the depth, color, alpha, accum, or stencil properties is set to
         * more than one, then they are reduced to one.
         */
        """
        pass

    def set_red_bits(self, const_FrameBufferProperties_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_red_bits(const FrameBufferProperties self, int n)
        
        /**
         *
         */
        """
        pass

    def set_rgba_bits(self, const_FrameBufferProperties_self, int_r, int_g, int_b, int_a): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_rgba_bits(const FrameBufferProperties self, int r, int g, int b, int a)
        
        /**
         * Convenience method for setting the red, green, blue and alpha bits in one
         * go.
         */
        """
        pass

    def set_rgb_color(self, const_FrameBufferProperties_self, bool_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_rgb_color(const FrameBufferProperties self, bool n)
        
        /**
         *
         */
        """
        pass

    def set_srgb_color(self, const_FrameBufferProperties_self, bool_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_srgb_color(const FrameBufferProperties self, bool n)
        
        /**
         *
         */
        """
        pass

    def set_stencil_bits(self, const_FrameBufferProperties_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_stencil_bits(const FrameBufferProperties self, int n)
        
        /**
         *
         */
        """
        pass

    def set_stereo(self, const_FrameBufferProperties_self, bool_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_stereo(const FrameBufferProperties self, bool n)
        
        /**
         *
         */
        """
        pass

    def subsumes(self, FrameBufferProperties_self, const_FrameBufferProperties_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        subsumes(FrameBufferProperties self, const FrameBufferProperties other)
        
        /**
         * Returns true if this set of properties makes strictly greater or equal
         * demands of the framebuffer than the other set of framebuffer properties.
         */
        """
        pass

    def verifyHardwareSoftware(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        verify_hardware_software(FrameBufferProperties self, const FrameBufferProperties props, str renderer)
        
        /**
         * Validates that the properties represent the desired kind of renderer
         * (hardware or software).  If not, prints out an error message and returns
         * false.
         */
        """
        pass

    def verify_hardware_software(self, FrameBufferProperties_self, const_FrameBufferProperties_props, str_renderer): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        verify_hardware_software(FrameBufferProperties self, const FrameBufferProperties props, str renderer)
        
        /**
         * Validates that the properties represent the desired kind of renderer
         * (hardware or software).  If not, prints out an error message and returns
         * false.
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

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    accum_bits = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    alpha_bits = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    aux_float = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    aux_hrgba = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    aux_rgba = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    back_buffers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    blue_bits = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    color_bits = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    coverage_samples = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    depth_bits = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """// Individual queries."""

    float_color = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    float_depth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    force_hardware = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    force_software = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    green_bits = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    indexed_color = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    multisamples = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    red_bits = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    rgb_color = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    srgb_color = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    stencil_bits = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    stereo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.FrameBufferProperties' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.FrameBufferProperties' objects>"
        '__doc__': '/**\n * A container for the various kinds of properties we might ask to have on a\n * graphics frameBuffer before we create a GSG.\n */',
        '__eq__': None, # (!) real value is "<slot wrapper '__eq__' of 'panda3d.core.FrameBufferProperties' objects>"
        '__ge__': None, # (!) real value is "<slot wrapper '__ge__' of 'panda3d.core.FrameBufferProperties' objects>"
        '__gt__': None, # (!) real value is "<slot wrapper '__gt__' of 'panda3d.core.FrameBufferProperties' objects>"
        '__hash__': None, # (!) real value is "<slot wrapper '__hash__' of 'panda3d.core.FrameBufferProperties' objects>"
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.FrameBufferProperties' objects>"
        '__le__': None, # (!) real value is "<slot wrapper '__le__' of 'panda3d.core.FrameBufferProperties' objects>"
        '__lt__': None, # (!) real value is "<slot wrapper '__lt__' of 'panda3d.core.FrameBufferProperties' objects>"
        '__ne__': None, # (!) real value is "<slot wrapper '__ne__' of 'panda3d.core.FrameBufferProperties' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2DE010>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.FrameBufferProperties' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.FrameBufferProperties' objects>"
        'accum_bits': None, # (!) real value is "<attribute 'accum_bits' of 'panda3d.core.FrameBufferProperties' objects>"
        'addProperties': None, # (!) real value is "<method 'addProperties' of 'panda3d.core.FrameBufferProperties' objects>"
        'add_properties': None, # (!) real value is "<method 'add_properties' of 'panda3d.core.FrameBufferProperties' objects>"
        'alpha_bits': None, # (!) real value is "<attribute 'alpha_bits' of 'panda3d.core.FrameBufferProperties' objects>"
        'aux_float': None, # (!) real value is "<attribute 'aux_float' of 'panda3d.core.FrameBufferProperties' objects>"
        'aux_hrgba': None, # (!) real value is "<attribute 'aux_hrgba' of 'panda3d.core.FrameBufferProperties' objects>"
        'aux_rgba': None, # (!) real value is "<attribute 'aux_rgba' of 'panda3d.core.FrameBufferProperties' objects>"
        'back_buffers': None, # (!) real value is "<attribute 'back_buffers' of 'panda3d.core.FrameBufferProperties' objects>"
        'blue_bits': None, # (!) real value is "<attribute 'blue_bits' of 'panda3d.core.FrameBufferProperties' objects>"
        'clear': None, # (!) real value is "<method 'clear' of 'panda3d.core.FrameBufferProperties' objects>"
        'color_bits': None, # (!) real value is "<attribute 'color_bits' of 'panda3d.core.FrameBufferProperties' objects>"
        'coverage_samples': None, # (!) real value is "<attribute 'coverage_samples' of 'panda3d.core.FrameBufferProperties' objects>"
        'depth_bits': None, # (!) real value is "<attribute 'depth_bits' of 'panda3d.core.FrameBufferProperties' objects>"
        'float_color': None, # (!) real value is "<attribute 'float_color' of 'panda3d.core.FrameBufferProperties' objects>"
        'float_depth': None, # (!) real value is "<attribute 'float_depth' of 'panda3d.core.FrameBufferProperties' objects>"
        'force_hardware': None, # (!) real value is "<attribute 'force_hardware' of 'panda3d.core.FrameBufferProperties' objects>"
        'force_software': None, # (!) real value is "<attribute 'force_software' of 'panda3d.core.FrameBufferProperties' objects>"
        'getAccumBits': None, # (!) real value is "<method 'getAccumBits' of 'panda3d.core.FrameBufferProperties' objects>"
        'getAlphaBits': None, # (!) real value is "<method 'getAlphaBits' of 'panda3d.core.FrameBufferProperties' objects>"
        'getAuxFloat': None, # (!) real value is "<method 'getAuxFloat' of 'panda3d.core.FrameBufferProperties' objects>"
        'getAuxHrgba': None, # (!) real value is "<method 'getAuxHrgba' of 'panda3d.core.FrameBufferProperties' objects>"
        'getAuxMask': None, # (!) real value is "<method 'getAuxMask' of 'panda3d.core.FrameBufferProperties' objects>"
        'getAuxRgba': None, # (!) real value is "<method 'getAuxRgba' of 'panda3d.core.FrameBufferProperties' objects>"
        'getBackBuffers': None, # (!) real value is "<method 'getBackBuffers' of 'panda3d.core.FrameBufferProperties' objects>"
        'getBlueBits': None, # (!) real value is "<method 'getBlueBits' of 'panda3d.core.FrameBufferProperties' objects>"
        'getBufferMask': None, # (!) real value is "<method 'getBufferMask' of 'panda3d.core.FrameBufferProperties' objects>"
        'getColorBits': None, # (!) real value is "<method 'getColorBits' of 'panda3d.core.FrameBufferProperties' objects>"
        'getCoverageSamples': None, # (!) real value is "<method 'getCoverageSamples' of 'panda3d.core.FrameBufferProperties' objects>"
        'getDefault': None, # (!) real value is '<staticmethod(<built-in method getDefault of type object at 0x00007FFCFE2DE010>)>'
        'getDepthBits': None, # (!) real value is "<method 'getDepthBits' of 'panda3d.core.FrameBufferProperties' objects>"
        'getFloatColor': None, # (!) real value is "<method 'getFloatColor' of 'panda3d.core.FrameBufferProperties' objects>"
        'getFloatDepth': None, # (!) real value is "<method 'getFloatDepth' of 'panda3d.core.FrameBufferProperties' objects>"
        'getForceHardware': None, # (!) real value is "<method 'getForceHardware' of 'panda3d.core.FrameBufferProperties' objects>"
        'getForceSoftware': None, # (!) real value is "<method 'getForceSoftware' of 'panda3d.core.FrameBufferProperties' objects>"
        'getGreenBits': None, # (!) real value is "<method 'getGreenBits' of 'panda3d.core.FrameBufferProperties' objects>"
        'getIndexedColor': None, # (!) real value is "<method 'getIndexedColor' of 'panda3d.core.FrameBufferProperties' objects>"
        'getMultisamples': None, # (!) real value is "<method 'getMultisamples' of 'panda3d.core.FrameBufferProperties' objects>"
        'getQuality': None, # (!) real value is "<method 'getQuality' of 'panda3d.core.FrameBufferProperties' objects>"
        'getRedBits': None, # (!) real value is "<method 'getRedBits' of 'panda3d.core.FrameBufferProperties' objects>"
        'getRgbColor': None, # (!) real value is "<method 'getRgbColor' of 'panda3d.core.FrameBufferProperties' objects>"
        'getSrgbColor': None, # (!) real value is "<method 'getSrgbColor' of 'panda3d.core.FrameBufferProperties' objects>"
        'getStencilBits': None, # (!) real value is "<method 'getStencilBits' of 'panda3d.core.FrameBufferProperties' objects>"
        'getStereo': None, # (!) real value is "<method 'getStereo' of 'panda3d.core.FrameBufferProperties' objects>"
        'get_accum_bits': None, # (!) real value is "<method 'get_accum_bits' of 'panda3d.core.FrameBufferProperties' objects>"
        'get_alpha_bits': None, # (!) real value is "<method 'get_alpha_bits' of 'panda3d.core.FrameBufferProperties' objects>"
        'get_aux_float': None, # (!) real value is "<method 'get_aux_float' of 'panda3d.core.FrameBufferProperties' objects>"
        'get_aux_hrgba': None, # (!) real value is "<method 'get_aux_hrgba' of 'panda3d.core.FrameBufferProperties' objects>"
        'get_aux_mask': None, # (!) real value is "<method 'get_aux_mask' of 'panda3d.core.FrameBufferProperties' objects>"
        'get_aux_rgba': None, # (!) real value is "<method 'get_aux_rgba' of 'panda3d.core.FrameBufferProperties' objects>"
        'get_back_buffers': None, # (!) real value is "<method 'get_back_buffers' of 'panda3d.core.FrameBufferProperties' objects>"
        'get_blue_bits': None, # (!) real value is "<method 'get_blue_bits' of 'panda3d.core.FrameBufferProperties' objects>"
        'get_buffer_mask': None, # (!) real value is "<method 'get_buffer_mask' of 'panda3d.core.FrameBufferProperties' objects>"
        'get_color_bits': None, # (!) real value is "<method 'get_color_bits' of 'panda3d.core.FrameBufferProperties' objects>"
        'get_coverage_samples': None, # (!) real value is "<method 'get_coverage_samples' of 'panda3d.core.FrameBufferProperties' objects>"
        'get_default': None, # (!) real value is '<staticmethod(<built-in method get_default of type object at 0x00007FFCFE2DE010>)>'
        'get_depth_bits': None, # (!) real value is "<method 'get_depth_bits' of 'panda3d.core.FrameBufferProperties' objects>"
        'get_float_color': None, # (!) real value is "<method 'get_float_color' of 'panda3d.core.FrameBufferProperties' objects>"
        'get_float_depth': None, # (!) real value is "<method 'get_float_depth' of 'panda3d.core.FrameBufferProperties' objects>"
        'get_force_hardware': None, # (!) real value is "<method 'get_force_hardware' of 'panda3d.core.FrameBufferProperties' objects>"
        'get_force_software': None, # (!) real value is "<method 'get_force_software' of 'panda3d.core.FrameBufferProperties' objects>"
        'get_green_bits': None, # (!) real value is "<method 'get_green_bits' of 'panda3d.core.FrameBufferProperties' objects>"
        'get_indexed_color': None, # (!) real value is "<method 'get_indexed_color' of 'panda3d.core.FrameBufferProperties' objects>"
        'get_multisamples': None, # (!) real value is "<method 'get_multisamples' of 'panda3d.core.FrameBufferProperties' objects>"
        'get_quality': None, # (!) real value is "<method 'get_quality' of 'panda3d.core.FrameBufferProperties' objects>"
        'get_red_bits': None, # (!) real value is "<method 'get_red_bits' of 'panda3d.core.FrameBufferProperties' objects>"
        'get_rgb_color': None, # (!) real value is "<method 'get_rgb_color' of 'panda3d.core.FrameBufferProperties' objects>"
        'get_srgb_color': None, # (!) real value is "<method 'get_srgb_color' of 'panda3d.core.FrameBufferProperties' objects>"
        'get_stencil_bits': None, # (!) real value is "<method 'get_stencil_bits' of 'panda3d.core.FrameBufferProperties' objects>"
        'get_stereo': None, # (!) real value is "<method 'get_stereo' of 'panda3d.core.FrameBufferProperties' objects>"
        'green_bits': None, # (!) real value is "<attribute 'green_bits' of 'panda3d.core.FrameBufferProperties' objects>"
        'indexed_color': None, # (!) real value is "<attribute 'indexed_color' of 'panda3d.core.FrameBufferProperties' objects>"
        'isAnySpecified': None, # (!) real value is "<method 'isAnySpecified' of 'panda3d.core.FrameBufferProperties' objects>"
        'isBasic': None, # (!) real value is "<method 'isBasic' of 'panda3d.core.FrameBufferProperties' objects>"
        'isSingleBuffered': None, # (!) real value is "<method 'isSingleBuffered' of 'panda3d.core.FrameBufferProperties' objects>"
        'isStereo': None, # (!) real value is "<method 'isStereo' of 'panda3d.core.FrameBufferProperties' objects>"
        'is_any_specified': None, # (!) real value is "<method 'is_any_specified' of 'panda3d.core.FrameBufferProperties' objects>"
        'is_basic': None, # (!) real value is "<method 'is_basic' of 'panda3d.core.FrameBufferProperties' objects>"
        'is_single_buffered': None, # (!) real value is "<method 'is_single_buffered' of 'panda3d.core.FrameBufferProperties' objects>"
        'is_stereo': None, # (!) real value is "<method 'is_stereo' of 'panda3d.core.FrameBufferProperties' objects>"
        'multisamples': None, # (!) real value is "<attribute 'multisamples' of 'panda3d.core.FrameBufferProperties' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.FrameBufferProperties' objects>"
        'red_bits': None, # (!) real value is "<attribute 'red_bits' of 'panda3d.core.FrameBufferProperties' objects>"
        'rgb_color': None, # (!) real value is "<attribute 'rgb_color' of 'panda3d.core.FrameBufferProperties' objects>"
        'setAccumBits': None, # (!) real value is "<method 'setAccumBits' of 'panda3d.core.FrameBufferProperties' objects>"
        'setAllSpecified': None, # (!) real value is "<method 'setAllSpecified' of 'panda3d.core.FrameBufferProperties' objects>"
        'setAlphaBits': None, # (!) real value is "<method 'setAlphaBits' of 'panda3d.core.FrameBufferProperties' objects>"
        'setAuxFloat': None, # (!) real value is "<method 'setAuxFloat' of 'panda3d.core.FrameBufferProperties' objects>"
        'setAuxHrgba': None, # (!) real value is "<method 'setAuxHrgba' of 'panda3d.core.FrameBufferProperties' objects>"
        'setAuxRgba': None, # (!) real value is "<method 'setAuxRgba' of 'panda3d.core.FrameBufferProperties' objects>"
        'setBackBuffers': None, # (!) real value is "<method 'setBackBuffers' of 'panda3d.core.FrameBufferProperties' objects>"
        'setBlueBits': None, # (!) real value is "<method 'setBlueBits' of 'panda3d.core.FrameBufferProperties' objects>"
        'setColorBits': None, # (!) real value is "<method 'setColorBits' of 'panda3d.core.FrameBufferProperties' objects>"
        'setCoverageSamples': None, # (!) real value is "<method 'setCoverageSamples' of 'panda3d.core.FrameBufferProperties' objects>"
        'setDepthBits': None, # (!) real value is "<method 'setDepthBits' of 'panda3d.core.FrameBufferProperties' objects>"
        'setFloatColor': None, # (!) real value is "<method 'setFloatColor' of 'panda3d.core.FrameBufferProperties' objects>"
        'setFloatDepth': None, # (!) real value is "<method 'setFloatDepth' of 'panda3d.core.FrameBufferProperties' objects>"
        'setForceHardware': None, # (!) real value is "<method 'setForceHardware' of 'panda3d.core.FrameBufferProperties' objects>"
        'setForceSoftware': None, # (!) real value is "<method 'setForceSoftware' of 'panda3d.core.FrameBufferProperties' objects>"
        'setGreenBits': None, # (!) real value is "<method 'setGreenBits' of 'panda3d.core.FrameBufferProperties' objects>"
        'setIndexedColor': None, # (!) real value is "<method 'setIndexedColor' of 'panda3d.core.FrameBufferProperties' objects>"
        'setMultisamples': None, # (!) real value is "<method 'setMultisamples' of 'panda3d.core.FrameBufferProperties' objects>"
        'setOneBitPerChannel': None, # (!) real value is "<method 'setOneBitPerChannel' of 'panda3d.core.FrameBufferProperties' objects>"
        'setRedBits': None, # (!) real value is "<method 'setRedBits' of 'panda3d.core.FrameBufferProperties' objects>"
        'setRgbColor': None, # (!) real value is "<method 'setRgbColor' of 'panda3d.core.FrameBufferProperties' objects>"
        'setRgbaBits': None, # (!) real value is "<method 'setRgbaBits' of 'panda3d.core.FrameBufferProperties' objects>"
        'setSrgbColor': None, # (!) real value is "<method 'setSrgbColor' of 'panda3d.core.FrameBufferProperties' objects>"
        'setStencilBits': None, # (!) real value is "<method 'setStencilBits' of 'panda3d.core.FrameBufferProperties' objects>"
        'setStereo': None, # (!) real value is "<method 'setStereo' of 'panda3d.core.FrameBufferProperties' objects>"
        'set_accum_bits': None, # (!) real value is "<method 'set_accum_bits' of 'panda3d.core.FrameBufferProperties' objects>"
        'set_all_specified': None, # (!) real value is "<method 'set_all_specified' of 'panda3d.core.FrameBufferProperties' objects>"
        'set_alpha_bits': None, # (!) real value is "<method 'set_alpha_bits' of 'panda3d.core.FrameBufferProperties' objects>"
        'set_aux_float': None, # (!) real value is "<method 'set_aux_float' of 'panda3d.core.FrameBufferProperties' objects>"
        'set_aux_hrgba': None, # (!) real value is "<method 'set_aux_hrgba' of 'panda3d.core.FrameBufferProperties' objects>"
        'set_aux_rgba': None, # (!) real value is "<method 'set_aux_rgba' of 'panda3d.core.FrameBufferProperties' objects>"
        'set_back_buffers': None, # (!) real value is "<method 'set_back_buffers' of 'panda3d.core.FrameBufferProperties' objects>"
        'set_blue_bits': None, # (!) real value is "<method 'set_blue_bits' of 'panda3d.core.FrameBufferProperties' objects>"
        'set_color_bits': None, # (!) real value is "<method 'set_color_bits' of 'panda3d.core.FrameBufferProperties' objects>"
        'set_coverage_samples': None, # (!) real value is "<method 'set_coverage_samples' of 'panda3d.core.FrameBufferProperties' objects>"
        'set_depth_bits': None, # (!) real value is "<method 'set_depth_bits' of 'panda3d.core.FrameBufferProperties' objects>"
        'set_float_color': None, # (!) real value is "<method 'set_float_color' of 'panda3d.core.FrameBufferProperties' objects>"
        'set_float_depth': None, # (!) real value is "<method 'set_float_depth' of 'panda3d.core.FrameBufferProperties' objects>"
        'set_force_hardware': None, # (!) real value is "<method 'set_force_hardware' of 'panda3d.core.FrameBufferProperties' objects>"
        'set_force_software': None, # (!) real value is "<method 'set_force_software' of 'panda3d.core.FrameBufferProperties' objects>"
        'set_green_bits': None, # (!) real value is "<method 'set_green_bits' of 'panda3d.core.FrameBufferProperties' objects>"
        'set_indexed_color': None, # (!) real value is "<method 'set_indexed_color' of 'panda3d.core.FrameBufferProperties' objects>"
        'set_multisamples': None, # (!) real value is "<method 'set_multisamples' of 'panda3d.core.FrameBufferProperties' objects>"
        'set_one_bit_per_channel': None, # (!) real value is "<method 'set_one_bit_per_channel' of 'panda3d.core.FrameBufferProperties' objects>"
        'set_red_bits': None, # (!) real value is "<method 'set_red_bits' of 'panda3d.core.FrameBufferProperties' objects>"
        'set_rgb_color': None, # (!) real value is "<method 'set_rgb_color' of 'panda3d.core.FrameBufferProperties' objects>"
        'set_rgba_bits': None, # (!) real value is "<method 'set_rgba_bits' of 'panda3d.core.FrameBufferProperties' objects>"
        'set_srgb_color': None, # (!) real value is "<method 'set_srgb_color' of 'panda3d.core.FrameBufferProperties' objects>"
        'set_stencil_bits': None, # (!) real value is "<method 'set_stencil_bits' of 'panda3d.core.FrameBufferProperties' objects>"
        'set_stereo': None, # (!) real value is "<method 'set_stereo' of 'panda3d.core.FrameBufferProperties' objects>"
        'setupColorTexture': None, # (!) real value is "<method 'setupColorTexture' of 'panda3d.core.FrameBufferProperties' objects>"
        'setupDepthTexture': None, # (!) real value is "<method 'setupDepthTexture' of 'panda3d.core.FrameBufferProperties' objects>"
        'setup_color_texture': None, # (!) real value is "<method 'setup_color_texture' of 'panda3d.core.FrameBufferProperties' objects>"
        'setup_depth_texture': None, # (!) real value is "<method 'setup_depth_texture' of 'panda3d.core.FrameBufferProperties' objects>"
        'srgb_color': None, # (!) real value is "<attribute 'srgb_color' of 'panda3d.core.FrameBufferProperties' objects>"
        'stencil_bits': None, # (!) real value is "<attribute 'stencil_bits' of 'panda3d.core.FrameBufferProperties' objects>"
        'stereo': None, # (!) real value is "<attribute 'stereo' of 'panda3d.core.FrameBufferProperties' objects>"
        'subsumes': None, # (!) real value is "<method 'subsumes' of 'panda3d.core.FrameBufferProperties' objects>"
        'verifyHardwareSoftware': None, # (!) real value is "<method 'verifyHardwareSoftware' of 'panda3d.core.FrameBufferProperties' objects>"
        'verify_hardware_software': None, # (!) real value is "<method 'verify_hardware_software' of 'panda3d.core.FrameBufferProperties' objects>"
    }


