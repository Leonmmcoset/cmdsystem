# encoding: utf-8
# module deploy_libs._overlapped
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\deploy_libs\_overlapped.pyd
# by generator 1.147
# no doc

# imports
from _overlapped import Overlapped


# Variables with simple values

ERROR_IO_PENDING = 997

ERROR_NETNAME_DELETED = 64

ERROR_OPERATION_ABORTED = 995

ERROR_PIPE_BUSY = 231

ERROR_SEM_TIMEOUT = 121

INFINITE = 4294967295

INVALID_HANDLE_VALUE = 18446744073709551615

NULL = 0

SO_UPDATE_ACCEPT_CONTEXT = 28683

SO_UPDATE_CONNECT_CONTEXT = 28688

TF_REUSE_SOCKET = 2

# functions

def BindLocal(*args, **kwargs): # real signature unknown
    """
    Bind a socket handle to an arbitrary local port.
    
    family should be AF_INET or AF_INET6.
    """
    pass

def ConnectPipe(*args, **kwargs): # real signature unknown
    """ Connect to the pipe for asynchronous I/O (overlapped). """
    pass

def CreateEvent(*args, **kwargs): # real signature unknown
    """
    Create an event.
    
    EventAttributes must be None.
    """
    pass

def CreateIoCompletionPort(*args, **kwargs): # real signature unknown
    """ Create a completion port or register a handle with a port. """
    pass

def FormatMessage(*args, **kwargs): # real signature unknown
    """ Return error message for an error code. """
    pass

def GetQueuedCompletionStatus(*args, **kwargs): # real signature unknown
    """
    Get a message from completion port.
    
    Wait for up to msecs milliseconds.
    """
    pass

def PostQueuedCompletionStatus(*args, **kwargs): # real signature unknown
    """ Post a message to completion port. """
    pass

def RegisterWaitWithQueue(*args, **kwargs): # real signature unknown
    """ Register wait for Object; when complete CompletionPort is notified. """
    pass

def ResetEvent(*args, **kwargs): # real signature unknown
    """ Reset event. """
    pass

def SetEvent(*args, **kwargs): # real signature unknown
    """ Set event. """
    pass

def UnregisterWait(*args, **kwargs): # real signature unknown
    """ Unregister wait handle. """
    pass

def UnregisterWaitEx(*args, **kwargs): # real signature unknown
    """ Unregister wait handle. """
    pass

def WSAConnect(*args, **kwargs): # real signature unknown
    """ Bind a remote address to a connectionless (UDP) socket. """
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001777C81A250>'

__spec__ = None # (!) real value is "ModuleSpec(name='deploy_libs._overlapped', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001777C81A250>, origin='C:\\\\Users\\\\leonm\\\\PycharmProjects\\\\LeonRandomPlus\\\\venv\\\\Lib\\\\site-packages\\\\deploy_libs\\\\_overlapped.pyd')"

