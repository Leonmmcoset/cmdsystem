# encoding: utf-8
# module PyQt5.QtNetwork
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtNetwork.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QTcpServer(__PyQt5_QtCore.QObject):
    """ QTcpServer(parent: Optional[QObject] = None) """
    def acceptError(self, *args, **kwargs): # real signature unknown
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

    def addPendingConnection(self, socket, QTcpSocket=None): # real signature unknown; restored from __doc__
        """ addPendingConnection(self, socket: Optional[QTcpSocket]) """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def close(self): # real signature unknown; restored from __doc__
        """ close(self) """
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def errorString(self): # real signature unknown; restored from __doc__
        """ errorString(self) -> str """
        return ""

    def hasPendingConnections(self): # real signature unknown; restored from __doc__
        """ hasPendingConnections(self) -> bool """
        return False

    def incomingConnection(self, handle): # real signature unknown; restored from __doc__
        """ incomingConnection(self, handle: PyQt5.sip.voidptr) """
        pass

    def isListening(self): # real signature unknown; restored from __doc__
        """ isListening(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def listen(self, address, QHostAddress=None, QHostAddress_SpecialAddress=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ listen(self, address: Union[QHostAddress, QHostAddress.SpecialAddress] = QHostAddress.Any, port: int = 0) -> bool """
        pass

    def maxPendingConnections(self): # real signature unknown; restored from __doc__
        """ maxPendingConnections(self) -> int """
        return 0

    def newConnection(self, *args, **kwargs): # real signature unknown
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

    def nextPendingConnection(self): # real signature unknown; restored from __doc__
        """ nextPendingConnection(self) -> Optional[QTcpSocket] """
        pass

    def pauseAccepting(self): # real signature unknown; restored from __doc__
        """ pauseAccepting(self) """
        pass

    def proxy(self): # real signature unknown; restored from __doc__
        """ proxy(self) -> QNetworkProxy """
        return QNetworkProxy

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def resumeAccepting(self): # real signature unknown; restored from __doc__
        """ resumeAccepting(self) """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def serverAddress(self): # real signature unknown; restored from __doc__
        """ serverAddress(self) -> QHostAddress """
        return QHostAddress

    def serverError(self): # real signature unknown; restored from __doc__
        """ serverError(self) -> QAbstractSocket.SocketError """
        pass

    def serverPort(self): # real signature unknown; restored from __doc__
        """ serverPort(self) -> int """
        return 0

    def setMaxPendingConnections(self, numConnections): # real signature unknown; restored from __doc__
        """ setMaxPendingConnections(self, numConnections: int) """
        pass

    def setProxy(self, networkProxy): # real signature unknown; restored from __doc__
        """ setProxy(self, networkProxy: QNetworkProxy) """
        pass

    def setSocketDescriptor(self, socketDescriptor): # real signature unknown; restored from __doc__
        """ setSocketDescriptor(self, socketDescriptor: PyQt5.sip.voidptr) -> bool """
        return False

    def socketDescriptor(self): # real signature unknown; restored from __doc__
        """ socketDescriptor(self) -> PyQt5.sip.voidptr """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def waitForNewConnection(self, msecs=0): # real signature unknown; restored from __doc__
        """ waitForNewConnection(self, msecs: int = 0) -> (bool, Optional[bool]) """
        pass

    def __init__(self, parent, QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass


