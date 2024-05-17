# encoding: utf-8
# module PyQt5.QtNetwork
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtNetwork.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QNetworkAddressEntry(__sip.simplewrapper):
    """
    QNetworkAddressEntry()
    QNetworkAddressEntry(other: QNetworkAddressEntry)
    """
    def broadcast(self): # real signature unknown; restored from __doc__
        """ broadcast(self) -> QHostAddress """
        return QHostAddress

    def clearAddressLifetime(self): # real signature unknown; restored from __doc__
        """ clearAddressLifetime(self) """
        pass

    def dnsEligibility(self): # real signature unknown; restored from __doc__
        """ dnsEligibility(self) -> QNetworkAddressEntry.DnsEligibilityStatus """
        pass

    def ip(self): # real signature unknown; restored from __doc__
        """ ip(self) -> QHostAddress """
        return QHostAddress

    def isLifetimeKnown(self): # real signature unknown; restored from __doc__
        """ isLifetimeKnown(self) -> bool """
        return False

    def isPermanent(self): # real signature unknown; restored from __doc__
        """ isPermanent(self) -> bool """
        return False

    def isTemporary(self): # real signature unknown; restored from __doc__
        """ isTemporary(self) -> bool """
        return False

    def netmask(self): # real signature unknown; restored from __doc__
        """ netmask(self) -> QHostAddress """
        return QHostAddress

    def preferredLifetime(self): # real signature unknown; restored from __doc__
        """ preferredLifetime(self) -> QDeadlineTimer """
        pass

    def prefixLength(self): # real signature unknown; restored from __doc__
        """ prefixLength(self) -> int """
        return 0

    def setAddressLifetime(self, preferred, validity): # real signature unknown; restored from __doc__
        """ setAddressLifetime(self, preferred: QDeadlineTimer, validity: QDeadlineTimer) """
        pass

    def setBroadcast(self, newBroadcast, QHostAddress=None, QHostAddress_SpecialAddress=None): # real signature unknown; restored from __doc__
        """ setBroadcast(self, newBroadcast: Union[QHostAddress, QHostAddress.SpecialAddress]) """
        pass

    def setDnsEligibility(self, status): # real signature unknown; restored from __doc__
        """ setDnsEligibility(self, status: QNetworkAddressEntry.DnsEligibilityStatus) """
        pass

    def setIp(self, newIp, QHostAddress=None, QHostAddress_SpecialAddress=None): # real signature unknown; restored from __doc__
        """ setIp(self, newIp: Union[QHostAddress, QHostAddress.SpecialAddress]) """
        pass

    def setNetmask(self, newNetmask, QHostAddress=None, QHostAddress_SpecialAddress=None): # real signature unknown; restored from __doc__
        """ setNetmask(self, newNetmask: Union[QHostAddress, QHostAddress.SpecialAddress]) """
        pass

    def setPrefixLength(self, length): # real signature unknown; restored from __doc__
        """ setPrefixLength(self, length: int) """
        pass

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: QNetworkAddressEntry) """
        pass

    def validityLifetime(self): # real signature unknown; restored from __doc__
        """ validityLifetime(self) -> QDeadlineTimer """
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


    DnsEligibilityUnknown = -1
    DnsEligible = 1
    DnsIneligible = 0
    __hash__ = None


