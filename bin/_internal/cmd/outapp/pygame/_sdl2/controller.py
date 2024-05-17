# encoding: utf-8
# module pygame._sdl2.controller
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\pygame\_sdl2\controller.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
from pygame._sdl2.sdl2 import error


# functions

def get_count(*args, **kwargs): # real signature unknown
    """ Returns the number of attached joysticks. """
    pass

def get_eventstate(*args, **kwargs): # real signature unknown
    pass

def get_init(*args, **kwargs): # real signature unknown
    pass

def init(*args, **kwargs): # real signature unknown
    pass

def is_controller(*args, **kwargs): # real signature unknown
    """
    Check if the given joystick is supported by the game controller interface.
    
        :param int index: Index of the joystick.
    
        :return: 1 if supported, 0 if unsupported or invalid index.
    """
    pass

def name_forindex(*args, **kwargs): # real signature unknown
    """
    Returns the name of controller,
            or NULL if there's no name or the index is invalid.
    """
    pass

def quit(*args, **kwargs): # real signature unknown
    pass

def set_eventstate(*args, **kwargs): # real signature unknown
    pass

def update(*args, **kwargs): # real signature unknown
    """
    Will automatically called by the event loop,
            not necessary to call this function.
    """
    pass

def _gamecontroller_init_check(*args, **kwargs): # real signature unknown
    pass

def _internal_mod_init(*args, **kwargs): # real signature unknown
    pass

def __reduce_cython__(*args, **kwargs): # real signature unknown
    pass

def __setstate_cython__(*args, **kwargs): # real signature unknown
    pass

# classes

class Controller(object):
    # no doc
    def as_joystick(self, *args, **kwargs): # real signature unknown
        pass

    def attached(self, *args, **kwargs): # real signature unknown
        pass

    def from_joystick(self, *args, **kwargs): # real signature unknown
        """ Create a controller object from pygame.joystick.Joystick object. """
        pass

    def get_axis(self, *args, **kwargs): # real signature unknown
        pass

    def get_button(self, *args, **kwargs): # real signature unknown
        pass

    def get_init(self, *args, **kwargs): # real signature unknown
        pass

    def get_mapping(self, *args, **kwargs): # real signature unknown
        pass

    def init(self, *args, **kwargs): # real signature unknown
        pass

    def quit(self, *args, **kwargs): # real signature unknown
        pass

    def rumble(self, *args, **kwargs): # real signature unknown
        """
        Play a rumble effect on the controller, with set power (0-1 range) and
                duration (in ms). Returns True if the effect was played successfully,
                False otherwise.
        """
        pass

    def set_mapping(self, *args, **kwargs): # real signature unknown
        pass

    def stop_rumble(self, *args, **kwargs): # real signature unknown
        """ Stop any rumble effect playing on the controller. """
        pass

    def _CLOSEDCHECK(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        """
        Create a controller object and open it by given index.
        
                :param int index: Index of the joystick.
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

    id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    _controllers = []


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001E525E50ED0>'

__pyx_capi__ = {
    '_controller_autoinit': None, # (!) real value is '<capsule object "int (void)" at 0x000001E525ECBAE0>'
    '_controller_autoquit': None, # (!) real value is '<capsule object "void (void)" at 0x000001E5267282A0>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='pygame._sdl2.controller', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001E525E50ED0>, origin='C:\\\\Users\\\\leonm\\\\PycharmProjects\\\\leonsystem\\\\venv\\\\Lib\\\\site-packages\\\\pygame\\\\_sdl2\\\\controller.cp311-win_amd64.pyd')"

__test__ = {}

