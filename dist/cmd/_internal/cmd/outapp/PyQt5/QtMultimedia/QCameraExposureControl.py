# encoding: utf-8
# module PyQt5.QtMultimedia
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtMultimedia.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


from .QMediaControl import QMediaControl

class QCameraExposureControl(QMediaControl):
    """ QCameraExposureControl(parent: Optional[QObject] = None) """
    def actualValue(self, parameter): # real signature unknown; restored from __doc__
        """ actualValue(self, parameter: QCameraExposureControl.ExposureParameter) -> Any """
        pass

    def actualValueChanged(self, *args, **kwargs): # real signature unknown
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

    def isParameterSupported(self, parameter): # real signature unknown; restored from __doc__
        """ isParameterSupported(self, parameter: QCameraExposureControl.ExposureParameter) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def parameterRangeChanged(self, *args, **kwargs): # real signature unknown
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

    def requestedValue(self, parameter): # real signature unknown; restored from __doc__
        """ requestedValue(self, parameter: QCameraExposureControl.ExposureParameter) -> Any """
        pass

    def requestedValueChanged(self, *args, **kwargs): # real signature unknown
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

    def setValue(self, parameter, value): # real signature unknown; restored from __doc__
        """ setValue(self, parameter: QCameraExposureControl.ExposureParameter, value: Any) -> bool """
        return False

    def supportedParameterRange(self, parameter): # real signature unknown; restored from __doc__
        """ supportedParameterRange(self, parameter: QCameraExposureControl.ExposureParameter) -> (List[Any], Optional[bool]) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent, QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    Aperture = 1
    ExposureCompensation = 3
    ExposureMode = 8
    ExtendedExposureParameter = 1000
    FlashCompensation = 5
    FlashPower = 4
    ISO = 0
    MeteringMode = 9
    ShutterSpeed = 2
    SpotMeteringPoint = 7
    TorchPower = 6


