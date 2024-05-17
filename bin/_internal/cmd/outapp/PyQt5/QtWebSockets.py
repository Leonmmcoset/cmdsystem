# encoding: utf-8
# module PyQt5.QtWebSockets
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtWebSockets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


# no functions
# classes

class QMaskGenerator(__PyQt5_QtCore.QObject):
    """ QMaskGenerator(parent: Optional[QObject] = None) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def nextMask(self): # real signature unknown; restored from __doc__
        """ nextMask(self) -> int """
        return 0

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def seed(self): # real signature unknown; restored from __doc__
        """ seed(self) -> bool """
        return False

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent, QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass


class QWebSocket(__PyQt5_QtCore.QObject):
    """ QWebSocket(origin: Optional[str] = '', version: QWebSocketProtocol.Version = QWebSocketProtocol.VersionLatest, parent: Optional[QObject] = None) """
    def abort(self): # real signature unknown; restored from __doc__
        """ abort(self) """
        pass

    def aboutToClose(self, *args, **kwargs): # real signature unknown
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

    def binaryFrameReceived(self, *args, **kwargs): # real signature unknown
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

    def binaryMessageReceived(self, *args, **kwargs): # real signature unknown
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

    def bytesToWrite(self): # real signature unknown; restored from __doc__
        """ bytesToWrite(self) -> int """
        return 0

    def bytesWritten(self, *args, **kwargs): # real signature unknown
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

    def close(self, closeCode=None, reason, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ close(self, closeCode: QWebSocketProtocol.CloseCode = QWebSocketProtocol.CloseCodeNormal, reason: Optional[str] = '') """
        pass

    def closeCode(self): # real signature unknown; restored from __doc__
        """ closeCode(self) -> QWebSocketProtocol.CloseCode """
        pass

    def closeReason(self): # real signature unknown; restored from __doc__
        """ closeReason(self) -> str """
        return ""

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

    def flush(self): # real signature unknown; restored from __doc__
        """ flush(self) -> bool """
        return False

    def ignoreSslErrors(self, errors=None, QSslError=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        ignoreSslErrors(self, errors: Iterable[QSslError])
        ignoreSslErrors(self)
        """
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def localAddress(self): # real signature unknown; restored from __doc__
        """ localAddress(self) -> QHostAddress """
        pass

    def localPort(self): # real signature unknown; restored from __doc__
        """ localPort(self) -> int """
        return 0

    def maskGenerator(self): # real signature unknown; restored from __doc__
        """ maskGenerator(self) -> Optional[QMaskGenerator] """
        pass

    def maxAllowedIncomingFrameSize(self): # real signature unknown; restored from __doc__
        """ maxAllowedIncomingFrameSize(self) -> int """
        return 0

    def maxAllowedIncomingMessageSize(self): # real signature unknown; restored from __doc__
        """ maxAllowedIncomingMessageSize(self) -> int """
        return 0

    def maxIncomingFrameSize(self): # real signature unknown; restored from __doc__
        """ maxIncomingFrameSize() -> int """
        return 0

    def maxIncomingMessageSize(self): # real signature unknown; restored from __doc__
        """ maxIncomingMessageSize() -> int """
        return 0

    def maxOutgoingFrameSize(self): # real signature unknown; restored from __doc__
        """ maxOutgoingFrameSize() -> int """
        return 0

    def open(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        open(self, url: QUrl)
        open(self, request: QNetworkRequest)
        """
        pass

    def origin(self): # real signature unknown; restored from __doc__
        """ origin(self) -> str """
        return ""

    def outgoingFrameSize(self): # real signature unknown; restored from __doc__
        """ outgoingFrameSize(self) -> int """
        return 0

    def pauseMode(self): # real signature unknown; restored from __doc__
        """ pauseMode(self) -> QAbstractSocket.PauseModes """
        pass

    def peerAddress(self): # real signature unknown; restored from __doc__
        """ peerAddress(self) -> QHostAddress """
        pass

    def peerName(self): # real signature unknown; restored from __doc__
        """ peerName(self) -> str """
        return ""

    def peerPort(self): # real signature unknown; restored from __doc__
        """ peerPort(self) -> int """
        return 0

    def ping(self, payload, QByteArray=None, bytes=None, bytearray=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ ping(self, payload: Union[QByteArray, bytes, bytearray] = QByteArray()) """
        pass

    def pong(self, *args, **kwargs): # real signature unknown
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

    def preSharedKeyAuthenticationRequired(self, *args, **kwargs): # real signature unknown
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

    def proxy(self): # real signature unknown; restored from __doc__
        """ proxy(self) -> QNetworkProxy """
        pass

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

    def readChannelFinished(self, *args, **kwargs): # real signature unknown
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

    def request(self): # real signature unknown; restored from __doc__
        """ request(self) -> QNetworkRequest """
        pass

    def requestUrl(self): # real signature unknown; restored from __doc__
        """ requestUrl(self) -> QUrl """
        pass

    def resourceName(self): # real signature unknown; restored from __doc__
        """ resourceName(self) -> str """
        return ""

    def resume(self): # real signature unknown; restored from __doc__
        """ resume(self) """
        pass

    def sendBinaryMessage(self, data, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ sendBinaryMessage(self, data: Union[QByteArray, bytes, bytearray]) -> int """
        return 0

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def sendTextMessage(self, message, p_str=None): # real signature unknown; restored from __doc__
        """ sendTextMessage(self, message: Optional[str]) -> int """
        return 0

    def setMaskGenerator(self, maskGenerator, QMaskGenerator=None): # real signature unknown; restored from __doc__
        """ setMaskGenerator(self, maskGenerator: Optional[QMaskGenerator]) """
        pass

    def setMaxAllowedIncomingFrameSize(self, maxAllowedIncomingFrameSize): # real signature unknown; restored from __doc__
        """ setMaxAllowedIncomingFrameSize(self, maxAllowedIncomingFrameSize: int) """
        pass

    def setMaxAllowedIncomingMessageSize(self, maxAllowedIncomingMessageSize): # real signature unknown; restored from __doc__
        """ setMaxAllowedIncomingMessageSize(self, maxAllowedIncomingMessageSize: int) """
        pass

    def setOutgoingFrameSize(self, outgoingFrameSize): # real signature unknown; restored from __doc__
        """ setOutgoingFrameSize(self, outgoingFrameSize: int) """
        pass

    def setPauseMode(self, pauseMode, QAbstractSocket_PauseModes=None, QAbstractSocket_PauseMode=None): # real signature unknown; restored from __doc__
        """ setPauseMode(self, pauseMode: Union[QAbstractSocket.PauseModes, QAbstractSocket.PauseMode]) """
        pass

    def setProxy(self, networkProxy): # real signature unknown; restored from __doc__
        """ setProxy(self, networkProxy: QNetworkProxy) """
        pass

    def setReadBufferSize(self, size): # real signature unknown; restored from __doc__
        """ setReadBufferSize(self, size: int) """
        pass

    def setSslConfiguration(self, sslConfiguration): # real signature unknown; restored from __doc__
        """ setSslConfiguration(self, sslConfiguration: QSslConfiguration) """
        pass

    def sslConfiguration(self): # real signature unknown; restored from __doc__
        """ sslConfiguration(self) -> QSslConfiguration """
        pass

    def sslErrors(self, *args, **kwargs): # real signature unknown
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

    def textFrameReceived(self, *args, **kwargs): # real signature unknown
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

    def textMessageReceived(self, *args, **kwargs): # real signature unknown
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

    def version(self): # real signature unknown; restored from __doc__
        """ version(self) -> QWebSocketProtocol.Version """
        pass

    def __init__(self, origin, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass


class QWebSocketCorsAuthenticator(__sip.simplewrapper):
    """
    QWebSocketCorsAuthenticator(origin: Optional[str])
    QWebSocketCorsAuthenticator(other: QWebSocketCorsAuthenticator)
    """
    def allowed(self): # real signature unknown; restored from __doc__
        """ allowed(self) -> bool """
        return False

    def origin(self): # real signature unknown; restored from __doc__
        """ origin(self) -> str """
        return ""

    def setAllowed(self, allowed): # real signature unknown; restored from __doc__
        """ setAllowed(self, allowed: bool) """
        pass

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: QWebSocketCorsAuthenticator) """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QWebSocketProtocol(__sip.simplewrapper):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    CloseCodeAbnormalDisconnection = 1006
    CloseCodeBadOperation = 1011
    CloseCodeDatatypeNotSupported = 1003
    CloseCodeGoingAway = 1001
    CloseCodeMissingExtension = 1010
    CloseCodeMissingStatusCode = 1005
    CloseCodeNormal = 1000
    CloseCodePolicyViolated = 1008
    CloseCodeProtocolError = 1002
    CloseCodeReserved1004 = 1004
    CloseCodeTlsHandshakeFailed = 1015
    CloseCodeTooMuchData = 1009
    CloseCodeWrongDatatype = 1007
    Version0 = 0
    Version13 = 13
    Version4 = 4
    Version5 = 5
    Version6 = 6
    Version7 = 7
    Version8 = 8
    VersionLatest = 13
    VersionUnknown = -1


class QWebSocketServer(__PyQt5_QtCore.QObject):
    """ QWebSocketServer(serverName: Optional[str], secureMode: QWebSocketServer.SslMode, parent: Optional[QObject] = None) """
    def acceptError(self, *args, **kwargs): # real signature unknown
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

    def close(self): # real signature unknown; restored from __doc__
        """ close(self) """
        pass

    def closed(self, *args, **kwargs): # real signature unknown
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

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def error(self): # real signature unknown; restored from __doc__
        """ error(self) -> QWebSocketProtocol.CloseCode """
        pass

    def errorString(self): # real signature unknown; restored from __doc__
        """ errorString(self) -> str """
        return ""

    def handleConnection(self, socket, QTcpSocket=None): # real signature unknown; restored from __doc__
        """ handleConnection(self, socket: Optional[QTcpSocket]) """
        pass

    def handshakeTimeoutMS(self): # real signature unknown; restored from __doc__
        """ handshakeTimeoutMS(self) -> int """
        return 0

    def hasPendingConnections(self): # real signature unknown; restored from __doc__
        """ hasPendingConnections(self) -> bool """
        return False

    def isListening(self): # real signature unknown; restored from __doc__
        """ isListening(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def listen(self, address, QHostAddress=None, QHostAddress_SpecialAddress=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ listen(self, address: Union[QHostAddress, QHostAddress.SpecialAddress] = QHostAddress.SpecialAddress.Any, port: int = 0) -> bool """
        pass

    def maxPendingConnections(self): # real signature unknown; restored from __doc__
        """ maxPendingConnections(self) -> int """
        return 0

    def nativeDescriptor(self): # real signature unknown; restored from __doc__
        """ nativeDescriptor(self) -> PyQt5.sip.voidptr """
        pass

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
        """ nextPendingConnection(self) -> Optional[QWebSocket] """
        pass

    def originAuthenticationRequired(self, *args, **kwargs): # real signature unknown
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

    def pauseAccepting(self): # real signature unknown; restored from __doc__
        """ pauseAccepting(self) """
        pass

    def peerVerifyError(self, *args, **kwargs): # real signature unknown
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

    def preSharedKeyAuthenticationRequired(self, *args, **kwargs): # real signature unknown
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

    def proxy(self): # real signature unknown; restored from __doc__
        """ proxy(self) -> QNetworkProxy """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def resumeAccepting(self): # real signature unknown; restored from __doc__
        """ resumeAccepting(self) """
        pass

    def secureMode(self): # real signature unknown; restored from __doc__
        """ secureMode(self) -> QWebSocketServer.SslMode """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def serverAddress(self): # real signature unknown; restored from __doc__
        """ serverAddress(self) -> QHostAddress """
        pass

    def serverError(self, *args, **kwargs): # real signature unknown
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

    def serverName(self): # real signature unknown; restored from __doc__
        """ serverName(self) -> str """
        return ""

    def serverPort(self): # real signature unknown; restored from __doc__
        """ serverPort(self) -> int """
        return 0

    def serverUrl(self): # real signature unknown; restored from __doc__
        """ serverUrl(self) -> QUrl """
        pass

    def setHandshakeTimeout(self, msec): # real signature unknown; restored from __doc__
        """ setHandshakeTimeout(self, msec: int) """
        pass

    def setMaxPendingConnections(self, numConnections): # real signature unknown; restored from __doc__
        """ setMaxPendingConnections(self, numConnections: int) """
        pass

    def setNativeDescriptor(self, descriptor): # real signature unknown; restored from __doc__
        """ setNativeDescriptor(self, descriptor: PyQt5.sip.voidptr) -> bool """
        return False

    def setProxy(self, networkProxy): # real signature unknown; restored from __doc__
        """ setProxy(self, networkProxy: QNetworkProxy) """
        pass

    def setServerName(self, serverName, p_str=None): # real signature unknown; restored from __doc__
        """ setServerName(self, serverName: Optional[str]) """
        pass

    def setSocketDescriptor(self, socketDescriptor): # real signature unknown; restored from __doc__
        """ setSocketDescriptor(self, socketDescriptor: int) -> bool """
        return False

    def setSslConfiguration(self, sslConfiguration): # real signature unknown; restored from __doc__
        """ setSslConfiguration(self, sslConfiguration: QSslConfiguration) """
        pass

    def socketDescriptor(self): # real signature unknown; restored from __doc__
        """ socketDescriptor(self) -> int """
        return 0

    def sslConfiguration(self): # real signature unknown; restored from __doc__
        """ sslConfiguration(self) -> QSslConfiguration """
        pass

    def sslErrors(self, *args, **kwargs): # real signature unknown
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

    def supportedVersions(self): # real signature unknown; restored from __doc__
        """ supportedVersions(self) -> List[QWebSocketProtocol.Version] """
        return []

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, serverName, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    NonSecureMode = 1
    SecureMode = 0


# variables with complex values



