# encoding: utf-8
# module PyQt5.QtNetwork
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtNetwork.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QNetworkCacheMetaData(__sip.simplewrapper):
    """
    QNetworkCacheMetaData()
    QNetworkCacheMetaData(other: QNetworkCacheMetaData)
    """
    def attributes(self): # real signature unknown; restored from __doc__
        """ attributes(self) -> Dict[QNetworkRequest.Attribute, Any] """
        return {}

    def expirationDate(self): # real signature unknown; restored from __doc__
        """ expirationDate(self) -> QDateTime """
        pass

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def lastModified(self): # real signature unknown; restored from __doc__
        """ lastModified(self) -> QDateTime """
        pass

    def rawHeaders(self): # real signature unknown; restored from __doc__
        """ rawHeaders(self) -> List[Tuple[QByteArray, QByteArray]] """
        return []

    def saveToDisk(self): # real signature unknown; restored from __doc__
        """ saveToDisk(self) -> bool """
        return False

    def setAttributes(self, attributes, QNetworkRequest_Attribute=None, Any=None): # real signature unknown; restored from __doc__
        """ setAttributes(self, attributes: Dict[QNetworkRequest.Attribute, Any]) """
        pass

    def setExpirationDate(self, dateTime, QDateTime=None, datetime_datetime=None): # real signature unknown; restored from __doc__
        """ setExpirationDate(self, dateTime: Union[QDateTime, datetime.datetime]) """
        pass

    def setLastModified(self, dateTime, QDateTime=None, datetime_datetime=None): # real signature unknown; restored from __doc__
        """ setLastModified(self, dateTime: Union[QDateTime, datetime.datetime]) """
        pass

    def setRawHeaders(self, headers, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setRawHeaders(self, headers: Iterable[Tuple[Union[QByteArray, bytes, bytearray], Union[QByteArray, bytes, bytearray]]]) """
        pass

    def setSaveToDisk(self, allow): # real signature unknown; restored from __doc__
        """ setSaveToDisk(self, allow: bool) """
        pass

    def setUrl(self, url): # real signature unknown; restored from __doc__
        """ setUrl(self, url: QUrl) """
        pass

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: QNetworkCacheMetaData) """
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


