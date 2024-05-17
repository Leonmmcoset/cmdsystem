# encoding: utf-8
# module PyQt5.QtNetwork
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtNetwork.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QHostAddress(__sip.simplewrapper):
    """
    QHostAddress()
    QHostAddress(address: QHostAddress.SpecialAddress)
    QHostAddress(ip4Addr: int)
    QHostAddress(address: Optional[str])
    QHostAddress(ip6Addr: Tuple[int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int])
    QHostAddress(copy: Union[QHostAddress, QHostAddress.SpecialAddress])
    """
    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def isBroadcast(self): # real signature unknown; restored from __doc__
        """ isBroadcast(self) -> bool """
        return False

    def isEqual(self, address, QHostAddress=None, QHostAddress_SpecialAddress=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ isEqual(self, address: Union[QHostAddress, QHostAddress.SpecialAddress], mode: Union[QHostAddress.ConversionMode, QHostAddress.ConversionModeFlag] = QHostAddress.TolerantConversion) -> bool """
        pass

    def isGlobal(self): # real signature unknown; restored from __doc__
        """ isGlobal(self) -> bool """
        return False

    def isInSubnet(self, subnet, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        isInSubnet(self, subnet: Union[QHostAddress, QHostAddress.SpecialAddress], netmask: int) -> bool
        isInSubnet(self, subnet: Tuple[Union[QHostAddress, QHostAddress.SpecialAddress], int]) -> bool
        """
        pass

    def isLinkLocal(self): # real signature unknown; restored from __doc__
        """ isLinkLocal(self) -> bool """
        return False

    def isLoopback(self): # real signature unknown; restored from __doc__
        """ isLoopback(self) -> bool """
        return False

    def isMulticast(self): # real signature unknown; restored from __doc__
        """ isMulticast(self) -> bool """
        return False

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def isSiteLocal(self): # real signature unknown; restored from __doc__
        """ isSiteLocal(self) -> bool """
        return False

    def isUniqueLocalUnicast(self): # real signature unknown; restored from __doc__
        """ isUniqueLocalUnicast(self) -> bool """
        return False

    def parseSubnet(self, subnet, p_str=None): # real signature unknown; restored from __doc__
        """ parseSubnet(subnet: Optional[str]) -> Tuple[QHostAddress, int] """
        pass

    def protocol(self): # real signature unknown; restored from __doc__
        """ protocol(self) -> QAbstractSocket.NetworkLayerProtocol """
        pass

    def scopeId(self): # real signature unknown; restored from __doc__
        """ scopeId(self) -> str """
        return ""

    def setAddress(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setAddress(self, address: QHostAddress.SpecialAddress)
        setAddress(self, ip4Addr: int)
        setAddress(self, address: Optional[str]) -> bool
        setAddress(self, ip6Addr: Tuple[int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int])
        """
        return False

    def setScopeId(self, id, p_str=None): # real signature unknown; restored from __doc__
        """ setScopeId(self, id: Optional[str]) """
        pass

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: QHostAddress) """
        pass

    def toIPv4Address(self): # real signature unknown; restored from __doc__
        """ toIPv4Address(self) -> int """
        return 0

    def toIPv6Address(self): # real signature unknown; restored from __doc__
        """ toIPv6Address(self) -> Tuple[int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int] """
        pass

    def toString(self): # real signature unknown; restored from __doc__
        """ toString(self) -> str """
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

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
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


    Any = 4
    AnyIPv4 = 6
    AnyIPv6 = 5
    Broadcast = 1
    ConvertLocalHost = 8
    ConvertUnspecifiedAddress = 4
    ConvertV4CompatToIPv4 = 2
    ConvertV4MappedToIPv4 = 1
    LocalHost = 2
    LocalHostIPv6 = 3
    Null = 0
    StrictConversion = 0
    TolerantConversion = 255


