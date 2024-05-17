# encoding: utf-8
# module PyQt5.QtNetwork
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtNetwork.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QNetworkReply(__PyQt5_QtCore.QIODevice):
    """ QNetworkReply(parent: Optional[QObject] = None) """
    def abort(self): # real signature unknown; restored from __doc__
        """ abort(self) """
        pass

    def attribute(self, code): # real signature unknown; restored from __doc__
        """ attribute(self, code: QNetworkRequest.Attribute) -> Any """
        pass

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

    def downloadProgress(self, *args, **kwargs): # real signature unknown
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

    def hasRawHeader(self, headerName, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ hasRawHeader(self, headerName: Union[QByteArray, bytes, bytearray]) -> bool """
        return False

    def header(self, header): # real signature unknown; restored from __doc__
        """ header(self, header: QNetworkRequest.KnownHeaders) -> Any """
        pass

    def ignoreSslErrors(self, errors=None, QSslError=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        ignoreSslErrors(self)
        ignoreSslErrors(self, errors: Iterable[QSslError])
        """
        pass

    def ignoreSslErrorsImplementation(self, a0, QSslError=None): # real signature unknown; restored from __doc__
        """ ignoreSslErrorsImplementation(self, a0: Iterable[QSslError]) """
        pass

    def isFinished(self): # real signature unknown; restored from __doc__
        """ isFinished(self) -> bool """
        return False

    def isRunning(self): # real signature unknown; restored from __doc__
        """ isRunning(self) -> bool """
        return False

    def isSequential(self): # real signature unknown; restored from __doc__
        """ isSequential(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def manager(self): # real signature unknown; restored from __doc__
        """ manager(self) -> Optional[QNetworkAccessManager] """
        pass

    def metaDataChanged(self, *args, **kwargs): # real signature unknown
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

    def operation(self): # real signature unknown; restored from __doc__
        """ operation(self) -> QNetworkAccessManager.Operation """
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

    def rawHeader(self, headerName, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ rawHeader(self, headerName: Union[QByteArray, bytes, bytearray]) -> QByteArray """
        pass

    def rawHeaderList(self): # real signature unknown; restored from __doc__
        """ rawHeaderList(self) -> List[QByteArray] """
        return []

    def rawHeaderPairs(self): # real signature unknown; restored from __doc__
        """ rawHeaderPairs(self) -> List[Tuple[QByteArray, QByteArray]] """
        return []

    def readBufferSize(self): # real signature unknown; restored from __doc__
        """ readBufferSize(self) -> int """
        return 0

    def readData(self, *args, **kwargs): # real signature unknown
        pass

    def readLineData(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def redirectAllowed(self, *args, **kwargs): # real signature unknown
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

    def redirected(self, *args, **kwargs): # real signature unknown
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

    def request(self): # real signature unknown; restored from __doc__
        """ request(self) -> QNetworkRequest """
        return QNetworkRequest

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setAttribute(self, code, value): # real signature unknown; restored from __doc__
        """ setAttribute(self, code: QNetworkRequest.Attribute, value: Any) """
        pass

    def setError(self, errorCode, errorString, p_str=None): # real signature unknown; restored from __doc__
        """ setError(self, errorCode: QNetworkReply.NetworkError, errorString: Optional[str]) """
        pass

    def setErrorString(self, *args, **kwargs): # real signature unknown
        pass

    def setFinished(self, finished): # real signature unknown; restored from __doc__
        """ setFinished(self, finished: bool) """
        pass

    def setHeader(self, header, value): # real signature unknown; restored from __doc__
        """ setHeader(self, header: QNetworkRequest.KnownHeaders, value: Any) """
        pass

    def setOpenMode(self, *args, **kwargs): # real signature unknown
        pass

    def setOperation(self, operation): # real signature unknown; restored from __doc__
        """ setOperation(self, operation: QNetworkAccessManager.Operation) """
        pass

    def setRawHeader(self, headerName, QByteArray=None, bytes=None, bytearray=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setRawHeader(self, headerName: Union[QByteArray, bytes, bytearray], value: Union[QByteArray, bytes, bytearray]) """
        pass

    def setReadBufferSize(self, size): # real signature unknown; restored from __doc__
        """ setReadBufferSize(self, size: int) """
        pass

    def setRequest(self, request): # real signature unknown; restored from __doc__
        """ setRequest(self, request: QNetworkRequest) """
        pass

    def setSslConfiguration(self, configuration): # real signature unknown; restored from __doc__
        """ setSslConfiguration(self, configuration: QSslConfiguration) """
        pass

    def setSslConfigurationImplementation(self, a0): # real signature unknown; restored from __doc__
        """ setSslConfigurationImplementation(self, a0: QSslConfiguration) """
        pass

    def setUrl(self, url): # real signature unknown; restored from __doc__
        """ setUrl(self, url: QUrl) """
        pass

    def sslConfiguration(self): # real signature unknown; restored from __doc__
        """ sslConfiguration(self) -> QSslConfiguration """
        return QSslConfiguration

    def sslConfigurationImplementation(self, a0): # real signature unknown; restored from __doc__
        """ sslConfigurationImplementation(self, a0: QSslConfiguration) """
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

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def uploadProgress(self, *args, **kwargs): # real signature unknown
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

    def url(self): # real signature unknown; restored from __doc__
        """ url(self) -> QUrl """
        pass

    def writeData(self, data, PyQt5_sip_array=None, bytes=None): # real signature unknown; restored from __doc__
        """ writeData(self, data: Optional[PyQt5.sip.array[bytes]]) -> int """
        return 0

    def __init__(self, parent, QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    AuthenticationRequiredError = 204
    BackgroundRequestNotAllowedError = 9
    ConnectionRefusedError = 1
    ContentAccessDenied = 201
    ContentConflictError = 206
    ContentGoneError = 207
    ContentNotFoundError = 203
    ContentOperationNotPermittedError = 202
    ContentReSendError = 205
    HostNotFoundError = 3
    InsecureRedirectError = 11
    InternalServerError = 401
    NetworkSessionFailedError = 8
    NoError = 0
    OperationCanceledError = 5
    OperationNotImplementedError = 402
    ProtocolFailure = 399
    ProtocolInvalidOperationError = 302
    ProtocolUnknownError = 301
    ProxyAuthenticationRequiredError = 105
    ProxyConnectionClosedError = 102
    ProxyConnectionRefusedError = 101
    ProxyNotFoundError = 103
    ProxyTimeoutError = 104
    RemoteHostClosedError = 2
    ServiceUnavailableError = 403
    SslHandshakeFailedError = 6
    TemporaryNetworkFailureError = 7
    TimeoutError = 4
    TooManyRedirectsError = 10
    UnknownContentError = 299
    UnknownNetworkError = 99
    UnknownProxyError = 199
    UnknownServerError = 499


