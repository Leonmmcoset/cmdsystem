# encoding: utf-8
# module PyQt5.QtMultimedia
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtMultimedia.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QAudioOutput(__PyQt5_QtCore.QObject):
    """
    QAudioOutput(format: QAudioFormat = QAudioFormat(), parent: Optional[QObject] = None)
    QAudioOutput(audioDevice: QAudioDeviceInfo, format: QAudioFormat = QAudioFormat(), parent: Optional[QObject] = None)
    """
    def bufferSize(self): # real signature unknown; restored from __doc__
        """ bufferSize(self) -> int """
        return 0

    def bytesFree(self): # real signature unknown; restored from __doc__
        """ bytesFree(self) -> int """
        return 0

    def category(self): # real signature unknown; restored from __doc__
        """ category(self) -> str """
        return ""

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def elapsedUSecs(self): # real signature unknown; restored from __doc__
        """ elapsedUSecs(self) -> int """
        return 0

    def error(self): # real signature unknown; restored from __doc__
        """ error(self) -> QAudio.Error """
        pass

    def format(self): # real signature unknown; restored from __doc__
        """ format(self) -> QAudioFormat """
        return QAudioFormat

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def notify(self, *args, **kwargs): # real signature unknown
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

    def notifyInterval(self): # real signature unknown; restored from __doc__
        """ notifyInterval(self) -> int """
        return 0

    def periodSize(self): # real signature unknown; restored from __doc__
        """ periodSize(self) -> int """
        return 0

    def processedUSecs(self): # real signature unknown; restored from __doc__
        """ processedUSecs(self) -> int """
        return 0

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def reset(self): # real signature unknown; restored from __doc__
        """ reset(self) """
        pass

    def resume(self): # real signature unknown; restored from __doc__
        """ resume(self) """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setBufferSize(self, bytes): # real signature unknown; restored from __doc__
        """ setBufferSize(self, bytes: int) """
        pass

    def setCategory(self, category, p_str=None): # real signature unknown; restored from __doc__
        """ setCategory(self, category: Optional[str]) """
        pass

    def setNotifyInterval(self, milliSeconds): # real signature unknown; restored from __doc__
        """ setNotifyInterval(self, milliSeconds: int) """
        pass

    def setVolume(self, a0): # real signature unknown; restored from __doc__
        """ setVolume(self, a0: float) """
        pass

    def start(self, device=None, QIODevice=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        start(self, device: Optional[QIODevice])
        start(self) -> Optional[QIODevice]
        """
        pass

    def state(self): # real signature unknown; restored from __doc__
        """ state(self) -> QAudio.State """
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

    def suspend(self): # real signature unknown; restored from __doc__
        """ suspend(self) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def volume(self): # real signature unknown; restored from __doc__
        """ volume(self) -> float """
        return 0.0

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


