# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


from .QPaintDeviceWindow import QPaintDeviceWindow

class QOpenGLWindow(QPaintDeviceWindow):
    """
    QOpenGLWindow(updateBehavior: QOpenGLWindow.UpdateBehavior = QOpenGLWindow.NoPartialUpdate, parent: Optional[QWindow] = None)
    QOpenGLWindow(shareContext: Optional[QOpenGLContext], updateBehavior: QOpenGLWindow.UpdateBehavior = QOpenGLWindow.NoPartialUpdate, parent: Optional[QWindow] = None)
    """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def context(self): # real signature unknown; restored from __doc__
        """ context(self) -> Optional[QOpenGLContext] """
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def defaultFramebufferObject(self): # real signature unknown; restored from __doc__
        """ defaultFramebufferObject(self) -> int """
        return 0

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def doneCurrent(self): # real signature unknown; restored from __doc__
        """ doneCurrent(self) """
        pass

    def event(self, *args, **kwargs): # real signature unknown
        pass

    def exposeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def focusInEvent(self, *args, **kwargs): # real signature unknown
        pass

    def focusOutEvent(self, *args, **kwargs): # real signature unknown
        pass

    def frameSwapped(self, *args, **kwargs): # real signature unknown
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

    def grabFramebuffer(self): # real signature unknown; restored from __doc__
        """ grabFramebuffer(self) -> QImage """
        return QImage

    def hideEvent(self, *args, **kwargs): # real signature unknown
        pass

    def initializeGL(self): # real signature unknown; restored from __doc__
        """ initializeGL(self) """
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def keyPressEvent(self, *args, **kwargs): # real signature unknown
        pass

    def keyReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def makeCurrent(self): # real signature unknown; restored from __doc__
        """ makeCurrent(self) """
        pass

    def metric(self, metric): # real signature unknown; restored from __doc__
        """ metric(self, metric: QPaintDevice.PaintDeviceMetric) -> int """
        return 0

    def mouseDoubleClickEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mouseMoveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mousePressEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mouseReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def moveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def paintEvent(self, event, QPaintEvent=None): # real signature unknown; restored from __doc__
        """ paintEvent(self, event: Optional[QPaintEvent]) """
        pass

    def paintGL(self): # real signature unknown; restored from __doc__
        """ paintGL(self) """
        pass

    def paintOverGL(self): # real signature unknown; restored from __doc__
        """ paintOverGL(self) """
        pass

    def paintUnderGL(self): # real signature unknown; restored from __doc__
        """ paintUnderGL(self) """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def resizeEvent(self, event, QResizeEvent=None): # real signature unknown; restored from __doc__
        """ resizeEvent(self, event: Optional[QResizeEvent]) """
        pass

    def resizeGL(self, w, h): # real signature unknown; restored from __doc__
        """ resizeGL(self, w: int, h: int) """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def shareContext(self): # real signature unknown; restored from __doc__
        """ shareContext(self) -> Optional[QOpenGLContext] """
        pass

    def showEvent(self, *args, **kwargs): # real signature unknown
        pass

    def tabletEvent(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def touchEvent(self, *args, **kwargs): # real signature unknown
        pass

    def updateBehavior(self): # real signature unknown; restored from __doc__
        """ updateBehavior(self) -> QOpenGLWindow.UpdateBehavior """
        pass

    def wheelEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    NoPartialUpdate = 0
    PartialUpdateBlend = 2
    PartialUpdateBlit = 1


