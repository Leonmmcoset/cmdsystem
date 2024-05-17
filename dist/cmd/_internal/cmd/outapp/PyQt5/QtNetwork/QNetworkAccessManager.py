# encoding: utf-8
# module PyQt5.QtNetwork
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtNetwork.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QNetworkAccessManager(__PyQt5_QtCore.QObject):
    """ QNetworkAccessManager(parent: Optional[QObject] = None) """
    def activeConfiguration(self): # real signature unknown; restored from __doc__
        """ activeConfiguration(self) -> QNetworkConfiguration """
        return QNetworkConfiguration

    def addStrictTransportSecurityHosts(self, knownHosts, QHstsPolicy=None): # real signature unknown; restored from __doc__
        """ addStrictTransportSecurityHosts(self, knownHosts: Iterable[QHstsPolicy]) """
        pass

    def authenticationRequired(self, *args, **kwargs): # real signature unknown
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

    def autoDeleteReplies(self): # real signature unknown; restored from __doc__
        """ autoDeleteReplies(self) -> bool """
        return False

    def cache(self): # real signature unknown; restored from __doc__
        """ cache(self) -> Optional[QAbstractNetworkCache] """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def clearAccessCache(self): # real signature unknown; restored from __doc__
        """ clearAccessCache(self) """
        pass

    def clearConnectionCache(self): # real signature unknown; restored from __doc__
        """ clearConnectionCache(self) """
        pass

    def configuration(self): # real signature unknown; restored from __doc__
        """ configuration(self) -> QNetworkConfiguration """
        return QNetworkConfiguration

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def connectToHost(self, hostName, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ connectToHost(self, hostName: Optional[str], port: int = 80) """
        pass

    def connectToHostEncrypted(self, hostName, p_str=None, *args, **kwargs): # real signature unknown; restored from __doc__ with multiple overloads
        """
        connectToHostEncrypted(self, hostName: Optional[str], port: int = 443, sslConfiguration: QSslConfiguration = QSslConfiguration.defaultConfiguration())
        connectToHostEncrypted(self, hostName: Optional[str], port: int, sslConfiguration: QSslConfiguration, peerName: Optional[str])
        """
        pass

    def cookieJar(self): # real signature unknown; restored from __doc__
        """ cookieJar(self) -> Optional[QNetworkCookieJar] """
        pass

    def createRequest(self, op, request, device, QIODevice=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ createRequest(self, op: QNetworkAccessManager.Operation, request: QNetworkRequest, device: Optional[QIODevice] = None) -> QNetworkReply """
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def deleteResource(self, request): # real signature unknown; restored from __doc__
        """ deleteResource(self, request: QNetworkRequest) -> Optional[QNetworkReply] """
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def enableStrictTransportSecurityStore(self, enabled, storeDir, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ enableStrictTransportSecurityStore(self, enabled: bool, storeDir: Optional[str] = '') """
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

    def get(self, request): # real signature unknown; restored from __doc__
        """ get(self, request: QNetworkRequest) -> Optional[QNetworkReply] """
        pass

    def head(self, request): # real signature unknown; restored from __doc__
        """ head(self, request: QNetworkRequest) -> Optional[QNetworkReply] """
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def isStrictTransportSecurityEnabled(self): # real signature unknown; restored from __doc__
        """ isStrictTransportSecurityEnabled(self) -> bool """
        return False

    def isStrictTransportSecurityStoreEnabled(self): # real signature unknown; restored from __doc__
        """ isStrictTransportSecurityStoreEnabled(self) -> bool """
        return False

    def networkAccessible(self): # real signature unknown; restored from __doc__
        """ networkAccessible(self) -> QNetworkAccessManager.NetworkAccessibility """
        pass

    def networkAccessibleChanged(self, *args, **kwargs): # real signature unknown
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

    def post(self, request, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        post(self, request: QNetworkRequest, data: Optional[QIODevice]) -> Optional[QNetworkReply]
        post(self, request: QNetworkRequest, data: Union[QByteArray, bytes, bytearray]) -> Optional[QNetworkReply]
        post(self, request: QNetworkRequest, multiPart: Optional[QHttpMultiPart]) -> Optional[QNetworkReply]
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

    def proxyFactory(self): # real signature unknown; restored from __doc__
        """ proxyFactory(self) -> Optional[QNetworkProxyFactory] """
        pass

    def put(self, request, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        put(self, request: QNetworkRequest, data: Optional[QIODevice]) -> Optional[QNetworkReply]
        put(self, request: QNetworkRequest, data: Union[QByteArray, bytes, bytearray]) -> Optional[QNetworkReply]
        put(self, request: QNetworkRequest, multiPart: Optional[QHttpMultiPart]) -> Optional[QNetworkReply]
        """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def redirectPolicy(self): # real signature unknown; restored from __doc__
        """ redirectPolicy(self) -> QNetworkRequest.RedirectPolicy """
        pass

    def sendCustomRequest(self, request, verb, QByteArray=None, bytes=None, bytearray=None, *args, **kwargs): # real signature unknown; restored from __doc__ with multiple overloads
        """
        sendCustomRequest(self, request: QNetworkRequest, verb: Union[QByteArray, bytes, bytearray], data: Optional[QIODevice] = None) -> Optional[QNetworkReply]
        sendCustomRequest(self, request: QNetworkRequest, verb: Union[QByteArray, bytes, bytearray], data: Union[QByteArray, bytes, bytearray]) -> Optional[QNetworkReply]
        sendCustomRequest(self, request: QNetworkRequest, verb: Union[QByteArray, bytes, bytearray], multiPart: Optional[QHttpMultiPart]) -> Optional[QNetworkReply]
        """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setAutoDeleteReplies(self, autoDelete): # real signature unknown; restored from __doc__
        """ setAutoDeleteReplies(self, autoDelete: bool) """
        pass

    def setCache(self, cache, QAbstractNetworkCache=None): # real signature unknown; restored from __doc__
        """ setCache(self, cache: Optional[QAbstractNetworkCache]) """
        pass

    def setConfiguration(self, config): # real signature unknown; restored from __doc__
        """ setConfiguration(self, config: QNetworkConfiguration) """
        pass

    def setCookieJar(self, cookieJar, QNetworkCookieJar=None): # real signature unknown; restored from __doc__
        """ setCookieJar(self, cookieJar: Optional[QNetworkCookieJar]) """
        pass

    def setNetworkAccessible(self, accessible): # real signature unknown; restored from __doc__
        """ setNetworkAccessible(self, accessible: QNetworkAccessManager.NetworkAccessibility) """
        pass

    def setProxy(self, proxy): # real signature unknown; restored from __doc__
        """ setProxy(self, proxy: QNetworkProxy) """
        pass

    def setProxyFactory(self, factory, QNetworkProxyFactory=None): # real signature unknown; restored from __doc__
        """ setProxyFactory(self, factory: Optional[QNetworkProxyFactory]) """
        pass

    def setRedirectPolicy(self, policy): # real signature unknown; restored from __doc__
        """ setRedirectPolicy(self, policy: QNetworkRequest.RedirectPolicy) """
        pass

    def setStrictTransportSecurityEnabled(self, enabled): # real signature unknown; restored from __doc__
        """ setStrictTransportSecurityEnabled(self, enabled: bool) """
        pass

    def setTransferTimeout(self, timeout=None): # real signature unknown; restored from __doc__
        """ setTransferTimeout(self, timeout: int = QNetworkRequest.TransferTimeoutConstant.DefaultTransferTimeoutConstant) """
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

    def strictTransportSecurityHosts(self): # real signature unknown; restored from __doc__
        """ strictTransportSecurityHosts(self) -> List[QHstsPolicy] """
        return []

    def supportedSchemes(self): # real signature unknown; restored from __doc__
        """ supportedSchemes(self) -> List[str] """
        return []

    def supportedSchemesImplementation(self): # real signature unknown; restored from __doc__
        """ supportedSchemesImplementation(self) -> List[str] """
        return []

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def transferTimeout(self): # real signature unknown; restored from __doc__
        """ transferTimeout(self) -> int """
        return 0

    def __init__(self, parent, QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    Accessible = 1
    CustomOperation = 6
    DeleteOperation = 5
    GetOperation = 2
    HeadOperation = 1
    NotAccessible = 0
    PostOperation = 4
    PutOperation = 3
    UnknownAccessibility = -1


