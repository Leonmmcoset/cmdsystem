# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


from .QInputEvent import QInputEvent

class QTouchEvent(QInputEvent):
    """
    QTouchEvent(eventType: QEvent.Type, device: Optional[QTouchDevice] = None, modifiers: Union[Qt.KeyboardModifiers, Qt.KeyboardModifier] = Qt.NoModifier, touchPointStates: Union[Qt.TouchPointStates, Qt.TouchPointState] = Qt.TouchPointStates(), touchPoints: Iterable[QTouchEvent.TouchPoint] = [])
    QTouchEvent(a0: QTouchEvent)
    """
    def device(self): # real signature unknown; restored from __doc__
        """ device(self) -> Optional[QTouchDevice] """
        pass

    def setDevice(self, adevice, QTouchDevice=None): # real signature unknown; restored from __doc__
        """ setDevice(self, adevice: Optional[QTouchDevice]) """
        pass

    def target(self): # real signature unknown; restored from __doc__
        """ target(self) -> Optional[QObject] """
        pass

    def touchPoints(self): # real signature unknown; restored from __doc__
        """ touchPoints(self) -> List[QTouchEvent.TouchPoint] """
        return []

    def touchPointStates(self): # real signature unknown; restored from __doc__
        """ touchPointStates(self) -> Qt.TouchPointStates """
        pass

    def window(self): # real signature unknown; restored from __doc__
        """ window(self) -> Optional[QWindow] """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass



