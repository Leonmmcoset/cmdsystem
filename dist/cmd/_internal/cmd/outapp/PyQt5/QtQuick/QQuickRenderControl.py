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


class QQuickRenderControl(__PyQt5_QtCore.QObject):
    """ QQuickRenderControl(parent: Optional[QObject] = None) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def grab(self): # real signature unknown; restored from __doc__
        """ grab(self) -> QImage """
        pass

    def initialize(self, gl, QOpenGLContext=None): # real signature unknown; restored from __doc__
        """ initialize(self, gl: Optional[QOpenGLContext]) """
        pass

    def invalidate(self): # real signature unknown; restored from __doc__
        """ invalidate(self) """
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def polishItems(self): # real signature unknown; restored from __doc__
        """ polishItems(self) """
        pass

    def prepareThread(self, targetThread, QThread=None): # real signature unknown; restored from __doc__
        """ prepareThread(self, targetThread: Optional[QThread]) """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def render(self): # real signature unknown; restored from __doc__
        """ render(self) """
        pass

    def renderRequested(self, *args, **kwargs): # real signature unknown
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

    def renderWindow(self, offset, QPoint=None): # real signature unknown; restored from __doc__
        """ renderWindow(self, offset: Optional[QPoint]) -> Optional[QWindow] """
        pass

    def renderWindowFor(self, win, QQuickWindow=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ renderWindowFor(win: Optional[QQuickWindow], offset: Optional[QPoint] = None) -> Optional[QWindow] """
        pass

    def sceneChanged(self, *args, **kwargs): # real signature unknown
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

    def sync(self): # real signature unknown; restored from __doc__
        """ sync(self) -> bool """
        return False

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent, QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass


