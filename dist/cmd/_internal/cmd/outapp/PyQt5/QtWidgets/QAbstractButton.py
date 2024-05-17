# encoding: utf-8
# module PyQt5.QtWidgets
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


from .QWidget import QWidget

class QAbstractButton(QWidget):
    """ QAbstractButton(parent: Optional[QWidget] = None) """
    def actionEvent(self, *args, **kwargs): # real signature unknown
        pass

    def animateClick(self, msecs=100): # real signature unknown; restored from __doc__
        """ animateClick(self, msecs: int = 100) """
        pass

    def autoExclusive(self): # real signature unknown; restored from __doc__
        """ autoExclusive(self) -> bool """
        return False

    def autoRepeat(self): # real signature unknown; restored from __doc__
        """ autoRepeat(self) -> bool """
        return False

    def autoRepeatDelay(self): # real signature unknown; restored from __doc__
        """ autoRepeatDelay(self) -> int """
        return 0

    def autoRepeatInterval(self): # real signature unknown; restored from __doc__
        """ autoRepeatInterval(self) -> int """
        return 0

    def changeEvent(self, e, QEvent=None): # real signature unknown; restored from __doc__
        """ changeEvent(self, e: Optional[QEvent]) """
        pass

    def checkStateSet(self): # real signature unknown; restored from __doc__
        """ checkStateSet(self) """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def click(self): # real signature unknown; restored from __doc__
        """ click(self) """
        pass

    def clicked(self, *args, **kwargs): # real signature unknown
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

    def enterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, e, QEvent=None): # real signature unknown; restored from __doc__
        """ event(self, e: Optional[QEvent]) -> bool """
        return False

    def focusInEvent(self, e, QFocusEvent=None): # real signature unknown; restored from __doc__
        """ focusInEvent(self, e: Optional[QFocusEvent]) """
        pass

    def focusNextChild(self, *args, **kwargs): # real signature unknown
        pass

    def focusNextPrevChild(self, *args, **kwargs): # real signature unknown
        pass

    def focusOutEvent(self, e, QFocusEvent=None): # real signature unknown; restored from __doc__
        """ focusOutEvent(self, e: Optional[QFocusEvent]) """
        pass

    def focusPreviousChild(self, *args, **kwargs): # real signature unknown
        pass

    def group(self): # real signature unknown; restored from __doc__
        """ group(self) -> Optional[QButtonGroup] """
        pass

    def hideEvent(self, *args, **kwargs): # real signature unknown
        pass

    def hitButton(self, pos): # real signature unknown; restored from __doc__
        """ hitButton(self, pos: QPoint) -> bool """
        return False

    def icon(self): # real signature unknown; restored from __doc__
        """ icon(self) -> QIcon """
        pass

    def iconSize(self): # real signature unknown; restored from __doc__
        """ iconSize(self) -> QSize """
        pass

    def initPainter(self, *args, **kwargs): # real signature unknown
        pass

    def inputMethodEvent(self, *args, **kwargs): # real signature unknown
        pass

    def isCheckable(self): # real signature unknown; restored from __doc__
        """ isCheckable(self) -> bool """
        return False

    def isChecked(self): # real signature unknown; restored from __doc__
        """ isChecked(self) -> bool """
        return False

    def isDown(self): # real signature unknown; restored from __doc__
        """ isDown(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def keyPressEvent(self, e, QKeyEvent=None): # real signature unknown; restored from __doc__
        """ keyPressEvent(self, e: Optional[QKeyEvent]) """
        pass

    def keyReleaseEvent(self, e, QKeyEvent=None): # real signature unknown; restored from __doc__
        """ keyReleaseEvent(self, e: Optional[QKeyEvent]) """
        pass

    def leaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def metric(self, *args, **kwargs): # real signature unknown
        pass

    def mouseDoubleClickEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mouseMoveEvent(self, e, QMouseEvent=None): # real signature unknown; restored from __doc__
        """ mouseMoveEvent(self, e: Optional[QMouseEvent]) """
        pass

    def mousePressEvent(self, e, QMouseEvent=None): # real signature unknown; restored from __doc__
        """ mousePressEvent(self, e: Optional[QMouseEvent]) """
        pass

    def mouseReleaseEvent(self, e, QMouseEvent=None): # real signature unknown; restored from __doc__
        """ mouseReleaseEvent(self, e: Optional[QMouseEvent]) """
        pass

    def moveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def nativeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def nextCheckState(self): # real signature unknown; restored from __doc__
        """ nextCheckState(self) """
        pass

    def paintEvent(self, e, QPaintEvent=None): # real signature unknown; restored from __doc__
        """ paintEvent(self, e: Optional[QPaintEvent]) """
        pass

    def pressed(self, *args, **kwargs): # real signature unknown
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

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def released(self, *args, **kwargs): # real signature unknown
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

    def resizeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setAutoExclusive(self, a0): # real signature unknown; restored from __doc__
        """ setAutoExclusive(self, a0: bool) """
        pass

    def setAutoRepeat(self, a0): # real signature unknown; restored from __doc__
        """ setAutoRepeat(self, a0: bool) """
        pass

    def setAutoRepeatDelay(self, a0): # real signature unknown; restored from __doc__
        """ setAutoRepeatDelay(self, a0: int) """
        pass

    def setAutoRepeatInterval(self, a0): # real signature unknown; restored from __doc__
        """ setAutoRepeatInterval(self, a0: int) """
        pass

    def setCheckable(self, a0): # real signature unknown; restored from __doc__
        """ setCheckable(self, a0: bool) """
        pass

    def setChecked(self, a0): # real signature unknown; restored from __doc__
        """ setChecked(self, a0: bool) """
        pass

    def setDown(self, a0): # real signature unknown; restored from __doc__
        """ setDown(self, a0: bool) """
        pass

    def setIcon(self, icon): # real signature unknown; restored from __doc__
        """ setIcon(self, icon: QIcon) """
        pass

    def setIconSize(self, size): # real signature unknown; restored from __doc__
        """ setIconSize(self, size: QSize) """
        pass

    def setShortcut(self, key, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setShortcut(self, key: Union[QKeySequence, QKeySequence.StandardKey, Optional[str], int]) """
        pass

    def setText(self, text, p_str=None): # real signature unknown; restored from __doc__
        """ setText(self, text: Optional[str]) """
        pass

    def sharedPainter(self, *args, **kwargs): # real signature unknown
        pass

    def shortcut(self): # real signature unknown; restored from __doc__
        """ shortcut(self) -> QKeySequence """
        pass

    def showEvent(self, *args, **kwargs): # real signature unknown
        pass

    def tabletEvent(self, *args, **kwargs): # real signature unknown
        pass

    def text(self): # real signature unknown; restored from __doc__
        """ text(self) -> str """
        return ""

    def timerEvent(self, e, QTimerEvent=None): # real signature unknown; restored from __doc__
        """ timerEvent(self, e: Optional[QTimerEvent]) """
        pass

    def toggle(self): # real signature unknown; restored from __doc__
        """ toggle(self) """
        pass

    def toggled(self, *args, **kwargs): # real signature unknown
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


