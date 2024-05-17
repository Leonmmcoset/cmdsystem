# encoding: utf-8
# module PyQt5.QtMultimedia
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtMultimedia.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QMediaObject(__PyQt5_QtCore.QObject):
    """ QMediaObject(parent: Optional[QObject], service: Optional[QMediaService]) """
    def addPropertyWatch(self, name, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ addPropertyWatch(self, name: Union[QByteArray, bytes, bytearray]) """
        pass

    def availability(self): # real signature unknown; restored from __doc__
        """ availability(self) -> QMultimedia.AvailabilityStatus """
        pass

    def availabilityChanged(self, *args, **kwargs): # real signature unknown
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

    def availableMetaData(self): # real signature unknown; restored from __doc__
        """ availableMetaData(self) -> List[str] """
        return []

    def bind(self, a0, QObject=None): # real signature unknown; restored from __doc__
        """ bind(self, a0: Optional[QObject]) -> bool """
        return False

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

    def isMetaDataAvailable(self): # real signature unknown; restored from __doc__
        """ isMetaDataAvailable(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def metaData(self, key, p_str=None): # real signature unknown; restored from __doc__
        """ metaData(self, key: Optional[str]) -> Any """
        pass

    def metaDataAvailableChanged(self, *args, **kwargs): # real signature unknown
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

    def metaDataChanged(self, *args, **kwargs): # real signature unknown
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

    def notifyInterval(self): # real signature unknown; restored from __doc__
        """ notifyInterval(self) -> int """
        return 0

    def notifyIntervalChanged(self, *args, **kwargs): # real signature unknown
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

    def removePropertyWatch(self, name, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ removePropertyWatch(self, name: Union[QByteArray, bytes, bytearray]) """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def service(self): # real signature unknown; restored from __doc__
        """ service(self) -> Optional[QMediaService] """
        pass

    def setNotifyInterval(self, milliSeconds): # real signature unknown; restored from __doc__
        """ setNotifyInterval(self, milliSeconds: int) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def unbind(self, a0, QObject=None): # real signature unknown; restored from __doc__
        """ unbind(self, a0: Optional[QObject]) """
        pass

    def __init__(self, parent, QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass


