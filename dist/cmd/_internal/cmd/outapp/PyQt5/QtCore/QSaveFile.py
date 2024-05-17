# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


from .QFileDevice import QFileDevice

class QSaveFile(QFileDevice):
    """
    QSaveFile(name: Optional[str])
    QSaveFile(parent: Optional[QObject] = None)
    QSaveFile(name: Optional[str], parent: Optional[QObject])
    """
    def cancelWriting(self): # real signature unknown; restored from __doc__
        """ cancelWriting(self) """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def close(self, *args, **kwargs): # real signature unknown
        pass

    def commit(self): # real signature unknown; restored from __doc__
        """ commit(self) -> bool """
        return False

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def directWriteFallback(self): # real signature unknown; restored from __doc__
        """ directWriteFallback(self) -> bool """
        return False

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def fileName(self): # real signature unknown; restored from __doc__
        """ fileName(self) -> str """
        return ""

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def open(self, flags, QIODevice_OpenMode=None, QIODevice_OpenModeFlag=None): # real signature unknown; restored from __doc__
        """ open(self, flags: Union[QIODevice.OpenMode, QIODevice.OpenModeFlag]) -> bool """
        return False

    def readData(self, *args, **kwargs): # real signature unknown
        pass

    def readLineData(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setDirectWriteFallback(self, enabled): # real signature unknown; restored from __doc__
        """ setDirectWriteFallback(self, enabled: bool) """
        pass

    def setErrorString(self, *args, **kwargs): # real signature unknown
        pass

    def setFileName(self, name, p_str=None): # real signature unknown; restored from __doc__
        """ setFileName(self, name: Optional[str]) """
        pass

    def setOpenMode(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def writeData(self, data, PyQt5_sip_array=None, bytes=None): # real signature unknown; restored from __doc__
        """ writeData(self, data: Optional[PyQt5.sip.array[bytes]]) -> int """
        return 0

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


