# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


from .QObject import QObject

class QIODevice(QObject):
    """
    QIODevice()
    QIODevice(parent: Optional[QObject])
    """
    def aboutToClose(self, *args, **kwargs): # real signature unknown
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

    def atEnd(self): # real signature unknown; restored from __doc__
        """ atEnd(self) -> bool """
        return False

    def bytesAvailable(self): # real signature unknown; restored from __doc__
        """ bytesAvailable(self) -> int """
        return 0

    def bytesToWrite(self): # real signature unknown; restored from __doc__
        """ bytesToWrite(self) -> int """
        return 0

    def bytesWritten(self, *args, **kwargs): # real signature unknown
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

    def canReadLine(self): # real signature unknown; restored from __doc__
        """ canReadLine(self) -> bool """
        return False

    def channelBytesWritten(self, *args, **kwargs): # real signature unknown
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

    def channelReadyRead(self, *args, **kwargs): # real signature unknown
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

    def close(self): # real signature unknown; restored from __doc__
        """ close(self) """
        pass

    def commitTransaction(self): # real signature unknown; restored from __doc__
        """ commitTransaction(self) """
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def currentReadChannel(self): # real signature unknown; restored from __doc__
        """ currentReadChannel(self) -> int """
        return 0

    def currentWriteChannel(self): # real signature unknown; restored from __doc__
        """ currentWriteChannel(self) -> int """
        return 0

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def errorString(self): # real signature unknown; restored from __doc__
        """ errorString(self) -> str """
        return ""

    def getChar(self): # real signature unknown; restored from __doc__
        """ getChar(self) -> (bool, Optional[bytes]) """
        pass

    def isOpen(self): # real signature unknown; restored from __doc__
        """ isOpen(self) -> bool """
        return False

    def isReadable(self): # real signature unknown; restored from __doc__
        """ isReadable(self) -> bool """
        return False

    def isSequential(self): # real signature unknown; restored from __doc__
        """ isSequential(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def isTextModeEnabled(self): # real signature unknown; restored from __doc__
        """ isTextModeEnabled(self) -> bool """
        return False

    def isTransactionStarted(self): # real signature unknown; restored from __doc__
        """ isTransactionStarted(self) -> bool """
        return False

    def isWritable(self): # real signature unknown; restored from __doc__
        """ isWritable(self) -> bool """
        return False

    def open(self, mode, QIODevice_OpenMode=None, QIODevice_OpenModeFlag=None): # real signature unknown; restored from __doc__
        """ open(self, mode: Union[QIODevice.OpenMode, QIODevice.OpenModeFlag]) -> bool """
        return False

    def openMode(self): # real signature unknown; restored from __doc__
        """ openMode(self) -> QIODevice.OpenMode """
        pass

    def peek(self, maxlen): # real signature unknown; restored from __doc__
        """ peek(self, maxlen: int) -> QByteArray """
        return QByteArray

    def pos(self): # real signature unknown; restored from __doc__
        """ pos(self) -> int """
        return 0

    def putChar(self, c): # real signature unknown; restored from __doc__
        """ putChar(self, c: str) -> bool """
        return False

    def read(self, maxlen): # real signature unknown; restored from __doc__
        """ read(self, maxlen: int) -> bytes """
        return b""

    def readAll(self): # real signature unknown; restored from __doc__
        """ readAll(self) -> QByteArray """
        return QByteArray

    def readChannelCount(self): # real signature unknown; restored from __doc__
        """ readChannelCount(self) -> int """
        return 0

    def readChannelFinished(self, *args, **kwargs): # real signature unknown
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

    def readData(self, maxlen): # real signature unknown; restored from __doc__
        """ readData(self, maxlen: int) -> bytes """
        return b""

    def readLine(self, maxlen=0): # real signature unknown; restored from __doc__
        """ readLine(self, maxlen: int = 0) -> bytes """
        return b""

    def readLineData(self, maxlen): # real signature unknown; restored from __doc__
        """ readLineData(self, maxlen: int) -> bytes """
        return b""

    def readyRead(self, *args, **kwargs): # real signature unknown
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

    def reset(self): # real signature unknown; restored from __doc__
        """ reset(self) -> bool """
        return False

    def rollbackTransaction(self): # real signature unknown; restored from __doc__
        """ rollbackTransaction(self) """
        pass

    def seek(self, pos): # real signature unknown; restored from __doc__
        """ seek(self, pos: int) -> bool """
        return False

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setCurrentReadChannel(self, channel): # real signature unknown; restored from __doc__
        """ setCurrentReadChannel(self, channel: int) """
        pass

    def setCurrentWriteChannel(self, channel): # real signature unknown; restored from __doc__
        """ setCurrentWriteChannel(self, channel: int) """
        pass

    def setErrorString(self, errorString, p_str=None): # real signature unknown; restored from __doc__
        """ setErrorString(self, errorString: Optional[str]) """
        pass

    def setOpenMode(self, openMode, QIODevice_OpenMode=None, QIODevice_OpenModeFlag=None): # real signature unknown; restored from __doc__
        """ setOpenMode(self, openMode: Union[QIODevice.OpenMode, QIODevice.OpenModeFlag]) """
        pass

    def setTextModeEnabled(self, enabled): # real signature unknown; restored from __doc__
        """ setTextModeEnabled(self, enabled: bool) """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ size(self) -> int """
        return 0

    def skip(self, maxSize): # real signature unknown; restored from __doc__
        """ skip(self, maxSize: int) -> int """
        return 0

    def startTransaction(self): # real signature unknown; restored from __doc__
        """ startTransaction(self) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def ungetChar(self, c): # real signature unknown; restored from __doc__
        """ ungetChar(self, c: str) """
        pass

    def waitForBytesWritten(self, msecs): # real signature unknown; restored from __doc__
        """ waitForBytesWritten(self, msecs: int) -> bool """
        return False

    def waitForReadyRead(self, msecs): # real signature unknown; restored from __doc__
        """ waitForReadyRead(self, msecs: int) -> bool """
        return False

    def write(self, data, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ write(self, data: Union[QByteArray, bytes, bytearray]) -> int """
        return 0

    def writeChannelCount(self): # real signature unknown; restored from __doc__
        """ writeChannelCount(self) -> int """
        return 0

    def writeData(self, data, PyQt5_sip_array=None, bytes=None): # real signature unknown; restored from __doc__
        """ writeData(self, data: Optional[PyQt5.sip.array[bytes]]) -> int """
        return 0

    def __init__(self, parent=None, QObject=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    Append = 4
    ExistingOnly = 128
    NewOnly = 64
    NotOpen = 0
    ReadOnly = 1
    ReadWrite = 3
    Text = 16
    Truncate = 8
    Unbuffered = 32
    WriteOnly = 2


