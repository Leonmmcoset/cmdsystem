# encoding: utf-8
# module PyQt5.QtNetwork
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtNetwork.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QAbstractSocket(__PyQt5_QtCore.QIODevice):
    """ QAbstractSocket(socketType: QAbstractSocket.SocketType, parent: Optional[QObject]) """
    def abort(self): # real signature unknown; restored from __doc__
        """ abort(self) """
        pass

    def atEnd(self): # real signature unknown; restored from __doc__
        """ atEnd(self) -> bool """
        return False

    def bind(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        bind(self, address: Union[QHostAddress, QHostAddress.SpecialAddress], port: int = 0, mode: Union[QAbstractSocket.BindMode, QAbstractSocket.BindFlag] = QAbstractSocket.DefaultForPlatform) -> bool
        bind(self, port: int = 0, mode: Union[QAbstractSocket.BindMode, QAbstractSocket.BindFlag] = QAbstractSocket.DefaultForPlatform) -> bool
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

    def connectToHost(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        connectToHost(self, hostName: Optional[str], port: int, mode: Union[QIODevice.OpenMode, QIODevice.OpenModeFlag] = QIODevice.ReadWrite, protocol: QAbstractSocket.NetworkLayerProtocol = QAbstractSocket.AnyIPProtocol)
        connectToHost(self, address: Union[QHostAddress, QHostAddress.SpecialAddress], port: int, mode: Union[QIODevice.OpenMode, QIODevice.OpenModeFlag] = QIODevice.ReadWrite)
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

    def disconnectFromHost(self): # real signature unknown; restored from __doc__
        """ disconnectFromHost(self) """
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

    def flush(self): # real signature unknown; restored from __doc__
        """ flush(self) -> bool """
        return False

    def hostFound(self, *args, **kwargs): # real signature unknown
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

    def isSequential(self): # real signature unknown; restored from __doc__
        """ isSequential(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def localAddress(self): # real signature unknown; restored from __doc__
        """ localAddress(self) -> QHostAddress """
        return QHostAddress

    def localPort(self): # real signature unknown; restored from __doc__
        """ localPort(self) -> int """
        return 0

    def pauseMode(self): # real signature unknown; restored from __doc__
        """ pauseMode(self) -> QAbstractSocket.PauseModes """
        pass

    def peerAddress(self): # real signature unknown; restored from __doc__
        """ peerAddress(self) -> QHostAddress """
        return QHostAddress

    def peerName(self): # real signature unknown; restored from __doc__
        """ peerName(self) -> str """
        return ""

    def peerPort(self): # real signature unknown; restored from __doc__
        """ peerPort(self) -> int """
        return 0

    def protocolTag(self): # real signature unknown; restored from __doc__
        """ protocolTag(self) -> str """
        return ""

    def proxy(self): # real signature unknown; restored from __doc__
        """ proxy(self) -> QNetworkProxy """
        return QNetworkProxy

    def proxyAuthenticationRequired(self, *args, **kwargs): # real signature unknown
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

    def resume(self): # real signature unknown; restored from __doc__
        """ resume(self) """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setErrorString(self, *args, **kwargs): # real signature unknown
        pass

    def setLocalAddress(self, address, QHostAddress=None, QHostAddress_SpecialAddress=None): # real signature unknown; restored from __doc__
        """ setLocalAddress(self, address: Union[QHostAddress, QHostAddress.SpecialAddress]) """
        pass

    def setLocalPort(self, port): # real signature unknown; restored from __doc__
        """ setLocalPort(self, port: int) """
        pass

    def setOpenMode(self, *args, **kwargs): # real signature unknown
        pass

    def setPauseMode(self, pauseMode, QAbstractSocket_PauseModes=None, QAbstractSocket_PauseMode=None): # real signature unknown; restored from __doc__
        """ setPauseMode(self, pauseMode: Union[QAbstractSocket.PauseModes, QAbstractSocket.PauseMode]) """
        pass

    def setPeerAddress(self, address, QHostAddress=None, QHostAddress_SpecialAddress=None): # real signature unknown; restored from __doc__
        """ setPeerAddress(self, address: Union[QHostAddress, QHostAddress.SpecialAddress]) """
        pass

    def setPeerName(self, name, p_str=None): # real signature unknown; restored from __doc__
        """ setPeerName(self, name: Optional[str]) """
        pass

    def setPeerPort(self, port): # real signature unknown; restored from __doc__
        """ setPeerPort(self, port: int) """
        pass

    def setProtocolTag(self, tag, p_str=None): # real signature unknown; restored from __doc__
        """ setProtocolTag(self, tag: Optional[str]) """
        pass

    def setProxy(self, networkProxy): # real signature unknown; restored from __doc__
        """ setProxy(self, networkProxy: QNetworkProxy) """
        pass

    def setReadBufferSize(self, size): # real signature unknown; restored from __doc__
        """ setReadBufferSize(self, size: int) """
        pass

    def setSocketDescriptor(self, socketDescriptor, state=None, mode, QIODevice_OpenMode=None, QIODevice_OpenModeFlag=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setSocketDescriptor(self, socketDescriptor: PyQt5.sip.voidptr, state: QAbstractSocket.SocketState = QAbstractSocket.ConnectedState, mode: Union[QIODevice.OpenMode, QIODevice.OpenModeFlag] = QIODevice.ReadWrite) -> bool """
        pass

    def setSocketError(self, socketError): # real signature unknown; restored from __doc__
        """ setSocketError(self, socketError: QAbstractSocket.SocketError) """
        pass

    def setSocketOption(self, option, value): # real signature unknown; restored from __doc__
        """ setSocketOption(self, option: QAbstractSocket.SocketOption, value: Any) """
        pass

    def setSocketState(self, state): # real signature unknown; restored from __doc__
        """ setSocketState(self, state: QAbstractSocket.SocketState) """
        pass

    def socketDescriptor(self): # real signature unknown; restored from __doc__
        """ socketDescriptor(self) -> PyQt5.sip.voidptr """
        pass

    def socketOption(self, option): # real signature unknown; restored from __doc__
        """ socketOption(self, option: QAbstractSocket.SocketOption) -> Any """
        pass

    def socketType(self): # real signature unknown; restored from __doc__
        """ socketType(self) -> QAbstractSocket.SocketType """
        pass

    def state(self): # real signature unknown; restored from __doc__
        """ state(self) -> QAbstractSocket.SocketState """
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

    def waitForBytesWritten(self, msecs=30000): # real signature unknown; restored from __doc__
        """ waitForBytesWritten(self, msecs: int = 30000) -> bool """
        return False

    def waitForConnected(self, msecs=30000): # real signature unknown; restored from __doc__
        """ waitForConnected(self, msecs: int = 30000) -> bool """
        return False

    def waitForDisconnected(self, msecs=30000): # real signature unknown; restored from __doc__
        """ waitForDisconnected(self, msecs: int = 30000) -> bool """
        return False

    def waitForReadyRead(self, msecs=30000): # real signature unknown; restored from __doc__
        """ waitForReadyRead(self, msecs: int = 30000) -> bool """
        return False

    def writeData(self, data, PyQt5_sip_array=None, bytes=None): # real signature unknown; restored from __doc__
        """ writeData(self, data: Optional[PyQt5.sip.array[bytes]]) -> int """
        return 0

    def __init__(self, socketType, parent, QObject=None): # real signature unknown; restored from __doc__
        pass

    AddressInUseError = 8
    AnyIPProtocol = 2
    BoundState = 4
    ClosingState = 6
    ConnectedState = 3
    ConnectingState = 2
    ConnectionRefusedError = 0
    DatagramTooLargeError = 6
    DefaultForPlatform = 0
    DontShareAddress = 2
    HostLookupState = 1
    HostNotFoundError = 2
    IPv4Protocol = 0
    IPv6Protocol = 1
    KeepAliveOption = 1
    ListeningState = 5
    LowDelayOption = 0
    MulticastLoopbackOption = 3
    MulticastTtlOption = 2
    NetworkError = 7
    OperationError = 19
    PathMtuSocketOption = 7
    PauseNever = 0
    PauseOnSslErrors = 1
    ProxyAuthenticationRequiredError = 12
    ProxyConnectionClosedError = 15
    ProxyConnectionRefusedError = 14
    ProxyConnectionTimeoutError = 16
    ProxyNotFoundError = 17
    ProxyProtocolError = 18
    ReceiveBufferSizeSocketOption = 6
    RemoteHostClosedError = 1
    ReuseAddressHint = 4
    SctpSocket = 2
    SendBufferSizeSocketOption = 5
    ShareAddress = 1
    SocketAccessError = 3
    SocketAddressNotAvailableError = 9
    SocketResourceError = 4
    SocketTimeoutError = 5
    SslHandshakeFailedError = 13
    SslInternalError = 20
    SslInvalidUserDataError = 21
    TcpSocket = 0
    TemporaryError = 22
    TypeOfServiceOption = 4
    UdpSocket = 1
    UnconnectedState = 0
    UnfinishedSocketOperationError = 11
    UnknownNetworkLayerProtocol = -1
    UnknownSocketError = -1
    UnknownSocketType = -1
    UnsupportedSocketOperationError = 10


