# encoding: utf-8
# module deploy_libs._tkinter
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\deploy_libs\_tkinter.pyd
# by generator 1.147
# no doc

# imports
from _tkinter import TclError, Tcl_Obj, TkappType, TkttType


# Variables with simple values

ALL_EVENTS = -3

DONT_WAIT = 2

EXCEPTION = 8

FILE_EVENTS = 8

IDLE_EVENTS = 32

READABLE = 2

TCL_VERSION = '8.6'

TIMER_EVENTS = 16

TK_VERSION = '8.6'

WINDOW_EVENTS = 4

WRITABLE = 4

# functions

def create(*args, **kwargs): # real signature unknown
    """
    wantTk
        if false, then Tk_Init() doesn't get called
      sync
        if true, then pass -sync to wish
      use
        if not None, then pass -use to wish
    """
    pass

def getbusywaitinterval(*args, **kwargs): # real signature unknown
    """ Return the current busy-wait interval between successive calls to Tcl_DoOneEvent in a threaded Python interpreter. """
    pass

def setbusywaitinterval(*args, **kwargs): # real signature unknown
    """
    Set the busy-wait interval in milliseconds between successive calls to Tcl_DoOneEvent in a threaded Python interpreter.
    
    It should be set to a divisor of the maximum time between frames in an animation.
    """
    pass

def _flatten(*args, **kwargs): # real signature unknown
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x00000283617AA250>'

__spec__ = None # (!) real value is "ModuleSpec(name='deploy_libs._tkinter', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x00000283617AA250>, origin='C:\\\\Users\\\\leonm\\\\PycharmProjects\\\\LeonRandomPlus\\\\venv\\\\Lib\\\\site-packages\\\\deploy_libs\\\\_tkinter.pyd')"

