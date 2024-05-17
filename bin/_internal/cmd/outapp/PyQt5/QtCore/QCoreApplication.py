# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


from .QObject import QObject

class QCoreApplication(QObject):
    """ QCoreApplication(argv: List[str]) """
    def aboutToQuit(self, *args, **kwargs): # real signature unknown
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

    def addLibraryPath(self, a0, p_str=None): # real signature unknown; restored from __doc__
        """ addLibraryPath(a0: Optional[str]) """
        pass

    def applicationDirPath(self): # real signature unknown; restored from __doc__
        """ applicationDirPath() -> str """
        return ""

    def applicationFilePath(self): # real signature unknown; restored from __doc__
        """ applicationFilePath() -> str """
        return ""

    def applicationName(self): # real signature unknown; restored from __doc__
        """ applicationName() -> str """
        return ""

    def applicationPid(self): # real signature unknown; restored from __doc__
        """ applicationPid() -> int """
        return 0

    def applicationVersion(self): # real signature unknown; restored from __doc__
        """ applicationVersion() -> str """
        return ""

    def arguments(self): # real signature unknown; restored from __doc__
        """ arguments() -> List[str] """
        return []

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def closingDown(self): # real signature unknown; restored from __doc__
        """ closingDown() -> bool """
        return False

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, a0, QEvent=None): # real signature unknown; restored from __doc__
        """ event(self, a0: Optional[QEvent]) -> bool """
        return False

    def eventDispatcher(self): # real signature unknown; restored from __doc__
        """ eventDispatcher() -> Optional[QAbstractEventDispatcher] """
        pass

    def exec(self): # real signature unknown; restored from __doc__
        """ exec() -> int """
        return 0

    def exec_(self): # real signature unknown; restored from __doc__
        """ exec_() -> int """
        return 0

    def exit(self, returnCode=0): # real signature unknown; restored from __doc__
        """ exit(returnCode: int = 0) """
        pass

    def flush(self): # real signature unknown; restored from __doc__
        """ flush() """
        pass

    def hasPendingEvents(self): # real signature unknown; restored from __doc__
        """ hasPendingEvents() -> bool """
        return False

    def installNativeEventFilter(self, filterObj, QAbstractNativeEventFilter=None): # real signature unknown; restored from __doc__
        """ installNativeEventFilter(self, filterObj: Optional[QAbstractNativeEventFilter]) """
        pass

    def installTranslator(self, messageFile, QTranslator=None): # real signature unknown; restored from __doc__
        """ installTranslator(messageFile: Optional[QTranslator]) -> bool """
        return False

    def instance(self): # real signature unknown; restored from __doc__
        """ instance() -> Optional[QCoreApplication] """
        pass

    def isQuitLockEnabled(self): # real signature unknown; restored from __doc__
        """ isQuitLockEnabled() -> bool """
        return False

    def isSetuidAllowed(self): # real signature unknown; restored from __doc__
        """ isSetuidAllowed() -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def libraryPaths(self): # real signature unknown; restored from __doc__
        """ libraryPaths() -> List[str] """
        return []

    def notify(self, a0, QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ notify(self, a0: Optional[QObject], a1: Optional[QEvent]) -> bool """
        pass

    def organizationDomain(self): # real signature unknown; restored from __doc__
        """ organizationDomain() -> str """
        return ""

    def organizationName(self): # real signature unknown; restored from __doc__
        """ organizationName() -> str """
        return ""

    def postEvent(self, receiver, QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ postEvent(receiver: Optional[QObject], event: Optional[QEvent], priority: int = Qt.EventPriority.NormalEventPriority) """
        pass

    def processEvents(self, flags, QEventLoop_ProcessEventsFlags=None, QEventLoop_ProcessEventsFlag=None, *args, **kwargs): # real signature unknown; restored from __doc__ with multiple overloads
        """
        processEvents(flags: Union[QEventLoop.ProcessEventsFlags, QEventLoop.ProcessEventsFlag] = QEventLoop.ProcessEventsFlag.AllEvents)
        processEvents(flags: Union[QEventLoop.ProcessEventsFlags, QEventLoop.ProcessEventsFlag], maxtime: int)
        """
        pass

    def quit(self): # real signature unknown; restored from __doc__
        """ quit() """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def removeLibraryPath(self, a0, p_str=None): # real signature unknown; restored from __doc__
        """ removeLibraryPath(a0: Optional[str]) """
        pass

    def removeNativeEventFilter(self, filterObj, QAbstractNativeEventFilter=None): # real signature unknown; restored from __doc__
        """ removeNativeEventFilter(self, filterObj: Optional[QAbstractNativeEventFilter]) """
        pass

    def removePostedEvents(self, receiver, QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ removePostedEvents(receiver: Optional[QObject], eventType: int = 0) """
        pass

    def removeTranslator(self, messageFile, QTranslator=None): # real signature unknown; restored from __doc__
        """ removeTranslator(messageFile: Optional[QTranslator]) -> bool """
        return False

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def sendEvent(self, receiver, QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ sendEvent(receiver: Optional[QObject], event: Optional[QEvent]) -> bool """
        pass

    def sendPostedEvents(self, receiver, QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ sendPostedEvents(receiver: Optional[QObject] = None, eventType: int = 0) """
        pass

    def setApplicationName(self, application, p_str=None): # real signature unknown; restored from __doc__
        """ setApplicationName(application: Optional[str]) """
        pass

    def setApplicationVersion(self, version, p_str=None): # real signature unknown; restored from __doc__
        """ setApplicationVersion(version: Optional[str]) """
        pass

    def setAttribute(self, attribute, on=True): # real signature unknown; restored from __doc__
        """ setAttribute(attribute: Qt.ApplicationAttribute, on: bool = True) """
        pass

    def setEventDispatcher(self, eventDispatcher, QAbstractEventDispatcher=None): # real signature unknown; restored from __doc__
        """ setEventDispatcher(eventDispatcher: Optional[QAbstractEventDispatcher]) """
        pass

    def setLibraryPaths(self, a0, Optional=None, p_str=None): # real signature unknown; restored from __doc__
        """ setLibraryPaths(a0: Iterable[Optional[str]]) """
        pass

    def setOrganizationDomain(self, orgDomain, p_str=None): # real signature unknown; restored from __doc__
        """ setOrganizationDomain(orgDomain: Optional[str]) """
        pass

    def setOrganizationName(self, orgName, p_str=None): # real signature unknown; restored from __doc__
        """ setOrganizationName(orgName: Optional[str]) """
        pass

    def setQuitLockEnabled(self, enabled): # real signature unknown; restored from __doc__
        """ setQuitLockEnabled(enabled: bool) """
        pass

    def setSetuidAllowed(self, allow): # real signature unknown; restored from __doc__
        """ setSetuidAllowed(allow: bool) """
        pass

    def startingUp(self): # real signature unknown; restored from __doc__
        """ startingUp() -> bool """
        return False

    def testAttribute(self, attribute): # real signature unknown; restored from __doc__
        """ testAttribute(attribute: Qt.ApplicationAttribute) -> bool """
        return False

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def translate(self, context, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ translate(context: Optional[str], sourceText: Optional[str], disambiguation: Optional[str] = None, n: int = -1) -> str """
        pass

    def __enter__(self): # real signature unknown; restored from __doc__
        """ __enter__(self) -> Any """
        pass

    def __exit__(self, type, value, traceback): # real signature unknown; restored from __doc__
        """ __exit__(self, type: Any, value: Any, traceback: Any) """
        pass

    def __init__(self, argv, p_str=None): # real signature unknown; restored from __doc__
        pass


