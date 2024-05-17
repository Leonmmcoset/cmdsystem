# encoding: utf-8
# module PyQt5.QtNetwork
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtNetwork.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QNetworkCookie(__sip.simplewrapper):
    """
    QNetworkCookie(name: Union[QByteArray, bytes, bytearray] = QByteArray(), value: Union[QByteArray, bytes, bytearray] = QByteArray())
    QNetworkCookie(other: QNetworkCookie)
    """
    def domain(self): # real signature unknown; restored from __doc__
        """ domain(self) -> str """
        return ""

    def expirationDate(self): # real signature unknown; restored from __doc__
        """ expirationDate(self) -> QDateTime """
        pass

    def hasSameIdentifier(self, other): # real signature unknown; restored from __doc__
        """ hasSameIdentifier(self, other: QNetworkCookie) -> bool """
        return False

    def isHttpOnly(self): # real signature unknown; restored from __doc__
        """ isHttpOnly(self) -> bool """
        return False

    def isSecure(self): # real signature unknown; restored from __doc__
        """ isSecure(self) -> bool """
        return False

    def isSessionCookie(self): # real signature unknown; restored from __doc__
        """ isSessionCookie(self) -> bool """
        return False

    def name(self): # real signature unknown; restored from __doc__
        """ name(self) -> QByteArray """
        pass

    def normalize(self, url): # real signature unknown; restored from __doc__
        """ normalize(self, url: QUrl) """
        pass

    def parseCookies(self, cookieString, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ parseCookies(cookieString: Union[QByteArray, bytes, bytearray]) -> List[QNetworkCookie] """
        return []

    def path(self): # real signature unknown; restored from __doc__
        """ path(self) -> str """
        return ""

    def setDomain(self, domain, p_str=None): # real signature unknown; restored from __doc__
        """ setDomain(self, domain: Optional[str]) """
        pass

    def setExpirationDate(self, date, QDateTime=None, datetime_datetime=None): # real signature unknown; restored from __doc__
        """ setExpirationDate(self, date: Union[QDateTime, datetime.datetime]) """
        pass

    def setHttpOnly(self, enable): # real signature unknown; restored from __doc__
        """ setHttpOnly(self, enable: bool) """
        pass

    def setName(self, cookieName, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ setName(self, cookieName: Union[QByteArray, bytes, bytearray]) """
        pass

    def setPath(self, path, p_str=None): # real signature unknown; restored from __doc__
        """ setPath(self, path: Optional[str]) """
        pass

    def setSecure(self, enable): # real signature unknown; restored from __doc__
        """ setSecure(self, enable: bool) """
        pass

    def setValue(self, value, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ setValue(self, value: Union[QByteArray, bytes, bytearray]) """
        pass

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: QNetworkCookie) """
        pass

    def toRawForm(self, form=None): # real signature unknown; restored from __doc__
        """ toRawForm(self, form: QNetworkCookie.RawForm = QNetworkCookie.Full) -> QByteArray """
        pass

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


    Full = 1
    NameAndValueOnly = 0
    __hash__ = None


