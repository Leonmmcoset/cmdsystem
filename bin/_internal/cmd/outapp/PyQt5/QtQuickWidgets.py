# encoding: utf-8
# module PyQt5.QtQuickWidgets
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtQuickWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtWidgets as __PyQt5_QtWidgets


# no functions
# classes

class QQuickWidget(__PyQt5_QtWidgets.QWidget):
    """
    QQuickWidget(parent: Optional[QWidget] = None)
    QQuickWidget(engine: Optional[QQmlEngine], parent: Optional[QWidget])
    QQuickWidget(source: QUrl, parent: Optional[QWidget] = None)
    """
    def actionEvent(self, *args, **kwargs): # real signature unknown
        pass

    def changeEvent(self, *args, **kwargs): # real signature unknown
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

    def destroy(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def dragEnterEvent(self, a0, QDragEnterEvent=None): # real signature unknown; restored from __doc__
        """ dragEnterEvent(self, a0: Optional[QDragEnterEvent]) """
        pass

    def dragLeaveEvent(self, a0, QDragLeaveEvent=None): # real signature unknown; restored from __doc__
        """ dragLeaveEvent(self, a0: Optional[QDragLeaveEvent]) """
        pass

    def dragMoveEvent(self, a0, QDragMoveEvent=None): # real signature unknown; restored from __doc__
        """ dragMoveEvent(self, a0: Optional[QDragMoveEvent]) """
        pass

    def dropEvent(self, a0, QDropEvent=None): # real signature unknown; restored from __doc__
        """ dropEvent(self, a0: Optional[QDropEvent]) """
        pass

    def engine(self): # real signature unknown; restored from __doc__
        """ engine(self) -> Optional[QQmlEngine] """
        pass

    def enterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def errors(self): # real signature unknown; restored from __doc__
        """ errors(self) -> List[QQmlError] """
        return []

    def event(self, a0, QEvent=None): # real signature unknown; restored from __doc__
        """ event(self, a0: Optional[QEvent]) -> bool """
        return False

    def focusInEvent(self, event, QFocusEvent=None): # real signature unknown; restored from __doc__
        """ focusInEvent(self, event: Optional[QFocusEvent]) """
        pass

    def focusNextChild(self, *args, **kwargs): # real signature unknown
        pass

    def focusNextPrevChild(self, next): # real signature unknown; restored from __doc__
        """ focusNextPrevChild(self, next: bool) -> bool """
        return False

    def focusOutEvent(self, event, QFocusEvent=None): # real signature unknown; restored from __doc__
        """ focusOutEvent(self, event: Optional[QFocusEvent]) """
        pass

    def focusPreviousChild(self, *args, **kwargs): # real signature unknown
        pass

    def format(self): # real signature unknown; restored from __doc__
        """ format(self) -> QSurfaceFormat """
        pass

    def grabFramebuffer(self): # real signature unknown; restored from __doc__
        """ grabFramebuffer(self) -> QImage """
        pass

    def hideEvent(self, a0, QHideEvent=None): # real signature unknown; restored from __doc__
        """ hideEvent(self, a0: Optional[QHideEvent]) """
        pass

    def initialSize(self): # real signature unknown; restored from __doc__
        """ initialSize(self) -> QSize """
        pass

    def initPainter(self, *args, **kwargs): # real signature unknown
        pass

    def inputMethodEvent(self, *args, **kwargs): # real signature unknown
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def keyPressEvent(self, a0, QKeyEvent=None): # real signature unknown; restored from __doc__
        """ keyPressEvent(self, a0: Optional[QKeyEvent]) """
        pass

    def keyReleaseEvent(self, a0, QKeyEvent=None): # real signature unknown; restored from __doc__
        """ keyReleaseEvent(self, a0: Optional[QKeyEvent]) """
        pass

    def leaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def metric(self, *args, **kwargs): # real signature unknown
        pass

    def mouseDoubleClickEvent(self, a0, QMouseEvent=None): # real signature unknown; restored from __doc__
        """ mouseDoubleClickEvent(self, a0: Optional[QMouseEvent]) """
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

    def paintEvent(self, event, QPaintEvent=None): # real signature unknown; restored from __doc__
        """ paintEvent(self, event: Optional[QPaintEvent]) """
        pass

    def quickWindow(self): # real signature unknown; restored from __doc__
        """ quickWindow(self) -> Optional[QQuickWindow] """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def resizeEvent(self, a0, QResizeEvent=None): # real signature unknown; restored from __doc__
        """ resizeEvent(self, a0: Optional[QResizeEvent]) """
        pass

    def resizeMode(self): # real signature unknown; restored from __doc__
        """ resizeMode(self) -> QQuickWidget.ResizeMode """
        pass

    def rootContext(self): # real signature unknown; restored from __doc__
        """ rootContext(self) -> Optional[QQmlContext] """
        pass

    def rootObject(self): # real signature unknown; restored from __doc__
        """ rootObject(self) -> Optional[QQuickItem] """
        pass

    def sceneGraphError(self, *args, **kwargs): # real signature unknown
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

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setClearColor(self, color, QColor=None, Qt_GlobalColor=None): # real signature unknown; restored from __doc__
        """ setClearColor(self, color: Union[QColor, Qt.GlobalColor]) """
        pass

    def setFormat(self, format): # real signature unknown; restored from __doc__
        """ setFormat(self, format: QSurfaceFormat) """
        pass

    def setResizeMode(self, a0): # real signature unknown; restored from __doc__
        """ setResizeMode(self, a0: QQuickWidget.ResizeMode) """
        pass

    def setSource(self, a0): # real signature unknown; restored from __doc__
        """ setSource(self, a0: QUrl) """
        pass

    def sharedPainter(self, *args, **kwargs): # real signature unknown
        pass

    def showEvent(self, a0, QShowEvent=None): # real signature unknown; restored from __doc__
        """ showEvent(self, a0: Optional[QShowEvent]) """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> QSize """
        pass

    def source(self): # real signature unknown; restored from __doc__
        """ source(self) -> QUrl """
        pass

    def status(self): # real signature unknown; restored from __doc__
        """ status(self) -> QQuickWidget.Status """
        pass

    def statusChanged(self, *args, **kwargs): # real signature unknown
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

    def tabletEvent(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, a0, QTimerEvent=None): # real signature unknown; restored from __doc__
        """ timerEvent(self, a0: Optional[QTimerEvent]) """
        pass

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

    def wheelEvent(self, a0, QWheelEvent=None): # real signature unknown; restored from __doc__
        """ wheelEvent(self, a0: Optional[QWheelEvent]) """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    Error = 3
    Loading = 2
    Null = 0
    Ready = 1
    SizeRootObjectToView = 1
    SizeViewToRootObject = 0


# variables with complex values



