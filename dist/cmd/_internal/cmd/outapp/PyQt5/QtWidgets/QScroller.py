# encoding: utf-8
# module PyQt5.QtWidgets
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


class QScroller(__PyQt5_QtCore.QObject):
    # no doc
    def activeScrollers(self): # real signature unknown; restored from __doc__
        """ activeScrollers() -> List[QScroller] """
        return []

    def ensureVisible(self, rect, xmargin, ymargin, scrollTime=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        ensureVisible(self, rect: QRectF, xmargin: float, ymargin: float)
        ensureVisible(self, rect: QRectF, xmargin: float, ymargin: float, scrollTime: int)
        """
        pass

    def finalPosition(self): # real signature unknown; restored from __doc__
        """ finalPosition(self) -> QPointF """
        pass

    def grabbedGesture(self, target, QObject=None): # real signature unknown; restored from __doc__
        """ grabbedGesture(target: Optional[QObject]) -> Qt.GestureType """
        pass

    def grabGesture(self, target, QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ grabGesture(target: Optional[QObject], scrollGestureType: QScroller.ScrollerGestureType = QScroller.TouchGesture) -> Qt.GestureType """
        pass

    def handleInput(self, input, position, QPointF=None, QPoint=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ handleInput(self, input: QScroller.Input, position: Union[QPointF, QPoint], timestamp: int = 0) -> bool """
        pass

    def hasScroller(self, target, QObject=None): # real signature unknown; restored from __doc__
        """ hasScroller(target: Optional[QObject]) -> bool """
        return False

    def pixelPerMeter(self): # real signature unknown; restored from __doc__
        """ pixelPerMeter(self) -> QPointF """
        pass

    def resendPrepareEvent(self): # real signature unknown; restored from __doc__
        """ resendPrepareEvent(self) """
        pass

    def scroller(self, target, QObject=None): # real signature unknown; restored from __doc__
        """ scroller(target: Optional[QObject]) -> Optional[QScroller] """
        pass

    def scrollerProperties(self): # real signature unknown; restored from __doc__
        """ scrollerProperties(self) -> QScrollerProperties """
        return QScrollerProperties

    def scrollerPropertiesChanged(self, *args, **kwargs): # real signature unknown
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

    def scrollTo(self, pos, QPointF=None, QPoint=None, *args=None, **kwargs=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        scrollTo(self, pos: Union[QPointF, QPoint])
        scrollTo(self, pos: Union[QPointF, QPoint], scrollTime: int)
        """
        pass

    def setScrollerProperties(self, prop): # real signature unknown; restored from __doc__
        """ setScrollerProperties(self, prop: QScrollerProperties) """
        pass

    def setSnapPositionsX(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setSnapPositionsX(self, positions: Iterable[float])
        setSnapPositionsX(self, first: float, interval: float)
        """
        pass

    def setSnapPositionsY(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setSnapPositionsY(self, positions: Iterable[float])
        setSnapPositionsY(self, first: float, interval: float)
        """
        pass

    def state(self): # real signature unknown; restored from __doc__
        """ state(self) -> QScroller.State """
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

    def target(self): # real signature unknown; restored from __doc__
        """ target(self) -> Optional[QObject] """
        pass

    def ungrabGesture(self, target, QObject=None): # real signature unknown; restored from __doc__
        """ ungrabGesture(target: Optional[QObject]) """
        pass

    def velocity(self): # real signature unknown; restored from __doc__
        """ velocity(self) -> QPointF """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    Dragging = 2
    Inactive = 0
    InputMove = 2
    InputPress = 1
    InputRelease = 3
    LeftMouseButtonGesture = 1
    MiddleMouseButtonGesture = 3
    Pressed = 1
    RightMouseButtonGesture = 2
    Scrolling = 3
    TouchGesture = 0


