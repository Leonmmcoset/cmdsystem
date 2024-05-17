# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


from .QObject import QObject

class QTimeLine(QObject):
    """ QTimeLine(duration: int = 1000, parent: Optional[QObject] = None) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def currentFrame(self): # real signature unknown; restored from __doc__
        """ currentFrame(self) -> int """
        return 0

    def currentTime(self): # real signature unknown; restored from __doc__
        """ currentTime(self) -> int """
        return 0

    def currentValue(self): # real signature unknown; restored from __doc__
        """ currentValue(self) -> float """
        return 0.0

    def curveShape(self): # real signature unknown; restored from __doc__
        """ curveShape(self) -> QTimeLine.CurveShape """
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def direction(self): # real signature unknown; restored from __doc__
        """ direction(self) -> QTimeLine.Direction """
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def duration(self): # real signature unknown; restored from __doc__
        """ duration(self) -> int """
        return 0

    def easingCurve(self): # real signature unknown; restored from __doc__
        """ easingCurve(self) -> QEasingCurve """
        return QEasingCurve

    def endFrame(self): # real signature unknown; restored from __doc__
        """ endFrame(self) -> int """
        return 0

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

    def frameChanged(self, *args, **kwargs): # real signature unknown
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

    def frameForTime(self, msec): # real signature unknown; restored from __doc__
        """ frameForTime(self, msec: int) -> int """
        return 0

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def loopCount(self): # real signature unknown; restored from __doc__
        """ loopCount(self) -> int """
        return 0

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def resume(self): # real signature unknown; restored from __doc__
        """ resume(self) """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setCurrentTime(self, msec): # real signature unknown; restored from __doc__
        """ setCurrentTime(self, msec: int) """
        pass

    def setCurveShape(self, shape): # real signature unknown; restored from __doc__
        """ setCurveShape(self, shape: QTimeLine.CurveShape) """
        pass

    def setDirection(self, direction): # real signature unknown; restored from __doc__
        """ setDirection(self, direction: QTimeLine.Direction) """
        pass

    def setDuration(self, duration): # real signature unknown; restored from __doc__
        """ setDuration(self, duration: int) """
        pass

    def setEasingCurve(self, curve, QEasingCurve=None, QEasingCurve_Type=None): # real signature unknown; restored from __doc__
        """ setEasingCurve(self, curve: Union[QEasingCurve, QEasingCurve.Type]) """
        pass

    def setEndFrame(self, frame): # real signature unknown; restored from __doc__
        """ setEndFrame(self, frame: int) """
        pass

    def setFrameRange(self, startFrame, endFrame): # real signature unknown; restored from __doc__
        """ setFrameRange(self, startFrame: int, endFrame: int) """
        pass

    def setLoopCount(self, count): # real signature unknown; restored from __doc__
        """ setLoopCount(self, count: int) """
        pass

    def setPaused(self, paused): # real signature unknown; restored from __doc__
        """ setPaused(self, paused: bool) """
        pass

    def setStartFrame(self, frame): # real signature unknown; restored from __doc__
        """ setStartFrame(self, frame: int) """
        pass

    def setUpdateInterval(self, interval): # real signature unknown; restored from __doc__
        """ setUpdateInterval(self, interval: int) """
        pass

    def start(self): # real signature unknown; restored from __doc__
        """ start(self) """
        pass

    def startFrame(self): # real signature unknown; restored from __doc__
        """ startFrame(self) -> int """
        return 0

    def state(self): # real signature unknown; restored from __doc__
        """ state(self) -> QTimeLine.State """
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

    def timerEvent(self, event, QTimerEvent=None): # real signature unknown; restored from __doc__
        """ timerEvent(self, event: Optional[QTimerEvent]) """
        pass

    def toggleDirection(self): # real signature unknown; restored from __doc__
        """ toggleDirection(self) """
        pass

    def updateInterval(self): # real signature unknown; restored from __doc__
        """ updateInterval(self) -> int """
        return 0

    def valueChanged(self, *args, **kwargs): # real signature unknown
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

    def valueForTime(self, msec): # real signature unknown; restored from __doc__
        """ valueForTime(self, msec: int) -> float """
        return 0.0

    def __init__(self, duration=1000, parent, QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    Backward = 1
    CosineCurve = 5
    EaseInCurve = 0
    EaseInOutCurve = 2
    EaseOutCurve = 1
    Forward = 0
    LinearCurve = 3
    NotRunning = 0
    Paused = 1
    Running = 2
    SineCurve = 4


