# encoding: utf-8
# module PyQt5.QtMultimedia
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtMultimedia.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


from .QMediaControl import QMediaControl

class QCameraLocksControl(QMediaControl):
    """ QCameraLocksControl(parent: Optional[QObject] = None) """
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

    def lockStatus(self, lock): # real signature unknown; restored from __doc__
        """ lockStatus(self, lock: QCamera.LockType) -> QCamera.LockStatus """
        pass

    def lockStatusChanged(self, *args, **kwargs): # real signature unknown
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

    def searchAndLock(self, locks, QCamera_LockTypes=None, QCamera_LockType=None): # real signature unknown; restored from __doc__
        """ searchAndLock(self, locks: Union[QCamera.LockTypes, QCamera.LockType]) """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def supportedLocks(self): # real signature unknown; restored from __doc__
        """ supportedLocks(self) -> QCamera.LockTypes """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def unlock(self, locks, QCamera_LockTypes=None, QCamera_LockType=None): # real signature unknown; restored from __doc__
        """ unlock(self, locks: Union[QCamera.LockTypes, QCamera.LockType]) """
        pass

    def __init__(self, parent, QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass


