# encoding: utf-8
# module PyQt5.QtDBus
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtDBus.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


# no functions
# classes

class QDBus(__sip.simplewrapper):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    AutoDetect = 3
    Block = 1
    BlockWithGui = 2
    NoBlock = 0


class QDBusAbstractAdaptor(__PyQt5_QtCore.QObject):
    """ QDBusAbstractAdaptor(parent: Optional[QObject]) """
    def autoRelaySignals(self): # real signature unknown; restored from __doc__
        """ autoRelaySignals(self) -> bool """
        return False

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setAutoRelaySignals(self, enable): # real signature unknown; restored from __doc__
        """ setAutoRelaySignals(self, enable: bool) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent, QObject=None): # real signature unknown; restored from __doc__
        pass


class QDBusAbstractInterface(__PyQt5_QtCore.QObject):
    """ QDBusAbstractInterface(service: Optional[str], path: Optional[str], interface: Optional[str], connection: QDBusConnection, parent: Optional[QObject]) """
    def asyncCall(self, method, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ asyncCall(self, method: Optional[str], arg1: Any = None, arg2: Any = None, arg3: Any = None, arg4: Any = None, arg5: Any = None, arg6: Any = None, arg7: Any = None, arg8: Any = None) -> QDBusPendingCall """
        pass

    def asyncCallWithArgumentList(self, method, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ asyncCallWithArgumentList(self, method: Optional[str], args: Iterable[Any]) -> QDBusPendingCall """
        pass

    def call(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        call(self, method: Optional[str], arg1: Any = None, arg2: Any = None, arg3: Any = None, arg4: Any = None, arg5: Any = None, arg6: Any = None, arg7: Any = None, arg8: Any = None) -> QDBusMessage
        call(self, mode: QDBus.CallMode, method: Optional[str], arg1: Any = None, arg2: Any = None, arg3: Any = None, arg4: Any = None, arg5: Any = None, arg6: Any = None, arg7: Any = None, arg8: Any = None) -> QDBusMessage
        """
        pass

    def callWithArgumentList(self, mode, method, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ callWithArgumentList(self, mode: QDBus.CallMode, method: Optional[str], args: Iterable[Any]) -> QDBusMessage """
        pass

    def callWithCallback(self, method, p_str=None, *args, **kwargs): # real signature unknown; restored from __doc__ with multiple overloads
        """
        callWithCallback(self, method: Optional[str], args: Iterable[Any], returnMethod: PYQT_SLOT, errorMethod: PYQT_SLOT) -> bool
        callWithCallback(self, method: Optional[str], args: Iterable[Any], slot: PYQT_SLOT) -> bool
        """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connection(self): # real signature unknown; restored from __doc__
        """ connection(self) -> QDBusConnection """
        return QDBusConnection

    def connectNotify(self, signal): # real signature unknown; restored from __doc__
        """ connectNotify(self, signal: QMetaMethod) """
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, signal): # real signature unknown; restored from __doc__
        """ disconnectNotify(self, signal: QMetaMethod) """
        pass

    def interface(self): # real signature unknown; restored from __doc__
        """ interface(self) -> str """
        return ""

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def lastError(self): # real signature unknown; restored from __doc__
        """ lastError(self) -> QDBusError """
        return QDBusError

    def path(self): # real signature unknown; restored from __doc__
        """ path(self) -> str """
        return ""

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def service(self): # real signature unknown; restored from __doc__
        """ service(self) -> str """
        return ""

    def setTimeout(self, timeout): # real signature unknown; restored from __doc__
        """ setTimeout(self, timeout: int) """
        pass

    def timeout(self): # real signature unknown; restored from __doc__
        """ timeout(self) -> int """
        return 0

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, service, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass


class QDBusArgument(__sip.simplewrapper):
    """
    QDBusArgument()
    QDBusArgument(other: QDBusArgument)
    QDBusArgument(arg: Any, id: int = QMetaType.Int)
    """
    def add(self, arg, id=None): # real signature unknown; restored from __doc__
        """ add(self, arg: Any, id: int = QMetaType.Int) """
        pass

    def beginArray(self, id): # real signature unknown; restored from __doc__
        """ beginArray(self, id: int) """
        pass

    def beginMap(self, kid, vid): # real signature unknown; restored from __doc__
        """ beginMap(self, kid: int, vid: int) """
        pass

    def beginMapEntry(self): # real signature unknown; restored from __doc__
        """ beginMapEntry(self) """
        pass

    def beginStructure(self): # real signature unknown; restored from __doc__
        """ beginStructure(self) """
        pass

    def endArray(self): # real signature unknown; restored from __doc__
        """ endArray(self) """
        pass

    def endMap(self): # real signature unknown; restored from __doc__
        """ endMap(self) """
        pass

    def endMapEntry(self): # real signature unknown; restored from __doc__
        """ endMapEntry(self) """
        pass

    def endStructure(self): # real signature unknown; restored from __doc__
        """ endStructure(self) """
        pass

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: QDBusArgument) """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QDBusConnection(__sip.simplewrapper):
    """
    QDBusConnection(name: Optional[str])
    QDBusConnection(other: QDBusConnection)
    """
    def asyncCall(self, message, timeout=-1): # real signature unknown; restored from __doc__
        """ asyncCall(self, message: QDBusMessage, timeout: int = -1) -> QDBusPendingCall """
        return QDBusPendingCall

    def baseService(self): # real signature unknown; restored from __doc__
        """ baseService(self) -> str """
        return ""

    def call(self, message, mode=None, timeout=-1): # real signature unknown; restored from __doc__
        """ call(self, message: QDBusMessage, mode: QDBus.CallMode = QDBus.Block, timeout: int = -1) -> QDBusMessage """
        return QDBusMessage

    def callWithCallback(self, message, returnMethod, errorMethod, timeout=-1): # real signature unknown; restored from __doc__
        """ callWithCallback(self, message: QDBusMessage, returnMethod: PYQT_SLOT, errorMethod: PYQT_SLOT, timeout: int = -1) -> bool """
        return False

    def connect(self, service, p_str=None, *args, **kwargs): # real signature unknown; restored from __doc__ with multiple overloads
        """
        connect(self, service: Optional[str], path: Optional[str], interface: Optional[str], name: Optional[str], slot: PYQT_SLOT) -> bool
        connect(self, service: Optional[str], path: Optional[str], interface: Optional[str], name: Optional[str], signature: Optional[str], slot: PYQT_SLOT) -> bool
        connect(self, service: Optional[str], path: Optional[str], interface: Optional[str], name: Optional[str], argumentMatch: Iterable[Optional[str]], signature: Optional[str], slot: PYQT_SLOT) -> bool
        """
        pass

    def connectionCapabilities(self): # real signature unknown; restored from __doc__
        """ connectionCapabilities(self) -> QDBusConnection.ConnectionCapabilities """
        pass

    def connectToBus(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        connectToBus(type: QDBusConnection.BusType, name: Optional[str]) -> QDBusConnection
        connectToBus(address: Optional[str], name: Optional[str]) -> QDBusConnection
        """
        return QDBusConnection

    def connectToPeer(self, address, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ connectToPeer(address: Optional[str], name: Optional[str]) -> QDBusConnection """
        pass

    def disconnect(self, service, p_str=None, *args, **kwargs): # real signature unknown; restored from __doc__ with multiple overloads
        """
        disconnect(self, service: Optional[str], path: Optional[str], interface: Optional[str], name: Optional[str], slot: PYQT_SLOT) -> bool
        disconnect(self, service: Optional[str], path: Optional[str], interface: Optional[str], name: Optional[str], signature: Optional[str], slot: PYQT_SLOT) -> bool
        disconnect(self, service: Optional[str], path: Optional[str], interface: Optional[str], name: Optional[str], argumentMatch: Iterable[Optional[str]], signature: Optional[str], slot: PYQT_SLOT) -> bool
        """
        pass

    def disconnectFromBus(self, name, p_str=None): # real signature unknown; restored from __doc__
        """ disconnectFromBus(name: Optional[str]) """
        pass

    def disconnectFromPeer(self, name, p_str=None): # real signature unknown; restored from __doc__
        """ disconnectFromPeer(name: Optional[str]) """
        pass

    def interface(self): # real signature unknown; restored from __doc__
        """ interface(self) -> Optional[QDBusConnectionInterface] """
        pass

    def isConnected(self): # real signature unknown; restored from __doc__
        """ isConnected(self) -> bool """
        return False

    def lastError(self): # real signature unknown; restored from __doc__
        """ lastError(self) -> QDBusError """
        return QDBusError

    def localMachineId(self): # real signature unknown; restored from __doc__
        """ localMachineId() -> QByteArray """
        pass

    def name(self): # real signature unknown; restored from __doc__
        """ name(self) -> str """
        return ""

    def objectRegisteredAt(self, path, p_str=None): # real signature unknown; restored from __doc__
        """ objectRegisteredAt(self, path: Optional[str]) -> Optional[QObject] """
        pass

    def registerObject(self, path, p_str=None, *args, **kwargs): # real signature unknown; restored from __doc__ with multiple overloads
        """
        registerObject(self, path: Optional[str], object: Optional[QObject], options: Union[QDBusConnection.RegisterOptions, QDBusConnection.RegisterOption] = QDBusConnection.ExportAdaptors) -> bool
        registerObject(self, path: Optional[str], interface: Optional[str], object: Optional[QObject], options: Union[QDBusConnection.RegisterOptions, QDBusConnection.RegisterOption] = QDBusConnection.ExportAdaptors) -> bool
        """
        pass

    def registerService(self, serviceName, p_str=None): # real signature unknown; restored from __doc__
        """ registerService(self, serviceName: Optional[str]) -> bool """
        return False

    def send(self, message): # real signature unknown; restored from __doc__
        """ send(self, message: QDBusMessage) -> bool """
        return False

    def sender(self): # real signature unknown; restored from __doc__
        """ sender() -> QDBusConnection """
        return QDBusConnection

    def sessionBus(self): # real signature unknown; restored from __doc__
        """ sessionBus() -> QDBusConnection """
        return QDBusConnection

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: QDBusConnection) """
        pass

    def systemBus(self): # real signature unknown; restored from __doc__
        """ systemBus() -> QDBusConnection """
        return QDBusConnection

    def unregisterObject(self, path, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ unregisterObject(self, path: Optional[str], mode: QDBusConnection.UnregisterMode = QDBusConnection.UnregisterNode) """
        pass

    def unregisterService(self, serviceName, p_str=None): # real signature unknown; restored from __doc__
        """ unregisterService(self, serviceName: Optional[str]) -> bool """
        return False

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    ActivationBus = 2
    ExportAdaptors = 1
    ExportAllContents = 4080
    ExportAllInvokables = 2176
    ExportAllProperties = 1088
    ExportAllSignal = 544
    ExportAllSignals = 544
    ExportAllSlots = 272
    ExportChildObjects = 4096
    ExportNonScriptableContents = 3840
    ExportNonScriptableInvokables = 2048
    ExportNonScriptableProperties = 1024
    ExportNonScriptableSignals = 512
    ExportNonScriptableSlots = 256
    ExportScriptableContents = 240
    ExportScriptableInvokables = 128
    ExportScriptableProperties = 64
    ExportScriptableSignals = 32
    ExportScriptableSlots = 16
    SessionBus = 0
    SystemBus = 1
    UnixFileDescriptorPassing = 1
    UnregisterNode = 0
    UnregisterTree = 1


class QDBusConnectionInterface(QDBusAbstractInterface):
    # no doc
    def activatableServiceNames(self): # real signature unknown; restored from __doc__
        """ activatableServiceNames(self) -> QDBusReply """
        return QDBusReply

    def callWithCallbackFailed(self, *args, **kwargs): # real signature unknown
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

    def isServiceRegistered(self, serviceName, p_str=None): # real signature unknown; restored from __doc__
        """ isServiceRegistered(self, serviceName: Optional[str]) -> QDBusReply """
        return QDBusReply

    def registeredServiceNames(self): # real signature unknown; restored from __doc__
        """ registeredServiceNames(self) -> QDBusReply """
        return QDBusReply

    def registerService(self, serviceName, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ registerService(self, serviceName: Optional[str], qoption: QDBusConnectionInterface.ServiceQueueOptions = QDBusConnectionInterface.DontQueueService, roption: QDBusConnectionInterface.ServiceReplacementOptions = QDBusConnectionInterface.DontAllowReplacement) -> QDBusReply """
        pass

    def serviceOwner(self, name, p_str=None): # real signature unknown; restored from __doc__
        """ serviceOwner(self, name: Optional[str]) -> QDBusReply """
        return QDBusReply

    def serviceOwnerChanged(self, *args, **kwargs): # real signature unknown
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

    def servicePid(self, serviceName, p_str=None): # real signature unknown; restored from __doc__
        """ servicePid(self, serviceName: Optional[str]) -> QDBusReply """
        return QDBusReply

    def serviceRegistered(self, *args, **kwargs): # real signature unknown
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

    def serviceUid(self, serviceName, p_str=None): # real signature unknown; restored from __doc__
        """ serviceUid(self, serviceName: Optional[str]) -> QDBusReply """
        return QDBusReply

    def serviceUnregistered(self, *args, **kwargs): # real signature unknown
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

    def startService(self, name, p_str=None): # real signature unknown; restored from __doc__
        """ startService(self, name: Optional[str]) -> QDBusReply """
        return QDBusReply

    def unregisterService(self, serviceName, p_str=None): # real signature unknown; restored from __doc__
        """ unregisterService(self, serviceName: Optional[str]) -> QDBusReply """
        return QDBusReply

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    AllowReplacement = 1
    DontAllowReplacement = 0
    DontQueueService = 0
    QueueService = 1
    ReplaceExistingService = 2
    ServiceNotRegistered = 0
    ServiceQueued = 2
    ServiceRegistered = 1


class QDBusError(__sip.simplewrapper):
    """ QDBusError(other: QDBusError) """
    def errorString(self, error): # real signature unknown; restored from __doc__
        """ errorString(error: QDBusError.ErrorType) -> str """
        return ""

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def message(self): # real signature unknown; restored from __doc__
        """ message(self) -> str """
        return ""

    def name(self): # real signature unknown; restored from __doc__
        """ name(self) -> str """
        return ""

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: QDBusError) """
        pass

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> QDBusError.ErrorType """
        pass

    def __init__(self, other): # real signature unknown; restored from __doc__
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    AccessDenied = 9
    AddressInUse = 13
    BadAddress = 6
    Disconnected = 14
    Failed = 2
    InternalError = 23
    InvalidArgs = 15
    InvalidInterface = 26
    InvalidMember = 27
    InvalidObjectPath = 25
    InvalidService = 24
    InvalidSignature = 18
    LimitsExceeded = 8
    NoError = 0
    NoMemory = 3
    NoNetwork = 12
    NoReply = 5
    NoServer = 10
    NotSupported = 7
    Other = 1
    PropertyReadOnly = 22
    ServiceUnknown = 4
    TimedOut = 17
    Timeout = 11
    UnknownInterface = 19
    UnknownMethod = 16
    UnknownObject = 20
    UnknownProperty = 21


class QDBusInterface(QDBusAbstractInterface):
    """ QDBusInterface(service: Optional[str], path: Optional[str], interface: Optional[str] = '', connection: QDBusConnection = QDBusConnection.sessionBus(), parent: Optional[QObject] = None) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, service, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass


class QDBusMessage(__sip.simplewrapper):
    """
    QDBusMessage()
    QDBusMessage(other: QDBusMessage)
    """
    def arguments(self): # real signature unknown; restored from __doc__
        """ arguments(self) -> List[Any] """
        return []

    def autoStartService(self): # real signature unknown; restored from __doc__
        """ autoStartService(self) -> bool """
        return False

    def createError(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        createError(name: Optional[str], msg: Optional[str]) -> QDBusMessage
        createError(error: QDBusError) -> QDBusMessage
        createError(type: QDBusError.ErrorType, msg: Optional[str]) -> QDBusMessage
        """
        return QDBusMessage

    def createErrorReply(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        createErrorReply(self, name: Optional[str], msg: Optional[str]) -> QDBusMessage
        createErrorReply(self, error: QDBusError) -> QDBusMessage
        createErrorReply(self, type: QDBusError.ErrorType, msg: Optional[str]) -> QDBusMessage
        """
        return QDBusMessage

    def createMethodCall(self, service, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ createMethodCall(service: Optional[str], path: Optional[str], interface: Optional[str], method: Optional[str]) -> QDBusMessage """
        pass

    def createReply(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        createReply(self, arguments: Iterable[Any] = []) -> QDBusMessage
        createReply(self, argument: Any) -> QDBusMessage
        """
        return QDBusMessage

    def createSignal(self, path, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ createSignal(path: Optional[str], interface: Optional[str], name: Optional[str]) -> QDBusMessage """
        pass

    def createTargetedSignal(self, service, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ createTargetedSignal(service: Optional[str], path: Optional[str], interface: Optional[str], name: Optional[str]) -> QDBusMessage """
        pass

    def errorMessage(self): # real signature unknown; restored from __doc__
        """ errorMessage(self) -> str """
        return ""

    def errorName(self): # real signature unknown; restored from __doc__
        """ errorName(self) -> str """
        return ""

    def interface(self): # real signature unknown; restored from __doc__
        """ interface(self) -> str """
        return ""

    def isDelayedReply(self): # real signature unknown; restored from __doc__
        """ isDelayedReply(self) -> bool """
        return False

    def isInteractiveAuthorizationAllowed(self): # real signature unknown; restored from __doc__
        """ isInteractiveAuthorizationAllowed(self) -> bool """
        return False

    def isReplyRequired(self): # real signature unknown; restored from __doc__
        """ isReplyRequired(self) -> bool """
        return False

    def member(self): # real signature unknown; restored from __doc__
        """ member(self) -> str """
        return ""

    def path(self): # real signature unknown; restored from __doc__
        """ path(self) -> str """
        return ""

    def service(self): # real signature unknown; restored from __doc__
        """ service(self) -> str """
        return ""

    def setArguments(self, arguments, Any=None): # real signature unknown; restored from __doc__
        """ setArguments(self, arguments: Iterable[Any]) """
        pass

    def setAutoStartService(self, enable): # real signature unknown; restored from __doc__
        """ setAutoStartService(self, enable: bool) """
        pass

    def setDelayedReply(self, enable): # real signature unknown; restored from __doc__
        """ setDelayedReply(self, enable: bool) """
        pass

    def setInteractiveAuthorizationAllowed(self, enable): # real signature unknown; restored from __doc__
        """ setInteractiveAuthorizationAllowed(self, enable: bool) """
        pass

    def signature(self): # real signature unknown; restored from __doc__
        """ signature(self) -> str """
        return ""

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: QDBusMessage) """
        pass

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> QDBusMessage.MessageType """
        pass

    def __init__(self, other=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __lshift__(self, *args, **kwargs): # real signature unknown
        """ Return self<<value. """
        pass

    def __rlshift__(self, *args, **kwargs): # real signature unknown
        """ Return value<<self. """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    ErrorMessage = 3
    InvalidMessage = 0
    MethodCallMessage = 1
    ReplyMessage = 2
    SignalMessage = 4


class QDBusObjectPath(__sip.simplewrapper):
    """
    QDBusObjectPath()
    QDBusObjectPath(objectPath: Optional[str])
    QDBusObjectPath(a0: QDBusObjectPath)
    """
    def path(self): # real signature unknown; restored from __doc__
        """ path(self) -> str """
        return ""

    def setPath(self, objectPath, p_str=None): # real signature unknown; restored from __doc__
        """ setPath(self, objectPath: Optional[str]) """
        pass

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: QDBusObjectPath) """
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



class QDBusPendingCall(__sip.simplewrapper):
    """ QDBusPendingCall(other: QDBusPendingCall) """
    def fromCompletedCall(self, message): # real signature unknown; restored from __doc__
        """ fromCompletedCall(message: QDBusMessage) -> QDBusPendingCall """
        return QDBusPendingCall

    def fromError(self, error): # real signature unknown; restored from __doc__
        """ fromError(error: QDBusError) -> QDBusPendingCall """
        return QDBusPendingCall

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: QDBusPendingCall) """
        pass

    def __init__(self, other): # real signature unknown; restored from __doc__
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QDBusPendingCallWatcher(__PyQt5_QtCore.QObject, QDBusPendingCall):
    """ QDBusPendingCallWatcher(call: QDBusPendingCall, parent: Optional[QObject] = None) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

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

    def isFinished(self): # real signature unknown; restored from __doc__
        """ isFinished(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def waitForFinished(self): # real signature unknown; restored from __doc__
        """ waitForFinished(self) """
        pass

    def __init__(self, call, parent, QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass


class QDBusPendingReply(QDBusPendingCall):
    """
    QDBusPendingReply()
    QDBusPendingReply(other: QDBusPendingReply)
    QDBusPendingReply(call: QDBusPendingCall)
    QDBusPendingReply(reply: QDBusMessage)
    """
    def argumentAt(self, index): # real signature unknown; restored from __doc__
        """ argumentAt(self, index: int) -> Any """
        pass

    def error(self): # real signature unknown; restored from __doc__
        """ error(self) -> QDBusError """
        return QDBusError

    def isError(self): # real signature unknown; restored from __doc__
        """ isError(self) -> bool """
        return False

    def isFinished(self): # real signature unknown; restored from __doc__
        """ isFinished(self) -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def reply(self): # real signature unknown; restored from __doc__
        """ reply(self) -> QDBusMessage """
        return QDBusMessage

    def value(self, type=None): # real signature unknown; restored from __doc__
        """ value(self, type: Any = None) -> Any """
        pass

    def waitForFinished(self): # real signature unknown; restored from __doc__
        """ waitForFinished(self) """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


class QDBusReply(__sip.simplewrapper):
    """
    QDBusReply(reply: QDBusMessage)
    QDBusReply(call: QDBusPendingCall)
    QDBusReply(error: QDBusError)
    QDBusReply(other: QDBusReply)
    """
    def error(self): # real signature unknown; restored from __doc__
        """ error(self) -> QDBusError """
        return QDBusError

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def value(self, type=None): # real signature unknown; restored from __doc__
        """ value(self, type: Any = None) -> Any """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QDBusServiceWatcher(__PyQt5_QtCore.QObject):
    """
    QDBusServiceWatcher(parent: Optional[QObject] = None)
    QDBusServiceWatcher(service: Optional[str], connection: QDBusConnection, watchMode: Union[QDBusServiceWatcher.WatchMode, QDBusServiceWatcher.WatchModeFlag] = QDBusServiceWatcher.WatchForOwnerChange, parent: Optional[QObject] = None)
    """
    def addWatchedService(self, newService, p_str=None): # real signature unknown; restored from __doc__
        """ addWatchedService(self, newService: Optional[str]) """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connection(self): # real signature unknown; restored from __doc__
        """ connection(self) -> QDBusConnection """
        return QDBusConnection

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def removeWatchedService(self, service, p_str=None): # real signature unknown; restored from __doc__
        """ removeWatchedService(self, service: Optional[str]) -> bool """
        return False

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def serviceOwnerChanged(self, *args, **kwargs): # real signature unknown
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

    def serviceRegistered(self, *args, **kwargs): # real signature unknown
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

    def serviceUnregistered(self, *args, **kwargs): # real signature unknown
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

    def setConnection(self, connection): # real signature unknown; restored from __doc__
        """ setConnection(self, connection: QDBusConnection) """
        pass

    def setWatchedServices(self, services, Optional=None, p_str=None): # real signature unknown; restored from __doc__
        """ setWatchedServices(self, services: Iterable[Optional[str]]) """
        pass

    def setWatchMode(self, mode, QDBusServiceWatcher_WatchMode=None, QDBusServiceWatcher_WatchModeFlag=None): # real signature unknown; restored from __doc__
        """ setWatchMode(self, mode: Union[QDBusServiceWatcher.WatchMode, QDBusServiceWatcher.WatchModeFlag]) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def watchedServices(self): # real signature unknown; restored from __doc__
        """ watchedServices(self) -> List[str] """
        return []

    def watchMode(self): # real signature unknown; restored from __doc__
        """ watchMode(self) -> QDBusServiceWatcher.WatchMode """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    WatchForOwnerChange = 3
    WatchForRegistration = 1
    WatchForUnregistration = 2


class QDBusSignature(__sip.simplewrapper):
    """
    QDBusSignature()
    QDBusSignature(dBusSignature: Optional[str])
    QDBusSignature(a0: QDBusSignature)
    """
    def setSignature(self, dBusSignature, p_str=None): # real signature unknown; restored from __doc__
        """ setSignature(self, dBusSignature: Optional[str]) """
        pass

    def signature(self): # real signature unknown; restored from __doc__
        """ signature(self) -> str """
        return ""

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: QDBusSignature) """
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



class QDBusUnixFileDescriptor(__sip.simplewrapper):
    """
    QDBusUnixFileDescriptor()
    QDBusUnixFileDescriptor(fileDescriptor: int)
    QDBusUnixFileDescriptor(other: QDBusUnixFileDescriptor)
    """
    def fileDescriptor(self): # real signature unknown; restored from __doc__
        """ fileDescriptor(self) -> int """
        return 0

    def isSupported(self): # real signature unknown; restored from __doc__
        """ isSupported() -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def setFileDescriptor(self, fileDescriptor): # real signature unknown; restored from __doc__
        """ setFileDescriptor(self, fileDescriptor: int) """
        pass

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: QDBusUnixFileDescriptor) """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QDBusVariant(__sip.simplewrapper):
    """
    QDBusVariant()
    QDBusVariant(dBusVariant: Any)
    QDBusVariant(a0: QDBusVariant)
    """
    def setVariant(self, dBusVariant): # real signature unknown; restored from __doc__
        """ setVariant(self, dBusVariant: Any) """
        pass

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: QDBusVariant) """
        pass

    def variant(self): # real signature unknown; restored from __doc__
        """ variant(self) -> Any """
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


    __hash__ = None


# variables with complex values



