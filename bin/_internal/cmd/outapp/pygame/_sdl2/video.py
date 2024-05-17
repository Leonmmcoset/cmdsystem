# encoding: utf-8
# module pygame._sdl2.video
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\pygame\_sdl2\video.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import os as os # C:\Users\leonm\AppData\Local\Programs\Python\Python311\Lib\os.py
from pygame._sdl2.sdl2 import error, errorfnc


# Variables with simple values

MESSAGEBOX_ERROR = 16
MESSAGEBOX_INFORMATION = 64
MESSAGEBOX_WARNING = 32

WINDOWPOS_CENTERED = 805240832
WINDOWPOS_UNDEFINED = 536805376

# functions

def get_drivers(*args, **kwargs): # real signature unknown
    pass

def get_grabbed_window(*args, **kwargs): # real signature unknown
    """
    return the Window with input grab enabled,
           or None if input isn't grabbed.
    """
    pass

def messagebox(*args, **kwargs): # real signature unknown
    """
    Display a message box.
    
        :param str title: A title string or None.
        :param str message: A message string.
        :param bool info: If ``True``, display an info message.
        :param bool warn: If ``True``, display a warning message.
        :param bool error: If ``True``, display an error message.
        :param tuple buttons: An optional sequence of buttons to show to the user (strings).
        :param int return_button: Button index to use if the return key is hit (-1 for none).
        :param int escape_button: Button index to use if the escape key is hit (-1 for none).
        :return: The index of the button that was pushed.
    """
    pass

def __reduce_cython__(*args, **kwargs): # real signature unknown
    pass

def __setstate_cython__(*args, **kwargs): # real signature unknown
    pass

# classes

