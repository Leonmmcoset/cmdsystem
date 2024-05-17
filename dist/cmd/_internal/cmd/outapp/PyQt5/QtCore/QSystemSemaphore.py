# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


class QSystemSemaphore(__sip.simplewrapper):
    """ QSystemSemaphore(key: Optional[str], initialValue: int = 0, mode: QSystemSemaphore.AccessMode = QSystemSemaphore.Open) """
    def acquire(self): # real signature unknown; restored from __doc__
        """ acquire(self) -> bool """
        return False

    def error(self): # real signature unknown; restored from __doc__
        """ error(self) -> QSystemSemaphore.SystemSemaphoreError """
        pass

    def errorString(self): # real signature unknown; restored from __doc__
        """ errorString(self) -> str """
        return ""

    def key(self): # real signature unknown; restored from __doc__
        """ key(self) -> str """
        return ""

    def release(self, n=1): # real signature unknown; restored from __doc__
        """ release(self, n: int = 1) -> bool """
        return False

    def setKey(self, key, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setKey(self, key: Optional[str], initialValue: int = 0, mode: QSystemSemaphore.AccessMode = QSystemSemaphore.Open) """
        pass

    def __init__(self, key, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    AlreadyExists = 3
    Create = 1
    KeyError = 2
    NoError = 0
    NotFound = 4
    Open = 0
    OutOfResources = 5
    PermissionDenied = 1
    UnknownError = 6


