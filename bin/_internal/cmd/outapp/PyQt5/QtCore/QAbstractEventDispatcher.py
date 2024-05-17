# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


from .QObject import QObject

class QAbstractEventDispatcher(QObject):
    """ QAbstractEventDispatcher(parent: Optional[QObject] = None) """
    def aboutToBlock(self, *args, **kwargs): # real signature unknown
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

    def awake(self, *args, **kwargs): # real signature unknown
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

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def closingDown(self): # real signature unknown; restored from __doc__
        """ closingDown(self) """
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def filterNativeEvent(self, eventType, QByteArray=None, bytes=None, bytearray=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ filterNativeEvent(self, eventType: Union[QByteArray, bytes, bytearray], message: Optional[PyQt5.sip.voidptr]) -> (bool, Optional[int]) """
        pass

    def flush(self): # real signature unknown; restored from __doc__
        """ flush(self) """
        pass

    def hasPendingEvents(self): # real signature unknown; restored from __doc__
        """ hasPendingEvents(self) -> bool """
        return False

    def installNativeEventFilter(self, filterObj, QAbstractNativeEventFilter=None): # real signature unknown; restored from __doc__
        """ installNativeEventFilter(self, filterObj: Optional[QAbstractNativeEventFilter]) """
        pass

    def instance(self, thread, QThread=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ instance(thread: Optional[QThread] = None) -> Optional[QAbstractEventDispatcher] """
        pass

    def interrupt(self): # real signature unknown; restored from __doc__
        """ interrupt(self) """
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def processEvents(self, flags, QEventLoop_ProcessEventsFlags=None, QEventLoop_ProcessEventsFlag=None): # real signature unknown; restored from __doc__
        """ processEvents(self, flags: Union[QEventLoop.ProcessEventsFlags, QEventLoop.ProcessEventsFlag]) -> bool """
        return False

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def registeredTimers(self, p_object, QObject=None): # real signature unknown; restored from __doc__
        """ registeredTimers(self, object: Optional[QObject]) -> List[QAbstractEventDispatcher.TimerInfo] """
        return []

    def registerEventNotifier(self, notifier, QWinEventNotifier=None): # real signature unknown; restored from __doc__
        """ registerEventNotifier(self, notifier: Optional[QWinEventNotifier]) -> bool """
        return False

    def registerSocketNotifier(self, notifier, QSocketNotifier=None): # real signature unknown; restored from __doc__
        """ registerSocketNotifier(self, notifier: Optional[QSocketNotifier]) """
        pass

    def registerTimer(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        registerTimer(self, interval: int, timerType: Qt.TimerType, object: Optional[QObject]) -> int
        registerTimer(self, timerId: int, interval: int, timerType: Qt.TimerType, object: Optional[QObject])
        """
        return 0

    def remainingTime(self, timerId): # real signature unknown; restored from __doc__
        """ remainingTime(self, timerId: int) -> int """
        return 0

    def removeNativeEventFilter(self, filterObj, QAbstractNativeEventFilter=None): # real signature unknown; restored from __doc__
        """ removeNativeEventFilter(self, filterObj: Optional[QAbstractNativeEventFilter]) """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def startingUp(self): # real signature unknown; restored from __doc__
        """ startingUp(self) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def unregisterEventNotifier(self, notifier, QWinEventNotifier=None): # real signature unknown; restored from __doc__
        """ unregisterEventNotifier(self, notifier: Optional[QWinEventNotifier]) """
        pass

    def unregisterSocketNotifier(self, notifier, QSocketNotifier=None): # real signature unknown; restored from __doc__
        """ unregisterSocketNotifier(self, notifier: Optional[QSocketNotifier]) """
        pass

    def unregisterTimer(self, timerId): # real signature unknown; restored from __doc__
        """ unregisterTimer(self, timerId: int) -> bool """
        return False

    def unregisterTimers(self, p_object, QObject=None): # real signature unknown; restored from __doc__
        """ unregisterTimers(self, object: Optional[QObject]) -> bool """
        return False

    def wakeUp(self): # real signature unknown; restored from __doc__
        """ wakeUp(self) """
        pass

    def __init__(self, parent, QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass



