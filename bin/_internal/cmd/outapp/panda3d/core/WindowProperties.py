# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class WindowProperties(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * A container for the various kinds of properties we might ask to have on a
     * graphics window before we open it.  This also serves to hold the current
     * properties for a window after it has been opened.
     */
    """
    def addProperties(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_properties(const WindowProperties self, const WindowProperties other)
        
        /**
         * Sets any properties that are explicitly specified in other on this object.
         * Leaves other properties unchanged.
         */
        """
        pass

    def add_properties(self, const_WindowProperties_self, const_WindowProperties_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_properties(const WindowProperties self, const WindowProperties other)
        
        /**
         * Sets any properties that are explicitly specified in other on this object.
         * Leaves other properties unchanged.
         */
        """
        pass

    def assign(self, const_WindowProperties_self, const_WindowProperties_copy): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        assign(const WindowProperties self, const WindowProperties copy)
        """
        pass

    def clear(self, const_WindowProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear(const WindowProperties self)
        
        /**
         * Unsets all properties that have been specified so far, and resets the
         * WindowProperties structure to its initial empty state.
         */
        """
        pass

    def clearCursorFilename(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_cursor_filename(const WindowProperties self)
        
        /**
         * Removes the cursor_filename specification from the properties.
         */
        """
        pass

    def clearCursorHidden(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_cursor_hidden(const WindowProperties self)
        
        /**
         * Removes the cursor_hidden specification from the properties.
         */
        """
        pass

    def clearDefault(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_default()
        
        /**
         * Returns the "default" WindowProperties to whatever is specified in the
         * user's config file.
         */
        """
        pass

    def clearFixedSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_fixed_size(const WindowProperties self)
        
        /**
         * Removes the fixed_size specification from the properties.
         */
        """
        pass

    def clearForeground(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_foreground(const WindowProperties self)
        
        /**
         * Removes the foreground specification from the properties.
         */
        """
        pass

    def clearFullscreen(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_fullscreen(const WindowProperties self)
        
        /**
         * Removes the fullscreen specification from the properties.
         */
        """
        pass

    def clearIconFilename(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_icon_filename(const WindowProperties self)
        
        /**
         * Removes the icon_filename specification from the properties.
         */
        """
        pass

    def clearMinimized(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_minimized(const WindowProperties self)
        
        /**
         * Removes the minimized specification from the properties.
         */
        """
        pass

    def clearMouseMode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_mouse_mode(const WindowProperties self)
        
        /**
         * Removes the mouse_mode specification from the properties.
         */
        """
        pass

    def clearOpen(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_open(const WindowProperties self)
        
        /**
         * Removes the open specification from the properties.
         */
        """
        pass

    def clearOrigin(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_origin(const WindowProperties self)
        
        /**
         * Removes the origin specification from the properties.
         */
        """
        pass

    def clearParentWindow(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_parent_window(const WindowProperties self)
        
        /**
         * Removes the S_parent_window specification from the properties.
         */
        """
        pass

    def clearRawMice(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_raw_mice(const WindowProperties self)
        
        /**
         * Removes the raw_mice specification from the properties.
         */
        """
        pass

    def clearSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_size(const WindowProperties self)
        
        /**
         * Removes the size specification from the properties.
         */
        """
        pass

    def clearTitle(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_title(const WindowProperties self)
        
        /**
         * Removes the title specification from the properties.
         */
        """
        pass

    def clearUndecorated(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_undecorated(const WindowProperties self)
        
        /**
         * Removes the undecorated specification from the properties.
         */
        """
        pass

    def clearZOrder(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_z_order(const WindowProperties self)
        
        /**
         * Removes the z_order specification from the properties.
         */
        """
        pass

    def clear_cursor_filename(self, const_WindowProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_cursor_filename(const WindowProperties self)
        
        /**
         * Removes the cursor_filename specification from the properties.
         */
        """
        pass

    def clear_cursor_hidden(self, const_WindowProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_cursor_hidden(const WindowProperties self)
        
        /**
         * Removes the cursor_hidden specification from the properties.
         */
        """
        pass

    def clear_default(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_default()
        
        /**
         * Returns the "default" WindowProperties to whatever is specified in the
         * user's config file.
         */
        """
        pass

    def clear_fixed_size(self, const_WindowProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_fixed_size(const WindowProperties self)
        
        /**
         * Removes the fixed_size specification from the properties.
         */
        """
        pass

    def clear_foreground(self, const_WindowProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_foreground(const WindowProperties self)
        
        /**
         * Removes the foreground specification from the properties.
         */
        """
        pass

    def clear_fullscreen(self, const_WindowProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_fullscreen(const WindowProperties self)
        
        /**
         * Removes the fullscreen specification from the properties.
         */
        """
        pass

    def clear_icon_filename(self, const_WindowProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_icon_filename(const WindowProperties self)
        
        /**
         * Removes the icon_filename specification from the properties.
         */
        """
        pass

    def clear_minimized(self, const_WindowProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_minimized(const WindowProperties self)
        
        /**
         * Removes the minimized specification from the properties.
         */
        """
        pass

    def clear_mouse_mode(self, const_WindowProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_mouse_mode(const WindowProperties self)
        
        /**
         * Removes the mouse_mode specification from the properties.
         */
        """
        pass

    def clear_open(self, const_WindowProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_open(const WindowProperties self)
        
        /**
         * Removes the open specification from the properties.
         */
        """
        pass

    def clear_origin(self, const_WindowProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_origin(const WindowProperties self)
        
        /**
         * Removes the origin specification from the properties.
         */
        """
        pass

    def clear_parent_window(self, const_WindowProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_parent_window(const WindowProperties self)
        
        /**
         * Removes the S_parent_window specification from the properties.
         */
        """
        pass

    def clear_raw_mice(self, const_WindowProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_raw_mice(const WindowProperties self)
        
        /**
         * Removes the raw_mice specification from the properties.
         */
        """
        pass

    def clear_size(self, const_WindowProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_size(const WindowProperties self)
        
        /**
         * Removes the size specification from the properties.
         */
        """
        pass

    def clear_title(self, const_WindowProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_title(const WindowProperties self)
        
        /**
         * Removes the title specification from the properties.
         */
        """
        pass

    def clear_undecorated(self, const_WindowProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_undecorated(const WindowProperties self)
        
        /**
         * Removes the undecorated specification from the properties.
         */
        """
        pass

    def clear_z_order(self, const_WindowProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_z_order(const WindowProperties self)
        
        /**
         * Removes the z_order specification from the properties.
         */
        """
        pass

    def getConfigProperties(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_config_properties()
        
        /**
         * Returns a WindowProperties structure with all of the default values filled
         * in according to the user's config file.
         */
        """
        pass

    def getCursorFilename(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_cursor_filename(WindowProperties self)
        
        /**
         * Returns the icon filename associated with the mouse cursor.
         */
        """
        pass

    def getCursorHidden(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_cursor_hidden(WindowProperties self)
        
        /**
         * Returns true if the mouse cursor is invisible.
         */
        """
        pass

    def getDefault(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_default()
        
        /**
         * Returns the "default" WindowProperties.  If set_default() has been called,
         * this returns that WindowProperties structure; otherwise, this returns
         * get_config_properties().
         */
        """
        pass

    def getFixedSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_fixed_size(WindowProperties self)
        
        /**
         * Returns true if the window cannot be resized by the user, false otherwise.
         */
        """
        pass

    def getForeground(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_foreground(WindowProperties self)
        
        /**
         * Returns true if the window is in the foreground.
         */
        """
        pass

    def getFullscreen(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_fullscreen(WindowProperties self)
        
        /**
         * Returns true if the window is in fullscreen mode.
         */
        """
        pass

    def getIconFilename(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_icon_filename(WindowProperties self)
        
        /**
         * Returns the icon filename associated with the window.
         */
        """
        pass

    def getMinimized(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_minimized(WindowProperties self)
        
        /**
         * Returns true if the window is minimized.
         */
        """
        pass

    def getMouseMode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_mouse_mode(WindowProperties self)
        
        /**
         * See set_mouse_mode().
         */
        """
        pass

    def getOpen(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_open(WindowProperties self)
        
        /**
         * Returns true if the window is open.
         */
        """
        pass

    def getOrigin(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_origin(WindowProperties self)
        
        /**
         * Returns the coordinates of the window's top-left corner, not including
         * decorations.
         */
        """
        pass

    def getParentWindow(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_parent_window(WindowProperties self)
        
        /**
         * Returns the parent window specification, or NULL if there is no parent
         * window specified.
         */
        """
        pass

    def getRawMice(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_raw_mice(WindowProperties self)
        
        /**
         * Returns true if the window reads the raw mice.
         */
        """
        pass

    def getSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_size(WindowProperties self)
        
        /**
         * Returns size in pixels of the useful part of the window, not including
         * decorations.
         */
        """
        pass

    def getTitle(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_title(WindowProperties self)
        
        /**
         * Returns the window's title.
         */
        """
        pass

    def getUndecorated(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_undecorated(WindowProperties self)
        
        /**
         * Returns true if the window has no border.
         */
        """
        pass

    def getXOrigin(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_x_origin(WindowProperties self)
        
        /**
         * Returns the x coordinate of the window's top-left corner, not including
         * decorations.
         */
        """
        pass

    def getXSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_x_size(WindowProperties self)
        
        /**
         * Returns size in pixels in the x dimension of the useful part of the window,
         * not including decorations.  That is, this is the window's width.
         */
        """
        pass

    def getYOrigin(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_y_origin(WindowProperties self)
        
        /**
         * Returns the y coordinate of the window's top-left corner, not including
         * decorations.
         */
        """
        pass

    def getYSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_y_size(WindowProperties self)
        
        /**
         * Returns size in pixels in the y dimension of the useful part of the window,
         * not including decorations.  That is, this is the window's height.
         */
        """
        pass

    def getZOrder(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_z_order(WindowProperties self)
        
        /**
         * Returns the window's z_order.
         */
        """
        pass

    def get_config_properties(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_config_properties()
        
        /**
         * Returns a WindowProperties structure with all of the default values filled
         * in according to the user's config file.
         */
        """
        pass

    def get_cursor_filename(self, WindowProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_cursor_filename(WindowProperties self)
        
        /**
         * Returns the icon filename associated with the mouse cursor.
         */
        """
        pass

    def get_cursor_hidden(self, WindowProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_cursor_hidden(WindowProperties self)
        
        /**
         * Returns true if the mouse cursor is invisible.
         */
        """
        pass

    def get_default(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_default()
        
        /**
         * Returns the "default" WindowProperties.  If set_default() has been called,
         * this returns that WindowProperties structure; otherwise, this returns
         * get_config_properties().
         */
        """
        pass

    def get_fixed_size(self, WindowProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_fixed_size(WindowProperties self)
        
        /**
         * Returns true if the window cannot be resized by the user, false otherwise.
         */
        """
        pass

    def get_foreground(self, WindowProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_foreground(WindowProperties self)
        
        /**
         * Returns true if the window is in the foreground.
         */
        """
        pass

    def get_fullscreen(self, WindowProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_fullscreen(WindowProperties self)
        
        /**
         * Returns true if the window is in fullscreen mode.
         */
        """
        pass

    def get_icon_filename(self, WindowProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_icon_filename(WindowProperties self)
        
        /**
         * Returns the icon filename associated with the window.
         */
        """
        pass

    def get_minimized(self, WindowProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_minimized(WindowProperties self)
        
        /**
         * Returns true if the window is minimized.
         */
        """
        pass

    def get_mouse_mode(self, WindowProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_mouse_mode(WindowProperties self)
        
        /**
         * See set_mouse_mode().
         */
        """
        pass

    def get_open(self, WindowProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_open(WindowProperties self)
        
        /**
         * Returns true if the window is open.
         */
        """
        pass

    def get_origin(self, WindowProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_origin(WindowProperties self)
        
        /**
         * Returns the coordinates of the window's top-left corner, not including
         * decorations.
         */
        """
        pass

    def get_parent_window(self, WindowProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_parent_window(WindowProperties self)
        
        /**
         * Returns the parent window specification, or NULL if there is no parent
         * window specified.
         */
        """
        pass

    def get_raw_mice(self, WindowProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_raw_mice(WindowProperties self)
        
        /**
         * Returns true if the window reads the raw mice.
         */
        """
        pass

    def get_size(self, WindowProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_size(WindowProperties self)
        
        /**
         * Returns size in pixels of the useful part of the window, not including
         * decorations.
         */
        """
        pass

    def get_title(self, WindowProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_title(WindowProperties self)
        
        /**
         * Returns the window's title.
         */
        """
        pass

    def get_undecorated(self, WindowProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_undecorated(WindowProperties self)
        
        /**
         * Returns true if the window has no border.
         */
        """
        pass

    def get_x_origin(self, WindowProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_x_origin(WindowProperties self)
        
        /**
         * Returns the x coordinate of the window's top-left corner, not including
         * decorations.
         */
        """
        pass

    def get_x_size(self, WindowProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_x_size(WindowProperties self)
        
        /**
         * Returns size in pixels in the x dimension of the useful part of the window,
         * not including decorations.  That is, this is the window's width.
         */
        """
        pass

    def get_y_origin(self, WindowProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_y_origin(WindowProperties self)
        
        /**
         * Returns the y coordinate of the window's top-left corner, not including
         * decorations.
         */
        """
        pass

    def get_y_size(self, WindowProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_y_size(WindowProperties self)
        
        /**
         * Returns size in pixels in the y dimension of the useful part of the window,
         * not including decorations.  That is, this is the window's height.
         */
        """
        pass

    def get_z_order(self, WindowProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_z_order(WindowProperties self)
        
        /**
         * Returns the window's z_order.
         */
        """
        pass

    def hasCursorFilename(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_cursor_filename(WindowProperties self)
        
        /**
         * Returns true if set_cursor_filename() has been specified.
         */
        """
        pass

    def hasCursorHidden(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_cursor_hidden(WindowProperties self)
        
        /**
         * Returns true if set_cursor_hidden() has been specified.
         */
        """
        pass

    def hasFixedSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_fixed_size(WindowProperties self)
        
        /**
         * Returns true if set_fixed_size() has been specified.
         */
        """
        pass

    def hasForeground(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_foreground(WindowProperties self)
        
        /**
         * Returns true if set_foreground() has been specified.
         */
        """
        pass

    def hasFullscreen(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_fullscreen(WindowProperties self)
        
        /**
         * Returns true if set_fullscreen() has been specified.
         */
        """
        pass

    def hasIconFilename(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_icon_filename(WindowProperties self)
        
        /**
         * Returns true if set_icon_filename() has been specified.
         */
        """
        pass

    def hasMinimized(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_minimized(WindowProperties self)
        
        /**
         * Returns true if set_minimized() has been specified.
         */
        """
        pass

    def hasMouseMode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_mouse_mode(WindowProperties self)
        
        /**
         *
         */
        """
        pass

    def hasOpen(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_open(WindowProperties self)
        
        /**
         * Returns true if set_open() has been specified.
         */
        """
        pass

    def hasOrigin(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_origin(WindowProperties self)
        
        /**
         * Returns true if the window origin has been specified, false otherwise.
         */
        """
        pass

    def hasParentWindow(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_parent_window(WindowProperties self)
        
        /**
         * Checks the S_parent_window specification from the properties.
         */
        """
        pass

    def hasRawMice(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_raw_mice(WindowProperties self)
        
        /**
         * Returns true if set_raw_mice() has been specified.
         */
        """
        pass

    def hasSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_size(WindowProperties self)
        
        /**
         * Returns true if the window size has been specified, false otherwise.
         */
        """
        pass

    def hasTitle(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_title(WindowProperties self)
        
        /**
         * Returns true if the window title has been specified, false otherwise.
         */
        """
        pass

    def hasUndecorated(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_undecorated(WindowProperties self)
        
        /**
         * Returns true if set_undecorated() has been specified.
         */
        """
        pass

    def hasZOrder(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_z_order(WindowProperties self)
        
        /**
         * Returns true if the window z_order has been specified, false otherwise.
         */
        """
        pass

    def has_cursor_filename(self, WindowProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_cursor_filename(WindowProperties self)
        
        /**
         * Returns true if set_cursor_filename() has been specified.
         */
        """
        pass

    def has_cursor_hidden(self, WindowProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_cursor_hidden(WindowProperties self)
        
        /**
         * Returns true if set_cursor_hidden() has been specified.
         */
        """
        pass

    def has_fixed_size(self, WindowProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_fixed_size(WindowProperties self)
        
        /**
         * Returns true if set_fixed_size() has been specified.
         */
        """
        pass

    def has_foreground(self, WindowProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_foreground(WindowProperties self)
        
        /**
         * Returns true if set_foreground() has been specified.
         */
        """
        pass

    def has_fullscreen(self, WindowProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_fullscreen(WindowProperties self)
        
        /**
         * Returns true if set_fullscreen() has been specified.
         */
        """
        pass

    def has_icon_filename(self, WindowProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_icon_filename(WindowProperties self)
        
        /**
         * Returns true if set_icon_filename() has been specified.
         */
        """
        pass

    def has_minimized(self, WindowProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_minimized(WindowProperties self)
        
        /**
         * Returns true if set_minimized() has been specified.
         */
        """
        pass

    def has_mouse_mode(self, WindowProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_mouse_mode(WindowProperties self)
        
        /**
         *
         */
        """
        pass

    def has_open(self, WindowProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_open(WindowProperties self)
        
        /**
         * Returns true if set_open() has been specified.
         */
        """
        pass

    def has_origin(self, WindowProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_origin(WindowProperties self)
        
        /**
         * Returns true if the window origin has been specified, false otherwise.
         */
        """
        pass

    def has_parent_window(self, WindowProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_parent_window(WindowProperties self)
        
        /**
         * Checks the S_parent_window specification from the properties.
         */
        """
        pass

    def has_raw_mice(self, WindowProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_raw_mice(WindowProperties self)
        
        /**
         * Returns true if set_raw_mice() has been specified.
         */
        """
        pass

    def has_size(self, WindowProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_size(WindowProperties self)
        
        /**
         * Returns true if the window size has been specified, false otherwise.
         */
        """
        pass

    def has_title(self, WindowProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_title(WindowProperties self)
        
        /**
         * Returns true if the window title has been specified, false otherwise.
         */
        """
        pass

    def has_undecorated(self, WindowProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_undecorated(WindowProperties self)
        
        /**
         * Returns true if set_undecorated() has been specified.
         */
        """
        pass

    def has_z_order(self, WindowProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_z_order(WindowProperties self)
        
        /**
         * Returns true if the window z_order has been specified, false otherwise.
         */
        """
        pass

    def isAnySpecified(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_any_specified(WindowProperties self)
        
        /**
         * Returns true if any properties have been specified, false otherwise.
         */
        """
        pass

    def is_any_specified(self, WindowProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_any_specified(WindowProperties self)
        
        /**
         * Returns true if any properties have been specified, false otherwise.
         */
        """
        pass

    def output(self, WindowProperties_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(WindowProperties self, ostream out)
        
        /**
         * Sets any properties that are explicitly specified in other on this object.
         * Leaves other properties unchanged.
         */
        """
        pass

    def setCursorFilename(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_cursor_filename(const WindowProperties self, const Filename cursor_filename)
        
        /**
         * Specifies the file that contains the icon to associate with the mouse
         * cursor when it is within the window (and visible).
         */
        """
        pass

    def setCursorHidden(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_cursor_hidden(const WindowProperties self, bool cursor_hidden)
        
        /**
         * Specifies whether the mouse cursor should be visible.
         */
        """
        pass

    def setDefault(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_default(const WindowProperties default_properties)
        
        /**
         * Replaces the "default" WindowProperties with the specified structure.  The
         * specified WindowProperties will be returned by future calls to
         * get_default(), until clear_default() is called.
         *
         * Note that this completely replaces the default properties; it is not
         * additive.
         */
        """
        pass

    def setFixedSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_fixed_size(const WindowProperties self, bool fixed_size)
        
        /**
         * Specifies whether the window should be resizable by the user.
         */
        """
        pass

    def setForeground(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_foreground(const WindowProperties self, bool foreground)
        
        /**
         * Specifies whether the window should be opened in the foreground (true), or
         * left in the background (false).
         */
        """
        pass

    def setFullscreen(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_fullscreen(const WindowProperties self, bool fullscreen)
        
        /**
         * Specifies whether the window should be opened in fullscreen mode (true) or
         * normal windowed mode (false, the default).
         */
        """
        pass

    def setIconFilename(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_icon_filename(const WindowProperties self, const Filename icon_filename)
        
        /**
         * Specifies the file that contains the icon to associate with the window when
         * it is minimized.
         */
        """
        pass

    def setMinimized(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_minimized(const WindowProperties self, bool minimized)
        
        /**
         * Specifies whether the window should be created minimized (true), or normal
         * (false).
         */
        """
        pass

    def setMouseMode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_mouse_mode(const WindowProperties self, int mode)
        
        /**
         * Specifies the mode in which the window is to operate its mouse pointer.
         *
         * M_absolute: the normal mode in which a mouse pointer operates, where the
         * mouse can move outside the window and the mouse coordinates are relative to
         * its position in the window.
         *
         * M_relative (OSX or Unix/X11 only): a mode where only relative movements are
         * reported; particularly useful for FPS-style mouse movements where you have
         * hidden the mouse pointer and are are more interested in how fast the mouse
         * is moving, rather than precisely where the pointer is hovering.
         *
         * This has no effect on Windows.  On Unix/X11, this requires the Xxf86dga
         * extension to be available.
         *
         * M_confined: this mode reports absolute mouse positions, but confines the
         * mouse pointer to the window boundary.  It can portably replace M_relative
         * for an FPS, but you need to periodically move the pointer to the center of
         * the window and track movement deltas.
         *
         */
        """
        pass

    def setOpen(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_open(const WindowProperties self, bool open)
        
        /**
         * Specifies whether the window should be open.  It is legal to create a
         * GraphicsWindow in the closed state, and later request it to open by
         * changing this flag.
         */
        """
        pass

    def setOrigin(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_origin(const WindowProperties self, const LPoint2i origin)
        set_origin(const WindowProperties self, int x_origin, int y_origin)
        
        /**
         * Specifies the origin on the screen (in pixels, relative to the top-left
         * corner) at which the window should appear.  This is the origin of the top-
         * left corner of the useful part of the window, not including decorations.
         */
        
        /**
         * Specifies the origin on the screen (in pixels, relative to the top-left
         * corner) at which the window should appear.  This is the origin of the top-
         * left corner of the useful part of the window, not including decorations.
         */
        """
        pass

    def setParentWindow(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_parent_window(const WindowProperties self)
        set_parent_window(const WindowProperties self, WindowHandle parent_window)
        set_parent_window(const WindowProperties self, int parent)
        
        /**
         * Specifies the window that this window should be attached to.  If this is
         * NULL or unspecified, the window will be created as a toplevel window on the
         * desktop; if this is non-NULL, the window will be bound as a child window to
         * the indicated parent window.
         *
         * You should use GraphicsPipe::make_window_handle() to create an instance of
         * a WindowHandle object given an appropriate OS-specific window handle
         * representation.  Each OS-specific GraphicsPipe class defines a
         * make_window_handle() method that returns an appropriate WindowHandle object
         * to wrap the particular OS-specific representation.
         */
        
        /**
         * Specifies the window that this window should be attached to.
         *
         * This is a deprecated variant on this method, and exists only for backward
         * compatibility.  Future code should use the version of set_parent_window()
         * below that receives a WindowHandle object; that interface is much more
         * robust.
         *
         * In this deprecated variant, the actual value for "parent" is platform-
         * specific.  On Windows, it is the HWND of the parent window, cast to an
         * unsigned integer.  On X11, it is the Window pointer of the parent window,
         * similarly cast.  On OSX, this is the NSWindow pointer, which doesn't appear
         * to work at all.
         */
        """
        pass

    def setRawMice(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_raw_mice(const WindowProperties self, bool raw_mice)
        
        /**
         * Specifies whether the window should read the raw mouse devices.
         */
        """
        pass

    def setSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_size(const WindowProperties self, const LVector2i size)
        set_size(const WindowProperties self, int x_size, int y_size)
        
        /**
         * Specifies the requested size of the window, in pixels.  This is the size of
         * the useful part of the window, not including decorations.
         */
        
        /**
         * Specifies the requested size of the window, in pixels.  This is the size of
         * the useful part of the window, not including decorations.
         */
        """
        pass

    def setTitle(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_title(const WindowProperties self, str title)
        
        /**
         * Specifies the title that should be assigned to the window.
         */
        """
        pass

    def setUndecorated(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_undecorated(const WindowProperties self, bool undecorated)
        
        /**
         * Specifies whether the window should be created with a visible title and
         * border (false, the default) or not (true).
         */
        """
        pass

    def setZOrder(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_z_order(const WindowProperties self, int z_order)
        
        /**
         * Specifies the relative ordering of the window with respect to other
         * windows.  If the z_order is Z_top, the window will always be on top of
         * other windows; if it is Z_bottom, it will always be below other windows.
         * Most windows will want to be Z_normal, which allows the user to control the
         * order.
         */
        """
        pass

    def set_cursor_filename(self, const_WindowProperties_self, const_Filename_cursor_filename): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_cursor_filename(const WindowProperties self, const Filename cursor_filename)
        
        /**
         * Specifies the file that contains the icon to associate with the mouse
         * cursor when it is within the window (and visible).
         */
        """
        pass

    def set_cursor_hidden(self, const_WindowProperties_self, bool_cursor_hidden): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_cursor_hidden(const WindowProperties self, bool cursor_hidden)
        
        /**
         * Specifies whether the mouse cursor should be visible.
         */
        """
        pass

    def set_default(self, const_WindowProperties_default_properties): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_default(const WindowProperties default_properties)
        
        /**
         * Replaces the "default" WindowProperties with the specified structure.  The
         * specified WindowProperties will be returned by future calls to
         * get_default(), until clear_default() is called.
         *
         * Note that this completely replaces the default properties; it is not
         * additive.
         */
        """
        pass

    def set_fixed_size(self, const_WindowProperties_self, bool_fixed_size): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_fixed_size(const WindowProperties self, bool fixed_size)
        
        /**
         * Specifies whether the window should be resizable by the user.
         */
        """
        pass

    def set_foreground(self, const_WindowProperties_self, bool_foreground): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_foreground(const WindowProperties self, bool foreground)
        
        /**
         * Specifies whether the window should be opened in the foreground (true), or
         * left in the background (false).
         */
        """
        pass

    def set_fullscreen(self, const_WindowProperties_self, bool_fullscreen): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_fullscreen(const WindowProperties self, bool fullscreen)
        
        /**
         * Specifies whether the window should be opened in fullscreen mode (true) or
         * normal windowed mode (false, the default).
         */
        """
        pass

    def set_icon_filename(self, const_WindowProperties_self, const_Filename_icon_filename): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_icon_filename(const WindowProperties self, const Filename icon_filename)
        
        /**
         * Specifies the file that contains the icon to associate with the window when
         * it is minimized.
         */
        """
        pass

    def set_minimized(self, const_WindowProperties_self, bool_minimized): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_minimized(const WindowProperties self, bool minimized)
        
        /**
         * Specifies whether the window should be created minimized (true), or normal
         * (false).
         */
        """
        pass

    def set_mouse_mode(self, const_WindowProperties_self, int_mode): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_mouse_mode(const WindowProperties self, int mode)
        
        /**
         * Specifies the mode in which the window is to operate its mouse pointer.
         *
         * M_absolute: the normal mode in which a mouse pointer operates, where the
         * mouse can move outside the window and the mouse coordinates are relative to
         * its position in the window.
         *
         * M_relative (OSX or Unix/X11 only): a mode where only relative movements are
         * reported; particularly useful for FPS-style mouse movements where you have
         * hidden the mouse pointer and are are more interested in how fast the mouse
         * is moving, rather than precisely where the pointer is hovering.
         *
         * This has no effect on Windows.  On Unix/X11, this requires the Xxf86dga
         * extension to be available.
         *
         * M_confined: this mode reports absolute mouse positions, but confines the
         * mouse pointer to the window boundary.  It can portably replace M_relative
         * for an FPS, but you need to periodically move the pointer to the center of
         * the window and track movement deltas.
         *
         */
        """
        pass

    def set_open(self, const_WindowProperties_self, bool_open): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_open(const WindowProperties self, bool open)
        
        /**
         * Specifies whether the window should be open.  It is legal to create a
         * GraphicsWindow in the closed state, and later request it to open by
         * changing this flag.
         */
        """
        pass

    def set_origin(self, const_WindowProperties_self, const_LPoint2i_origin): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_origin(const WindowProperties self, const LPoint2i origin)
        set_origin(const WindowProperties self, int x_origin, int y_origin)
        
        /**
         * Specifies the origin on the screen (in pixels, relative to the top-left
         * corner) at which the window should appear.  This is the origin of the top-
         * left corner of the useful part of the window, not including decorations.
         */
        
        /**
         * Specifies the origin on the screen (in pixels, relative to the top-left
         * corner) at which the window should appear.  This is the origin of the top-
         * left corner of the useful part of the window, not including decorations.
         */
        """
        pass

    def set_parent_window(self, const_WindowProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_parent_window(const WindowProperties self)
        set_parent_window(const WindowProperties self, WindowHandle parent_window)
        set_parent_window(const WindowProperties self, int parent)
        
        /**
         * Specifies the window that this window should be attached to.  If this is
         * NULL or unspecified, the window will be created as a toplevel window on the
         * desktop; if this is non-NULL, the window will be bound as a child window to
         * the indicated parent window.
         *
         * You should use GraphicsPipe::make_window_handle() to create an instance of
         * a WindowHandle object given an appropriate OS-specific window handle
         * representation.  Each OS-specific GraphicsPipe class defines a
         * make_window_handle() method that returns an appropriate WindowHandle object
         * to wrap the particular OS-specific representation.
         */
        
        /**
         * Specifies the window that this window should be attached to.
         *
         * This is a deprecated variant on this method, and exists only for backward
         * compatibility.  Future code should use the version of set_parent_window()
         * below that receives a WindowHandle object; that interface is much more
         * robust.
         *
         * In this deprecated variant, the actual value for "parent" is platform-
         * specific.  On Windows, it is the HWND of the parent window, cast to an
         * unsigned integer.  On X11, it is the Window pointer of the parent window,
         * similarly cast.  On OSX, this is the NSWindow pointer, which doesn't appear
         * to work at all.
         */
        """
        pass

    def set_raw_mice(self, const_WindowProperties_self, bool_raw_mice): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_raw_mice(const WindowProperties self, bool raw_mice)
        
        /**
         * Specifies whether the window should read the raw mouse devices.
         */
        """
        pass

    def set_size(self, const_WindowProperties_self, const_LVector2i_size): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_size(const WindowProperties self, const LVector2i size)
        set_size(const WindowProperties self, int x_size, int y_size)
        
        /**
         * Specifies the requested size of the window, in pixels.  This is the size of
         * the useful part of the window, not including decorations.
         */
        
        /**
         * Specifies the requested size of the window, in pixels.  This is the size of
         * the useful part of the window, not including decorations.
         */
        """
        pass

    def set_title(self, const_WindowProperties_self, str_title): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_title(const WindowProperties self, str title)
        
        /**
         * Specifies the title that should be assigned to the window.
         */
        """
        pass

    def set_undecorated(self, const_WindowProperties_self, bool_undecorated): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_undecorated(const WindowProperties self, bool undecorated)
        
        /**
         * Specifies whether the window should be created with a visible title and
         * border (false, the default) or not (true).
         */
        """
        pass

    def set_z_order(self, const_WindowProperties_self, int_z_order): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_z_order(const WindowProperties self, int z_order)
        
        /**
         * Specifies the relative ordering of the window with respect to other
         * windows.  If the z_order is Z_top, the window will always be on top of
         * other windows; if it is Z_bottom, it will always be below other windows.
         * Most windows will want to be Z_normal, which allows the user to control the
         * order.
         */
        """
        pass

    def size(self, const_LVecBase2i_size): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        size(const LVecBase2i size)
        size(int x_size, int y_size)
        
        /**
         * Returns a WindowProperties structure with only the size specified.  The
         * size is the only property that matters to buffers.
         *
         * @deprecated in the Python API, use WindowProperties(size=(x, y)) instead.
         */
        """
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

    cursor_filename = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    cursor_hidden = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    fixed_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    foreground = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    fullscreen = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    icon_filename = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    minimized = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mouse_mode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    open = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    origin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_window = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    title = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    undecorated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    z_order = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    config_properties = None # (!) real value is 'origin=(-2, -2) size=(800, 600) title="Panda" !undecorated !fixed_size !fullscreen open !cursor_hidden absolute '
    default = None # (!) real value is 'origin=(-2, -2) size=(800, 600) title="Panda" !undecorated !fixed_size !fullscreen open !cursor_hidden absolute '
    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        'MAbsolute': 0,
        'MConfined': 2,
        'MRelative': 1,
        'M_absolute': 0,
        'M_confined': 2,
        'M_relative': 1,
        'ZBottom': 0,
        'ZNormal': 1,
        'ZTop': 2,
        'Z_bottom': 0,
        'Z_normal': 1,
        'Z_top': 2,
        '__doc__': '/**\n * A container for the various kinds of properties we might ask to have on a\n * graphics window before we open it.  This also serves to hold the current\n * properties for a window after it has been opened.\n */',
        '__eq__': None, # (!) real value is "<slot wrapper '__eq__' of 'panda3d.core.WindowProperties' objects>"
        '__ge__': None, # (!) real value is "<slot wrapper '__ge__' of 'panda3d.core.WindowProperties' objects>"
        '__gt__': None, # (!) real value is "<slot wrapper '__gt__' of 'panda3d.core.WindowProperties' objects>"
        '__hash__': None, # (!) real value is "<slot wrapper '__hash__' of 'panda3d.core.WindowProperties' objects>"
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.WindowProperties' objects>"
        '__le__': None, # (!) real value is "<slot wrapper '__le__' of 'panda3d.core.WindowProperties' objects>"
        '__lt__': None, # (!) real value is "<slot wrapper '__lt__' of 'panda3d.core.WindowProperties' objects>"
        '__ne__': None, # (!) real value is "<slot wrapper '__ne__' of 'panda3d.core.WindowProperties' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2DD360>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.WindowProperties' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.WindowProperties' objects>"
        'addProperties': None, # (!) real value is "<method 'addProperties' of 'panda3d.core.WindowProperties' objects>"
        'add_properties': None, # (!) real value is "<method 'add_properties' of 'panda3d.core.WindowProperties' objects>"
        'assign': None, # (!) real value is "<method 'assign' of 'panda3d.core.WindowProperties' objects>"
        'clear': None, # (!) real value is "<method 'clear' of 'panda3d.core.WindowProperties' objects>"
        'clearCursorFilename': None, # (!) real value is "<method 'clearCursorFilename' of 'panda3d.core.WindowProperties' objects>"
        'clearCursorHidden': None, # (!) real value is "<method 'clearCursorHidden' of 'panda3d.core.WindowProperties' objects>"
        'clearDefault': None, # (!) real value is '<staticmethod(<built-in method clearDefault of type object at 0x00007FFCFE2DD360>)>'
        'clearFixedSize': None, # (!) real value is "<method 'clearFixedSize' of 'panda3d.core.WindowProperties' objects>"
        'clearForeground': None, # (!) real value is "<method 'clearForeground' of 'panda3d.core.WindowProperties' objects>"
        'clearFullscreen': None, # (!) real value is "<method 'clearFullscreen' of 'panda3d.core.WindowProperties' objects>"
        'clearIconFilename': None, # (!) real value is "<method 'clearIconFilename' of 'panda3d.core.WindowProperties' objects>"
        'clearMinimized': None, # (!) real value is "<method 'clearMinimized' of 'panda3d.core.WindowProperties' objects>"
        'clearMouseMode': None, # (!) real value is "<method 'clearMouseMode' of 'panda3d.core.WindowProperties' objects>"
        'clearOpen': None, # (!) real value is "<method 'clearOpen' of 'panda3d.core.WindowProperties' objects>"
        'clearOrigin': None, # (!) real value is "<method 'clearOrigin' of 'panda3d.core.WindowProperties' objects>"
        'clearParentWindow': None, # (!) real value is "<method 'clearParentWindow' of 'panda3d.core.WindowProperties' objects>"
        'clearRawMice': None, # (!) real value is "<method 'clearRawMice' of 'panda3d.core.WindowProperties' objects>"
        'clearSize': None, # (!) real value is "<method 'clearSize' of 'panda3d.core.WindowProperties' objects>"
        'clearTitle': None, # (!) real value is "<method 'clearTitle' of 'panda3d.core.WindowProperties' objects>"
        'clearUndecorated': None, # (!) real value is "<method 'clearUndecorated' of 'panda3d.core.WindowProperties' objects>"
        'clearZOrder': None, # (!) real value is "<method 'clearZOrder' of 'panda3d.core.WindowProperties' objects>"
        'clear_cursor_filename': None, # (!) real value is "<method 'clear_cursor_filename' of 'panda3d.core.WindowProperties' objects>"
        'clear_cursor_hidden': None, # (!) real value is "<method 'clear_cursor_hidden' of 'panda3d.core.WindowProperties' objects>"
        'clear_default': None, # (!) real value is '<staticmethod(<built-in method clear_default of type object at 0x00007FFCFE2DD360>)>'
        'clear_fixed_size': None, # (!) real value is "<method 'clear_fixed_size' of 'panda3d.core.WindowProperties' objects>"
        'clear_foreground': None, # (!) real value is "<method 'clear_foreground' of 'panda3d.core.WindowProperties' objects>"
        'clear_fullscreen': None, # (!) real value is "<method 'clear_fullscreen' of 'panda3d.core.WindowProperties' objects>"
        'clear_icon_filename': None, # (!) real value is "<method 'clear_icon_filename' of 'panda3d.core.WindowProperties' objects>"
        'clear_minimized': None, # (!) real value is "<method 'clear_minimized' of 'panda3d.core.WindowProperties' objects>"
        'clear_mouse_mode': None, # (!) real value is "<method 'clear_mouse_mode' of 'panda3d.core.WindowProperties' objects>"
        'clear_open': None, # (!) real value is "<method 'clear_open' of 'panda3d.core.WindowProperties' objects>"
        'clear_origin': None, # (!) real value is "<method 'clear_origin' of 'panda3d.core.WindowProperties' objects>"
        'clear_parent_window': None, # (!) real value is "<method 'clear_parent_window' of 'panda3d.core.WindowProperties' objects>"
        'clear_raw_mice': None, # (!) real value is "<method 'clear_raw_mice' of 'panda3d.core.WindowProperties' objects>"
        'clear_size': None, # (!) real value is "<method 'clear_size' of 'panda3d.core.WindowProperties' objects>"
        'clear_title': None, # (!) real value is "<method 'clear_title' of 'panda3d.core.WindowProperties' objects>"
        'clear_undecorated': None, # (!) real value is "<method 'clear_undecorated' of 'panda3d.core.WindowProperties' objects>"
        'clear_z_order': None, # (!) real value is "<method 'clear_z_order' of 'panda3d.core.WindowProperties' objects>"
        'config_properties': None, # (!) real value is "<attribute 'config_properties' of 'panda3d.core.WindowProperties'>"
        'cursor_filename': None, # (!) real value is "<attribute 'cursor_filename' of 'panda3d.core.WindowProperties' objects>"
        'cursor_hidden': None, # (!) real value is "<attribute 'cursor_hidden' of 'panda3d.core.WindowProperties' objects>"
        'default': None, # (!) real value is "<attribute 'default' of 'panda3d.core.WindowProperties'>"
        'fixed_size': None, # (!) real value is "<attribute 'fixed_size' of 'panda3d.core.WindowProperties' objects>"
        'foreground': None, # (!) real value is "<attribute 'foreground' of 'panda3d.core.WindowProperties' objects>"
        'fullscreen': None, # (!) real value is "<attribute 'fullscreen' of 'panda3d.core.WindowProperties' objects>"
        'getConfigProperties': None, # (!) real value is '<staticmethod(<built-in method getConfigProperties of type object at 0x00007FFCFE2DD360>)>'
        'getCursorFilename': None, # (!) real value is "<method 'getCursorFilename' of 'panda3d.core.WindowProperties' objects>"
        'getCursorHidden': None, # (!) real value is "<method 'getCursorHidden' of 'panda3d.core.WindowProperties' objects>"
        'getDefault': None, # (!) real value is '<staticmethod(<built-in method getDefault of type object at 0x00007FFCFE2DD360>)>'
        'getFixedSize': None, # (!) real value is "<method 'getFixedSize' of 'panda3d.core.WindowProperties' objects>"
        'getForeground': None, # (!) real value is "<method 'getForeground' of 'panda3d.core.WindowProperties' objects>"
        'getFullscreen': None, # (!) real value is "<method 'getFullscreen' of 'panda3d.core.WindowProperties' objects>"
        'getIconFilename': None, # (!) real value is "<method 'getIconFilename' of 'panda3d.core.WindowProperties' objects>"
        'getMinimized': None, # (!) real value is "<method 'getMinimized' of 'panda3d.core.WindowProperties' objects>"
        'getMouseMode': None, # (!) real value is "<method 'getMouseMode' of 'panda3d.core.WindowProperties' objects>"
        'getOpen': None, # (!) real value is "<method 'getOpen' of 'panda3d.core.WindowProperties' objects>"
        'getOrigin': None, # (!) real value is "<method 'getOrigin' of 'panda3d.core.WindowProperties' objects>"
        'getParentWindow': None, # (!) real value is "<method 'getParentWindow' of 'panda3d.core.WindowProperties' objects>"
        'getRawMice': None, # (!) real value is "<method 'getRawMice' of 'panda3d.core.WindowProperties' objects>"
        'getSize': None, # (!) real value is "<method 'getSize' of 'panda3d.core.WindowProperties' objects>"
        'getTitle': None, # (!) real value is "<method 'getTitle' of 'panda3d.core.WindowProperties' objects>"
        'getUndecorated': None, # (!) real value is "<method 'getUndecorated' of 'panda3d.core.WindowProperties' objects>"
        'getXOrigin': None, # (!) real value is "<method 'getXOrigin' of 'panda3d.core.WindowProperties' objects>"
        'getXSize': None, # (!) real value is "<method 'getXSize' of 'panda3d.core.WindowProperties' objects>"
        'getYOrigin': None, # (!) real value is "<method 'getYOrigin' of 'panda3d.core.WindowProperties' objects>"
        'getYSize': None, # (!) real value is "<method 'getYSize' of 'panda3d.core.WindowProperties' objects>"
        'getZOrder': None, # (!) real value is "<method 'getZOrder' of 'panda3d.core.WindowProperties' objects>"
        'get_config_properties': None, # (!) real value is '<staticmethod(<built-in method get_config_properties of type object at 0x00007FFCFE2DD360>)>'
        'get_cursor_filename': None, # (!) real value is "<method 'get_cursor_filename' of 'panda3d.core.WindowProperties' objects>"
        'get_cursor_hidden': None, # (!) real value is "<method 'get_cursor_hidden' of 'panda3d.core.WindowProperties' objects>"
        'get_default': None, # (!) real value is '<staticmethod(<built-in method get_default of type object at 0x00007FFCFE2DD360>)>'
        'get_fixed_size': None, # (!) real value is "<method 'get_fixed_size' of 'panda3d.core.WindowProperties' objects>"
        'get_foreground': None, # (!) real value is "<method 'get_foreground' of 'panda3d.core.WindowProperties' objects>"
        'get_fullscreen': None, # (!) real value is "<method 'get_fullscreen' of 'panda3d.core.WindowProperties' objects>"
        'get_icon_filename': None, # (!) real value is "<method 'get_icon_filename' of 'panda3d.core.WindowProperties' objects>"
        'get_minimized': None, # (!) real value is "<method 'get_minimized' of 'panda3d.core.WindowProperties' objects>"
        'get_mouse_mode': None, # (!) real value is "<method 'get_mouse_mode' of 'panda3d.core.WindowProperties' objects>"
        'get_open': None, # (!) real value is "<method 'get_open' of 'panda3d.core.WindowProperties' objects>"
        'get_origin': None, # (!) real value is "<method 'get_origin' of 'panda3d.core.WindowProperties' objects>"
        'get_parent_window': None, # (!) real value is "<method 'get_parent_window' of 'panda3d.core.WindowProperties' objects>"
        'get_raw_mice': None, # (!) real value is "<method 'get_raw_mice' of 'panda3d.core.WindowProperties' objects>"
        'get_size': None, # (!) real value is "<method 'get_size' of 'panda3d.core.WindowProperties' objects>"
        'get_title': None, # (!) real value is "<method 'get_title' of 'panda3d.core.WindowProperties' objects>"
        'get_undecorated': None, # (!) real value is "<method 'get_undecorated' of 'panda3d.core.WindowProperties' objects>"
        'get_x_origin': None, # (!) real value is "<method 'get_x_origin' of 'panda3d.core.WindowProperties' objects>"
        'get_x_size': None, # (!) real value is "<method 'get_x_size' of 'panda3d.core.WindowProperties' objects>"
        'get_y_origin': None, # (!) real value is "<method 'get_y_origin' of 'panda3d.core.WindowProperties' objects>"
        'get_y_size': None, # (!) real value is "<method 'get_y_size' of 'panda3d.core.WindowProperties' objects>"
        'get_z_order': None, # (!) real value is "<method 'get_z_order' of 'panda3d.core.WindowProperties' objects>"
        'hasCursorFilename': None, # (!) real value is "<method 'hasCursorFilename' of 'panda3d.core.WindowProperties' objects>"
        'hasCursorHidden': None, # (!) real value is "<method 'hasCursorHidden' of 'panda3d.core.WindowProperties' objects>"
        'hasFixedSize': None, # (!) real value is "<method 'hasFixedSize' of 'panda3d.core.WindowProperties' objects>"
        'hasForeground': None, # (!) real value is "<method 'hasForeground' of 'panda3d.core.WindowProperties' objects>"
        'hasFullscreen': None, # (!) real value is "<method 'hasFullscreen' of 'panda3d.core.WindowProperties' objects>"
        'hasIconFilename': None, # (!) real value is "<method 'hasIconFilename' of 'panda3d.core.WindowProperties' objects>"
        'hasMinimized': None, # (!) real value is "<method 'hasMinimized' of 'panda3d.core.WindowProperties' objects>"
        'hasMouseMode': None, # (!) real value is "<method 'hasMouseMode' of 'panda3d.core.WindowProperties' objects>"
        'hasOpen': None, # (!) real value is "<method 'hasOpen' of 'panda3d.core.WindowProperties' objects>"
        'hasOrigin': None, # (!) real value is "<method 'hasOrigin' of 'panda3d.core.WindowProperties' objects>"
        'hasParentWindow': None, # (!) real value is "<method 'hasParentWindow' of 'panda3d.core.WindowProperties' objects>"
        'hasRawMice': None, # (!) real value is "<method 'hasRawMice' of 'panda3d.core.WindowProperties' objects>"
        'hasSize': None, # (!) real value is "<method 'hasSize' of 'panda3d.core.WindowProperties' objects>"
        'hasTitle': None, # (!) real value is "<method 'hasTitle' of 'panda3d.core.WindowProperties' objects>"
        'hasUndecorated': None, # (!) real value is "<method 'hasUndecorated' of 'panda3d.core.WindowProperties' objects>"
        'hasZOrder': None, # (!) real value is "<method 'hasZOrder' of 'panda3d.core.WindowProperties' objects>"
        'has_cursor_filename': None, # (!) real value is "<method 'has_cursor_filename' of 'panda3d.core.WindowProperties' objects>"
        'has_cursor_hidden': None, # (!) real value is "<method 'has_cursor_hidden' of 'panda3d.core.WindowProperties' objects>"
        'has_fixed_size': None, # (!) real value is "<method 'has_fixed_size' of 'panda3d.core.WindowProperties' objects>"
        'has_foreground': None, # (!) real value is "<method 'has_foreground' of 'panda3d.core.WindowProperties' objects>"
        'has_fullscreen': None, # (!) real value is "<method 'has_fullscreen' of 'panda3d.core.WindowProperties' objects>"
        'has_icon_filename': None, # (!) real value is "<method 'has_icon_filename' of 'panda3d.core.WindowProperties' objects>"
        'has_minimized': None, # (!) real value is "<method 'has_minimized' of 'panda3d.core.WindowProperties' objects>"
        'has_mouse_mode': None, # (!) real value is "<method 'has_mouse_mode' of 'panda3d.core.WindowProperties' objects>"
        'has_open': None, # (!) real value is "<method 'has_open' of 'panda3d.core.WindowProperties' objects>"
        'has_origin': None, # (!) real value is "<method 'has_origin' of 'panda3d.core.WindowProperties' objects>"
        'has_parent_window': None, # (!) real value is "<method 'has_parent_window' of 'panda3d.core.WindowProperties' objects>"
        'has_raw_mice': None, # (!) real value is "<method 'has_raw_mice' of 'panda3d.core.WindowProperties' objects>"
        'has_size': None, # (!) real value is "<method 'has_size' of 'panda3d.core.WindowProperties' objects>"
        'has_title': None, # (!) real value is "<method 'has_title' of 'panda3d.core.WindowProperties' objects>"
        'has_undecorated': None, # (!) real value is "<method 'has_undecorated' of 'panda3d.core.WindowProperties' objects>"
        'has_z_order': None, # (!) real value is "<method 'has_z_order' of 'panda3d.core.WindowProperties' objects>"
        'icon_filename': None, # (!) real value is "<attribute 'icon_filename' of 'panda3d.core.WindowProperties' objects>"
        'isAnySpecified': None, # (!) real value is "<method 'isAnySpecified' of 'panda3d.core.WindowProperties' objects>"
        'is_any_specified': None, # (!) real value is "<method 'is_any_specified' of 'panda3d.core.WindowProperties' objects>"
        'minimized': None, # (!) real value is "<attribute 'minimized' of 'panda3d.core.WindowProperties' objects>"
        'mouse_mode': None, # (!) real value is "<attribute 'mouse_mode' of 'panda3d.core.WindowProperties' objects>"
        'open': None, # (!) real value is "<attribute 'open' of 'panda3d.core.WindowProperties' objects>"
        'origin': None, # (!) real value is "<attribute 'origin' of 'panda3d.core.WindowProperties' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.WindowProperties' objects>"
        'parent_window': None, # (!) real value is "<attribute 'parent_window' of 'panda3d.core.WindowProperties' objects>"
        'setCursorFilename': None, # (!) real value is "<method 'setCursorFilename' of 'panda3d.core.WindowProperties' objects>"
        'setCursorHidden': None, # (!) real value is "<method 'setCursorHidden' of 'panda3d.core.WindowProperties' objects>"
        'setDefault': None, # (!) real value is '<staticmethod(<built-in method setDefault of type object at 0x00007FFCFE2DD360>)>'
        'setFixedSize': None, # (!) real value is "<method 'setFixedSize' of 'panda3d.core.WindowProperties' objects>"
        'setForeground': None, # (!) real value is "<method 'setForeground' of 'panda3d.core.WindowProperties' objects>"
        'setFullscreen': None, # (!) real value is "<method 'setFullscreen' of 'panda3d.core.WindowProperties' objects>"
        'setIconFilename': None, # (!) real value is "<method 'setIconFilename' of 'panda3d.core.WindowProperties' objects>"
        'setMinimized': None, # (!) real value is "<method 'setMinimized' of 'panda3d.core.WindowProperties' objects>"
        'setMouseMode': None, # (!) real value is "<method 'setMouseMode' of 'panda3d.core.WindowProperties' objects>"
        'setOpen': None, # (!) real value is "<method 'setOpen' of 'panda3d.core.WindowProperties' objects>"
        'setOrigin': None, # (!) real value is "<method 'setOrigin' of 'panda3d.core.WindowProperties' objects>"
        'setParentWindow': None, # (!) real value is "<method 'setParentWindow' of 'panda3d.core.WindowProperties' objects>"
        'setRawMice': None, # (!) real value is "<method 'setRawMice' of 'panda3d.core.WindowProperties' objects>"
        'setSize': None, # (!) real value is "<method 'setSize' of 'panda3d.core.WindowProperties' objects>"
        'setTitle': None, # (!) real value is "<method 'setTitle' of 'panda3d.core.WindowProperties' objects>"
        'setUndecorated': None, # (!) real value is "<method 'setUndecorated' of 'panda3d.core.WindowProperties' objects>"
        'setZOrder': None, # (!) real value is "<method 'setZOrder' of 'panda3d.core.WindowProperties' objects>"
        'set_cursor_filename': None, # (!) real value is "<method 'set_cursor_filename' of 'panda3d.core.WindowProperties' objects>"
        'set_cursor_hidden': None, # (!) real value is "<method 'set_cursor_hidden' of 'panda3d.core.WindowProperties' objects>"
        'set_default': None, # (!) real value is '<staticmethod(<built-in method set_default of type object at 0x00007FFCFE2DD360>)>'
        'set_fixed_size': None, # (!) real value is "<method 'set_fixed_size' of 'panda3d.core.WindowProperties' objects>"
        'set_foreground': None, # (!) real value is "<method 'set_foreground' of 'panda3d.core.WindowProperties' objects>"
        'set_fullscreen': None, # (!) real value is "<method 'set_fullscreen' of 'panda3d.core.WindowProperties' objects>"
        'set_icon_filename': None, # (!) real value is "<method 'set_icon_filename' of 'panda3d.core.WindowProperties' objects>"
        'set_minimized': None, # (!) real value is "<method 'set_minimized' of 'panda3d.core.WindowProperties' objects>"
        'set_mouse_mode': None, # (!) real value is "<method 'set_mouse_mode' of 'panda3d.core.WindowProperties' objects>"
        'set_open': None, # (!) real value is "<method 'set_open' of 'panda3d.core.WindowProperties' objects>"
        'set_origin': None, # (!) real value is "<method 'set_origin' of 'panda3d.core.WindowProperties' objects>"
        'set_parent_window': None, # (!) real value is "<method 'set_parent_window' of 'panda3d.core.WindowProperties' objects>"
        'set_raw_mice': None, # (!) real value is "<method 'set_raw_mice' of 'panda3d.core.WindowProperties' objects>"
        'set_size': None, # (!) real value is "<method 'set_size' of 'panda3d.core.WindowProperties' objects>"
        'set_title': None, # (!) real value is "<method 'set_title' of 'panda3d.core.WindowProperties' objects>"
        'set_undecorated': None, # (!) real value is "<method 'set_undecorated' of 'panda3d.core.WindowProperties' objects>"
        'set_z_order': None, # (!) real value is "<method 'set_z_order' of 'panda3d.core.WindowProperties' objects>"
        'size': None, # (!) real value is "<attribute 'size' of 'panda3d.core.WindowProperties'>"
        'title': None, # (!) real value is "<attribute 'title' of 'panda3d.core.WindowProperties' objects>"
        'undecorated': None, # (!) real value is "<attribute 'undecorated' of 'panda3d.core.WindowProperties' objects>"
        'z_order': None, # (!) real value is "<attribute 'z_order' of 'panda3d.core.WindowProperties' objects>"
    }
    MAbsolute = 0
    MConfined = 2
    MRelative = 1
    M_absolute = 0
    M_confined = 2
    M_relative = 1
    ZBottom = 0
    ZNormal = 1
    ZTop = 2
    Z_bottom = 0
    Z_normal = 1
    Z_top = 2


