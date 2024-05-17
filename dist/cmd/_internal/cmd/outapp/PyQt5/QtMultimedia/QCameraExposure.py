# encoding: utf-8
# module PyQt5.QtMultimedia
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtMultimedia.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QCameraExposure(__PyQt5_QtCore.QObject):
    # no doc
    def aperture(self): # real signature unknown; restored from __doc__
        """ aperture(self) -> float """
        return 0.0

    def apertureChanged(self, *args, **kwargs): # real signature unknown
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

    def apertureRangeChanged(self, *args, **kwargs): # real signature unknown
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

    def exposureCompensation(self): # real signature unknown; restored from __doc__
        """ exposureCompensation(self) -> float """
        return 0.0

    def exposureCompensationChanged(self, *args, **kwargs): # real signature unknown
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

    def exposureMode(self): # real signature unknown; restored from __doc__
        """ exposureMode(self) -> QCameraExposure.ExposureMode """
        pass

    def flashMode(self): # real signature unknown; restored from __doc__
        """ flashMode(self) -> QCameraExposure.FlashModes """
        pass

    def flashReady(self, *args, **kwargs): # real signature unknown
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

    def isAvailable(self): # real signature unknown; restored from __doc__
        """ isAvailable(self) -> bool """
        return False

    def isExposureModeSupported(self, mode): # real signature unknown; restored from __doc__
        """ isExposureModeSupported(self, mode: QCameraExposure.ExposureMode) -> bool """
        return False

    def isFlashModeSupported(self, mode, QCameraExposure_FlashModes=None, QCameraExposure_FlashMode=None): # real signature unknown; restored from __doc__
        """ isFlashModeSupported(self, mode: Union[QCameraExposure.FlashModes, QCameraExposure.FlashMode]) -> bool """
        return False

    def isFlashReady(self): # real signature unknown; restored from __doc__
        """ isFlashReady(self) -> bool """
        return False

    def isMeteringModeSupported(self, mode): # real signature unknown; restored from __doc__
        """ isMeteringModeSupported(self, mode: QCameraExposure.MeteringMode) -> bool """
        return False

    def isoSensitivity(self): # real signature unknown; restored from __doc__
        """ isoSensitivity(self) -> int """
        return 0

    def isoSensitivityChanged(self, *args, **kwargs): # real signature unknown
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

    def meteringMode(self): # real signature unknown; restored from __doc__
        """ meteringMode(self) -> QCameraExposure.MeteringMode """
        pass

    def requestedAperture(self): # real signature unknown; restored from __doc__
        """ requestedAperture(self) -> float """
        return 0.0

    def requestedIsoSensitivity(self): # real signature unknown; restored from __doc__
        """ requestedIsoSensitivity(self) -> int """
        return 0

    def requestedShutterSpeed(self): # real signature unknown; restored from __doc__
        """ requestedShutterSpeed(self) -> float """
        return 0.0

    def setAutoAperture(self): # real signature unknown; restored from __doc__
        """ setAutoAperture(self) """
        pass

    def setAutoIsoSensitivity(self): # real signature unknown; restored from __doc__
        """ setAutoIsoSensitivity(self) """
        pass

    def setAutoShutterSpeed(self): # real signature unknown; restored from __doc__
        """ setAutoShutterSpeed(self) """
        pass

    def setExposureCompensation(self, ev): # real signature unknown; restored from __doc__
        """ setExposureCompensation(self, ev: float) """
        pass

    def setExposureMode(self, mode): # real signature unknown; restored from __doc__
        """ setExposureMode(self, mode: QCameraExposure.ExposureMode) """
        pass

    def setFlashMode(self, mode, QCameraExposure_FlashModes=None, QCameraExposure_FlashMode=None): # real signature unknown; restored from __doc__
        """ setFlashMode(self, mode: Union[QCameraExposure.FlashModes, QCameraExposure.FlashMode]) """
        pass

    def setManualAperture(self, aperture): # real signature unknown; restored from __doc__
        """ setManualAperture(self, aperture: float) """
        pass

    def setManualIsoSensitivity(self, iso): # real signature unknown; restored from __doc__
        """ setManualIsoSensitivity(self, iso: int) """
        pass

    def setManualShutterSpeed(self, seconds): # real signature unknown; restored from __doc__
        """ setManualShutterSpeed(self, seconds: float) """
        pass

    def setMeteringMode(self, mode): # real signature unknown; restored from __doc__
        """ setMeteringMode(self, mode: QCameraExposure.MeteringMode) """
        pass

    def setSpotMeteringPoint(self, point, QPointF=None, QPoint=None): # real signature unknown; restored from __doc__
        """ setSpotMeteringPoint(self, point: Union[QPointF, QPoint]) """
        pass

    def shutterSpeed(self): # real signature unknown; restored from __doc__
        """ shutterSpeed(self) -> float """
        return 0.0

    def shutterSpeedChanged(self, *args, **kwargs): # real signature unknown
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

    def shutterSpeedRangeChanged(self, *args, **kwargs): # real signature unknown
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

    def spotMeteringPoint(self): # real signature unknown; restored from __doc__
        """ spotMeteringPoint(self) -> QPointF """
        pass

    def supportedApertures(self): # real signature unknown; restored from __doc__
        """ supportedApertures(self) -> (List[float], Optional[bool]) """
        pass

    def supportedIsoSensitivities(self): # real signature unknown; restored from __doc__
        """ supportedIsoSensitivities(self) -> (List[int], Optional[bool]) """
        pass

    def supportedShutterSpeeds(self): # real signature unknown; restored from __doc__
        """ supportedShutterSpeeds(self) -> (List[float], Optional[bool]) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    ExposureAction = 11
    ExposureAuto = 0
    ExposureBacklight = 4
    ExposureBarcode = 20
    ExposureBeach = 8
    ExposureCandlelight = 19
    ExposureFireworks = 17
    ExposureLandscape = 12
    ExposureLargeAperture = 9
    ExposureManual = 1
    ExposureModeVendor = 1000
    ExposureNight = 3
    ExposureNightPortrait = 13
    ExposureParty = 18
    ExposurePortrait = 2
    ExposureSmallAperture = 10
    ExposureSnow = 7
    ExposureSports = 6
    ExposureSpotlight = 5
    ExposureSteadyPhoto = 16
    ExposureSunset = 15
    ExposureTheatre = 14
    FlashAuto = 1
    FlashFill = 16
    FlashManual = 512
    FlashOff = 2
    FlashOn = 4
    FlashRedEyeReduction = 8
    FlashSlowSyncFrontCurtain = 128
    FlashSlowSyncRearCurtain = 256
    FlashTorch = 32
    FlashVideoLight = 64
    MeteringAverage = 2
    MeteringMatrix = 1
    MeteringSpot = 3


