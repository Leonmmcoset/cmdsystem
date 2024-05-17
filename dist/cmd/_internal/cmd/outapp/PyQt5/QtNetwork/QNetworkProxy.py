# encoding: utf-8
# module PyQt5.QtNetwork
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtNetwork.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QNetworkProxy(__sip.simplewrapper):
    """
    QNetworkProxy()
    QNetworkProxy(type: QNetworkProxy.ProxyType, hostName: Optional[str] = '', port: int = 0, user: Optional[str] = '', password: Optional[str] = '')
    QNetworkProxy(other: QNetworkProxy)
    """
    def applicationProxy(self): # real signature unknown; restored from __doc__
        """ applicationProxy() -> QNetworkProxy """
        return QNetworkProxy

    def capabilities(self): # real signature unknown; restored from __doc__
        """ capabilities(self) -> QNetworkProxy.Capabilities """
        pass

    def hasRawHeader(self, headerName, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ hasRawHeader(self, headerName: Union[QByteArray, bytes, bytearray]) -> bool """
        return False

    def header(self, header): # real signature unknown; restored from __doc__
        """ header(self, header: QNetworkRequest.KnownHeaders) -> Any """
        pass

    def hostName(self): # real signature unknown; restored from __doc__
        """ hostName(self) -> str """
        return ""

    def isCachingProxy(self): # real signature unknown; restored from __doc__
        """ isCachingProxy(self) -> bool """
        return False

    def isTransparentProxy(self): # real signature unknown; restored from __doc__
        """ isTransparentProxy(self) -> bool """
        return False

    def password(self): # real signature unknown; restored from __doc__
        """ password(self) -> str """
        return ""

    def port(self): # real signature unknown; restored from __doc__
        """ port(self) -> int """
        return 0

    def rawHeader(self, headerName, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ rawHeader(self, headerName: Union[QByteArray, bytes, bytearray]) -> QByteArray """
        pass

    def rawHeaderList(self): # real signature unknown; restored from __doc__
        """ rawHeaderList(self) -> List[QByteArray] """
        return []

    def setApplicationProxy(self, proxy): # real signature unknown; restored from __doc__
        """ setApplicationProxy(proxy: QNetworkProxy) """
        pass

    def setCapabilities(self, capab, QNetworkProxy_Capabilities=None, QNetworkProxy_Capability=None): # real signature unknown; restored from __doc__
        """ setCapabilities(self, capab: Union[QNetworkProxy.Capabilities, QNetworkProxy.Capability]) """
        pass

    def setHeader(self, header, value): # real signature unknown; restored from __doc__
        """ setHeader(self, header: QNetworkRequest.KnownHeaders, value: Any) """
        pass

    def setHostName(self, hostName, p_str=None): # real signature unknown; restored from __doc__
        """ setHostName(self, hostName: Optional[str]) """
        pass

    def setPassword(self, password, p_str=None): # real signature unknown; restored from __doc__
        """ setPassword(self, password: Optional[str]) """
        pass

    def setPort(self, port): # real signature unknown; restored from __doc__
        """ setPort(self, port: int) """
        pass

    def setRawHeader(self, headerName, QByteArray=None, bytes=None, bytearray=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setRawHeader(self, headerName: Union[QByteArray, bytes, bytearray], value: Union[QByteArray, bytes, bytearray]) """
        pass

    def setType(self, type): # real signature unknown; restored from __doc__
        """ setType(self, type: QNetworkProxy.ProxyType) """
        pass

    def setUser(self, userName, p_str=None): # real signature unknown; restored from __doc__
        """ setUser(self, userName: Optional[str]) """
        pass

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: QNetworkProxy) """
        pass

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> QNetworkProxy.ProxyType """
        pass

    def user(self): # real signature unknown; restored from __doc__
        """ user(self) -> str """
        return ""

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


    CachingCapability = 8
    DefaultProxy = 0
    FtpCachingProxy = 5
    HostNameLookupCapability = 16
    HttpCachingProxy = 4
    HttpProxy = 3
    ListeningCapability = 2
    NoProxy = 2
    SctpListeningCapability = 64
    SctpTunnelingCapability = 32
    Socks5Proxy = 1
    TunnelingCapability = 1
    UdpTunnelingCapability = 4
    __hash__ = None


