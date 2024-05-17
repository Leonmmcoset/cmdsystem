# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class DrawableRegion(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * This is a base class for GraphicsWindow (actually, GraphicsOutput) and
     * DisplayRegion, both of which are conceptually rectangular regions into
     * which drawing commands may be issued.  Sometimes you want to deal with a
     * single display region, and sometimes you want to deal with the whole window
     * at once, particularly for issuing clear commands and capturing screenshots.
     */
    """
    def disableClears(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        disable_clears(const DrawableRegion self)
        
        /**
         * Disables both the color and depth clear.  See set_clear_color_active and
         * set_clear_depth_active.
         */
        """
        pass

    def disable_clears(self, const_DrawableRegion_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        disable_clears(const DrawableRegion self)
        
        /**
         * Disables both the color and depth clear.  See set_clear_color_active and
         * set_clear_depth_active.
         */
        """
        pass

    def getClearActive(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_clear_active(DrawableRegion self, int n)
        
        /**
         * Gets the clear-active flag for any bitplane.
         */
        """
        pass

    def getClearColor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_clear_color(DrawableRegion self)
        
        /**
         * Returns the current clear color value.  This is the value that will be used
         * to clear the color buffer every frame, but only if get_clear_color_active()
         * returns true.  If get_clear_color_active() returns false, this is
         * meaningless.
         */
        """
        pass

    def getClearColorActive(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_clear_color_active(DrawableRegion self)
        
        /**
         * Returns the current setting of the flag that indicates whether the color
         * buffer should be cleared every frame.  See set_clear_color_active().
         */
        """
        pass

    def getClearDepth(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_clear_depth(DrawableRegion self)
        
        /**
         * Returns the current clear depth value.  This is the value that will be used
         * to clear the depth buffer every frame, but only if get_clear_depth_active()
         * returns true.  If get_clear_depth_active() returns false, this is
         * meaningless.
         */
        """
        pass

    def getClearDepthActive(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_clear_depth_active(DrawableRegion self)
        
        /**
         * Returns the current setting of the flag that indicates whether the depth
         * buffer should be cleared every frame.  See set_clear_depth_active().
         */
        """
        pass

    def getClearStencil(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_clear_stencil(DrawableRegion self)
        
        /**
         * Returns the current clear stencil value.  This is the value that will be
         * used to clear the stencil buffer every frame, but only if
         * get_clear_stencil_active() returns true.  If get_clear_stencil_active()
         * returns false, this is meaningless.
         */
        """
        pass

    def getClearStencilActive(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_clear_stencil_active(DrawableRegion self)
        
        /**
         * Returns the current setting of the flag that indicates whether the color
         * buffer should be cleared every frame.  See set_clear_stencil_active().
         */
        """
        pass

    def getClearValue(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_clear_value(DrawableRegion self, int n)
        
        /**
         * Returns the clear value for any bitplane.
         */
        """
        pass

    def getPixelFactor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_pixel_factor(DrawableRegion self)
        
        /**
         * Returns the amount by which the height and width of the region will be
         * scaled internally, based on the zoom factor set by set_pixel_zoom().  This
         * will return 1.0 if the pixel_zoom was not set or if it is not being
         * respected (for instance, because the underlying renderer doesn't support it
         * --see supports_pixel_zoom).
         */
        """
        pass

    def getPixelZoom(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_pixel_zoom(DrawableRegion self)
        
        /**
         * Returns the value set by set_pixel_zoom(), regardless of whether it is
         * being respected or not.  Also see get_pixel_factor().
         */
        """
        pass

    def getRenderbufferType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_renderbuffer_type(int plane)
        
        /**
         * Returns the RenderBuffer::Type that corresponds to a RenderTexturePlane.
         */
        """
        pass

    def get_clear_active(self, DrawableRegion_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_clear_active(DrawableRegion self, int n)
        
        /**
         * Gets the clear-active flag for any bitplane.
         */
        """
        pass

    def get_clear_color(self, DrawableRegion_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_clear_color(DrawableRegion self)
        
        /**
         * Returns the current clear color value.  This is the value that will be used
         * to clear the color buffer every frame, but only if get_clear_color_active()
         * returns true.  If get_clear_color_active() returns false, this is
         * meaningless.
         */
        """
        pass

    def get_clear_color_active(self, DrawableRegion_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_clear_color_active(DrawableRegion self)
        
        /**
         * Returns the current setting of the flag that indicates whether the color
         * buffer should be cleared every frame.  See set_clear_color_active().
         */
        """
        pass

    def get_clear_depth(self, DrawableRegion_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_clear_depth(DrawableRegion self)
        
        /**
         * Returns the current clear depth value.  This is the value that will be used
         * to clear the depth buffer every frame, but only if get_clear_depth_active()
         * returns true.  If get_clear_depth_active() returns false, this is
         * meaningless.
         */
        """
        pass

    def get_clear_depth_active(self, DrawableRegion_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_clear_depth_active(DrawableRegion self)
        
        /**
         * Returns the current setting of the flag that indicates whether the depth
         * buffer should be cleared every frame.  See set_clear_depth_active().
         */
        """
        pass

    def get_clear_stencil(self, DrawableRegion_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_clear_stencil(DrawableRegion self)
        
        /**
         * Returns the current clear stencil value.  This is the value that will be
         * used to clear the stencil buffer every frame, but only if
         * get_clear_stencil_active() returns true.  If get_clear_stencil_active()
         * returns false, this is meaningless.
         */
        """
        pass

    def get_clear_stencil_active(self, DrawableRegion_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_clear_stencil_active(DrawableRegion self)
        
        /**
         * Returns the current setting of the flag that indicates whether the color
         * buffer should be cleared every frame.  See set_clear_stencil_active().
         */
        """
        pass

    def get_clear_value(self, DrawableRegion_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_clear_value(DrawableRegion self, int n)
        
        /**
         * Returns the clear value for any bitplane.
         */
        """
        pass

    def get_pixel_factor(self, DrawableRegion_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_pixel_factor(DrawableRegion self)
        
        /**
         * Returns the amount by which the height and width of the region will be
         * scaled internally, based on the zoom factor set by set_pixel_zoom().  This
         * will return 1.0 if the pixel_zoom was not set or if it is not being
         * respected (for instance, because the underlying renderer doesn't support it
         * --see supports_pixel_zoom).
         */
        """
        pass

    def get_pixel_zoom(self, DrawableRegion_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_pixel_zoom(DrawableRegion self)
        
        /**
         * Returns the value set by set_pixel_zoom(), regardless of whether it is
         * being respected or not.  Also see get_pixel_factor().
         */
        """
        pass

    def get_renderbuffer_type(self, int_plane): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_renderbuffer_type(int plane)
        
        /**
         * Returns the RenderBuffer::Type that corresponds to a RenderTexturePlane.
         */
        """
        pass

    def isAnyClearActive(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_any_clear_active(DrawableRegion self)
        
        /**
         * Returns true if any of the clear types (so far there are just color or
         * depth) have been set active, or false if none of them are active and there
         * is no need to clear.
         */
        """
        pass

    def is_any_clear_active(self, DrawableRegion_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_any_clear_active(DrawableRegion self)
        
        /**
         * Returns true if any of the clear types (so far there are just color or
         * depth) have been set active, or false if none of them are active and there
         * is no need to clear.
         */
        """
        pass

    def setClearActive(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_clear_active(const DrawableRegion self, int n, bool clear_aux_active)
        
        /**
         * Sets the clear-active flag for any bitplane.
         */
        """
        pass

    def setClearColor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_clear_color(const DrawableRegion self, const LVecBase4f color)
        
        /**
         * Sets the clear color to the indicated value.  This is the value that will
         * be used to clear the color buffer every frame, but only if
         * get_clear_color_active() returns true.  If get_clear_color_active() returns
         * false, this is meaningless.
         */
        """
        pass

    def setClearColorActive(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_clear_color_active(const DrawableRegion self, bool clear_color_active)
        
        /**
         * Toggles the flag that indicates whether the color buffer should be cleared
         * every frame.  If this is true, the color buffer will be cleared to the
         * color indicated by set_clear_color(); otherwise, it will be left alone.
         */
        """
        pass

    def setClearDepth(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_clear_depth(const DrawableRegion self, float depth)
        
        /**
         * Sets the clear depth to the indicated value.  This is the value that will
         * be used to clear the depth buffer every frame, but only if
         * get_clear_depth_active() returns true.  If get_clear_depth_active() returns
         * false, this is meaningless.
         */
        """
        pass

    def setClearDepthActive(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_clear_depth_active(const DrawableRegion self, bool clear_depth_active)
        
        /**
         * Toggles the flag that indicates whether the depth buffer should be cleared
         * every frame.  If this is true, the depth buffer will be cleared to the
         * depth value indicated by set_clear_depth(); otherwise, it will be left
         * alone.
         */
        """
        pass

    def setClearStencil(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_clear_stencil(const DrawableRegion self, int stencil)
        
        /**
         * Sets the clear stencil to the indicated value.  This is the value that will
         * be used to clear the stencil buffer every frame, but only if
         * get_clear_color_active() returns true.  If get_clear_stencil_active()
         * returns false, this is meaningless.
         */
        """
        pass

    def setClearStencilActive(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_clear_stencil_active(const DrawableRegion self, bool clear_stencil_active)
        
        /**
         * Toggles the flag that indicates whether the stencil buffer should be
         * cleared every frame.  If this is true, the stencil buffer will be cleared
         * to the value indicated by set_clear_stencil(); otherwise, it will be left
         * alone.
         */
        """
        pass

    def setClearValue(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_clear_value(const DrawableRegion self, int n, const LVecBase4f clear_value)
        
        /**
         * Sets the clear value for any bitplane.
         */
        """
        pass

    def setPixelZoom(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_pixel_zoom(const DrawableRegion self, float pixel_zoom)
        
        /**
         * Sets the amount by which the pixels of the region are scaled internally
         * when filling the image interally.  Setting this number larger makes the
         * pixels blockier, but may make the rendering faster, particularly for
         * software renderers.  Setting this number to 2.0 reduces the number of
         * pixels that have to be filled by the renderer by a factor of 2.0.  It
         * doesn't make sense to set this lower than 1.0.
         *
         * It is possible to set this on either individual DisplayRegions or on
         * overall GraphicsWindows, but you will get better performance for setting it
         * on the window rather than its individual DisplayRegions.  Also, you may not
         * set it on a DisplayRegion that doesn't have both clear_color() and
         * clear_depth() enabled.
         *
         * This property is only supported on renderers for which it is particularly
         * useful--currently, this is the tinydisplay software renderer.  Other kinds
         * of renderers allow you to set this property, but ignore it.
         */
        """
        pass

    def set_clear_active(self, const_DrawableRegion_self, int_n, bool_clear_aux_active): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_clear_active(const DrawableRegion self, int n, bool clear_aux_active)
        
        /**
         * Sets the clear-active flag for any bitplane.
         */
        """
        pass

    def set_clear_color(self, const_DrawableRegion_self, const_LVecBase4f_color): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_clear_color(const DrawableRegion self, const LVecBase4f color)
        
        /**
         * Sets the clear color to the indicated value.  This is the value that will
         * be used to clear the color buffer every frame, but only if
         * get_clear_color_active() returns true.  If get_clear_color_active() returns
         * false, this is meaningless.
         */
        """
        pass

    def set_clear_color_active(self, const_DrawableRegion_self, bool_clear_color_active): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_clear_color_active(const DrawableRegion self, bool clear_color_active)
        
        /**
         * Toggles the flag that indicates whether the color buffer should be cleared
         * every frame.  If this is true, the color buffer will be cleared to the
         * color indicated by set_clear_color(); otherwise, it will be left alone.
         */
        """
        pass

    def set_clear_depth(self, const_DrawableRegion_self, float_depth): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_clear_depth(const DrawableRegion self, float depth)
        
        /**
         * Sets the clear depth to the indicated value.  This is the value that will
         * be used to clear the depth buffer every frame, but only if
         * get_clear_depth_active() returns true.  If get_clear_depth_active() returns
         * false, this is meaningless.
         */
        """
        pass

    def set_clear_depth_active(self, const_DrawableRegion_self, bool_clear_depth_active): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_clear_depth_active(const DrawableRegion self, bool clear_depth_active)
        
        /**
         * Toggles the flag that indicates whether the depth buffer should be cleared
         * every frame.  If this is true, the depth buffer will be cleared to the
         * depth value indicated by set_clear_depth(); otherwise, it will be left
         * alone.
         */
        """
        pass

    def set_clear_stencil(self, const_DrawableRegion_self, int_stencil): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_clear_stencil(const DrawableRegion self, int stencil)
        
        /**
         * Sets the clear stencil to the indicated value.  This is the value that will
         * be used to clear the stencil buffer every frame, but only if
         * get_clear_color_active() returns true.  If get_clear_stencil_active()
         * returns false, this is meaningless.
         */
        """
        pass

    def set_clear_stencil_active(self, const_DrawableRegion_self, bool_clear_stencil_active): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_clear_stencil_active(const DrawableRegion self, bool clear_stencil_active)
        
        /**
         * Toggles the flag that indicates whether the stencil buffer should be
         * cleared every frame.  If this is true, the stencil buffer will be cleared
         * to the value indicated by set_clear_stencil(); otherwise, it will be left
         * alone.
         */
        """
        pass

    def set_clear_value(self, const_DrawableRegion_self, int_n, const_LVecBase4f_clear_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_clear_value(const DrawableRegion self, int n, const LVecBase4f clear_value)
        
        /**
         * Sets the clear value for any bitplane.
         */
        """
        pass

    def set_pixel_zoom(self, const_DrawableRegion_self, float_pixel_zoom): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_pixel_zoom(const DrawableRegion self, float pixel_zoom)
        
        /**
         * Sets the amount by which the pixels of the region are scaled internally
         * when filling the image interally.  Setting this number larger makes the
         * pixels blockier, but may make the rendering faster, particularly for
         * software renderers.  Setting this number to 2.0 reduces the number of
         * pixels that have to be filled by the renderer by a factor of 2.0.  It
         * doesn't make sense to set this lower than 1.0.
         *
         * It is possible to set this on either individual DisplayRegions or on
         * overall GraphicsWindows, but you will get better performance for setting it
         * on the window rather than its individual DisplayRegions.  Also, you may not
         * set it on a DisplayRegion that doesn't have both clear_color() and
         * clear_depth() enabled.
         *
         * This property is only supported on renderers for which it is particularly
         * useful--currently, this is the tinydisplay software renderer.  Other kinds
         * of renderers allow you to set this property, but ignore it.
         */
        """
        pass

    def supportsPixelZoom(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        supports_pixel_zoom(DrawableRegion self)
        
        /**
         * Returns true if a call to set_pixel_zoom() will be respected, false if it
         * will be ignored.  If this returns false, then get_pixel_factor() will
         * always return 1.0, regardless of what value you specify for
         * set_pixel_zoom().
         *
         * This may return false if the underlying renderer doesn't support pixel
         * zooming, or if you have called this on a DisplayRegion that doesn't have
         * both set_clear_color() and set_clear_depth() enabled.
         */
        """
        pass

    def supports_pixel_zoom(self, DrawableRegion_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        supports_pixel_zoom(DrawableRegion self)
        
        /**
         * Returns true if a call to set_pixel_zoom() will be respected, false if it
         * will be ignored.  If this returns false, then get_pixel_factor() will
         * always return 1.0, regardless of what value you specify for
         * set_pixel_zoom().
         *
         * This may return false if the underlying renderer doesn't support pixel
         * zooming, or if you have called this on a DisplayRegion that doesn't have
         * both set_clear_color() and set_clear_depth() enabled.
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    clear_color = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    clear_depth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    clear_stencil = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pixel_factor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pixel_zoom = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        'RTPAuxFloat0': 11,
        'RTPAuxFloat1': 12,
        'RTPAuxFloat2': 13,
        'RTPAuxFloat3': 14,
        'RTPAuxHrgba0': 7,
        'RTPAuxHrgba1': 8,
        'RTPAuxHrgba2': 9,
        'RTPAuxHrgba3': 10,
        'RTPAuxRgba0': 3,
        'RTPAuxRgba1': 4,
        'RTPAuxRgba2': 5,
        'RTPAuxRgba3': 6,
        'RTPCOUNT': 16,
        'RTPColor': 2,
        'RTPDepth': 15,
        'RTPDepthStencil': 1,
        'RTPStencil': 0,
        'RTP_COUNT': 16,
        'RTP_aux_float_0': 11,
        'RTP_aux_float_1': 12,
        'RTP_aux_float_2': 13,
        'RTP_aux_float_3': 14,
        'RTP_aux_hrgba_0': 7,
        'RTP_aux_hrgba_1': 8,
        'RTP_aux_hrgba_2': 9,
        'RTP_aux_hrgba_3': 10,
        'RTP_aux_rgba_0': 3,
        'RTP_aux_rgba_1': 4,
        'RTP_aux_rgba_2': 5,
        'RTP_aux_rgba_3': 6,
        'RTP_color': 2,
        'RTP_depth': 15,
        'RTP_depth_stencil': 1,
        'RTP_stencil': 0,
        '__doc__': '/**\n * This is a base class for GraphicsWindow (actually, GraphicsOutput) and\n * DisplayRegion, both of which are conceptually rectangular regions into\n * which drawing commands may be issued.  Sometimes you want to deal with a\n * single display region, and sometimes you want to deal with the whole window\n * at once, particularly for issuing clear commands and capturing screenshots.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.DrawableRegion' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2DCDF0>'
        'clear_color': None, # (!) real value is "<attribute 'clear_color' of 'panda3d.core.DrawableRegion' objects>"
        'clear_depth': None, # (!) real value is "<attribute 'clear_depth' of 'panda3d.core.DrawableRegion' objects>"
        'clear_stencil': None, # (!) real value is "<attribute 'clear_stencil' of 'panda3d.core.DrawableRegion' objects>"
        'disableClears': None, # (!) real value is "<method 'disableClears' of 'panda3d.core.DrawableRegion' objects>"
        'disable_clears': None, # (!) real value is "<method 'disable_clears' of 'panda3d.core.DrawableRegion' objects>"
        'getClearActive': None, # (!) real value is "<method 'getClearActive' of 'panda3d.core.DrawableRegion' objects>"
        'getClearColor': None, # (!) real value is "<method 'getClearColor' of 'panda3d.core.DrawableRegion' objects>"
        'getClearColorActive': None, # (!) real value is "<method 'getClearColorActive' of 'panda3d.core.DrawableRegion' objects>"
        'getClearDepth': None, # (!) real value is "<method 'getClearDepth' of 'panda3d.core.DrawableRegion' objects>"
        'getClearDepthActive': None, # (!) real value is "<method 'getClearDepthActive' of 'panda3d.core.DrawableRegion' objects>"
        'getClearStencil': None, # (!) real value is "<method 'getClearStencil' of 'panda3d.core.DrawableRegion' objects>"
        'getClearStencilActive': None, # (!) real value is "<method 'getClearStencilActive' of 'panda3d.core.DrawableRegion' objects>"
        'getClearValue': None, # (!) real value is "<method 'getClearValue' of 'panda3d.core.DrawableRegion' objects>"
        'getPixelFactor': None, # (!) real value is "<method 'getPixelFactor' of 'panda3d.core.DrawableRegion' objects>"
        'getPixelZoom': None, # (!) real value is "<method 'getPixelZoom' of 'panda3d.core.DrawableRegion' objects>"
        'getRenderbufferType': None, # (!) real value is '<staticmethod(<built-in method getRenderbufferType of type object at 0x00007FFCFE2DCDF0>)>'
        'get_clear_active': None, # (!) real value is "<method 'get_clear_active' of 'panda3d.core.DrawableRegion' objects>"
        'get_clear_color': None, # (!) real value is "<method 'get_clear_color' of 'panda3d.core.DrawableRegion' objects>"
        'get_clear_color_active': None, # (!) real value is "<method 'get_clear_color_active' of 'panda3d.core.DrawableRegion' objects>"
        'get_clear_depth': None, # (!) real value is "<method 'get_clear_depth' of 'panda3d.core.DrawableRegion' objects>"
        'get_clear_depth_active': None, # (!) real value is "<method 'get_clear_depth_active' of 'panda3d.core.DrawableRegion' objects>"
        'get_clear_stencil': None, # (!) real value is "<method 'get_clear_stencil' of 'panda3d.core.DrawableRegion' objects>"
        'get_clear_stencil_active': None, # (!) real value is "<method 'get_clear_stencil_active' of 'panda3d.core.DrawableRegion' objects>"
        'get_clear_value': None, # (!) real value is "<method 'get_clear_value' of 'panda3d.core.DrawableRegion' objects>"
        'get_pixel_factor': None, # (!) real value is "<method 'get_pixel_factor' of 'panda3d.core.DrawableRegion' objects>"
        'get_pixel_zoom': None, # (!) real value is "<method 'get_pixel_zoom' of 'panda3d.core.DrawableRegion' objects>"
        'get_renderbuffer_type': None, # (!) real value is '<staticmethod(<built-in method get_renderbuffer_type of type object at 0x00007FFCFE2DCDF0>)>'
        'isAnyClearActive': None, # (!) real value is "<method 'isAnyClearActive' of 'panda3d.core.DrawableRegion' objects>"
        'is_any_clear_active': None, # (!) real value is "<method 'is_any_clear_active' of 'panda3d.core.DrawableRegion' objects>"
        'pixel_factor': None, # (!) real value is "<attribute 'pixel_factor' of 'panda3d.core.DrawableRegion' objects>"
        'pixel_zoom': None, # (!) real value is "<attribute 'pixel_zoom' of 'panda3d.core.DrawableRegion' objects>"
        'setClearActive': None, # (!) real value is "<method 'setClearActive' of 'panda3d.core.DrawableRegion' objects>"
        'setClearColor': None, # (!) real value is "<method 'setClearColor' of 'panda3d.core.DrawableRegion' objects>"
        'setClearColorActive': None, # (!) real value is "<method 'setClearColorActive' of 'panda3d.core.DrawableRegion' objects>"
        'setClearDepth': None, # (!) real value is "<method 'setClearDepth' of 'panda3d.core.DrawableRegion' objects>"
        'setClearDepthActive': None, # (!) real value is "<method 'setClearDepthActive' of 'panda3d.core.DrawableRegion' objects>"
        'setClearStencil': None, # (!) real value is "<method 'setClearStencil' of 'panda3d.core.DrawableRegion' objects>"
        'setClearStencilActive': None, # (!) real value is "<method 'setClearStencilActive' of 'panda3d.core.DrawableRegion' objects>"
        'setClearValue': None, # (!) real value is "<method 'setClearValue' of 'panda3d.core.DrawableRegion' objects>"
        'setPixelZoom': None, # (!) real value is "<method 'setPixelZoom' of 'panda3d.core.DrawableRegion' objects>"
        'set_clear_active': None, # (!) real value is "<method 'set_clear_active' of 'panda3d.core.DrawableRegion' objects>"
        'set_clear_color': None, # (!) real value is "<method 'set_clear_color' of 'panda3d.core.DrawableRegion' objects>"
        'set_clear_color_active': None, # (!) real value is "<method 'set_clear_color_active' of 'panda3d.core.DrawableRegion' objects>"
        'set_clear_depth': None, # (!) real value is "<method 'set_clear_depth' of 'panda3d.core.DrawableRegion' objects>"
        'set_clear_depth_active': None, # (!) real value is "<method 'set_clear_depth_active' of 'panda3d.core.DrawableRegion' objects>"
        'set_clear_stencil': None, # (!) real value is "<method 'set_clear_stencil' of 'panda3d.core.DrawableRegion' objects>"
        'set_clear_stencil_active': None, # (!) real value is "<method 'set_clear_stencil_active' of 'panda3d.core.DrawableRegion' objects>"
        'set_clear_value': None, # (!) real value is "<method 'set_clear_value' of 'panda3d.core.DrawableRegion' objects>"
        'set_pixel_zoom': None, # (!) real value is "<method 'set_pixel_zoom' of 'panda3d.core.DrawableRegion' objects>"
        'supportsPixelZoom': None, # (!) real value is "<method 'supportsPixelZoom' of 'panda3d.core.DrawableRegion' objects>"
        'supports_pixel_zoom': None, # (!) real value is "<method 'supports_pixel_zoom' of 'panda3d.core.DrawableRegion' objects>"
    }
    RTPAuxFloat0 = 11
    RTPAuxFloat1 = 12
    RTPAuxFloat2 = 13
    RTPAuxFloat3 = 14
    RTPAuxHrgba0 = 7
    RTPAuxHrgba1 = 8
    RTPAuxHrgba2 = 9
    RTPAuxHrgba3 = 10
    RTPAuxRgba0 = 3
    RTPAuxRgba1 = 4
    RTPAuxRgba2 = 5
    RTPAuxRgba3 = 6
    RTPColor = 2
    RTPCOUNT = 16
    RTPDepth = 15
    RTPDepthStencil = 1
    RTPStencil = 0
    RTP_aux_float_0 = 11
    RTP_aux_float_1 = 12
    RTP_aux_float_2 = 13
    RTP_aux_float_3 = 14
    RTP_aux_hrgba_0 = 7
    RTP_aux_hrgba_1 = 8
    RTP_aux_hrgba_2 = 9
    RTP_aux_hrgba_3 = 10
    RTP_aux_rgba_0 = 3
    RTP_aux_rgba_1 = 4
    RTP_aux_rgba_2 = 5
    RTP_aux_rgba_3 = 6
    RTP_color = 2
    RTP_COUNT = 16
    RTP_depth = 15
    RTP_depth_stencil = 1
    RTP_stencil = 0


