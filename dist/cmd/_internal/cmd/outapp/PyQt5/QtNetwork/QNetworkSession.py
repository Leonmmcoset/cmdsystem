# encoding: utf-8
# module PyQt5.QtNetwork
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtNetwork.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QNetworkSession(__PyQt5_QtCore.QObject):
    """ QNetworkSession(connConfig: QNetworkConfiguration, parent: Optional[QObject] = None) """
    def accept(self): # real signature unknown; restored from __doc__
        """ accept(self) """
        pass

    def activeTime(self): # real signature unknown; restored from __doc__
        """ activeTime(self) -> int """
        return 0

    def bytesReceived(self): # real signature unknown; restored from __doc__
        """ bytesReceived(self) -> int """
        return 0

    def bytesWritten(self): # real signature unknown; restored from __doc__
        """ bytesWritten(self) -> int """
        return 0

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def close(self): # real signature unknown; restored from __doc__
        """ close(self) """
        pass

    def closed(self, *args, **kwargs): # real signature unknown
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

    def configuration(self): # real signature unknown; restored from __doc__
        """ configuration(self) -> QNetworkConfiguration """
        return QNetworkConfiguration

    def connectNotify(self, signal): # real signature unknown; restored from __doc__
        """ connectNotify(self, signal: QMetaMethod) """
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, signal): # real signature unknown; restored from __doc__
        """ disconnectNotify(self, signal: QMetaMethod) """
        pass

    def error(self, *args, **kwargs): # real signature unknown
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

    def errorString(self): # real signature unknown; restored from __doc__
        """ errorString(self) -> str """
        return ""

    def ignore(self): # real signature unknown; restored from __doc__
        """ ignore(self) """
        pass

    def interface(self): # real signature unknown; restored from __doc__
        """ interface(self) -> QNetworkInterface """
        return QNetworkInterface

    def isOpen(self): # real signature unknown; restored from __doc__
        """ isOpen(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def migrate(self): # real signature unknown; restored from __doc__
        """ migrate(self) """
        pass

    def newConfigurationActivated(self, *args, **kwargs): # real signature unknown
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

    def open(self): # real signature unknown; restored from __doc__
        """ open(self) """
        pass

    def opened(self, *args, **kwargs): # real signature unknown
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

    def preferredConfigurationChanged(self, *args, **kwargs): # real signature unknown
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

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def reject(self): # real signature unknown; restored from __doc__
        """ reject(self) """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def sessionProperty(self, key, p_str=None): # real signature unknown; restored from __doc__
        """ sessionProperty(self, key: Optional[str]) -> Any """
        pass

    def setSessionProperty(self, key, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setSessionProperty(self, key: Optional[str], value: Any) """
        pass

    def state(self): # real signature unknown; restored from __doc__
        """ state(self) -> QNetworkSession.State """
        pass

    def stateChanged(self, *args, **kwargs): # real signature unknown
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

    def stop(self): # real signature unknown; restored from __doc__
        """ stop(self) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def usagePolicies(self): # real signature unknown; restored from __doc__
        """ usagePolicies(self) -> QNetworkSession.UsagePolicies """
        pass

    def usagePoliciesChanged(self, *args, **kwargs): # real signature unknown
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

    def waitForOpened(self, msecs=30000): # real signature unknown; restored from __doc__
        """ waitForOpened(self, msecs: int = 30000) -> bool """
        return False

    def __init__(self, connConfig, parent, QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    Closing = 4
    Connected = 3
    Connecting = 2
    Disconnected = 5
    Invalid = 0
    InvalidConfigurationError = 4
    NoBackgroundTrafficPolicy = 1
    NoPolicy = 0
    NotAvailable = 1
    OperationNotSupportedError = 3
    Roaming = 6
    RoamingError = 2
    SessionAbortedError = 1
    UnknownSessionError = 0


