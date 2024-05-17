# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


from .QIODevice import QIODevice

class QProcess(QIODevice):
    """ QProcess(parent: Optional[QObject] = None) """
    def arguments(self): # real signature unknown; restored from __doc__
        """ arguments(self) -> List[str] """
        return []

    def atEnd(self): # real signature unknown; restored from __doc__
        """ atEnd(self) -> bool """
        return False

    def bytesAvailable(self): # real signature unknown; restored from __doc__
        """ bytesAvailable(self) -> int """
        return 0

    def bytesToWrite(self): # real signature unknown; restored from __doc__
        """ bytesToWrite(self) -> int """
        return 0

    def canReadLine(self): # real signature unknown; restored from __doc__
        """ canReadLine(self) -> bool """
        return False

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def close(self): # real signature unknown; restored from __doc__
        """ close(self) """
        pass

    def closeReadChannel(self, channel): # real signature unknown; restored from __doc__
        """ closeReadChannel(self, channel: QProcess.ProcessChannel) """
        pass

    def closeWriteChannel(self): # real signature unknown; restored from __doc__
        """ closeWriteChannel(self) """
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

    def errorOccurred(self, *args, **kwargs): # real signature unknown
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

    def execute(self, program, p_str=None, *args=None, **kwargs=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        execute(program: Optional[str], arguments: Iterable[Optional[str]]) -> int
        execute(program: Optional[str]) -> int
        """
        return 0

    def exitCode(self): # real signature unknown; restored from __doc__
        """ exitCode(self) -> int """
        return 0

    def exitStatus(self): # real signature unknown; restored from __doc__
        """ exitStatus(self) -> QProcess.ExitStatus """
        pass

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

    def inputChannelMode(self): # real signature unknown; restored from __doc__
        """ inputChannelMode(self) -> QProcess.InputChannelMode """
        pass

    def isSequential(self): # real signature unknown; restored from __doc__
        """ isSequential(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def kill(self): # real signature unknown; restored from __doc__
        """ kill(self) """
        pass

    def nullDevice(self): # real signature unknown; restored from __doc__
        """ nullDevice() -> str """
        return ""

    def open(self, mode, QIODevice_OpenMode=None, QIODevice_OpenModeFlag=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ open(self, mode: Union[QIODevice.OpenMode, QIODevice.OpenModeFlag] = QIODevice.ReadWrite) -> bool """
        pass

    def pid(self): # real signature unknown; restored from __doc__
        """ pid(self) -> Optional[PyQt5.sip.voidptr] """
        pass

    def processChannelMode(self): # real signature unknown; restored from __doc__
        """ processChannelMode(self) -> QProcess.ProcessChannelMode """
        pass

    def processEnvironment(self): # real signature unknown; restored from __doc__
        """ processEnvironment(self) -> QProcessEnvironment """
        return QProcessEnvironment

    def processId(self): # real signature unknown; restored from __doc__
        """ processId(self) -> int """
        return 0

    def program(self): # real signature unknown; restored from __doc__
        """ program(self) -> str """
        return ""

    def readAllStandardError(self): # real signature unknown; restored from __doc__
        """ readAllStandardError(self) -> QByteArray """
        return QByteArray

    def readAllStandardOutput(self): # real signature unknown; restored from __doc__
        """ readAllStandardOutput(self) -> QByteArray """
        return QByteArray

    def readChannel(self): # real signature unknown; restored from __doc__
        """ readChannel(self) -> QProcess.ProcessChannel """
        pass

    def readData(self, maxlen): # real signature unknown; restored from __doc__
        """ readData(self, maxlen: int) -> bytes """
        return b""

    def readLineData(self, *args, **kwargs): # real signature unknown
        pass

    def readyReadStandardError(self, *args, **kwargs): # real signature unknown
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

    def readyReadStandardOutput(self, *args, **kwargs): # real signature unknown
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

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setArguments(self, arguments, Optional=None, p_str=None): # real signature unknown; restored from __doc__
        """ setArguments(self, arguments: Iterable[Optional[str]]) """
        pass

    def setErrorString(self, *args, **kwargs): # real signature unknown
        pass

    def setInputChannelMode(self, mode): # real signature unknown; restored from __doc__
        """ setInputChannelMode(self, mode: QProcess.InputChannelMode) """
        pass

    def setOpenMode(self, *args, **kwargs): # real signature unknown
        pass

    def setProcessChannelMode(self, mode): # real signature unknown; restored from __doc__
        """ setProcessChannelMode(self, mode: QProcess.ProcessChannelMode) """
        pass

    def setProcessEnvironment(self, environment): # real signature unknown; restored from __doc__
        """ setProcessEnvironment(self, environment: QProcessEnvironment) """
        pass

    def setProcessState(self, state): # real signature unknown; restored from __doc__
        """ setProcessState(self, state: QProcess.ProcessState) """
        pass

    def setProgram(self, program, p_str=None): # real signature unknown; restored from __doc__
        """ setProgram(self, program: Optional[str]) """
        pass

    def setReadChannel(self, channel): # real signature unknown; restored from __doc__
        """ setReadChannel(self, channel: QProcess.ProcessChannel) """
        pass

    def setStandardErrorFile(self, fileName, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setStandardErrorFile(self, fileName: Optional[str], mode: Union[QIODevice.OpenMode, QIODevice.OpenModeFlag] = QIODevice.Truncate) """
        pass

    def setStandardInputFile(self, fileName, p_str=None): # real signature unknown; restored from __doc__
        """ setStandardInputFile(self, fileName: Optional[str]) """
        pass

    def setStandardOutputFile(self, fileName, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setStandardOutputFile(self, fileName: Optional[str], mode: Union[QIODevice.OpenMode, QIODevice.OpenModeFlag] = QIODevice.Truncate) """
        pass

    def setStandardOutputProcess(self, destination, QProcess=None): # real signature unknown; restored from __doc__
        """ setStandardOutputProcess(self, destination: Optional[QProcess]) """
        pass

    def setupChildProcess(self): # real signature unknown; restored from __doc__
        """ setupChildProcess(self) """
        pass

    def setWorkingDirectory(self, dir, p_str=None): # real signature unknown; restored from __doc__
        """ setWorkingDirectory(self, dir: Optional[str]) """
        pass

    def start(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        start(self, program: Optional[str], arguments: Iterable[Optional[str]], mode: Union[QIODevice.OpenMode, QIODevice.OpenModeFlag] = QIODevice.ReadWrite)
        start(self, command: Optional[str], mode: Union[QIODevice.OpenMode, QIODevice.OpenModeFlag] = QIODevice.ReadWrite)
        start(self, mode: Union[QIODevice.OpenMode, QIODevice.OpenModeFlag] = QIODevice.ReadWrite)
        """
        pass

    def startDetached(self, program=None, p_str=None, *args=None, **kwargs=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        startDetached(program: Optional[str], arguments: Iterable[Optional[str]], workingDirectory: Optional[str]) -> (bool, Optional[int])
        startDetached(program: Optional[str], arguments: Iterable[Optional[str]]) -> bool
        startDetached(program: Optional[str]) -> bool
        startDetached(self) -> (bool, Optional[int])
        """
        return False

    def started(self, *args, **kwargs): # real signature unknown
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

    def state(self): # real signature unknown; restored from __doc__
        """ state(self) -> QProcess.ProcessState """
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

    def systemEnvironment(self): # real signature unknown; restored from __doc__
        """ systemEnvironment() -> List[str] """
        return []

    def terminate(self): # real signature unknown; restored from __doc__
        """ terminate(self) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def waitForBytesWritten(self, msecs=30000): # real signature unknown; restored from __doc__
        """ waitForBytesWritten(self, msecs: int = 30000) -> bool """
        return False

    def waitForFinished(self, msecs=30000): # real signature unknown; restored from __doc__
        """ waitForFinished(self, msecs: int = 30000) -> bool """
        return False

    def waitForReadyRead(self, msecs=30000): # real signature unknown; restored from __doc__
        """ waitForReadyRead(self, msecs: int = 30000) -> bool """
        return False

    def waitForStarted(self, msecs=30000): # real signature unknown; restored from __doc__
        """ waitForStarted(self, msecs: int = 30000) -> bool """
        return False

    def workingDirectory(self): # real signature unknown; restored from __doc__
        """ workingDirectory(self) -> str """
        return ""

    def writeData(self, data, PyQt5_sip_array=None, bytes=None): # real signature unknown; restored from __doc__
        """ writeData(self, data: Optional[PyQt5.sip.array[bytes]]) -> int """
        return 0

    def __init__(self, parent, QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    Crashed = 1
    CrashExit = 1
    FailedToStart = 0
    ForwardedChannels = 2
    ForwardedErrorChannel = 4
    ForwardedInputChannel = 1
    ForwardedOutputChannel = 3
    ManagedInputChannel = 0
    MergedChannels = 1
    NormalExit = 0
    NotRunning = 0
    ReadError = 3
    Running = 2
    SeparateChannels = 0
    StandardError = 1
    StandardOutput = 0
    Starting = 1
    Timedout = 2
    UnknownError = 5
    WriteError = 4


