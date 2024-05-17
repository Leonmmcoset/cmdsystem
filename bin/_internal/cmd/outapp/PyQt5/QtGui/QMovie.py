# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QMovie(__PyQt5_QtCore.QObject):
    """
    QMovie(parent: Optional[QObject] = None)
    QMovie(device: Optional[QIODevice], format: Union[QByteArray, bytes, bytearray] = QByteArray(), parent: Optional[QObject] = None)
    QMovie(fileName: Optional[str], format: Union[QByteArray, bytes, bytearray] = QByteArray(), parent: Optional[QObject] = None)
    """
    def backgroundColor(self): # real signature unknown; restored from __doc__
        """ backgroundColor(self) -> QColor """
        return QColor

    def cacheMode(self): # real signature unknown; restored from __doc__
        """ cacheMode(self) -> QMovie.CacheMode """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def currentFrameNumber(self): # real signature unknown; restored from __doc__
        """ currentFrameNumber(self) -> int """
        return 0

    def currentImage(self): # real signature unknown; restored from __doc__
        """ currentImage(self) -> QImage """
        return QImage

    def currentPixmap(self): # real signature unknown; restored from __doc__
        """ currentPixmap(self) -> QPixmap """
        return QPixmap

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def device(self): # real signature unknown; restored from __doc__
        """ device(self) -> Optional[QIODevice] """
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def error(self, *args, **kwargs): # real signature unknown
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

    def fileName(self): # real signature unknown; restored from __doc__
        """ fileName(self) -> str """
        return ""

    def finished(self, *args, **kwargs): # real signature unknown
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

    def format(self): # real signature unknown; restored from __doc__
        """ format(self) -> QByteArray """
        pass

    def frameChanged(self, *args, **kwargs): # real signature unknown
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

    def frameCount(self): # real signature unknown; restored from __doc__
        """ frameCount(self) -> int """
        return 0

    def frameRect(self): # real signature unknown; restored from __doc__
        """ frameRect(self) -> QRect """
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def jumpToFrame(self, frameNumber): # real signature unknown; restored from __doc__
        """ jumpToFrame(self, frameNumber: int) -> bool """
        return False

    def jumpToNextFrame(self): # real signature unknown; restored from __doc__
        """ jumpToNextFrame(self) -> bool """
        return False

    def lastError(self): # real signature unknown; restored from __doc__
        """ lastError(self) -> QImageReader.ImageReaderError """
        pass

    def lastErrorString(self): # real signature unknown; restored from __doc__
        """ lastErrorString(self) -> str """
        return ""

    def loopCount(self): # real signature unknown; restored from __doc__
        """ loopCount(self) -> int """
        return 0

    def nextFrameDelay(self): # real signature unknown; restored from __doc__
        """ nextFrameDelay(self) -> int """
        return 0

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def resized(self, *args, **kwargs): # real signature unknown
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

    def scaledSize(self): # real signature unknown; restored from __doc__
        """ scaledSize(self) -> QSize """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setBackgroundColor(self, color, QColor=None, Qt_GlobalColor=None): # real signature unknown; restored from __doc__
        """ setBackgroundColor(self, color: Union[QColor, Qt.GlobalColor]) """
        pass

    def setCacheMode(self, mode): # real signature unknown; restored from __doc__
        """ setCacheMode(self, mode: QMovie.CacheMode) """
        pass

    def setDevice(self, device, QIODevice=None): # real signature unknown; restored from __doc__
        """ setDevice(self, device: Optional[QIODevice]) """
        pass

    def setFileName(self, fileName, p_str=None): # real signature unknown; restored from __doc__
        """ setFileName(self, fileName: Optional[str]) """
        pass

    def setFormat(self, format, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ setFormat(self, format: Union[QByteArray, bytes, bytearray]) """
        pass

    def setPaused(self, paused): # real signature unknown; restored from __doc__
        """ setPaused(self, paused: bool) """
        pass

    def setScaledSize(self, size): # real signature unknown; restored from __doc__
        """ setScaledSize(self, size: QSize) """
        pass

    def setSpeed(self, percentSpeed): # real signature unknown; restored from __doc__
        """ setSpeed(self, percentSpeed: int) """
        pass

    def speed(self): # real signature unknown; restored from __doc__
        """ speed(self) -> int """
        return 0

    def start(self): # real signature unknown; restored from __doc__
        """ start(self) """
        pass

    def started(self, *args, **kwargs): # real signature unknown
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

    def state(self): # real signature unknown; restored from __doc__
        """ state(self) -> QMovie.MovieState """
        pass

    def stateChanged(self, *args, **kwargs): # real signature unknown
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

    def stop(self): # real signature unknown; restored from __doc__
        """ stop(self) """
        pass

    def supportedFormats(self): # real signature unknown; restored from __doc__
        """ supportedFormats() -> List[QByteArray] """
        return []

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def updated(self, *args, **kwargs): # real signature unknown
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

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    CacheAll = 1
    CacheNone = 0
    NotRunning = 0
    Paused = 1
    Running = 2


