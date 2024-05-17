# encoding: utf-8
# module PyQt5.QtMultimedia
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtMultimedia.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


from .QMediaObject import QMediaObject

class QCamera(QMediaObject):
    """
    QCamera(parent: Optional[QObject] = None)
    QCamera(device: Union[QByteArray, bytes, bytearray], parent: Optional[QObject] = None)
    QCamera(cameraInfo: QCameraInfo, parent: Optional[QObject] = None)
    QCamera(position: QCamera.Position, parent: Optional[QObject] = None)
    """
    def addPropertyWatch(self, *args, **kwargs): # real signature unknown
        pass

    def availability(self): # real signature unknown; restored from __doc__
        """ availability(self) -> QMultimedia.AvailabilityStatus """
        pass

    def availableDevices(self): # real signature unknown; restored from __doc__
        """ availableDevices() -> List[QByteArray] """
        return []

    def captureMode(self): # real signature unknown; restored from __doc__
        """ captureMode(self) -> QCamera.CaptureModes """
        pass

    def captureModeChanged(self, *args, **kwargs): # real signature unknown
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

    def deviceDescription(self, device, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ deviceDescription(device: Union[QByteArray, bytes, bytearray]) -> str """
        return ""

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

    def errorOccurred(self, *args, **kwargs): # real signature unknown
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

    def exposure(self): # real signature unknown; restored from __doc__
        """ exposure(self) -> Optional[QCameraExposure] """
        pass

    def focus(self): # real signature unknown; restored from __doc__
        """ focus(self) -> Optional[QCameraFocus] """
        pass

    def imageProcessing(self): # real signature unknown; restored from __doc__
        """ imageProcessing(self) -> Optional[QCameraImageProcessing] """
        pass

    def isCaptureModeSupported(self, mode, QCamera_CaptureModes=None, QCamera_CaptureMode=None): # real signature unknown; restored from __doc__
        """ isCaptureModeSupported(self, mode: Union[QCamera.CaptureModes, QCamera.CaptureMode]) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def load(self): # real signature unknown; restored from __doc__
        """ load(self) """
        pass

    def locked(self, *args, **kwargs): # real signature unknown
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

    def lockFailed(self, *args, **kwargs): # real signature unknown
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

    def lockStatus(self, lock=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        lockStatus(self) -> QCamera.LockStatus
        lockStatus(self, lock: QCamera.LockType) -> QCamera.LockStatus
        """
        pass

    def lockStatusChanged(self, *args, **kwargs): # real signature unknown
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

    def requestedLocks(self): # real signature unknown; restored from __doc__
        """ requestedLocks(self) -> QCamera.LockTypes """
        pass

    def searchAndLock(self, locks=None, QCamera_LockTypes=None, QCamera_LockType=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        searchAndLock(self)
        searchAndLock(self, locks: Union[QCamera.LockTypes, QCamera.LockType])
        """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setCaptureMode(self, mode, QCamera_CaptureModes=None, QCamera_CaptureMode=None): # real signature unknown; restored from __doc__
        """ setCaptureMode(self, mode: Union[QCamera.CaptureModes, QCamera.CaptureMode]) """
        pass

    def setViewfinder(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setViewfinder(self, viewfinder: Optional[QVideoWidget])
        setViewfinder(self, viewfinder: Optional[QGraphicsVideoItem])
        setViewfinder(self, surface: Optional[QAbstractVideoSurface])
        """
        pass

    def setViewfinderSettings(self, settings): # real signature unknown; restored from __doc__
        """ setViewfinderSettings(self, settings: QCameraViewfinderSettings) """
        pass

    def start(self): # real signature unknown; restored from __doc__
        """ start(self) """
        pass

    def state(self): # real signature unknown; restored from __doc__
        """ state(self) -> QCamera.State """
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
        """ status(self) -> QCamera.Status """
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

    def supportedLocks(self): # real signature unknown; restored from __doc__
        """ supportedLocks(self) -> QCamera.LockTypes """
        pass

    def supportedViewfinderFrameRateRanges(self, settings=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ supportedViewfinderFrameRateRanges(self, settings: QCameraViewfinderSettings = QCameraViewfinderSettings()) -> List[QCamera.FrameRateRange] """
        pass

    def supportedViewfinderPixelFormats(self, settings=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ supportedViewfinderPixelFormats(self, settings: QCameraViewfinderSettings = QCameraViewfinderSettings()) -> List[QVideoFrame.PixelFormat] """
        pass

    def supportedViewfinderResolutions(self, settings=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ supportedViewfinderResolutions(self, settings: QCameraViewfinderSettings = QCameraViewfinderSettings()) -> List[QSize] """
        pass

    def supportedViewfinderSettings(self, settings=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ supportedViewfinderSettings(self, settings: QCameraViewfinderSettings = QCameraViewfinderSettings()) -> List[QCameraViewfinderSettings] """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def unload(self): # real signature unknown; restored from __doc__
        """ unload(self) """
        pass

    def unlock(self, locks=None, QCamera_LockTypes=None, QCamera_LockType=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        unlock(self)
        unlock(self, locks: Union[QCamera.LockTypes, QCamera.LockType])
        """
        pass

    def viewfinderSettings(self): # real signature unknown; restored from __doc__
        """ viewfinderSettings(self) -> QCameraViewfinderSettings """
        return QCameraViewfinderSettings

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    ActiveState = 2
    ActiveStatus = 8
    BackFace = 1
    CameraError = 1
    CaptureStillImage = 1
    CaptureVideo = 2
    CaptureViewfinder = 0
    FrontFace = 2
    InvalidRequestError = 2
    LoadedState = 1
    LoadedStatus = 4
    LoadingStatus = 2
    LockAcquired = 1
    Locked = 2
    LockExposure = 1
    LockFailed = 2
    LockFocus = 4
    LockLost = 3
    LockTemporaryLost = 4
    LockWhiteBalance = 2
    NoError = 0
    NoLock = 0
    NotSupportedFeatureError = 4
    Searching = 1
    ServiceMissingError = 3
    StandbyStatus = 5
    StartingStatus = 6
    StoppingStatus = 7
    UnavailableStatus = 0
    UnloadedState = 0
    UnloadedStatus = 1
    UnloadingStatus = 3
    Unlocked = 0
    UnspecifiedPosition = 0
    UserRequest = 0


