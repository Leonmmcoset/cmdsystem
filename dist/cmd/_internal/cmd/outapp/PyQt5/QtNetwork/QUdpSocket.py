# encoding: utf-8
# module PyQt5.QtNetwork
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtNetwork.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


from .QAbstractSocket import QAbstractSocket

class QUdpSocket(QAbstractSocket):
    """ QUdpSocket(parent: Optional[QObject] = None) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def hasPendingDatagrams(self): # real signature unknown; restored from __doc__
        """ hasPendingDatagrams(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def joinMulticastGroup(self, groupAddress, QHostAddress=None, QHostAddress_SpecialAddress=None, *args=None, **kwargs=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        joinMulticastGroup(self, groupAddress: Union[QHostAddress, QHostAddress.SpecialAddress]) -> bool
        joinMulticastGroup(self, groupAddress: Union[QHostAddress, QHostAddress.SpecialAddress], iface: QNetworkInterface) -> bool
        """
        return False

    def leaveMulticastGroup(self, groupAddress, QHostAddress=None, QHostAddress_SpecialAddress=None, *args=None, **kwargs=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        leaveMulticastGroup(self, groupAddress: Union[QHostAddress, QHostAddress.SpecialAddress]) -> bool
        leaveMulticastGroup(self, groupAddress: Union[QHostAddress, QHostAddress.SpecialAddress], iface: QNetworkInterface) -> bool
        """
        return False

    def multicastInterface(self): # real signature unknown; restored from __doc__
        """ multicastInterface(self) -> QNetworkInterface """
        return QNetworkInterface

    def pendingDatagramSize(self): # real signature unknown; restored from __doc__
        """ pendingDatagramSize(self) -> int """
        return 0

    def readData(self, *args, **kwargs): # real signature unknown
        pass

    def readDatagram(self, maxlen): # real signature unknown; restored from __doc__
        """ readDatagram(self, maxlen: int) -> (bytes, Optional[QHostAddress], Optional[int]) """
        pass

    def readLineData(self, *args, **kwargs): # real signature unknown
        pass

    def receiveDatagram(self, maxSize=-1): # real signature unknown; restored from __doc__
        """ receiveDatagram(self, maxSize: int = -1) -> QNetworkDatagram """
        return QNetworkDatagram

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setErrorString(self, *args, **kwargs): # real signature unknown
        pass

    def setLocalAddress(self, *args, **kwargs): # real signature unknown
        pass

    def setLocalPort(self, *args, **kwargs): # real signature unknown
        pass

    def setMulticastInterface(self, iface): # real signature unknown; restored from __doc__
        """ setMulticastInterface(self, iface: QNetworkInterface) """
        pass

    def setOpenMode(self, *args, **kwargs): # real signature unknown
        pass

    def setPeerAddress(self, *args, **kwargs): # real signature unknown
        pass

    def setPeerName(self, *args, **kwargs): # real signature unknown
        pass

    def setPeerPort(self, *args, **kwargs): # real signature unknown
        pass

    def setSocketError(self, *args, **kwargs): # real signature unknown
        pass

    def setSocketState(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def writeData(self, *args, **kwargs): # real signature unknown
        pass

    def writeDatagram(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        writeDatagram(self, data: Optional[PyQt5.sip.array[bytes]], host: Union[QHostAddress, QHostAddress.SpecialAddress], port: int) -> int
        writeDatagram(self, datagram: Union[QByteArray, bytes, bytearray], host: Union[QHostAddress, QHostAddress.SpecialAddress], port: int) -> int
        writeDatagram(self, datagram: QNetworkDatagram) -> int
        """
        return 0

    def __init__(self, parent, QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass


