# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


from .QObject import QObject

class QThread(QObject):
    """ QThread(parent: Optional[QObject] = None) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def currentThread(self): # real signature unknown; restored from __doc__
        """ currentThread() -> Optional[QThread] """
        pass

    def currentThreadId(self): # real signature unknown; restored from __doc__
        """ currentThreadId() -> Optional[PyQt5.sip.voidptr] """
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, event, QEvent=None): # real signature unknown; restored from __doc__
        """ event(self, event: Optional[QEvent]) -> bool """
        return False

    def eventDispatcher(self): # real signature unknown; restored from __doc__
        """ eventDispatcher(self) -> Optional[QAbstractEventDispatcher] """
        pass

    def exec(self): # real signature unknown; restored from __doc__
        """ exec(self) -> int """
        return 0

    def exec_(self): # real signature unknown; restored from __doc__
        """ exec_(self) -> int """
        return 0

    def exit(self, returnCode=0): # real signature unknown; restored from __doc__
        """ exit(self, returnCode: int = 0) """
        pass

    def finished(self, *args, **kwargs): # real signature unknown
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
        pass

    def idealThreadCount(self): # real signature unknown; restored from __doc__
        """ idealThreadCount() -> int """
        return 0

    def isFinished(self): # real signature unknown; restored from __doc__
        """ isFinished(self) -> bool """
        return False

    def isInterruptionRequested(self): # real signature unknown; restored from __doc__
        """ isInterruptionRequested(self) -> bool """
        return False

    def isRunning(self): # real signature unknown; restored from __doc__
        """ isRunning(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def loopLevel(self): # real signature unknown; restored from __doc__
        """ loopLevel(self) -> int """
        return 0

    def msleep(self, a0): # real signature unknown; restored from __doc__
        """ msleep(a0: int) """
        pass

    def priority(self): # real signature unknown; restored from __doc__
        """ priority(self) -> QThread.Priority """
        pass

    def quit(self): # real signature unknown; restored from __doc__
        """ quit(self) """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def requestInterruption(self): # real signature unknown; restored from __doc__
        """ requestInterruption(self) """
        pass

    def run(self): # real signature unknown; restored from __doc__
        """ run(self) """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setEventDispatcher(self, eventDispatcher, QAbstractEventDispatcher=None): # real signature unknown; restored from __doc__
        """ setEventDispatcher(self, eventDispatcher: Optional[QAbstractEventDispatcher]) """
        pass

    def setPriority(self, priority): # real signature unknown; restored from __doc__
        """ setPriority(self, priority: QThread.Priority) """
        pass

    def setStackSize(self, stackSize): # real signature unknown; restored from __doc__
        """ setStackSize(self, stackSize: int) """
        pass

    def setTerminationEnabled(self, enabled=True): # real signature unknown; restored from __doc__
        """ setTerminationEnabled(enabled: bool = True) """
        pass

    def sleep(self, a0): # real signature unknown; restored from __doc__
        """ sleep(a0: int) """
        pass

    def stackSize(self): # real signature unknown; restored from __doc__
        """ stackSize(self) -> int """
        return 0

    def start(self, priority=None): # real signature unknown; restored from __doc__
        """ start(self, priority: QThread.Priority = QThread.InheritPriority) """
        pass

    def started(self, *args, **kwargs): # real signature unknown
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
        pass

    def terminate(self): # real signature unknown; restored from __doc__
        """ terminate(self) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def usleep(self, a0): # real signature unknown; restored from __doc__
        """ usleep(a0: int) """
        pass

    def wait(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        wait(self, msecs: int = ULONG_MAX) -> bool
        wait(self, deadline: QDeadlineTimer) -> bool
        """
        return False

    def yieldCurrentThread(self): # real signature unknown; restored from __doc__
        """ yieldCurrentThread() """
        pass

    def __init__(self, parent, QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    HighestPriority = 5
    HighPriority = 4
    IdlePriority = 0
    InheritPriority = 7
    LowestPriority = 1
    LowPriority = 2
    NormalPriority = 3
    TimeCriticalPriority = 6


