# encoding: utf-8
# module PyQt5.QtLocation
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtLocation.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QGeoCodeReply(__PyQt5_QtCore.QObject):
    """
    QGeoCodeReply(error: QGeoCodeReply.Error, errorString: Optional[str], parent: Optional[QObject] = None)
    QGeoCodeReply(parent: Optional[QObject] = None)
    """
    def abort(self): # real signature unknown; restored from __doc__
        """ abort(self) """
        pass

    def aborted(self, *args, **kwargs): # real signature unknown
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

    def addLocation(self, location): # real signature unknown; restored from __doc__
        """ addLocation(self, location: QGeoLocation) """
        pass

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

    def isFinished(self): # real signature unknown; restored from __doc__
        """ isFinished(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def limit(self): # real signature unknown; restored from __doc__
        """ limit(self) -> int """
        return 0

    def locations(self): # real signature unknown; restored from __doc__
        """ locations(self) -> List[QGeoLocation] """
        return []

    def offset(self): # real signature unknown; restored from __doc__
        """ offset(self) -> int """
        return 0

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setError(self, error, errorString, p_str=None): # real signature unknown; restored from __doc__
        """ setError(self, error: QGeoCodeReply.Error, errorString: Optional[str]) """
        pass

    def setFinished(self, finished): # real signature unknown; restored from __doc__
        """ setFinished(self, finished: bool) """
        pass

    def setLimit(self, limit): # real signature unknown; restored from __doc__
        """ setLimit(self, limit: int) """
        pass

    def setLocations(self, locations, QGeoLocation=None): # real signature unknown; restored from __doc__
        """ setLocations(self, locations: Iterable[QGeoLocation]) """
        pass

    def setOffset(self, offset): # real signature unknown; restored from __doc__
        """ setOffset(self, offset: int) """
        pass

    def setViewport(self, viewport): # real signature unknown; restored from __doc__
        """ setViewport(self, viewport: QGeoShape) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def viewport(self): # real signature unknown; restored from __doc__
        """ viewport(self) -> QGeoShape """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    CombinationError = 5
    CommunicationError = 2
    EngineNotSetError = 1
    NoError = 0
    ParseError = 3
    UnknownError = 6
    UnsupportedOptionError = 4


