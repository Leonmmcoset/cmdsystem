# encoding: utf-8
# module pygame._sdl2.sdl2
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\pygame\_sdl2\sdl2.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>

# Variables with simple values

INIT_AUDIO = 16
INIT_EVENTS = 16384
INIT_EVERYTHING = 62001
INIT_GAMECONTROLLER = 8192
INIT_HAPTIC = 4096
INIT_JOYSTICK = 512
INIT_NOPARACHUTE = 1048576
INIT_TIMER = 1
INIT_VIDEO = 32

# functions

def init_subsystem(*args, **kwargs): # real signature unknown
    """
    Use this function to initialize specific subsystems.
    
        :param int flags: any of the flags used by.
    
            * INIT_TIMER timer subsystem
            * INIT_AUDIO audio subsystem
            * INIT_VIDEO video subsystem; automatically initializes the events subsystem
            * INIT_JOYSTICK joystick subsystem; automatically initializes the events subsystem
            * INIT_HAPTIC haptic (force feedback) subsystem
            * INIT_GAMECONTROLLER controller subsystem; automatically initializes the joystick subsystem
            * INIT_EVENTS events subsystem
            * INIT_EVERYTHING all of the above subsystems
            * INIT_NOPARACHUTE compatibility; this flag is ignored
    """
    pass

# classes

class error(RuntimeError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x0000023B08317350>'

__spec__ = None # (!) real value is "ModuleSpec(name='pygame._sdl2.sdl2', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x0000023B08317350>, origin='C:\\\\Users\\\\leonm\\\\PycharmProjects\\\\leonsystem\\\\venv\\\\Lib\\\\site-packages\\\\pygame\\\\_sdl2\\\\sdl2.cp311-win_amd64.pyd')"

__test__ = {}

