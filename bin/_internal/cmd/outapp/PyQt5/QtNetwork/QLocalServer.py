# encoding: utf-8
# module PyQt5.QtNetwork
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtNetwork.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QLocalServer(__PyQt5_QtCore.QObject):
    """ QLocalServer(parent: Optional[QObject] = None) """
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

    def fullServerName(self): # real signature unknown; restored from __doc__
        """ fullServerName(self) -> str """
        return ""

    def hasPendingConnections(self): # real signature unknown; restored from __doc__
        """ hasPendingConnections(self) -> bool """
        return False

    def incomingConnection(self, socketDescriptor): # real signature unknown; restored from __doc__
        """ incomingConnection(self, socketDescriptor: PyQt5.sip.voidptr) """
        pass

    def isListening(self): # real signature unknown; restored from __doc__
        """ isListening(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def listen(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        listen(self, name: Optional[str]) -> bool
        listen(self, socketDescriptor: PyQt5.sip.voidptr) -> bool
        """
        return False

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
        """ nextPendingConnection(self) -> Optional[QLocalSocket] """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def removeServer(self, name, p_str=None): # real signature unknown; restored from __doc__
        """ removeServer(name: Optional[str]) -> bool """
        return False

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def serverError(self): # real signature unknown; restored from __doc__
        """ serverError(self) -> QAbstractSocket.SocketError """
        pass

    def serverName(self): # real signature unknown; restored from __doc__
        """ serverName(self) -> str """
        return ""

    def setMaxPendingConnections(self, numConnections): # real signature unknown; restored from __doc__
        """ setMaxPendingConnections(self, numConnections: int) """
        pass

    def setSocketOptions(self, options, QLocalServer_SocketOptions=None, QLocalServer_SocketOption=None): # real signature unknown; restored from __doc__
        """ setSocketOptions(self, options: Union[QLocalServer.SocketOptions, QLocalServer.SocketOption]) """
        pass

    def socketDescriptor(self): # real signature unknown; restored from __doc__
        """ socketDescriptor(self) -> PyQt5.sip.voidptr """
        pass

    def socketOptions(self): # real signature unknown; restored from __doc__
        """ socketOptions(self) -> QLocalServer.SocketOptions """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def waitForNewConnection(self, msecs=0): # real signature unknown; restored from __doc__
        """ waitForNewConnection(self, msecs: int = 0) -> (bool, Optional[bool]) """
        pass

    def __init__(self, parent, QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    GroupAccessOption = 2
    OtherAccessOption = 4
    UserAccessOption = 1
    WorldAccessOption = 7


