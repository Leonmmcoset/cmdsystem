# encoding: utf-8
# module PyQt5.QtQuick
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtQuick.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import PyQt5.QtQml as __PyQt5_QtQml
import sip as __sip


from .QQuickWindow import QQuickWindow

class QQuickView(QQuickWindow):
    """
    QQuickView(parent: Optional[QWindow] = None)
    QQuickView(engine: Optional[QQmlEngine], parent: Optional[QWindow])
    QQuickView(source: QUrl, parent: Optional[QWindow] = None)
    """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def engine(self): # real signature unknown; restored from __doc__
        """ engine(self) -> Optional[QQmlEngine] """
        pass

    def errors(self): # real signature unknown; restored from __doc__
        """ errors(self) -> List[QQmlError] """
        return []

    def event(self, *args, **kwargs): # real signature unknown
        pass

    def exposeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def focusInEvent(self, *args, **kwargs): # real signature unknown
        pass

    def focusOutEvent(self, *args, **kwargs): # real signature unknown
        pass

    def hideEvent(self, *args, **kwargs): # real signature unknown
        pass

    def initialSize(self): # real signature unknown; restored from __doc__
        """ initialSize(self) -> QSize """
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def keyPressEvent(self, a0, QKeyEvent=None): # real signature unknown; restored from __doc__
        """ keyPressEvent(self, a0: Optional[QKeyEvent]) """
        pass

    def keyReleaseEvent(self, a0, QKeyEvent=None): # real signature unknown; restored from __doc__
        """ keyReleaseEvent(self, a0: Optional[QKeyEvent]) """
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

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def resizeEvent(self, a0, QResizeEvent=None): # real signature unknown; restored from __doc__
        """ resizeEvent(self, a0: Optional[QResizeEvent]) """
        pass

    def resizeMode(self): # real signature unknown; restored from __doc__
        """ resizeMode(self) -> QQuickView.ResizeMode """
        pass

    def rootContext(self): # real signature unknown; restored from __doc__
        """ rootContext(self) -> Optional[QQmlContext] """
        pass

    def rootObject(self): # real signature unknown; restored from __doc__
        """ rootObject(self) -> Optional[QQuickItem] """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setInitialProperties(self, initialProperties, p_str=None, Any=None): # real signature unknown; restored from __doc__
        """ setInitialProperties(self, initialProperties: Dict[str, Any]) """
        pass

    def setResizeMode(self, a0): # real signature unknown; restored from __doc__
        """ setResizeMode(self, a0: QQuickView.ResizeMode) """
        pass

    def setSource(self, a0): # real signature unknown; restored from __doc__
        """ setSource(self, a0: QUrl) """
        pass

    def showEvent(self, *args, **kwargs): # real signature unknown
        pass

    def source(self): # real signature unknown; restored from __doc__
        """ source(self) -> QUrl """
        pass

    def status(self): # real signature unknown; restored from __doc__
        """ status(self) -> QQuickView.Status """
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

    def touchEvent(self, *args, **kwargs): # real signature unknown
        pass

    def wheelEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    Error = 3
    Loading = 2
    Null = 0
    Ready = 1
    SizeRootObjectToView = 1
    SizeViewToRootObject = 0


