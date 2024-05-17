# encoding: utf-8
# module _signal
# from (built-in)
# by generator 1.147
"""
This module provides mechanisms to use signal handlers in Python.

Functions:

alarm() -- cause SIGALRM after a specified time [Unix only]
setitimer() -- cause a signal (described below) after a specified
               float time and the timer may restart then [Unix only]
getitimer() -- get current value of timer [Unix only]
signal() -- set the action for a given signal
getsignal() -- get the signal action for a given signal
pause() -- wait until a signal arrives [Unix only]
default_int_handler() -- default SIGINT handler

signal constants:
SIG_DFL -- used to refer to the system default handler
SIG_IGN -- used to ignore the signal
NSIG -- number of defined signals
SIGINT, SIGTERM, etc. -- signal numbers

itimer constants:
ITIMER_REAL -- decrements in real time, and delivers SIGALRM upon
               expiration
ITIMER_VIRTUAL -- decrements only when the process is executing,
               and delivers SIGVTALRM upon expiration
ITIMER_PROF -- decrements both when the process is executing and
               when the system is executing on behalf of the process.
               Coupled with ITIMER_VIRTUAL, this timer is usually
               used to profile the time spent by the application
               in user and kernel space. SIGPROF is delivered upon
               expiration.


*** IMPORTANT NOTICE ***
A signal handler function is called with two arguments:
the first is the signal number, the second is the interrupted stack frame.
"""
# no imports

# Variables with simple values

CTRL_BREAK_EVENT = 1

CTRL_C_EVENT = 0

NSIG = 23

SIGABRT = 22
SIGBREAK = 21
SIGFPE = 8
SIGILL = 4
SIGINT = 2
SIGSEGV = 11
SIGTERM = 15

SIG_DFL = 0
SIG_IGN = 1

# functions

def default_int_handler(*args, **kwargs): # real signature unknown
    """
    The default handler for SIGINT installed by Python.
    
    It raises KeyboardInterrupt.
    """
    pass

def getsignal(*args, **kwargs): # real signature unknown
    """
    Return the current action for the given signal.
    
    The return value can be:
      SIG_IGN -- if the signal is being ignored
      SIG_DFL -- if the default action for the signal is in effect
      None    -- if an unknown handler is in effect
      anything else -- the callable Python object used as a handler
    """
    pass

def raise_signal(*args, **kwargs): # real signature unknown
    """ Send a signal to the executing process. """
    pass

def set_wakeup_fd(fd, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    set_wakeup_fd(fd, *, warn_on_full_buffer=True) -> fd
    
    Sets the fd to be written to (with the signal number) when a signal
    comes in.  A library can use this to wakeup select or poll.
    The previous fd or -1 is returned.
    
    The fd must be non-blocking.
    """
    pass

def signal(): # real signature unknown; restored from __doc__
    """
    Set the action for the given signal.
    
    The action can be SIG_DFL, SIG_IGN, or a callable Python object.
    The previous action is returned.  See getsignal() for possible return values.
    
    *** IMPORTANT NOTICE ***
    A signal handler function is called with two arguments:
    the first is the signal number, the second is the interrupted stack frame.
    """
    pass

def strsignal(*args, **kwargs): # real signature unknown
    """
    Return the system description of the given signal.
    
    The return values can be such as "Interrupt", "Segmentation fault", etc.
    Returns None if the signal is not recognized.
    """
    pass

def valid_signals(*args, **kwargs): # real signature unknown
    """
    Return a set of valid signal numbers on this platform.
    
    The signal numbers returned by this function can be safely passed to
    functions like `pthread_sigmask`.
    """
    pass

# classes

class __loader__(object):
    """
    Meta path import for built-in modules.
    
        All methods are either class or static methods to avoid the need to
        instantiate the class.
    """
    def create_module(spec): # reliably restored by inspect
        """ Create a built-in module """
        pass

    def exec_module(module): # reliably restored by inspect
        """ Exec a built-in module """
        pass

    @classmethod
    def find_module(cls, *args, **kwargs): # real signature unknown
        """
        Find the built-in module.
        
                If 'path' is ever specified then the search is considered a failure.
        
                This method is deprecated.  Use find_spec() instead.
        """
        pass

    @classmethod
    def find_spec(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def get_code(cls, *args, **kwargs): # real signature unknown
        """ Return None as built-in modules do not have code objects. """
        pass

    @classmethod
    def get_source(cls, *args, **kwargs): # real signature unknown
        """ Return None as built-in modules do not have source code. """
        pass

    @classmethod
    def is_package(cls, *args, **kwargs): # real signature unknown
        """ Return False as built-in modules are never packages. """
        pass

    @classmethod
    def load_module(cls, *args, **kwargs): # real signature unknown
        """
        Load the specified module into sys.modules and return it.
        
            This method is deprecated.  Use loader.exec_module() instead.
        """
        pass

    def module_repr(module): # reliably restored by inspect
        """
        Return repr for the module.
        
                The method is deprecated.  The import machinery does the job itself.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    _ORIGIN = 'built-in'
    __dict__ = None # (!) real value is "mappingproxy({'__module__': '_frozen_importlib', '__doc__': 'Meta path import for built-in modules.\\n\\n    All methods are either class or static methods to avoid the need to\\n    instantiate the class.\\n\\n    ', '_ORIGIN': 'built-in', 'module_repr': <staticmethod(<function BuiltinImporter.module_repr at 0x000001E3875E28E0>)>, 'find_spec': <classmethod(<function BuiltinImporter.find_spec at 0x000001E3875E2980>)>, 'find_module': <classmethod(<function BuiltinImporter.find_module at 0x000001E3875E2A20>)>, 'create_module': <staticmethod(<function BuiltinImporter.create_module at 0x000001E3875E2AC0>)>, 'exec_module': <staticmethod(<function BuiltinImporter.exec_module at 0x000001E3875E2B60>)>, 'get_code': <classmethod(<function BuiltinImporter.get_code at 0x000001E3875E2CA0>)>, 'get_source': <classmethod(<function BuiltinImporter.get_source at 0x000001E3875E2DE0>)>, 'is_package': <classmethod(<function BuiltinImporter.is_package at 0x000001E3875E2F20>)>, 'load_module': <classmethod(<function _load_module_shim at 0x000001E3875E1C60>)>, '__dict__': <attribute '__dict__' of 'BuiltinImporter' objects>, '__weakref__': <attribute '__weakref__' of 'BuiltinImporter' objects>})"


# variables with complex values

__spec__ = None # (!) real value is "ModuleSpec(name='_signal', loader=<class '_frozen_importlib.BuiltinImporter'>, origin='built-in')"

