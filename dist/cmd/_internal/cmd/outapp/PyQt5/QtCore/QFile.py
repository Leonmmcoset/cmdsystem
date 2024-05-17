# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


from .QFileDevice import QFileDevice

class QFile(QFileDevice):
    """
    QFile()
    QFile(name: Optional[str])
    QFile(parent: Optional[QObject])
    QFile(name: Optional[str], parent: Optional[QObject])
    """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def copy(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        copy(self, newName: Optional[str]) -> bool
        copy(fileName: Optional[str], newName: Optional[str]) -> bool
        """
        return False

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def decodeName(self, localFileName, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        decodeName(localFileName: Union[QByteArray, bytes, bytearray]) -> str
        decodeName(localFileName: Optional[str]) -> str
        """
        return ""

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def encodeName(self, fileName, p_str=None): # real signature unknown; restored from __doc__
        """ encodeName(fileName: Optional[str]) -> QByteArray """
        return QByteArray

    def exists(self, fileName=None, p_str=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        exists(self) -> bool
        exists(fileName: Optional[str]) -> bool
        """
        return False

    def fileName(self): # real signature unknown; restored from __doc__
        """ fileName(self) -> str """
        return ""

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def link(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        link(self, newName: Optional[str]) -> bool
        link(oldname: Optional[str], newName: Optional[str]) -> bool
        """
        return False

    def moveToTrash(self, fileName=None, p_str=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        moveToTrash(self) -> bool
        moveToTrash(fileName: Optional[str]) -> (bool, Optional[str])
        """
        return False

    def open(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        open(self, flags: Union[QIODevice.OpenMode, QIODevice.OpenModeFlag]) -> bool
        open(self, fd: int, ioFlags: Union[QIODevice.OpenMode, QIODevice.OpenModeFlag], handleFlags: Union[QFileDevice.FileHandleFlags, QFileDevice.FileHandleFlag] = QFileDevice.FileHandleFlag.DontCloseHandle) -> bool
        """
        return False

    def permissions(self, filename=None, p_str=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        permissions(self) -> QFileDevice.Permissions
        permissions(filename: Optional[str]) -> QFileDevice.Permissions
        """
        pass

    def readData(self, *args, **kwargs): # real signature unknown
        pass

    def readLineData(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def remove(self, fileName=None, p_str=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        remove(self) -> bool
        remove(fileName: Optional[str]) -> bool
        """
        return False

    def rename(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        rename(self, newName: Optional[str]) -> bool
        rename(oldName: Optional[str], newName: Optional[str]) -> bool
        """
        return False

    def resize(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        resize(self, sz: int) -> bool
        resize(filename: Optional[str], sz: int) -> bool
        """
        return False

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setErrorString(self, *args, **kwargs): # real signature unknown
        pass

    def setFileName(self, name, p_str=None): # real signature unknown; restored from __doc__
        """ setFileName(self, name: Optional[str]) """
        pass

    def setOpenMode(self, *args, **kwargs): # real signature unknown
        pass

    def setPermissions(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setPermissions(self, permissionSpec: Union[QFileDevice.Permissions, QFileDevice.Permission]) -> bool
        setPermissions(filename: Optional[str], permissionSpec: Union[QFileDevice.Permissions, QFileDevice.Permission]) -> bool
        """
        return False

    def size(self): # real signature unknown; restored from __doc__
        """ size(self) -> int """
        return 0

    def symLinkTarget(self, fileName=None, p_str=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        symLinkTarget(self) -> str
        symLinkTarget(fileName: Optional[str]) -> str
        """
        return ""

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def writeData(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


