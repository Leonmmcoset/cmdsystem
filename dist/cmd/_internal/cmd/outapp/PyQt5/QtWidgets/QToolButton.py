# encoding: utf-8
# module PyQt5.QtWidgets
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


from .QAbstractButton import QAbstractButton

class QToolButton(QAbstractButton):
    """ QToolButton(parent: Optional[QWidget] = None) """
    def actionEvent(self, a0, QActionEvent=None): # real signature unknown; restored from __doc__
        """ actionEvent(self, a0: Optional[QActionEvent]) """
        pass

    def arrowType(self): # real signature unknown; restored from __doc__
        """ arrowType(self) -> Qt.ArrowType """
        pass

    def autoRaise(self): # real signature unknown; restored from __doc__
        """ autoRaise(self) -> bool """
        return False

    def changeEvent(self, a0, QEvent=None): # real signature unknown; restored from __doc__
        """ changeEvent(self, a0: Optional[QEvent]) """
        pass

    def checkStateSet(self, *args, **kwargs): # real signature unknown
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def closeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def contextMenuEvent(self, *args, **kwargs): # real signature unknown
        pass

    def create(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def defaultAction(self): # real signature unknown; restored from __doc__
        """ defaultAction(self) -> Optional[QAction] """
        pass

    def destroy(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def dragEnterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dragLeaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dragMoveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dropEvent(self, *args, **kwargs): # real signature unknown
        pass

    def enterEvent(self, a0, QEvent=None): # real signature unknown; restored from __doc__
        """ enterEvent(self, a0: Optional[QEvent]) """
        pass

    def event(self, e, QEvent=None): # real signature unknown; restored from __doc__
        """ event(self, e: Optional[QEvent]) -> bool """
        return False

    def focusInEvent(self, *args, **kwargs): # real signature unknown
        pass

    def focusNextChild(self, *args, **kwargs): # real signature unknown
        pass

    def focusNextPrevChild(self, *args, **kwargs): # real signature unknown
        pass

    def focusOutEvent(self, *args, **kwargs): # real signature unknown
        pass

    def focusPreviousChild(self, *args, **kwargs): # real signature unknown
        pass

    def hideEvent(self, *args, **kwargs): # real signature unknown
        pass

    def hitButton(self, pos): # real signature unknown; restored from __doc__
        """ hitButton(self, pos: QPoint) -> bool """
        return False

    def initPainter(self, *args, **kwargs): # real signature unknown
        pass

    def initStyleOption(self, option, QStyleOptionToolButton=None): # real signature unknown; restored from __doc__
        """ initStyleOption(self, option: Optional[QStyleOptionToolButton]) """
        pass

    def inputMethodEvent(self, *args, **kwargs): # real signature unknown
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def keyPressEvent(self, *args, **kwargs): # real signature unknown
        pass

    def keyReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def leaveEvent(self, a0, QEvent=None): # real signature unknown; restored from __doc__
        """ leaveEvent(self, a0: Optional[QEvent]) """
        pass

    def menu(self): # real signature unknown; restored from __doc__
        """ menu(self) -> Optional[QMenu] """
        pass

    def metric(self, *args, **kwargs): # real signature unknown
        pass

    def minimumSizeHint(self): # real signature unknown; restored from __doc__
        """ minimumSizeHint(self) -> QSize """
        pass

    def mouseDoubleClickEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mouseMoveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mousePressEvent(self, a0, QMouseEvent=None): # real signature unknown; restored from __doc__
        """ mousePressEvent(self, a0: Optional[QMouseEvent]) """
        pass

    def mouseReleaseEvent(self, a0, QMouseEvent=None): # real signature unknown; restored from __doc__
        """ mouseReleaseEvent(self, a0: Optional[QMouseEvent]) """
        pass

    def moveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def nativeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def nextCheckState(self): # real signature unknown; restored from __doc__
        """ nextCheckState(self) """
        pass

    def paintEvent(self, a0, QPaintEvent=None): # real signature unknown; restored from __doc__
        """ paintEvent(self, a0: Optional[QPaintEvent]) """
        pass

    def popupMode(self): # real signature unknown; restored from __doc__
        """ popupMode(self) -> QToolButton.ToolButtonPopupMode """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def resizeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setArrowType(self, type): # real signature unknown; restored from __doc__
        """ setArrowType(self, type: Qt.ArrowType) """
        pass

    def setAutoRaise(self, enable): # real signature unknown; restored from __doc__
        """ setAutoRaise(self, enable: bool) """
        pass

    def setDefaultAction(self, a0, QAction=None): # real signature unknown; restored from __doc__
        """ setDefaultAction(self, a0: Optional[QAction]) """
        pass

    def setMenu(self, menu, QMenu=None): # real signature unknown; restored from __doc__
        """ setMenu(self, menu: Optional[QMenu]) """
        pass

    def setPopupMode(self, mode): # real signature unknown; restored from __doc__
        """ setPopupMode(self, mode: QToolButton.ToolButtonPopupMode) """
        pass

    def setToolButtonStyle(self, style): # real signature unknown; restored from __doc__
        """ setToolButtonStyle(self, style: Qt.ToolButtonStyle) """
        pass

    def sharedPainter(self, *args, **kwargs): # real signature unknown
        pass

    def showEvent(self, *args, **kwargs): # real signature unknown
        pass

    def showMenu(self): # real signature unknown; restored from __doc__
        """ showMenu(self) """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> QSize """
        pass

    def tabletEvent(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, a0, QTimerEvent=None): # real signature unknown; restored from __doc__
        """ timerEvent(self, a0: Optional[QTimerEvent]) """
        pass

    def toolButtonStyle(self): # real signature unknown; restored from __doc__
        """ toolButtonStyle(self) -> Qt.ToolButtonStyle """
        pass

    def triggered(self, *args, **kwargs): # real signature unknown
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

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

    def wheelEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent, QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    DelayedPopup = 0
    InstantPopup = 2
    MenuButtonPopup = 1


