# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


from .QObject import QObject

class QThreadPool(QObject):
    """ QThreadPool(parent: Optional[QObject] = None) """
    def activeThreadCount(self): # real signature unknown; restored from __doc__
        """ activeThreadCount(self) -> int """
        return 0

    def cancel(self, runnable, QRunnable=None): # real signature unknown; restored from __doc__
        """ cancel(self, runnable: Optional[QRunnable]) """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def contains(self, thread, QThread=None): # real signature unknown; restored from __doc__
        """ contains(self, thread: Optional[QThread]) -> bool """
        return False

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def expiryTimeout(self): # real signature unknown; restored from __doc__
        """ expiryTimeout(self) -> int """
        return 0

    def globalInstance(self): # real signature unknown; restored from __doc__
        """ globalInstance() -> Optional[QThreadPool] """
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def maxThreadCount(self): # real signature unknown; restored from __doc__
        """ maxThreadCount(self) -> int """
        return 0

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def releaseThread(self): # real signature unknown; restored from __doc__
        """ releaseThread(self) """
        pass

    def reserveThread(self): # real signature unknown; restored from __doc__
        """ reserveThread(self) """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setExpiryTimeout(self, expiryTimeout): # real signature unknown; restored from __doc__
        """ setExpiryTimeout(self, expiryTimeout: int) """
        pass

    def setMaxThreadCount(self, maxThreadCount): # real signature unknown; restored from __doc__
        """ setMaxThreadCount(self, maxThreadCount: int) """
        pass

    def setStackSize(self, stackSize): # real signature unknown; restored from __doc__
        """ setStackSize(self, stackSize: int) """
        pass

    def stackSize(self): # real signature unknown; restored from __doc__
        """ stackSize(self) -> int """
        return 0

    def start(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        start(self, runnable: Optional[QRunnable], priority: int = 0)
        start(self, functionToRun: Callable[[], None], priority: int = 0)
        """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def tryStart(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        tryStart(self, runnable: Optional[QRunnable]) -> bool
        tryStart(self, functionToRun: Callable[[], None]) -> bool
        """
        return False

    def tryTake(self, runnable, QRunnable=None): # real signature unknown; restored from __doc__
        """ tryTake(self, runnable: Optional[QRunnable]) -> bool """
        return False

    def waitForDone(self, msecs=-1): # real signature unknown; restored from __doc__
        """ waitForDone(self, msecs: int = -1) -> bool """
        return False

    def __init__(self, parent, QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass


