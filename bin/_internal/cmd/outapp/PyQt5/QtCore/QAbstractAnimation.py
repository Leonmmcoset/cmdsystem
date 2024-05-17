# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


from .QObject import QObject

class QAbstractAnimation(QObject):
    """ QAbstractAnimation(parent: Optional[QObject] = None) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def currentLoop(self): # real signature unknown; restored from __doc__
        """ currentLoop(self) -> int """
        return 0

    def currentLoopChanged(self, *args, **kwargs): # real signature unknown
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

    def currentLoopTime(self): # real signature unknown; restored from __doc__
        """ currentLoopTime(self) -> int """
        return 0

    def currentTime(self): # real signature unknown; restored from __doc__
        """ currentTime(self) -> int """
        return 0

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def direction(self): # real signature unknown; restored from __doc__
        """ direction(self) -> QAbstractAnimation.Direction """
        pass

    def directionChanged(self, *args, **kwargs): # real signature unknown
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

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def duration(self): # real signature unknown; restored from __doc__
        """ duration(self) -> int """
        return 0

    def event(self, event, QEvent=None): # real signature unknown; restored from __doc__
        """ event(self, event: Optional[QEvent]) -> bool """
        return False

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

    def group(self): # real signature unknown; restored from __doc__
        """ group(self) -> Optional[QAnimationGroup] """
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def loopCount(self): # real signature unknown; restored from __doc__
        """ loopCount(self) -> int """
        return 0

    def pause(self): # real signature unknown; restored from __doc__
        """ pause(self) """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def resume(self): # real signature unknown; restored from __doc__
        """ resume(self) """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setCurrentTime(self, msecs): # real signature unknown; restored from __doc__
        """ setCurrentTime(self, msecs: int) """
        pass

    def setDirection(self, direction): # real signature unknown; restored from __doc__
        """ setDirection(self, direction: QAbstractAnimation.Direction) """
        pass

    def setLoopCount(self, loopCount): # real signature unknown; restored from __doc__
        """ setLoopCount(self, loopCount: int) """
        pass

    def setPaused(self, a0): # real signature unknown; restored from __doc__
        """ setPaused(self, a0: bool) """
        pass

    def start(self, policy=None): # real signature unknown; restored from __doc__
        """ start(self, policy: QAbstractAnimation.DeletionPolicy = QAbstractAnimation.KeepWhenStopped) """
        pass

    def state(self): # real signature unknown; restored from __doc__
        """ state(self) -> QAbstractAnimation.State """
        pass

    def stateChanged(self, *args, **kwargs): # real signature unknown
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

    def stop(self): # real signature unknown; restored from __doc__
        """ stop(self) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def totalDuration(self): # real signature unknown; restored from __doc__
        """ totalDuration(self) -> int """
        return 0

    def updateCurrentTime(self, currentTime): # real signature unknown; restored from __doc__
        """ updateCurrentTime(self, currentTime: int) """
        pass

    def updateDirection(self, direction): # real signature unknown; restored from __doc__
        """ updateDirection(self, direction: QAbstractAnimation.Direction) """
        pass

    def updateState(self, newState, oldState): # real signature unknown; restored from __doc__
        """ updateState(self, newState: QAbstractAnimation.State, oldState: QAbstractAnimation.State) """
        pass

    def __init__(self, parent, QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    Backward = 1
    DeleteWhenStopped = 1
    Forward = 0
    KeepWhenStopped = 0
    Paused = 1
    Running = 2
    Stopped = 0


