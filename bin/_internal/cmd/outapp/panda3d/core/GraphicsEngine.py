# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .ReferenceCount import ReferenceCount

class GraphicsEngine(ReferenceCount):
    """
    /**
     * This class is the main interface to controlling the render process.  There
     * is typically only one GraphicsEngine in an application, and it synchronizes
     * rendering to all all of the active windows; although it is possible to have
     * multiple GraphicsEngine objects if multiple synchronicity groups are
     * required.
     *
     * The GraphicsEngine is responsible for managing the various cull and draw
     * threads.  The application simply calls engine->render_frame() and considers
     * it done.
     */
    """
    def addWindow(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_window(const GraphicsEngine self, GraphicsOutput window, int sort)
        
        /**
         * This can be used to add a newly-created GraphicsOutput object (and its GSG)
         * to the engine's list of windows, and requests that it be opened.  This
         * shouldn't be called by user code as make_output normally does this under
         * the hood; it may be useful in esoteric cases in which a custom window
         * object is used.
         *
         * This can be called during the rendering loop, unlike make_output(); the
         * window will be opened before the next frame begins rendering.  Because it
         * doesn't call open_windows(), however, it's not guaranteed that the window
         * will succeed opening even if it returns true.
         */
        """
        pass

    def add_window(self, const_GraphicsEngine_self, GraphicsOutput_window, int_sort): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_window(const GraphicsEngine self, GraphicsOutput window, int sort)
        
        /**
         * This can be used to add a newly-created GraphicsOutput object (and its GSG)
         * to the engine's list of windows, and requests that it be opened.  This
         * shouldn't be called by user code as make_output normally does this under
         * the hood; it may be useful in esoteric cases in which a custom window
         * object is used.
         *
         * This can be called during the rendering loop, unlike make_output(); the
         * window will be opened before the next frame begins rendering.  Because it
         * doesn't call open_windows(), however, it's not guaranteed that the window
         * will succeed opening even if it returns true.
         */
        """
        pass

    def dispatchCompute(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        dispatch_compute(const GraphicsEngine self, const LVecBase3i work_groups, const ShaderAttrib sattr, GraphicsStateGuardian gsg)
        
        /**
         * Asks the indicated GraphicsStateGuardian to dispatch the compute shader in
         * the given ShaderAttrib using the given work group counts.  This can act as
         * an interface for running a one-off compute shader, without having to store
         * it in the scene graph using a ComputeNode.
         *
         * Since this requires a round-trip to the draw thread, it may require waiting
         * for the current thread to finish rendering if it is called in a
         * multithreaded environment.  However, you can call this several consecutive
         * times on different textures for little additional cost.
         *
         * The return value is true if the operation is successful, false otherwise.
         */
        """
        pass

    def dispatch_compute(self, const_GraphicsEngine_self, const_LVecBase3i_work_groups, const_ShaderAttrib_sattr, GraphicsStateGuardian_gsg): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        dispatch_compute(const GraphicsEngine self, const LVecBase3i work_groups, const ShaderAttrib sattr, GraphicsStateGuardian gsg)
        
        /**
         * Asks the indicated GraphicsStateGuardian to dispatch the compute shader in
         * the given ShaderAttrib using the given work group counts.  This can act as
         * an interface for running a one-off compute shader, without having to store
         * it in the scene graph using a ComputeNode.
         *
         * Since this requires a round-trip to the draw thread, it may require waiting
         * for the current thread to finish rendering if it is called in a
         * multithreaded environment.  However, you can call this several consecutive
         * times on different textures for little additional cost.
         *
         * The return value is true if the operation is successful, false otherwise.
         */
        """
        pass

    def extractTextureData(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        extract_texture_data(const GraphicsEngine self, Texture tex, GraphicsStateGuardian gsg)
        
        /**
         * Asks the indicated GraphicsStateGuardian to retrieve the texture memory
         * image of the indicated texture and store it in the texture's ram_image
         * field.  The image can then be written to disk via Texture::write(), or
         * otherwise manipulated on the CPU.
         *
         * This is useful for retrieving the contents of a texture that has been
         * somehow generated on the graphics card, instead of having been loaded the
         * normal way via Texture::read() or Texture::load(). It is particularly
         * useful for getting the data associated with a compressed texture image.
         *
         * Since this requires a round-trip to the draw thread, it may require waiting
         * for the current thread to finish rendering if it is called in a
         * multithreaded environment.  However, you can call this several consecutive
         * times on different textures for little additional cost.
         *
         * If the texture has not yet been loaded to the GSG in question, it will be
         * loaded immediately.
         *
         * The return value is true if the operation is successful, false otherwise.
         */
        """
        pass

    def extract_texture_data(self, const_GraphicsEngine_self, Texture_tex, GraphicsStateGuardian_gsg): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        extract_texture_data(const GraphicsEngine self, Texture tex, GraphicsStateGuardian gsg)
        
        /**
         * Asks the indicated GraphicsStateGuardian to retrieve the texture memory
         * image of the indicated texture and store it in the texture's ram_image
         * field.  The image can then be written to disk via Texture::write(), or
         * otherwise manipulated on the CPU.
         *
         * This is useful for retrieving the contents of a texture that has been
         * somehow generated on the graphics card, instead of having been loaded the
         * normal way via Texture::read() or Texture::load(). It is particularly
         * useful for getting the data associated with a compressed texture image.
         *
         * Since this requires a round-trip to the draw thread, it may require waiting
         * for the current thread to finish rendering if it is called in a
         * multithreaded environment.  However, you can call this several consecutive
         * times on different textures for little additional cost.
         *
         * If the texture has not yet been loaded to the GSG in question, it will be
         * loaded immediately.
         *
         * The return value is true if the operation is successful, false otherwise.
         */
        """
        pass

    def flipFrame(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        flip_frame(const GraphicsEngine self)
        
        /**
         * Waits for all the threads that started drawing their last frame to finish
         * drawing, and then flips all the windows.  It is not usually necessary to
         * call this explicitly, unless you need to see the previous frame right away.
         */
        """
        pass

    def flip_frame(self, const_GraphicsEngine_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        flip_frame(const GraphicsEngine self)
        
        /**
         * Waits for all the threads that started drawing their last frame to finish
         * drawing, and then flips all the windows.  It is not usually necessary to
         * call this explicitly, unless you need to see the previous frame right away.
         */
        """
        pass

    def getAutoFlip(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_auto_flip(GraphicsEngine self)
        
        /**
         * Returns the current setting for the auto-flip flag.  See set_auto_flip.
         */
        """
        pass

    def getDefaultLoader(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_default_loader(GraphicsEngine self)
        
        /**
         * Returns the Loader object that will be assigned to every GSG created with
         * this GraphicsEngine.  See GraphicsStateGuardian::set_loader().
         */
        """
        pass

    def getGlobalPtr(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_global_ptr()
        
        /**
         *
         */
        """
        pass

    def getNumWindows(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_windows(GraphicsEngine self)
        
        /**
         * Returns the number of windows (or buffers) managed by the engine.
         */
        """
        pass

    def getPortalCull(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_portal_cull(GraphicsEngine self)
        
        /**
         * Returns the current setting for the portal culling flag.
         */
        """
        pass

    def getRenderLock(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_render_lock(GraphicsEngine self)
        
        /**
         * Returns a ReMutex object that is held by the GraphicsEngine during the
         * entire call to render_frame().  While you hold this lock you can be
         * confident that no part of the frame will be rendered (at least by the app
         * thread).
         */
        """
        pass

    def getThreadingModel(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_threading_model(GraphicsEngine self)
        
        /**
         * Returns the threading model that will be applied to future objects.  See
         * set_threading_model().
         */
        """
        pass

    def getWindow(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_window(GraphicsEngine self, int n)
        
        /**
         * Returns the nth window or buffers managed by the engine, in sorted order.
         */
        """
        pass

    def getWindows(self, *args, **kwargs): # real signature unknown
        pass

    def get_auto_flip(self, GraphicsEngine_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_auto_flip(GraphicsEngine self)
        
        /**
         * Returns the current setting for the auto-flip flag.  See set_auto_flip.
         */
        """
        pass

    def get_default_loader(self, GraphicsEngine_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_default_loader(GraphicsEngine self)
        
        /**
         * Returns the Loader object that will be assigned to every GSG created with
         * this GraphicsEngine.  See GraphicsStateGuardian::set_loader().
         */
        """
        pass

    def get_global_ptr(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_global_ptr()
        
        /**
         *
         */
        """
        pass

    def get_num_windows(self, GraphicsEngine_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_windows(GraphicsEngine self)
        
        /**
         * Returns the number of windows (or buffers) managed by the engine.
         */
        """
        pass

    def get_portal_cull(self, GraphicsEngine_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_portal_cull(GraphicsEngine self)
        
        /**
         * Returns the current setting for the portal culling flag.
         */
        """
        pass

    def get_render_lock(self, GraphicsEngine_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_render_lock(GraphicsEngine self)
        
        /**
         * Returns a ReMutex object that is held by the GraphicsEngine during the
         * entire call to render_frame().  While you hold this lock you can be
         * confident that no part of the frame will be rendered (at least by the app
         * thread).
         */
        """
        pass

    def get_threading_model(self, GraphicsEngine_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_threading_model(GraphicsEngine self)
        
        /**
         * Returns the threading model that will be applied to future objects.  See
         * set_threading_model().
         */
        """
        pass

    def get_window(self, GraphicsEngine_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_window(GraphicsEngine self, int n)
        
        /**
         * Returns the nth window or buffers managed by the engine, in sorted order.
         */
        """
        pass

    def get_windows(self, *args, **kwargs): # real signature unknown
        pass

    def isEmpty(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_empty(GraphicsEngine self)
        
        /**
         * Returns true if there are no windows or buffers managed by the engine,
         * false if there is at least one.
         */
        """
        pass

    def is_empty(self, GraphicsEngine_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_empty(GraphicsEngine self)
        
        /**
         * Returns true if there are no windows or buffers managed by the engine,
         * false if there is at least one.
         */
        """
        pass

    def makeBuffer(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_buffer(const GraphicsEngine self, GraphicsStateGuardian gsg, str name, int sort, int x_size, int y_size)
        make_buffer(const GraphicsEngine self, GraphicsOutput host, str name, int sort, int x_size, int y_size)
        
        // Syntactic shorthand versions of make_output
        
        /**
         * Syntactic shorthand for make_output.  This is the preferred way to create
         * an offscreen buffer, when you already have an onscreen window or another
         * buffer to start with.  For the first parameter, pass an existing
         * GraphicsOutput object, e.g.  the main window; this allows the buffer to
         * adapt itself to that window's framebuffer properties, and allows maximum
         * sharing of resources.
         */
        
        /**
         * Syntactic shorthand for make_output.  This flavor accepts a GSG rather than
         * a GraphicsOutput as the first parameter, which is too limiting and
         * disallows the possibility of creating a ParasiteBuffer if the user's
         * graphics hardware prefers that.  It also attempts to request specific
         * framebuffer properties and may therefore do a poorer job of sharing the GSG
         * between the old buffer and the new.
         *
         * For these reasons, this variant is a poor choice unless you are creating an
         * offscreen buffer for the first time, without an onscreen window already in
         * existence.  If you already have an onscreen window, you should use the
         * other flavor of make_buffer() instead, which accepts a GraphicsOutput as
         * the first parameter.
         */
        """
        pass

    def makeOutput(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_output(const GraphicsEngine self, GraphicsPipe pipe, str name, int sort, const FrameBufferProperties fb_prop, const WindowProperties win_prop, int flags, GraphicsStateGuardian gsg, GraphicsOutput host)
        """
        pass

    def makeParasite(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_parasite(const GraphicsEngine self, GraphicsOutput host, str name, int sort, int x_size, int y_size)
        
        /**
         * Syntactic shorthand for make_buffer.
         */
        """
        pass

    def make_buffer(self, const_GraphicsEngine_self, GraphicsStateGuardian_gsg, str_name, int_sort, int_x_size, int_y_size): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_buffer(const GraphicsEngine self, GraphicsStateGuardian gsg, str name, int sort, int x_size, int y_size)
        make_buffer(const GraphicsEngine self, GraphicsOutput host, str name, int sort, int x_size, int y_size)
        
        // Syntactic shorthand versions of make_output
        
        /**
         * Syntactic shorthand for make_output.  This is the preferred way to create
         * an offscreen buffer, when you already have an onscreen window or another
         * buffer to start with.  For the first parameter, pass an existing
         * GraphicsOutput object, e.g.  the main window; this allows the buffer to
         * adapt itself to that window's framebuffer properties, and allows maximum
         * sharing of resources.
         */
        
        /**
         * Syntactic shorthand for make_output.  This flavor accepts a GSG rather than
         * a GraphicsOutput as the first parameter, which is too limiting and
         * disallows the possibility of creating a ParasiteBuffer if the user's
         * graphics hardware prefers that.  It also attempts to request specific
         * framebuffer properties and may therefore do a poorer job of sharing the GSG
         * between the old buffer and the new.
         *
         * For these reasons, this variant is a poor choice unless you are creating an
         * offscreen buffer for the first time, without an onscreen window already in
         * existence.  If you already have an onscreen window, you should use the
         * other flavor of make_buffer() instead, which accepts a GraphicsOutput as
         * the first parameter.
         */
        """
        pass

    def make_output(self, const_GraphicsEngine_self, GraphicsPipe_pipe, str_name, int_sort, const_FrameBufferProperties_fb_prop, const_WindowProperties_win_prop, int_flags, GraphicsStateGuardian_gsg, GraphicsOutput_host): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_output(const GraphicsEngine self, GraphicsPipe pipe, str name, int sort, const FrameBufferProperties fb_prop, const WindowProperties win_prop, int flags, GraphicsStateGuardian gsg, GraphicsOutput host)
        """
        pass

    def make_parasite(self, const_GraphicsEngine_self, GraphicsOutput_host, str_name, int_sort, int_x_size, int_y_size): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_parasite(const GraphicsEngine self, GraphicsOutput host, str name, int sort, int x_size, int y_size)
        
        /**
         * Syntactic shorthand for make_buffer.
         */
        """
        pass

    def openWindows(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        open_windows(const GraphicsEngine self)
        
        /**
         * Fully opens (or closes) any windows that have recently been requested open
         * or closed, without rendering any frames.  It is not necessary to call this
         * explicitly, since windows will be automatically opened or closed when the
         * next frame is rendered, but you may call this if you want your windows now
         * without seeing a frame go by.
         */
        """
        pass

    def open_windows(self, const_GraphicsEngine_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        open_windows(const GraphicsEngine self)
        
        /**
         * Fully opens (or closes) any windows that have recently been requested open
         * or closed, without rendering any frames.  It is not necessary to call this
         * explicitly, since windows will be automatically opened or closed when the
         * next frame is rendered, but you may call this if you want your windows now
         * without seeing a frame go by.
         */
        """
        pass

    def readyFlip(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        ready_flip(const GraphicsEngine self)
        
        /**
         * Waits for all the threads that started drawing their last frame to finish
         * drawing.  Returns when all threads have actually finished drawing, as
         * opposed to 'sync_frame' we seems to return once all draw calls have been
         * submitted.  Calling 'flip_frame' after this function should immediately
         * cause a buffer flip.  This function will only work in opengl right now, for
         * all other graphics pipelines it will simply return immediately.  In opengl
         * it's a bit of a hack: it will attempt to read a single pixel from the frame
         * buffer to force the graphics card to finish drawing before it returns
         */
        """
        pass

    def ready_flip(self, const_GraphicsEngine_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        ready_flip(const GraphicsEngine self)
        
        /**
         * Waits for all the threads that started drawing their last frame to finish
         * drawing.  Returns when all threads have actually finished drawing, as
         * opposed to 'sync_frame' we seems to return once all draw calls have been
         * submitted.  Calling 'flip_frame' after this function should immediately
         * cause a buffer flip.  This function will only work in opengl right now, for
         * all other graphics pipelines it will simply return immediately.  In opengl
         * it's a bit of a hack: it will attempt to read a single pixel from the frame
         * buffer to force the graphics card to finish drawing before it returns
         */
        """
        pass

    def removeAllWindows(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_all_windows(const GraphicsEngine self)
        
        /**
         * Removes and closes all windows from the engine.  This also cleans up and
         * terminates any threads that have been started to service those windows.
         */
        """
        pass

    def removeWindow(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_window(const GraphicsEngine self, GraphicsOutput window)
        
        /**
         * Removes the indicated window or offscreen buffer from the set of windows
         * that will be processed when render_frame() is called.  This also closes the
         * window if it is open, and removes the window from its GraphicsPipe,
         * allowing the window to be destructed if there are no other references to
         * it.  (However, the window may not be actually closed until next frame, if
         * it is controlled by a sub-thread.)
         *
         * The return value is true if the window was removed, false if it was not
         * found.
         *
         * Unlike remove_all_windows(), this function does not terminate any of the
         * threads that may have been started to service this window; they are left
         * running (since you might open a new window later on these threads).  If
         * your intention is to clean up before shutting down, it is better to call
         * remove_all_windows() then to call remove_window() one at a time.
         */
        """
        pass

    def remove_all_windows(self, const_GraphicsEngine_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_all_windows(const GraphicsEngine self)
        
        /**
         * Removes and closes all windows from the engine.  This also cleans up and
         * terminates any threads that have been started to service those windows.
         */
        """
        pass

    def remove_window(self, const_GraphicsEngine_self, GraphicsOutput_window): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_window(const GraphicsEngine self, GraphicsOutput window)
        
        /**
         * Removes the indicated window or offscreen buffer from the set of windows
         * that will be processed when render_frame() is called.  This also closes the
         * window if it is open, and removes the window from its GraphicsPipe,
         * allowing the window to be destructed if there are no other references to
         * it.  (However, the window may not be actually closed until next frame, if
         * it is controlled by a sub-thread.)
         *
         * The return value is true if the window was removed, false if it was not
         * found.
         *
         * Unlike remove_all_windows(), this function does not terminate any of the
         * threads that may have been started to service this window; they are left
         * running (since you might open a new window later on these threads).  If
         * your intention is to clean up before shutting down, it is better to call
         * remove_all_windows() then to call remove_window() one at a time.
         */
        """
        pass

    def renderFrame(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        render_frame(const GraphicsEngine self)
        
        /**
         * Renders the next frame in all the registered windows, and flips all of the
         * frame buffers.
         */
        """
        pass

    def render_frame(self, const_GraphicsEngine_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        render_frame(const GraphicsEngine self)
        
        /**
         * Renders the next frame in all the registered windows, and flips all of the
         * frame buffers.
         */
        """
        pass

    def resetAllWindows(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        reset_all_windows(const GraphicsEngine self, bool swapchain)
        
        /**
         * Resets the framebuffer of the current window.  This is currently used by
         * DirectX 8 only.  It calls a reset_window function on each active window to
         * release/create old/new framebuffer
         */
        """
        pass

    def reset_all_windows(self, const_GraphicsEngine_self, bool_swapchain): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        reset_all_windows(const GraphicsEngine self, bool swapchain)
        
        /**
         * Resets the framebuffer of the current window.  This is currently used by
         * DirectX 8 only.  It calls a reset_window function on each active window to
         * release/create old/new framebuffer
         */
        """
        pass

    def setAutoFlip(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_auto_flip(const GraphicsEngine self, bool auto_flip)
        
        /**
         * Set this flag true to indicate the GraphicsEngine should automatically
         * cause windows to sync and flip as soon as they have finished drawing,
         * rather than waiting for all of the windows to finish drawing first so they
         * can flip together.
         *
         * This only affects the timing of when the flip occurs.  If this is true (the
         * default), the flip occurs before render_frame() returns.  If this is false,
         * the flip occurs whenever flip_frame() is called, or at the beginning of the
         * next call to render_frame(), if flip_frame() is never called.
         */
        """
        pass

    def setDefaultLoader(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_default_loader(const GraphicsEngine self, Loader loader)
        
        /**
         * Sets the Loader object that will be assigned to every GSG created with this
         * GraphicsEngine.  See GraphicsStateGuardian::set_loader().
         */
        """
        pass

    def setPortalCull(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_portal_cull(const GraphicsEngine self, bool value)
        
        /**
         * Set this flag true to indicate the GraphicsEngine should start portal
         * culling
         */
        """
        pass

    def setThreadingModel(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_threading_model(const GraphicsEngine self, const GraphicsThreadingModel threading_model)
        
        /**
         * Specifies how future objects created via make_gsg(), make_buffer(), and
         * make_output() will be threaded.  This does not affect any already-created
         * objects.
         */
        """
        pass

    def set_auto_flip(self, const_GraphicsEngine_self, bool_auto_flip): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_auto_flip(const GraphicsEngine self, bool auto_flip)
        
        /**
         * Set this flag true to indicate the GraphicsEngine should automatically
         * cause windows to sync and flip as soon as they have finished drawing,
         * rather than waiting for all of the windows to finish drawing first so they
         * can flip together.
         *
         * This only affects the timing of when the flip occurs.  If this is true (the
         * default), the flip occurs before render_frame() returns.  If this is false,
         * the flip occurs whenever flip_frame() is called, or at the beginning of the
         * next call to render_frame(), if flip_frame() is never called.
         */
        """
        pass

    def set_default_loader(self, const_GraphicsEngine_self, Loader_loader): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_default_loader(const GraphicsEngine self, Loader loader)
        
        /**
         * Sets the Loader object that will be assigned to every GSG created with this
         * GraphicsEngine.  See GraphicsStateGuardian::set_loader().
         */
        """
        pass

    def set_portal_cull(self, const_GraphicsEngine_self, bool_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_portal_cull(const GraphicsEngine self, bool value)
        
        /**
         * Set this flag true to indicate the GraphicsEngine should start portal
         * culling
         */
        """
        pass

    def set_threading_model(self, const_GraphicsEngine_self, const_GraphicsThreadingModel_threading_model): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_threading_model(const GraphicsEngine self, const GraphicsThreadingModel threading_model)
        
        /**
         * Specifies how future objects created via make_gsg(), make_buffer(), and
         * make_output() will be threaded.  This does not affect any already-created
         * objects.
         */
        """
        pass

    def syncFrame(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        sync_frame(const GraphicsEngine self)
        
        /**
         * Waits for all the threads that started drawing their last frame to finish
         * drawing.  The windows are not yet flipped when this returns; see also
         * flip_frame(). It is not usually necessary to call this explicitly, unless
         * you need to see the previous frame right away.
         */
        """
        pass

    def sync_frame(self, const_GraphicsEngine_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        sync_frame(const GraphicsEngine self)
        
        /**
         * Waits for all the threads that started drawing their last frame to finish
         * drawing.  The windows are not yet flipped when this returns; see also
         * flip_frame(). It is not usually necessary to call this explicitly, unless
         * you need to see the previous frame right away.
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    auto_flip = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    default_loader = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    portal_cull = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    render_lock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    threading_model = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    windows = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * This class is the main interface to controlling the render process.  There\n * is typically only one GraphicsEngine in an application, and it synchronizes\n * rendering to all all of the active windows; although it is possible to have\n * multiple GraphicsEngine objects if multiple synchronicity groups are\n * required.\n *\n * The GraphicsEngine is responsible for managing the various cull and draw\n * threads.  The application simply calls engine->render_frame() and considers\n * it done.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.GraphicsEngine' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2DDAA0>'
        'addWindow': None, # (!) real value is "<method 'addWindow' of 'panda3d.core.GraphicsEngine' objects>"
        'add_window': None, # (!) real value is "<method 'add_window' of 'panda3d.core.GraphicsEngine' objects>"
        'auto_flip': None, # (!) real value is "<attribute 'auto_flip' of 'panda3d.core.GraphicsEngine' objects>"
        'default_loader': None, # (!) real value is "<attribute 'default_loader' of 'panda3d.core.GraphicsEngine' objects>"
        'dispatchCompute': None, # (!) real value is "<method 'dispatchCompute' of 'panda3d.core.GraphicsEngine' objects>"
        'dispatch_compute': None, # (!) real value is "<method 'dispatch_compute' of 'panda3d.core.GraphicsEngine' objects>"
        'extractTextureData': None, # (!) real value is "<method 'extractTextureData' of 'panda3d.core.GraphicsEngine' objects>"
        'extract_texture_data': None, # (!) real value is "<method 'extract_texture_data' of 'panda3d.core.GraphicsEngine' objects>"
        'flipFrame': None, # (!) real value is "<method 'flipFrame' of 'panda3d.core.GraphicsEngine' objects>"
        'flip_frame': None, # (!) real value is "<method 'flip_frame' of 'panda3d.core.GraphicsEngine' objects>"
        'getAutoFlip': None, # (!) real value is "<method 'getAutoFlip' of 'panda3d.core.GraphicsEngine' objects>"
        'getDefaultLoader': None, # (!) real value is "<method 'getDefaultLoader' of 'panda3d.core.GraphicsEngine' objects>"
        'getGlobalPtr': None, # (!) real value is '<staticmethod(<built-in method getGlobalPtr of type object at 0x00007FFCFE2DDAA0>)>'
        'getNumWindows': None, # (!) real value is "<method 'getNumWindows' of 'panda3d.core.GraphicsEngine' objects>"
        'getPortalCull': None, # (!) real value is "<method 'getPortalCull' of 'panda3d.core.GraphicsEngine' objects>"
        'getRenderLock': None, # (!) real value is "<method 'getRenderLock' of 'panda3d.core.GraphicsEngine' objects>"
        'getThreadingModel': None, # (!) real value is "<method 'getThreadingModel' of 'panda3d.core.GraphicsEngine' objects>"
        'getWindow': None, # (!) real value is "<method 'getWindow' of 'panda3d.core.GraphicsEngine' objects>"
        'getWindows': None, # (!) real value is "<method 'getWindows' of 'panda3d.core.GraphicsEngine' objects>"
        'get_auto_flip': None, # (!) real value is "<method 'get_auto_flip' of 'panda3d.core.GraphicsEngine' objects>"
        'get_default_loader': None, # (!) real value is "<method 'get_default_loader' of 'panda3d.core.GraphicsEngine' objects>"
        'get_global_ptr': None, # (!) real value is '<staticmethod(<built-in method get_global_ptr of type object at 0x00007FFCFE2DDAA0>)>'
        'get_num_windows': None, # (!) real value is "<method 'get_num_windows' of 'panda3d.core.GraphicsEngine' objects>"
        'get_portal_cull': None, # (!) real value is "<method 'get_portal_cull' of 'panda3d.core.GraphicsEngine' objects>"
        'get_render_lock': None, # (!) real value is "<method 'get_render_lock' of 'panda3d.core.GraphicsEngine' objects>"
        'get_threading_model': None, # (!) real value is "<method 'get_threading_model' of 'panda3d.core.GraphicsEngine' objects>"
        'get_window': None, # (!) real value is "<method 'get_window' of 'panda3d.core.GraphicsEngine' objects>"
        'get_windows': None, # (!) real value is "<method 'get_windows' of 'panda3d.core.GraphicsEngine' objects>"
        'isEmpty': None, # (!) real value is "<method 'isEmpty' of 'panda3d.core.GraphicsEngine' objects>"
        'is_empty': None, # (!) real value is "<method 'is_empty' of 'panda3d.core.GraphicsEngine' objects>"
        'makeBuffer': None, # (!) real value is "<method 'makeBuffer' of 'panda3d.core.GraphicsEngine' objects>"
        'makeOutput': None, # (!) real value is "<method 'makeOutput' of 'panda3d.core.GraphicsEngine' objects>"
        'makeParasite': None, # (!) real value is "<method 'makeParasite' of 'panda3d.core.GraphicsEngine' objects>"
        'make_buffer': None, # (!) real value is "<method 'make_buffer' of 'panda3d.core.GraphicsEngine' objects>"
        'make_output': None, # (!) real value is "<method 'make_output' of 'panda3d.core.GraphicsEngine' objects>"
        'make_parasite': None, # (!) real value is "<method 'make_parasite' of 'panda3d.core.GraphicsEngine' objects>"
        'openWindows': None, # (!) real value is "<method 'openWindows' of 'panda3d.core.GraphicsEngine' objects>"
        'open_windows': None, # (!) real value is "<method 'open_windows' of 'panda3d.core.GraphicsEngine' objects>"
        'portal_cull': None, # (!) real value is "<attribute 'portal_cull' of 'panda3d.core.GraphicsEngine' objects>"
        'readyFlip': None, # (!) real value is "<method 'readyFlip' of 'panda3d.core.GraphicsEngine' objects>"
        'ready_flip': None, # (!) real value is "<method 'ready_flip' of 'panda3d.core.GraphicsEngine' objects>"
        'removeAllWindows': None, # (!) real value is "<method 'removeAllWindows' of 'panda3d.core.GraphicsEngine' objects>"
        'removeWindow': None, # (!) real value is "<method 'removeWindow' of 'panda3d.core.GraphicsEngine' objects>"
        'remove_all_windows': None, # (!) real value is "<method 'remove_all_windows' of 'panda3d.core.GraphicsEngine' objects>"
        'remove_window': None, # (!) real value is "<method 'remove_window' of 'panda3d.core.GraphicsEngine' objects>"
        'renderFrame': None, # (!) real value is "<method 'renderFrame' of 'panda3d.core.GraphicsEngine' objects>"
        'render_frame': None, # (!) real value is "<method 'render_frame' of 'panda3d.core.GraphicsEngine' objects>"
        'render_lock': None, # (!) real value is "<attribute 'render_lock' of 'panda3d.core.GraphicsEngine' objects>"
        'resetAllWindows': None, # (!) real value is "<method 'resetAllWindows' of 'panda3d.core.GraphicsEngine' objects>"
        'reset_all_windows': None, # (!) real value is "<method 'reset_all_windows' of 'panda3d.core.GraphicsEngine' objects>"
        'setAutoFlip': None, # (!) real value is "<method 'setAutoFlip' of 'panda3d.core.GraphicsEngine' objects>"
        'setDefaultLoader': None, # (!) real value is "<method 'setDefaultLoader' of 'panda3d.core.GraphicsEngine' objects>"
        'setPortalCull': None, # (!) real value is "<method 'setPortalCull' of 'panda3d.core.GraphicsEngine' objects>"
        'setThreadingModel': None, # (!) real value is "<method 'setThreadingModel' of 'panda3d.core.GraphicsEngine' objects>"
        'set_auto_flip': None, # (!) real value is "<method 'set_auto_flip' of 'panda3d.core.GraphicsEngine' objects>"
        'set_default_loader': None, # (!) real value is "<method 'set_default_loader' of 'panda3d.core.GraphicsEngine' objects>"
        'set_portal_cull': None, # (!) real value is "<method 'set_portal_cull' of 'panda3d.core.GraphicsEngine' objects>"
        'set_threading_model': None, # (!) real value is "<method 'set_threading_model' of 'panda3d.core.GraphicsEngine' objects>"
        'syncFrame': None, # (!) real value is "<method 'syncFrame' of 'panda3d.core.GraphicsEngine' objects>"
        'sync_frame': None, # (!) real value is "<method 'sync_frame' of 'panda3d.core.GraphicsEngine' objects>"
        'threading_model': None, # (!) real value is "<attribute 'threading_model' of 'panda3d.core.GraphicsEngine' objects>"
        'windows': None, # (!) real value is "<attribute 'windows' of 'panda3d.core.GraphicsEngine' objects>"
    }


