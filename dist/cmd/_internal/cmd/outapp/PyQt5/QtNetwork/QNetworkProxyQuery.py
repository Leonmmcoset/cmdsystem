# encoding: utf-8
# module PyQt5.QtNetwork
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtNetwork.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QNetworkProxyQuery(__sip.simplewrapper):
    """
    QNetworkProxyQuery()
    QNetworkProxyQuery(requestUrl: QUrl, type: QNetworkProxyQuery.QueryType = QNetworkProxyQuery.UrlRequest)
    QNetworkProxyQuery(hostname: Optional[str], port: int, protocolTag: Optional[str] = '', type: QNetworkProxyQuery.QueryType = QNetworkProxyQuery.TcpSocket)
    QNetworkProxyQuery(bindPort: int, protocolTag: Optional[str] = '', type: QNetworkProxyQuery.QueryType = QNetworkProxyQuery.TcpServer)
    QNetworkProxyQuery(networkConfiguration: QNetworkConfiguration, requestUrl: QUrl, queryType: QNetworkProxyQuery.QueryType = QNetworkProxyQuery.UrlRequest)
    QNetworkProxyQuery(networkConfiguration: QNetworkConfiguration, hostname: Optional[str], port: int, protocolTag: Optional[str] = '', type: QNetworkProxyQuery.QueryType = QNetworkProxyQuery.TcpSocket)
    QNetworkProxyQuery(networkConfiguration: QNetworkConfiguration, bindPort: int, protocolTag: Optional[str] = '', type: QNetworkProxyQuery.QueryType = QNetworkProxyQuery.TcpServer)
    QNetworkProxyQuery(other: QNetworkProxyQuery)
    """
    def localPort(self): # real signature unknown; restored from __doc__
        """ localPort(self) -> int """
        return 0

    def networkConfiguration(self): # real signature unknown; restored from __doc__
        """ networkConfiguration(self) -> QNetworkConfiguration """
        return QNetworkConfiguration

    def peerHostName(self): # real signature unknown; restored from __doc__
        """ peerHostName(self) -> str """
        return ""

    def peerPort(self): # real signature unknown; restored from __doc__
        """ peerPort(self) -> int """
        return 0

    def protocolTag(self): # real signature unknown; restored from __doc__
        """ protocolTag(self) -> str """
        return ""

    def queryType(self): # real signature unknown; restored from __doc__
        """ queryType(self) -> QNetworkProxyQuery.QueryType """
        pass

    def setLocalPort(self, port): # real signature unknown; restored from __doc__
        """ setLocalPort(self, port: int) """
        pass

    def setNetworkConfiguration(self, networkConfiguration): # real signature unknown; restored from __doc__
        """ setNetworkConfiguration(self, networkConfiguration: QNetworkConfiguration) """
        pass

    def setPeerHostName(self, hostname, p_str=None): # real signature unknown; restored from __doc__
        """ setPeerHostName(self, hostname: Optional[str]) """
        pass

    def setPeerPort(self, port): # real signature unknown; restored from __doc__
        """ setPeerPort(self, port: int) """
        pass

    def setProtocolTag(self, protocolTag, p_str=None): # real signature unknown; restored from __doc__
        """ setProtocolTag(self, protocolTag: Optional[str]) """
        pass

    def setQueryType(self, type): # real signature unknown; restored from __doc__
        """ setQueryType(self, type: QNetworkProxyQuery.QueryType) """
        pass

    def setUrl(self, url): # real signature unknown; restored from __doc__
        """ setUrl(self, url: QUrl) """
        pass

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: QNetworkProxyQuery) """
        pass

    def url(self): # real signature unknown; restored from __doc__
        """ url(self) -> QUrl """
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


    SctpServer = 102
    SctpSocket = 2
    TcpServer = 100
    TcpSocket = 0
    UdpSocket = 1
    UrlRequest = 101
    __hash__ = None


