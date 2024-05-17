# encoding: utf-8
# module PyQt5.QtSensors
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtSensors.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QSensor(__PyQt5_QtCore.QObject):
    """ QSensor(type: Union[QByteArray, bytes, bytearray], parent: Optional[QObject] = None) """
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

    def addFilter(self, filter, QSensorFilter=None): # real signature unknown; restored from __doc__
        """ addFilter(self, filter: Optional[QSensorFilter]) """
        pass

    def alwaysOnChanged(self, *args, **kwargs): # real signature unknown
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

    def availableDataRates(self): # real signature unknown; restored from __doc__
        """ availableDataRates(self) -> List[Tuple[int, int]] """
        return []

    def availableSensorsChanged(self, *args, **kwargs): # real signature unknown
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

    def axesOrientationMode(self): # real signature unknown; restored from __doc__
        """ axesOrientationMode(self) -> QSensor.AxesOrientationMode """
        pass

    def axesOrientationModeChanged(self, *args, **kwargs): # real signature unknown
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

    def bufferSize(self): # real signature unknown; restored from __doc__
        """ bufferSize(self) -> int """
        return 0

    def bufferSizeChanged(self, *args, **kwargs): # real signature unknown
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

    def busyChanged(self, *args, **kwargs): # real signature unknown
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

    def connectToBackend(self): # real signature unknown; restored from __doc__
        """ connectToBackend(self) -> bool """
        return False

    def currentOrientation(self): # real signature unknown; restored from __doc__
        """ currentOrientation(self) -> int """
        return 0

    def currentOrientationChanged(self, *args, **kwargs): # real signature unknown
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

    def dataRate(self): # real signature unknown; restored from __doc__
        """ dataRate(self) -> int """
        return 0

    def dataRateChanged(self, *args, **kwargs): # real signature unknown
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

    def defaultSensorForType(self, type, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ defaultSensorForType(type: Union[QByteArray, bytes, bytearray]) -> QByteArray """
        pass

    def description(self): # real signature unknown; restored from __doc__
        """ description(self) -> str """
        return ""

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def efficientBufferSize(self): # real signature unknown; restored from __doc__
        """ efficientBufferSize(self) -> int """
        return 0

    def efficientBufferSizeChanged(self, *args, **kwargs): # real signature unknown
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

    def error(self): # real signature unknown; restored from __doc__
        """ error(self) -> int """
        return 0

    def filters(self): # real signature unknown; restored from __doc__
        """ filters(self) -> List[QSensorFilter] """
        return []

    def identifier(self): # real signature unknown; restored from __doc__
        """ identifier(self) -> QByteArray """
        pass

    def isActive(self): # real signature unknown; restored from __doc__
        """ isActive(self) -> bool """
        return False

    def isAlwaysOn(self): # real signature unknown; restored from __doc__
        """ isAlwaysOn(self) -> bool """
        return False

    def isBusy(self): # real signature unknown; restored from __doc__
        """ isBusy(self) -> bool """
        return False

    def isConnectedToBackend(self): # real signature unknown; restored from __doc__
        """ isConnectedToBackend(self) -> bool """
        return False

    def isFeatureSupported(self, feature): # real signature unknown; restored from __doc__
        """ isFeatureSupported(self, feature: QSensor.Feature) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def maxBufferSize(self): # real signature unknown; restored from __doc__
        """ maxBufferSize(self) -> int """
        return 0

    def maxBufferSizeChanged(self, *args, **kwargs): # real signature unknown
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

    def outputRange(self): # real signature unknown; restored from __doc__
        """ outputRange(self) -> int """
        return 0

    def outputRanges(self): # real signature unknown; restored from __doc__
        """ outputRanges(self) -> List[qoutputrange] """
        return []

    def reading(self): # real signature unknown; restored from __doc__
        """ reading(self) -> Optional[QSensorReading] """
        pass

    def readingChanged(self, *args, **kwargs): # real signature unknown
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

    def removeFilter(self, filter, QSensorFilter=None): # real signature unknown; restored from __doc__
        """ removeFilter(self, filter: Optional[QSensorFilter]) """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def sensorError(self, *args, **kwargs): # real signature unknown
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

    def sensorsForType(self, type, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ sensorsForType(type: Union[QByteArray, bytes, bytearray]) -> List[QByteArray] """
        return []

    def sensorTypes(self): # real signature unknown; restored from __doc__
        """ sensorTypes() -> List[QByteArray] """
        return []

    def setActive(self, active): # real signature unknown; restored from __doc__
        """ setActive(self, active: bool) """
        pass

    def setAlwaysOn(self, alwaysOn): # real signature unknown; restored from __doc__
        """ setAlwaysOn(self, alwaysOn: bool) """
        pass

    def setAxesOrientationMode(self, axesOrientationMode): # real signature unknown; restored from __doc__
        """ setAxesOrientationMode(self, axesOrientationMode: QSensor.AxesOrientationMode) """
        pass

    def setBufferSize(self, bufferSize): # real signature unknown; restored from __doc__
        """ setBufferSize(self, bufferSize: int) """
        pass

    def setCurrentOrientation(self, currentOrientation): # real signature unknown; restored from __doc__
        """ setCurrentOrientation(self, currentOrientation: int) """
        pass

    def setDataRate(self, rate): # real signature unknown; restored from __doc__
        """ setDataRate(self, rate: int) """
        pass

    def setEfficientBufferSize(self, efficientBufferSize): # real signature unknown; restored from __doc__
        """ setEfficientBufferSize(self, efficientBufferSize: int) """
        pass

    def setIdentifier(self, identifier, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ setIdentifier(self, identifier: Union[QByteArray, bytes, bytearray]) """
        pass

    def setMaxBufferSize(self, maxBufferSize): # real signature unknown; restored from __doc__
        """ setMaxBufferSize(self, maxBufferSize: int) """
        pass

    def setOutputRange(self, index): # real signature unknown; restored from __doc__
        """ setOutputRange(self, index: int) """
        pass

    def setSkipDuplicates(self, skipDuplicates): # real signature unknown; restored from __doc__
        """ setSkipDuplicates(self, skipDuplicates: bool) """
        pass

    def setUserOrientation(self, userOrientation): # real signature unknown; restored from __doc__
        """ setUserOrientation(self, userOrientation: int) """
        pass

    def skipDuplicates(self): # real signature unknown; restored from __doc__
        """ skipDuplicates(self) -> bool """
        return False

    def skipDuplicatesChanged(self, *args, **kwargs): # real signature unknown
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

    def start(self): # real signature unknown; restored from __doc__
        """ start(self) -> bool """
        return False

    def stop(self): # real signature unknown; restored from __doc__
        """ stop(self) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> QByteArray """
        pass

    def userOrientation(self): # real signature unknown; restored from __doc__
        """ userOrientation(self) -> int """
        return 0

    def userOrientationChanged(self, *args, **kwargs): # real signature unknown
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

    def __init__(self, type, QByteArray=None, bytes=None, bytearray=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    AccelerationMode = 4
    AlwaysOn = 1
    AutomaticOrientation = 1
    AxesOrientation = 6
    Buffering = 0
    FieldOfView = 3
    FixedOrientation = 0
    GeoValues = 2
    PressureSensorTemperature = 7
    SkipDuplicates = 5
    UserOrientation = 2


