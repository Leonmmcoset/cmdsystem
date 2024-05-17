# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .GraphicsOutputBase import GraphicsOutputBase

from .DrawableRegion import DrawableRegion

class GraphicsOutput(GraphicsOutputBase, DrawableRegion):
    """
    /**
     * This is a base class for the various different classes that represent the
     * result of a frame of rendering.  The most common kind of GraphicsOutput is
     * a GraphicsWindow, which is a real-time window on the desktop, but another
     * example is GraphicsBuffer, which is an offscreen buffer.
     *
     * The actual rendering, and anything associated with the graphics context
     * itself, is managed by the associated GraphicsStateGuardian (which might
     * output to multiple GraphicsOutput objects).
     *
     * GraphicsOutputs are not actually writable to bam files, of course, but they
     * may be passed as event parameters, so they inherit from
     * TypedWritableReferenceCount instead of TypedReferenceCount for that
     * convenience.
     */
    """
    def addRenderTexture(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_render_texture(const GraphicsOutput self, Texture tex, int mode, int bitplane)
        
        /**
         * Creates a new Texture object, suitable for rendering the contents of this
         * buffer into, and appends it to the list of render textures.
         *
         * If tex is not NULL, it is the texture that will be set up for rendering
         * into; otherwise, a new Texture object will be created, in which case you
         * may call get_texture() to retrieve the new texture pointer.
         *
         * You can specify a bitplane to attach the texture to.  the legal choices
         * are:
         *
         * - RTP_depth
         * - RTP_depth_stencil
         * - RTP_color
         * - RTP_aux_rgba_0
         * - RTP_aux_rgba_1
         * - RTP_aux_rgba_2
         * - RTP_aux_rgba_3
         *
         * If you do not specify a bitplane to attach the texture to, this routine
         * will use a default based on the texture's format:
         *
         * - F_depth_component attaches to RTP_depth
         * - F_depth_stencil attaches to RTP_depth_stencil
         * - all other formats attach to RTP_color.
         *
         * The texture's format will be changed to match the format of the bitplane to
         * which it is attached.  For example, if you pass in an F_rgba texture and
         * order that it be attached to RTP_depth_stencil, it will turn into an
         * F_depth_stencil texture.
         *
         * Also see make_texture_buffer(), which is a higher-level interface for
         * preparing render-to-a-texture mode.
         */
        """
        pass

    def add_render_texture(self, const_GraphicsOutput_self, Texture_tex, int_mode, int_bitplane): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_render_texture(const GraphicsOutput self, Texture tex, int mode, int bitplane)
        
        /**
         * Creates a new Texture object, suitable for rendering the contents of this
         * buffer into, and appends it to the list of render textures.
         *
         * If tex is not NULL, it is the texture that will be set up for rendering
         * into; otherwise, a new Texture object will be created, in which case you
         * may call get_texture() to retrieve the new texture pointer.
         *
         * You can specify a bitplane to attach the texture to.  the legal choices
         * are:
         *
         * - RTP_depth
         * - RTP_depth_stencil
         * - RTP_color
         * - RTP_aux_rgba_0
         * - RTP_aux_rgba_1
         * - RTP_aux_rgba_2
         * - RTP_aux_rgba_3
         *
         * If you do not specify a bitplane to attach the texture to, this routine
         * will use a default based on the texture's format:
         *
         * - F_depth_component attaches to RTP_depth
         * - F_depth_stencil attaches to RTP_depth_stencil
         * - all other formats attach to RTP_color.
         *
         * The texture's format will be changed to match the format of the bitplane to
         * which it is attached.  For example, if you pass in an F_rgba texture and
         * order that it be attached to RTP_depth_stencil, it will turn into an
         * F_depth_stencil texture.
         *
         * Also see make_texture_buffer(), which is a higher-level interface for
         * preparing render-to-a-texture mode.
         */
        """
        pass

    def clearChildSort(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_child_sort(const GraphicsOutput self)
        
        /**
         * Resets the sort value of future offscreen buffers created by
         * make_texture_sort() to the default value.  See set_child_sort().
         */
        """
        pass

    def clearDeleteFlag(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_delete_flag(const GraphicsOutput self)
        
        /**
         * Resets the delete flag, so the GraphicsOutput will not be automatically
         * deleted before the beginning of the next frame.
         */
        """
        pass

    def clearRenderTextures(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_render_textures(const GraphicsOutput self)
        
        /**
         * If the GraphicsOutput is currently rendering to a texture, then all
         * textures are dissociated from the GraphicsOuput.
         */
        """
        pass

    def clear_child_sort(self, const_GraphicsOutput_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_child_sort(const GraphicsOutput self)
        
        /**
         * Resets the sort value of future offscreen buffers created by
         * make_texture_sort() to the default value.  See set_child_sort().
         */
        """
        pass

    def clear_delete_flag(self, const_GraphicsOutput_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_delete_flag(const GraphicsOutput self)
        
        /**
         * Resets the delete flag, so the GraphicsOutput will not be automatically
         * deleted before the beginning of the next frame.
         */
        """
        pass

    def clear_render_textures(self, const_GraphicsOutput_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_render_textures(const GraphicsOutput self)
        
        /**
         * If the GraphicsOutput is currently rendering to a texture, then all
         * textures are dissociated from the GraphicsOuput.
         */
        """
        pass

    def countTextures(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        count_textures(GraphicsOutput self)
        
        /**
         * If the GraphicsOutput is set to render into a texture, returns the number
         * of textures that are being rendered into.  Normally, the textures would be
         * associated with different buffers - a color texture, a depth texture, and a
         * stencil texture.
         */
        """
        pass

    def count_textures(self, GraphicsOutput_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        count_textures(GraphicsOutput self)
        
        /**
         * If the GraphicsOutput is set to render into a texture, returns the number
         * of textures that are being rendered into.  Normally, the textures would be
         * associated with different buffers - a color texture, a depth texture, and a
         * stencil texture.
         */
        """
        pass

    def flipReady(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        flip_ready(GraphicsOutput self)
        
        // These are not intended to be called directly by the user, but they're
        // published anyway since they might occasionally be useful for low-level
        // debugging.
        
        /**
         * Returns true if a frame has been rendered and needs to be flipped, false
         * otherwise.
         */
        """
        pass

    def flip_ready(self, GraphicsOutput_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        flip_ready(GraphicsOutput self)
        
        // These are not intended to be called directly by the user, but they're
        // published anyway since they might occasionally be useful for low-level
        // debugging.
        
        /**
         * Returns true if a frame has been rendered and needs to be flipped, false
         * otherwise.
         */
        """
        pass

    def getActiveDisplayRegion(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_active_display_region(GraphicsOutput self, int n)
        
        /**
         * Returns the nth active DisplayRegion of those that have been created within
         * the window.  This may return NULL if n is out of bounds; particularly
         * likely if the number of display regions has changed since the last call to
         * get_num_active_display_regions().
         */
        """
        pass

    def getActiveDisplayRegions(self, *args, **kwargs): # real signature unknown
        pass

    def getChildSort(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_child_sort(GraphicsOutput self)
        
        /**
         * Returns the sort value of future offscreen buffers created by
         * make_texture_sort(). See set_child_sort().
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getDeleteFlag(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_delete_flag(GraphicsOutput self)
        
        /**
         * Returns the current setting of the delete flag.  When this is true, the
         * GraphicsOutput will automatically be removed before the beginning of the
         * next frame by the GraphicsEngine.
         */
        """
        pass

    def getDisplayRegion(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_display_region(GraphicsOutput self, int n)
        
        /**
         * Returns the nth DisplayRegion of those that have been created within the
         * window.  This may return NULL if n is out of bounds; particularly likely if
         * the number of display regions has changed since the last call to
         * get_num_display_regions().
         */
        """
        pass

    def getDisplayRegions(self, *args, **kwargs): # real signature unknown
        pass

    def getEngine(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_engine(GraphicsOutput self)
        
        /**
         * Returns the graphics engine that created this output.  Since there is
         * normally only one GraphicsEngine object in an application, this is usually
         * the same as the global GraphicsEngine.
         */
        """
        pass

    def getFbProperties(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_fb_properties(GraphicsOutput self)
        
        /**
         * Returns the framebuffer properties of the window.
         */
        """
        pass

    def getFbSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_fb_size(GraphicsOutput self)
        
        /**
         * Returns the internal size of the window or buffer.  This is almost always
         * the same as get_size(), except when a pixel_zoom is in effect--see
         * set_pixel_zoom().
         */
        """
        pass

    def getFbXSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_fb_x_size(GraphicsOutput self)
        
        /**
         * Returns the internal width of the window or buffer.  This is almost always
         * the same as get_x_size(), except when a pixel_zoom is in effect--see
         * set_pixel_zoom().
         */
        """
        pass

    def getFbYSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_fb_y_size(GraphicsOutput self)
        
        /**
         * Returns the internal height of the window or buffer.  This is almost always
         * the same as get_y_size(), except when a pixel_zoom is in effect--see
         * set_pixel_zoom().
         */
        """
        pass

    def getGsg(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_gsg(GraphicsOutput self)
        
        /**
         * Returns the GSG that is associated with this window.  There is a one-to-one
         * association between windows and GSG's.
         *
         * This may return NULL if the graphics context has not yet been created for
         * the window, e.g.  before the first frame has rendered; or after the window
         * has been closed.
         */
        """
        pass

    def getHost(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_host(const GraphicsOutput self)
        
        /**
         * This is normally called only from within make_texture_buffer().  When
         * called on a ParasiteBuffer, it returns the host of that buffer; but when
         * called on some other buffer, it returns the buffer itself.
         */
        """
        pass

    def getInverted(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_inverted(GraphicsOutput self)
        
        /**
         * Returns the current setting of the inverted flag.  When this is true, the
         * scene is rendered into the window upside-down, flipped like a mirror along
         * the X axis.  See set_inverted().
         */
        """
        pass

    def getLeftEyeColorMask(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_left_eye_color_mask(GraphicsOutput self)
        
        /**
         * Returns the color mask in effect when rendering a left-eye view in red_blue
         * stereo mode.  This is one or more bits defined in
         * ColorWriteAttrib::Channels.  See set_red_blue_stereo().
         */
        """
        pass

    def getName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_name(GraphicsOutput self)
        
        /**
         * Returns the name that was passed to the GraphicsOutput constructor.
         */
        """
        pass

    def getNumActiveDisplayRegions(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_active_display_regions(GraphicsOutput self)
        
        /**
         * Returns the number of active DisplayRegions that have been created within
         * the window.
         */
        """
        pass

    def getNumDisplayRegions(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_display_regions(GraphicsOutput self)
        
        /**
         * Returns the number of DisplayRegions that have been created within the
         * window, active or otherwise.
         */
        """
        pass

    def getOneShot(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_one_shot(GraphicsOutput self)
        
        /**
         * Returns the current setting of the one-shot flag.  When this is true, the
         * GraphicsOutput will automatically set itself inactive after the next frame.
         */
        """
        pass

    def getOverlayDisplayRegion(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_overlay_display_region(GraphicsOutput self)
        
        /**
         * Returns the special "overlay" DisplayRegion that is created for each window
         * or buffer.  This DisplayRegion covers the entire window, but cannot be used
         * for rendering.  It is a placeholder only, to indicate the dimensions of the
         * window, and is usually used internally for purposes such as clearing the
         * window, or grabbing a screenshot of the window.
         *
         * There are very few applications that require access to this DisplayRegion.
         * Normally, you should create your own DisplayRegion that covers the window,
         * if you want to render to the window.
         */
        """
        pass

    def getPipe(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_pipe(GraphicsOutput self)
        
        /**
         * Returns the GraphicsPipe that this window is associated with.  It is
         * possible that the GraphicsPipe might have been deleted while an outstanding
         * PT(GraphicsOutput) prevented all of its children windows from also being
         * deleted; in this unlikely case, get_pipe() may return NULL.
         */
        """
        pass

    def getRedBlueStereo(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_red_blue_stereo(GraphicsOutput self)
        
        /**
         * Returns whether red-blue stereo mode is in effect for this particular
         * window.  See set_red_blue_stereo().
         */
        """
        pass

    def getRightEyeColorMask(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_right_eye_color_mask(GraphicsOutput self)
        
        /**
         * Returns the color mask in effect when rendering a right-eye view in
         * red_blue stereo mode.  This is one or more bits defined in
         * ColorWriteAttrib::Channels.  See set_red_blue_stereo().
         */
        """
        pass

    def getRtmMode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_rtm_mode(GraphicsOutput self, int i)
        
        /**
         * Returns the RenderTextureMode associated with the nth render-texture.
         * Returns RTM_none if there is no such texture.
         */
        """
        pass

    def getSbsLeftDimensions(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_sbs_left_dimensions(GraphicsOutput self)
        
        /**
         * Returns the effective sub-region of the window for displaying the left
         * channel, if side-by-side stereo mode is in effect for the window.  See
         * set_side_by_side_stereo().
         */
        """
        pass

    def getSbsLeftSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_sbs_left_size(GraphicsOutput self)
        
        /**
         * If side-by-side stereo is enabled, this returns the pixel size of the left
         * eye, based on scaling get_size() by get_sbs_left_dimensions().  If side-by-
         * side stereo is not enabled, this returns the same as get_size().
         */
        """
        pass

    def getSbsLeftXSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_sbs_left_x_size(GraphicsOutput self)
        
        /**
         * If side-by-side stereo is enabled, this returns the pixel width of the left
         * eye, based on scaling get_x_size() by get_sbs_left_dimensions().  If side-
         * by-side stereo is not enabled, this returns the same as get_x_size().
         */
        """
        pass

    def getSbsLeftYSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_sbs_left_y_size(GraphicsOutput self)
        
        /**
         * If side-by-side stereo is enabled, this returns the pixel height of the
         * left eye, based on scaling get_y_size() by get_sbs_left_dimensions().  If
         * side-by-side stereo is not enabled, this returns the same as get_y_size().
         */
        """
        pass

    def getSbsRightDimensions(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_sbs_right_dimensions(GraphicsOutput self)
        
        /**
         * Returns the effective sub-region of the window for displaying the right
         * channel, if side-by-side stereo mode is in effect for the window.  See
         * set_side_by_side_stereo().
         */
        """
        pass

    def getSbsRightSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_sbs_right_size(GraphicsOutput self)
        
        /**
         * If side-by-side stereo is enabled, this returns the pixel size of the right
         * eye, based on scaling get_size() by get_sbs_right_dimensions().  If side-
         * by-side stereo is not enabled, this returns the same as get_size().
         */
        """
        pass

    def getSbsRightXSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_sbs_right_x_size(GraphicsOutput self)
        
        /**
         * If side-by-side stereo is enabled, this returns the pixel width of the
         * right eye, based on scaling get_x_size() by get_sbs_right_dimensions().  If
         * side-by-side stereo is not enabled, this returns the same as get_x_size().
         */
        """
        pass

    def getSbsRightYSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_sbs_right_y_size(GraphicsOutput self)
        
        /**
         * If side-by-side stereo is enabled, this returns the pixel height of the
         * right eye, based on scaling get_y_size() by get_sbs_right_dimensions().  If
         * side-by-side stereo is not enabled, this returns the same as get_y_size().
         */
        """
        pass

    def getScreenshot(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_screenshot(const GraphicsOutput self)
        get_screenshot(const GraphicsOutput self, PNMImage image)
        
        /**
         * Captures the most-recently rendered image from the framebuffer into the
         * indicated PNMImage.  Returns true on success, false on failure.
         */
        
        /**
         * Captures the most-recently rendered image from the framebuffer and returns
         * it as Texture, or NULL on failure.
         */
        """
        pass

    def getSideBySideStereo(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_side_by_side_stereo(GraphicsOutput self)
        
        /**
         * Returns whether side-by-side stereo mode is in effect for this particular
         * window.  See set_side_by_side_stereo().
         */
        """
        pass

    def getSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_size(GraphicsOutput self)
        
        /**
         * Returns the visible size of the window or buffer, if it is known.  In
         * certain cases (e.g.  fullscreen windows), the size may not be known until
         * after the object has been fully created.  Check has_size() first.
         *
         * Certain objects (like windows) may change size spontaneously; this method
         * is not thread-safe.  To get the size of a window in a thread-safe manner,
         * query get_properties().
         */
        """
        pass

    def getSort(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_sort(GraphicsOutput self)
        
        /**
         * Returns the sorting order of this particular GraphicsOutput.  The various
         * GraphicsOutputs within a particular thread will be rendered in the
         * indicated order.
         */
        """
        pass

    def getSupportsRenderTexture(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_supports_render_texture(GraphicsOutput self)
        
        /**
         * Returns true if this particular GraphicsOutput can render directly into a
         * texture, or false if it must always copy-to-texture at the end of each
         * frame to achieve this effect.
         */
        """
        pass

    def getSwapEyes(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_swap_eyes(GraphicsOutput self)
        
        /**
         * Returns the current setting of the "swap eyes" flag.  See set_swap_eyes().
         */
        """
        pass

    def getTexture(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_texture(GraphicsOutput self, int i)
        
        /**
         * Returns the nth texture into which the GraphicsOutput renders.  Returns
         * NULL if there is no such texture.
         *
         * If the texture is non-NULL, it may be applied to geometry to be rendered
         * for any other windows or outputs that share the same GSG as this
         * GraphicsOutput.  The effect is undefined for windows that share a different
         * GSG; usually in these cases the texture will be invalid.
         */
        """
        pass

    def getTextureCard(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_texture_card(const GraphicsOutput self)
        
        /**
         * Returns a PandaNode containing a square polygon.  The dimensions are
         * (-1,0,-1) to (1,0,1). The texture coordinates are such that the texture of
         * this GraphicsOutput is aligned properly to the polygon.  The GraphicsOutput
         * promises to surgically update the Geom inside the PandaNode if necessary to
         * maintain this invariant.
         *
         * Each invocation of this function returns a freshly- allocated PandaNode.
         * You can therefore safely modify the RenderAttribs of the PandaNode.  The
         * PandaNode is initially textured with the texture of this GraphicOutput.
         */
        """
        pass

    def getTexturePlane(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_texture_plane(GraphicsOutput self, int i)
        
        /**
         * Returns the RenderTexturePlane associated with the nth render-texture.
         * Returns 0 if there is no such texture.
         */
        """
        pass

    def getXSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_x_size(GraphicsOutput self)
        
        /**
         * Returns the visible width of the window or buffer, if it is known.  In
         * certain cases (e.g.  fullscreen windows), the size may not be known until
         * after the object has been fully created.  Check has_size() first.
         *
         * Certain objects (like windows) may change size spontaneously; this method
         * is not thread-safe.  To get the size of a window in a thread-safe manner,
         * query get_properties().
         */
        """
        pass

    def getYSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_y_size(GraphicsOutput self)
        
        /**
         * Returns the visible height of the window or buffer, if it is known.  In
         * certain cases (e.g.  fullscreen windows), the size may not be known until
         * after the object has been fully created.  Check has_size() first.
         *
         * Certain objects (like windows) may change size spontaneously; this method
         * is not thread-safe.  To get the size of a window in a thread-safe manner,
         * query get_properties().
         */
        """
        pass

    def get_active_display_region(self, GraphicsOutput_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_active_display_region(GraphicsOutput self, int n)
        
        /**
         * Returns the nth active DisplayRegion of those that have been created within
         * the window.  This may return NULL if n is out of bounds; particularly
         * likely if the number of display regions has changed since the last call to
         * get_num_active_display_regions().
         */
        """
        pass

    def get_active_display_regions(self, *args, **kwargs): # real signature unknown
        pass

    def get_child_sort(self, GraphicsOutput_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_child_sort(GraphicsOutput self)
        
        /**
         * Returns the sort value of future offscreen buffers created by
         * make_texture_sort(). See set_child_sort().
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_delete_flag(self, GraphicsOutput_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_delete_flag(GraphicsOutput self)
        
        /**
         * Returns the current setting of the delete flag.  When this is true, the
         * GraphicsOutput will automatically be removed before the beginning of the
         * next frame by the GraphicsEngine.
         */
        """
        pass

    def get_display_region(self, GraphicsOutput_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_display_region(GraphicsOutput self, int n)
        
        /**
         * Returns the nth DisplayRegion of those that have been created within the
         * window.  This may return NULL if n is out of bounds; particularly likely if
         * the number of display regions has changed since the last call to
         * get_num_display_regions().
         */
        """
        pass

    def get_display_regions(self, *args, **kwargs): # real signature unknown
        pass

    def get_engine(self, GraphicsOutput_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_engine(GraphicsOutput self)
        
        /**
         * Returns the graphics engine that created this output.  Since there is
         * normally only one GraphicsEngine object in an application, this is usually
         * the same as the global GraphicsEngine.
         */
        """
        pass

    def get_fb_properties(self, GraphicsOutput_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_fb_properties(GraphicsOutput self)
        
        /**
         * Returns the framebuffer properties of the window.
         */
        """
        pass

    def get_fb_size(self, GraphicsOutput_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_fb_size(GraphicsOutput self)
        
        /**
         * Returns the internal size of the window or buffer.  This is almost always
         * the same as get_size(), except when a pixel_zoom is in effect--see
         * set_pixel_zoom().
         */
        """
        pass

    def get_fb_x_size(self, GraphicsOutput_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_fb_x_size(GraphicsOutput self)
        
        /**
         * Returns the internal width of the window or buffer.  This is almost always
         * the same as get_x_size(), except when a pixel_zoom is in effect--see
         * set_pixel_zoom().
         */
        """
        pass

    def get_fb_y_size(self, GraphicsOutput_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_fb_y_size(GraphicsOutput self)
        
        /**
         * Returns the internal height of the window or buffer.  This is almost always
         * the same as get_y_size(), except when a pixel_zoom is in effect--see
         * set_pixel_zoom().
         */
        """
        pass

    def get_gsg(self, GraphicsOutput_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_gsg(GraphicsOutput self)
        
        /**
         * Returns the GSG that is associated with this window.  There is a one-to-one
         * association between windows and GSG's.
         *
         * This may return NULL if the graphics context has not yet been created for
         * the window, e.g.  before the first frame has rendered; or after the window
         * has been closed.
         */
        """
        pass

    def get_host(self, const_GraphicsOutput_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_host(const GraphicsOutput self)
        
        /**
         * This is normally called only from within make_texture_buffer().  When
         * called on a ParasiteBuffer, it returns the host of that buffer; but when
         * called on some other buffer, it returns the buffer itself.
         */
        """
        pass

    def get_inverted(self, GraphicsOutput_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_inverted(GraphicsOutput self)
        
        /**
         * Returns the current setting of the inverted flag.  When this is true, the
         * scene is rendered into the window upside-down, flipped like a mirror along
         * the X axis.  See set_inverted().
         */
        """
        pass

    def get_left_eye_color_mask(self, GraphicsOutput_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_left_eye_color_mask(GraphicsOutput self)
        
        /**
         * Returns the color mask in effect when rendering a left-eye view in red_blue
         * stereo mode.  This is one or more bits defined in
         * ColorWriteAttrib::Channels.  See set_red_blue_stereo().
         */
        """
        pass

    def get_name(self, GraphicsOutput_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_name(GraphicsOutput self)
        
        /**
         * Returns the name that was passed to the GraphicsOutput constructor.
         */
        """
        pass

    def get_num_active_display_regions(self, GraphicsOutput_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_active_display_regions(GraphicsOutput self)
        
        /**
         * Returns the number of active DisplayRegions that have been created within
         * the window.
         */
        """
        pass

    def get_num_display_regions(self, GraphicsOutput_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_display_regions(GraphicsOutput self)
        
        /**
         * Returns the number of DisplayRegions that have been created within the
         * window, active or otherwise.
         */
        """
        pass

    def get_one_shot(self, GraphicsOutput_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_one_shot(GraphicsOutput self)
        
        /**
         * Returns the current setting of the one-shot flag.  When this is true, the
         * GraphicsOutput will automatically set itself inactive after the next frame.
         */
        """
        pass

    def get_overlay_display_region(self, GraphicsOutput_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_overlay_display_region(GraphicsOutput self)
        
        /**
         * Returns the special "overlay" DisplayRegion that is created for each window
         * or buffer.  This DisplayRegion covers the entire window, but cannot be used
         * for rendering.  It is a placeholder only, to indicate the dimensions of the
         * window, and is usually used internally for purposes such as clearing the
         * window, or grabbing a screenshot of the window.
         *
         * There are very few applications that require access to this DisplayRegion.
         * Normally, you should create your own DisplayRegion that covers the window,
         * if you want to render to the window.
         */
        """
        pass

    def get_pipe(self, GraphicsOutput_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_pipe(GraphicsOutput self)
        
        /**
         * Returns the GraphicsPipe that this window is associated with.  It is
         * possible that the GraphicsPipe might have been deleted while an outstanding
         * PT(GraphicsOutput) prevented all of its children windows from also being
         * deleted; in this unlikely case, get_pipe() may return NULL.
         */
        """
        pass

    def get_red_blue_stereo(self, GraphicsOutput_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_red_blue_stereo(GraphicsOutput self)
        
        /**
         * Returns whether red-blue stereo mode is in effect for this particular
         * window.  See set_red_blue_stereo().
         */
        """
        pass

    def get_right_eye_color_mask(self, GraphicsOutput_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_right_eye_color_mask(GraphicsOutput self)
        
        /**
         * Returns the color mask in effect when rendering a right-eye view in
         * red_blue stereo mode.  This is one or more bits defined in
         * ColorWriteAttrib::Channels.  See set_red_blue_stereo().
         */
        """
        pass

    def get_rtm_mode(self, GraphicsOutput_self, int_i): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_rtm_mode(GraphicsOutput self, int i)
        
        /**
         * Returns the RenderTextureMode associated with the nth render-texture.
         * Returns RTM_none if there is no such texture.
         */
        """
        pass

    def get_sbs_left_dimensions(self, GraphicsOutput_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_sbs_left_dimensions(GraphicsOutput self)
        
        /**
         * Returns the effective sub-region of the window for displaying the left
         * channel, if side-by-side stereo mode is in effect for the window.  See
         * set_side_by_side_stereo().
         */
        """
        pass

    def get_sbs_left_size(self, GraphicsOutput_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_sbs_left_size(GraphicsOutput self)
        
        /**
         * If side-by-side stereo is enabled, this returns the pixel size of the left
         * eye, based on scaling get_size() by get_sbs_left_dimensions().  If side-by-
         * side stereo is not enabled, this returns the same as get_size().
         */
        """
        pass

    def get_sbs_left_x_size(self, GraphicsOutput_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_sbs_left_x_size(GraphicsOutput self)
        
        /**
         * If side-by-side stereo is enabled, this returns the pixel width of the left
         * eye, based on scaling get_x_size() by get_sbs_left_dimensions().  If side-
         * by-side stereo is not enabled, this returns the same as get_x_size().
         */
        """
        pass

    def get_sbs_left_y_size(self, GraphicsOutput_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_sbs_left_y_size(GraphicsOutput self)
        
        /**
         * If side-by-side stereo is enabled, this returns the pixel height of the
         * left eye, based on scaling get_y_size() by get_sbs_left_dimensions().  If
         * side-by-side stereo is not enabled, this returns the same as get_y_size().
         */
        """
        pass

    def get_sbs_right_dimensions(self, GraphicsOutput_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_sbs_right_dimensions(GraphicsOutput self)
        
        /**
         * Returns the effective sub-region of the window for displaying the right
         * channel, if side-by-side stereo mode is in effect for the window.  See
         * set_side_by_side_stereo().
         */
        """
        pass

    def get_sbs_right_size(self, GraphicsOutput_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_sbs_right_size(GraphicsOutput self)
        
        /**
         * If side-by-side stereo is enabled, this returns the pixel size of the right
         * eye, based on scaling get_size() by get_sbs_right_dimensions().  If side-
         * by-side stereo is not enabled, this returns the same as get_size().
         */
        """
        pass

    def get_sbs_right_x_size(self, GraphicsOutput_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_sbs_right_x_size(GraphicsOutput self)
        
        /**
         * If side-by-side stereo is enabled, this returns the pixel width of the
         * right eye, based on scaling get_x_size() by get_sbs_right_dimensions().  If
         * side-by-side stereo is not enabled, this returns the same as get_x_size().
         */
        """
        pass

    def get_sbs_right_y_size(self, GraphicsOutput_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_sbs_right_y_size(GraphicsOutput self)
        
        /**
         * If side-by-side stereo is enabled, this returns the pixel height of the
         * right eye, based on scaling get_y_size() by get_sbs_right_dimensions().  If
         * side-by-side stereo is not enabled, this returns the same as get_y_size().
         */
        """
        pass

    def get_screenshot(self, const_GraphicsOutput_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_screenshot(const GraphicsOutput self)
        get_screenshot(const GraphicsOutput self, PNMImage image)
        
        /**
         * Captures the most-recently rendered image from the framebuffer into the
         * indicated PNMImage.  Returns true on success, false on failure.
         */
        
        /**
         * Captures the most-recently rendered image from the framebuffer and returns
         * it as Texture, or NULL on failure.
         */
        """
        pass

    def get_side_by_side_stereo(self, GraphicsOutput_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_side_by_side_stereo(GraphicsOutput self)
        
        /**
         * Returns whether side-by-side stereo mode is in effect for this particular
         * window.  See set_side_by_side_stereo().
         */
        """
        pass

    def get_size(self, GraphicsOutput_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_size(GraphicsOutput self)
        
        /**
         * Returns the visible size of the window or buffer, if it is known.  In
         * certain cases (e.g.  fullscreen windows), the size may not be known until
         * after the object has been fully created.  Check has_size() first.
         *
         * Certain objects (like windows) may change size spontaneously; this method
         * is not thread-safe.  To get the size of a window in a thread-safe manner,
         * query get_properties().
         */
        """
        pass

    def get_sort(self, GraphicsOutput_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_sort(GraphicsOutput self)
        
        /**
         * Returns the sorting order of this particular GraphicsOutput.  The various
         * GraphicsOutputs within a particular thread will be rendered in the
         * indicated order.
         */
        """
        pass

    def get_supports_render_texture(self, GraphicsOutput_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_supports_render_texture(GraphicsOutput self)
        
        /**
         * Returns true if this particular GraphicsOutput can render directly into a
         * texture, or false if it must always copy-to-texture at the end of each
         * frame to achieve this effect.
         */
        """
        pass

    def get_swap_eyes(self, GraphicsOutput_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_swap_eyes(GraphicsOutput self)
        
        /**
         * Returns the current setting of the "swap eyes" flag.  See set_swap_eyes().
         */
        """
        pass

    def get_texture(self, GraphicsOutput_self, int_i): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_texture(GraphicsOutput self, int i)
        
        /**
         * Returns the nth texture into which the GraphicsOutput renders.  Returns
         * NULL if there is no such texture.
         *
         * If the texture is non-NULL, it may be applied to geometry to be rendered
         * for any other windows or outputs that share the same GSG as this
         * GraphicsOutput.  The effect is undefined for windows that share a different
         * GSG; usually in these cases the texture will be invalid.
         */
        """
        pass

    def get_texture_card(self, const_GraphicsOutput_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_texture_card(const GraphicsOutput self)
        
        /**
         * Returns a PandaNode containing a square polygon.  The dimensions are
         * (-1,0,-1) to (1,0,1). The texture coordinates are such that the texture of
         * this GraphicsOutput is aligned properly to the polygon.  The GraphicsOutput
         * promises to surgically update the Geom inside the PandaNode if necessary to
         * maintain this invariant.
         *
         * Each invocation of this function returns a freshly- allocated PandaNode.
         * You can therefore safely modify the RenderAttribs of the PandaNode.  The
         * PandaNode is initially textured with the texture of this GraphicOutput.
         */
        """
        pass

    def get_texture_plane(self, GraphicsOutput_self, int_i): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_texture_plane(GraphicsOutput self, int i)
        
        /**
         * Returns the RenderTexturePlane associated with the nth render-texture.
         * Returns 0 if there is no such texture.
         */
        """
        pass

    def get_x_size(self, GraphicsOutput_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_x_size(GraphicsOutput self)
        
        /**
         * Returns the visible width of the window or buffer, if it is known.  In
         * certain cases (e.g.  fullscreen windows), the size may not be known until
         * after the object has been fully created.  Check has_size() first.
         *
         * Certain objects (like windows) may change size spontaneously; this method
         * is not thread-safe.  To get the size of a window in a thread-safe manner,
         * query get_properties().
         */
        """
        pass

    def get_y_size(self, GraphicsOutput_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_y_size(GraphicsOutput self)
        
        /**
         * Returns the visible height of the window or buffer, if it is known.  In
         * certain cases (e.g.  fullscreen windows), the size may not be known until
         * after the object has been fully created.  Check has_size() first.
         *
         * Certain objects (like windows) may change size spontaneously; this method
         * is not thread-safe.  To get the size of a window in a thread-safe manner,
         * query get_properties().
         */
        """
        pass

    def hasSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_size(GraphicsOutput self)
        
        /**
         * Returns true if the size of the window/frame buffer is known, false
         * otherwise.  In certain cases the size may not be known until after the
         * object has been fully created.  Also, certain objects (like windows) may
         * change size spontaneously.
         */
        """
        pass

    def hasTexture(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_texture(GraphicsOutput self)
        
        /**
         * Returns true if the GraphicsOutput is rendering into any textures at all.
         */
        """
        pass

    def has_size(self, GraphicsOutput_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_size(GraphicsOutput self)
        
        /**
         * Returns true if the size of the window/frame buffer is known, false
         * otherwise.  In certain cases the size may not be known until after the
         * object has been fully created.  Also, certain objects (like windows) may
         * change size spontaneously.
         */
        """
        pass

    def has_texture(self, GraphicsOutput_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_texture(GraphicsOutput self)
        
        /**
         * Returns true if the GraphicsOutput is rendering into any textures at all.
         */
        """
        pass

    def isActive(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_active(GraphicsOutput self)
        
        /**
         * Returns true if the window is ready to be rendered into, false otherwise.
         */
        """
        pass

    def isNonzeroSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_nonzero_size(GraphicsOutput self)
        
        /**
         * Returns true if the output has a nonzero size in both X and Y, or false if
         * it is zero (and therefore invalid).
         */
        """
        pass

    def isStereo(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_stereo(GraphicsOutput self)
        
        /**
         * Returns Returns true if this window can render stereo DisplayRegions,
         * either through red-blue stereo (see set_red_blue_stereo()) or through true
         * hardware stereo rendering.
         */
        """
        pass

    def isValid(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_valid(GraphicsOutput self)
        
        /**
         * Returns true if the output is fully created and ready for rendering, false
         * otherwise.
         */
        """
        pass

    def is_active(self, GraphicsOutput_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_active(GraphicsOutput self)
        
        /**
         * Returns true if the window is ready to be rendered into, false otherwise.
         */
        """
        pass

    def is_nonzero_size(self, GraphicsOutput_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_nonzero_size(GraphicsOutput self)
        
        /**
         * Returns true if the output has a nonzero size in both X and Y, or false if
         * it is zero (and therefore invalid).
         */
        """
        pass

    def is_stereo(self, GraphicsOutput_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_stereo(GraphicsOutput self)
        
        /**
         * Returns Returns true if this window can render stereo DisplayRegions,
         * either through red-blue stereo (see set_red_blue_stereo()) or through true
         * hardware stereo rendering.
         */
        """
        pass

    def is_valid(self, GraphicsOutput_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_valid(GraphicsOutput self)
        
        /**
         * Returns true if the output is fully created and ready for rendering, false
         * otherwise.
         */
        """
        pass

    def makeCubeMap(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_cube_map(const GraphicsOutput self, str name, int size, NodePath camera_rig, BitMask camera_mask, bool to_ram, FrameBufferProperties fbp)
        
        /**
         * This is similar to make_texture_buffer() in that it allocates a separate
         * buffer suitable for rendering to a texture that can be assigned to geometry
         * in this window, but in this case, the buffer is set up to render the six
         * faces of a cube map.
         *
         * The buffer is automatically set up with six display regions and six
         * cameras, each of which are assigned the indicated draw_mask and parented to
         * the given camera_rig node (which you should then put in your scene to
         * render the cube map from the appropriate point of view).
         *
         * You may take the texture associated with the buffer and apply it to
         * geometry, particularly with TexGenAttrib::M_world_cube_map also in effect,
         * to apply a reflection of everything seen by the camera rig.
         */
        """
        pass

    def makeDisplayRegion(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_display_region(const GraphicsOutput self)
        make_display_region(const GraphicsOutput self, const LVecBase4f dimensions)
        make_display_region(const GraphicsOutput self, float l, float r, float b, float t)
        
        /**
         * Creates a new DisplayRegion that covers the entire window.
         *
         * If is_stereo() is true for this window, and default-stereo-camera is
         * configured true, this actually makes a StereoDisplayRegion.  Call
         * make_mono_display_region() or make_stereo_display_region() if you want to
         * insist on one or the other.
         */
        
        /**
         * Creates a new DisplayRegion that covers the indicated sub-rectangle within
         * the window.  The range on all parameters is 0..1.
         *
         * If is_stereo() is true for this window, and default-stereo-camera is
         * configured true, this actually makes a StereoDisplayRegion.  Call
         * make_mono_display_region() or make_stereo_display_region() if you want to
         * insist on one or the other.
         */
        
        /**
         * Creates a new DisplayRegion that covers the indicated sub-rectangle within
         * the window.  The range on all parameters is 0..1.
         *
         * If is_stereo() is true for this window, and default-stereo-camera is
         * configured true, this actually makes a StereoDisplayRegion.  Call
         * make_mono_display_region() or make_stereo_display_region() if you want to
         * insist on one or the other.
         */
        """
        pass

    def makeMonoDisplayRegion(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_mono_display_region(const GraphicsOutput self)
        make_mono_display_region(const GraphicsOutput self, const LVecBase4f dimensions)
        make_mono_display_region(const GraphicsOutput self, float l, float r, float b, float t)
        
        /**
         * Creates a new DisplayRegion that covers the entire window.
         *
         * This generally returns a mono DisplayRegion, even if is_stereo() is true.
         * However, if side-by-side stereo is enabled, this will return a
         * StereoDisplayRegion whose two eyes are both set to SC_mono.  (This is
         * necessary because in side-by-side stereo mode, it is necessary to draw even
         * mono DisplayRegions twice).
         */
        
        /**
         * Creates a new DisplayRegion that covers the entire window.
         *
         * This generally returns a mono DisplayRegion, even if is_stereo() is true.
         * However, if side-by-side stereo is enabled, this will return a
         * StereoDisplayRegion whose two eyes are both set to SC_mono.  (This is
         * necessary because in side-by-side stereo mode, it is necessary to draw even
         * mono DisplayRegions twice).
         */
        
        /**
         * Creates a new DisplayRegion that covers the indicated sub-rectangle within
         * the window.  The range on all parameters is 0..1.
         *
         * This generally returns a mono DisplayRegion, even if is_stereo() is true.
         * However, if side-by-side stereo is enabled, this will return a
         * StereoDisplayRegion whose two eyes are both set to SC_mono.  (This is
         * necessary because in side-by-side stereo mode, it is necessary to draw even
         * mono DisplayRegions twice).
         */
        """
        pass

    def makeScreenshotFilename(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_screenshot_filename(str prefix)
        
        /**
         * Saves a screenshot of the region to a default filename, and returns the
         * filename, or empty string if the screenshot failed.  The default filename
         * is generated from the supplied prefix and from the Config variable
         * screenshot-filename, which contains the following strings:
         *
         * %~p - the supplied prefix %~f - the frame count %~e - the value of
         * screenshot-extension All other % strings in strftime().
         */
        """
        pass

    def makeStereoDisplayRegion(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_stereo_display_region(const GraphicsOutput self)
        make_stereo_display_region(const GraphicsOutput self, const LVecBase4f dimensions)
        make_stereo_display_region(const GraphicsOutput self, float l, float r, float b, float t)
        
        /**
         * Creates a new DisplayRegion that covers the entire window.
         *
         * This always returns a stereo DisplayRegion, even if is_stereo() is false.
         */
        
        /**
         * Creates a new DisplayRegion that covers the entire window.
         *
         * This always returns a stereo DisplayRegion, even if is_stereo() is false.
         */
        
        /**
         * Creates a new DisplayRegion that covers the indicated sub-rectangle within
         * the window.  The range on all parameters is 0..1.
         *
         * This always returns a stereo DisplayRegion, even if is_stereo() is false.
         */
        """
        pass

    def makeTextureBuffer(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_texture_buffer(const GraphicsOutput self, str name, int x_size, int y_size, Texture tex, bool to_ram, FrameBufferProperties fbp)
        
        /**
         * Creates and returns an offscreen buffer for rendering into, the result of
         * which will be a texture suitable for applying to geometry within the scene
         * rendered into this window.
         *
         * If you pass zero as the buffer size, the buffer will have the same size as
         * the host window, and will automatically be resized when the host window is.
         *
         * If tex is not NULL, it is the texture that will be set up for rendering
         * into; otherwise, a new Texture object will be created.  In either case, the
         * target texture can be retrieved from the return value with
         * buffer->get_texture() (assuming the return value is not NULL).
         *
         * If to_ram is true, the buffer will be set up to download its contents to
         * the system RAM memory associated with the Texture object, instead of
         * keeping it strictly within texture memory; this is much slower, but it
         * allows using the texture with any GSG.
         *
         * This will attempt to be smart about maximizing render performance while
         * minimizing framebuffer waste.  It might return a GraphicsBuffer set to
         * render directly into a texture, if possible; or it might return a
         * ParasiteBuffer that renders into this window.  The return value is NULL if
         * the buffer could not be created for some reason.
         *
         * When you are done using the buffer, you should remove it with a call to
         * GraphicsEngine::remove_window().
         */
        """
        pass

    def make_cube_map(self, const_GraphicsOutput_self, str_name, int_size, NodePath_camera_rig, BitMask_camera_mask, bool_to_ram, FrameBufferProperties_fbp): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_cube_map(const GraphicsOutput self, str name, int size, NodePath camera_rig, BitMask camera_mask, bool to_ram, FrameBufferProperties fbp)
        
        /**
         * This is similar to make_texture_buffer() in that it allocates a separate
         * buffer suitable for rendering to a texture that can be assigned to geometry
         * in this window, but in this case, the buffer is set up to render the six
         * faces of a cube map.
         *
         * The buffer is automatically set up with six display regions and six
         * cameras, each of which are assigned the indicated draw_mask and parented to
         * the given camera_rig node (which you should then put in your scene to
         * render the cube map from the appropriate point of view).
         *
         * You may take the texture associated with the buffer and apply it to
         * geometry, particularly with TexGenAttrib::M_world_cube_map also in effect,
         * to apply a reflection of everything seen by the camera rig.
         */
        """
        pass

    def make_display_region(self, const_GraphicsOutput_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_display_region(const GraphicsOutput self)
        make_display_region(const GraphicsOutput self, const LVecBase4f dimensions)
        make_display_region(const GraphicsOutput self, float l, float r, float b, float t)
        
        /**
         * Creates a new DisplayRegion that covers the entire window.
         *
         * If is_stereo() is true for this window, and default-stereo-camera is
         * configured true, this actually makes a StereoDisplayRegion.  Call
         * make_mono_display_region() or make_stereo_display_region() if you want to
         * insist on one or the other.
         */
        
        /**
         * Creates a new DisplayRegion that covers the indicated sub-rectangle within
         * the window.  The range on all parameters is 0..1.
         *
         * If is_stereo() is true for this window, and default-stereo-camera is
         * configured true, this actually makes a StereoDisplayRegion.  Call
         * make_mono_display_region() or make_stereo_display_region() if you want to
         * insist on one or the other.
         */
        
        /**
         * Creates a new DisplayRegion that covers the indicated sub-rectangle within
         * the window.  The range on all parameters is 0..1.
         *
         * If is_stereo() is true for this window, and default-stereo-camera is
         * configured true, this actually makes a StereoDisplayRegion.  Call
         * make_mono_display_region() or make_stereo_display_region() if you want to
         * insist on one or the other.
         */
        """
        pass

    def make_mono_display_region(self, const_GraphicsOutput_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_mono_display_region(const GraphicsOutput self)
        make_mono_display_region(const GraphicsOutput self, const LVecBase4f dimensions)
        make_mono_display_region(const GraphicsOutput self, float l, float r, float b, float t)
        
        /**
         * Creates a new DisplayRegion that covers the entire window.
         *
         * This generally returns a mono DisplayRegion, even if is_stereo() is true.
         * However, if side-by-side stereo is enabled, this will return a
         * StereoDisplayRegion whose two eyes are both set to SC_mono.  (This is
         * necessary because in side-by-side stereo mode, it is necessary to draw even
         * mono DisplayRegions twice).
         */
        
        /**
         * Creates a new DisplayRegion that covers the entire window.
         *
         * This generally returns a mono DisplayRegion, even if is_stereo() is true.
         * However, if side-by-side stereo is enabled, this will return a
         * StereoDisplayRegion whose two eyes are both set to SC_mono.  (This is
         * necessary because in side-by-side stereo mode, it is necessary to draw even
         * mono DisplayRegions twice).
         */
        
        /**
         * Creates a new DisplayRegion that covers the indicated sub-rectangle within
         * the window.  The range on all parameters is 0..1.
         *
         * This generally returns a mono DisplayRegion, even if is_stereo() is true.
         * However, if side-by-side stereo is enabled, this will return a
         * StereoDisplayRegion whose two eyes are both set to SC_mono.  (This is
         * necessary because in side-by-side stereo mode, it is necessary to draw even
         * mono DisplayRegions twice).
         */
        """
        pass

    def make_screenshot_filename(self, str_prefix): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_screenshot_filename(str prefix)
        
        /**
         * Saves a screenshot of the region to a default filename, and returns the
         * filename, or empty string if the screenshot failed.  The default filename
         * is generated from the supplied prefix and from the Config variable
         * screenshot-filename, which contains the following strings:
         *
         * %~p - the supplied prefix %~f - the frame count %~e - the value of
         * screenshot-extension All other % strings in strftime().
         */
        """
        pass

    def make_stereo_display_region(self, const_GraphicsOutput_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_stereo_display_region(const GraphicsOutput self)
        make_stereo_display_region(const GraphicsOutput self, const LVecBase4f dimensions)
        make_stereo_display_region(const GraphicsOutput self, float l, float r, float b, float t)
        
        /**
         * Creates a new DisplayRegion that covers the entire window.
         *
         * This always returns a stereo DisplayRegion, even if is_stereo() is false.
         */
        
        /**
         * Creates a new DisplayRegion that covers the entire window.
         *
         * This always returns a stereo DisplayRegion, even if is_stereo() is false.
         */
        
        /**
         * Creates a new DisplayRegion that covers the indicated sub-rectangle within
         * the window.  The range on all parameters is 0..1.
         *
         * This always returns a stereo DisplayRegion, even if is_stereo() is false.
         */
        """
        pass

    def make_texture_buffer(self, const_GraphicsOutput_self, str_name, int_x_size, int_y_size, Texture_tex, bool_to_ram, FrameBufferProperties_fbp): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_texture_buffer(const GraphicsOutput self, str name, int x_size, int y_size, Texture tex, bool to_ram, FrameBufferProperties fbp)
        
        /**
         * Creates and returns an offscreen buffer for rendering into, the result of
         * which will be a texture suitable for applying to geometry within the scene
         * rendered into this window.
         *
         * If you pass zero as the buffer size, the buffer will have the same size as
         * the host window, and will automatically be resized when the host window is.
         *
         * If tex is not NULL, it is the texture that will be set up for rendering
         * into; otherwise, a new Texture object will be created.  In either case, the
         * target texture can be retrieved from the return value with
         * buffer->get_texture() (assuming the return value is not NULL).
         *
         * If to_ram is true, the buffer will be set up to download its contents to
         * the system RAM memory associated with the Texture object, instead of
         * keeping it strictly within texture memory; this is much slower, but it
         * allows using the texture with any GSG.
         *
         * This will attempt to be smart about maximizing render performance while
         * minimizing framebuffer waste.  It might return a GraphicsBuffer set to
         * render directly into a texture, if possible; or it might return a
         * ParasiteBuffer that renders into this window.  The return value is NULL if
         * the buffer could not be created for some reason.
         *
         * When you are done using the buffer, you should remove it with a call to
         * GraphicsEngine::remove_window().
         */
        """
        pass

    def removeAllDisplayRegions(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_all_display_regions(const GraphicsOutput self)
        
        /**
         * Removes all display regions from the window, except the default one that is
         * created with the window.
         */
        """
        pass

    def removeDisplayRegion(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_display_region(const GraphicsOutput self, DisplayRegion display_region)
        
        /**
         * Removes the indicated DisplayRegion from the window, and destructs it if
         * there are no other references.
         *
         * Returns true if the DisplayRegion is found and removed, false if it was not
         * a part of the window.
         */
        """
        pass

    def remove_all_display_regions(self, const_GraphicsOutput_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_all_display_regions(const GraphicsOutput self)
        
        /**
         * Removes all display regions from the window, except the default one that is
         * created with the window.
         */
        """
        pass

    def remove_display_region(self, const_GraphicsOutput_self, DisplayRegion_display_region): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_display_region(const GraphicsOutput self, DisplayRegion display_region)
        
        /**
         * Removes the indicated DisplayRegion from the window, and destructs it if
         * there are no other references.
         *
         * Returns true if the DisplayRegion is found and removed, false if it was not
         * a part of the window.
         */
        """
        pass

    def saveScreenshot(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        save_screenshot(const GraphicsOutput self, const Filename filename, str image_comment)
        
        /**
         * Saves a screenshot of the region to the indicated filename.  The image
         * comment is an optional user readable string that will be saved with the
         * header of the image (if the file format supports embedded data; for example
         * jpg allows comments).  Returns true on success, false on failure.
         */
        """
        pass

    def saveScreenshotDefault(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        save_screenshot_default(const GraphicsOutput self, str prefix)
        
        /**
         * Saves a screenshot of the region to a default filename, and returns the
         * filename, or empty string if the screenshot failed.  The filename is
         * generated by make_screenshot_filename().
         */
        """
        pass

    def save_screenshot(self, const_GraphicsOutput_self, const_Filename_filename, str_image_comment): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        save_screenshot(const GraphicsOutput self, const Filename filename, str image_comment)
        
        /**
         * Saves a screenshot of the region to the indicated filename.  The image
         * comment is an optional user readable string that will be saved with the
         * header of the image (if the file format supports embedded data; for example
         * jpg allows comments).  Returns true on success, false on failure.
         */
        """
        pass

    def save_screenshot_default(self, const_GraphicsOutput_self, str_prefix): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        save_screenshot_default(const GraphicsOutput self, str prefix)
        
        /**
         * Saves a screenshot of the region to a default filename, and returns the
         * filename, or empty string if the screenshot failed.  The filename is
         * generated by make_screenshot_filename().
         */
        """
        pass

    def setActive(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_active(const GraphicsOutput self, bool active)
        
        /**
         * Sets the active flag associated with the GraphicsOutput.  If the
         * GraphicsOutput is marked inactive, nothing is rendered.
         */
        """
        pass

    def setChildSort(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_child_sort(const GraphicsOutput self, int child_sort)
        
        /**
         * Specifies the sort value of future offscreen buffers created by
         * make_texture_sort().
         *
         * The purpose of this method is to allow the user to limit the sort value
         * chosen for a buffer created via make_texture_buffer().  Normally, this
         * buffer will be assigned a value of get_sort() - 1, so that it will be
         * rendered before this window is rendered; but sometimes this isn't
         * sufficiently early, especially if other buffers also have a view into the
         * same scene.
         *
         * If you specify a value here, then new buffers created via
         * make_texture_buffer() will be given that sort value instead of get_sort() -
         * 1.
         */
        """
        pass

    def setInverted(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_inverted(const GraphicsOutput self, bool inverted)
        
        /**
         * Changes the current setting of the inverted flag.  When this is true, the
         * scene is rendered into the window upside-down and backwards, that is,
         * inverted as if viewed through a mirror placed on the floor.
         *
         * This is primarily intended to support DirectX (and a few buggy OpenGL
         * graphics drivers) that perform a framebuffer-to-texture copy upside-down
         * from the usual OpenGL (and Panda) convention.  Panda will automatically set
         * this flag for offscreen buffers on hardware that is known to do this, to
         * compensate when rendering offscreen into a texture.
         */
        """
        pass

    def setOneShot(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_one_shot(const GraphicsOutput self, bool one_shot)
        
        /**
         * Changes the current setting of the one-shot flag.  When this is true, the
         * GraphicsOutput will render the current frame and then automatically set
         * itself inactive.  This is particularly useful for buffers that are created
         * for the purposes of render-to-texture, for static textures that don't need
         * to be continually re-rendered once they have been rendered the first time.
         *
         * Setting the buffer inactive is not the same thing as destroying it.  You
         * are still responsible for passing this buffer to
         * GraphicsEngine::remove_window() when you no longer need the texture, in
         * order to clean up fully.  (However, you should not call remove_window() on
         * this buffer while the texture is still needed, because depending on the
         * render-to-texture mechanism in use, this may invalidate the texture
         * contents.)
         */
        """
        pass

    def setOverlayDisplayRegion(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_overlay_display_region(const GraphicsOutput self, DisplayRegion display_region)
        
        /**
         * Replaces the special "overlay" DisplayRegion that is created for each
         * window or buffer.  See get_overlay_display_region().  This must be a new
         * DisplayRegion that has already been created for this window, for instance
         * via a call to make_mono_display_region().  You are responsible for ensuring
         * that the new DisplayRegion covers the entire window.  The previous overlay
         * display region is not automatically removed; you must explicitly call
         * remove_display_region() on it after replacing it with this method, if you
         * wish it to be removed.
         *
         * Normally, there is no reason to change the overlay DisplayRegion, so this
         * method should be used only in very unusual circumstances.
         */
        """
        pass

    def setRedBlueStereo(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_red_blue_stereo(const GraphicsOutput self, bool red_blue_stereo, int left_eye_color_mask, int right_eye_color_mask)
        
        /**
         * Enables red-blue stereo mode on this particular window.  When red-blue
         * stereo mode is in effect, DisplayRegions that have the "left" channel set
         * will render in the red (or specified) channel only, while DisplayRegions
         * that have the "right" channel set will render in the blue (or specified)
         * channel only.
         *
         * The remaining two parameters specify the particular color channel(s) to
         * associate with each eye.  Use the bits defined in
         * ColorWriteAttrib::Channels.
         *
         * This can be used to achieve a cheesy stereo mode in the absence of
         * hardware-supported stereo.
         */
        """
        pass

    def setSideBySideStereo(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_side_by_side_stereo(const GraphicsOutput self, bool side_by_side_stereo)
        set_side_by_side_stereo(const GraphicsOutput self, bool side_by_side_stereo, const LVecBase4f sbs_left_dimensions, const LVecBase4f sbs_right_dimensions)
        
        /**
         * Enables side-by-side stereo mode on this particular window.  When side-by-
         * side stereo mode is in effect, DisplayRegions that have the "left" channel
         * set will render on the part of the window specified by sbs_left_dimensions
         * (typically the left half: (0, 0.5, 0, 1)), while DisplayRegions that have
         * the "right" channel set will render on the part of the window specified by
         * sbs_right_dimensions (typically the right half: (0.5, 1, 0, 1)).
         *
         * This is commonly used in a dual-monitor mode, where a window is opened that
         * spans two monitors, and each monitor represents a different eye.
         */
        
        /**
         * Enables side-by-side stereo mode on this particular window.  When side-by-
         * side stereo mode is in effect, DisplayRegions that have the "left" channel
         * set will render on the part of the window specified by sbs_left_dimensions
         * (typically the left half: (0, 0.5, 0, 1)), while DisplayRegions that have
         * the "right" channel set will render on the part of the window specified by
         * sbs_right_dimensions (typically the right half: (0.5, 1, 0, 1)).
         *
         * This is commonly used in a dual-monitor mode, where a window is opened that
         * spans two monitors, and each monitor represents a different eye.
         */
        """
        pass

    def setSort(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_sort(const GraphicsOutput self, int sort)
        
        /**
         * Adjusts the sorting order of this particular GraphicsOutput, relative to
         * other GraphicsOutputs.
         */
        """
        pass

    def setSwapEyes(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_swap_eyes(const GraphicsOutput self, bool swap_eyes)
        
        /**
         * Changes the "swap eyes" flag.  This flag is normally false.  When it is
         * true, the left and right channels of a stereo DisplayRegion are sent to the
         * opposite channels in the rendering backend.  This is meant to work around
         * hardware that inadvertently swaps the output channels, or hardware for
         * which it cannot be determined which channel is which until runtime.
         */
        """
        pass

    def setupRenderTexture(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        setup_render_texture(const GraphicsOutput self, Texture tex, bool allow_bind, bool to_ram)
        
        /**
         * This is a deprecated interface that made sense back when GraphicsOutputs
         * could only render into one texture at a time.  From now on, use
         * clear_render_textures and add_render_texture instead.
         *
         * @deprecated Use add_render_texture() instead.
         */
        """
        pass

    def setup_render_texture(self, const_GraphicsOutput_self, Texture_tex, bool_allow_bind, bool_to_ram): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        setup_render_texture(const GraphicsOutput self, Texture tex, bool allow_bind, bool to_ram)
        
        /**
         * This is a deprecated interface that made sense back when GraphicsOutputs
         * could only render into one texture at a time.  From now on, use
         * clear_render_textures and add_render_texture instead.
         *
         * @deprecated Use add_render_texture() instead.
         */
        """
        pass

    def set_active(self, const_GraphicsOutput_self, bool_active): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_active(const GraphicsOutput self, bool active)
        
        /**
         * Sets the active flag associated with the GraphicsOutput.  If the
         * GraphicsOutput is marked inactive, nothing is rendered.
         */
        """
        pass

    def set_child_sort(self, const_GraphicsOutput_self, int_child_sort): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_child_sort(const GraphicsOutput self, int child_sort)
        
        /**
         * Specifies the sort value of future offscreen buffers created by
         * make_texture_sort().
         *
         * The purpose of this method is to allow the user to limit the sort value
         * chosen for a buffer created via make_texture_buffer().  Normally, this
         * buffer will be assigned a value of get_sort() - 1, so that it will be
         * rendered before this window is rendered; but sometimes this isn't
         * sufficiently early, especially if other buffers also have a view into the
         * same scene.
         *
         * If you specify a value here, then new buffers created via
         * make_texture_buffer() will be given that sort value instead of get_sort() -
         * 1.
         */
        """
        pass

    def set_inverted(self, const_GraphicsOutput_self, bool_inverted): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_inverted(const GraphicsOutput self, bool inverted)
        
        /**
         * Changes the current setting of the inverted flag.  When this is true, the
         * scene is rendered into the window upside-down and backwards, that is,
         * inverted as if viewed through a mirror placed on the floor.
         *
         * This is primarily intended to support DirectX (and a few buggy OpenGL
         * graphics drivers) that perform a framebuffer-to-texture copy upside-down
         * from the usual OpenGL (and Panda) convention.  Panda will automatically set
         * this flag for offscreen buffers on hardware that is known to do this, to
         * compensate when rendering offscreen into a texture.
         */
        """
        pass

    def set_one_shot(self, const_GraphicsOutput_self, bool_one_shot): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_one_shot(const GraphicsOutput self, bool one_shot)
        
        /**
         * Changes the current setting of the one-shot flag.  When this is true, the
         * GraphicsOutput will render the current frame and then automatically set
         * itself inactive.  This is particularly useful for buffers that are created
         * for the purposes of render-to-texture, for static textures that don't need
         * to be continually re-rendered once they have been rendered the first time.
         *
         * Setting the buffer inactive is not the same thing as destroying it.  You
         * are still responsible for passing this buffer to
         * GraphicsEngine::remove_window() when you no longer need the texture, in
         * order to clean up fully.  (However, you should not call remove_window() on
         * this buffer while the texture is still needed, because depending on the
         * render-to-texture mechanism in use, this may invalidate the texture
         * contents.)
         */
        """
        pass

    def set_overlay_display_region(self, const_GraphicsOutput_self, DisplayRegion_display_region): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_overlay_display_region(const GraphicsOutput self, DisplayRegion display_region)
        
        /**
         * Replaces the special "overlay" DisplayRegion that is created for each
         * window or buffer.  See get_overlay_display_region().  This must be a new
         * DisplayRegion that has already been created for this window, for instance
         * via a call to make_mono_display_region().  You are responsible for ensuring
         * that the new DisplayRegion covers the entire window.  The previous overlay
         * display region is not automatically removed; you must explicitly call
         * remove_display_region() on it after replacing it with this method, if you
         * wish it to be removed.
         *
         * Normally, there is no reason to change the overlay DisplayRegion, so this
         * method should be used only in very unusual circumstances.
         */
        """
        pass

    def set_red_blue_stereo(self, const_GraphicsOutput_self, bool_red_blue_stereo, int_left_eye_color_mask, int_right_eye_color_mask): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_red_blue_stereo(const GraphicsOutput self, bool red_blue_stereo, int left_eye_color_mask, int right_eye_color_mask)
        
        /**
         * Enables red-blue stereo mode on this particular window.  When red-blue
         * stereo mode is in effect, DisplayRegions that have the "left" channel set
         * will render in the red (or specified) channel only, while DisplayRegions
         * that have the "right" channel set will render in the blue (or specified)
         * channel only.
         *
         * The remaining two parameters specify the particular color channel(s) to
         * associate with each eye.  Use the bits defined in
         * ColorWriteAttrib::Channels.
         *
         * This can be used to achieve a cheesy stereo mode in the absence of
         * hardware-supported stereo.
         */
        """
        pass

    def set_side_by_side_stereo(self, const_GraphicsOutput_self, bool_side_by_side_stereo): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_side_by_side_stereo(const GraphicsOutput self, bool side_by_side_stereo)
        set_side_by_side_stereo(const GraphicsOutput self, bool side_by_side_stereo, const LVecBase4f sbs_left_dimensions, const LVecBase4f sbs_right_dimensions)
        
        /**
         * Enables side-by-side stereo mode on this particular window.  When side-by-
         * side stereo mode is in effect, DisplayRegions that have the "left" channel
         * set will render on the part of the window specified by sbs_left_dimensions
         * (typically the left half: (0, 0.5, 0, 1)), while DisplayRegions that have
         * the "right" channel set will render on the part of the window specified by
         * sbs_right_dimensions (typically the right half: (0.5, 1, 0, 1)).
         *
         * This is commonly used in a dual-monitor mode, where a window is opened that
         * spans two monitors, and each monitor represents a different eye.
         */
        
        /**
         * Enables side-by-side stereo mode on this particular window.  When side-by-
         * side stereo mode is in effect, DisplayRegions that have the "left" channel
         * set will render on the part of the window specified by sbs_left_dimensions
         * (typically the left half: (0, 0.5, 0, 1)), while DisplayRegions that have
         * the "right" channel set will render on the part of the window specified by
         * sbs_right_dimensions (typically the right half: (0.5, 1, 0, 1)).
         *
         * This is commonly used in a dual-monitor mode, where a window is opened that
         * spans two monitors, and each monitor represents a different eye.
         */
        """
        pass

    def set_sort(self, const_GraphicsOutput_self, int_sort): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_sort(const GraphicsOutput self, int sort)
        
        /**
         * Adjusts the sorting order of this particular GraphicsOutput, relative to
         * other GraphicsOutputs.
         */
        """
        pass

    def set_swap_eyes(self, const_GraphicsOutput_self, bool_swap_eyes): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_swap_eyes(const GraphicsOutput self, bool swap_eyes)
        
        /**
         * Changes the "swap eyes" flag.  This flag is normally false.  When it is
         * true, the left and right channels of a stereo DisplayRegion are sent to the
         * opposite channels in the rendering backend.  This is meant to work around
         * hardware that inadvertently swaps the output channels, or hardware for
         * which it cannot be determined which channel is which until runtime.
         */
        """
        pass

    def shareDepthBuffer(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        share_depth_buffer(const GraphicsOutput self, GraphicsOutput graphics_output)
        
        /**
         * Will attempt to use the depth buffer of the input graphics_output.  The
         * buffer sizes must be exactly the same.
         */
        """
        pass

    def share_depth_buffer(self, const_GraphicsOutput_self, GraphicsOutput_graphics_output): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        share_depth_buffer(const GraphicsOutput self, GraphicsOutput graphics_output)
        
        /**
         * Will attempt to use the depth buffer of the input graphics_output.  The
         * buffer sizes must be exactly the same.
         */
        """
        pass

    def triggerCopy(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        trigger_copy(const GraphicsOutput self)
        
        /**
         * When the GraphicsOutput is in triggered copy mode, this function triggers
         * the copy (at the end of the next frame).
         * @returns a future that can be awaited.
         */
        """
        pass

    def trigger_copy(self, const_GraphicsOutput_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        trigger_copy(const GraphicsOutput self)
        
        /**
         * When the GraphicsOutput is in triggered copy mode, this function triggers
         * the copy (at the end of the next frame).
         * @returns a future that can be awaited.
         */
        """
        pass

    def unshareDepthBuffer(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        unshare_depth_buffer(const GraphicsOutput self)
        
        /**
         * Discontinue sharing the depth buffer.
         */
        """
        pass

    def unshare_depth_buffer(self, const_GraphicsOutput_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        unshare_depth_buffer(const GraphicsOutput self)
        
        /**
         * Discontinue sharing the depth buffer.
         */
        """
        pass

    def upcastToDrawableRegion(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_DrawableRegion(const GraphicsOutput self)
        
        upcast from GraphicsOutput to DrawableRegion
        """
        pass

    def upcastToGraphicsOutputBase(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_GraphicsOutputBase(const GraphicsOutput self)
        
        upcast from GraphicsOutput to GraphicsOutputBase
        """
        pass

    def upcast_to_DrawableRegion(self, const_GraphicsOutput_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_DrawableRegion(const GraphicsOutput self)
        
        upcast from GraphicsOutput to DrawableRegion
        """
        pass

    def upcast_to_GraphicsOutputBase(self, const_GraphicsOutput_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_GraphicsOutputBase(const GraphicsOutput self)
        
        upcast from GraphicsOutput to GraphicsOutputBase
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    active = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    active_display_regions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    child_sort = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    display_regions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    engine = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    fb_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    gsg = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    inverted = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    one_shot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pipe = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    sbs_left_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    sbs_right_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    sort = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    supports_render_texture = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    swap_eyes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        'FMParasite': 1,
        'FMRefresh': 2,
        'FMRender': 0,
        'FM_parasite': 1,
        'FM_refresh': 2,
        'FM_render': 0,
        'RTMBindLayered': 6,
        'RTMBindOrCopy': 1,
        'RTMCopyRam': 3,
        'RTMCopyTexture': 2,
        'RTMNone': 0,
        'RTMTriggeredCopyRam': 5,
        'RTMTriggeredCopyTexture': 4,
        'RTM_bind_layered': 6,
        'RTM_bind_or_copy': 1,
        'RTM_copy_ram': 3,
        'RTM_copy_texture': 2,
        'RTM_none': 0,
        'RTM_triggered_copy_ram': 5,
        'RTM_triggered_copy_texture': 4,
        '__doc__': '/**\n * This is a base class for the various different classes that represent the\n * result of a frame of rendering.  The most common kind of GraphicsOutput is\n * a GraphicsWindow, which is a real-time window on the desktop, but another\n * example is GraphicsBuffer, which is an offscreen buffer.\n *\n * The actual rendering, and anything associated with the graphics context\n * itself, is managed by the associated GraphicsStateGuardian (which might\n * output to multiple GraphicsOutput objects).\n *\n * GraphicsOutputs are not actually writable to bam files, of course, but they\n * may be passed as event parameters, so they inherit from\n * TypedWritableReferenceCount instead of TypedReferenceCount for that\n * convenience.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.GraphicsOutput' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2DD700>'
        'active': None, # (!) real value is "<attribute 'active' of 'panda3d.core.GraphicsOutput' objects>"
        'active_display_regions': None, # (!) real value is "<attribute 'active_display_regions' of 'panda3d.core.GraphicsOutput' objects>"
        'addRenderTexture': None, # (!) real value is "<method 'addRenderTexture' of 'panda3d.core.GraphicsOutput' objects>"
        'add_render_texture': None, # (!) real value is "<method 'add_render_texture' of 'panda3d.core.GraphicsOutput' objects>"
        'child_sort': None, # (!) real value is "<attribute 'child_sort' of 'panda3d.core.GraphicsOutput' objects>"
        'clearChildSort': None, # (!) real value is "<method 'clearChildSort' of 'panda3d.core.GraphicsOutput' objects>"
        'clearDeleteFlag': None, # (!) real value is "<method 'clearDeleteFlag' of 'panda3d.core.GraphicsOutput' objects>"
        'clearRenderTextures': None, # (!) real value is "<method 'clearRenderTextures' of 'panda3d.core.GraphicsOutput' objects>"
        'clear_child_sort': None, # (!) real value is "<method 'clear_child_sort' of 'panda3d.core.GraphicsOutput' objects>"
        'clear_delete_flag': None, # (!) real value is "<method 'clear_delete_flag' of 'panda3d.core.GraphicsOutput' objects>"
        'clear_render_textures': None, # (!) real value is "<method 'clear_render_textures' of 'panda3d.core.GraphicsOutput' objects>"
        'countTextures': None, # (!) real value is "<method 'countTextures' of 'panda3d.core.GraphicsOutput' objects>"
        'count_textures': None, # (!) real value is "<method 'count_textures' of 'panda3d.core.GraphicsOutput' objects>"
        'display_regions': None, # (!) real value is "<attribute 'display_regions' of 'panda3d.core.GraphicsOutput' objects>"
        'engine': None, # (!) real value is "<attribute 'engine' of 'panda3d.core.GraphicsOutput' objects>"
        'fb_size': None, # (!) real value is "<attribute 'fb_size' of 'panda3d.core.GraphicsOutput' objects>"
        'flipReady': None, # (!) real value is "<method 'flipReady' of 'panda3d.core.GraphicsOutput' objects>"
        'flip_ready': None, # (!) real value is "<method 'flip_ready' of 'panda3d.core.GraphicsOutput' objects>"
        'getActiveDisplayRegion': None, # (!) real value is "<method 'getActiveDisplayRegion' of 'panda3d.core.GraphicsOutput' objects>"
        'getActiveDisplayRegions': None, # (!) real value is "<method 'getActiveDisplayRegions' of 'panda3d.core.GraphicsOutput' objects>"
        'getChildSort': None, # (!) real value is "<method 'getChildSort' of 'panda3d.core.GraphicsOutput' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2DD700>)>'
        'getDeleteFlag': None, # (!) real value is "<method 'getDeleteFlag' of 'panda3d.core.GraphicsOutput' objects>"
        'getDisplayRegion': None, # (!) real value is "<method 'getDisplayRegion' of 'panda3d.core.GraphicsOutput' objects>"
        'getDisplayRegions': None, # (!) real value is "<method 'getDisplayRegions' of 'panda3d.core.GraphicsOutput' objects>"
        'getEngine': None, # (!) real value is "<method 'getEngine' of 'panda3d.core.GraphicsOutput' objects>"
        'getFbProperties': None, # (!) real value is "<method 'getFbProperties' of 'panda3d.core.GraphicsOutput' objects>"
        'getFbSize': None, # (!) real value is "<method 'getFbSize' of 'panda3d.core.GraphicsOutput' objects>"
        'getFbXSize': None, # (!) real value is "<method 'getFbXSize' of 'panda3d.core.GraphicsOutput' objects>"
        'getFbYSize': None, # (!) real value is "<method 'getFbYSize' of 'panda3d.core.GraphicsOutput' objects>"
        'getGsg': None, # (!) real value is "<method 'getGsg' of 'panda3d.core.GraphicsOutput' objects>"
        'getHost': None, # (!) real value is "<method 'getHost' of 'panda3d.core.GraphicsOutput' objects>"
        'getInverted': None, # (!) real value is "<method 'getInverted' of 'panda3d.core.GraphicsOutput' objects>"
        'getLeftEyeColorMask': None, # (!) real value is "<method 'getLeftEyeColorMask' of 'panda3d.core.GraphicsOutput' objects>"
        'getName': None, # (!) real value is "<method 'getName' of 'panda3d.core.GraphicsOutput' objects>"
        'getNumActiveDisplayRegions': None, # (!) real value is "<method 'getNumActiveDisplayRegions' of 'panda3d.core.GraphicsOutput' objects>"
        'getNumDisplayRegions': None, # (!) real value is "<method 'getNumDisplayRegions' of 'panda3d.core.GraphicsOutput' objects>"
        'getOneShot': None, # (!) real value is "<method 'getOneShot' of 'panda3d.core.GraphicsOutput' objects>"
        'getOverlayDisplayRegion': None, # (!) real value is "<method 'getOverlayDisplayRegion' of 'panda3d.core.GraphicsOutput' objects>"
        'getPipe': None, # (!) real value is "<method 'getPipe' of 'panda3d.core.GraphicsOutput' objects>"
        'getRedBlueStereo': None, # (!) real value is "<method 'getRedBlueStereo' of 'panda3d.core.GraphicsOutput' objects>"
        'getRightEyeColorMask': None, # (!) real value is "<method 'getRightEyeColorMask' of 'panda3d.core.GraphicsOutput' objects>"
        'getRtmMode': None, # (!) real value is "<method 'getRtmMode' of 'panda3d.core.GraphicsOutput' objects>"
        'getSbsLeftDimensions': None, # (!) real value is "<method 'getSbsLeftDimensions' of 'panda3d.core.GraphicsOutput' objects>"
        'getSbsLeftSize': None, # (!) real value is "<method 'getSbsLeftSize' of 'panda3d.core.GraphicsOutput' objects>"
        'getSbsLeftXSize': None, # (!) real value is "<method 'getSbsLeftXSize' of 'panda3d.core.GraphicsOutput' objects>"
        'getSbsLeftYSize': None, # (!) real value is "<method 'getSbsLeftYSize' of 'panda3d.core.GraphicsOutput' objects>"
        'getSbsRightDimensions': None, # (!) real value is "<method 'getSbsRightDimensions' of 'panda3d.core.GraphicsOutput' objects>"
        'getSbsRightSize': None, # (!) real value is "<method 'getSbsRightSize' of 'panda3d.core.GraphicsOutput' objects>"
        'getSbsRightXSize': None, # (!) real value is "<method 'getSbsRightXSize' of 'panda3d.core.GraphicsOutput' objects>"
        'getSbsRightYSize': None, # (!) real value is "<method 'getSbsRightYSize' of 'panda3d.core.GraphicsOutput' objects>"
        'getScreenshot': None, # (!) real value is "<method 'getScreenshot' of 'panda3d.core.GraphicsOutput' objects>"
        'getSideBySideStereo': None, # (!) real value is "<method 'getSideBySideStereo' of 'panda3d.core.GraphicsOutput' objects>"
        'getSize': None, # (!) real value is "<method 'getSize' of 'panda3d.core.GraphicsOutput' objects>"
        'getSort': None, # (!) real value is "<method 'getSort' of 'panda3d.core.GraphicsOutput' objects>"
        'getSupportsRenderTexture': None, # (!) real value is "<method 'getSupportsRenderTexture' of 'panda3d.core.GraphicsOutput' objects>"
        'getSwapEyes': None, # (!) real value is "<method 'getSwapEyes' of 'panda3d.core.GraphicsOutput' objects>"
        'getTexture': None, # (!) real value is "<method 'getTexture' of 'panda3d.core.GraphicsOutput' objects>"
        'getTextureCard': None, # (!) real value is "<method 'getTextureCard' of 'panda3d.core.GraphicsOutput' objects>"
        'getTexturePlane': None, # (!) real value is "<method 'getTexturePlane' of 'panda3d.core.GraphicsOutput' objects>"
        'getXSize': None, # (!) real value is "<method 'getXSize' of 'panda3d.core.GraphicsOutput' objects>"
        'getYSize': None, # (!) real value is "<method 'getYSize' of 'panda3d.core.GraphicsOutput' objects>"
        'get_active_display_region': None, # (!) real value is "<method 'get_active_display_region' of 'panda3d.core.GraphicsOutput' objects>"
        'get_active_display_regions': None, # (!) real value is "<method 'get_active_display_regions' of 'panda3d.core.GraphicsOutput' objects>"
        'get_child_sort': None, # (!) real value is "<method 'get_child_sort' of 'panda3d.core.GraphicsOutput' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2DD700>)>'
        'get_delete_flag': None, # (!) real value is "<method 'get_delete_flag' of 'panda3d.core.GraphicsOutput' objects>"
        'get_display_region': None, # (!) real value is "<method 'get_display_region' of 'panda3d.core.GraphicsOutput' objects>"
        'get_display_regions': None, # (!) real value is "<method 'get_display_regions' of 'panda3d.core.GraphicsOutput' objects>"
        'get_engine': None, # (!) real value is "<method 'get_engine' of 'panda3d.core.GraphicsOutput' objects>"
        'get_fb_properties': None, # (!) real value is "<method 'get_fb_properties' of 'panda3d.core.GraphicsOutput' objects>"
        'get_fb_size': None, # (!) real value is "<method 'get_fb_size' of 'panda3d.core.GraphicsOutput' objects>"
        'get_fb_x_size': None, # (!) real value is "<method 'get_fb_x_size' of 'panda3d.core.GraphicsOutput' objects>"
        'get_fb_y_size': None, # (!) real value is "<method 'get_fb_y_size' of 'panda3d.core.GraphicsOutput' objects>"
        'get_gsg': None, # (!) real value is "<method 'get_gsg' of 'panda3d.core.GraphicsOutput' objects>"
        'get_host': None, # (!) real value is "<method 'get_host' of 'panda3d.core.GraphicsOutput' objects>"
        'get_inverted': None, # (!) real value is "<method 'get_inverted' of 'panda3d.core.GraphicsOutput' objects>"
        'get_left_eye_color_mask': None, # (!) real value is "<method 'get_left_eye_color_mask' of 'panda3d.core.GraphicsOutput' objects>"
        'get_name': None, # (!) real value is "<method 'get_name' of 'panda3d.core.GraphicsOutput' objects>"
        'get_num_active_display_regions': None, # (!) real value is "<method 'get_num_active_display_regions' of 'panda3d.core.GraphicsOutput' objects>"
        'get_num_display_regions': None, # (!) real value is "<method 'get_num_display_regions' of 'panda3d.core.GraphicsOutput' objects>"
        'get_one_shot': None, # (!) real value is "<method 'get_one_shot' of 'panda3d.core.GraphicsOutput' objects>"
        'get_overlay_display_region': None, # (!) real value is "<method 'get_overlay_display_region' of 'panda3d.core.GraphicsOutput' objects>"
        'get_pipe': None, # (!) real value is "<method 'get_pipe' of 'panda3d.core.GraphicsOutput' objects>"
        'get_red_blue_stereo': None, # (!) real value is "<method 'get_red_blue_stereo' of 'panda3d.core.GraphicsOutput' objects>"
        'get_right_eye_color_mask': None, # (!) real value is "<method 'get_right_eye_color_mask' of 'panda3d.core.GraphicsOutput' objects>"
        'get_rtm_mode': None, # (!) real value is "<method 'get_rtm_mode' of 'panda3d.core.GraphicsOutput' objects>"
        'get_sbs_left_dimensions': None, # (!) real value is "<method 'get_sbs_left_dimensions' of 'panda3d.core.GraphicsOutput' objects>"
        'get_sbs_left_size': None, # (!) real value is "<method 'get_sbs_left_size' of 'panda3d.core.GraphicsOutput' objects>"
        'get_sbs_left_x_size': None, # (!) real value is "<method 'get_sbs_left_x_size' of 'panda3d.core.GraphicsOutput' objects>"
        'get_sbs_left_y_size': None, # (!) real value is "<method 'get_sbs_left_y_size' of 'panda3d.core.GraphicsOutput' objects>"
        'get_sbs_right_dimensions': None, # (!) real value is "<method 'get_sbs_right_dimensions' of 'panda3d.core.GraphicsOutput' objects>"
        'get_sbs_right_size': None, # (!) real value is "<method 'get_sbs_right_size' of 'panda3d.core.GraphicsOutput' objects>"
        'get_sbs_right_x_size': None, # (!) real value is "<method 'get_sbs_right_x_size' of 'panda3d.core.GraphicsOutput' objects>"
        'get_sbs_right_y_size': None, # (!) real value is "<method 'get_sbs_right_y_size' of 'panda3d.core.GraphicsOutput' objects>"
        'get_screenshot': None, # (!) real value is "<method 'get_screenshot' of 'panda3d.core.GraphicsOutput' objects>"
        'get_side_by_side_stereo': None, # (!) real value is "<method 'get_side_by_side_stereo' of 'panda3d.core.GraphicsOutput' objects>"
        'get_size': None, # (!) real value is "<method 'get_size' of 'panda3d.core.GraphicsOutput' objects>"
        'get_sort': None, # (!) real value is "<method 'get_sort' of 'panda3d.core.GraphicsOutput' objects>"
        'get_supports_render_texture': None, # (!) real value is "<method 'get_supports_render_texture' of 'panda3d.core.GraphicsOutput' objects>"
        'get_swap_eyes': None, # (!) real value is "<method 'get_swap_eyes' of 'panda3d.core.GraphicsOutput' objects>"
        'get_texture': None, # (!) real value is "<method 'get_texture' of 'panda3d.core.GraphicsOutput' objects>"
        'get_texture_card': None, # (!) real value is "<method 'get_texture_card' of 'panda3d.core.GraphicsOutput' objects>"
        'get_texture_plane': None, # (!) real value is "<method 'get_texture_plane' of 'panda3d.core.GraphicsOutput' objects>"
        'get_x_size': None, # (!) real value is "<method 'get_x_size' of 'panda3d.core.GraphicsOutput' objects>"
        'get_y_size': None, # (!) real value is "<method 'get_y_size' of 'panda3d.core.GraphicsOutput' objects>"
        'gsg': None, # (!) real value is "<attribute 'gsg' of 'panda3d.core.GraphicsOutput' objects>"
        'hasSize': None, # (!) real value is "<method 'hasSize' of 'panda3d.core.GraphicsOutput' objects>"
        'hasTexture': None, # (!) real value is "<method 'hasTexture' of 'panda3d.core.GraphicsOutput' objects>"
        'has_size': None, # (!) real value is "<method 'has_size' of 'panda3d.core.GraphicsOutput' objects>"
        'has_texture': None, # (!) real value is "<method 'has_texture' of 'panda3d.core.GraphicsOutput' objects>"
        'inverted': None, # (!) real value is "<attribute 'inverted' of 'panda3d.core.GraphicsOutput' objects>"
        'isActive': None, # (!) real value is "<method 'isActive' of 'panda3d.core.GraphicsOutput' objects>"
        'isNonzeroSize': None, # (!) real value is "<method 'isNonzeroSize' of 'panda3d.core.GraphicsOutput' objects>"
        'isStereo': None, # (!) real value is "<method 'isStereo' of 'panda3d.core.GraphicsOutput' objects>"
        'isValid': None, # (!) real value is "<method 'isValid' of 'panda3d.core.GraphicsOutput' objects>"
        'is_active': None, # (!) real value is "<method 'is_active' of 'panda3d.core.GraphicsOutput' objects>"
        'is_nonzero_size': None, # (!) real value is "<method 'is_nonzero_size' of 'panda3d.core.GraphicsOutput' objects>"
        'is_stereo': None, # (!) real value is "<method 'is_stereo' of 'panda3d.core.GraphicsOutput' objects>"
        'is_valid': None, # (!) real value is "<method 'is_valid' of 'panda3d.core.GraphicsOutput' objects>"
        'makeCubeMap': None, # (!) real value is "<method 'makeCubeMap' of 'panda3d.core.GraphicsOutput' objects>"
        'makeDisplayRegion': None, # (!) real value is "<method 'makeDisplayRegion' of 'panda3d.core.GraphicsOutput' objects>"
        'makeMonoDisplayRegion': None, # (!) real value is "<method 'makeMonoDisplayRegion' of 'panda3d.core.GraphicsOutput' objects>"
        'makeScreenshotFilename': None, # (!) real value is '<staticmethod(<built-in method makeScreenshotFilename of type object at 0x00007FFCFE2DD700>)>'
        'makeStereoDisplayRegion': None, # (!) real value is "<method 'makeStereoDisplayRegion' of 'panda3d.core.GraphicsOutput' objects>"
        'makeTextureBuffer': None, # (!) real value is "<method 'makeTextureBuffer' of 'panda3d.core.GraphicsOutput' objects>"
        'make_cube_map': None, # (!) real value is "<method 'make_cube_map' of 'panda3d.core.GraphicsOutput' objects>"
        'make_display_region': None, # (!) real value is "<method 'make_display_region' of 'panda3d.core.GraphicsOutput' objects>"
        'make_mono_display_region': None, # (!) real value is "<method 'make_mono_display_region' of 'panda3d.core.GraphicsOutput' objects>"
        'make_screenshot_filename': None, # (!) real value is '<staticmethod(<built-in method make_screenshot_filename of type object at 0x00007FFCFE2DD700>)>'
        'make_stereo_display_region': None, # (!) real value is "<method 'make_stereo_display_region' of 'panda3d.core.GraphicsOutput' objects>"
        'make_texture_buffer': None, # (!) real value is "<method 'make_texture_buffer' of 'panda3d.core.GraphicsOutput' objects>"
        'name': None, # (!) real value is "<attribute 'name' of 'panda3d.core.GraphicsOutput' objects>"
        'one_shot': None, # (!) real value is "<attribute 'one_shot' of 'panda3d.core.GraphicsOutput' objects>"
        'pipe': None, # (!) real value is "<attribute 'pipe' of 'panda3d.core.GraphicsOutput' objects>"
        'removeAllDisplayRegions': None, # (!) real value is "<method 'removeAllDisplayRegions' of 'panda3d.core.GraphicsOutput' objects>"
        'removeDisplayRegion': None, # (!) real value is "<method 'removeDisplayRegion' of 'panda3d.core.GraphicsOutput' objects>"
        'remove_all_display_regions': None, # (!) real value is "<method 'remove_all_display_regions' of 'panda3d.core.GraphicsOutput' objects>"
        'remove_display_region': None, # (!) real value is "<method 'remove_display_region' of 'panda3d.core.GraphicsOutput' objects>"
        'saveScreenshot': None, # (!) real value is "<method 'saveScreenshot' of 'panda3d.core.GraphicsOutput' objects>"
        'saveScreenshotDefault': None, # (!) real value is "<method 'saveScreenshotDefault' of 'panda3d.core.GraphicsOutput' objects>"
        'save_screenshot': None, # (!) real value is "<method 'save_screenshot' of 'panda3d.core.GraphicsOutput' objects>"
        'save_screenshot_default': None, # (!) real value is "<method 'save_screenshot_default' of 'panda3d.core.GraphicsOutput' objects>"
        'sbs_left_size': None, # (!) real value is "<attribute 'sbs_left_size' of 'panda3d.core.GraphicsOutput' objects>"
        'sbs_right_size': None, # (!) real value is "<attribute 'sbs_right_size' of 'panda3d.core.GraphicsOutput' objects>"
        'setActive': None, # (!) real value is "<method 'setActive' of 'panda3d.core.GraphicsOutput' objects>"
        'setChildSort': None, # (!) real value is "<method 'setChildSort' of 'panda3d.core.GraphicsOutput' objects>"
        'setInverted': None, # (!) real value is "<method 'setInverted' of 'panda3d.core.GraphicsOutput' objects>"
        'setOneShot': None, # (!) real value is "<method 'setOneShot' of 'panda3d.core.GraphicsOutput' objects>"
        'setOverlayDisplayRegion': None, # (!) real value is "<method 'setOverlayDisplayRegion' of 'panda3d.core.GraphicsOutput' objects>"
        'setRedBlueStereo': None, # (!) real value is "<method 'setRedBlueStereo' of 'panda3d.core.GraphicsOutput' objects>"
        'setSideBySideStereo': None, # (!) real value is "<method 'setSideBySideStereo' of 'panda3d.core.GraphicsOutput' objects>"
        'setSort': None, # (!) real value is "<method 'setSort' of 'panda3d.core.GraphicsOutput' objects>"
        'setSwapEyes': None, # (!) real value is "<method 'setSwapEyes' of 'panda3d.core.GraphicsOutput' objects>"
        'set_active': None, # (!) real value is "<method 'set_active' of 'panda3d.core.GraphicsOutput' objects>"
        'set_child_sort': None, # (!) real value is "<method 'set_child_sort' of 'panda3d.core.GraphicsOutput' objects>"
        'set_inverted': None, # (!) real value is "<method 'set_inverted' of 'panda3d.core.GraphicsOutput' objects>"
        'set_one_shot': None, # (!) real value is "<method 'set_one_shot' of 'panda3d.core.GraphicsOutput' objects>"
        'set_overlay_display_region': None, # (!) real value is "<method 'set_overlay_display_region' of 'panda3d.core.GraphicsOutput' objects>"
        'set_red_blue_stereo': None, # (!) real value is "<method 'set_red_blue_stereo' of 'panda3d.core.GraphicsOutput' objects>"
        'set_side_by_side_stereo': None, # (!) real value is "<method 'set_side_by_side_stereo' of 'panda3d.core.GraphicsOutput' objects>"
        'set_sort': None, # (!) real value is "<method 'set_sort' of 'panda3d.core.GraphicsOutput' objects>"
        'set_swap_eyes': None, # (!) real value is "<method 'set_swap_eyes' of 'panda3d.core.GraphicsOutput' objects>"
        'setupRenderTexture': None, # (!) real value is "<method 'setupRenderTexture' of 'panda3d.core.GraphicsOutput' objects>"
        'setup_render_texture': None, # (!) real value is "<method 'setup_render_texture' of 'panda3d.core.GraphicsOutput' objects>"
        'shareDepthBuffer': None, # (!) real value is "<method 'shareDepthBuffer' of 'panda3d.core.GraphicsOutput' objects>"
        'share_depth_buffer': None, # (!) real value is "<method 'share_depth_buffer' of 'panda3d.core.GraphicsOutput' objects>"
        'size': None, # (!) real value is "<attribute 'size' of 'panda3d.core.GraphicsOutput' objects>"
        'sort': None, # (!) real value is "<attribute 'sort' of 'panda3d.core.GraphicsOutput' objects>"
        'supports_render_texture': None, # (!) real value is "<attribute 'supports_render_texture' of 'panda3d.core.GraphicsOutput' objects>"
        'swap_eyes': None, # (!) real value is "<attribute 'swap_eyes' of 'panda3d.core.GraphicsOutput' objects>"
        'triggerCopy': None, # (!) real value is "<method 'triggerCopy' of 'panda3d.core.GraphicsOutput' objects>"
        'trigger_copy': None, # (!) real value is "<method 'trigger_copy' of 'panda3d.core.GraphicsOutput' objects>"
        'unshareDepthBuffer': None, # (!) real value is "<method 'unshareDepthBuffer' of 'panda3d.core.GraphicsOutput' objects>"
        'unshare_depth_buffer': None, # (!) real value is "<method 'unshare_depth_buffer' of 'panda3d.core.GraphicsOutput' objects>"
        'upcastToDrawableRegion': None, # (!) real value is "<method 'upcastToDrawableRegion' of 'panda3d.core.GraphicsOutput' objects>"
        'upcastToGraphicsOutputBase': None, # (!) real value is "<method 'upcastToGraphicsOutputBase' of 'panda3d.core.GraphicsOutput' objects>"
        'upcast_to_DrawableRegion': None, # (!) real value is "<method 'upcast_to_DrawableRegion' of 'panda3d.core.GraphicsOutput' objects>"
        'upcast_to_GraphicsOutputBase': None, # (!) real value is "<method 'upcast_to_GraphicsOutputBase' of 'panda3d.core.GraphicsOutput' objects>"
    }
    FMParasite = 1
    FMRefresh = 2
    FMRender = 0
    FM_parasite = 1
    FM_refresh = 2
    FM_render = 0
    RTMBindLayered = 6
    RTMBindOrCopy = 1
    RTMCopyRam = 3
    RTMCopyTexture = 2
    RTMNone = 0
    RTMTriggeredCopyRam = 5
    RTMTriggeredCopyTexture = 4
    RTM_bind_layered = 6
    RTM_bind_or_copy = 1
    RTM_copy_ram = 3
    RTM_copy_texture = 2
    RTM_none = 0
    RTM_triggered_copy_ram = 5
    RTM_triggered_copy_texture = 4


