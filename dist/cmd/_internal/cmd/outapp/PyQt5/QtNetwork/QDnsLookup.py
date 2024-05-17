# encoding: utf-8
# module PyQt5.QtNetwork
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtNetwork.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QDnsLookup(__PyQt5_QtCore.QObject):
    """
    QDnsLookup(parent: Optional[QObject] = None)
    QDnsLookup(type: QDnsLookup.Type, name: Optional[str], parent: Optional[QObject] = None)
    QDnsLookup(type: QDnsLookup.Type, name: Optional[str], nameserver: Union[QHostAddress, QHostAddress.SpecialAddress], parent: Optional[QObject] = None)
    """
    def abort(self): # real signature unknown; restored from __doc__
        """ abort(self) """
        pass

    def canonicalNameRecords(self): # real signature unknown; restored from __doc__
        """ canonicalNameRecords(self) -> List[QDnsDomainNameRecord] """
        return []

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def error(self): # real signature unknown; restored from __doc__
        """ error(self) -> QDnsLookup.Error """
        pass

    def errorString(self): # real signature unknown; restored from __doc__
        """ errorString(self) -> str """
        return ""

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

    def hostAddressRecords(self): # real signature unknown; restored from __doc__
        """ hostAddressRecords(self) -> List[QDnsHostAddressRecord] """
        return []

    def isFinished(self): # real signature unknown; restored from __doc__
        """ isFinished(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def lookup(self): # real signature unknown; restored from __doc__
        """ lookup(self) """
        pass

    def mailExchangeRecords(self): # real signature unknown; restored from __doc__
        """ mailExchangeRecords(self) -> List[QDnsMailExchangeRecord] """
        return []

    def name(self): # real signature unknown; restored from __doc__
        """ name(self) -> str """
        return ""

    def nameChanged(self, *args, **kwargs): # real signature unknown
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

    def nameserver(self): # real signature unknown; restored from __doc__
        """ nameserver(self) -> QHostAddress """
        return QHostAddress

    def nameserverChanged(self, *args, **kwargs): # real signature unknown
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

    def nameServerRecords(self): # real signature unknown; restored from __doc__
        """ nameServerRecords(self) -> List[QDnsDomainNameRecord] """
        return []

    def pointerRecords(self): # real signature unknown; restored from __doc__
        """ pointerRecords(self) -> List[QDnsDomainNameRecord] """
        return []

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def serviceRecords(self): # real signature unknown; restored from __doc__
        """ serviceRecords(self) -> List[QDnsServiceRecord] """
        return []

    def setName(self, name, p_str=None): # real signature unknown; restored from __doc__
        """ setName(self, name: Optional[str]) """
        pass

    def setNameserver(self, nameserver, QHostAddress=None, QHostAddress_SpecialAddress=None): # real signature unknown; restored from __doc__
        """ setNameserver(self, nameserver: Union[QHostAddress, QHostAddress.SpecialAddress]) """
        pass

    def setType(self, a0): # real signature unknown; restored from __doc__
        """ setType(self, a0: QDnsLookup.Type) """
        pass

    def textRecords(self): # real signature unknown; restored from __doc__
        """ textRecords(self) -> List[QDnsTextRecord] """
        return []

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> QDnsLookup.Type """
        pass

    def typeChanged(self, *args, **kwargs): # real signature unknown
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

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    A = 1
    AAAA = 28
    ANY = 255
    CNAME = 5
    InvalidReplyError = 4
    InvalidRequestError = 3
    MX = 15
    NoError = 0
    NotFoundError = 7
    NS = 2
    OperationCancelledError = 2
    PTR = 12
    ResolverError = 1
    ServerFailureError = 5
    ServerRefusedError = 6
    SRV = 33
    TXT = 16


