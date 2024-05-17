# encoding: utf-8
# module PyQt5.QtMultimedia
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtMultimedia.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QAbstractVideoSurface(__PyQt5_QtCore.QObject):
    """ QAbstractVideoSurface(parent: Optional[QObject] = None) """
    def activeChanged(self, *args, **kwargs): # real signature unknown
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

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def error(self): # real signature unknown; restored from __doc__
        """ error(self) -> QAbstractVideoSurface.Error """
        pass

    def isActive(self): # real signature unknown; restored from __doc__
        """ isActive(self) -> bool """
        return False

    def isFormatSupported(self, format): # real signature unknown; restored from __doc__
        """ isFormatSupported(self, format: QVideoSurfaceFormat) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def nativeResolution(self): # real signature unknown; restored from __doc__
        """ nativeResolution(self) -> QSize """
        pass

    def nativeResolutionChanged(self, *args, **kwargs): # real signature unknown
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

    def nearestFormat(self, format): # real signature unknown; restored from __doc__
        """ nearestFormat(self, format: QVideoSurfaceFormat) -> QVideoSurfaceFormat """
        return QVideoSurfaceFormat

    def present(self, frame): # real signature unknown; restored from __doc__
        """ present(self, frame: QVideoFrame) -> bool """
        return False

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setError(self, error): # real signature unknown; restored from __doc__
        """ setError(self, error: QAbstractVideoSurface.Error) """
        pass

    def setNativeResolution(self, resolution): # real signature unknown; restored from __doc__
        """ setNativeResolution(self, resolution: QSize) """
        pass

    def start(self, format): # real signature unknown; restored from __doc__
        """ start(self, format: QVideoSurfaceFormat) -> bool """
        return False

    def stop(self): # real signature unknown; restored from __doc__
        """ stop(self) """
        pass

    def supportedFormatsChanged(self, *args, **kwargs): # real signature unknown
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

    def supportedPixelFormats(self, type=None): # real signature unknown; restored from __doc__
        """ supportedPixelFormats(self, type: QAbstractVideoBuffer.HandleType = QAbstractVideoBuffer.NoHandle) -> List[QVideoFrame.PixelFormat] """
        return []

    def surfaceFormat(self): # real signature unknown; restored from __doc__
        """ surfaceFormat(self) -> QVideoSurfaceFormat """
        return QVideoSurfaceFormat

    def surfaceFormatChanged(self, *args, **kwargs): # real signature unknown
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

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent, QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    IncorrectFormatError = 2
    NoError = 0
    ResourceError = 4
    StoppedError = 3
    UnsupportedFormatError = 1