class Image(object):
    # no doc
    def draw(self, *args, **kwargs): # real signature unknown
        """
        Copy a portion of the image to the rendering target.
        
                :param srcrect: source rectangle specifying a sub-image, or None for the entire image.
                :param dstrect: destination rectangle or position on the render target, or None for entire target.
                                The image is stretched to fill dstrect.
        """
        pass

    def get_rect(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    alpha = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    angle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    blend_mode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    color = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    flip_x = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    flip_y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    origin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    srcrect = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    texture = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001E3C3A7BAB0>'


class Renderer(object):
    # no doc
    def blit(self, *args, **kwargs): # real signature unknown
        """
        Only for compatibility.
                Textures created by different Renderers cannot shared with each other!
                :param source: A Texture or Image to draw.
                :param dest: destination on the render target.
                :param area: the portion of source texture.
                :param special_flags: have no effect at this moment.
        """
        pass

    def clear(self, *args, **kwargs): # real signature unknown
        """ Clear the current rendering target with the drawing color. """
        pass

    def compose_custom_blend_mode(self, *args, **kwargs): # real signature unknown
        """
        Use this function to compose a custom blend mode.. 
        
                :param color_mode: A tuple (srcColorFactor, dstColorFactor, colorOperation)
                :param alpha_mode: A tuple (srcAlphaFactor, dstAlphaFactor, alphaOperation)
                :return: A blend mode to be used with Renderer.draw_blend_mode and Texure.blend_mode
        """
        pass

    def draw_line(self, *args, **kwargs): # real signature unknown
        pass

    def draw_point(self, *args, **kwargs): # real signature unknown
        pass

    def draw_rect(self, *args, **kwargs): # real signature unknown
        pass

    def fill_rect(self, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def from_window(cls, *args, **kwargs): # real signature unknown
        pass

    def get_viewport(self, *args, **kwargs): # real signature unknown
        """
        Returns the drawing area on the target.
        
                :rtype: pygame.Rect
        """
        pass

    def present(self, *args, **kwargs): # real signature unknown
        """
        Present the composed backbuffer to the screen.
        
                Updates the screen with any rendering performed since previous call.
        """
        pass

    def set_viewport(self, *args, **kwargs): # real signature unknown
        """
        Set the drawing area on the target.
                If this is set to ``None``, the entire target will be used.
        
                :param area: A ``pygame.Rect`` or tuple representing the
                             drawing area on the target, or None.
        """
        pass

    def to_surface(self, *args, **kwargs): # real signature unknown
        """
        Read pixels from the current rendering target and create a pygame.Surface.
                    WARNING: This is a very slow operation, and should not be used frequently.
        
                :param surface: A surface to read the pixel data into.
                                It must be large enough to fit the area, or ``ValueError`` is
                                raised.
                                If ``None``, a new surface is returned.
                :param area: The area of the screen to read pixels from. The area is
                             clipped to fit inside the viewport.
                             If ``None``, the entire viewport is used.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        """
        Create a 2D rendering context for a window.
        
                :param Window window: where rendering is displayed.
                :param int index: index of rendering driver to initialize,
                                  or -1 to init the first supporting requested options.
                :param int accelerated: if 1, the renderer uses hardware acceleration.
                                        if 0, the renderer is a software fallback.
                                        -1 gives precedence to renderers using hardware acceleration.
                :param bool vsync: .present() is synchronized with the refresh rate.
                :param bool target_texture: the renderer supports rendering to texture.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    draw_blend_mode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    draw_color = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """ Color used by the drawing functions.
        """

    logical_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    scale = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    target = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """ The current render target. Set to ``None`` for the default target.

        :rtype: Texture, None
        """


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001E3C3A7BA50>'


class RendererDriverInfo(object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'pygame._sdl2.video', '__repr__': <cyfunction RendererDriverInfo.__repr__ at 0x000001E3C3AB9CB0>, '__dict__': <attribute '__dict__' of 'RendererDriverInfo' objects>, '__weakref__': <attribute '__weakref__' of 'RendererDriverInfo' objects>, '__doc__': None})"


class Texture(object):
    # no doc
    def draw(self, *args, **kwargs): # real signature unknown
        """
        Copy a portion of the texture to the rendering target.
        
                :param srcrect: source rectangle on the texture, or None for the entire texture.
                :param dstrect: destination rectangle or position on the render target, or None for entire target.
                                The texture is stretched to fill dstrect.
                :param float angle: angle (in degrees) to rotate dstrect around (clockwise).
                :param origin: point around which dstrect will be rotated.
                               If None, it will equal the center: (dstrect.w/2, dstrect.h/2).
                :param bool flip_x: flip horizontally.
                :param bool flip_y: flip vertically.
        """
        pass

    def from_surface(self, *args, **kwargs): # real signature unknown
        """
        Create a texture from an existing surface.
        
                :param Renderer renderer: Rendering context for the texture.
                :param pygame.Surface surface: The surface to create a texture from.
        """
        pass

    def get_rect(self): # real signature unknown; restored from __doc__
        """
        Get the rectangular area of the texture.
                like surface.get_rect(), returns a new rectangle covering the entire surface.
                This rectangle will always start at 0, 0 with a width. and height the same size as the texture.
        """
        pass

    def update(self, *args, **kwargs): # real signature unknown
        """
        Update the texture with Surface.
                This is a fairly slow function, intended for use with static textures that do not change often.
        
                If the texture is intended to be updated often,
                it is preferred to create the texture as streaming and use the locking functions.
        
                While this function will work with streaming textures,
                for optimization reasons you may not get the pixels back if you lock the texture afterward.
        
                :param surface: source Surface.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        """
        Create an empty texture.
        
                :param Renderer renderer: Rendering context for the texture.
                :param tuple size: The width and height of the texture.
                :param int depth: The pixel format (0 to use the default).
        
                One of ``static``, ``streaming``, or ``target`` can be set
                to ``True``. If all are ``False``, then ``static`` is used.
        
                :param bool static: Changes rarely, not lockable.
                :param bool streaming: Changes frequently, lockable.
                :param bool target: Can be used as a render target.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    alpha = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    blend_mode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    color = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    renderer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001E3C3A7BA80>'


class Window(object):
    # no doc
    def destroy(self, *args, **kwargs): # real signature unknown
        """ Destroys the window. """
        pass

    def focus(self, *args, **kwargs): # real signature unknown
        """
        Raise the window above other windows and set the input focus.
        
                :param bool input_only: if ``True``, the window will be given input focus
                                        but may be completely obscured by other windows.
        """
        pass

    @classmethod
    def from_display_module(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def from_window(cls, *args, **kwargs): # real signature unknown
        pass

    def hide(self, *args, **kwargs): # real signature unknown
        """ Hide the window. """
        pass

    def maximize(self, *args, **kwargs): # real signature unknown
        """ Maximize the window. """
        pass

    def minimize(self, *args, **kwargs): # real signature unknown
        """ Minimize the window. """
        pass

    def restore(self, *args, **kwargs): # real signature unknown
        """ Restore the size and position of a minimized or maximized window. """
        pass

    def set_fullscreen(self, *args, **kwargs): # real signature unknown
        """
        Enable fullscreen for the window
        
                :param bool desktop: If ``True``: use the current desktop resolution.
                                     If ``False``: change the fullscreen resolution to the window size.
        
                .. seealso:: :func:`set_windowed`
        """
        pass

    def set_icon(self, *args, **kwargs): # real signature unknown
        """
        Set the icon for the window.
        
                :param pygame.Surface surface: A Surface to use as the icon.
        """
        pass

    def set_modal_for(self, *args, **kwargs): # real signature unknown
        """
        set the window as a modal for a parent window
                This function is only supported on X11.
        """
        pass

    def set_windowed(self, *args, **kwargs): # real signature unknown
        """
        Enable windowed mode
        
                .. seealso:: :func:`set_fullscreen`
        """
        pass

    def show(self, *args, **kwargs): # real signature unknown
        """ Show the window. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        """
        Create a window with the specified position, dimensions, and flags.
        
                :param str title: the title of the window, in UTF-8 encoding
                :param tuple size: the size of the window, in screen coordinates (width, height)
                :param position: a tuple specifying the window position, WINDOWPOS_CENTERED, or WINDOWPOS_UNDEFINED.
                :param bool fullscreen: fullscreen window using the window size as the resolution (videomode change)
                :param bool fullscreen_desktop: fullscreen window using the current desktop resolution
                :param bool opengl: Usable with OpenGL context. You will still need to create an OpenGL context.
                :param bool vulkan: usable with a Vulkan instance
                :param bool hidden: window is not visible
                :param bool borderless: no window decoration
                :param bool resizable: window can be resized
                :param bool minimized: window is minimized
                :param bool maximized: window is maximized
                :param bool input_grabbed: window has grabbed input focus
                :param bool input_focus: window has input focus
                :param bool mouse_focus: window has mouse focus
                :param bool foreign: window not created by SDL
                :param bool allow_highdpi: window should be created in high-DPI mode if supported (>= SDL 2.0.1)
                :param bool mouse_capture: window has mouse captured (unrelated to INPUT_GRABBED, >= SDL 2.0.4)
                :param bool always_on_top: window should always be above others (X11 only, >= SDL 2.0.5)
                :param bool skip_taskbar: window should not be added to the taskbar (X11 only, >= SDL 2.0.5)
                :param bool utility: window should be treated as a utility window (X11 only, >= SDL 2.0.5)
                :param bool tooltip: window should be treated as a tooltip (X11 only, >= SDL 2.0.5)
                :param bool popup_menu: window should be treated as a popup menu (X11 only, >= SDL 2.0.5)
        """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    borderless = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """ Add or remove the border from the actual window.

        .. note:: You can't change the border state of a fullscreen window.
        """

    display_index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """ The index of the display associated with the window. *Read-only*.

        :rtype: int
        """

    grab = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """ Window's input grab state (``True`` or ``False``).

        Set it to ``True`` to grab, ``False`` to release.

        When input is grabbed the mouse is confined to the window.
        If the caller enables a grab while another window is currently grabbed,
        the other window loses its grab in favor of the caller's window.

        :rtype: bool
        """

    id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """ A unique window ID. *Read-only*.

        :rtype: int
        """

    opacity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """ Window opacity. It ranges between 0.0 (fully transparent)
        and 1.0 (fully opaque)."""

    position = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """ Window's screen coordinates, or WINDOWPOS_CENTERED or WINDOWPOS_UNDEFINED"""

    relative_mouse = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """ Window's relative mouse motion state (``True`` or ``False``).

        Set it to ``True`` to enable, ``False`` to disable.
        If mouse.set_visible(True) is set the input will be grabbed,
        and the mouse will enter endless relative motion mode.

        :rtype: bool
        """

    resizable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """ Sets whether the window is resizable.
        """

    size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """ The size of the window's client area."""

    title = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """ The title of the window or u"" if there is none.
        """


    DEFAULT_SIZE = (
        640,
        480,
    )
    _kwarg_to_flag = {
        'allow_highdpi': 0,
        'always_on_top': 0,
        'borderless': 16,
        'foreign': 0,
        'hidden': 8,
        'input_focus': 0,
        'input_grabbed': 0,
        'maximized': 128,
        'minimized': 64,
        'mouse_capture': 0,
        'mouse_focus': 0,
        'opengl': 2,
        'popup_menu': 0,
        'resizable': 32,
        'skip_taskbar': 0,
        'tooltip': 0,
        'utility': 0,
        'vulkan': 0,
    }


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001E3C398C850>'

__spec__ = None # (!) real value is "ModuleSpec(name='pygame._sdl2.video', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001E3C398C850>, origin='C:\\\\Users\\\\leonm\\\\PycharmProjects\\\\leonsystem\\\\venv\\\\Lib\\\\site-packages\\\\pygame\\\\_sdl2\\\\video.cp311-win_amd64.pyd')"

__test__ = {}

