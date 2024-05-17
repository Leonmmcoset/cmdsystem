# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


from .QSurface import QSurface

class QOffscreenSurface(__PyQt5_QtCore.QObject, QSurface):
    """
    QOffscreenSurface(screen: Optional[QScreen] = None)
    QOffscreenSurface(screen: Optional[QScreen], parent: Optional[QObject])
    """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def create(self): # real signature unknown; restored from __doc__
        """ create(self) """
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def destroy(self): # real signature unknown; restored from __doc__
        """ destroy(self) """
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def format(self): # real signature unknown; restored from __doc__
        """ format(self) -> QSurfaceFormat """
        return QSurfaceFormat

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def nativeHandle(self): # real signature unknown; restored from __doc__
        """ nativeHandle(self) -> Optional[PyQt5.sip.voidptr] """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def requestedFormat(self): # real signature unknown; restored from __doc__
        """ requestedFormat(self) -> QSurfaceFormat """
        return QSurfaceFormat

    def screen(self): # real signature unknown; restored from __doc__
        """ screen(self) -> Optional[QScreen] """
        pass

    def screenChanged(self, *args, **kwargs): # real signature unknown
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

    def setFormat(self, format): # real signature unknown; restored from __doc__
        """ setFormat(self, format: QSurfaceFormat) """
        pass

    def setNativeHandle(self, handle, PyQt5_sip_voidptr=None): # real signature unknown; restored from __doc__
        """ setNativeHandle(self, handle: Optional[PyQt5.sip.voidptr]) """
        pass

    def setScreen(self, screen, QScreen=None): # real signature unknown; restored from __doc__
        """ setScreen(self, screen: Optional[QScreen]) """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ size(self) -> QSize """
        pass

    def surfaceType(self): # real signature unknown; restored from __doc__
        """ surfaceType(self) -> QSurface.SurfaceType """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, screen, QScreen=None, *args, **kwargs): # real signature unknown; restored from __doc__ with multiple overloads
        pass


