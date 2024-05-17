# encoding: utf-8
# module PyQt5.QtWidgets
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


class QGestureEvent(__PyQt5_QtCore.QEvent):
    """
    QGestureEvent(gestures: Iterable[QGesture])
    QGestureEvent(a0: QGestureEvent)
    """
    def accept(self, a0=None, QGesture=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        accept(self)
        accept(self, a0: Optional[QGesture])
        accept(self, a0: Qt.GestureType)
        """
        pass

    def activeGestures(self): # real signature unknown; restored from __doc__
        """ activeGestures(self) -> List[QGesture] """
        return []

    def canceledGestures(self): # real signature unknown; restored from __doc__
        """ canceledGestures(self) -> List[QGesture] """
        return []

    def gesture(self, type): # real signature unknown; restored from __doc__
        """ gesture(self, type: Qt.GestureType) -> Optional[QGesture] """
        pass

    def gestures(self): # real signature unknown; restored from __doc__
        """ gestures(self) -> List[QGesture] """
        return []

    def ignore(self, a0=None, QGesture=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        ignore(self)
        ignore(self, a0: Optional[QGesture])
        ignore(self, a0: Qt.GestureType)
        """
        pass

    def isAccepted(self, a0=None, QGesture=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        isAccepted(self) -> bool
        isAccepted(self, a0: Optional[QGesture]) -> bool
        isAccepted(self, a0: Qt.GestureType) -> bool
        """
        return False

    def mapToGraphicsScene(self, gesturePoint, QPointF=None, QPoint=None): # real signature unknown; restored from __doc__
        """ mapToGraphicsScene(self, gesturePoint: Union[QPointF, QPoint]) -> QPointF """
        pass

    def setAccepted(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setAccepted(self, accepted: bool)
        setAccepted(self, a0: Optional[QGesture], a1: bool)
        setAccepted(self, a0: Qt.GestureType, a1: bool)
        """
        pass

    def widget(self): # real signature unknown; restored from __doc__
        """ widget(self) -> Optional[QWidget] """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


