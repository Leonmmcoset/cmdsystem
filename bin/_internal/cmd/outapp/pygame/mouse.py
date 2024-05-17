# encoding: utf-8
# module pygame.mouse
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\pygame\mouse.cp311-win_amd64.pyd
# by generator 1.147
""" pygame module to work with the mouse """
# no imports

# functions

def get_cursor(): # reliably restored by inspect
    """
    get_cursor() -> pygame.cursors.Cursor
        get the current mouse cursor
    """
    pass

def get_focused(): # real signature unknown; restored from __doc__
    """
    get_focused() -> bool
    check if the display is receiving mouse input
    """
    return False

def get_pos(): # real signature unknown; restored from __doc__
    """
    get_pos() -> (x, y)
    get the mouse cursor position
    """
    pass

def get_pressed(num_buttons=3): # real signature unknown; restored from __doc__
    """
    get_pressed(num_buttons=3) -> (button1, button2, button3)
    get_pressed(num_buttons=5) -> (button1, button2, button3, button4, button5)
    get the state of the mouse buttons
    """
    pass

def get_rel(): # real signature unknown; restored from __doc__
    """
    get_rel() -> (x, y)
    get the amount of mouse movement
    """
    pass

def get_visible(): # real signature unknown; restored from __doc__
    """
    get_visible() -> bool
    get the current visibility state of the mouse cursor
    """
    return False

def set_cursor(*args): # reliably restored by inspect
    """
    set_cursor(pygame.cursors.Cursor OR args for a pygame.cursors.Cursor) -> None
        set the mouse cursor to a new cursor
    """
    pass

def set_pos(x=None, y=None): # real signature unknown; restored from __doc__
    """
    set_pos([x, y]) -> None
    set the mouse cursor position
    """
    pass

def set_system_cursor(constant): # real signature unknown; restored from __doc__
    """
    set_system_cursor(constant) -> None
    set the mouse cursor to a system variant
    """
    pass

def set_visible(bool): # real signature unknown; restored from __doc__
    """
    set_visible(bool) -> bool
    hide or show the mouse cursor
    """
    return False

def _get_cursor(*args, **kwargs): # real signature unknown
    """ Internal API for mouse.get_cursor """
    pass

def _set_cursor(*args, **kwargs): # real signature unknown
    """ Internal API for mouse.set_cursor """
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x0000020BA70D0F90>'

__spec__ = None # (!) real value is "ModuleSpec(name='pygame.mouse', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x0000020BA70D0F90>, origin='C:\\\\Users\\\\leonm\\\\PycharmProjects\\\\leonsystem\\\\venv\\\\Lib\\\\site-packages\\\\pygame\\\\mouse.cp311-win_amd64.pyd')"

