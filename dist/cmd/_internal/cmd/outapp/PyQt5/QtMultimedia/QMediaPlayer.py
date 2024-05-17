# encoding: utf-8
# module PyQt5.QtMultimedia
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtMultimedia.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


from .QMediaObject import QMediaObject

class QMediaPlayer(QMediaObject):
    """ QMediaPlayer(parent: Optional[QObject] = None, flags: Union[QMediaPlayer.Flags, QMediaPlayer.Flag] = QMediaPlayer.Flags()) """
    def addPropertyWatch(self, *args, **kwargs): # real signature unknown
        pass

    def audioAvailableChanged(self, *args, **kwargs): # real signature unknown
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

    def audioRole(self): # real signature unknown; restored from __doc__
        """ audioRole(self) -> QAudio.Role """
        pass

    def audioRoleChanged(self, *args, **kwargs): # real signature unknown
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

    def availability(self): # real signature unknown; restored from __doc__
        """ availability(self) -> QMultimedia.AvailabilityStatus """
        pass

    def bind(self, a0, QObject=None): # real signature unknown; restored from __doc__
        """ bind(self, a0: Optional[QObject]) -> bool """
        return False

    def bufferStatus(self): # real signature unknown; restored from __doc__
        """ bufferStatus(self) -> int """
        return 0

    def bufferStatusChanged(self, *args, **kwargs): # real signature unknown
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

    def currentMedia(self): # real signature unknown; restored from __doc__
        """ currentMedia(self) -> QMediaContent """
        return QMediaContent

    def currentMediaChanged(self, *args, **kwargs): # real signature unknown
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

    def currentNetworkConfiguration(self): # real signature unknown; restored from __doc__
        """ currentNetworkConfiguration(self) -> QNetworkConfiguration """
        pass

    def customAudioRole(self): # real signature unknown; restored from __doc__
        """ customAudioRole(self) -> str """
        return ""

    def customAudioRoleChanged(self, *args, **kwargs): # real signature unknown
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

    def hasSupport(self, mimeType, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ hasSupport(mimeType: Optional[str], codecs: Iterable[Optional[str]] = [], flags: Union[QMediaPlayer.Flags, QMediaPlayer.Flag] = QMediaPlayer.Flags()) -> QMultimedia.SupportEstimate """
        pass

    def isAudioAvailable(self): # real signature unknown; restored from __doc__
        """ isAudioAvailable(self) -> bool """
        return False

    def isMuted(self): # real signature unknown; restored from __doc__
        """ isMuted(self) -> bool """
        return False

    def isSeekable(self): # real signature unknown; restored from __doc__
        """ isSeekable(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def isVideoAvailable(self): # real signature unknown; restored from __doc__
        """ isVideoAvailable(self) -> bool """
        return False

    def media(self): # real signature unknown; restored from __doc__
        """ media(self) -> QMediaContent """
        return QMediaContent

    def mediaChanged(self, *args, **kwargs): # real signature unknown
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

    def mediaStatus(self): # real signature unknown; restored from __doc__
        """ mediaStatus(self) -> QMediaPlayer.MediaStatus """
        pass

    def mediaStatusChanged(self, *args, **kwargs): # real signature unknown
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

    def mediaStream(self): # real signature unknown; restored from __doc__
        """ mediaStream(self) -> Optional[QIODevice] """
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

    def networkConfigurationChanged(self, *args, **kwargs): # real signature unknown
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

    def pause(self): # real signature unknown; restored from __doc__
        """ pause(self) """
        pass

    def play(self): # real signature unknown; restored from __doc__
        """ play(self) """
        pass

    def playbackRate(self): # real signature unknown; restored from __doc__
        """ playbackRate(self) -> float """
        return 0.0

    def playbackRateChanged(self, *args, **kwargs): # real signature unknown
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

    def playlist(self): # real signature unknown; restored from __doc__
        """ playlist(self) -> Optional[QMediaPlaylist] """
        pass

    def position(self): # real signature unknown; restored from __doc__
        """ position(self) -> int """
        return 0

    def positionChanged(self, *args, **kwargs): # real signature unknown
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

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def removePropertyWatch(self, *args, **kwargs): # real signature unknown
        pass

    def seekableChanged(self, *args, **kwargs): # real signature unknown
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

    def setAudioRole(self, audioRole): # real signature unknown; restored from __doc__
        """ setAudioRole(self, audioRole: QAudio.Role) """
        pass

    def setCustomAudioRole(self, audioRole, p_str=None): # real signature unknown; restored from __doc__
        """ setCustomAudioRole(self, audioRole: Optional[str]) """
        pass

    def setMedia(self, media, stream, QIODevice=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setMedia(self, media: QMediaContent, stream: Optional[QIODevice] = None) """
        pass

    def setMuted(self, muted): # real signature unknown; restored from __doc__
        """ setMuted(self, muted: bool) """
        pass

    def setNetworkConfigurations(self, configurations, QNetworkConfiguration=None): # real signature unknown; restored from __doc__
        """ setNetworkConfigurations(self, configurations: Iterable[QNetworkConfiguration]) """
        pass

    def setPlaybackRate(self, rate): # real signature unknown; restored from __doc__
        """ setPlaybackRate(self, rate: float) """
        pass

    def setPlaylist(self, playlist, QMediaPlaylist=None): # real signature unknown; restored from __doc__
        """ setPlaylist(self, playlist: Optional[QMediaPlaylist]) """
        pass

    def setPosition(self, position): # real signature unknown; restored from __doc__
        """ setPosition(self, position: int) """
        pass

    def setVideoOutput(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setVideoOutput(self, a0: Optional[QVideoWidget])
        setVideoOutput(self, a0: Optional[QGraphicsVideoItem])
        setVideoOutput(self, surface: Optional[QAbstractVideoSurface])
        setVideoOutput(self, surfaces: Iterable[QAbstractVideoSurface])
        """
        pass

    def setVolume(self, volume): # real signature unknown; restored from __doc__
        """ setVolume(self, volume: int) """
        pass

    def state(self): # real signature unknown; restored from __doc__
        """ state(self) -> QMediaPlayer.State """
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

    def supportedAudioRoles(self): # real signature unknown; restored from __doc__
        """ supportedAudioRoles(self) -> List[QAudio.Role] """
        return []

    def supportedCustomAudioRoles(self): # real signature unknown; restored from __doc__
        """ supportedCustomAudioRoles(self) -> List[str] """
        return []

    def supportedMimeTypes(self, flags, QMediaPlayer_Flags=None, QMediaPlayer_Flag=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ supportedMimeTypes(flags: Union[QMediaPlayer.Flags, QMediaPlayer.Flag] = QMediaPlayer.Flags()) -> List[str] """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def unbind(self, a0, QObject=None): # real signature unknown; restored from __doc__
        """ unbind(self, a0: Optional[QObject]) """
        pass

    def videoAvailableChanged(self, *args, **kwargs): # real signature unknown
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

    def volume(self): # real signature unknown; restored from __doc__
        """ volume(self) -> int """
        return 0

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

    def __init__(self, parent, QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    AccessDeniedError = 4
    BufferedMedia = 6
    BufferingMedia = 5
    EndOfMedia = 7
    FormatError = 2
    InvalidMedia = 8
    LoadedMedia = 3
    LoadingMedia = 2
    LowLatency = 1
    NetworkError = 3
    NoError = 0
    NoMedia = 1
    PausedState = 2
    PlayingState = 1
    ResourceError = 1
    ServiceMissingError = 5
    StalledMedia = 4
    StoppedState = 0
    StreamPlayback = 2
    UnknownMediaStatus = 0
    VideoSurface = 4


