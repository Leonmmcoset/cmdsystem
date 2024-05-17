# encoding: utf-8
# module PyQt5.QtMultimedia
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtMultimedia.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


from .QMediaBindableInterface import QMediaBindableInterface

class QMediaRecorder(__PyQt5_QtCore.QObject, QMediaBindableInterface):
    """ QMediaRecorder(mediaObject: Optional[QMediaObject], parent: Optional[QObject] = None) """
    def actualLocation(self): # real signature unknown; restored from __doc__
        """ actualLocation(self) -> QUrl """
        pass

    def actualLocationChanged(self, *args, **kwargs): # real signature unknown
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

    def audioCodecDescription(self, codecName, p_str=None): # real signature unknown; restored from __doc__
        """ audioCodecDescription(self, codecName: Optional[str]) -> str """
        return ""

    def audioSettings(self): # real signature unknown; restored from __doc__
        """ audioSettings(self) -> QAudioEncoderSettings """
        return QAudioEncoderSettings

    def availability(self): # real signature unknown; restored from __doc__
        """ availability(self) -> QMultimedia.AvailabilityStatus """
        pass

    def availabilityChanged(self, *args, **kwargs): # real signature unknown
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

    def availableMetaData(self): # real signature unknown; restored from __doc__
        """ availableMetaData(self) -> List[str] """
        return []

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def containerDescription(self, format, p_str=None): # real signature unknown; restored from __doc__
        """ containerDescription(self, format: Optional[str]) -> str """
        return ""

    def containerFormat(self): # real signature unknown; restored from __doc__
        """ containerFormat(self) -> str """
        return ""

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def duration(self): # real signature unknown; restored from __doc__
        """ duration(self) -> int """
        return 0

    def durationChanged(self, *args, **kwargs): # real signature unknown
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

    def errorString(self): # real signature unknown; restored from __doc__
        """ errorString(self) -> str """
        return ""

    def isAvailable(self): # real signature unknown; restored from __doc__
        """ isAvailable(self) -> bool """
        return False

    def isMetaDataAvailable(self): # real signature unknown; restored from __doc__
        """ isMetaDataAvailable(self) -> bool """
        return False

    def isMetaDataWritable(self): # real signature unknown; restored from __doc__
        """ isMetaDataWritable(self) -> bool """
        return False

    def isMuted(self): # real signature unknown; restored from __doc__
        """ isMuted(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def mediaObject(self): # real signature unknown; restored from __doc__
        """ mediaObject(self) -> Optional[QMediaObject] """
        pass

    def metaData(self, key, p_str=None): # real signature unknown; restored from __doc__
        """ metaData(self, key: Optional[str]) -> Any """
        pass

    def metaDataAvailableChanged(self, *args, **kwargs): # real signature unknown
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

    def metaDataChanged(self, *args, **kwargs): # real signature unknown
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

    def metaDataWritableChanged(self, *args, **kwargs): # real signature unknown
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

    def mutedChanged(self, *args, **kwargs): # real signature unknown
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

    def outputLocation(self): # real signature unknown; restored from __doc__
        """ outputLocation(self) -> QUrl """
        pass

    def pause(self): # real signature unknown; restored from __doc__
        """ pause(self) """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def record(self): # real signature unknown; restored from __doc__
        """ record(self) """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setAudioSettings(self, audioSettings): # real signature unknown; restored from __doc__
        """ setAudioSettings(self, audioSettings: QAudioEncoderSettings) """
        pass

    def setContainerFormat(self, container, p_str=None): # real signature unknown; restored from __doc__
        """ setContainerFormat(self, container: Optional[str]) """
        pass

    def setEncodingSettings(self, audio, video=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setEncodingSettings(self, audio: QAudioEncoderSettings, video: QVideoEncoderSettings = QVideoEncoderSettings(), container: Optional[str] = '') """
        pass

    def setMediaObject(self, p_object, QMediaObject=None): # real signature unknown; restored from __doc__
        """ setMediaObject(self, object: Optional[QMediaObject]) -> bool """
        return False

    def setMetaData(self, key, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setMetaData(self, key: Optional[str], value: Any) """
        pass

    def setMuted(self, muted): # real signature unknown; restored from __doc__
        """ setMuted(self, muted: bool) """
        pass

    def setOutputLocation(self, location): # real signature unknown; restored from __doc__
        """ setOutputLocation(self, location: QUrl) -> bool """
        return False

    def setVideoSettings(self, videoSettings): # real signature unknown; restored from __doc__
        """ setVideoSettings(self, videoSettings: QVideoEncoderSettings) """
        pass

    def setVolume(self, volume): # real signature unknown; restored from __doc__
        """ setVolume(self, volume: float) """
        pass

    def state(self): # real signature unknown; restored from __doc__
        """ state(self) -> QMediaRecorder.State """
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

    def status(self): # real signature unknown; restored from __doc__
        """ status(self) -> QMediaRecorder.Status """
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

    def stop(self): # real signature unknown; restored from __doc__
        """ stop(self) """
        pass

    def supportedAudioCodecs(self): # real signature unknown; restored from __doc__
        """ supportedAudioCodecs(self) -> List[str] """
        return []

    def supportedAudioSampleRates(self, settings=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ supportedAudioSampleRates(self, settings: QAudioEncoderSettings = QAudioEncoderSettings()) -> (List[int], Optional[bool]) """
        pass

    def supportedContainers(self): # real signature unknown; restored from __doc__
        """ supportedContainers(self) -> List[str] """
        return []

    def supportedFrameRates(self, settings=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ supportedFrameRates(self, settings: QVideoEncoderSettings = QVideoEncoderSettings()) -> (List[float], Optional[bool]) """
        pass

    def supportedResolutions(self, settings=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ supportedResolutions(self, settings: QVideoEncoderSettings = QVideoEncoderSettings()) -> (List[QSize], Optional[bool]) """
        pass

    def supportedVideoCodecs(self): # real signature unknown; restored from __doc__
        """ supportedVideoCodecs(self) -> List[str] """
        return []

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def videoCodecDescription(self, codecName, p_str=None): # real signature unknown; restored from __doc__
        """ videoCodecDescription(self, codecName: Optional[str]) -> str """
        return ""

    def videoSettings(self): # real signature unknown; restored from __doc__
        """ videoSettings(self) -> QVideoEncoderSettings """
        return QVideoEncoderSettings

    def volume(self): # real signature unknown; restored from __doc__
        """ volume(self) -> float """
        return 0.0

    def volumeChanged(self, *args, **kwargs): # real signature unknown
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

    def __init__(self, mediaObject, QMediaObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    FinalizingStatus = 7
    FormatError = 2
    LoadedStatus = 3
    LoadingStatus = 2
    NoError = 0
    OutOfSpaceError = 3
    PausedState = 2
    PausedStatus = 6
    RecordingState = 1
    RecordingStatus = 5
    ResourceError = 1
    StartingStatus = 4
    StoppedState = 0
    UnavailableStatus = 0
    UnloadedStatus = 1


