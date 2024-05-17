# encoding: utf-8
# module PyQt5.QtBluetooth
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtBluetooth.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


# no functions
# classes

class QBluetooth(__sip.simplewrapper):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    AttAuthenticationRequired = 2
    AttAuthorizationRequired = 1
    AttEncryptionRequired = 4
    Authentication = 2
    Authorization = 1
    Encryption = 4
    NoSecurity = 0
    Secure = 8


class QBluetoothAddress(__sip.wrapper):
    """
    QBluetoothAddress()
    QBluetoothAddress(address: int)
    QBluetoothAddress(address: Optional[str])
    QBluetoothAddress(other: QBluetoothAddress)
    """
    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def toString(self): # real signature unknown; restored from __doc__
        """ toString(self) -> str """
        return ""

    def toUInt64(self): # real signature unknown; restored from __doc__
        """ toUInt64(self) -> int """
        return 0

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __hash__ = None


class QBluetoothDeviceDiscoveryAgent(__PyQt5_QtCore.QObject):
    """
    QBluetoothDeviceDiscoveryAgent(parent: Optional[QObject] = None)
    QBluetoothDeviceDiscoveryAgent(deviceAdapter: QBluetoothAddress, parent: Optional[QObject] = None)
    """
    def canceled(self, *args, **kwargs): # real signature unknown
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

    def deviceDiscovered(self, *args, **kwargs): # real signature unknown
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

    def deviceUpdated(self, *args, **kwargs): # real signature unknown
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

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def discoveredDevices(self): # real signature unknown; restored from __doc__
        """ discoveredDevices(self) -> List[QBluetoothDeviceInfo] """
        return []

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

    def inquiryType(self): # real signature unknown; restored from __doc__
        """ inquiryType(self) -> QBluetoothDeviceDiscoveryAgent.InquiryType """
        pass

    def isActive(self): # real signature unknown; restored from __doc__
        """ isActive(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def lowEnergyDiscoveryTimeout(self): # real signature unknown; restored from __doc__
        """ lowEnergyDiscoveryTimeout(self) -> int """
        return 0

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setInquiryType(self, type): # real signature unknown; restored from __doc__
        """ setInquiryType(self, type: QBluetoothDeviceDiscoveryAgent.InquiryType) """
        pass

    def setLowEnergyDiscoveryTimeout(self, msTimeout): # real signature unknown; restored from __doc__
        """ setLowEnergyDiscoveryTimeout(self, msTimeout: int) """
        pass

    def start(self, method=None, QBluetoothDeviceDiscoveryAgent_DiscoveryMethods=None, QBluetoothDeviceDiscoveryAgent_DiscoveryMethod=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        start(self)
        start(self, method: Union[QBluetoothDeviceDiscoveryAgent.DiscoveryMethods, QBluetoothDeviceDiscoveryAgent.DiscoveryMethod])
        """
        pass

    def stop(self): # real signature unknown; restored from __doc__
        """ stop(self) """
        pass

    def supportedDiscoveryMethods(self): # real signature unknown; restored from __doc__
        """ supportedDiscoveryMethods() -> QBluetoothDeviceDiscoveryAgent.DiscoveryMethods """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    ClassicMethod = 1
    GeneralUnlimitedInquiry = 0
    InputOutputError = 1
    InvalidBluetoothAdapterError = 3
    LimitedInquiry = 1
    LowEnergyMethod = 2
    NoError = 0
    NoMethod = 0
    PoweredOffError = 2
    UnknownError = 100
    UnsupportedDiscoveryMethod = 5
    UnsupportedPlatformError = 4


class QBluetoothDeviceInfo(__sip.wrapper):
    """
    QBluetoothDeviceInfo()
    QBluetoothDeviceInfo(address: QBluetoothAddress, name: Optional[str], classOfDevice: int)
    QBluetoothDeviceInfo(uuid: QBluetoothUuid, name: Optional[str], classOfDevice: int)
    QBluetoothDeviceInfo(other: QBluetoothDeviceInfo)
    """
    def address(self): # real signature unknown; restored from __doc__
        """ address(self) -> QBluetoothAddress """
        return QBluetoothAddress

    def coreConfigurations(self): # real signature unknown; restored from __doc__
        """ coreConfigurations(self) -> QBluetoothDeviceInfo.CoreConfigurations """
        pass

    def deviceUuid(self): # real signature unknown; restored from __doc__
        """ deviceUuid(self) -> QBluetoothUuid """
        return QBluetoothUuid

    def isCached(self): # real signature unknown; restored from __doc__
        """ isCached(self) -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def majorDeviceClass(self): # real signature unknown; restored from __doc__
        """ majorDeviceClass(self) -> QBluetoothDeviceInfo.MajorDeviceClass """
        pass

    def manufacturerData(self, manufacturerId=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        manufacturerData(self, manufacturerId: int) -> QByteArray
        manufacturerData(self) -> Dict[int, QByteArray]
        """
        return {}

    def manufacturerIds(self): # real signature unknown; restored from __doc__
        """ manufacturerIds(self) -> List[int] """
        return []

    def minorDeviceClass(self): # real signature unknown; restored from __doc__
        """ minorDeviceClass(self) -> int """
        return 0

    def name(self): # real signature unknown; restored from __doc__
        """ name(self) -> str """
        return ""

    def rssi(self): # real signature unknown; restored from __doc__
        """ rssi(self) -> int """
        return 0

    def serviceClasses(self): # real signature unknown; restored from __doc__
        """ serviceClasses(self) -> QBluetoothDeviceInfo.ServiceClasses """
        pass

    def serviceUuids(self): # real signature unknown; restored from __doc__
        """ serviceUuids(self) -> (List[QBluetoothUuid], Optional[QBluetoothDeviceInfo.DataCompleteness]) """
        pass

    def serviceUuidsCompleteness(self): # real signature unknown; restored from __doc__
        """ serviceUuidsCompleteness(self) -> QBluetoothDeviceInfo.DataCompleteness """
        pass

    def setCached(self, cached): # real signature unknown; restored from __doc__
        """ setCached(self, cached: bool) """
        pass

    def setCoreConfigurations(self, coreConfigs, QBluetoothDeviceInfo_CoreConfigurations=None, QBluetoothDeviceInfo_CoreConfiguration=None): # real signature unknown; restored from __doc__
        """ setCoreConfigurations(self, coreConfigs: Union[QBluetoothDeviceInfo.CoreConfigurations, QBluetoothDeviceInfo.CoreConfiguration]) """
        pass

    def setDeviceUuid(self, uuid): # real signature unknown; restored from __doc__
        """ setDeviceUuid(self, uuid: QBluetoothUuid) """
        pass

    def setManufacturerData(self, manufacturerId, data, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ setManufacturerData(self, manufacturerId: int, data: Union[QByteArray, bytes, bytearray]) -> bool """
        return False

    def setRssi(self, signal): # real signature unknown; restored from __doc__
        """ setRssi(self, signal: int) """
        pass

    def setServiceUuids(self, uuids, QBluetoothUuid=None, *args=None, **kwargs=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setServiceUuids(self, uuids: Iterable[QBluetoothUuid], completeness: QBluetoothDeviceInfo.DataCompleteness)
        setServiceUuids(self, uuids: Iterable[QBluetoothUuid])
        """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    AllServices = 2047
    AudioService = 32
    AudioVideoDevice = 4
    BaseRateAndLowEnergyCoreConfiguration = 3
    BaseRateCoreConfiguration = 2
    Camcorder = 13
    CapturingService = 8
    CarAudio = 8
    CardReaderPeripheral = 6
    CellularPhone = 1
    CommonIsdnAccessPhone = 5
    ComputerDevice = 1
    CordlessPhone = 2
    DataComplete = 0
    DataIncomplete = 1
    DataUnavailable = 2
    DesktopComputer = 1
    DigitizerTabletPeripheral = 5
    GamepadPeripheral = 2
    GamingDevice = 18
    HandheldClamShellComputer = 4
    HandheldComputer = 5
    HandsFreeDevice = 2
    Headphones = 6
    HealthBloodPressureMonitor = 1
    HealthDataDisplay = 7
    HealthDevice = 9
    HealthGlucoseMeter = 4
    HealthPulseOximeter = 5
    HealthStepCounter = 8
    HealthThermometer = 2
    HealthWeightScale = 3
    HiFiAudioDevice = 10
    ImageCamera = 8
    ImageDisplay = 4
    ImagePrinter = 32
    ImageScanner = 16
    ImagingDevice = 6
    InformationService = 128
    JoystickPeripheral = 1
    KeyboardPeripheral = 16
    KeyboardWithPointingDevicePeripheral = 48
    LANAccessDevice = 3
    LaptopComputer = 3
    Loudspeaker = 5
    LowEnergyCoreConfiguration = 1
    Microphone = 4
    MiscellaneousDevice = 0
    NetworkDevice = 3
    NetworkFullService = 0
    NetworkingService = 2
    NetworkLoadFactorFive = 40
    NetworkLoadFactorFour = 32
    NetworkLoadFactorOne = 8
    NetworkLoadFactorSix = 48
    NetworkLoadFactorThree = 24
    NetworkLoadFactorTwo = 16
    NetworkNoService = 56
    NoService = 0
    ObjectTransferService = 16
    PeripheralDevice = 5
    PhoneDevice = 2
    PointingDevicePeripheral = 32
    PortableAudioDevice = 7
    PositioningService = 1
    RemoteControlPeripheral = 3
    RenderingService = 4
    SensingDevicePeripheral = 4
    ServerComputer = 2
    SetTopBox = 9
    SmartPhone = 3
    TelephonyService = 64
    ToyController = 4
    ToyDevice = 8
    ToyDoll = 3
    ToyGame = 5
    ToyRobot = 1
    ToyVehicle = 2
    UncategorizedAudioVideoDevice = 0
    UncategorizedComputer = 0
    UncategorizedDevice = 31
    UncategorizedHealthDevice = 0
    UncategorizedImagingDevice = 0
    UncategorizedMiscellaneous = 0
    UncategorizedPeripheral = 0
    UncategorizedPhone = 0
    UncategorizedToy = 0
    UncategorizedWearableDevice = 0
    UnknownCoreConfiguration = 0
    Vcr = 11
    VideoCamera = 12
    VideoConferencing = 16
    VideoDisplayAndLoudspeaker = 15
    VideoMonitor = 14
    WearableComputer = 6
    WearableDevice = 7
    WearableGlasses = 5
    WearableHeadsetDevice = 1
    WearableHelmet = 4
    WearableJacket = 3
    WearablePager = 2
    WearableWristWatch = 1
    WiredModemOrVoiceGatewayPhone = 4
    __hash__ = None


class QBluetoothHostInfo(__sip.wrapper):
    """
    QBluetoothHostInfo()
    QBluetoothHostInfo(other: QBluetoothHostInfo)
    """
    def address(self): # real signature unknown; restored from __doc__
        """ address(self) -> QBluetoothAddress """
        return QBluetoothAddress

    def name(self): # real signature unknown; restored from __doc__
        """ name(self) -> str """
        return ""

    def setAddress(self, address): # real signature unknown; restored from __doc__
        """ setAddress(self, address: QBluetoothAddress) """
        pass

    def setName(self, name, p_str=None): # real signature unknown; restored from __doc__
        """ setName(self, name: Optional[str]) """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, other=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __hash__ = None


class QBluetoothLocalDevice(__PyQt5_QtCore.QObject):
    """
    QBluetoothLocalDevice(parent: Optional[QObject] = None)
    QBluetoothLocalDevice(address: QBluetoothAddress, parent: Optional[QObject] = None)
    """
    def address(self): # real signature unknown; restored from __doc__
        """ address(self) -> QBluetoothAddress """
        return QBluetoothAddress

    def allDevices(self): # real signature unknown; restored from __doc__
        """ allDevices() -> List[QBluetoothHostInfo] """
        return []

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectedDevices(self): # real signature unknown; restored from __doc__
        """ connectedDevices(self) -> List[QBluetoothAddress] """
        return []

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def deviceConnected(self, *args, **kwargs): # real signature unknown
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

    def deviceDisconnected(self, *args, **kwargs): # real signature unknown
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

    def hostMode(self): # real signature unknown; restored from __doc__
        """ hostMode(self) -> QBluetoothLocalDevice.HostMode """
        pass

    def hostModeStateChanged(self, *args, **kwargs): # real signature unknown
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

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def name(self): # real signature unknown; restored from __doc__
        """ name(self) -> str """
        return ""

    def pairingConfirmation(self, confirmation): # real signature unknown; restored from __doc__
        """ pairingConfirmation(self, confirmation: bool) """
        pass

    def pairingDisplayConfirmation(self, *args, **kwargs): # real signature unknown
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

    def pairingDisplayPinCode(self, *args, **kwargs): # real signature unknown
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

    def pairingFinished(self, *args, **kwargs): # real signature unknown
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

    def pairingStatus(self, address): # real signature unknown; restored from __doc__
        """ pairingStatus(self, address: QBluetoothAddress) -> QBluetoothLocalDevice.Pairing """
        pass

    def powerOn(self): # real signature unknown; restored from __doc__
        """ powerOn(self) """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def requestPairing(self, address, pairing): # real signature unknown; restored from __doc__
        """ requestPairing(self, address: QBluetoothAddress, pairing: QBluetoothLocalDevice.Pairing) """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setHostMode(self, mode): # real signature unknown; restored from __doc__
        """ setHostMode(self, mode: QBluetoothLocalDevice.HostMode) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    AuthorizedPaired = 2
    HostConnectable = 1
    HostDiscoverable = 2
    HostDiscoverableLimitedInquiry = 3
    HostPoweredOff = 0
    NoError = 0
    Paired = 1
    PairingError = 1
    UnknownError = 100
    Unpaired = 0


class QBluetoothServer(__PyQt5_QtCore.QObject):
    """ QBluetoothServer(serverType: QBluetoothServiceInfo.Protocol, parent: Optional[QObject] = None) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def close(self): # real signature unknown; restored from __doc__
        """ close(self) """
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
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

    def hasPendingConnections(self): # real signature unknown; restored from __doc__
        """ hasPendingConnections(self) -> bool """
        return False

    def isListening(self): # real signature unknown; restored from __doc__
        """ isListening(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def listen(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        listen(self, address: QBluetoothAddress = QBluetoothAddress(), port: int = 0) -> bool
        listen(self, uuid: QBluetoothUuid, serviceName: Optional[str] = '') -> QBluetoothServiceInfo
        """
        pass

    def maxPendingConnections(self): # real signature unknown; restored from __doc__
        """ maxPendingConnections(self) -> int """
        return 0

    def newConnection(self, *args, **kwargs): # real signature unknown
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

    def nextPendingConnection(self): # real signature unknown; restored from __doc__
        """ nextPendingConnection(self) -> Optional[QBluetoothSocket] """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def securityFlags(self): # real signature unknown; restored from __doc__
        """ securityFlags(self) -> QBluetooth.SecurityFlags """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def serverAddress(self): # real signature unknown; restored from __doc__
        """ serverAddress(self) -> QBluetoothAddress """
        return QBluetoothAddress

    def serverPort(self): # real signature unknown; restored from __doc__
        """ serverPort(self) -> int """
        return 0

    def serverType(self): # real signature unknown; restored from __doc__
        """ serverType(self) -> QBluetoothServiceInfo.Protocol """
        pass

    def setMaxPendingConnections(self, numConnections): # real signature unknown; restored from __doc__
        """ setMaxPendingConnections(self, numConnections: int) """
        pass

    def setSecurityFlags(self, security, QBluetooth_SecurityFlags=None, QBluetooth_Security=None): # real signature unknown; restored from __doc__
        """ setSecurityFlags(self, security: Union[QBluetooth.SecurityFlags, QBluetooth.Security]) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, serverType, parent, QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    InputOutputError = 3
    NoError = 0
    PoweredOffError = 2
    ServiceAlreadyRegisteredError = 4
    UnknownError = 1
    UnsupportedProtocolError = 5


class QBluetoothServiceDiscoveryAgent(__PyQt5_QtCore.QObject):
    """
    QBluetoothServiceDiscoveryAgent(parent: Optional[QObject] = None)
    QBluetoothServiceDiscoveryAgent(deviceAdapter: QBluetoothAddress, parent: Optional[QObject] = None)
    """
    def canceled(self, *args, **kwargs): # real signature unknown
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

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def discoveredServices(self): # real signature unknown; restored from __doc__
        """ discoveredServices(self) -> List[QBluetoothServiceInfo] """
        return []

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

    def isActive(self): # real signature unknown; restored from __doc__
        """ isActive(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def remoteAddress(self): # real signature unknown; restored from __doc__
        """ remoteAddress(self) -> QBluetoothAddress """
        return QBluetoothAddress

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def serviceDiscovered(self, *args, **kwargs): # real signature unknown
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

    def setRemoteAddress(self, address): # real signature unknown; restored from __doc__
        """ setRemoteAddress(self, address: QBluetoothAddress) -> bool """
        return False

    def setUuidFilter(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setUuidFilter(self, uuids: Iterable[QBluetoothUuid])
        setUuidFilter(self, uuid: QBluetoothUuid)
        """
        pass

    def start(self, mode=None): # real signature unknown; restored from __doc__
        """ start(self, mode: QBluetoothServiceDiscoveryAgent.DiscoveryMode = QBluetoothServiceDiscoveryAgent.MinimalDiscovery) """
        pass

    def stop(self): # real signature unknown; restored from __doc__
        """ stop(self) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def uuidFilter(self): # real signature unknown; restored from __doc__
        """ uuidFilter(self) -> List[QBluetoothUuid] """
        return []

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    FullDiscovery = 1
    InputOutputError = 1
    InvalidBluetoothAdapterError = 3
    MinimalDiscovery = 0
    NoError = 0
    PoweredOffError = 2
    UnknownError = 100


class QBluetoothServiceInfo(__sip.wrapper):
    """
    QBluetoothServiceInfo()
    QBluetoothServiceInfo(other: QBluetoothServiceInfo)
    """
    def attribute(self, attributeId): # real signature unknown; restored from __doc__
        """ attribute(self, attributeId: int) -> Any """
        pass

    def attributes(self): # real signature unknown; restored from __doc__
        """ attributes(self) -> List[int] """
        return []

    def contains(self, attributeId): # real signature unknown; restored from __doc__
        """ contains(self, attributeId: int) -> bool """
        return False

    def device(self): # real signature unknown; restored from __doc__
        """ device(self) -> QBluetoothDeviceInfo """
        return QBluetoothDeviceInfo

    def isComplete(self): # real signature unknown; restored from __doc__
        """ isComplete(self) -> bool """
        return False

    def isRegistered(self): # real signature unknown; restored from __doc__
        """ isRegistered(self) -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def protocolDescriptor(self, protocol): # real signature unknown; restored from __doc__
        """ protocolDescriptor(self, protocol: QBluetoothUuid.ProtocolUuid) -> List[Any] """
        return []

    def protocolServiceMultiplexer(self): # real signature unknown; restored from __doc__
        """ protocolServiceMultiplexer(self) -> int """
        return 0

    def registerService(self, localAdapter=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ registerService(self, localAdapter: QBluetoothAddress = QBluetoothAddress()) -> bool """
        pass

    def removeAttribute(self, attributeId): # real signature unknown; restored from __doc__
        """ removeAttribute(self, attributeId: int) """
        pass

    def serverChannel(self): # real signature unknown; restored from __doc__
        """ serverChannel(self) -> int """
        return 0

    def serviceAvailability(self): # real signature unknown; restored from __doc__
        """ serviceAvailability(self) -> int """
        return 0

    def serviceClassUuids(self): # real signature unknown; restored from __doc__
        """ serviceClassUuids(self) -> List[QBluetoothUuid] """
        return []

    def serviceDescription(self): # real signature unknown; restored from __doc__
        """ serviceDescription(self) -> str """
        return ""

    def serviceName(self): # real signature unknown; restored from __doc__
        """ serviceName(self) -> str """
        return ""

    def serviceProvider(self): # real signature unknown; restored from __doc__
        """ serviceProvider(self) -> str """
        return ""

    def serviceUuid(self): # real signature unknown; restored from __doc__
        """ serviceUuid(self) -> QBluetoothUuid """
        return QBluetoothUuid

    def setAttribute(self, attributeId, value, Any=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setAttribute(self, attributeId: int, value: QBluetoothUuid)
        setAttribute(self, attributeId: int, value: Iterable[Any])
        setAttribute(self, attributeId: int, value: Any)
        """
        pass

    def setDevice(self, info): # real signature unknown; restored from __doc__
        """ setDevice(self, info: QBluetoothDeviceInfo) """
        pass

    def setServiceAvailability(self, availability): # real signature unknown; restored from __doc__
        """ setServiceAvailability(self, availability: int) """
        pass

    def setServiceDescription(self, description, p_str=None): # real signature unknown; restored from __doc__
        """ setServiceDescription(self, description: Optional[str]) """
        pass

    def setServiceName(self, name, p_str=None): # real signature unknown; restored from __doc__
        """ setServiceName(self, name: Optional[str]) """
        pass

    def setServiceProvider(self, provider, p_str=None): # real signature unknown; restored from __doc__
        """ setServiceProvider(self, provider: Optional[str]) """
        pass

    def setServiceUuid(self, uuid): # real signature unknown; restored from __doc__
        """ setServiceUuid(self, uuid: QBluetoothUuid) """
        pass

    def socketProtocol(self): # real signature unknown; restored from __doc__
        """ socketProtocol(self) -> QBluetoothServiceInfo.Protocol """
        pass

    def unregisterService(self): # real signature unknown; restored from __doc__
        """ unregisterService(self) -> bool """
        return False

    def __init__(self, other=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    AdditionalProtocolDescriptorList = 13
    BluetoothProfileDescriptorList = 9
    BrowseGroupList = 5
    ClientExecutableUrl = 11
    DocumentationUrl = 10
    IconUrl = 12
    L2capProtocol = 1
    LanguageBaseAttributeIdList = 6
    PrimaryLanguageBase = 256
    ProtocolDescriptorList = 4
    RfcommProtocol = 2
    ServiceAvailability = 8
    ServiceClassIds = 1
    ServiceDescription = 257
    ServiceId = 3
    ServiceInfoTimeToLive = 7
    ServiceName = 256
    ServiceProvider = 258
    ServiceRecordHandle = 0
    ServiceRecordState = 2
    UnknownProtocol = 0


class QBluetoothSocket(__PyQt5_QtCore.QIODevice):
    """
    QBluetoothSocket(socketType: QBluetoothServiceInfo.Protocol, parent: Optional[QObject] = None)
    QBluetoothSocket(parent: Optional[QObject] = None)
    """
    def abort(self): # real signature unknown; restored from __doc__
        """ abort(self) """
        pass

    def bytesAvailable(self): # real signature unknown; restored from __doc__
        """ bytesAvailable(self) -> int """
        return 0

    def bytesToWrite(self): # real signature unknown; restored from __doc__
        """ bytesToWrite(self) -> int """
        return 0

    def canReadLine(self): # real signature unknown; restored from __doc__
        """ canReadLine(self) -> bool """
        return False

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def close(self): # real signature unknown; restored from __doc__
        """ close(self) """
        pass

    def connected(self, *args, **kwargs): # real signature unknown
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

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def connectToService(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        connectToService(self, service: QBluetoothServiceInfo, mode: Union[QIODevice.OpenMode, QIODevice.OpenModeFlag] = QIODevice.ReadWrite)
        connectToService(self, address: QBluetoothAddress, uuid: QBluetoothUuid, mode: Union[QIODevice.OpenMode, QIODevice.OpenModeFlag] = QIODevice.ReadWrite)
        connectToService(self, address: QBluetoothAddress, port: int, mode: Union[QIODevice.OpenMode, QIODevice.OpenModeFlag] = QIODevice.ReadWrite)
        """
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnected(self, *args, **kwargs): # real signature unknown
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

    def disconnectFromService(self): # real signature unknown; restored from __doc__
        """ disconnectFromService(self) """
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def doDeviceDiscovery(self, service, openMode, QIODevice_OpenMode=None, QIODevice_OpenModeFlag=None): # real signature unknown; restored from __doc__
        """ doDeviceDiscovery(self, service: QBluetoothServiceInfo, openMode: Union[QIODevice.OpenMode, QIODevice.OpenModeFlag]) """
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

    def isSequential(self): # real signature unknown; restored from __doc__
        """ isSequential(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def localAddress(self): # real signature unknown; restored from __doc__
        """ localAddress(self) -> QBluetoothAddress """
        return QBluetoothAddress

    def localName(self): # real signature unknown; restored from __doc__
        """ localName(self) -> str """
        return ""

    def localPort(self): # real signature unknown; restored from __doc__
        """ localPort(self) -> int """
        return 0

    def peerAddress(self): # real signature unknown; restored from __doc__
        """ peerAddress(self) -> QBluetoothAddress """
        return QBluetoothAddress

    def peerName(self): # real signature unknown; restored from __doc__
        """ peerName(self) -> str """
        return ""

    def peerPort(self): # real signature unknown; restored from __doc__
        """ peerPort(self) -> int """
        return 0

    def preferredSecurityFlags(self): # real signature unknown; restored from __doc__
        """ preferredSecurityFlags(self) -> QBluetooth.SecurityFlags """
        pass

    def readData(self, maxlen): # real signature unknown; restored from __doc__
        """ readData(self, maxlen: int) -> bytes """
        return b""

    def readLineData(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setErrorString(self, *args, **kwargs): # real signature unknown
        pass

    def setOpenMode(self, *args, **kwargs): # real signature unknown
        pass

    def setPreferredSecurityFlags(self, flags, QBluetooth_SecurityFlags=None, QBluetooth_Security=None): # real signature unknown; restored from __doc__
        """ setPreferredSecurityFlags(self, flags: Union[QBluetooth.SecurityFlags, QBluetooth.Security]) """
        pass

    def setSocketDescriptor(self, socketDescriptor, socketType, state=None, mode, QIODevice_OpenMode=None, QIODevice_OpenModeFlag=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setSocketDescriptor(self, socketDescriptor: int, socketType: QBluetoothServiceInfo.Protocol, state: QBluetoothSocket.SocketState = QBluetoothSocket.ConnectedState, mode: Union[QIODevice.OpenMode, QIODevice.OpenModeFlag] = QIODevice.ReadWrite) -> bool """
        pass

    def setSocketError(self, error): # real signature unknown; restored from __doc__
        """ setSocketError(self, error: QBluetoothSocket.SocketError) """
        pass

    def setSocketState(self, state): # real signature unknown; restored from __doc__
        """ setSocketState(self, state: QBluetoothSocket.SocketState) """
        pass

    def socketDescriptor(self): # real signature unknown; restored from __doc__
        """ socketDescriptor(self) -> int """
        return 0

    def socketType(self): # real signature unknown; restored from __doc__
        """ socketType(self) -> QBluetoothServiceInfo.Protocol """
        pass

    def state(self): # real signature unknown; restored from __doc__
        """ state(self) -> QBluetoothSocket.SocketState """
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

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def writeData(self, data, PyQt5_sip_array=None, bytes=None): # real signature unknown; restored from __doc__
        """ writeData(self, data: Optional[PyQt5.sip.array[bytes]]) -> int """
        return 0

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    BoundState = 4
    ClosingState = 6
    ConnectedState = 3
    ConnectingState = 2
    HostNotFoundError = 2
    ListeningState = 5
    NetworkError = 7
    NoSocketError = -2
    OperationError = 19
    RemoteHostClosedError = 1
    ServiceLookupState = 1
    ServiceNotFoundError = 9
    UnconnectedState = 0
    UnknownSocketError = -1
    UnsupportedProtocolError = 8


class QBluetoothTransferManager(__PyQt5_QtCore.QObject):
    """ QBluetoothTransferManager(parent: Optional[QObject] = None) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

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

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def put(self, request, data, QIODevice=None): # real signature unknown; restored from __doc__
        """ put(self, request: QBluetoothTransferRequest, data: Optional[QIODevice]) -> Optional[QBluetoothTransferReply] """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent, QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass


class QBluetoothTransferReply(__PyQt5_QtCore.QObject):
    """ QBluetoothTransferReply(parent: Optional[QObject] = None) """
    def abort(self): # real signature unknown; restored from __doc__
        """ abort(self) """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
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

    def errorString(self): # real signature unknown; restored from __doc__
        """ errorString(self) -> str """
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

    def isFinished(self): # real signature unknown; restored from __doc__
        """ isFinished(self) -> bool """
        return False

    def isRunning(self): # real signature unknown; restored from __doc__
        """ isRunning(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def manager(self): # real signature unknown; restored from __doc__
        """ manager(self) -> Optional[QBluetoothTransferManager] """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def request(self): # real signature unknown; restored from __doc__
        """ request(self) -> QBluetoothTransferRequest """
        return QBluetoothTransferRequest

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setManager(self, manager, QBluetoothTransferManager=None): # real signature unknown; restored from __doc__
        """ setManager(self, manager: Optional[QBluetoothTransferManager]) """
        pass

    def setRequest(self, request): # real signature unknown; restored from __doc__
        """ setRequest(self, request: QBluetoothTransferRequest) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def transferProgress(self, *args, **kwargs): # real signature unknown
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

    FileNotFoundError = 2
    HostNotFoundError = 3
    IODeviceNotReadableError = 5
    NoError = 0
    ResourceBusyError = 6
    SessionError = 7
    UnknownError = 1
    UserCanceledTransferError = 4


class QBluetoothTransferRequest(__sip.wrapper):
    """
    QBluetoothTransferRequest(address: QBluetoothAddress = QBluetoothAddress())
    QBluetoothTransferRequest(other: QBluetoothTransferRequest)
    """
    def address(self): # real signature unknown; restored from __doc__
        """ address(self) -> QBluetoothAddress """
        return QBluetoothAddress

    def attribute(self, code, defaultValue=None): # real signature unknown; restored from __doc__
        """ attribute(self, code: QBluetoothTransferRequest.Attribute, defaultValue: Any = None) -> Any """
        pass

    def setAttribute(self, code, value): # real signature unknown; restored from __doc__
        """ setAttribute(self, code: QBluetoothTransferRequest.Attribute, value: Any) """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    DescriptionAttribute = 0
    LengthAttribute = 3
    NameAttribute = 4
    TimeAttribute = 1
    TypeAttribute = 2
    __hash__ = None


class QBluetoothUuid(__PyQt5_QtCore.QUuid):
    """
    QBluetoothUuid()
    QBluetoothUuid(uuid: QBluetoothUuid.ProtocolUuid)
    QBluetoothUuid(uuid: QBluetoothUuid.ServiceClassUuid)
    QBluetoothUuid(uuid: QBluetoothUuid.CharacteristicType)
    QBluetoothUuid(uuid: QBluetoothUuid.DescriptorType)
    QBluetoothUuid(uuid: int)
    QBluetoothUuid(uuid: Tuple[int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int])
    QBluetoothUuid(uuid: Optional[str])
    QBluetoothUuid(uuid: QBluetoothUuid)
    QBluetoothUuid(uuid: QUuid)
    """
    def characteristicToString(self, uuid): # real signature unknown; restored from __doc__
        """ characteristicToString(uuid: QBluetoothUuid.CharacteristicType) -> str """
        return ""

    def descriptorToString(self, uuid): # real signature unknown; restored from __doc__
        """ descriptorToString(uuid: QBluetoothUuid.DescriptorType) -> str """
        return ""

    def minimumSize(self): # real signature unknown; restored from __doc__
        """ minimumSize(self) -> int """
        return 0

    def protocolToString(self, uuid): # real signature unknown; restored from __doc__
        """ protocolToString(uuid: QBluetoothUuid.ProtocolUuid) -> str """
        return ""

    def serviceClassToString(self, uuid): # real signature unknown; restored from __doc__
        """ serviceClassToString(uuid: QBluetoothUuid.ServiceClassUuid) -> str """
        return ""

    def toUInt128(self): # real signature unknown; restored from __doc__
        """ toUInt128(self) -> Tuple[int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int] """
        pass

    def toUInt16(self): # real signature unknown; restored from __doc__
        """ toUInt16(self) -> (int, Optional[bool]) """
        pass

    def toUInt32(self): # real signature unknown; restored from __doc__
        """ toUInt32(self) -> (int, Optional[bool]) """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, uuid=None, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    AdvancedAudioDistribution = 4365
    AerobicHeartRateLowerLimit = 10878
    AerobicHeartRateUpperLimit = 10884
    AerobicThreshold = 10879
    Age = 10880
    AlertCategoryID = 10819
    AlertCategoryIDBitMask = 10818
    AlertLevel = 10758
    AlertNotificationControlPoint = 10820
    AlertNotificationService = 6161
    AlertStatus = 10815
    AnaerobicHeartRateLowerLimit = 10881
    AnaerobicHeartRateUpperLimit = 10882
    AnaerobicThreshold = 10883
    ApparentWindDirection = 10867
    ApparentWindSpeed = 10866
    Appearance = 10753
    Att = 7
    AudioSink = 4363
    AudioSource = 4362
    Avctp = 23
    Avdtp = 25
    AV_RemoteControl = 4366
    AV_RemoteControlController = 4367
    AV_RemoteControlTarget = 4364
    BarometricPressureTrend = 10915
    BasicImage = 4378
    BasicPrinting = 4386
    BatteryLevel = 10777
    BatteryService = 6159
    BloodPressure = 6160
    BloodPressureFeature = 10825
    BloodPressureMeasurement = 10805
    Bnep = 15
    BodyComposition = 6171
    BodyCompositionFeature = 10907
    BodyCompositionMeasurement = 10908
    BodySensorLocation = 10808
    BondManagement = 6174
    BootKeyboardInputReport = 10786
    BootKeyboardOutputReport = 10802
    BootMouseInputReport = 10803
    BrowseGroupDescriptor = 4097
    CharacteristicAggregateFormat = 10501
    CharacteristicExtendedProperties = 10496
    CharacteristicPresentationFormat = 10500
    CharacteristicUserDescription = 10497
    ClientCharacteristicConfiguration = 10498
    Cmtp = 27
    ContinuousGlucoseMonitoring = 6175
    CSCFeature = 10844
    CSCMeasurement = 10843
    CurrentTime = 10795
    CurrentTimeService = 6149
    CyclingPower = 6168
    CyclingPowerControlPoint = 10854
    CyclingPowerFeature = 10853
    CyclingPowerMeasurement = 10851
    CyclingPowerVector = 10852
    CyclingSpeedAndCadence = 6166
    DatabaseChangeIncrement = 10905
    DateOfBirth = 10885
    DateOfThresholdAssessment = 10886
    DateTime = 10760
    DayDateTime = 10762
    DayOfWeek = 10761
    DescriptorValueChanged = 10877
    DeviceInformation = 6154
    DeviceName = 10752
    DewPoint = 10875
    DialupNetworking = 4355
    DirectPrinting = 4376
    DirectPrintingReferenceObjectsService = 4384
    Display3D = 4407
    DSTOffset = 10765
    Elevation = 10860
    EmailAddress = 10887
    EnvironmentalSensing = 6170
    EnvironmentalSensingConfiguration = 10507
    EnvironmentalSensingMeasurement = 10508
    EnvironmentalSensingTriggerSetting = 10509
    ExactTime256 = 10764
    ExternalReportReference = 10503
    FatBurnHeartRateLowerLimit = 10888
    FatBurnHeartRateUpperLimit = 10889
    FirmwareRevisionString = 10790
    FirstName = 10890
    FiveZoneHeartRateLimits = 10891
    Ftp = 10
    Gender = 10892
    GenericAccess = 6144
    GenericAttribute = 6145
    GenericAudio = 4611
    GenericFileTransfer = 4610
    GenericNetworking = 4609
    GenericTelephony = 4612
    Glasses3D = 4408
    Glucose = 6152
    GlucoseFeature = 10833
    GlucoseMeasurement = 10776
    GlucoseMeasurementContext = 10804
    GN = 4375
    GNSS = 4405
    GNSSServer = 4406
    GustFactor = 10868
    Handsfree = 4382
    HandsfreeAudioGateway = 4383
    HardcopyCableReplacement = 4389
    HardcopyControlChannel = 18
    HardcopyDataChannel = 20
    HardcopyNotification = 22
    HardwareRevisionString = 10791
    HCRPrint = 4390
    HCRScan = 4391
    HDP = 5120
    HDPSink = 5122
    HDPSource = 5121
    Headset = 4360
    HeadsetAG = 4370
    HeadsetHS = 4401
    HealthThermometer = 6153
    HeartRate = 6157
    HeartRateControlPoint = 10809
    HeartRateMax = 10893
    HeartRateMeasurement = 10807
    HeatIndex = 10874
    Height = 10894
    HIDControlPoint = 10828
    HIDInformation = 10826
    Hidp = 17
    HipCircumference = 10895
    Http = 12
    HumanInterfaceDevice = 6162
    HumanInterfaceDeviceService = 4388
    Humidity = 10863
    IEEE1107320601RegulatoryCertificationDataList = 10794
    ImagingAutomaticArchive = 4380
    ImagingReferenceObjects = 4381
    ImagingResponder = 4379
    ImmediateAlert = 6146
    IntermediateCuffPressure = 10806
    IntermediateTemperature = 10782
    Ip = 9
    IrMCSync = 4356
    IrMCSyncCommand = 4359
    Irradiance = 10871
    L2cap = 256
    LANAccessUsingPPP = 4354
    Language = 10914
    LastName = 10896
    LinkLoss = 6147
    LNControlPoint = 10859
    LNFeature = 10858
    LocalTimeInformation = 10767
    LocationAndNavigation = 6169
    LocationAndSpeed = 10855
    MagneticDeclination = 10796
    MagneticFluxDensity2D = 10912
    MagneticFluxDensity3D = 10913
    ManufacturerNameString = 10793
    MaximumRecommendedHeartRate = 10897
    McapControlChannel = 30
    McapDataChannel = 31
    MeasurementInterval = 10785
    MessageAccessProfile = 4404
    MessageAccessServer = 4402
    MessageNotificationServer = 4403
    ModelNumberString = 10788
    MPSProfile = 4410
    MPSService = 4411
    NAP = 4374
    Navigation = 10856
    NewAlert = 10822
    NextDSTChangeService = 6151
    Obex = 8
    OBEXFileTransfer = 4358
    ObexObjectPush = 4357
    PANU = 4373
    PeripheralPreferredConnectionParameters = 10756
    PeripheralPrivacyFlag = 10754
    PhoneAlertStatusService = 6158
    PhonebookAccess = 4400
    PhonebookAccessPCE = 4398
    PhonebookAccessPSE = 4399
    PnPID = 10832
    PnPInformation = 4608
    PollenConcentration = 10869
    PositionQuality = 10857
    Pressure = 10861
    PrintingStatus = 4387
    ProtocolMode = 10830
    PublicBrowseGroup = 4098
    Rainfall = 10872
    ReconnectionAddress = 10755
    RecordAccessControlPoint = 10834
    ReferencePrinting = 4377
    ReferenceTimeInformation = 10772
    ReferenceTimeUpdateService = 6150
    ReflectedUI = 4385
    Report = 10829
    ReportMap = 10827
    ReportReference = 10504
    RestingHeartRate = 10898
    Rfcomm = 3
    RingerControlPoint = 10816
    RingerSetting = 10817
    RSCFeature = 10836
    RSCMeasurement = 10835
    RunningSpeedAndCadence = 6164
    ScanIntervalWindow = 10831
    ScanParameters = 6163
    ScanRefresh = 10801
    SCControlPoint = 10837
    Sdp = 1
    SensorLocation = 10845
    SerialNumberString = 10789
    SerialPort = 4353
    ServerCharacteristicConfiguration = 10499
    ServiceChanged = 10757
    ServiceDiscoveryServer = 4096
    SIMAccess = 4397
    SoftwareRevisionString = 10792
    SportTypeForAerobicAnaerobicThresholds = 10899
    SupportedNewAlertCategory = 10823
    SupportedUnreadAlertCategory = 10824
    Synchronization3D = 4409
    SystemID = 10787
    Tcp = 4
    TcsAt = 6
    TcsBin = 5
    Temperature = 10862
    TemperatureMeasurement = 10780
    TemperatureType = 10781
    ThreeZoneHeartRateLimits = 10900
    TimeAccuracy = 10770
    TimeSource = 10771
    TimeUpdateControlPoint = 10774
    TimeUpdateState = 10775
    TimeWithDST = 10769
    TimeZone = 10766
    TrueWindDirection = 10865
    TrueWindSpeed = 10864
    TwoZoneHeartRateLimits = 10901
    TxPower = 6148
    TxPowerLevel = 10759
    UdiCPlain = 29
    Udp = 2
    UnknownDescriptorType = 0
    UnreadAlertStatus = 10821
    Upnp = 16
    UserControlPoint = 10911
    UserData = 6172
    UserIndex = 10906
    UVIndex = 10870
    ValidRange = 10502
    VideoDistribution = 4869
    VideoSink = 4868
    VideoSource = 4867
    VO2Max = 10902
    WaistCircumference = 10903
    Weight = 10904
    WeightMeasurement = 10909
    WeightScale = 6173
    WeightScaleFeature = 10910
    WindChill = 10873
    Wsp = 14
    __hash__ = None


class QLowEnergyAdvertisingData(__sip.wrapper):
    """
    QLowEnergyAdvertisingData()
    QLowEnergyAdvertisingData(other: QLowEnergyAdvertisingData)
    """
    def discoverability(self): # real signature unknown; restored from __doc__
        """ discoverability(self) -> QLowEnergyAdvertisingData.Discoverability """
        pass

    def includePowerLevel(self): # real signature unknown; restored from __doc__
        """ includePowerLevel(self) -> bool """
        return False

    def invalidManufacturerId(self): # real signature unknown; restored from __doc__
        """ invalidManufacturerId() -> int """
        return 0

    def localName(self): # real signature unknown; restored from __doc__
        """ localName(self) -> str """
        return ""

    def manufacturerData(self): # real signature unknown; restored from __doc__
        """ manufacturerData(self) -> QByteArray """
        pass

    def manufacturerId(self): # real signature unknown; restored from __doc__
        """ manufacturerId(self) -> int """
        return 0

    def rawData(self): # real signature unknown; restored from __doc__
        """ rawData(self) -> QByteArray """
        pass

    def services(self): # real signature unknown; restored from __doc__
        """ services(self) -> List[QBluetoothUuid] """
        return []

    def setDiscoverability(self, mode): # real signature unknown; restored from __doc__
        """ setDiscoverability(self, mode: QLowEnergyAdvertisingData.Discoverability) """
        pass

    def setIncludePowerLevel(self, doInclude): # real signature unknown; restored from __doc__
        """ setIncludePowerLevel(self, doInclude: bool) """
        pass

    def setLocalName(self, name, p_str=None): # real signature unknown; restored from __doc__
        """ setLocalName(self, name: Optional[str]) """
        pass

    def setManufacturerData(self, id, data, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ setManufacturerData(self, id: int, data: Union[QByteArray, bytes, bytearray]) """
        pass

    def setRawData(self, data, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ setRawData(self, data: Union[QByteArray, bytes, bytearray]) """
        pass

    def setServices(self, services, QBluetoothUuid=None): # real signature unknown; restored from __doc__
        """ setServices(self, services: Iterable[QBluetoothUuid]) """
        pass

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: QLowEnergyAdvertisingData) """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, other=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    DiscoverabilityGeneral = 2
    DiscoverabilityLimited = 1
    DiscoverabilityNone = 0
    __hash__ = None


class QLowEnergyAdvertisingParameters(__sip.wrapper):
    """
    QLowEnergyAdvertisingParameters()
    QLowEnergyAdvertisingParameters(other: QLowEnergyAdvertisingParameters)
    """
    def filterPolicy(self): # real signature unknown; restored from __doc__
        """ filterPolicy(self) -> QLowEnergyAdvertisingParameters.FilterPolicy """
        pass

    def maximumInterval(self): # real signature unknown; restored from __doc__
        """ maximumInterval(self) -> int """
        return 0

    def minimumInterval(self): # real signature unknown; restored from __doc__
        """ minimumInterval(self) -> int """
        return 0

    def mode(self): # real signature unknown; restored from __doc__
        """ mode(self) -> QLowEnergyAdvertisingParameters.Mode """
        pass

    def setInterval(self, minimum, maximum): # real signature unknown; restored from __doc__
        """ setInterval(self, minimum: int, maximum: int) """
        pass

    def setMode(self, mode): # real signature unknown; restored from __doc__
        """ setMode(self, mode: QLowEnergyAdvertisingParameters.Mode) """
        pass

    def setWhiteList(self, whiteList, QLowEnergyAdvertisingParameters_AddressInfo=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setWhiteList(self, whiteList: Iterable[QLowEnergyAdvertisingParameters.AddressInfo], policy: QLowEnergyAdvertisingParameters.FilterPolicy) """
        pass

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: QLowEnergyAdvertisingParameters) """
        pass

    def whiteList(self): # real signature unknown; restored from __doc__
        """ whiteList(self) -> List[QLowEnergyAdvertisingParameters.AddressInfo] """
        return []

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, other=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    AdvInd = 0
    AdvNonConnInd = 3
    AdvScanInd = 2
    IgnoreWhiteList = 0
    UseWhiteListForConnecting = 2
    UseWhiteListForScanning = 1
    UseWhiteListForScanningAndConnecting = 3
    __hash__ = None


class QLowEnergyCharacteristic(__sip.wrapper):
    """
    QLowEnergyCharacteristic()
    QLowEnergyCharacteristic(other: QLowEnergyCharacteristic)
    """
    def descriptor(self, uuid): # real signature unknown; restored from __doc__
        """ descriptor(self, uuid: QBluetoothUuid) -> QLowEnergyDescriptor """
        return QLowEnergyDescriptor

    def descriptors(self): # real signature unknown; restored from __doc__
        """ descriptors(self) -> List[QLowEnergyDescriptor] """
        return []

    def handle(self): # real signature unknown; restored from __doc__
        """ handle(self) -> int """
        return 0

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def name(self): # real signature unknown; restored from __doc__
        """ name(self) -> str """
        return ""

    def properties(self): # real signature unknown; restored from __doc__
        """ properties(self) -> QLowEnergyCharacteristic.PropertyTypes """
        pass

    def uuid(self): # real signature unknown; restored from __doc__
        """ uuid(self) -> QBluetoothUuid """
        return QBluetoothUuid

    def value(self): # real signature unknown; restored from __doc__
        """ value(self) -> QByteArray """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, other=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    Broadcasting = 1
    ExtendedProperty = 128
    Indicate = 32
    Notify = 16
    Read = 2
    Unknown = 0
    Write = 8
    WriteNoResponse = 4
    WriteSigned = 64
    __hash__ = None


class QLowEnergyCharacteristicData(__sip.wrapper):
    """
    QLowEnergyCharacteristicData()
    QLowEnergyCharacteristicData(other: QLowEnergyCharacteristicData)
    """
    def addDescriptor(self, descriptor): # real signature unknown; restored from __doc__
        """ addDescriptor(self, descriptor: QLowEnergyDescriptorData) """
        pass

    def descriptors(self): # real signature unknown; restored from __doc__
        """ descriptors(self) -> List[QLowEnergyDescriptorData] """
        return []

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def maximumValueLength(self): # real signature unknown; restored from __doc__
        """ maximumValueLength(self) -> int """
        return 0

    def minimumValueLength(self): # real signature unknown; restored from __doc__
        """ minimumValueLength(self) -> int """
        return 0

    def properties(self): # real signature unknown; restored from __doc__
        """ properties(self) -> QLowEnergyCharacteristic.PropertyTypes """
        pass

    def readConstraints(self): # real signature unknown; restored from __doc__
        """ readConstraints(self) -> QBluetooth.AttAccessConstraints """
        pass

    def setDescriptors(self, descriptors, QLowEnergyDescriptorData=None): # real signature unknown; restored from __doc__
        """ setDescriptors(self, descriptors: Iterable[QLowEnergyDescriptorData]) """
        pass

    def setProperties(self, properties, QLowEnergyCharacteristic_PropertyTypes=None, QLowEnergyCharacteristic_PropertyType=None): # real signature unknown; restored from __doc__
        """ setProperties(self, properties: Union[QLowEnergyCharacteristic.PropertyTypes, QLowEnergyCharacteristic.PropertyType]) """
        pass

    def setReadConstraints(self, constraints, QBluetooth_AttAccessConstraints=None, QBluetooth_AttAccessConstraint=None): # real signature unknown; restored from __doc__
        """ setReadConstraints(self, constraints: Union[QBluetooth.AttAccessConstraints, QBluetooth.AttAccessConstraint]) """
        pass

    def setUuid(self, uuid): # real signature unknown; restored from __doc__
        """ setUuid(self, uuid: QBluetoothUuid) """
        pass

    def setValue(self, value, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ setValue(self, value: Union[QByteArray, bytes, bytearray]) """
        pass

    def setValueLength(self, minimum, maximum): # real signature unknown; restored from __doc__
        """ setValueLength(self, minimum: int, maximum: int) """
        pass

    def setWriteConstraints(self, constraints, QBluetooth_AttAccessConstraints=None, QBluetooth_AttAccessConstraint=None): # real signature unknown; restored from __doc__
        """ setWriteConstraints(self, constraints: Union[QBluetooth.AttAccessConstraints, QBluetooth.AttAccessConstraint]) """
        pass

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: QLowEnergyCharacteristicData) """
        pass

    def uuid(self): # real signature unknown; restored from __doc__
        """ uuid(self) -> QBluetoothUuid """
        return QBluetoothUuid

    def value(self): # real signature unknown; restored from __doc__
        """ value(self) -> QByteArray """
        pass

    def writeConstraints(self): # real signature unknown; restored from __doc__
        """ writeConstraints(self) -> QBluetooth.AttAccessConstraints """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, other=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __hash__ = None


class QLowEnergyConnectionParameters(__sip.wrapper):
    """
    QLowEnergyConnectionParameters()
    QLowEnergyConnectionParameters(other: QLowEnergyConnectionParameters)
    """
    def latency(self): # real signature unknown; restored from __doc__
        """ latency(self) -> int """
        return 0

    def maximumInterval(self): # real signature unknown; restored from __doc__
        """ maximumInterval(self) -> float """
        return 0.0

    def minimumInterval(self): # real signature unknown; restored from __doc__
        """ minimumInterval(self) -> float """
        return 0.0

    def setIntervalRange(self, minimum, maximum): # real signature unknown; restored from __doc__
        """ setIntervalRange(self, minimum: float, maximum: float) """
        pass

    def setLatency(self, latency): # real signature unknown; restored from __doc__
        """ setLatency(self, latency: int) """
        pass

    def setSupervisionTimeout(self, timeout): # real signature unknown; restored from __doc__
        """ setSupervisionTimeout(self, timeout: int) """
        pass

    def supervisionTimeout(self): # real signature unknown; restored from __doc__
        """ supervisionTimeout(self) -> int """
        return 0

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: QLowEnergyConnectionParameters) """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, other=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __hash__ = None


class QLowEnergyController(__PyQt5_QtCore.QObject):
    """
    QLowEnergyController(remoteDevice: QBluetoothDeviceInfo, parent: Optional[QObject] = None)
    QLowEnergyController(remoteDevice: QBluetoothAddress, parent: Optional[QObject] = None)
    QLowEnergyController(remoteDevice: QBluetoothAddress, localDevice: QBluetoothAddress, parent: Optional[QObject] = None)
    """
    def addService(self, service, parent, QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ addService(self, service: QLowEnergyServiceData, parent: Optional[QObject] = None) -> Optional[QLowEnergyService] """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connected(self, *args, **kwargs): # real signature unknown
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

    def connectionUpdated(self, *args, **kwargs): # real signature unknown
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

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def connectToDevice(self): # real signature unknown; restored from __doc__
        """ connectToDevice(self) """
        pass

    def createCentral(self, remoteDevice, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        createCentral(remoteDevice: QBluetoothDeviceInfo, parent: Optional[QObject] = None) -> Optional[QLowEnergyController]
        createCentral(remoteDevice: QBluetoothAddress, localDevice: QBluetoothAddress, parent: Optional[QObject] = None) -> Optional[QLowEnergyController]
        """
        pass

    def createPeripheral(self, parent, QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ createPeripheral(parent: Optional[QObject] = None) -> Optional[QLowEnergyController] """
        pass

    def createServiceObject(self, service, parent, QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ createServiceObject(self, service: QBluetoothUuid, parent: Optional[QObject] = None) -> Optional[QLowEnergyService] """
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnected(self, *args, **kwargs): # real signature unknown
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

    def disconnectFromDevice(self): # real signature unknown; restored from __doc__
        """ disconnectFromDevice(self) """
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def discoverServices(self): # real signature unknown; restored from __doc__
        """ discoverServices(self) """
        pass

    def discoveryFinished(self, *args, **kwargs): # real signature unknown
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

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def localAddress(self): # real signature unknown; restored from __doc__
        """ localAddress(self) -> QBluetoothAddress """
        return QBluetoothAddress

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def remoteAddress(self): # real signature unknown; restored from __doc__
        """ remoteAddress(self) -> QBluetoothAddress """
        return QBluetoothAddress

    def remoteAddressType(self): # real signature unknown; restored from __doc__
        """ remoteAddressType(self) -> QLowEnergyController.RemoteAddressType """
        pass

    def remoteDeviceUuid(self): # real signature unknown; restored from __doc__
        """ remoteDeviceUuid(self) -> QBluetoothUuid """
        return QBluetoothUuid

    def remoteName(self): # real signature unknown; restored from __doc__
        """ remoteName(self) -> str """
        return ""

    def requestConnectionUpdate(self, parameters): # real signature unknown; restored from __doc__
        """ requestConnectionUpdate(self, parameters: QLowEnergyConnectionParameters) """
        pass

    def role(self): # real signature unknown; restored from __doc__
        """ role(self) -> QLowEnergyController.Role """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def serviceDiscovered(self, *args, **kwargs): # real signature unknown
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

    def services(self): # real signature unknown; restored from __doc__
        """ services(self) -> List[QBluetoothUuid] """
        return []

    def setRemoteAddressType(self, type): # real signature unknown; restored from __doc__
        """ setRemoteAddressType(self, type: QLowEnergyController.RemoteAddressType) """
        pass

    def startAdvertising(self, parameters, advertisingData, scanResponseData=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ startAdvertising(self, parameters: QLowEnergyAdvertisingParameters, advertisingData: QLowEnergyAdvertisingData, scanResponseData: QLowEnergyAdvertisingData = QLowEnergyAdvertisingData()) """
        pass

    def state(self): # real signature unknown; restored from __doc__
        """ state(self) -> QLowEnergyController.ControllerState """
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

    def stopAdvertising(self): # real signature unknown; restored from __doc__
        """ stopAdvertising(self) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, remoteDevice, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    AdvertisingError = 6
    AdvertisingState = 6
    AuthorizationError = 8
    CentralRole = 0
    ClosingState = 5
    ConnectedState = 2
    ConnectingState = 1
    ConnectionError = 5
    DiscoveredState = 4
    DiscoveringState = 3
    InvalidBluetoothAdapterError = 4
    NetworkError = 3
    NoError = 0
    PeripheralRole = 1
    PublicAddress = 0
    RandomAddress = 1
    RemoteHostClosedError = 7
    UnconnectedState = 0
    UnknownError = 1
    UnknownRemoteDeviceError = 2


class QLowEnergyDescriptor(__sip.wrapper):
    """
    QLowEnergyDescriptor()
    QLowEnergyDescriptor(other: QLowEnergyDescriptor)
    """
    def handle(self): # real signature unknown; restored from __doc__
        """ handle(self) -> int """
        return 0

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def name(self): # real signature unknown; restored from __doc__
        """ name(self) -> str """
        return ""

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> QBluetoothUuid.DescriptorType """
        pass

    def uuid(self): # real signature unknown; restored from __doc__
        """ uuid(self) -> QBluetoothUuid """
        return QBluetoothUuid

    def value(self): # real signature unknown; restored from __doc__
        """ value(self) -> QByteArray """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, other=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __hash__ = None


class QLowEnergyDescriptorData(__sip.wrapper):
    """
    QLowEnergyDescriptorData()
    QLowEnergyDescriptorData(uuid: QBluetoothUuid, value: Union[QByteArray, bytes, bytearray])
    QLowEnergyDescriptorData(other: QLowEnergyDescriptorData)
    """
    def isReadable(self): # real signature unknown; restored from __doc__
        """ isReadable(self) -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def isWritable(self): # real signature unknown; restored from __doc__
        """ isWritable(self) -> bool """
        return False

    def readConstraints(self): # real signature unknown; restored from __doc__
        """ readConstraints(self) -> QBluetooth.AttAccessConstraints """
        pass

    def setReadPermissions(self, readable, constraints, QBluetooth_AttAccessConstraints=None, QBluetooth_AttAccessConstraint=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setReadPermissions(self, readable: bool, constraints: Union[QBluetooth.AttAccessConstraints, QBluetooth.AttAccessConstraint] = QBluetooth.AttAccessConstraints()) """
        pass

    def setUuid(self, uuid): # real signature unknown; restored from __doc__
        """ setUuid(self, uuid: QBluetoothUuid) """
        pass

    def setValue(self, value, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ setValue(self, value: Union[QByteArray, bytes, bytearray]) """
        pass

    def setWritePermissions(self, writable, constraints, QBluetooth_AttAccessConstraints=None, QBluetooth_AttAccessConstraint=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setWritePermissions(self, writable: bool, constraints: Union[QBluetooth.AttAccessConstraints, QBluetooth.AttAccessConstraint] = QBluetooth.AttAccessConstraints()) """
        pass

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: QLowEnergyDescriptorData) """
        pass

    def uuid(self): # real signature unknown; restored from __doc__
        """ uuid(self) -> QBluetoothUuid """
        return QBluetoothUuid

    def value(self): # real signature unknown; restored from __doc__
        """ value(self) -> QByteArray """
        pass

    def writeConstraints(self): # real signature unknown; restored from __doc__
        """ writeConstraints(self) -> QBluetooth.AttAccessConstraints """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __hash__ = None


class QLowEnergyService(__PyQt5_QtCore.QObject):
    # no doc
    def characteristic(self, uuid): # real signature unknown; restored from __doc__
        """ characteristic(self, uuid: QBluetoothUuid) -> QLowEnergyCharacteristic """
        return QLowEnergyCharacteristic

    def characteristicChanged(self, *args, **kwargs): # real signature unknown
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

    def characteristicRead(self, *args, **kwargs): # real signature unknown
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

    def characteristics(self): # real signature unknown; restored from __doc__
        """ characteristics(self) -> List[QLowEnergyCharacteristic] """
        return []

    def characteristicWritten(self, *args, **kwargs): # real signature unknown
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

    def contains(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        contains(self, characteristic: QLowEnergyCharacteristic) -> bool
        contains(self, descriptor: QLowEnergyDescriptor) -> bool
        """
        return False

    def descriptorRead(self, *args, **kwargs): # real signature unknown
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

    def descriptorWritten(self, *args, **kwargs): # real signature unknown
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

    def discoverDetails(self): # real signature unknown; restored from __doc__
        """ discoverDetails(self) """
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

    def includedServices(self): # real signature unknown; restored from __doc__
        """ includedServices(self) -> List[QBluetoothUuid] """
        return []

    def readCharacteristic(self, characteristic): # real signature unknown; restored from __doc__
        """ readCharacteristic(self, characteristic: QLowEnergyCharacteristic) """
        pass

    def readDescriptor(self, descriptor): # real signature unknown; restored from __doc__
        """ readDescriptor(self, descriptor: QLowEnergyDescriptor) """
        pass

    def serviceName(self): # real signature unknown; restored from __doc__
        """ serviceName(self) -> str """
        return ""

    def serviceUuid(self): # real signature unknown; restored from __doc__
        """ serviceUuid(self) -> QBluetoothUuid """
        return QBluetoothUuid

    def state(self): # real signature unknown; restored from __doc__
        """ state(self) -> QLowEnergyService.ServiceState """
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

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> QLowEnergyService.ServiceTypes """
        pass

    def writeCharacteristic(self, characteristic, newValue, QByteArray=None, bytes=None, bytearray=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ writeCharacteristic(self, characteristic: QLowEnergyCharacteristic, newValue: Union[QByteArray, bytes, bytearray], mode: QLowEnergyService.WriteMode = QLowEnergyService.WriteWithResponse) """
        pass

    def writeDescriptor(self, descriptor, newValue, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ writeDescriptor(self, descriptor: QLowEnergyDescriptor, newValue: Union[QByteArray, bytes, bytearray]) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    CharacteristicReadError = 5
    CharacteristicWriteError = 2
    DescriptorReadError = 6
    DescriptorWriteError = 3
    DiscoveringServices = 2
    DiscoveryRequired = 1
    IncludedService = 2
    InvalidService = 0
    LocalService = 4
    NoError = 0
    OperationError = 1
    PrimaryService = 1
    ServiceDiscovered = 3
    UnknownError = 4
    WriteSigned = 2
    WriteWithoutResponse = 1
    WriteWithResponse = 0


class QLowEnergyServiceData(__sip.wrapper):
    """
    QLowEnergyServiceData()
    QLowEnergyServiceData(other: QLowEnergyServiceData)
    """
    def addCharacteristic(self, characteristic): # real signature unknown; restored from __doc__
        """ addCharacteristic(self, characteristic: QLowEnergyCharacteristicData) """
        pass

    def addIncludedService(self, service, QLowEnergyService=None): # real signature unknown; restored from __doc__
        """ addIncludedService(self, service: Optional[QLowEnergyService]) """
        pass

    def characteristics(self): # real signature unknown; restored from __doc__
        """ characteristics(self) -> List[QLowEnergyCharacteristicData] """
        return []

    def includedServices(self): # real signature unknown; restored from __doc__
        """ includedServices(self) -> List[QLowEnergyService] """
        return []

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def setCharacteristics(self, characteristics, QLowEnergyCharacteristicData=None): # real signature unknown; restored from __doc__
        """ setCharacteristics(self, characteristics: Iterable[QLowEnergyCharacteristicData]) """
        pass

    def setIncludedServices(self, services, QLowEnergyService=None): # real signature unknown; restored from __doc__
        """ setIncludedServices(self, services: Iterable[QLowEnergyService]) """
        pass

    def setType(self, type): # real signature unknown; restored from __doc__
        """ setType(self, type: QLowEnergyServiceData.ServiceType) """
        pass

    def setUuid(self, uuid): # real signature unknown; restored from __doc__
        """ setUuid(self, uuid: QBluetoothUuid) """
        pass

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: QLowEnergyServiceData) """
        pass

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> QLowEnergyServiceData.ServiceType """
        pass

    def uuid(self): # real signature unknown; restored from __doc__
        """ uuid(self) -> QBluetoothUuid """
        return QBluetoothUuid

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, other=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    ServiceTypePrimary = 10240
    ServiceTypeSecondary = 10241
    __hash__ = None


# variables with complex values



