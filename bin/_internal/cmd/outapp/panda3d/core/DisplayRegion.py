# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .TypedReferenceCount import TypedReferenceCount

from .DrawableRegion import DrawableRegion

class DisplayRegion(TypedReferenceCount, DrawableRegion):
    """
    /**
     * A rectangular subregion within a window for rendering into.  Typically,
     * there is one DisplayRegion that covers the whole window, but you may also
     * create smaller DisplayRegions for having different regions within the
     * window that represent different scenes.  You may also stack up
     * DisplayRegions like panes of glass, usually for layering 2-d interfaces on
     * top of a 3-d scene.
     */
    """
    def clearCullCallback(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_cull_callback(const DisplayRegion self)
        
        /**
         * Removes the callback set by an earlier call to set_cull_callback().
         */
        """
        pass

    def clearCullResult(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_cull_result(const DisplayRegion self)
        
        /**
         *
         */
        """
        pass

    def clearDrawCallback(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_draw_callback(const DisplayRegion self)
        
        /**
         * Removes the callback set by an earlier call to set_draw_callback().
         */
        """
        pass

    def clear_cull_callback(self, const_DisplayRegion_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_cull_callback(const DisplayRegion self)
        
        /**
         * Removes the callback set by an earlier call to set_cull_callback().
         */
        """
        pass

    def clear_cull_result(self, const_DisplayRegion_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_cull_result(const DisplayRegion self)
        
        /**
         *
         */
        """
        pass

    def clear_draw_callback(self, const_DisplayRegion_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_draw_callback(const DisplayRegion self)
        
        /**
         * Removes the callback set by an earlier call to set_draw_callback().
         */
        """
        pass

    def getBottom(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_bottom(DisplayRegion self, int i)
        
        /**
         * Retrieves the y coordinate of the bottom edge of the rectangle within its
         * GraphicsOutput.  This number will be in the range [0..1].
         */
        """
        pass

    def getCamera(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_camera(DisplayRegion self, Thread current_thread)
        
        /**
         * Returns the camera associated with this DisplayRegion, or an empty NodePath
         * if no camera is associated.
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getCullCallback(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_cull_callback(DisplayRegion self)
        
        /**
         * Returns the CallbackObject set by set_cull_callback().
         */
        """
        pass

    def getCullTraverser(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_cull_traverser(const DisplayRegion self)
        
        /**
         * Returns the CullTraverser that will be used to draw the contents of this
         * DisplayRegion.
         */
        """
        pass

    def getDimensions(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_dimensions(DisplayRegion self, int i)
        
        /**
         * Retrieves the coordinates of the DisplayRegion's rectangle within its
         * GraphicsOutput.  These numbers will be in the range [0..1].
         */
        
        /**
         * Retrieves the coordinates of the DisplayRegion's rectangle within its
         * GraphicsOutput.  These numbers will be in the range [0..1].
         */
        
        /**
         * Retrieves the coordinates of the DisplayRegion's rectangle within its
         * GraphicsOutput.  These numbers will be in the range [0..1].
         */
        """
        pass

    def getDrawCallback(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_draw_callback(DisplayRegion self)
        
        /**
         * Returns the CallbackObject set by set_draw_callback().
         */
        """
        pass

    def getIncompleteRender(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_incomplete_render(DisplayRegion self)
        
        /**
         * Returns the incomplete_render flag.  See set_incomplete_render().
         */
        """
        pass

    def getLeft(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_left(DisplayRegion self, int i)
        
        /**
         * Retrieves the x coordinate of the left edge of the rectangle within its
         * GraphicsOutput.  This number will be in the range [0..1].
         */
        """
        pass

    def getLensIndex(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_lens_index(DisplayRegion self)
        
        /**
         * Returns the specific lens of the associated Camera that will be used for
         * rendering this scene.  Most Cameras hold only one lens, but for multiple
         * lenses this method may be used to selected between them.
         */
        """
        pass

    def getNumRegions(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_regions(DisplayRegion self)
        
        /**
         * Returns the number of regions, see set_num_regions.
         */
        """
        pass

    def getPipe(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_pipe(DisplayRegion self)
        
        /**
         * Returns the GraphicsPipe that this DisplayRegion is ultimately associated
         * with, or NULL if no pipe is associated.
         */
        """
        pass

    def getPixelHeight(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_pixel_height(DisplayRegion self, int i)
        
        /**
         * Returns the height of the DisplayRegion in pixels.
         */
        """
        pass

    def getPixelSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_pixel_size(DisplayRegion self, int i)
        
        /**
         * Returns the size of the DisplayRegion in pixels.
         */
        """
        pass

    def getPixelWidth(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_pixel_width(DisplayRegion self, int i)
        
        /**
         * Returns the width of the DisplayRegion in pixels.
         */
        """
        pass

    def getRight(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_right(DisplayRegion self, int i)
        
        /**
         * Retrieves the x coordinate of the right edge of the rectangle within its
         * GraphicsOutput.  This number will be in the range [0..1].
         */
        """
        pass

    def getScissorEnabled(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_scissor_enabled(DisplayRegion self)
        
        /**
         * Returns whether or not scissor testing is enabled for this region.  The
         * default is true, except for the overlay display region.
         */
        """
        pass

    def getScreenshot(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_screenshot(const DisplayRegion self)
        get_screenshot(const DisplayRegion self, PNMImage image)
        
        /**
         * Captures the most-recently rendered image from the framebuffer into the
         * indicated PNMImage.  Returns true on success, false on failure.
         */
        
        /**
         * Captures the most-recently rendered image from the framebuffer and returns
         * it as a Texture, or NULL on failure.
         */
        """
        pass

    def getSort(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_sort(DisplayRegion self)
        
        /**
         * Returns the sort value associated with the DisplayRegion.
         */
        """
        pass

    def getStereoChannel(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_stereo_channel(DisplayRegion self)
        
        /**
         * Returns whether the DisplayRegion is specified as the left or right channel
         * of a stereo pair, or whether it is a normal, monocular image.  See
         * set_stereo_channel().
         */
        """
        pass

    def getTargetTexPage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_target_tex_page(DisplayRegion self)
        
        /**
         * Returns the target page number associated with this particular
         * DisplayRegion, or -1 if it is not associated with a page.  See
         * set_target_tex_page().
         */
        """
        pass

    def getTextureReloadPriority(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_texture_reload_priority(DisplayRegion self)
        
        /**
         * Returns the priority which is assigned to asynchronous texture reload
         * requests.  See set_texture_reload_priority().
         */
        """
        pass

    def getTexViewOffset(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_tex_view_offset(DisplayRegion self)
        
        /**
         * Returns the current texture view offset for this DisplayRegion.  This is
         * normally set to zero.  If nonzero, it is used to select a particular view
         * of any multiview textures that are rendered within this DisplayRegion.
         *
         * For a StereoDisplayRegion, this is normally 0 for the left eye, and 1 for
         * the right eye, to support stereo textures.
         */
        """
        pass

    def getTop(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_top(DisplayRegion self, int i)
        
        /**
         * Retrieves the y coordinate of the top edge of the rectangle within its
         * GraphicsOutput.  This number will be in the range [0..1].
         */
        """
        pass

    def getWindow(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_window(DisplayRegion self)
        
        /**
         * Returns the GraphicsOutput that this DisplayRegion is ultimately associated
         * with, or NULL if no window is associated.
         */
        """
        pass

    def get_bottom(self, DisplayRegion_self, int_i): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_bottom(DisplayRegion self, int i)
        
        /**
         * Retrieves the y coordinate of the bottom edge of the rectangle within its
         * GraphicsOutput.  This number will be in the range [0..1].
         */
        """
        pass

    def get_camera(self, DisplayRegion_self, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_camera(DisplayRegion self, Thread current_thread)
        
        /**
         * Returns the camera associated with this DisplayRegion, or an empty NodePath
         * if no camera is associated.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_cull_callback(self, DisplayRegion_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_cull_callback(DisplayRegion self)
        
        /**
         * Returns the CallbackObject set by set_cull_callback().
         */
        """
        pass

    def get_cull_traverser(self, const_DisplayRegion_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_cull_traverser(const DisplayRegion self)
        
        /**
         * Returns the CullTraverser that will be used to draw the contents of this
         * DisplayRegion.
         */
        """
        pass

    def get_dimensions(self, DisplayRegion_self, int_i): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_dimensions(DisplayRegion self, int i)
        
        /**
         * Retrieves the coordinates of the DisplayRegion's rectangle within its
         * GraphicsOutput.  These numbers will be in the range [0..1].
         */
        
        /**
         * Retrieves the coordinates of the DisplayRegion's rectangle within its
         * GraphicsOutput.  These numbers will be in the range [0..1].
         */
        
        /**
         * Retrieves the coordinates of the DisplayRegion's rectangle within its
         * GraphicsOutput.  These numbers will be in the range [0..1].
         */
        """
        pass

    def get_draw_callback(self, DisplayRegion_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_draw_callback(DisplayRegion self)
        
        /**
         * Returns the CallbackObject set by set_draw_callback().
         */
        """
        pass

    def get_incomplete_render(self, DisplayRegion_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_incomplete_render(DisplayRegion self)
        
        /**
         * Returns the incomplete_render flag.  See set_incomplete_render().
         */
        """
        pass

    def get_left(self, DisplayRegion_self, int_i): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_left(DisplayRegion self, int i)
        
        /**
         * Retrieves the x coordinate of the left edge of the rectangle within its
         * GraphicsOutput.  This number will be in the range [0..1].
         */
        """
        pass

    def get_lens_index(self, DisplayRegion_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_lens_index(DisplayRegion self)
        
        /**
         * Returns the specific lens of the associated Camera that will be used for
         * rendering this scene.  Most Cameras hold only one lens, but for multiple
         * lenses this method may be used to selected between them.
         */
        """
        pass

    def get_num_regions(self, DisplayRegion_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_regions(DisplayRegion self)
        
        /**
         * Returns the number of regions, see set_num_regions.
         */
        """
        pass

    def get_pipe(self, DisplayRegion_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_pipe(DisplayRegion self)
        
        /**
         * Returns the GraphicsPipe that this DisplayRegion is ultimately associated
         * with, or NULL if no pipe is associated.
         */
        """
        pass

    def get_pixel_height(self, DisplayRegion_self, int_i): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_pixel_height(DisplayRegion self, int i)
        
        /**
         * Returns the height of the DisplayRegion in pixels.
         */
        """
        pass

    def get_pixel_size(self, DisplayRegion_self, int_i): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_pixel_size(DisplayRegion self, int i)
        
        /**
         * Returns the size of the DisplayRegion in pixels.
         */
        """
        pass

    def get_pixel_width(self, DisplayRegion_self, int_i): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_pixel_width(DisplayRegion self, int i)
        
        /**
         * Returns the width of the DisplayRegion in pixels.
         */
        """
        pass

    def get_right(self, DisplayRegion_self, int_i): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_right(DisplayRegion self, int i)
        
        /**
         * Retrieves the x coordinate of the right edge of the rectangle within its
         * GraphicsOutput.  This number will be in the range [0..1].
         */
        """
        pass

    def get_scissor_enabled(self, DisplayRegion_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_scissor_enabled(DisplayRegion self)
        
        /**
         * Returns whether or not scissor testing is enabled for this region.  The
         * default is true, except for the overlay display region.
         */
        """
        pass

    def get_screenshot(self, const_DisplayRegion_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_screenshot(const DisplayRegion self)
        get_screenshot(const DisplayRegion self, PNMImage image)
        
        /**
         * Captures the most-recently rendered image from the framebuffer into the
         * indicated PNMImage.  Returns true on success, false on failure.
         */
        
        /**
         * Captures the most-recently rendered image from the framebuffer and returns
         * it as a Texture, or NULL on failure.
         */
        """
        pass

    def get_sort(self, DisplayRegion_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_sort(DisplayRegion self)
        
        /**
         * Returns the sort value associated with the DisplayRegion.
         */
        """
        pass

    def get_stereo_channel(self, DisplayRegion_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_stereo_channel(DisplayRegion self)
        
        /**
         * Returns whether the DisplayRegion is specified as the left or right channel
         * of a stereo pair, or whether it is a normal, monocular image.  See
         * set_stereo_channel().
         */
        """
        pass

    def get_target_tex_page(self, DisplayRegion_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_target_tex_page(DisplayRegion self)
        
        /**
         * Returns the target page number associated with this particular
         * DisplayRegion, or -1 if it is not associated with a page.  See
         * set_target_tex_page().
         */
        """
        pass

    def get_texture_reload_priority(self, DisplayRegion_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_texture_reload_priority(DisplayRegion self)
        
        /**
         * Returns the priority which is assigned to asynchronous texture reload
         * requests.  See set_texture_reload_priority().
         */
        """
        pass

    def get_tex_view_offset(self, DisplayRegion_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_tex_view_offset(DisplayRegion self)
        
        /**
         * Returns the current texture view offset for this DisplayRegion.  This is
         * normally set to zero.  If nonzero, it is used to select a particular view
         * of any multiview textures that are rendered within this DisplayRegion.
         *
         * For a StereoDisplayRegion, this is normally 0 for the left eye, and 1 for
         * the right eye, to support stereo textures.
         */
        """
        pass

    def get_top(self, DisplayRegion_self, int_i): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_top(DisplayRegion self, int i)
        
        /**
         * Retrieves the y coordinate of the top edge of the rectangle within its
         * GraphicsOutput.  This number will be in the range [0..1].
         */
        """
        pass

    def get_window(self, DisplayRegion_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_window(DisplayRegion self)
        
        /**
         * Returns the GraphicsOutput that this DisplayRegion is ultimately associated
         * with, or NULL if no window is associated.
         */
        """
        pass

    def isActive(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_active(DisplayRegion self)
        
        /**
         * Returns the active flag associated with the DisplayRegion.
         */
        """
        pass

    def isStereo(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_stereo(DisplayRegion self)
        
        /**
         * Returns true if this is a StereoDisplayRegion, false otherwise.
         */
        """
        pass

    def is_active(self, DisplayRegion_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_active(DisplayRegion self)
        
        /**
         * Returns the active flag associated with the DisplayRegion.
         */
        """
        pass

    def is_stereo(self, DisplayRegion_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_stereo(DisplayRegion self)
        
        /**
         * Returns true if this is a StereoDisplayRegion, false otherwise.
         */
        """
        pass

    def makeCullResultGraph(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_cull_result_graph(const DisplayRegion self)
        
        /**
         * Returns a special scene graph constructed to represent the results of the
         * last frame's cull operation.
         *
         * This will be a hierarchy of nodes, one node for each bin, each of which
         * will in term be a parent of a number of GeomNodes, representing the
         * geometry drawn in each bin.
         *
         * This is useful mainly for high-level debugging and abstraction tools; it
         * should not be mistaken for the low-level cull result itself, which is
         * constructed and maintained internally.  No such scene graph is normally
         * constructed during the rendering of a frame; this is an artificial
         * construct created for the purpose of making it easy to analyze the results
         * of the cull operation.
         */
        """
        pass

    def makeScreenshotFilename(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_screenshot_filename(str prefix)
        
        /**
         * Synthesizes a suitable default filename for passing to save_screenshot().
         *
         * The default filename is generated from the supplied prefix and from the
         * Config variable screenshot-filename, which contains the following strings:
         *
         * %~p - the supplied prefix %~f - the frame count %~e - the value of
         * screenshot-extension All other % strings in strftime().
         */
        """
        pass

    def make_cull_result_graph(self, const_DisplayRegion_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_cull_result_graph(const DisplayRegion self)
        
        /**
         * Returns a special scene graph constructed to represent the results of the
         * last frame's cull operation.
         *
         * This will be a hierarchy of nodes, one node for each bin, each of which
         * will in term be a parent of a number of GeomNodes, representing the
         * geometry drawn in each bin.
         *
         * This is useful mainly for high-level debugging and abstraction tools; it
         * should not be mistaken for the low-level cull result itself, which is
         * constructed and maintained internally.  No such scene graph is normally
         * constructed during the rendering of a frame; this is an artificial
         * construct created for the purpose of making it easy to analyze the results
         * of the cull operation.
         */
        """
        pass

    def make_screenshot_filename(self, str_prefix): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_screenshot_filename(str prefix)
        
        /**
         * Synthesizes a suitable default filename for passing to save_screenshot().
         *
         * The default filename is generated from the supplied prefix and from the
         * Config variable screenshot-filename, which contains the following strings:
         *
         * %~p - the supplied prefix %~f - the frame count %~e - the value of
         * screenshot-extension All other % strings in strftime().
         */
        """
        pass

    def output(self, DisplayRegion_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(DisplayRegion self, ostream out)
        
        /**
         *
         */
        """
        pass

    def saveScreenshot(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        save_screenshot(const DisplayRegion self, const Filename filename, str image_comment)
        
        /**
         * Saves a screenshot of the region to the indicated filename.  Returns true
         * on success, false on failure.
         */
        """
        pass

    def saveScreenshotDefault(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        save_screenshot_default(const DisplayRegion self, str prefix)
        
        /**
         * Saves a screenshot of the region to a default filename, and returns the
         * filename, or empty string if the screenshot failed.  The filename is
         * generated by make_screenshot_filename().
         */
        """
        pass

    def save_screenshot(self, const_DisplayRegion_self, const_Filename_filename, str_image_comment): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        save_screenshot(const DisplayRegion self, const Filename filename, str image_comment)
        
        /**
         * Saves a screenshot of the region to the indicated filename.  Returns true
         * on success, false on failure.
         */
        """
        pass

    def save_screenshot_default(self, const_DisplayRegion_self, str_prefix): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        save_screenshot_default(const DisplayRegion self, str prefix)
        
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
        set_active(const DisplayRegion self, bool active)
        
        /**
         * Sets the active flag associated with the DisplayRegion.  If the
         * DisplayRegion is marked inactive, nothing is rendered.
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         */
        """
        pass

    def setCamera(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_camera(const DisplayRegion self, const NodePath camera)
        
        /**
         * Sets the camera that is associated with this DisplayRegion.  There is a
         * one-to-many association between cameras and DisplayRegions; one camera may
         * be shared by multiple DisplayRegions.
         *
         * The camera is actually set via a NodePath, which clarifies which instance
         * of the camera (if there happen to be multiple instances) we should use.
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         */
        """
        pass

    def setCubeMapIndex(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_cube_map_index(const DisplayRegion self, int cube_map_index)
        
        /**
         * Deprecated; replaced by set_target_tex_page().
         */
        """
        pass

    def setCullCallback(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_cull_callback(const DisplayRegion self, CallbackObject object)
        
        /**
         * Sets the CallbackObject that will be notified when the DisplayRegion is
         * visited during the cull traversal.  This callback will be made during the
         * cull thread.
         *
         * The cull traversal is responsible for determining which nodes are visible
         * and within the view frustum, and for accumulating state and transform, and
         * generally building up the list of CullableObjects that are to be eventually
         * passed to the draw traversal for rendering.
         *
         * At the time the cull traversal callback is made, the traversal for this
         * DisplayRegion has not yet started.
         *
         * The callback is passed an instance of a DisplayRegionCullCallbackData,
         * which contains pointers to the current scene information, as well as the
         * current DisplayRegion and GSG.  The callback *replaces* the normal cull
         * behavior, so if your callback does nothing, the scene graph will not be
         * traversed and therefore nothing will be drawn.  If you wish the normal cull
         * traversal to be performed for this DisplayRegion, you must call
         * cbdata->upcall() from your callback.
         */
        """
        pass

    def setCullTraverser(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_cull_traverser(const DisplayRegion self, CullTraverser trav)
        
        /**
         * Specifies the CullTraverser that will be used to draw the contents of this
         * DisplayRegion.  Normally the default CullTraverser is sufficient, but this
         * may be changed to change the default cull behavior.
         */
        """
        pass

    def setDimensions(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_dimensions(const DisplayRegion self, const LVecBase4f dimensions)
        set_dimensions(const DisplayRegion self, int i, const LVecBase4f dimensions)
        set_dimensions(const DisplayRegion self, float l, float r, float b, float t)
        set_dimensions(const DisplayRegion self, int i, float l, float r, float b, float t)
        
        /**
         * Changes the portion of the framebuffer this DisplayRegion corresponds to.
         * The parameters range from 0 to 1, where 0,0 is the lower left corner and
         * 1,1 is the upper right; (0, 1, 0, 1) represents the whole screen.
         */
        
        /**
         * Changes the portion of the framebuffer this DisplayRegion corresponds to.
         * The parameters range from 0 to 1, where 0,0 is the lower left corner and
         * 1,1 is the upper right; (0, 1, 0, 1) represents the whole screen.
         */
        
        /**
         * Changes the portion of the framebuffer this DisplayRegion corresponds to.
         * The parameters range from 0 to 1, where 0,0 is the lower left corner and
         * 1,1 is the upper right; (0, 1, 0, 1) represents the whole screen.
         */
        
        /**
         * Changes the portion of the framebuffer this DisplayRegion corresponds to.
         * The parameters range from 0 to 1, where 0,0 is the lower left corner and
         * 1,1 is the upper right; (0, 1, 0, 1) represents the whole screen.
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         */
        """
        pass

    def setDrawCallback(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_draw_callback(const DisplayRegion self, CallbackObject object)
        
        /**
         * Sets the CallbackObject that will be notified when the contents of
         * DisplayRegion is drawn during the draw traversal.  This callback will be
         * made during the draw thread.
         *
         * The draw traversal is responsible for actually issuing the commands to the
         * graphics engine to draw primitives.  Its job is to walk through the list of
         * CullableObjects build up by the cull traversal, as quickly as possible,
         * issuing the appropriate commands to draw each one.
         *
         * At the time the draw traversal callback is made, the graphics state is in
         * the initial state, and no projection matrix or modelview matrix is in
         * effect.  begin_scene() has not yet been called, and no objects have yet
         * been drawn.  However, the viewport has already been set to the appropriate
         * part of the window, and the clear commands for this DisplayRegion (if any)
         * have been issued.
         *
         * The callback is passed an instance of a DisplayRegionDrawCallbackData,
         * which contains pointers to the current scene information, as well as the
         * current DisplayRegion and GSG.  The callback *replaces* the normal draw
         * behavior, so if your callback does nothing, nothing in the DisplayRegion
         * will be drawn.  If you wish the draw traversal to continue to draw the
         * contents of this DisplayRegion, you must call cbdata->upcall() from your
         * callback.
         */
        """
        pass

    def setIncompleteRender(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_incomplete_render(const DisplayRegion self, bool incomplete_render)
        
        /**
         * Sets the incomplete_render flag.  When this is true, the frame will be
         * rendered even if some of the geometry or textures in the scene are not
         * available (e.g.  they have been temporarily paged out).  When this is
         * false, the frame will be held up while this data is reloaded.
         *
         * This flag may also be set on the GraphicsStateGuardian.  It will be
         * considered true for a given DisplayRegion only if it is true on both the
         * GSG and on the DisplayRegion.
         *
         * See GraphicsStateGuardian::set_incomplete_render() for more detail.
         */
        """
        pass

    def setLensIndex(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_lens_index(const DisplayRegion self, int index)
        
        /**
         * Sets the lens index, allows for multiple lenses to be attached to a camera.
         * This is useful for a variety of setups, such as fish eye rendering.  The
         * default is 0.
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         */
        """
        pass

    def setNumRegions(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_num_regions(const DisplayRegion self, int i)
        
        /**
         * Sets the number of regions that this DisplayRegion indicates.  Usually,
         * this number is 1 (and it is always at least 1), and only the first is used
         * for rendering.  However, if more than one is provided, you may select which
         * one to render into using a geometry shader (gl_ViewportIndex in GLSL).
         */
        """
        pass

    def setScissorEnabled(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_scissor_enabled(const DisplayRegion self, bool scissor_enabled)
        
        /**
         * Sets whether or not scissor testing is enabled for this region.  The
         * default is true, except for the overlay display region.
         */
        """
        pass

    def setSort(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_sort(const DisplayRegion self, int sort)
        
        /**
         * Sets the sort value associated with the DisplayRegion.  Within a window,
         * DisplayRegions will be rendered in order from the lowest sort value to the
         * highest.
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         */
        """
        pass

    def setStereoChannel(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_stereo_channel(const DisplayRegion self, int stereo_channel)
        
        /**
         * Specifies whether the DisplayRegion represents the left or right channel of
         * a stereo pair, or whether it is a normal, monocular image.  This
         * automatically adjusts the lens that is used to render to this DisplayRegion
         * to its left or right eye, according to the lens's stereo properties.
         *
         * When the DisplayRegion is attached to a stereo window (one for which
         * is_stereo() returns true), this also specifies which physical channel the
         * DisplayRegion renders to.
         *
         * Normally you would create at least two DisplayRegions for a stereo window,
         * one for each of the left and right channels.  The two DisplayRegions may
         * share the same camera (and thus the same lens); this parameter is used to
         * control the exact properties of the lens when it is used to render into
         * this DisplayRegion.
         *
         * Also see the StereoDisplayRegion, which automates managing a pair of
         * left/right DisplayRegions.
         *
         * An ordinary DisplayRegion may be set to SC_mono, SC_left, or SC_right.  You
         * may set SC_stereo only on a StereoDisplayRegion.
         *
         * This call also resets tex_view_offset to its default value, which is 0 for
         * the left eye or 1 for the right eye of a stereo display region, or 0 for a
         * mono display region.
         */
        """
        pass

    def setTargetTexPage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_target_tex_page(const DisplayRegion self, int page)
        
        /**
         * This is a special parameter that is only used when rendering the faces of a
         * cube map or multipage and/or multiview texture.
         *
         * This sets up the DisplayRegion to render to the ith page and jth view of
         * its associated texture(s); the value must be consistent with the range of
         * values availble to the texture.  A normal DisplayRegion that is not
         * associated with any particular page should be set to page -1 and view 0.
         *
         * This is particularly useful when rendering cube maps and/or stereo
         * textures.
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         */
        """
        pass

    def setTextureReloadPriority(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_texture_reload_priority(const DisplayRegion self, int texture_reload_priority)
        
        /**
         * Specifies an integer priority which is assigned to any asynchronous texture
         * reload requests spawned while processing this DisplayRegion.  This controls
         * which textures are loaded first when multiple textures need to be reloaded
         * at once; it also controls the relative priority between asynchronous
         * texture loads and asynchronous model or animation loads.
         *
         * Specifying a larger number here makes the textures rendered by this
         * DisplayRegion load up first.  This may be particularly useful to do, for
         * instance, for the DisplayRegion that renders the gui.
         */
        """
        pass

    def setTexViewOffset(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_tex_view_offset(const DisplayRegion self, int tex_view_offset)
        
        /**
         * Sets the current texture view offset for this DisplayRegion.  This is
         * normally set to zero.  If nonzero, it is used to select a particular view
         * of any multiview textures that are rendered within this DisplayRegion.
         *
         * For a StereoDisplayRegion, this is normally 0 for the left eye, and 1 for
         * the right eye, to support stereo textures.  This is set automatically when
         * you call set_stereo_channel().
         */
        """
        pass

    def set_active(self, const_DisplayRegion_self, bool_active): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_active(const DisplayRegion self, bool active)
        
        /**
         * Sets the active flag associated with the DisplayRegion.  If the
         * DisplayRegion is marked inactive, nothing is rendered.
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         */
        """
        pass

    def set_camera(self, const_DisplayRegion_self, const_NodePath_camera): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_camera(const DisplayRegion self, const NodePath camera)
        
        /**
         * Sets the camera that is associated with this DisplayRegion.  There is a
         * one-to-many association between cameras and DisplayRegions; one camera may
         * be shared by multiple DisplayRegions.
         *
         * The camera is actually set via a NodePath, which clarifies which instance
         * of the camera (if there happen to be multiple instances) we should use.
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         */
        """
        pass

    def set_cube_map_index(self, const_DisplayRegion_self, int_cube_map_index): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_cube_map_index(const DisplayRegion self, int cube_map_index)
        
        /**
         * Deprecated; replaced by set_target_tex_page().
         */
        """
        pass

    def set_cull_callback(self, const_DisplayRegion_self, CallbackObject_object): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_cull_callback(const DisplayRegion self, CallbackObject object)
        
        /**
         * Sets the CallbackObject that will be notified when the DisplayRegion is
         * visited during the cull traversal.  This callback will be made during the
         * cull thread.
         *
         * The cull traversal is responsible for determining which nodes are visible
         * and within the view frustum, and for accumulating state and transform, and
         * generally building up the list of CullableObjects that are to be eventually
         * passed to the draw traversal for rendering.
         *
         * At the time the cull traversal callback is made, the traversal for this
         * DisplayRegion has not yet started.
         *
         * The callback is passed an instance of a DisplayRegionCullCallbackData,
         * which contains pointers to the current scene information, as well as the
         * current DisplayRegion and GSG.  The callback *replaces* the normal cull
         * behavior, so if your callback does nothing, the scene graph will not be
         * traversed and therefore nothing will be drawn.  If you wish the normal cull
         * traversal to be performed for this DisplayRegion, you must call
         * cbdata->upcall() from your callback.
         */
        """
        pass

    def set_cull_traverser(self, const_DisplayRegion_self, CullTraverser_trav): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_cull_traverser(const DisplayRegion self, CullTraverser trav)
        
        /**
         * Specifies the CullTraverser that will be used to draw the contents of this
         * DisplayRegion.  Normally the default CullTraverser is sufficient, but this
         * may be changed to change the default cull behavior.
         */
        """
        pass

    def set_dimensions(self, const_DisplayRegion_self, const_LVecBase4f_dimensions): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_dimensions(const DisplayRegion self, const LVecBase4f dimensions)
        set_dimensions(const DisplayRegion self, int i, const LVecBase4f dimensions)
        set_dimensions(const DisplayRegion self, float l, float r, float b, float t)
        set_dimensions(const DisplayRegion self, int i, float l, float r, float b, float t)
        
        /**
         * Changes the portion of the framebuffer this DisplayRegion corresponds to.
         * The parameters range from 0 to 1, where 0,0 is the lower left corner and
         * 1,1 is the upper right; (0, 1, 0, 1) represents the whole screen.
         */
        
        /**
         * Changes the portion of the framebuffer this DisplayRegion corresponds to.
         * The parameters range from 0 to 1, where 0,0 is the lower left corner and
         * 1,1 is the upper right; (0, 1, 0, 1) represents the whole screen.
         */
        
        /**
         * Changes the portion of the framebuffer this DisplayRegion corresponds to.
         * The parameters range from 0 to 1, where 0,0 is the lower left corner and
         * 1,1 is the upper right; (0, 1, 0, 1) represents the whole screen.
         */
        
        /**
         * Changes the portion of the framebuffer this DisplayRegion corresponds to.
         * The parameters range from 0 to 1, where 0,0 is the lower left corner and
         * 1,1 is the upper right; (0, 1, 0, 1) represents the whole screen.
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         */
        """
        pass

    def set_draw_callback(self, const_DisplayRegion_self, CallbackObject_object): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_draw_callback(const DisplayRegion self, CallbackObject object)
        
        /**
         * Sets the CallbackObject that will be notified when the contents of
         * DisplayRegion is drawn during the draw traversal.  This callback will be
         * made during the draw thread.
         *
         * The draw traversal is responsible for actually issuing the commands to the
         * graphics engine to draw primitives.  Its job is to walk through the list of
         * CullableObjects build up by the cull traversal, as quickly as possible,
         * issuing the appropriate commands to draw each one.
         *
         * At the time the draw traversal callback is made, the graphics state is in
         * the initial state, and no projection matrix or modelview matrix is in
         * effect.  begin_scene() has not yet been called, and no objects have yet
         * been drawn.  However, the viewport has already been set to the appropriate
         * part of the window, and the clear commands for this DisplayRegion (if any)
         * have been issued.
         *
         * The callback is passed an instance of a DisplayRegionDrawCallbackData,
         * which contains pointers to the current scene information, as well as the
         * current DisplayRegion and GSG.  The callback *replaces* the normal draw
         * behavior, so if your callback does nothing, nothing in the DisplayRegion
         * will be drawn.  If you wish the draw traversal to continue to draw the
         * contents of this DisplayRegion, you must call cbdata->upcall() from your
         * callback.
         */
        """
        pass

    def set_incomplete_render(self, const_DisplayRegion_self, bool_incomplete_render): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_incomplete_render(const DisplayRegion self, bool incomplete_render)
        
        /**
         * Sets the incomplete_render flag.  When this is true, the frame will be
         * rendered even if some of the geometry or textures in the scene are not
         * available (e.g.  they have been temporarily paged out).  When this is
         * false, the frame will be held up while this data is reloaded.
         *
         * This flag may also be set on the GraphicsStateGuardian.  It will be
         * considered true for a given DisplayRegion only if it is true on both the
         * GSG and on the DisplayRegion.
         *
         * See GraphicsStateGuardian::set_incomplete_render() for more detail.
         */
        """
        pass

    def set_lens_index(self, const_DisplayRegion_self, int_index): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_lens_index(const DisplayRegion self, int index)
        
        /**
         * Sets the lens index, allows for multiple lenses to be attached to a camera.
         * This is useful for a variety of setups, such as fish eye rendering.  The
         * default is 0.
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         */
        """
        pass

    def set_num_regions(self, const_DisplayRegion_self, int_i): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_num_regions(const DisplayRegion self, int i)
        
        /**
         * Sets the number of regions that this DisplayRegion indicates.  Usually,
         * this number is 1 (and it is always at least 1), and only the first is used
         * for rendering.  However, if more than one is provided, you may select which
         * one to render into using a geometry shader (gl_ViewportIndex in GLSL).
         */
        """
        pass

    def set_scissor_enabled(self, const_DisplayRegion_self, bool_scissor_enabled): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_scissor_enabled(const DisplayRegion self, bool scissor_enabled)
        
        /**
         * Sets whether or not scissor testing is enabled for this region.  The
         * default is true, except for the overlay display region.
         */
        """
        pass

    def set_sort(self, const_DisplayRegion_self, int_sort): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_sort(const DisplayRegion self, int sort)
        
        /**
         * Sets the sort value associated with the DisplayRegion.  Within a window,
         * DisplayRegions will be rendered in order from the lowest sort value to the
         * highest.
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         */
        """
        pass

    def set_stereo_channel(self, const_DisplayRegion_self, int_stereo_channel): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_stereo_channel(const DisplayRegion self, int stereo_channel)
        
        /**
         * Specifies whether the DisplayRegion represents the left or right channel of
         * a stereo pair, or whether it is a normal, monocular image.  This
         * automatically adjusts the lens that is used to render to this DisplayRegion
         * to its left or right eye, according to the lens's stereo properties.
         *
         * When the DisplayRegion is attached to a stereo window (one for which
         * is_stereo() returns true), this also specifies which physical channel the
         * DisplayRegion renders to.
         *
         * Normally you would create at least two DisplayRegions for a stereo window,
         * one for each of the left and right channels.  The two DisplayRegions may
         * share the same camera (and thus the same lens); this parameter is used to
         * control the exact properties of the lens when it is used to render into
         * this DisplayRegion.
         *
         * Also see the StereoDisplayRegion, which automates managing a pair of
         * left/right DisplayRegions.
         *
         * An ordinary DisplayRegion may be set to SC_mono, SC_left, or SC_right.  You
         * may set SC_stereo only on a StereoDisplayRegion.
         *
         * This call also resets tex_view_offset to its default value, which is 0 for
         * the left eye or 1 for the right eye of a stereo display region, or 0 for a
         * mono display region.
         */
        """
        pass

    def set_target_tex_page(self, const_DisplayRegion_self, int_page): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_target_tex_page(const DisplayRegion self, int page)
        
        /**
         * This is a special parameter that is only used when rendering the faces of a
         * cube map or multipage and/or multiview texture.
         *
         * This sets up the DisplayRegion to render to the ith page and jth view of
         * its associated texture(s); the value must be consistent with the range of
         * values availble to the texture.  A normal DisplayRegion that is not
         * associated with any particular page should be set to page -1 and view 0.
         *
         * This is particularly useful when rendering cube maps and/or stereo
         * textures.
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         */
        """
        pass

    def set_texture_reload_priority(self, const_DisplayRegion_self, int_texture_reload_priority): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_texture_reload_priority(const DisplayRegion self, int texture_reload_priority)
        
        /**
         * Specifies an integer priority which is assigned to any asynchronous texture
         * reload requests spawned while processing this DisplayRegion.  This controls
         * which textures are loaded first when multiple textures need to be reloaded
         * at once; it also controls the relative priority between asynchronous
         * texture loads and asynchronous model or animation loads.
         *
         * Specifying a larger number here makes the textures rendered by this
         * DisplayRegion load up first.  This may be particularly useful to do, for
         * instance, for the DisplayRegion that renders the gui.
         */
        """
        pass

    def set_tex_view_offset(self, const_DisplayRegion_self, int_tex_view_offset): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_tex_view_offset(const DisplayRegion self, int tex_view_offset)
        
        /**
         * Sets the current texture view offset for this DisplayRegion.  This is
         * normally set to zero.  If nonzero, it is used to select a particular view
         * of any multiview textures that are rendered within this DisplayRegion.
         *
         * For a StereoDisplayRegion, this is normally 0 for the left eye, and 1 for
         * the right eye, to support stereo textures.  This is set automatically when
         * you call set_stereo_channel().
         */
        """
        pass

    def upcastToDrawableRegion(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_DrawableRegion(const DisplayRegion self)
        
        upcast from DisplayRegion to DrawableRegion
        """
        pass

    def upcastToTypedReferenceCount(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_TypedReferenceCount(const DisplayRegion self)
        
        upcast from DisplayRegion to TypedReferenceCount
        """
        pass

    def upcast_to_DrawableRegion(self, const_DisplayRegion_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_DrawableRegion(const DisplayRegion self)
        
        upcast from DisplayRegion to DrawableRegion
        """
        pass

    def upcast_to_TypedReferenceCount(self, const_DisplayRegion_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_TypedReferenceCount(const DisplayRegion self)
        
        upcast from DisplayRegion to TypedReferenceCount
        """
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

    active = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    camera = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    cull_callback = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    cull_traverser = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dimensions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    draw_callback = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    incomplete_render = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    lens_index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pipe = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pixel_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    scissor_enabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    sort = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    stereo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    stereo_channel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    target_tex_page = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    texture_reload_priority = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tex_view_offset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    window = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * A rectangular subregion within a window for rendering into.  Typically,\n * there is one DisplayRegion that covers the whole window, but you may also\n * create smaller DisplayRegions for having different regions within the\n * window that represent different scenes.  You may also stack up\n * DisplayRegions like panes of glass, usually for layering 2-d interfaces on\n * top of a 3-d scene.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.DisplayRegion' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2DD530>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.DisplayRegion' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.DisplayRegion' objects>"
        'active': None, # (!) real value is "<attribute 'active' of 'panda3d.core.DisplayRegion' objects>"
        'camera': None, # (!) real value is "<attribute 'camera' of 'panda3d.core.DisplayRegion' objects>"
        'clearCullCallback': None, # (!) real value is "<method 'clearCullCallback' of 'panda3d.core.DisplayRegion' objects>"
        'clearCullResult': None, # (!) real value is "<method 'clearCullResult' of 'panda3d.core.DisplayRegion' objects>"
        'clearDrawCallback': None, # (!) real value is "<method 'clearDrawCallback' of 'panda3d.core.DisplayRegion' objects>"
        'clear_cull_callback': None, # (!) real value is "<method 'clear_cull_callback' of 'panda3d.core.DisplayRegion' objects>"
        'clear_cull_result': None, # (!) real value is "<method 'clear_cull_result' of 'panda3d.core.DisplayRegion' objects>"
        'clear_draw_callback': None, # (!) real value is "<method 'clear_draw_callback' of 'panda3d.core.DisplayRegion' objects>"
        'cull_callback': None, # (!) real value is "<attribute 'cull_callback' of 'panda3d.core.DisplayRegion' objects>"
        'cull_traverser': None, # (!) real value is "<attribute 'cull_traverser' of 'panda3d.core.DisplayRegion' objects>"
        'dimensions': None, # (!) real value is "<attribute 'dimensions' of 'panda3d.core.DisplayRegion' objects>"
        'draw_callback': None, # (!) real value is "<attribute 'draw_callback' of 'panda3d.core.DisplayRegion' objects>"
        'getBottom': None, # (!) real value is "<method 'getBottom' of 'panda3d.core.DisplayRegion' objects>"
        'getCamera': None, # (!) real value is "<method 'getCamera' of 'panda3d.core.DisplayRegion' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2DD530>)>'
        'getCullCallback': None, # (!) real value is "<method 'getCullCallback' of 'panda3d.core.DisplayRegion' objects>"
        'getCullTraverser': None, # (!) real value is "<method 'getCullTraverser' of 'panda3d.core.DisplayRegion' objects>"
        'getDimensions': None, # (!) real value is "<method 'getDimensions' of 'panda3d.core.DisplayRegion' objects>"
        'getDrawCallback': None, # (!) real value is "<method 'getDrawCallback' of 'panda3d.core.DisplayRegion' objects>"
        'getIncompleteRender': None, # (!) real value is "<method 'getIncompleteRender' of 'panda3d.core.DisplayRegion' objects>"
        'getLeft': None, # (!) real value is "<method 'getLeft' of 'panda3d.core.DisplayRegion' objects>"
        'getLensIndex': None, # (!) real value is "<method 'getLensIndex' of 'panda3d.core.DisplayRegion' objects>"
        'getNumRegions': None, # (!) real value is "<method 'getNumRegions' of 'panda3d.core.DisplayRegion' objects>"
        'getPipe': None, # (!) real value is "<method 'getPipe' of 'panda3d.core.DisplayRegion' objects>"
        'getPixelHeight': None, # (!) real value is "<method 'getPixelHeight' of 'panda3d.core.DisplayRegion' objects>"
        'getPixelSize': None, # (!) real value is "<method 'getPixelSize' of 'panda3d.core.DisplayRegion' objects>"
        'getPixelWidth': None, # (!) real value is "<method 'getPixelWidth' of 'panda3d.core.DisplayRegion' objects>"
        'getRight': None, # (!) real value is "<method 'getRight' of 'panda3d.core.DisplayRegion' objects>"
        'getScissorEnabled': None, # (!) real value is "<method 'getScissorEnabled' of 'panda3d.core.DisplayRegion' objects>"
        'getScreenshot': None, # (!) real value is "<method 'getScreenshot' of 'panda3d.core.DisplayRegion' objects>"
        'getSort': None, # (!) real value is "<method 'getSort' of 'panda3d.core.DisplayRegion' objects>"
        'getStereoChannel': None, # (!) real value is "<method 'getStereoChannel' of 'panda3d.core.DisplayRegion' objects>"
        'getTargetTexPage': None, # (!) real value is "<method 'getTargetTexPage' of 'panda3d.core.DisplayRegion' objects>"
        'getTexViewOffset': None, # (!) real value is "<method 'getTexViewOffset' of 'panda3d.core.DisplayRegion' objects>"
        'getTextureReloadPriority': None, # (!) real value is "<method 'getTextureReloadPriority' of 'panda3d.core.DisplayRegion' objects>"
        'getTop': None, # (!) real value is "<method 'getTop' of 'panda3d.core.DisplayRegion' objects>"
        'getWindow': None, # (!) real value is "<method 'getWindow' of 'panda3d.core.DisplayRegion' objects>"
        'get_bottom': None, # (!) real value is "<method 'get_bottom' of 'panda3d.core.DisplayRegion' objects>"
        'get_camera': None, # (!) real value is "<method 'get_camera' of 'panda3d.core.DisplayRegion' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2DD530>)>'
        'get_cull_callback': None, # (!) real value is "<method 'get_cull_callback' of 'panda3d.core.DisplayRegion' objects>"
        'get_cull_traverser': None, # (!) real value is "<method 'get_cull_traverser' of 'panda3d.core.DisplayRegion' objects>"
        'get_dimensions': None, # (!) real value is "<method 'get_dimensions' of 'panda3d.core.DisplayRegion' objects>"
        'get_draw_callback': None, # (!) real value is "<method 'get_draw_callback' of 'panda3d.core.DisplayRegion' objects>"
        'get_incomplete_render': None, # (!) real value is "<method 'get_incomplete_render' of 'panda3d.core.DisplayRegion' objects>"
        'get_left': None, # (!) real value is "<method 'get_left' of 'panda3d.core.DisplayRegion' objects>"
        'get_lens_index': None, # (!) real value is "<method 'get_lens_index' of 'panda3d.core.DisplayRegion' objects>"
        'get_num_regions': None, # (!) real value is "<method 'get_num_regions' of 'panda3d.core.DisplayRegion' objects>"
        'get_pipe': None, # (!) real value is "<method 'get_pipe' of 'panda3d.core.DisplayRegion' objects>"
        'get_pixel_height': None, # (!) real value is "<method 'get_pixel_height' of 'panda3d.core.DisplayRegion' objects>"
        'get_pixel_size': None, # (!) real value is "<method 'get_pixel_size' of 'panda3d.core.DisplayRegion' objects>"
        'get_pixel_width': None, # (!) real value is "<method 'get_pixel_width' of 'panda3d.core.DisplayRegion' objects>"
        'get_right': None, # (!) real value is "<method 'get_right' of 'panda3d.core.DisplayRegion' objects>"
        'get_scissor_enabled': None, # (!) real value is "<method 'get_scissor_enabled' of 'panda3d.core.DisplayRegion' objects>"
        'get_screenshot': None, # (!) real value is "<method 'get_screenshot' of 'panda3d.core.DisplayRegion' objects>"
        'get_sort': None, # (!) real value is "<method 'get_sort' of 'panda3d.core.DisplayRegion' objects>"
        'get_stereo_channel': None, # (!) real value is "<method 'get_stereo_channel' of 'panda3d.core.DisplayRegion' objects>"
        'get_target_tex_page': None, # (!) real value is "<method 'get_target_tex_page' of 'panda3d.core.DisplayRegion' objects>"
        'get_tex_view_offset': None, # (!) real value is "<method 'get_tex_view_offset' of 'panda3d.core.DisplayRegion' objects>"
        'get_texture_reload_priority': None, # (!) real value is "<method 'get_texture_reload_priority' of 'panda3d.core.DisplayRegion' objects>"
        'get_top': None, # (!) real value is "<method 'get_top' of 'panda3d.core.DisplayRegion' objects>"
        'get_window': None, # (!) real value is "<method 'get_window' of 'panda3d.core.DisplayRegion' objects>"
        'incomplete_render': None, # (!) real value is "<attribute 'incomplete_render' of 'panda3d.core.DisplayRegion' objects>"
        'isActive': None, # (!) real value is "<method 'isActive' of 'panda3d.core.DisplayRegion' objects>"
        'isStereo': None, # (!) real value is "<method 'isStereo' of 'panda3d.core.DisplayRegion' objects>"
        'is_active': None, # (!) real value is "<method 'is_active' of 'panda3d.core.DisplayRegion' objects>"
        'is_stereo': None, # (!) real value is "<method 'is_stereo' of 'panda3d.core.DisplayRegion' objects>"
        'lens_index': None, # (!) real value is "<attribute 'lens_index' of 'panda3d.core.DisplayRegion' objects>"
        'makeCullResultGraph': None, # (!) real value is "<method 'makeCullResultGraph' of 'panda3d.core.DisplayRegion' objects>"
        'makeScreenshotFilename': None, # (!) real value is '<staticmethod(<built-in method makeScreenshotFilename of type object at 0x00007FFCFE2DD530>)>'
        'make_cull_result_graph': None, # (!) real value is "<method 'make_cull_result_graph' of 'panda3d.core.DisplayRegion' objects>"
        'make_screenshot_filename': None, # (!) real value is '<staticmethod(<built-in method make_screenshot_filename of type object at 0x00007FFCFE2DD530>)>'
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.DisplayRegion' objects>"
        'pipe': None, # (!) real value is "<attribute 'pipe' of 'panda3d.core.DisplayRegion' objects>"
        'pixel_size': None, # (!) real value is "<attribute 'pixel_size' of 'panda3d.core.DisplayRegion' objects>"
        'saveScreenshot': None, # (!) real value is "<method 'saveScreenshot' of 'panda3d.core.DisplayRegion' objects>"
        'saveScreenshotDefault': None, # (!) real value is "<method 'saveScreenshotDefault' of 'panda3d.core.DisplayRegion' objects>"
        'save_screenshot': None, # (!) real value is "<method 'save_screenshot' of 'panda3d.core.DisplayRegion' objects>"
        'save_screenshot_default': None, # (!) real value is "<method 'save_screenshot_default' of 'panda3d.core.DisplayRegion' objects>"
        'scissor_enabled': None, # (!) real value is "<attribute 'scissor_enabled' of 'panda3d.core.DisplayRegion' objects>"
        'setActive': None, # (!) real value is "<method 'setActive' of 'panda3d.core.DisplayRegion' objects>"
        'setCamera': None, # (!) real value is "<method 'setCamera' of 'panda3d.core.DisplayRegion' objects>"
        'setCubeMapIndex': None, # (!) real value is "<method 'setCubeMapIndex' of 'panda3d.core.DisplayRegion' objects>"
        'setCullCallback': None, # (!) real value is "<method 'setCullCallback' of 'panda3d.core.DisplayRegion' objects>"
        'setCullTraverser': None, # (!) real value is "<method 'setCullTraverser' of 'panda3d.core.DisplayRegion' objects>"
        'setDimensions': None, # (!) real value is "<method 'setDimensions' of 'panda3d.core.DisplayRegion' objects>"
        'setDrawCallback': None, # (!) real value is "<method 'setDrawCallback' of 'panda3d.core.DisplayRegion' objects>"
        'setIncompleteRender': None, # (!) real value is "<method 'setIncompleteRender' of 'panda3d.core.DisplayRegion' objects>"
        'setLensIndex': None, # (!) real value is "<method 'setLensIndex' of 'panda3d.core.DisplayRegion' objects>"
        'setNumRegions': None, # (!) real value is "<method 'setNumRegions' of 'panda3d.core.DisplayRegion' objects>"
        'setScissorEnabled': None, # (!) real value is "<method 'setScissorEnabled' of 'panda3d.core.DisplayRegion' objects>"
        'setSort': None, # (!) real value is "<method 'setSort' of 'panda3d.core.DisplayRegion' objects>"
        'setStereoChannel': None, # (!) real value is "<method 'setStereoChannel' of 'panda3d.core.DisplayRegion' objects>"
        'setTargetTexPage': None, # (!) real value is "<method 'setTargetTexPage' of 'panda3d.core.DisplayRegion' objects>"
        'setTexViewOffset': None, # (!) real value is "<method 'setTexViewOffset' of 'panda3d.core.DisplayRegion' objects>"
        'setTextureReloadPriority': None, # (!) real value is "<method 'setTextureReloadPriority' of 'panda3d.core.DisplayRegion' objects>"
        'set_active': None, # (!) real value is "<method 'set_active' of 'panda3d.core.DisplayRegion' objects>"
        'set_camera': None, # (!) real value is "<method 'set_camera' of 'panda3d.core.DisplayRegion' objects>"
        'set_cube_map_index': None, # (!) real value is "<method 'set_cube_map_index' of 'panda3d.core.DisplayRegion' objects>"
        'set_cull_callback': None, # (!) real value is "<method 'set_cull_callback' of 'panda3d.core.DisplayRegion' objects>"
        'set_cull_traverser': None, # (!) real value is "<method 'set_cull_traverser' of 'panda3d.core.DisplayRegion' objects>"
        'set_dimensions': None, # (!) real value is "<method 'set_dimensions' of 'panda3d.core.DisplayRegion' objects>"
        'set_draw_callback': None, # (!) real value is "<method 'set_draw_callback' of 'panda3d.core.DisplayRegion' objects>"
        'set_incomplete_render': None, # (!) real value is "<method 'set_incomplete_render' of 'panda3d.core.DisplayRegion' objects>"
        'set_lens_index': None, # (!) real value is "<method 'set_lens_index' of 'panda3d.core.DisplayRegion' objects>"
        'set_num_regions': None, # (!) real value is "<method 'set_num_regions' of 'panda3d.core.DisplayRegion' objects>"
        'set_scissor_enabled': None, # (!) real value is "<method 'set_scissor_enabled' of 'panda3d.core.DisplayRegion' objects>"
        'set_sort': None, # (!) real value is "<method 'set_sort' of 'panda3d.core.DisplayRegion' objects>"
        'set_stereo_channel': None, # (!) real value is "<method 'set_stereo_channel' of 'panda3d.core.DisplayRegion' objects>"
        'set_target_tex_page': None, # (!) real value is "<method 'set_target_tex_page' of 'panda3d.core.DisplayRegion' objects>"
        'set_tex_view_offset': None, # (!) real value is "<method 'set_tex_view_offset' of 'panda3d.core.DisplayRegion' objects>"
        'set_texture_reload_priority': None, # (!) real value is "<method 'set_texture_reload_priority' of 'panda3d.core.DisplayRegion' objects>"
        'sort': None, # (!) real value is "<attribute 'sort' of 'panda3d.core.DisplayRegion' objects>"
        'stereo': None, # (!) real value is "<attribute 'stereo' of 'panda3d.core.DisplayRegion' objects>"
        'stereo_channel': None, # (!) real value is "<attribute 'stereo_channel' of 'panda3d.core.DisplayRegion' objects>"
        'target_tex_page': None, # (!) real value is "<attribute 'target_tex_page' of 'panda3d.core.DisplayRegion' objects>"
        'tex_view_offset': None, # (!) real value is "<attribute 'tex_view_offset' of 'panda3d.core.DisplayRegion' objects>"
        'texture_reload_priority': None, # (!) real value is "<attribute 'texture_reload_priority' of 'panda3d.core.DisplayRegion' objects>"
        'upcastToDrawableRegion': None, # (!) real value is "<method 'upcastToDrawableRegion' of 'panda3d.core.DisplayRegion' objects>"
        'upcastToTypedReferenceCount': None, # (!) real value is "<method 'upcastToTypedReferenceCount' of 'panda3d.core.DisplayRegion' objects>"
        'upcast_to_DrawableRegion': None, # (!) real value is "<method 'upcast_to_DrawableRegion' of 'panda3d.core.DisplayRegion' objects>"
        'upcast_to_TypedReferenceCount': None, # (!) real value is "<method 'upcast_to_TypedReferenceCount' of 'panda3d.core.DisplayRegion' objects>"
        'window': None, # (!) real value is "<attribute 'window' of 'panda3d.core.DisplayRegion' objects>"
    }


