# encoding: utf-8
# module PyQt5.QtRemoteObjects
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtRemoteObjects.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


# no functions
# classes

class QAbstractItemModelReplica(__PyQt5_QtCore.QAbstractItemModel):
    # no doc
    def availableRoles(self): # real signature unknown; restored from __doc__
        """ availableRoles(self) -> List[int] """
        return []

    def columnCount(self, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ columnCount(self, parent: QModelIndex = QModelIndex()) -> int """
        pass

    def data(self, index, role=None): # real signature unknown; restored from __doc__
        """ data(self, index: QModelIndex, role: int = Qt.ItemDataRole.DisplayRole) -> Any """
        pass

    def flags(self, index): # real signature unknown; restored from __doc__
        """ flags(self, index: QModelIndex) -> Qt.ItemFlags """
        pass

    def hasChildren(self, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ hasChildren(self, parent: QModelIndex = QModelIndex()) -> bool """
        pass

    def hasData(self, index, role): # real signature unknown; restored from __doc__
        """ hasData(self, index: QModelIndex, role: int) -> bool """
        return False

    def headerData(self, section, orientation, role): # real signature unknown; restored from __doc__
        """ headerData(self, section: int, orientation: Qt.Orientation, role: int) -> Any """
        pass

    def index(self, row, column, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ index(self, row: int, column: int, parent: QModelIndex = QModelIndex()) -> QModelIndex """
        pass

    def initialized(self, *args, **kwargs): # real signature unknown
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

    def isInitialized(self): # real signature unknown; restored from __doc__
        """ isInitialized(self) -> bool """
        return False

    def parent(self, index): # real signature unknown; restored from __doc__
        """ parent(self, index: QModelIndex) -> QModelIndex """
        pass

    def roleNames(self): # real signature unknown; restored from __doc__
        """ roleNames(self) -> Dict[int, QByteArray] """
        return {}

    def rootCacheSize(self): # real signature unknown; restored from __doc__
        """ rootCacheSize(self) -> int """
        return 0

    def rowCount(self, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ rowCount(self, parent: QModelIndex = QModelIndex()) -> int """
        pass

    def selectionModel(self): # real signature unknown; restored from __doc__
        """ selectionModel(self) -> Optional[QItemSelectionModel] """
        pass

    def setData(self, index, value, role=None): # real signature unknown; restored from __doc__
        """ setData(self, index: QModelIndex, value: Any, role: int = Qt.ItemDataRole.EditRole) -> bool """
        return False

    def setRootCacheSize(self, rootCacheSize): # real signature unknown; restored from __doc__
        """ setRootCacheSize(self, rootCacheSize: int) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class QRemoteObjectAbstractPersistedStore(__PyQt5_QtCore.QObject):
    """ QRemoteObjectAbstractPersistedStore(parent: Optional[QObject] = None) """
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

    def restoreProperties(self, repName, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ restoreProperties(self, repName: Optional[str], repSig: Union[QByteArray, bytes, bytearray]) -> List[Any] """
        pass

    def saveProperties(self, repName, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ saveProperties(self, repName: Optional[str], repSig: Union[QByteArray, bytes, bytearray], values: Iterable[Any]) """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent, QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass


class QRemoteObjectReplica(__PyQt5_QtCore.QObject):
    # no doc
    def initialized(self, *args, **kwargs): # real signature unknown
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

    def isInitialized(self): # real signature unknown; restored from __doc__
        """ isInitialized(self) -> bool """
        return False

    def isReplicaValid(self): # real signature unknown; restored from __doc__
        """ isReplicaValid(self) -> bool """
        return False

    def node(self): # real signature unknown; restored from __doc__
        """ node(self) -> Optional[QRemoteObjectNode] """
        pass

    def notified(self, *args, **kwargs): # real signature unknown
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

    def setNode(self, node, QRemoteObjectNode=None): # real signature unknown; restored from __doc__
        """ setNode(self, node: Optional[QRemoteObjectNode]) """
        pass

    def state(self): # real signature unknown; restored from __doc__
        """ state(self) -> QRemoteObjectReplica.State """
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

    def waitForSource(self, timeout=30000): # real signature unknown; restored from __doc__
        """ waitForSource(self, timeout: int = 30000) -> bool """
        return False

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    Default = 1
    SignatureMismatch = 4
    Suspect = 3
    Uninitialized = 0
    Valid = 2


class QRemoteObjectDynamicReplica(QRemoteObjectReplica):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class QRemoteObjectNode(__PyQt5_QtCore.QObject):
    """
    QRemoteObjectNode(parent: Optional[QObject] = None)
    QRemoteObjectNode(registryAddress: QUrl, parent: Optional[QObject] = None)
    """
    def acquireDynamic(self, name, p_str=None): # real signature unknown; restored from __doc__
        """ acquireDynamic(self, name: Optional[str]) -> Optional[QRemoteObjectDynamicReplica] """
        pass

    def acquireModel(self, name, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ acquireModel(self, name: Optional[str], action: QtRemoteObjects.InitialAction = QtRemoteObjects.FetchRootSize, rolesHint: Iterable[int] = []) -> Optional[QAbstractItemModelReplica] """
        pass

    def addClientSideConnection(self, ioDevice, QIODevice=None): # real signature unknown; restored from __doc__
        """ addClientSideConnection(self, ioDevice: Optional[QIODevice]) """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def connectToNode(self, address): # real signature unknown; restored from __doc__
        """ connectToNode(self, address: QUrl) -> bool """
        return False

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
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

    def heartbeatInterval(self): # real signature unknown; restored from __doc__
        """ heartbeatInterval(self) -> int """
        return 0

    def heartbeatIntervalChanged(self, *args, **kwargs): # real signature unknown
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

    def instances(self, typeName, p_str=None): # real signature unknown; restored from __doc__
        """ instances(self, typeName: Optional[str]) -> List[str] """
        return []

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def lastError(self): # real signature unknown; restored from __doc__
        """ lastError(self) -> QRemoteObjectNode.ErrorCode """
        pass

    def persistedStore(self): # real signature unknown; restored from __doc__
        """ persistedStore(self) -> Optional[QRemoteObjectAbstractPersistedStore] """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def registry(self): # real signature unknown; restored from __doc__
        """ registry(self) -> Optional[QRemoteObjectRegistry] """
        pass

    def registryUrl(self): # real signature unknown; restored from __doc__
        """ registryUrl(self) -> QUrl """
        pass

    def remoteObjectAdded(self, *args, **kwargs): # real signature unknown
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

    def remoteObjectRemoved(self, *args, **kwargs): # real signature unknown
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

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setHeartbeatInterval(self, interval): # real signature unknown; restored from __doc__
        """ setHeartbeatInterval(self, interval: int) """
        pass

    def setName(self, name, p_str=None): # real signature unknown; restored from __doc__
        """ setName(self, name: Optional[str]) """
        pass

    def setPersistedStore(self, persistedStore, QRemoteObjectAbstractPersistedStore=None): # real signature unknown; restored from __doc__
        """ setPersistedStore(self, persistedStore: Optional[QRemoteObjectAbstractPersistedStore]) """
        pass

    def setRegistryUrl(self, registryAddress): # real signature unknown; restored from __doc__
        """ setRegistryUrl(self, registryAddress: QUrl) -> bool """
        return False

    def timerEvent(self, a0, QTimerEvent=None): # real signature unknown; restored from __doc__
        """ timerEvent(self, a0: Optional[QTimerEvent]) """
        pass

    def waitForRegistry(self, timeout=30000): # real signature unknown; restored from __doc__
        """ waitForRegistry(self, timeout: int = 30000) -> bool """
        return False

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    HostUrlInvalid = 9
    ListenFailed = 11
    MissingObjectName = 8
    NodeIsNoServer = 3
    NoError = 0
    OperationNotValidOnClientNode = 6
    ProtocolMismatch = 10
    RegistryAlreadyHosted = 2
    RegistryNotAcquired = 1
    ServerAlreadyCreated = 4
    SourceNotRegistered = 7
    UnintendedRegistryHosting = 5


class QRemoteObjectHostBase(QRemoteObjectNode):
    # no doc
    def addHostSideConnection(self, ioDevice, QIODevice=None): # real signature unknown; restored from __doc__
        """ addHostSideConnection(self, ioDevice: Optional[QIODevice]) """
        pass

    def disableRemoting(self, remoteObject, QObject=None): # real signature unknown; restored from __doc__
        """ disableRemoting(self, remoteObject: Optional[QObject]) -> bool """
        return False

    def enableRemoting(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        enableRemoting(self, object: Optional[QObject], name: Optional[str] = '') -> bool
        enableRemoting(self, model: Optional[QAbstractItemModel], name: Optional[str], roles: Iterable[int], selectionModel: Optional[QItemSelectionModel] = None) -> bool
        """
        pass

    def proxy(self, registryUrl, hostUrl=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ proxy(self, registryUrl: QUrl, hostUrl: QUrl = QUrl()) -> bool """
        pass

    def reverseProxy(self): # real signature unknown; restored from __doc__
        """ reverseProxy(self) -> bool """
        return False

    def setName(self, name, p_str=None): # real signature unknown; restored from __doc__
        """ setName(self, name: Optional[str]) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    AllowExternalRegistration = 1
    BuiltInSchemasOnly = 0


class QRemoteObjectHost(QRemoteObjectHostBase):
    """
    QRemoteObjectHost(parent: Optional[QObject] = None)
    QRemoteObjectHost(address: QUrl, registryAddress: QUrl = QUrl(), allowedSchemas: QRemoteObjectHostBase.AllowedSchemas = QRemoteObjectHostBase.BuiltInSchemasOnly, parent: Optional[QObject] = None)
    QRemoteObjectHost(address: QUrl, parent: Optional[QObject])
    """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def hostUrl(self): # real signature unknown; restored from __doc__
        """ hostUrl(self) -> QUrl """
        pass

    def hostUrlChanged(self, *args, **kwargs): # real signature unknown
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

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setHostUrl(self, hostAddress, allowedSchemas=None): # real signature unknown; restored from __doc__
        """ setHostUrl(self, hostAddress: QUrl, allowedSchemas: QRemoteObjectHostBase.AllowedSchemas = QRemoteObjectHostBase.BuiltInSchemasOnly) -> bool """
        return False

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


class QRemoteObjectRegistry(QRemoteObjectReplica):
    # no doc
    def remoteObjectAdded(self, *args, **kwargs): # real signature unknown
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

    def remoteObjectRemoved(self, *args, **kwargs): # real signature unknown
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

    def sourceLocations(self): # real signature unknown; restored from __doc__
        """ sourceLocations(self) -> Dict[str, QRemoteObjectSourceLocationInfo] """
        return {}

    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class QRemoteObjectRegistryHost(QRemoteObjectHostBase):
    """ QRemoteObjectRegistryHost(registryAddress: QUrl = QUrl(), parent: Optional[QObject] = None) """
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

    def setRegistryUrl(self, registryUrl): # real signature unknown; restored from __doc__
        """ setRegistryUrl(self, registryUrl: QUrl) -> bool """
        return False

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, registryAddress=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass


class QRemoteObjectSourceLocationInfo(__sip.simplewrapper):
    """
    QRemoteObjectSourceLocationInfo()
    QRemoteObjectSourceLocationInfo(typeName_: Optional[str], hostUrl_: QUrl)
    QRemoteObjectSourceLocationInfo(a0: QRemoteObjectSourceLocationInfo)
    """
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


class QtRemoteObjects(__sip.simplewrapper):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    FetchRootSize = 0
    PrefetchData = 1


# variables with complex values



