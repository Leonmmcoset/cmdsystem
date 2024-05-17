# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


from .QAbstractAnimation import QAbstractAnimation

class QVariantAnimation(QAbstractAnimation):
    """ QVariantAnimation(parent: Optional[QObject] = None) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def currentValue(self): # real signature unknown; restored from __doc__
        """ currentValue(self) -> Any """
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def duration(self): # real signature unknown; restored from __doc__
        """ duration(self) -> int """
        return 0

    def easingCurve(self): # real signature unknown; restored from __doc__
        """ easingCurve(self) -> QEasingCurve """
        return QEasingCurve

    def endValue(self): # real signature unknown; restored from __doc__
        """ endValue(self) -> Any """
        pass

    def event(self, event, QEvent=None): # real signature unknown; restored from __doc__
        """ event(self, event: Optional[QEvent]) -> bool """
        return False

    def interpolated(self, from_, to, progress): # real signature unknown; restored from __doc__
        """ interpolated(self, from_: Any, to: Any, progress: float) -> Any """
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def keyValueAt(self, step): # real signature unknown; restored from __doc__
        """ keyValueAt(self, step: float) -> Any """
        pass

    def keyValues(self): # real signature unknown; restored from __doc__
        """ keyValues(self) -> List[Tuple[float, Any]] """
        return []

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setDuration(self, msecs): # real signature unknown; restored from __doc__
        """ setDuration(self, msecs: int) """
        pass

    def setEasingCurve(self, easing, QEasingCurve=None, QEasingCurve_Type=None): # real signature unknown; restored from __doc__
        """ setEasingCurve(self, easing: Union[QEasingCurve, QEasingCurve.Type]) """
        pass

    def setEndValue(self, value): # real signature unknown; restored from __doc__
        """ setEndValue(self, value: Any) """
        pass

    def setKeyValueAt(self, step, value): # real signature unknown; restored from __doc__
        """ setKeyValueAt(self, step: float, value: Any) """
        pass

    def setKeyValues(self, values, Tuple=None, p_float=None, Any=None): # real signature unknown; restored from __doc__
        """ setKeyValues(self, values: Iterable[Tuple[float, Any]]) """
        pass

    def setStartValue(self, value): # real signature unknown; restored from __doc__
        """ setStartValue(self, value: Any) """
        pass

    def startValue(self): # real signature unknown; restored from __doc__
        """ startValue(self) -> Any """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def updateCurrentTime(self, a0): # real signature unknown; restored from __doc__
        """ updateCurrentTime(self, a0: int) """
        pass

    def updateCurrentValue(self, value): # real signature unknown; restored from __doc__
        """ updateCurrentValue(self, value: Any) """
        pass

    def updateDirection(self, *args, **kwargs): # real signature unknown
        pass

    def updateState(self, newState, oldState): # real signature unknown; restored from __doc__
        """ updateState(self, newState: QAbstractAnimation.State, oldState: QAbstractAnimation.State) """
        pass

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

    def __init__(self, parent, QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass


