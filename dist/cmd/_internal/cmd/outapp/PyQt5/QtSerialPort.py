# encoding: utf-8
# module PyQt5.QtSerialPort
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtSerialPort.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


# no functions
# classes

class QSerialPort(__PyQt5_QtCore.QIODevice):
    """
    QSerialPort(parent: Optional[QObject] = None)
    QSerialPort(name: Optional[str], parent: Optional[QObject] = None)
    QSerialPort(info: QSerialPortInfo, parent: Optional[QObject] = None)
    """
    def atEnd(self): # real signature unknown; restored from __doc__
        """ atEnd(self) -> bool """
        return False

    def baudRate(self, dir, QSerialPort_Directions=None, QSerialPort_Direction=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ baudRate(self, dir: Union[QSerialPort.Directions, QSerialPort.Direction] = QSerialPort.AllDirections) -> int """
        pass

    def baudRateChanged(self, *args, **kwargs): # real signature unknown
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

    def breakEnabledChanged(self, *args, **kwargs): # real signature unknown
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

    def clear(self, dir, QSerialPort_Directions=None, QSerialPort_Direction=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ clear(self, dir: Union[QSerialPort.Directions, QSerialPort.Direction] = QSerialPort.AllDirections) -> bool """
        pass

    def clearError(self): # real signature unknown; restored from __doc__
        """ clearError(self) """
        pass

    def close(self): # real signature unknown; restored from __doc__
        """ close(self) """
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dataBits(self): # real signature unknown; restored from __doc__
        """ dataBits(self) -> QSerialPort.DataBits """
        pass

    def dataBitsChanged(self, *args, **kwargs): # real signature unknown
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

    def dataErrorPolicy(self): # real signature unknown; restored from __doc__
        """ dataErrorPolicy(self) -> QSerialPort.DataErrorPolicy """
        pass

    def dataErrorPolicyChanged(self, *args, **kwargs): # real signature unknown
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

    def dataTerminalReadyChanged(self, *args, **kwargs): # real signature unknown
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

    def flowControl(self): # real signature unknown; restored from __doc__
        """ flowControl(self) -> QSerialPort.FlowControl """
        pass

    def flowControlChanged(self, *args, **kwargs): # real signature unknown
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

    def flush(self): # real signature unknown; restored from __doc__
        """ flush(self) -> bool """
        return False

    def handle(self): # real signature unknown; restored from __doc__
        """ handle(self) -> Optional[PyQt5.sip.voidptr] """
        pass

    def isBreakEnabled(self): # real signature unknown; restored from __doc__
        """ isBreakEnabled(self) -> bool """
        return False

    def isDataTerminalReady(self): # real signature unknown; restored from __doc__
        """ isDataTerminalReady(self) -> bool """
        return False

    def isRequestToSend(self): # real signature unknown; restored from __doc__
        """ isRequestToSend(self) -> bool """
        return False

    def isSequential(self): # real signature unknown; restored from __doc__
        """ isSequential(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def open(self, mode, QIODevice_OpenMode=None, QIODevice_OpenModeFlag=None): # real signature unknown; restored from __doc__
        """ open(self, mode: Union[QIODevice.OpenMode, QIODevice.OpenModeFlag]) -> bool """
        return False

    def parity(self): # real signature unknown; restored from __doc__
        """ parity(self) -> QSerialPort.Parity """
        pass

    def parityChanged(self, *args, **kwargs): # real signature unknown
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

    def pinoutSignals(self): # real signature unknown; restored from __doc__
        """ pinoutSignals(self) -> QSerialPort.PinoutSignals """
        pass

    def portName(self): # real signature unknown; restored from __doc__
        """ portName(self) -> str """
        return ""

    def readBufferSize(self): # real signature unknown; restored from __doc__
        """ readBufferSize(self) -> int """
        return 0

    def readData(self, maxlen): # real signature unknown; restored from __doc__
        """ readData(self, maxlen: int) -> bytes """
        return b""

    def readLineData(self, maxlen): # real signature unknown; restored from __doc__
        """ readLineData(self, maxlen: int) -> bytes """
        return b""

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def requestToSendChanged(self, *args, **kwargs): # real signature unknown
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

    def sendBreak(self, duration=0): # real signature unknown; restored from __doc__
        """ sendBreak(self, duration: int = 0) -> bool """
        return False

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setBaudRate(self, baudRate, dir, QSerialPort_Directions=None, QSerialPort_Direction=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setBaudRate(self, baudRate: int, dir: Union[QSerialPort.Directions, QSerialPort.Direction] = QSerialPort.AllDirections) -> bool """
        pass

    def setBreakEnabled(self, enabled=True): # real signature unknown; restored from __doc__
        """ setBreakEnabled(self, enabled: bool = True) -> bool """
        return False

    def setDataBits(self, dataBits): # real signature unknown; restored from __doc__
        """ setDataBits(self, dataBits: QSerialPort.DataBits) -> bool """
        return False

    def setDataErrorPolicy(self, policy=None): # real signature unknown; restored from __doc__
        """ setDataErrorPolicy(self, policy: QSerialPort.DataErrorPolicy = QSerialPort.IgnorePolicy) -> bool """
        return False

    def setDataTerminalReady(self, set): # real signature unknown; restored from __doc__
        """ setDataTerminalReady(self, set: bool) -> bool """
        return False

    def setErrorString(self, *args, **kwargs): # real signature unknown
        pass

    def setFlowControl(self, flow): # real signature unknown; restored from __doc__
        """ setFlowControl(self, flow: QSerialPort.FlowControl) -> bool """
        return False

    def setOpenMode(self, *args, **kwargs): # real signature unknown
        pass

    def setParity(self, parity): # real signature unknown; restored from __doc__
        """ setParity(self, parity: QSerialPort.Parity) -> bool """
        return False

    def setPort(self, info): # real signature unknown; restored from __doc__
        """ setPort(self, info: QSerialPortInfo) """
        pass

    def setPortName(self, name, p_str=None): # real signature unknown; restored from __doc__
        """ setPortName(self, name: Optional[str]) """
        pass

    def setReadBufferSize(self, size): # real signature unknown; restored from __doc__
        """ setReadBufferSize(self, size: int) """
        pass

    def setRequestToSend(self, set): # real signature unknown; restored from __doc__
        """ setRequestToSend(self, set: bool) -> bool """
        return False

    def setSettingsRestoredOnClose(self, restore): # real signature unknown; restored from __doc__
        """ setSettingsRestoredOnClose(self, restore: bool) """
        pass

    def setStopBits(self, stopBits): # real signature unknown; restored from __doc__
        """ setStopBits(self, stopBits: QSerialPort.StopBits) -> bool """
        return False

    def settingsRestoredOnClose(self): # real signature unknown; restored from __doc__
        """ settingsRestoredOnClose(self) -> bool """
        return False

    def settingsRestoredOnCloseChanged(self, *args, **kwargs): # real signature unknown
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

    def stopBits(self): # real signature unknown; restored from __doc__
        """ stopBits(self) -> QSerialPort.StopBits """
        pass

    def stopBitsChanged(self, *args, **kwargs): # real signature unknown
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

    def waitForBytesWritten(self, msecs=30000): # real signature unknown; restored from __doc__
        """ waitForBytesWritten(self, msecs: int = 30000) -> bool """
        return False

    def waitForReadyRead(self, msecs=30000): # real signature unknown; restored from __doc__
        """ waitForReadyRead(self, msecs: int = 30000) -> bool """
        return False

    def writeData(self, data, PyQt5_sip_array=None, bytes=None): # real signature unknown; restored from __doc__
        """ writeData(self, data: Optional[PyQt5.sip.array[bytes]]) -> int """
        return 0

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    AllDirections = 3
    Baud115200 = 115200
    Baud1200 = 1200
    Baud19200 = 19200
    Baud2400 = 2400
    Baud38400 = 38400
    Baud4800 = 4800
    Baud57600 = 57600
    Baud9600 = 9600
    BreakConditionError = 6
    ClearToSendSignal = 128
    Data5 = 5
    Data6 = 6
    Data7 = 7
    Data8 = 8
    DataCarrierDetectSignal = 8
    DataSetReadySignal = 16
    DataTerminalReadySignal = 4
    DeviceNotFoundError = 1
    EvenParity = 2
    FramingError = 5
    HardwareControl = 1
    IgnorePolicy = 2
    Input = 1
    MarkParity = 5
    NoError = 0
    NoFlowControl = 0
    NoParity = 0
    NoSignal = 0
    NotOpenError = 13
    OddParity = 3
    OneAndHalfStop = 3
    OneStop = 1
    OpenError = 3
    Output = 2
    ParityError = 4
    PassZeroPolicy = 1
    PermissionError = 2
    ReadError = 8
    ReceivedDataSignal = 2
    RequestToSendSignal = 64
    ResourceError = 9
    RingIndicatorSignal = 32
    SecondaryReceivedDataSignal = 512
    SecondaryTransmittedDataSignal = 256
    SkipPolicy = 0
    SoftwareControl = 2
    SpaceParity = 4
    StopReceivingPolicy = 3
    TimeoutError = 12
    TransmittedDataSignal = 1
    TwoStop = 2
    UnknownBaud = -1
    UnknownDataBits = -1
    UnknownError = 11
    UnknownFlowControl = -1
    UnknownParity = -1
    UnknownPolicy = -1
    UnknownStopBits = -1
    UnsupportedOperationError = 10
    WriteError = 7


class QSerialPortInfo(__sip.simplewrapper):
    """
    QSerialPortInfo()
    QSerialPortInfo(port: QSerialPort)
    QSerialPortInfo(name: Optional[str])
    QSerialPortInfo(other: QSerialPortInfo)
    """
    def availablePorts(self): # real signature unknown; restored from __doc__
        """ availablePorts() -> List[QSerialPortInfo] """
        return []

    def description(self): # real signature unknown; restored from __doc__
        """ description(self) -> str """
        return ""

    def hasProductIdentifier(self): # real signature unknown; restored from __doc__
        """ hasProductIdentifier(self) -> bool """
        return False

    def hasVendorIdentifier(self): # real signature unknown; restored from __doc__
        """ hasVendorIdentifier(self) -> bool """
        return False

    def isBusy(self): # real signature unknown; restored from __doc__
        """ isBusy(self) -> bool """
        return False

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def manufacturer(self): # real signature unknown; restored from __doc__
        """ manufacturer(self) -> str """
        return ""

    def portName(self): # real signature unknown; restored from __doc__
        """ portName(self) -> str """
        return ""

    def productIdentifier(self): # real signature unknown; restored from __doc__
        """ productIdentifier(self) -> int """
        return 0

    def serialNumber(self): # real signature unknown; restored from __doc__
        """ serialNumber(self) -> str """
        return ""

    def standardBaudRates(self): # real signature unknown; restored from __doc__
        """ standardBaudRates() -> List[int] """
        return []

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: QSerialPortInfo) """
        pass

    def systemLocation(self): # real signature unknown; restored from __doc__
        """ systemLocation(self) -> str """
        return ""

    def vendorIdentifier(self): # real signature unknown; restored from __doc__
        """ vendorIdentifier(self) -> int """
        return 0

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



# variables with complex values



