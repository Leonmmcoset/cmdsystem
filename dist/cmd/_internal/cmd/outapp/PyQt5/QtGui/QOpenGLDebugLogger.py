# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QOpenGLDebugLogger(__PyQt5_QtCore.QObject):
    """ QOpenGLDebugLogger(parent: Optional[QObject] = None) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disableMessages(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        disableMessages(self, sources: Union[QOpenGLDebugMessage.Sources, QOpenGLDebugMessage.Source] = QOpenGLDebugMessage.AnySource, types: Union[QOpenGLDebugMessage.Types, QOpenGLDebugMessage.Type] = QOpenGLDebugMessage.AnyType, severities: Union[QOpenGLDebugMessage.Severities, QOpenGLDebugMessage.Severity] = QOpenGLDebugMessage.Severity.AnySeverity)
        disableMessages(self, ids: Iterable[int], sources: Union[QOpenGLDebugMessage.Sources, QOpenGLDebugMessage.Source] = QOpenGLDebugMessage.AnySource, types: Union[QOpenGLDebugMessage.Types, QOpenGLDebugMessage.Type] = QOpenGLDebugMessage.AnyType)
        """
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def enableMessages(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        enableMessages(self, sources: Union[QOpenGLDebugMessage.Sources, QOpenGLDebugMessage.Source] = QOpenGLDebugMessage.AnySource, types: Union[QOpenGLDebugMessage.Types, QOpenGLDebugMessage.Type] = QOpenGLDebugMessage.AnyType, severities: Union[QOpenGLDebugMessage.Severities, QOpenGLDebugMessage.Severity] = QOpenGLDebugMessage.Severity.AnySeverity)
        enableMessages(self, ids: Iterable[int], sources: Union[QOpenGLDebugMessage.Sources, QOpenGLDebugMessage.Source] = QOpenGLDebugMessage.AnySource, types: Union[QOpenGLDebugMessage.Types, QOpenGLDebugMessage.Type] = QOpenGLDebugMessage.AnyType)
        """
        pass

    def initialize(self): # real signature unknown; restored from __doc__
        """ initialize(self) -> bool """
        return False

    def isLogging(self): # real signature unknown; restored from __doc__
        """ isLogging(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def loggedMessages(self): # real signature unknown; restored from __doc__
        """ loggedMessages(self) -> List[QOpenGLDebugMessage] """
        return []

    def loggingMode(self): # real signature unknown; restored from __doc__
        """ loggingMode(self) -> QOpenGLDebugLogger.LoggingMode """
        pass

    def logMessage(self, debugMessage): # real signature unknown; restored from __doc__
        """ logMessage(self, debugMessage: QOpenGLDebugMessage) """
        pass

    def maximumMessageLength(self): # real signature unknown; restored from __doc__
        """ maximumMessageLength(self) -> int """
        return 0

    def messageLogged(self, *args, **kwargs): # real signature unknown
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

    def popGroup(self): # real signature unknown; restored from __doc__
        """ popGroup(self) """
        pass

    def pushGroup(self, name, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ pushGroup(self, name: Optional[str], id: int = 0, source: QOpenGLDebugMessage.Source = QOpenGLDebugMessage.ApplicationSource) """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def startLogging(self, loggingMode=None): # real signature unknown; restored from __doc__
        """ startLogging(self, loggingMode: QOpenGLDebugLogger.LoggingMode = QOpenGLDebugLogger.AsynchronousLogging) """
        pass

    def stopLogging(self): # real signature unknown; restored from __doc__
        """ stopLogging(self) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent, QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    AsynchronousLogging = 0
    SynchronousLogging = 1


