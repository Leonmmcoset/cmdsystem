# encoding: utf-8
# module PyQt5.QtNetwork
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtNetwork.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QHostInfo(__sip.simplewrapper):
    """
    QHostInfo(id: int = -1)
    QHostInfo(d: QHostInfo)
    """
    def abortHostLookup(self, lookupId): # real signature unknown; restored from __doc__
        """ abortHostLookup(lookupId: int) """
        pass

    def addresses(self): # real signature unknown; restored from __doc__
        """ addresses(self) -> List[QHostAddress] """
        return []

    def error(self): # real signature unknown; restored from __doc__
        """ error(self) -> QHostInfo.HostInfoError """
        pass

    def errorString(self): # real signature unknown; restored from __doc__
        """ errorString(self) -> str """
        return ""

    def fromName(self, name, p_str=None): # real signature unknown; restored from __doc__
        """ fromName(name: Optional[str]) -> QHostInfo """
        return QHostInfo

    def hostName(self): # real signature unknown; restored from __doc__
        """ hostName(self) -> str """
        return ""

    def localDomainName(self): # real signature unknown; restored from __doc__
        """ localDomainName() -> str """
        return ""

    def localHostName(self): # real signature unknown; restored from __doc__
        """ localHostName() -> str """
        return ""

    def lookupHost(self, name, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ lookupHost(name: Optional[str], slot: PYQT_SLOT) -> int """
        pass

    def lookupId(self): # real signature unknown; restored from __doc__
        """ lookupId(self) -> int """
        return 0

    def setAddresses(self, addresses, Union=None, QHostAddress=None, QHostAddress_SpecialAddress=None): # real signature unknown; restored from __doc__
        """ setAddresses(self, addresses: Iterable[Union[QHostAddress, QHostAddress.SpecialAddress]]) """
        pass

    def setError(self, error): # real signature unknown; restored from __doc__
        """ setError(self, error: QHostInfo.HostInfoError) """
        pass

    def setErrorString(self, errorString, p_str=None): # real signature unknown; restored from __doc__
        """ setErrorString(self, errorString: Optional[str]) """
        pass

    def setHostName(self, name, p_str=None): # real signature unknown; restored from __doc__
        """ setHostName(self, name: Optional[str]) """
        pass

    def setLookupId(self, id): # real signature unknown; restored from __doc__
        """ setLookupId(self, id: int) """
        pass

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: QHostInfo) """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    HostNotFound = 1
    NoError = 0
    UnknownError = 2


