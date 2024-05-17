# encoding: utf-8
# module PyQt5.QtNetwork
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtNetwork.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


from .QTcpSocket import QTcpSocket

class QSslSocket(QTcpSocket):
    """ QSslSocket(parent: Optional[QObject] = None) """
    def abort(self): # real signature unknown; restored from __doc__
        """ abort(self) """
        pass

    def addCaCertificate(self, certificate): # real signature unknown; restored from __doc__
        """ addCaCertificate(self, certificate: QSslCertificate) """
        pass

    def addCaCertificates(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        addCaCertificates(self, path: Optional[str], format: QSsl.EncodingFormat = QSsl.Pem, syntax: QRegExp.PatternSyntax = QRegExp.FixedString) -> bool
        addCaCertificates(self, certificates: Iterable[QSslCertificate])
        """
        pass

    def addDefaultCaCertificate(self, certificate): # real signature unknown; restored from __doc__
        """ addDefaultCaCertificate(certificate: QSslCertificate) """
        pass

    def addDefaultCaCertificates(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        addDefaultCaCertificates(path: Optional[str], format: QSsl.EncodingFormat = QSsl.Pem, syntax: QRegExp.PatternSyntax = QRegExp.FixedString) -> bool
        addDefaultCaCertificates(certificates: Iterable[QSslCertificate])
        """
        pass

    def atEnd(self): # real signature unknown; restored from __doc__
        """ atEnd(self) -> bool """
        return False

    def bytesAvailable(self): # real signature unknown; restored from __doc__
        """ bytesAvailable(self) -> int """
        return 0

    def bytesToWrite(self): # real signature unknown; restored from __doc__
        """ bytesToWrite(self) -> int """
        return 0

    def caCertificates(self): # real signature unknown; restored from __doc__
        """ caCertificates(self) -> List[QSslCertificate] """
        return []

    def canReadLine(self): # real signature unknown; restored from __doc__
        """ canReadLine(self) -> bool """
        return False

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def ciphers(self): # real signature unknown; restored from __doc__
        """ ciphers(self) -> List[QSslCipher] """
        return []

    def close(self): # real signature unknown; restored from __doc__
        """ close(self) """
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def connectToHost(self, hostName, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ connectToHost(self, hostName: Optional[str], port: int, mode: Union[QIODevice.OpenMode, QIODevice.OpenModeFlag] = QIODevice.ReadWrite, protocol: QAbstractSocket.NetworkLayerProtocol = QAbstractSocket.AnyIPProtocol) """
        pass

    def connectToHostEncrypted(self, hostName, p_str=None, *args, **kwargs): # real signature unknown; restored from __doc__ with multiple overloads
        """
        connectToHostEncrypted(self, hostName: Optional[str], port: int, mode: Union[QIODevice.OpenMode, QIODevice.OpenModeFlag] = QIODevice.ReadWrite, protocol: QAbstractSocket.NetworkLayerProtocol = QAbstractSocket.AnyIPProtocol)
        connectToHostEncrypted(self, hostName: Optional[str], port: int, sslPeerName: Optional[str], mode: Union[QIODevice.OpenMode, QIODevice.OpenModeFlag] = QIODevice.ReadWrite, protocol: QAbstractSocket.NetworkLayerProtocol = QAbstractSocket.AnyIPProtocol)
        """
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def defaultCaCertificates(self): # real signature unknown; restored from __doc__
        """ defaultCaCertificates() -> List[QSslCertificate] """
        return []

    def defaultCiphers(self): # real signature unknown; restored from __doc__
        """ defaultCiphers() -> List[QSslCipher] """
        return []

    def disconnectFromHost(self): # real signature unknown; restored from __doc__
        """ disconnectFromHost(self) """
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def encrypted(self, *args, **kwargs): # real signature unknown
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

    def encryptedBytesAvailable(self): # real signature unknown; restored from __doc__
        """ encryptedBytesAvailable(self) -> int """
        return 0

    def encryptedBytesToWrite(self): # real signature unknown; restored from __doc__
        """ encryptedBytesToWrite(self) -> int """
        return 0

    def encryptedBytesWritten(self, *args, **kwargs): # real signature unknown
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

    def ignoreSslErrors(self, errors=None, QSslError=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        ignoreSslErrors(self)
        ignoreSslErrors(self, errors: Iterable[QSslError])
        """
        pass

    def isEncrypted(self): # real signature unknown; restored from __doc__
        """ isEncrypted(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def localCertificate(self): # real signature unknown; restored from __doc__
        """ localCertificate(self) -> QSslCertificate """
        return QSslCertificate

    def localCertificateChain(self): # real signature unknown; restored from __doc__
        """ localCertificateChain(self) -> List[QSslCertificate] """
        return []

    def mode(self): # real signature unknown; restored from __doc__
        """ mode(self) -> QSslSocket.SslMode """
        pass

    def modeChanged(self, *args, **kwargs): # real signature unknown
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

    def newSessionTicketReceived(self, *args, **kwargs): # real signature unknown
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

    def ocspResponses(self): # real signature unknown; restored from __doc__
        """ ocspResponses(self) -> List[QOcspResponse] """
        return []

    def peerCertificate(self): # real signature unknown; restored from __doc__
        """ peerCertificate(self) -> QSslCertificate """
        return QSslCertificate

    def peerCertificateChain(self): # real signature unknown; restored from __doc__
        """ peerCertificateChain(self) -> List[QSslCertificate] """
        return []

    def peerVerifyDepth(self): # real signature unknown; restored from __doc__
        """ peerVerifyDepth(self) -> int """
        return 0

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

    def peerVerifyMode(self): # real signature unknown; restored from __doc__
        """ peerVerifyMode(self) -> QSslSocket.PeerVerifyMode """
        pass

    def peerVerifyName(self): # real signature unknown; restored from __doc__
        """ peerVerifyName(self) -> str """
        return ""

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

    def privateKey(self): # real signature unknown; restored from __doc__
        """ privateKey(self) -> QSslKey """
        return QSslKey

    def protocol(self): # real signature unknown; restored from __doc__
        """ protocol(self) -> QSsl.SslProtocol """
        pass

    def readData(self, maxlen): # real signature unknown; restored from __doc__
        """ readData(self, maxlen: int) -> bytes """
        return b""

    def readLineData(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def resume(self): # real signature unknown; restored from __doc__
        """ resume(self) """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def sessionCipher(self): # real signature unknown; restored from __doc__
        """ sessionCipher(self) -> QSslCipher """
        return QSslCipher

    def sessionProtocol(self): # real signature unknown; restored from __doc__
        """ sessionProtocol(self) -> QSsl.SslProtocol """
        pass

    def setCaCertificates(self, certificates, QSslCertificate=None): # real signature unknown; restored from __doc__
        """ setCaCertificates(self, certificates: Iterable[QSslCertificate]) """
        pass

    def setCiphers(self, ciphers, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setCiphers(self, ciphers: Iterable[QSslCipher])
        setCiphers(self, ciphers: Optional[str])
        """
        pass

    def setDefaultCaCertificates(self, certificates, QSslCertificate=None): # real signature unknown; restored from __doc__
        """ setDefaultCaCertificates(certificates: Iterable[QSslCertificate]) """
        pass

    def setDefaultCiphers(self, ciphers, QSslCipher=None): # real signature unknown; restored from __doc__
        """ setDefaultCiphers(ciphers: Iterable[QSslCipher]) """
        pass

    def setErrorString(self, *args, **kwargs): # real signature unknown
        pass

    def setLocalAddress(self, *args, **kwargs): # real signature unknown
        pass

    def setLocalCertificate(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setLocalCertificate(self, certificate: QSslCertificate)
        setLocalCertificate(self, path: Optional[str], format: QSsl.EncodingFormat = QSsl.Pem)
        """
        pass

    def setLocalCertificateChain(self, localChain, QSslCertificate=None): # real signature unknown; restored from __doc__
        """ setLocalCertificateChain(self, localChain: Iterable[QSslCertificate]) """
        pass

    def setLocalPort(self, *args, **kwargs): # real signature unknown
        pass

    def setOpenMode(self, *args, **kwargs): # real signature unknown
        pass

    def setPeerAddress(self, *args, **kwargs): # real signature unknown
        pass

    def setPeerName(self, *args, **kwargs): # real signature unknown
        pass

    def setPeerPort(self, *args, **kwargs): # real signature unknown
        pass

    def setPeerVerifyDepth(self, depth): # real signature unknown; restored from __doc__
        """ setPeerVerifyDepth(self, depth: int) """
        pass

    def setPeerVerifyMode(self, mode): # real signature unknown; restored from __doc__
        """ setPeerVerifyMode(self, mode: QSslSocket.PeerVerifyMode) """
        pass

    def setPeerVerifyName(self, hostName, p_str=None): # real signature unknown; restored from __doc__
        """ setPeerVerifyName(self, hostName: Optional[str]) """
        pass

    def setPrivateKey(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setPrivateKey(self, key: QSslKey)
        setPrivateKey(self, fileName: Optional[str], algorithm: QSsl.KeyAlgorithm = QSsl.Rsa, format: QSsl.EncodingFormat = QSsl.Pem, passPhrase: Union[QByteArray, bytes, bytearray] = QByteArray())
        """
        pass

    def setProtocol(self, protocol): # real signature unknown; restored from __doc__
        """ setProtocol(self, protocol: QSsl.SslProtocol) """
        pass

    def setReadBufferSize(self, size): # real signature unknown; restored from __doc__
        """ setReadBufferSize(self, size: int) """
        pass

    def setSocketDescriptor(self, socketDescriptor, state=None, mode, QIODevice_OpenMode=None, QIODevice_OpenModeFlag=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setSocketDescriptor(self, socketDescriptor: PyQt5.sip.voidptr, state: QAbstractSocket.SocketState = QAbstractSocket.ConnectedState, mode: Union[QIODevice.OpenMode, QIODevice.OpenModeFlag] = QIODevice.ReadWrite) -> bool """
        pass

    def setSocketError(self, *args, **kwargs): # real signature unknown
        pass

    def setSocketOption(self, option, value): # real signature unknown; restored from __doc__
        """ setSocketOption(self, option: QAbstractSocket.SocketOption, value: Any) """
        pass

    def setSocketState(self, *args, **kwargs): # real signature unknown
        pass

    def setSslConfiguration(self, config): # real signature unknown; restored from __doc__
        """ setSslConfiguration(self, config: QSslConfiguration) """
        pass

    def socketOption(self, option): # real signature unknown; restored from __doc__
        """ socketOption(self, option: QAbstractSocket.SocketOption) -> Any """
        pass

    def sslConfiguration(self): # real signature unknown; restored from __doc__
        """ sslConfiguration(self) -> QSslConfiguration """
        return QSslConfiguration

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

    def sslHandshakeErrors(self): # real signature unknown; restored from __doc__
        """ sslHandshakeErrors(self) -> List[QSslError] """
        return []

    def sslLibraryBuildVersionNumber(self): # real signature unknown; restored from __doc__
        """ sslLibraryBuildVersionNumber() -> int """
        return 0

    def sslLibraryBuildVersionString(self): # real signature unknown; restored from __doc__
        """ sslLibraryBuildVersionString() -> str """
        return ""

    def sslLibraryVersionNumber(self): # real signature unknown; restored from __doc__
        """ sslLibraryVersionNumber() -> int """
        return 0

    def sslLibraryVersionString(self): # real signature unknown; restored from __doc__
        """ sslLibraryVersionString() -> str """
        return ""

    def startClientEncryption(self): # real signature unknown; restored from __doc__
        """ startClientEncryption(self) """
        pass

    def startServerEncryption(self): # real signature unknown; restored from __doc__
        """ startServerEncryption(self) """
        pass

    def supportedCiphers(self): # real signature unknown; restored from __doc__
        """ supportedCiphers() -> List[QSslCipher] """
        return []

    def supportsSsl(self): # real signature unknown; restored from __doc__
        """ supportsSsl() -> bool """
        return False

    def systemCaCertificates(self): # real signature unknown; restored from __doc__
        """ systemCaCertificates() -> List[QSslCertificate] """
        return []

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

    def waitForEncrypted(self, msecs=30000): # real signature unknown; restored from __doc__
        """ waitForEncrypted(self, msecs: int = 30000) -> bool """
        return False

    def waitForReadyRead(self, msecs=30000): # real signature unknown; restored from __doc__
        """ waitForReadyRead(self, msecs: int = 30000) -> bool """
        return False

    def writeData(self, data, PyQt5_sip_array=None, bytes=None): # real signature unknown; restored from __doc__
        """ writeData(self, data: Optional[PyQt5.sip.array[bytes]]) -> int """
        return 0

    def __init__(self, parent, QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    AutoVerifyPeer = 3
    QueryPeer = 1
    SslClientMode = 1
    SslServerMode = 2
    UnencryptedMode = 0
    VerifyNone = 0
    VerifyPeer = 2


