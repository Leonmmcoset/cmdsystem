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

class QMdiSubWindow(QWidget):
    """ QMdiSubWindow(parent: Optional[QWidget] = None, flags: Union[Qt.WindowFlags, Qt.WindowType] = Qt.WindowFlags()) """
    def aboutToActivate(self, *args, **kwargs): # real signature unknown
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

    def actionEvent(self, *args, **kwargs): # real signature unknown
        pass

    def changeEvent(self, changeEvent, QEvent=None): # real signature unknown; restored from __doc__
        """ changeEvent(self, changeEvent: Optional[QEvent]) """
        pass

    def childEvent(self, childEvent, QChildEvent=None): # real signature unknown; restored from __doc__
        """ childEvent(self, childEvent: Optional[QChildEvent]) """
        pass

    def closeEvent(self, closeEvent, QCloseEvent=None): # real signature unknown; restored from __doc__
        """ closeEvent(self, closeEvent: Optional[QCloseEvent]) """
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def contextMenuEvent(self, contextMenuEvent, QContextMenuEvent=None): # real signature unknown; restored from __doc__
        """ contextMenuEvent(self, contextMenuEvent: Optional[QContextMenuEvent]) """
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

    def event(self, event, QEvent=None): # real signature unknown; restored from __doc__
        """ event(self, event: Optional[QEvent]) -> bool """
        return False

    def eventFilter(self, p_object, QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ eventFilter(self, object: Optional[QObject], event: Optional[QEvent]) -> bool """
        pass

    def focusInEvent(self, focusInEvent, QFocusEvent=None): # real signature unknown; restored from __doc__
        """ focusInEvent(self, focusInEvent: Optional[QFocusEvent]) """
        pass

    def focusNextChild(self, *args, **kwargs): # real signature unknown
        pass

    def focusNextPrevChild(self, *args, **kwargs): # real signature unknown
        pass

    def focusOutEvent(self, focusOutEvent, QFocusEvent=None): # real signature unknown; restored from __doc__
        """ focusOutEvent(self, focusOutEvent: Optional[QFocusEvent]) """
        pass

    def focusPreviousChild(self, *args, **kwargs): # real signature unknown
        pass

    def hideEvent(self, hideEvent, QHideEvent=None): # real signature unknown; restored from __doc__
        """ hideEvent(self, hideEvent: Optional[QHideEvent]) """
        pass

    def initPainter(self, *args, **kwargs): # real signature unknown
        pass

    def inputMethodEvent(self, *args, **kwargs): # real signature unknown
        pass

    def isShaded(self): # real signature unknown; restored from __doc__
        """ isShaded(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def keyboardPageStep(self): # real signature unknown; restored from __doc__
        """ keyboardPageStep(self) -> int """
        return 0

    def keyboardSingleStep(self): # real signature unknown; restored from __doc__
        """ keyboardSingleStep(self) -> int """
        return 0

    def keyPressEvent(self, keyEvent, QKeyEvent=None): # real signature unknown; restored from __doc__
        """ keyPressEvent(self, keyEvent: Optional[QKeyEvent]) """
        pass

    def keyReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def leaveEvent(self, leaveEvent, QEvent=None): # real signature unknown; restored from __doc__
        """ leaveEvent(self, leaveEvent: Optional[QEvent]) """
        pass

    def mdiArea(self): # real signature unknown; restored from __doc__
        """ mdiArea(self) -> Optional[QMdiArea] """
        pass

    def metric(self, *args, **kwargs): # real signature unknown
        pass

    def minimumSizeHint(self): # real signature unknown; restored from __doc__
        """ minimumSizeHint(self) -> QSize """
        pass

    def mouseDoubleClickEvent(self, mouseEvent, QMouseEvent=None): # real signature unknown; restored from __doc__
        """ mouseDoubleClickEvent(self, mouseEvent: Optional[QMouseEvent]) """
        pass

    def mouseMoveEvent(self, mouseEvent, QMouseEvent=None): # real signature unknown; restored from __doc__
        """ mouseMoveEvent(self, mouseEvent: Optional[QMouseEvent]) """
        pass

    def mousePressEvent(self, mouseEvent, QMouseEvent=None): # real signature unknown; restored from __doc__
        """ mousePressEvent(self, mouseEvent: Optional[QMouseEvent]) """
        pass

    def mouseReleaseEvent(self, mouseEvent, QMouseEvent=None): # real signature unknown; restored from __doc__
        """ mouseReleaseEvent(self, mouseEvent: Optional[QMouseEvent]) """
        pass

    def moveEvent(self, moveEvent, QMoveEvent=None): # real signature unknown; restored from __doc__
        """ moveEvent(self, moveEvent: Optional[QMoveEvent]) """
        pass

    def nativeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def paintEvent(self, paintEvent, QPaintEvent=None): # real signature unknown; restored from __doc__
        """ paintEvent(self, paintEvent: Optional[QPaintEvent]) """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def resizeEvent(self, resizeEvent, QResizeEvent=None): # real signature unknown; restored from __doc__
        """ resizeEvent(self, resizeEvent: Optional[QResizeEvent]) """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setKeyboardPageStep(self, step): # real signature unknown; restored from __doc__
        """ setKeyboardPageStep(self, step: int) """
        pass

    def setKeyboardSingleStep(self, step): # real signature unknown; restored from __doc__
        """ setKeyboardSingleStep(self, step: int) """
        pass

    def setOption(self, option, on=True): # real signature unknown; restored from __doc__
        """ setOption(self, option: QMdiSubWindow.SubWindowOption, on: bool = True) """
        pass

    def setSystemMenu(self, systemMenu, QMenu=None): # real signature unknown; restored from __doc__
        """ setSystemMenu(self, systemMenu: Optional[QMenu]) """
        pass

    def setWidget(self, widget, QWidget=None): # real signature unknown; restored from __doc__
        """ setWidget(self, widget: Optional[QWidget]) """
        pass

    def sharedPainter(self, *args, **kwargs): # real signature unknown
        pass

    def showEvent(self, showEvent, QShowEvent=None): # real signature unknown; restored from __doc__
        """ showEvent(self, showEvent: Optional[QShowEvent]) """
        pass

    def showShaded(self): # real signature unknown; restored from __doc__
        """ showShaded(self) """
        pass

    def showSystemMenu(self): # real signature unknown; restored from __doc__
        """ showSystemMenu(self) """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> QSize """
        pass

    def systemMenu(self): # real signature unknown; restored from __doc__
        """ systemMenu(self) -> Optional[QMenu] """
        pass

    def tabletEvent(self, *args, **kwargs): # real signature unknown
        pass

    def testOption(self, a0): # real signature unknown; restored from __doc__
        """ testOption(self, a0: QMdiSubWindow.SubWindowOption) -> bool """
        return False

    def timerEvent(self, timerEvent, QTimerEvent=None): # real signature unknown; restored from __doc__
        """ timerEvent(self, timerEvent: Optional[QTimerEvent]) """
        pass

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

    def wheelEvent(self, *args, **kwargs): # real signature unknown
        pass

    def widget(self): # real signature unknown; restored from __doc__
        """ widget(self) -> Optional[QWidget] """
        pass

    def windowStateChanged(self, *args, **kwargs): # real signature unknown
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

    def __init__(self, parent, QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    RubberBandMove = 8
    RubberBandResize = 4


