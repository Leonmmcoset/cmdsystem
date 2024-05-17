# encoding: utf-8
# module pygame.display
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\pygame\display.cp311-win_amd64.pyd
# by generator 1.147
""" pygame module to control the display window and screen """
# no imports

# functions

def flip(): # real signature unknown; restored from __doc__
    """
    flip() -> None
    Update the full display Surface to the screen
    """
    pass

def get_active(): # real signature unknown; restored from __doc__
    """
    get_active() -> bool
    Returns True when the display is active on the screen
    """
    return False

def get_allow_screensaver(): # real signature unknown; restored from __doc__
    """
    get_allow_screensaver() -> bool
    Return whether the screensaver is allowed to run.
    """
    return False

def get_caption(): # real signature unknown; restored from __doc__
    """
    get_caption() -> (title, icontitle)
    Get the current window caption
    """
    pass

def get_desktop_sizes(): # real signature unknown; restored from __doc__
    """
    get_desktop_sizes() -> list
    Get sizes of active desktops
    """
    return []

def get_driver(): # real signature unknown; restored from __doc__
    """
    get_driver() -> name
    Get the name of the pygame display backend
    """
    pass

def get_init(): # real signature unknown; restored from __doc__
    """
    get_init() -> bool
    Returns True if the display module has been initialized
    """
    return False

def get_num_displays(): # real signature unknown; restored from __doc__
    """
    get_num_displays() -> int
    Return the number of displays
    """
    return 0

def get_surface(): # real signature unknown; restored from __doc__
    """
    get_surface() -> Surface
    Get a reference to the currently set display surface
    """
    pass

def get_window_size(): # real signature unknown; restored from __doc__
    """
    get_window_size() -> tuple
    Return the size of the window or screen
    """
    return ()

def get_wm_info(): # real signature unknown; restored from __doc__
    """
    get_wm_info() -> dict
    Get information about the current windowing system
    """
    return {}

def gl_get_attribute(flag): # real signature unknown; restored from __doc__
    """
    gl_get_attribute(flag) -> value
    Get the value for an OpenGL flag for the current display
    """
    pass

def gl_set_attribute(flag, value): # real signature unknown; restored from __doc__
    """
    gl_set_attribute(flag, value) -> None
    Request an OpenGL display attribute for the display mode
    """
    pass

def iconify(): # real signature unknown; restored from __doc__
    """
    iconify() -> bool
    Iconify the display surface
    """
    return False

def Info(): # real signature unknown; restored from __doc__
    """
    Info() -> VideoInfo
    Create a video display information object
    """
    pass

def init(): # real signature unknown; restored from __doc__
    """
    init() -> None
    Initialize the display module
    """
    pass

def is_fullscreen(*args, **kwargs): # real signature unknown
    """ provisional API, subject to change """
    pass

def list_modes(depth=0, flags=None, display=0): # real signature unknown; restored from __doc__
    """
    list_modes(depth=0, flags=pygame.FULLSCREEN, display=0) -> list
    Get list of available fullscreen modes
    """
    return []

def mode_ok(size, flags=0, depth=0, display=0): # real signature unknown; restored from __doc__
    """
    mode_ok(size, flags=0, depth=0, display=0) -> depth
    Pick the best color depth for a display mode
    """
    pass

def quit(): # real signature unknown; restored from __doc__
    """
    quit() -> None
    Uninitialize the display module
    """
    pass

def set_allow_screensaver(bool): # real signature unknown; restored from __doc__
    """
    set_allow_screensaver(bool) -> None
    Set whether the screensaver may run
    """
    pass

def set_caption(title, icontitle=None): # real signature unknown; restored from __doc__
    """
    set_caption(title, icontitle=None) -> None
    Set the current window caption
    """
    pass

def set_gamma(red, green=None, blue=None): # real signature unknown; restored from __doc__
    """
    set_gamma(red, green=None, blue=None) -> bool
    Change the hardware gamma ramps
    """
    return False

def set_gamma_ramp(red, green, blue): # real signature unknown; restored from __doc__
    """
    set_gamma_ramp(red, green, blue) -> bool
    Change the hardware gamma ramps with a custom lookup
    """
    return False

def set_icon(Surface): # real signature unknown; restored from __doc__
    """
    set_icon(Surface) -> None
    Change the system image for the display window
    """
    pass

def set_mode(size=00, flags=0, depth=0, display=0, vsync=0): # real signature unknown; restored from __doc__
    """
    set_mode(size=(0, 0), flags=0, depth=0, display=0, vsync=0) -> Surface
    Initialize a window or screen for display
    """
    pass

def set_palette(palette=None): # real signature unknown; restored from __doc__
    """
    set_palette(palette=None) -> None
    Set the display color palette for indexed displays
    """
    pass

def toggle_fullscreen(): # real signature unknown; restored from __doc__
    """
    toggle_fullscreen() -> int
    Switch between fullscreen and windowed displays
    """
    return 0

def update(rectangle=None): # real signature unknown; restored from __doc__
    """
    update(rectangle=None) -> None
    update(rectangle_list) -> None
    Update portions of the screen for software displays
    """
    pass

def _get_renderer_info(*args, **kwargs): # real signature unknown
    """ provisional API, subject to change """
    pass

def _resize_event(*args, **kwargs): # real signature unknown
    """ DEPRECATED, never officially supported, kept only for compatibility with release candidate """
    pass

def _set_autoresize(*args, **kwargs): # real signature unknown
    """ provisional API, subject to change """
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x0000016BF2C99710>'

__spec__ = None # (!) real value is "ModuleSpec(name='pygame.display', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x0000016BF2C99710>, origin='C:\\\\Users\\\\leonm\\\\PycharmProjects\\\\leonsystem\\\\venv\\\\Lib\\\\site-packages\\\\pygame\\\\display.cp311-win_amd64.pyd')"

