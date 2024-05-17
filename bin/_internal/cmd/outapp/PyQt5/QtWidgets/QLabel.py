# encoding: utf-8
# module PyQt5.QtWidgets
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


from .QFrame import QFrame

class QLabel(QFrame):
    """
    QLabel(parent: Optional[QWidget] = None, flags: Union[Qt.WindowFlags, Qt.WindowType] = Qt.WindowFlags())
    QLabel(text: Optional[str], parent: Optional[QWidget] = None, flags: Union[Qt.WindowFlags, Qt.WindowType] = Qt.WindowFlags())
    """
    def actionEvent(self, *args, **kwargs): # real signature unknown
        pass

    def alignment(self): # real signature unknown; restored from __doc__
        """ alignment(self) -> Qt.Alignment """
        pass

    def buddy(self): # real signature unknown; restored from __doc__
        """ buddy(self) -> Optional[QWidget] """
        pass

    def changeEvent(self, a0, QEvent=None): # real signature unknown; restored from __doc__
        """ changeEvent(self, a0: Optional[QEvent]) """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def closeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def contextMenuEvent(self, ev, QContextMenuEvent=None): # real signature unknown; restored from __doc__
        """ contextMenuEvent(self, ev: Optional[QContextMenuEvent]) """
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

    def drawFrame(self, *args, **kwargs): # real signature unknown
        pass

    def dropEvent(self, *args, **kwargs): # real signature unknown
        pass

    def enterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, e, QEvent=None): # real signature unknown; restored from __doc__
        """ event(self, e: Optional[QEvent]) -> bool """
        return False

    def focusInEvent(self, ev, QFocusEvent=None): # real signature unknown; restored from __doc__
        """ focusInEvent(self, ev: Optional[QFocusEvent]) """
        pass

    def focusNextChild(self, *args, **kwargs): # real signature unknown
        pass

    def focusNextPrevChild(self, next): # real signature unknown; restored from __doc__
        """ focusNextPrevChild(self, next: bool) -> bool """
        return False

    def focusOutEvent(self, ev, QFocusEvent=None): # real signature unknown; restored from __doc__
        """ focusOutEvent(self, ev: Optional[QFocusEvent]) """
        pass

    def focusPreviousChild(self, *args, **kwargs): # real signature unknown
        pass

    def hasScaledContents(self): # real signature unknown; restored from __doc__
        """ hasScaledContents(self) -> bool """
        return False

    def hasSelectedText(self): # real signature unknown; restored from __doc__
        """ hasSelectedText(self) -> bool """
        return False

    def heightForWidth(self, a0): # real signature unknown; restored from __doc__
        """ heightForWidth(self, a0: int) -> int """
        return 0

    def hideEvent(self, *args, **kwargs): # real signature unknown
        pass

    def indent(self): # real signature unknown; restored from __doc__
        """ indent(self) -> int """
        return 0

    def initPainter(self, *args, **kwargs): # real signature unknown
        pass

    def initStyleOption(self, *args, **kwargs): # real signature unknown
        pass

    def inputMethodEvent(self, *args, **kwargs): # real signature unknown
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def keyPressEvent(self, ev, QKeyEvent=None): # real signature unknown; restored from __doc__
        """ keyPressEvent(self, ev: Optional[QKeyEvent]) """
        pass

    def keyReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def leaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def linkActivated(self, *args, **kwargs): # real signature unknown
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

    def linkHovered(self, *args, **kwargs): # real signature unknown
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

    def margin(self): # real signature unknown; restored from __doc__
        """ margin(self) -> int """
        return 0

    def metric(self, *args, **kwargs): # real signature unknown
        pass

    def minimumSizeHint(self): # real signature unknown; restored from __doc__
        """ minimumSizeHint(self) -> QSize """
        pass

    def mouseDoubleClickEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mouseMoveEvent(self, ev, QMouseEvent=None): # real signature unknown; restored from __doc__
        """ mouseMoveEvent(self, ev: Optional[QMouseEvent]) """
        pass

    def mousePressEvent(self, ev, QMouseEvent=None): # real signature unknown; restored from __doc__
        """ mousePressEvent(self, ev: Optional[QMouseEvent]) """
        pass

    def mouseReleaseEvent(self, ev, QMouseEvent=None): # real signature unknown; restored from __doc__
        """ mouseReleaseEvent(self, ev: Optional[QMouseEvent]) """
        pass

    def moveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def movie(self): # real signature unknown; restored from __doc__
        """ movie(self) -> Optional[QMovie] """
        pass

    def nativeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def openExternalLinks(self): # real signature unknown; restored from __doc__
        """ openExternalLinks(self) -> bool """
        return False

    def paintEvent(self, a0, QPaintEvent=None): # real signature unknown; restored from __doc__
        """ paintEvent(self, a0: Optional[QPaintEvent]) """
        pass

    def picture(self): # real signature unknown; restored from __doc__
        """ picture(self) -> Optional[QPicture] """
        pass

    def pixmap(self): # real signature unknown; restored from __doc__
        """ pixmap(self) -> Optional[QPixmap] """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def resizeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def selectedText(self): # real signature unknown; restored from __doc__
        """ selectedText(self) -> str """
        return ""

    def selectionStart(self): # real signature unknown; restored from __doc__
        """ selectionStart(self) -> int """
        return 0

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setAlignment(self, a0, Qt_Alignment=None, Qt_AlignmentFlag=None): # real signature unknown; restored from __doc__
        """ setAlignment(self, a0: Union[Qt.Alignment, Qt.AlignmentFlag]) """
        pass

    def setBuddy(self, a0, QWidget=None): # real signature unknown; restored from __doc__
        """ setBuddy(self, a0: Optional[QWidget]) """
        pass

    def setIndent(self, a0): # real signature unknown; restored from __doc__
        """ setIndent(self, a0: int) """
        pass

    def setMargin(self, a0): # real signature unknown; restored from __doc__
        """ setMargin(self, a0: int) """
        pass

    def setMovie(self, movie, QMovie=None): # real signature unknown; restored from __doc__
        """ setMovie(self, movie: Optional[QMovie]) """
        pass

    def setNum(self, a0): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setNum(self, a0: float)
        setNum(self, a0: int)
        """
        pass

    def setOpenExternalLinks(self, open): # real signature unknown; restored from __doc__
        """ setOpenExternalLinks(self, open: bool) """
        pass

    def setPicture(self, a0): # real signature unknown; restored from __doc__
        """ setPicture(self, a0: QPicture) """
        pass

    def setPixmap(self, a0): # real signature unknown; restored from __doc__
        """ setPixmap(self, a0: QPixmap) """
        pass

    def setScaledContents(self, a0): # real signature unknown; restored from __doc__
        """ setScaledContents(self, a0: bool) """
        pass

    def setSelection(self, a0, a1): # real signature unknown; restored from __doc__
        """ setSelection(self, a0: int, a1: int) """
        pass

    def setText(self, a0, p_str=None): # real signature unknown; restored from __doc__
        """ setText(self, a0: Optional[str]) """
        pass

    def setTextFormat(self, a0): # real signature unknown; restored from __doc__
        """ setTextFormat(self, a0: Qt.TextFormat) """
        pass

    def setTextInteractionFlags(self, flags, Qt_TextInteractionFlags=None, Qt_TextInteractionFlag=None): # real signature unknown; restored from __doc__
        """ setTextInteractionFlags(self, flags: Union[Qt.TextInteractionFlags, Qt.TextInteractionFlag]) """
        pass

    def setWordWrap(self, on): # real signature unknown; restored from __doc__
        """ setWordWrap(self, on: bool) """
        pass

    def sharedPainter(self, *args, **kwargs): # real signature unknown
        pass

    def showEvent(self, *args, **kwargs): # real signature unknown
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> QSize """
        pass

    def tabletEvent(self, *args, **kwargs): # real signature unknown
        pass

    def text(self): # real signature unknown; restored from __doc__
        """ text(self) -> str """
        return ""

    def textFormat(self): # real signature unknown; restored from __doc__
        """ textFormat(self) -> Qt.TextFormat """
        pass

    def textInteractionFlags(self): # real signature unknown; restored from __doc__
        """ textInteractionFlags(self) -> Qt.TextInteractionFlags """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

    def wheelEvent(self, *args, **kwargs): # real signature unknown
        pass

    def wordWrap(self): # real signature unknown; restored from __doc__
        """ wordWrap(self) -> bool """
        return False

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


