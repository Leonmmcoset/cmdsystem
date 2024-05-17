# encoding: utf-8
# module PyQt5.QtNfc
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtNfc.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


# no functions
# classes

class QNdefFilter(__sip.simplewrapper):
    """
    QNdefFilter()
    QNdefFilter(other: QNdefFilter)
    """
    def appendRecord(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        appendRecord(self, typeNameFormat: QNdefRecord.TypeNameFormat, type: Union[QByteArray, bytes, bytearray], min: int = 1, max: int = 1)
        appendRecord(self, record: QNdefFilter.Record)
        """
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def orderMatch(self): # real signature unknown; restored from __doc__
        """ orderMatch(self) -> bool """
        return False

    def recordAt(self, i): # real signature unknown; restored from __doc__
        """ recordAt(self, i: int) -> QNdefFilter.Record """
        pass

    def recordCount(self): # real signature unknown; restored from __doc__
        """ recordCount(self) -> int """
        return 0

    def setOrderMatch(self, on): # real signature unknown; restored from __doc__
        """ setOrderMatch(self, on: bool) """
        pass

    def __init__(self, other=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""




class QNdefMessage(__sip.simplewrapper):
    """
    QNdefMessage()
    QNdefMessage(record: QNdefRecord)
    QNdefMessage(message: QNdefMessage)
    QNdefMessage(records: Iterable[QNdefRecord])
    """
    def fromByteArray(self, message, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ fromByteArray(message: Union[QByteArray, bytes, bytearray]) -> QNdefMessage """
        return QNdefMessage

    def toByteArray(self): # real signature unknown; restored from __doc__
        """ toByteArray(self) -> QByteArray """
        pass

    def __delitem__(self, *args, **kwargs): # real signature unknown
        """ Delete self[key]. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
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

    def __setitem__(self, *args, **kwargs): # real signature unknown
        """ Set self[key] to value. """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __hash__ = None


class QNdefRecord(__sip.simplewrapper):
    """
    QNdefRecord()
    QNdefRecord(other: QNdefRecord)
    """
    def id(self): # real signature unknown; restored from __doc__
        """ id(self) -> QByteArray """
        pass

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ isEmpty(self) -> bool """
        return False

    def payload(self): # real signature unknown; restored from __doc__
        """ payload(self) -> QByteArray """
        pass

    def setId(self, id, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ setId(self, id: Union[QByteArray, bytes, bytearray]) """
        pass

    def setPayload(self, payload, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ setPayload(self, payload: Union[QByteArray, bytes, bytearray]) """
        pass

    def setType(self, type, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ setType(self, type: Union[QByteArray, bytes, bytearray]) """
        pass

    def setTypeNameFormat(self, typeNameFormat): # real signature unknown; restored from __doc__
        """ setTypeNameFormat(self, typeNameFormat: QNdefRecord.TypeNameFormat) """
        pass

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> QByteArray """
        pass

    def typeNameFormat(self): # real signature unknown; restored from __doc__
        """ typeNameFormat(self) -> QNdefRecord.TypeNameFormat """
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


    Empty = 0
    ExternalRtd = 4
    Mime = 2
    NfcRtd = 1
    Unknown = 5
    Uri = 3


class QNdefNfcIconRecord(QNdefRecord):
    """
    QNdefNfcIconRecord()
    QNdefNfcIconRecord(other: QNdefRecord)
    QNdefNfcIconRecord(a0: QNdefNfcIconRecord)
    """
    def data(self): # real signature unknown; restored from __doc__
        """ data(self) -> QByteArray """
        pass

    def setData(self, data, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ setData(self, data: Union[QByteArray, bytes, bytearray]) """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


class QNdefNfcSmartPosterRecord(QNdefRecord):
    """
    QNdefNfcSmartPosterRecord()
    QNdefNfcSmartPosterRecord(other: QNdefNfcSmartPosterRecord)
    QNdefNfcSmartPosterRecord(other: QNdefRecord)
    """
    def action(self): # real signature unknown; restored from __doc__
        """ action(self) -> QNdefNfcSmartPosterRecord.Action """
        pass

    def addIcon(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        addIcon(self, icon: QNdefNfcIconRecord)
        addIcon(self, type: Union[QByteArray, bytes, bytearray], data: Union[QByteArray, bytes, bytearray])
        """
        pass

    def addTitle(self, text, p_str=None, *args=None, **kwargs=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        addTitle(self, text: QNdefNfcTextRecord) -> bool
        addTitle(self, text: Optional[str], locale: Optional[str], encoding: QNdefNfcTextRecord.Encoding) -> bool
        """
        return False

    def hasAction(self): # real signature unknown; restored from __doc__
        """ hasAction(self) -> bool """
        return False

    def hasIcon(self, mimetype, QByteArray=None, bytes=None, bytearray=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ hasIcon(self, mimetype: Union[QByteArray, bytes, bytearray] = QByteArray()) -> bool """
        pass

    def hasSize(self): # real signature unknown; restored from __doc__
        """ hasSize(self) -> bool """
        return False

    def hasTitle(self, locale, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ hasTitle(self, locale: Optional[str] = '') -> bool """
        pass

    def hasTypeInfo(self): # real signature unknown; restored from __doc__
        """ hasTypeInfo(self) -> bool """
        return False

    def icon(self, mimetype, QByteArray=None, bytes=None, bytearray=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ icon(self, mimetype: Union[QByteArray, bytes, bytearray] = QByteArray()) -> QByteArray """
        pass

    def iconCount(self): # real signature unknown; restored from __doc__
        """ iconCount(self) -> int """
        return 0

    def iconRecord(self, index): # real signature unknown; restored from __doc__
        """ iconRecord(self, index: int) -> QNdefNfcIconRecord """
        return QNdefNfcIconRecord

    def iconRecords(self): # real signature unknown; restored from __doc__
        """ iconRecords(self) -> List[QNdefNfcIconRecord] """
        return []

    def removeIcon(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        removeIcon(self, icon: QNdefNfcIconRecord) -> bool
        removeIcon(self, type: Union[QByteArray, bytes, bytearray]) -> bool
        """
        return False

    def removeTitle(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        removeTitle(self, text: QNdefNfcTextRecord) -> bool
        removeTitle(self, locale: Optional[str]) -> bool
        """
        return False

    def setAction(self, act): # real signature unknown; restored from __doc__
        """ setAction(self, act: QNdefNfcSmartPosterRecord.Action) """
        pass

    def setIcons(self, icons, QNdefNfcIconRecord=None): # real signature unknown; restored from __doc__
        """ setIcons(self, icons: Iterable[QNdefNfcIconRecord]) """
        pass

    def setPayload(self, payload, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ setPayload(self, payload: Union[QByteArray, bytes, bytearray]) """
        pass

    def setSize(self, size): # real signature unknown; restored from __doc__
        """ setSize(self, size: int) """
        pass

    def setTitles(self, titles, QNdefNfcTextRecord=None): # real signature unknown; restored from __doc__
        """ setTitles(self, titles: Iterable[QNdefNfcTextRecord]) """
        pass

    def setTypeInfo(self, type, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ setTypeInfo(self, type: Union[QByteArray, bytes, bytearray]) """
        pass

    def setUri(self, url): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setUri(self, url: QNdefNfcUriRecord)
        setUri(self, url: QUrl)
        """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ size(self) -> int """
        return 0

    def title(self, locale, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ title(self, locale: Optional[str] = '') -> str """
        pass

    def titleCount(self): # real signature unknown; restored from __doc__
        """ titleCount(self) -> int """
        return 0

    def titleRecord(self, index): # real signature unknown; restored from __doc__
        """ titleRecord(self, index: int) -> QNdefNfcTextRecord """
        return QNdefNfcTextRecord

    def titleRecords(self): # real signature unknown; restored from __doc__
        """ titleRecords(self) -> List[QNdefNfcTextRecord] """
        return []

    def typeInfo(self): # real signature unknown; restored from __doc__
        """ typeInfo(self) -> QByteArray """
        pass

    def uri(self): # real signature unknown; restored from __doc__
        """ uri(self) -> QUrl """
        pass

    def uriRecord(self): # real signature unknown; restored from __doc__
        """ uriRecord(self) -> QNdefNfcUriRecord """
        return QNdefNfcUriRecord

    def __init__(self, other=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    DoAction = 0
    EditAction = 2
    SaveAction = 1
    UnspecifiedAction = -1


class QNdefNfcTextRecord(QNdefRecord):
    """
    QNdefNfcTextRecord()
    QNdefNfcTextRecord(other: QNdefRecord)
    QNdefNfcTextRecord(a0: QNdefNfcTextRecord)
    """
    def encoding(self): # real signature unknown; restored from __doc__
        """ encoding(self) -> QNdefNfcTextRecord.Encoding """
        pass

    def locale(self): # real signature unknown; restored from __doc__
        """ locale(self) -> str """
        return ""

    def setEncoding(self, encoding): # real signature unknown; restored from __doc__
        """ setEncoding(self, encoding: QNdefNfcTextRecord.Encoding) """
        pass

    def setLocale(self, locale, p_str=None): # real signature unknown; restored from __doc__
        """ setLocale(self, locale: Optional[str]) """
        pass

    def setText(self, text, p_str=None): # real signature unknown; restored from __doc__
        """ setText(self, text: Optional[str]) """
        pass

    def text(self): # real signature unknown; restored from __doc__
        """ text(self) -> str """
        return ""

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    Utf16 = 1
    Utf8 = 0


class QNdefNfcUriRecord(QNdefRecord):
    """
    QNdefNfcUriRecord()
    QNdefNfcUriRecord(other: QNdefRecord)
    QNdefNfcUriRecord(a0: QNdefNfcUriRecord)
    """
    def setUri(self, uri): # real signature unknown; restored from __doc__
        """ setUri(self, uri: QUrl) """
        pass

    def uri(self): # real signature unknown; restored from __doc__
        """ uri(self) -> QUrl """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


class QNearFieldManager(__PyQt5_QtCore.QObject):
    """ QNearFieldManager(parent: Optional[QObject] = None) """
    def adapterStateChanged(self, *args, **kwargs): # real signature unknown
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

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def isAvailable(self): # real signature unknown; restored from __doc__
        """ isAvailable(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def isSupported(self): # real signature unknown; restored from __doc__
        """ isSupported(self) -> bool """
        return False

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def registerNdefMessageHandler(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        registerNdefMessageHandler(self, slot: PYQT_SLOT) -> int
        registerNdefMessageHandler(self, typeNameFormat: QNdefRecord.TypeNameFormat, type: Union[QByteArray, bytes, bytearray], slot: PYQT_SLOT) -> int
        registerNdefMessageHandler(self, filter: QNdefFilter, slot: PYQT_SLOT) -> int
        """
        return 0

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setTargetAccessModes(self, accessModes, QNearFieldManager_TargetAccessModes=None, QNearFieldManager_TargetAccessMode=None): # real signature unknown; restored from __doc__
        """ setTargetAccessModes(self, accessModes: Union[QNearFieldManager.TargetAccessModes, QNearFieldManager.TargetAccessMode]) """
        pass

    def startTargetDetection(self): # real signature unknown; restored from __doc__
        """ startTargetDetection(self) -> bool """
        return False

    def stopTargetDetection(self): # real signature unknown; restored from __doc__
        """ stopTargetDetection(self) """
        pass

    def targetAccessModes(self): # real signature unknown; restored from __doc__
        """ targetAccessModes(self) -> QNearFieldManager.TargetAccessModes """
        pass

    def targetDetected(self, *args, **kwargs): # real signature unknown
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

    def targetLost(self, *args, **kwargs): # real signature unknown
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

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def unregisterNdefMessageHandler(self, handlerId): # real signature unknown; restored from __doc__
        """ unregisterNdefMessageHandler(self, handlerId: int) -> bool """
        return False

    def __init__(self, parent, QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    NdefReadTargetAccess = 1
    NdefWriteTargetAccess = 2
    NoTargetAccess = 0
    TagTypeSpecificTargetAccess = 4


class QNearFieldShareManager(__PyQt5_QtCore.QObject):
    """ QNearFieldShareManager(parent: Optional[QObject] = None) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

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

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setShareModes(self, modes, QNearFieldShareManager_ShareModes=None, QNearFieldShareManager_ShareMode=None): # real signature unknown; restored from __doc__
        """ setShareModes(self, modes: Union[QNearFieldShareManager.ShareModes, QNearFieldShareManager.ShareMode]) """
        pass

    def shareError(self): # real signature unknown; restored from __doc__
        """ shareError(self) -> QNearFieldShareManager.ShareError """
        pass

    def shareModes(self): # real signature unknown; restored from __doc__
        """ shareModes(self) -> QNearFieldShareManager.ShareModes """
        pass

    def shareModesChanged(self, *args, **kwargs): # real signature unknown
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

    def supportedShareModes(self): # real signature unknown; restored from __doc__
        """ supportedShareModes() -> QNearFieldShareManager.ShareModes """
        pass

    def targetDetected(self, *args, **kwargs): # real signature unknown
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

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent, QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    FileShare = 2
    InvalidShareContentError = 2
    NdefShare = 1
    NoError = 0
    NoShare = 0
    ShareAlreadyInProgressError = 7
    ShareCanceledError = 3
    ShareInterruptedError = 4
    SharePermissionDeniedError = 8
    ShareRejectedError = 5
    UnknownError = 1
    UnsupportedShareModeError = 6


class QNearFieldShareTarget(__PyQt5_QtCore.QObject):
    # no doc
    def cancel(self): # real signature unknown; restored from __doc__
        """ cancel(self) """
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

    def isShareInProgress(self): # real signature unknown; restored from __doc__
        """ isShareInProgress(self) -> bool """
        return False

    def share(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        share(self, message: QNdefMessage) -> bool
        share(self, files: Iterable[QFileInfo]) -> bool
        """
        return False

    def shareError(self): # real signature unknown; restored from __doc__
        """ shareError(self) -> QNearFieldShareManager.ShareError """
        pass

    def shareFinished(self, *args, **kwargs): # real signature unknown
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

    def shareModes(self): # real signature unknown; restored from __doc__
        """ shareModes(self) -> QNearFieldShareManager.ShareModes """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class QNearFieldTarget(__PyQt5_QtCore.QObject):
    """ QNearFieldTarget(parent: Optional[QObject] = None) """
    def accessMethods(self): # real signature unknown; restored from __doc__
        """ accessMethods(self) -> QNearFieldTarget.AccessMethods """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnect(self): # real signature unknown; restored from __doc__
        """ disconnect(self) -> bool """
        return False

    def disconnected(self, *args, **kwargs): # real signature unknown
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

    def handleResponse(self, id, response, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ handleResponse(self, id: QNearFieldTarget.RequestId, response: Union[QByteArray, bytes, bytearray]) -> bool """
        return False

    def hasNdefMessage(self): # real signature unknown; restored from __doc__
        """ hasNdefMessage(self) -> bool """
        return False

    def isProcessingCommand(self): # real signature unknown; restored from __doc__
        """ isProcessingCommand(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def keepConnection(self): # real signature unknown; restored from __doc__
        """ keepConnection(self) -> bool """
        return False

    def maxCommandLength(self): # real signature unknown; restored from __doc__
        """ maxCommandLength(self) -> int """
        return 0

    def ndefMessageRead(self, *args, **kwargs): # real signature unknown
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

    def ndefMessagesWritten(self, *args, **kwargs): # real signature unknown
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

    def readNdefMessages(self): # real signature unknown; restored from __doc__
        """ readNdefMessages(self) -> QNearFieldTarget.RequestId """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def reportError(self, error, id): # real signature unknown; restored from __doc__
        """ reportError(self, error: QNearFieldTarget.Error, id: QNearFieldTarget.RequestId) """
        pass

    def requestCompleted(self, *args, **kwargs): # real signature unknown
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

    def requestResponse(self, id): # real signature unknown; restored from __doc__
        """ requestResponse(self, id: QNearFieldTarget.RequestId) -> Any """
        pass

    def sendCommand(self, command, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ sendCommand(self, command: Union[QByteArray, bytes, bytearray]) -> QNearFieldTarget.RequestId """
        pass

    def sendCommands(self, commands, Union=None, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ sendCommands(self, commands: Iterable[Union[QByteArray, bytes, bytearray]]) -> QNearFieldTarget.RequestId """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setKeepConnection(self, isPersistent): # real signature unknown; restored from __doc__
        """ setKeepConnection(self, isPersistent: bool) -> bool """
        return False

    def setResponseForRequest(self, id, response, emitRequestCompleted=True): # real signature unknown; restored from __doc__
        """ setResponseForRequest(self, id: QNearFieldTarget.RequestId, response: Any, emitRequestCompleted: bool = True) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> QNearFieldTarget.Type """
        pass

    def uid(self): # real signature unknown; restored from __doc__
        """ uid(self) -> QByteArray """
        pass

    def url(self): # real signature unknown; restored from __doc__
        """ url(self) -> QUrl """
        pass

    def waitForRequestCompleted(self, id, msecs=5000): # real signature unknown; restored from __doc__
        """ waitForRequestCompleted(self, id: QNearFieldTarget.RequestId, msecs: int = 5000) -> bool """
        return False

    def writeNdefMessages(self, messages, QNdefMessage=None): # real signature unknown; restored from __doc__
        """ writeNdefMessages(self, messages: Iterable[QNdefMessage]) -> QNearFieldTarget.RequestId """
        pass

    def __init__(self, parent, QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    ChecksumMismatchError = 5
    CommandError = 9
    InvalidParametersError = 6
    LlcpAccess = 4
    MifareTag = 5
    NdefAccess = 1
    NdefReadError = 7
    NdefWriteError = 8
    NfcTagType1 = 1
    NfcTagType2 = 2
    NfcTagType3 = 3
    NfcTagType4 = 4
    NoError = 0
    NoResponseError = 4
    ProprietaryTag = 0
    TagTypeSpecificAccess = 2
    TargetOutOfRangeError = 3
    UnknownAccess = 0
    UnknownError = 1
    UnsupportedError = 2


class QQmlNdefRecord(__PyQt5_QtCore.QObject):
    """
    QQmlNdefRecord(parent: Optional[QObject] = None)
    QQmlNdefRecord(record: QNdefRecord, parent: Optional[QObject] = None)
    """
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

    def record(self): # real signature unknown; restored from __doc__
        """ record(self) -> QNdefRecord """
        return QNdefRecord

    def recordChanged(self, *args, **kwargs): # real signature unknown
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

    def setRecord(self, record): # real signature unknown; restored from __doc__
        """ setRecord(self, record: QNdefRecord) """
        pass

    def setType(self, t, p_str=None): # real signature unknown; restored from __doc__
        """ setType(self, t: Optional[str]) """
        pass

    def setTypeNameFormat(self, typeNameFormat): # real signature unknown; restored from __doc__
        """ setTypeNameFormat(self, typeNameFormat: QQmlNdefRecord.TypeNameFormat) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> str """
        return ""

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

    def typeNameFormat(self): # real signature unknown; restored from __doc__
        """ typeNameFormat(self) -> QQmlNdefRecord.TypeNameFormat """
        pass

    def typeNameFormatChanged(self, *args, **kwargs): # real signature unknown
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

    Empty = 0
    ExternalRtd = 4
    Mime = 2
    NfcRtd = 1
    Unknown = 5
    Uri = 3


# variables with complex values



