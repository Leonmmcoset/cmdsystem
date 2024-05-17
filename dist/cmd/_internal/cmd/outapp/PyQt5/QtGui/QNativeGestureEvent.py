# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


from .QInputEvent import QInputEvent

class QNativeGestureEvent(QInputEvent):
    """
    QNativeGestureEvent(type: Qt.NativeGestureType, localPos: Union[QPointF, QPoint], windowPos: Union[QPointF, QPoint], screenPos: Union[QPointF, QPoint], value: float, sequenceId: int, intArgument: int)
    QNativeGestureEvent(type: Qt.NativeGestureType, dev: Optional[QTouchDevice], localPos: Union[QPointF, QPoint], windowPos: Union[QPointF, QPoint], screenPos: Union[QPointF, QPoint], value: float, sequenceId: int, intArgument: int)
    QNativeGestureEvent(a0: QNativeGestureEvent)
    """
    def device(self): # real signature unknown; restored from __doc__
        """ device(self) -> Optional[QTouchDevice] """
        pass

    def gestureType(self): # real signature unknown; restored from __doc__
        """ gestureType(self) -> Qt.NativeGestureType """
        pass

    def globalPos(self): # real signature unknown; restored from __doc__
        """ globalPos(self) -> QPoint """
        pass

    def localPos(self): # real signature unknown; restored from __doc__
        """ localPos(self) -> QPointF """
        pass

    def pos(self): # real signature unknown; restored from __doc__
        """ pos(self) -> QPoint """
        pass

    def screenPos(self): # real signature unknown; restored from __doc__
        """ screenPos(self) -> QPointF """
        pass

    def value(self): # real signature unknown; restored from __doc__
        """ value(self) -> float """
        return 0.0

    def windowPos(self): # real signature unknown; restored from __doc__
        """ windowPos(self) -> QPointF """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


