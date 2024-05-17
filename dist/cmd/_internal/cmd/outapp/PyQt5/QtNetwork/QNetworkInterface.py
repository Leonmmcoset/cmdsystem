# encoding: utf-8
# module PyQt5.QtNetwork
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtNetwork.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QNetworkInterface(__sip.simplewrapper):
    """
    QNetworkInterface()
    QNetworkInterface(other: QNetworkInterface)
    """
    def addressEntries(self): # real signature unknown; restored from __doc__
        """ addressEntries(self) -> List[QNetworkAddressEntry] """
        return []

    def allAddresses(self): # real signature unknown; restored from __doc__
        """ allAddresses() -> List[QHostAddress] """
        return []

    def allInterfaces(self): # real signature unknown; restored from __doc__
        """ allInterfaces() -> List[QNetworkInterface] """
        return []

    def flags(self): # real signature unknown; restored from __doc__
        """ flags(self) -> QNetworkInterface.InterfaceFlags """
        pass

    def hardwareAddress(self): # real signature unknown; restored from __doc__
        """ hardwareAddress(self) -> str """
        return ""

    def humanReadableName(self): # real signature unknown; restored from __doc__
        """ humanReadableName(self) -> str """
        return ""

    def index(self): # real signature unknown; restored from __doc__
        """ index(self) -> int """
        return 0

    def interfaceFromIndex(self, index): # real signature unknown; restored from __doc__
        """ interfaceFromIndex(index: int) -> QNetworkInterface """
        return QNetworkInterface

    def interfaceFromName(self, name, p_str=None): # real signature unknown; restored from __doc__
        """ interfaceFromName(name: Optional[str]) -> QNetworkInterface """
        return QNetworkInterface

    def interfaceIndexFromName(self, name, p_str=None): # real signature unknown; restored from __doc__
        """ interfaceIndexFromName(name: Optional[str]) -> int """
        return 0

    def interfaceNameFromIndex(self, index): # real signature unknown; restored from __doc__
        """ interfaceNameFromIndex(index: int) -> str """
        return ""

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def maximumTransmissionUnit(self): # real signature unknown; restored from __doc__
        """ maximumTransmissionUnit(self) -> int """
        return 0

    def name(self): # real signature unknown; restored from __doc__
        """ name(self) -> str """
        return ""

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: QNetworkInterface) """
        pass

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> QNetworkInterface.InterfaceType """
        pass

    def __init__(self, other=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    CanBroadcast = 4
    CanBus = 5
    CanMulticast = 32
    Ethernet = 3
    Fddi = 7
    Ieee1394 = 13
    Ieee80211 = 8
    Ieee802154 = 10
    Ieee80216 = 12
    IsLoopBack = 8
    IsPointToPoint = 16
    IsRunning = 2
    IsUp = 1
    Loopback = 1
    Phonet = 9
    Ppp = 6
    SixLoWPAN = 11
    Slip = 4
    Unknown = 0
    Virtual = 2
    Wifi = 8


