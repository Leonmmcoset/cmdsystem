# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .GraphicsOutput import GraphicsOutput

class GraphicsWindow(GraphicsOutput):
    """
    /**
     * A window, fullscreen or on a desktop, into which a graphics device sends
     * its output for interactive display.
     */
    """
    def clearRejectedProperties(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_rejected_properties(const GraphicsWindow self)
        
        /**
         * Empties the set of failed properties that will be returned by
         * get_rejected_properties().
         */
        """
        pass

    def clear_rejected_properties(self, const_GraphicsWindow_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_rejected_properties(const GraphicsWindow self)
        
        /**
         * Empties the set of failed properties that will be returned by
         * get_rejected_properties().
         */
        """
        pass

    def closeIme(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        close_ime(const GraphicsWindow self)
        
        /**
         * Forces the ime window to close if any
         *
         */
        """
        pass

    def close_ime(self, const_GraphicsWindow_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        close_ime(const GraphicsWindow self)
        
        /**
         * Forces the ime window to close if any
         *
         */
        """
        pass

    def disablePointerEvents(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        disable_pointer_events(const GraphicsWindow self, int device)
        
        /**
         * Turn off the generation of pointer events.
         */
        """
        pass

    def disable_pointer_events(self, const_GraphicsWindow_self, int_device): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        disable_pointer_events(const GraphicsWindow self, int device)
        
        /**
         * Turn off the generation of pointer events.
         */
        """
        pass

    def enablePointerEvents(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        enable_pointer_events(const GraphicsWindow self, int device)
        
        /**
         * Turn on the generation of pointer events.
         */
        """
        pass

    def enable_pointer_events(self, const_GraphicsWindow_self, int_device): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        enable_pointer_events(const GraphicsWindow self, int device)
        
        /**
         * Turn on the generation of pointer events.
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getCloseRequestEvent(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_close_request_event(GraphicsWindow self)
        
        /**
         * Returns the name of the event set via set_close_request_event().  If this
         * string is nonempty, then when the user requests to close window, this event
         * will be generated instead.  See set_close_request_event().
         */
        """
        pass

    def getInputDevice(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_input_device(GraphicsWindow self, int i)
        
        /**
         * Returns the nth input device associated with the window.  Typically, a
         * window will have exactly one input device: the keyboard/mouse pair.
         */
        """
        pass

    def getInputDeviceName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_input_device_name(GraphicsWindow self, int device)
        
        /**
         * Returns the name of the nth input device.
         */
        """
        pass

    def getInputDeviceNames(self, *args, **kwargs): # real signature unknown
        pass

    def getInputDevices(self, *args, **kwargs): # real signature unknown
        pass

    def getKeyboardMap(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_keyboard_map(GraphicsWindow self)
        
        /**
         * Returns a ButtonMap containing the association between raw buttons and
         * virtual buttons.
         */
        """
        pass

    def getNumInputDevices(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_input_devices(GraphicsWindow self)
        
        // Mouse and keyboard routines
        
        // Mouse and keyboard routines
        
        // Mouse and keyboard routines
        
        /**
         * Returns the number of separate input devices associated with the window.
         * Typically, a window will have exactly one input device: the keyboard/mouse
         * pair.  However, some windows may have no input devices, and others may add
         * additional devices, for instance for a joystick.
         */
        """
        pass

    def getPointer(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_pointer(GraphicsWindow self, int device)
        
        /**
         * Returns the MouseData associated with the nth input device's pointer.
         * Using this to access raw mice (with an index other than 0) is deprecated,
         * see the InputDeviceManager interface instead.
         */
        """
        pass

    def getProperties(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_properties(GraphicsWindow self)
        
        /**
         * Returns the current properties of the window.
         */
        """
        pass

    def getRejectedProperties(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_rejected_properties(GraphicsWindow self)
        
        /**
         * Returns the set of properties that have recently been requested, but could
         * not be applied to the window for some reason.  This set of properties will
         * remain unchanged until they are changed by a new failed request, or
         * clear_rejected_properties() is called.
         */
        """
        pass

    def getRequestedProperties(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_requested_properties(GraphicsWindow self)
        
        /**
         * Returns the properties of the window that are currently requested.  These
         * properties will be applied to the window (if valid) at the next execution
         * of process_events().
         */
        """
        pass

    def getUnexposedDraw(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_unexposed_draw(GraphicsWindow self)
        
        /**
         * See set_unexposed_draw().
         */
        """
        pass

    def getWindowEvent(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_window_event(GraphicsWindow self)
        
        /**
         * Returns the name of the event that is generated when this window is
         * modified externally, e.g.  to be resized or closed by the user.  See
         * set_window_event().
         */
        """
        pass

    def getWindowHandle(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_window_handle(GraphicsWindow self)
        
        /**
         * Returns the WindowHandle corresponding to this window on the desktop.  This
         * is mainly useful for communicating with external libraries.  Use
         * window_handle->get_os_handle()->get_handle(), or
         * window_handle->get_string_handle(), to get the actual OS-specific window
         * handle object, whatever type that might be.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_close_request_event(self, GraphicsWindow_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_close_request_event(GraphicsWindow self)
        
        /**
         * Returns the name of the event set via set_close_request_event().  If this
         * string is nonempty, then when the user requests to close window, this event
         * will be generated instead.  See set_close_request_event().
         */
        """
        pass

    def get_input_device(self, GraphicsWindow_self, int_i): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_input_device(GraphicsWindow self, int i)
        
        /**
         * Returns the nth input device associated with the window.  Typically, a
         * window will have exactly one input device: the keyboard/mouse pair.
         */
        """
        pass

    def get_input_devices(self, *args, **kwargs): # real signature unknown
        pass

    def get_input_device_name(self, GraphicsWindow_self, int_device): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_input_device_name(GraphicsWindow self, int device)
        
        /**
         * Returns the name of the nth input device.
         */
        """
        pass

    def get_input_device_names(self, *args, **kwargs): # real signature unknown
        pass

    def get_keyboard_map(self, GraphicsWindow_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_keyboard_map(GraphicsWindow self)
        
        /**
         * Returns a ButtonMap containing the association between raw buttons and
         * virtual buttons.
         */
        """
        pass

    def get_num_input_devices(self, GraphicsWindow_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_input_devices(GraphicsWindow self)
        
        // Mouse and keyboard routines
        
        // Mouse and keyboard routines
        
        // Mouse and keyboard routines
        
        /**
         * Returns the number of separate input devices associated with the window.
         * Typically, a window will have exactly one input device: the keyboard/mouse
         * pair.  However, some windows may have no input devices, and others may add
         * additional devices, for instance for a joystick.
         */
        """
        pass

    def get_pointer(self, GraphicsWindow_self, int_device): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_pointer(GraphicsWindow self, int device)
        
        /**
         * Returns the MouseData associated with the nth input device's pointer.
         * Using this to access raw mice (with an index other than 0) is deprecated,
         * see the InputDeviceManager interface instead.
         */
        """
        pass

    def get_properties(self, GraphicsWindow_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_properties(GraphicsWindow self)
        
        /**
         * Returns the current properties of the window.
         */
        """
        pass

    def get_rejected_properties(self, GraphicsWindow_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_rejected_properties(GraphicsWindow self)
        
        /**
         * Returns the set of properties that have recently been requested, but could
         * not be applied to the window for some reason.  This set of properties will
         * remain unchanged until they are changed by a new failed request, or
         * clear_rejected_properties() is called.
         */
        """
        pass

    def get_requested_properties(self, GraphicsWindow_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_requested_properties(GraphicsWindow self)
        
        /**
         * Returns the properties of the window that are currently requested.  These
         * properties will be applied to the window (if valid) at the next execution
         * of process_events().
         */
        """
        pass

    def get_unexposed_draw(self, GraphicsWindow_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_unexposed_draw(GraphicsWindow self)
        
        /**
         * See set_unexposed_draw().
         */
        """
        pass

    def get_window_event(self, GraphicsWindow_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_window_event(GraphicsWindow self)
        
        /**
         * Returns the name of the event that is generated when this window is
         * modified externally, e.g.  to be resized or closed by the user.  See
         * set_window_event().
         */
        """
        pass

    def get_window_handle(self, GraphicsWindow_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_window_handle(GraphicsWindow self)
        
        /**
         * Returns the WindowHandle corresponding to this window on the desktop.  This
         * is mainly useful for communicating with external libraries.  Use
         * window_handle->get_os_handle()->get_handle(), or
         * window_handle->get_string_handle(), to get the actual OS-specific window
         * handle object, whatever type that might be.
         */
        """
        pass

    def hasKeyboard(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_keyboard(GraphicsWindow self, int device)
        
        /**
         * Returns true if the nth input device has a keyboard, false otherwise.
         */
        """
        pass

    def hasPointer(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_pointer(GraphicsWindow self, int device)
        
        /**
         * Returns true if the nth input device has a screen-space pointer (for
         * instance, a mouse), false otherwise.
         */
        """
        pass

    def has_keyboard(self, GraphicsWindow_self, int_device): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_keyboard(GraphicsWindow self, int device)
        
        /**
         * Returns true if the nth input device has a keyboard, false otherwise.
         */
        """
        pass

    def has_pointer(self, GraphicsWindow_self, int_device): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_pointer(GraphicsWindow self, int device)
        
        /**
         * Returns true if the nth input device has a screen-space pointer (for
         * instance, a mouse), false otherwise.
         */
        """
        pass

    def isClosed(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_closed(GraphicsWindow self)
        
        /**
         * Returns true if the window has not yet been opened, or has been fully
         * closed, false if it is open.  The window is not opened immediately after
         * GraphicsEngine::make_output() is called; nor is it closed immediately after
         * GraphicsEngine::remove_window() is called.  Either operation may take a
         * frame or two.
         */
        """
        pass

    def isFullscreen(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_fullscreen(GraphicsWindow self)
        
        /**
         * Returns true if the window has been opened as a fullscreen window, false
         * otherwise.
         */
        """
        pass

    def is_closed(self, GraphicsWindow_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_closed(GraphicsWindow self)
        
        /**
         * Returns true if the window has not yet been opened, or has been fully
         * closed, false if it is open.  The window is not opened immediately after
         * GraphicsEngine::make_output() is called; nor is it closed immediately after
         * GraphicsEngine::remove_window() is called.  Either operation may take a
         * frame or two.
         */
        """
        pass

    def is_fullscreen(self, GraphicsWindow_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_fullscreen(GraphicsWindow self)
        
        /**
         * Returns true if the window has been opened as a fullscreen window, false
         * otherwise.
         */
        """
        pass

    def movePointer(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        move_pointer(const GraphicsWindow self, int device, int x, int y)
        
        /**
         * Forces the pointer to the indicated position within the window, if
         * possible.
         *
         * Returns true if successful, false on failure.  This may fail if the mouse
         * is not currently within the window, or if the API doesn't support this
         * operation.
         */
        """
        pass

    def move_pointer(self, const_GraphicsWindow_self, int_device, int_x, int_y): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        move_pointer(const GraphicsWindow self, int device, int x, int y)
        
        /**
         * Forces the pointer to the indicated position within the window, if
         * possible.
         *
         * Returns true if successful, false on failure.  This may fail if the mouse
         * is not currently within the window, or if the API doesn't support this
         * operation.
         */
        """
        pass

    def requestProperties(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        request_properties(const GraphicsWindow self, const WindowProperties requested_properties)
        
        /**
         * Requests a property change on the window.  For example, use this method to
         * request a window change size or minimize or something.
         *
         * The change is not made immediately; rather, the request is saved and will
         * be applied the next time the window task is run (probably at the next
         * frame).
         */
        """
        pass

    def request_properties(self, const_GraphicsWindow_self, const_WindowProperties_requested_properties): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        request_properties(const GraphicsWindow self, const WindowProperties requested_properties)
        
        /**
         * Requests a property change on the window.  For example, use this method to
         * request a window change size or minimize or something.
         *
         * The change is not made immediately; rather, the request is saved and will
         * be applied the next time the window task is run (probably at the next
         * frame).
         */
        """
        pass

    def setCloseRequestEvent(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_close_request_event(const GraphicsWindow self, str close_request_event)
        
        /**
         * Sets the event that is triggered when the user requests to close the
         * window, e.g.  via alt-F4, or clicking on the close box.
         *
         * The default for each window is for this event to be the empty string, which
         * means the window-close request is handled immediately by Panda (and the
         * window will be closed without the app getting a chance to intervene).  If
         * you set this to a nonempty string, then the window is not closed, but
         * instead the event is thrown.  It is then up to the app to respond
         * appropriately, for instance by presenting an "are you sure?"  dialog box,
         * and eventually calling close_window() when the user is sure.
         *
         * It is considered poor form to set this string and then not handle the
         * event.  This can frustrate the user by making it difficult for him to
         * cleanly shut down the application (and may force the user to hard-kill the
         * app, or reboot the machine).
         */
        """
        pass

    def setUnexposedDraw(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_unexposed_draw(const GraphicsWindow self, bool unexposed_draw)
        
        /**
         * If this flag is false, the window is redrawn only after it has received a
         * recent "unexpose" or "draw" event from the underlying windowing system.  If
         * this flag is true, the window is redrawn every frame regardless.  Setting
         * this false may prevent the window from redrawing unnecessarily when it is
         * hidden, and may play nicer with other windows on the desktop, but may
         * adversely affect frame rate even when the window is fully visible; setting
         * it true will ensure that the window contents are always current.
         */
        """
        pass

    def setWindowEvent(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_window_event(const GraphicsWindow self, str window_event)
        
        /**
         * Changes the name of the event that is generated when this window is
         * modified externally, e.g.  to be resized or closed by the user.
         *
         * By default, all windows have the same window event unless they are
         * explicitly changed.  When the event is generated, it includes one
         * parameter: the window itself.
         */
        """
        pass

    def set_close_request_event(self, const_GraphicsWindow_self, str_close_request_event): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_close_request_event(const GraphicsWindow self, str close_request_event)
        
        /**
         * Sets the event that is triggered when the user requests to close the
         * window, e.g.  via alt-F4, or clicking on the close box.
         *
         * The default for each window is for this event to be the empty string, which
         * means the window-close request is handled immediately by Panda (and the
         * window will be closed without the app getting a chance to intervene).  If
         * you set this to a nonempty string, then the window is not closed, but
         * instead the event is thrown.  It is then up to the app to respond
         * appropriately, for instance by presenting an "are you sure?"  dialog box,
         * and eventually calling close_window() when the user is sure.
         *
         * It is considered poor form to set this string and then not handle the
         * event.  This can frustrate the user by making it difficult for him to
         * cleanly shut down the application (and may force the user to hard-kill the
         * app, or reboot the machine).
         */
        """
        pass

    def set_unexposed_draw(self, const_GraphicsWindow_self, bool_unexposed_draw): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_unexposed_draw(const GraphicsWindow self, bool unexposed_draw)
        
        /**
         * If this flag is false, the window is redrawn only after it has received a
         * recent "unexpose" or "draw" event from the underlying windowing system.  If
         * this flag is true, the window is redrawn every frame regardless.  Setting
         * this false may prevent the window from redrawing unnecessarily when it is
         * hidden, and may play nicer with other windows on the desktop, but may
         * adversely affect frame rate even when the window is fully visible; setting
         * it true will ensure that the window contents are always current.
         */
        """
        pass

    def set_window_event(self, const_GraphicsWindow_self, str_window_event): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_window_event(const GraphicsWindow self, str window_event)
        
        /**
         * Changes the name of the event that is generated when this window is
         * modified externally, e.g.  to be resized or closed by the user.
         *
         * By default, all windows have the same window event unless they are
         * explicitly changed.  When the event is generated, it includes one
         * parameter: the window itself.
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    closed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    close_request_event = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    properties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    rejected_properties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    requested_properties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    unexposed_draw = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    window_event = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    window_handle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * A window, fullscreen or on a desktop, into which a graphics device sends\n * its output for interactive display.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.GraphicsWindow' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2DE750>'
        'clearRejectedProperties': None, # (!) real value is "<method 'clearRejectedProperties' of 'panda3d.core.GraphicsWindow' objects>"
        'clear_rejected_properties': None, # (!) real value is "<method 'clear_rejected_properties' of 'panda3d.core.GraphicsWindow' objects>"
        'closeIme': None, # (!) real value is "<method 'closeIme' of 'panda3d.core.GraphicsWindow' objects>"
        'close_ime': None, # (!) real value is "<method 'close_ime' of 'panda3d.core.GraphicsWindow' objects>"
        'close_request_event': None, # (!) real value is "<attribute 'close_request_event' of 'panda3d.core.GraphicsWindow' objects>"
        'closed': None, # (!) real value is "<attribute 'closed' of 'panda3d.core.GraphicsWindow' objects>"
        'disablePointerEvents': None, # (!) real value is "<method 'disablePointerEvents' of 'panda3d.core.GraphicsWindow' objects>"
        'disable_pointer_events': None, # (!) real value is "<method 'disable_pointer_events' of 'panda3d.core.GraphicsWindow' objects>"
        'enablePointerEvents': None, # (!) real value is "<method 'enablePointerEvents' of 'panda3d.core.GraphicsWindow' objects>"
        'enable_pointer_events': None, # (!) real value is "<method 'enable_pointer_events' of 'panda3d.core.GraphicsWindow' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2DE750>)>'
        'getCloseRequestEvent': None, # (!) real value is "<method 'getCloseRequestEvent' of 'panda3d.core.GraphicsWindow' objects>"
        'getInputDevice': None, # (!) real value is "<method 'getInputDevice' of 'panda3d.core.GraphicsWindow' objects>"
        'getInputDeviceName': None, # (!) real value is "<method 'getInputDeviceName' of 'panda3d.core.GraphicsWindow' objects>"
        'getInputDeviceNames': None, # (!) real value is "<method 'getInputDeviceNames' of 'panda3d.core.GraphicsWindow' objects>"
        'getInputDevices': None, # (!) real value is "<method 'getInputDevices' of 'panda3d.core.GraphicsWindow' objects>"
        'getKeyboardMap': None, # (!) real value is "<method 'getKeyboardMap' of 'panda3d.core.GraphicsWindow' objects>"
        'getNumInputDevices': None, # (!) real value is "<method 'getNumInputDevices' of 'panda3d.core.GraphicsWindow' objects>"
        'getPointer': None, # (!) real value is "<method 'getPointer' of 'panda3d.core.GraphicsWindow' objects>"
        'getProperties': None, # (!) real value is "<method 'getProperties' of 'panda3d.core.GraphicsWindow' objects>"
        'getRejectedProperties': None, # (!) real value is "<method 'getRejectedProperties' of 'panda3d.core.GraphicsWindow' objects>"
        'getRequestedProperties': None, # (!) real value is "<method 'getRequestedProperties' of 'panda3d.core.GraphicsWindow' objects>"
        'getUnexposedDraw': None, # (!) real value is "<method 'getUnexposedDraw' of 'panda3d.core.GraphicsWindow' objects>"
        'getWindowEvent': None, # (!) real value is "<method 'getWindowEvent' of 'panda3d.core.GraphicsWindow' objects>"
        'getWindowHandle': None, # (!) real value is "<method 'getWindowHandle' of 'panda3d.core.GraphicsWindow' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2DE750>)>'
        'get_close_request_event': None, # (!) real value is "<method 'get_close_request_event' of 'panda3d.core.GraphicsWindow' objects>"
        'get_input_device': None, # (!) real value is "<method 'get_input_device' of 'panda3d.core.GraphicsWindow' objects>"
        'get_input_device_name': None, # (!) real value is "<method 'get_input_device_name' of 'panda3d.core.GraphicsWindow' objects>"
        'get_input_device_names': None, # (!) real value is "<method 'get_input_device_names' of 'panda3d.core.GraphicsWindow' objects>"
        'get_input_devices': None, # (!) real value is "<method 'get_input_devices' of 'panda3d.core.GraphicsWindow' objects>"
        'get_keyboard_map': None, # (!) real value is "<method 'get_keyboard_map' of 'panda3d.core.GraphicsWindow' objects>"
        'get_num_input_devices': None, # (!) real value is "<method 'get_num_input_devices' of 'panda3d.core.GraphicsWindow' objects>"
        'get_pointer': None, # (!) real value is "<method 'get_pointer' of 'panda3d.core.GraphicsWindow' objects>"
        'get_properties': None, # (!) real value is "<method 'get_properties' of 'panda3d.core.GraphicsWindow' objects>"
        'get_rejected_properties': None, # (!) real value is "<method 'get_rejected_properties' of 'panda3d.core.GraphicsWindow' objects>"
        'get_requested_properties': None, # (!) real value is "<method 'get_requested_properties' of 'panda3d.core.GraphicsWindow' objects>"
        'get_unexposed_draw': None, # (!) real value is "<method 'get_unexposed_draw' of 'panda3d.core.GraphicsWindow' objects>"
        'get_window_event': None, # (!) real value is "<method 'get_window_event' of 'panda3d.core.GraphicsWindow' objects>"
        'get_window_handle': None, # (!) real value is "<method 'get_window_handle' of 'panda3d.core.GraphicsWindow' objects>"
        'hasKeyboard': None, # (!) real value is "<method 'hasKeyboard' of 'panda3d.core.GraphicsWindow' objects>"
        'hasPointer': None, # (!) real value is "<method 'hasPointer' of 'panda3d.core.GraphicsWindow' objects>"
        'has_keyboard': None, # (!) real value is "<method 'has_keyboard' of 'panda3d.core.GraphicsWindow' objects>"
        'has_pointer': None, # (!) real value is "<method 'has_pointer' of 'panda3d.core.GraphicsWindow' objects>"
        'isClosed': None, # (!) real value is "<method 'isClosed' of 'panda3d.core.GraphicsWindow' objects>"
        'isFullscreen': None, # (!) real value is "<method 'isFullscreen' of 'panda3d.core.GraphicsWindow' objects>"
        'is_closed': None, # (!) real value is "<method 'is_closed' of 'panda3d.core.GraphicsWindow' objects>"
        'is_fullscreen': None, # (!) real value is "<method 'is_fullscreen' of 'panda3d.core.GraphicsWindow' objects>"
        'movePointer': None, # (!) real value is "<method 'movePointer' of 'panda3d.core.GraphicsWindow' objects>"
        'move_pointer': None, # (!) real value is "<method 'move_pointer' of 'panda3d.core.GraphicsWindow' objects>"
        'properties': None, # (!) real value is "<attribute 'properties' of 'panda3d.core.GraphicsWindow' objects>"
        'rejected_properties': None, # (!) real value is "<attribute 'rejected_properties' of 'panda3d.core.GraphicsWindow' objects>"
        'requestProperties': None, # (!) real value is "<method 'requestProperties' of 'panda3d.core.GraphicsWindow' objects>"
        'request_properties': None, # (!) real value is "<method 'request_properties' of 'panda3d.core.GraphicsWindow' objects>"
        'requested_properties': None, # (!) real value is "<attribute 'requested_properties' of 'panda3d.core.GraphicsWindow' objects>"
        'setCloseRequestEvent': None, # (!) real value is "<method 'setCloseRequestEvent' of 'panda3d.core.GraphicsWindow' objects>"
        'setUnexposedDraw': None, # (!) real value is "<method 'setUnexposedDraw' of 'panda3d.core.GraphicsWindow' objects>"
        'setWindowEvent': None, # (!) real value is "<method 'setWindowEvent' of 'panda3d.core.GraphicsWindow' objects>"
        'set_close_request_event': None, # (!) real value is "<method 'set_close_request_event' of 'panda3d.core.GraphicsWindow' objects>"
        'set_unexposed_draw': None, # (!) real value is "<method 'set_unexposed_draw' of 'panda3d.core.GraphicsWindow' objects>"
        'set_window_event': None, # (!) real value is "<method 'set_window_event' of 'panda3d.core.GraphicsWindow' objects>"
        'unexposed_draw': None, # (!) real value is "<attribute 'unexposed_draw' of 'panda3d.core.GraphicsWindow' objects>"
        'window_event': None, # (!) real value is "<attribute 'window_event' of 'panda3d.core.GraphicsWindow' objects>"
        'window_handle': None, # (!) real value is "<attribute 'window_handle' of 'panda3d.core.GraphicsWindow' objects>"
    }


