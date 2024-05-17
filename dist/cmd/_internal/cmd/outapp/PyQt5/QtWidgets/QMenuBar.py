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

class QMenuBar(QWidget):
    """ QMenuBar(parent: Optional[QWidget] = None) """
    def actionAt(self, a0): # real signature unknown; restored from __doc__
        """ actionAt(self, a0: QPoint) -> Optional[QAction] """
        pass

    def actionEvent(self, a0, QActionEvent=None): # real signature unknown; restored from __doc__
        """ actionEvent(self, a0: Optional[QActionEvent]) """
        pass

    def actionGeometry(self, a0, QAction=None): # real signature unknown; restored from __doc__
        """ actionGeometry(self, a0: Optional[QAction]) -> QRect """
        pass

    def activeAction(self): # real signature unknown; restored from __doc__
        """ activeAction(self) -> Optional[QAction] """
        pass

    def addAction(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        addAction(self, action: Optional[QAction])
        addAction(self, text: Optional[str]) -> Optional[QAction]
        addAction(self, text: Optional[str], slot: PYQT_SLOT) -> Optional[QAction]
        """
        pass

    def addMenu(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        addMenu(self, menu: Optional[QMenu]) -> Optional[QAction]
        addMenu(self, title: Optional[str]) -> Optional[QMenu]
        addMenu(self, icon: QIcon, title: Optional[str]) -> Optional[QMenu]
        """
        pass

    def addSeparator(self): # real signature unknown; restored from __doc__
        """ addSeparator(self) -> Optional[QAction] """
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

    def contextMenuEvent(self, *args, **kwargs): # real signature unknown
        pass

    def cornerWidget(self, corner=None): # real signature unknown; restored from __doc__
        """ cornerWidget(self, corner: Qt.Corner = Qt.TopRightCorner) -> Optional[QWidget] """
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

    def event(self, a0, QEvent=None): # real signature unknown; restored from __doc__
        """ event(self, a0: Optional[QEvent]) -> bool """
        return False

    def eventFilter(self, a0, QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ eventFilter(self, a0: Optional[QObject], a1: Optional[QEvent]) -> bool """
        pass

    def focusInEvent(self, a0, QFocusEvent=None): # real signature unknown; restored from __doc__
        """ focusInEvent(self, a0: Optional[QFocusEvent]) """
        pass

    def focusNextChild(self, *args, **kwargs): # real signature unknown
        pass

    def focusNextPrevChild(self, *args, **kwargs): # real signature unknown
        pass

    def focusOutEvent(self, a0, QFocusEvent=None): # real signature unknown; restored from __doc__
        """ focusOutEvent(self, a0: Optional[QFocusEvent]) """
        pass

    def focusPreviousChild(self, *args, **kwargs): # real signature unknown
        pass

    def heightForWidth(self, a0): # real signature unknown; restored from __doc__
        """ heightForWidth(self, a0: int) -> int """
        return 0

    def hideEvent(self, *args, **kwargs): # real signature unknown
        pass

    def hovered(self, *args, **kwargs): # real signature unknown
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

    def initPainter(self, *args, **kwargs): # real signature unknown
        pass

    def initStyleOption(self, option, QStyleOptionMenuItem=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ initStyleOption(self, option: Optional[QStyleOptionMenuItem], action: Optional[QAction]) """
        pass

    def inputMethodEvent(self, *args, **kwargs): # real signature unknown
        pass

    def insertMenu(self, before, QAction=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ insertMenu(self, before: Optional[QAction], menu: Optional[QMenu]) -> Optional[QAction] """
        pass

    def insertSeparator(self, before, QAction=None): # real signature unknown; restored from __doc__
        """ insertSeparator(self, before: Optional[QAction]) -> Optional[QAction] """
        pass

    def isDefaultUp(self): # real signature unknown; restored from __doc__
        """ isDefaultUp(self) -> bool """
        return False

    def isNativeMenuBar(self): # real signature unknown; restored from __doc__
        """ isNativeMenuBar(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def keyPressEvent(self, a0, QKeyEvent=None): # real signature unknown; restored from __doc__
        """ keyPressEvent(self, a0: Optional[QKeyEvent]) """
        pass

    def keyReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def leaveEvent(self, a0, QEvent=None): # real signature unknown; restored from __doc__
        """ leaveEvent(self, a0: Optional[QEvent]) """
        pass

    def metric(self, *args, **kwargs): # real signature unknown
        pass

    def minimumSizeHint(self): # real signature unknown; restored from __doc__
        """ minimumSizeHint(self) -> QSize """
        pass

    def mouseDoubleClickEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mouseMoveEvent(self, a0, QMouseEvent=None): # real signature unknown; restored from __doc__
        """ mouseMoveEvent(self, a0: Optional[QMouseEvent]) """
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

    def paintEvent(self, a0, QPaintEvent=None): # real signature unknown; restored from __doc__
        """ paintEvent(self, a0: Optional[QPaintEvent]) """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def resizeEvent(self, a0, QResizeEvent=None): # real signature unknown; restored from __doc__
        """ resizeEvent(self, a0: Optional[QResizeEvent]) """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setActiveAction(self, action, QAction=None): # real signature unknown; restored from __doc__
        """ setActiveAction(self, action: Optional[QAction]) """
        pass

    def setCornerWidget(self, widget, QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setCornerWidget(self, widget: Optional[QWidget], corner: Qt.Corner = Qt.TopRightCorner) """
        pass

    def setDefaultUp(self, a0): # real signature unknown; restored from __doc__
        """ setDefaultUp(self, a0: bool) """
        pass

    def setNativeMenuBar(self, nativeMenuBar): # real signature unknown; restored from __doc__
        """ setNativeMenuBar(self, nativeMenuBar: bool) """
        pass

    def setVisible(self, visible): # real signature unknown; restored from __doc__
        """ setVisible(self, visible: bool) """
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

    def timerEvent(self, a0, QTimerEvent=None): # real signature unknown; restored from __doc__
        """ timerEvent(self, a0: Optional[QTimerEvent]) """
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


