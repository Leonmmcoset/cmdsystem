# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


# Variables with simple values

PYQT_VERSION = 331530

PYQT_VERSION_STR = '5.15.10'

QtCriticalMsg = 2
QtDebugMsg = 0
QtFatalMsg = 3
QtInfoMsg = 4
QtSystemMsg = 2
QtWarningMsg = 1

QT_VERSION = 331522

QT_VERSION_STR = '5.15.2'

# functions

def bin_(s): # real signature unknown; restored from __doc__
    """ bin_(s: QTextStream) -> QTextStream """
    return QTextStream

def bom(s): # real signature unknown; restored from __doc__
    """ bom(s: QTextStream) -> QTextStream """
    return QTextStream

def center(s): # real signature unknown; restored from __doc__
    """ center(s: QTextStream) -> QTextStream """
    return QTextStream

def dec(s): # real signature unknown; restored from __doc__
    """ dec(s: QTextStream) -> QTextStream """
    return QTextStream

def endl(s): # real signature unknown; restored from __doc__
    """ endl(s: QTextStream) -> QTextStream """
    return QTextStream

def fixed(s): # real signature unknown; restored from __doc__
    """ fixed(s: QTextStream) -> QTextStream """
    return QTextStream

def flush(s): # real signature unknown; restored from __doc__
    """ flush(s: QTextStream) -> QTextStream """
    return QTextStream

def forcepoint(s): # real signature unknown; restored from __doc__
    """ forcepoint(s: QTextStream) -> QTextStream """
    return QTextStream

def forcesign(s): # real signature unknown; restored from __doc__
    """ forcesign(s: QTextStream) -> QTextStream """
    return QTextStream

def hex_(s): # real signature unknown; restored from __doc__
    """ hex_(s: QTextStream) -> QTextStream """
    return QTextStream

def left(s): # real signature unknown; restored from __doc__
    """ left(s: QTextStream) -> QTextStream """
    return QTextStream

def lowercasebase(s): # real signature unknown; restored from __doc__
    """ lowercasebase(s: QTextStream) -> QTextStream """
    return QTextStream

def lowercasedigits(s): # real signature unknown; restored from __doc__
    """ lowercasedigits(s: QTextStream) -> QTextStream """
    return QTextStream

def noforcepoint(s): # real signature unknown; restored from __doc__
    """ noforcepoint(s: QTextStream) -> QTextStream """
    return QTextStream

def noforcesign(s): # real signature unknown; restored from __doc__
    """ noforcesign(s: QTextStream) -> QTextStream """
    return QTextStream

def noshowbase(s): # real signature unknown; restored from __doc__
    """ noshowbase(s: QTextStream) -> QTextStream """
    return QTextStream

def oct_(s): # real signature unknown; restored from __doc__
    """ oct_(s: QTextStream) -> QTextStream """
    return QTextStream

def pyqtPickleProtocol(): # real signature unknown; restored from __doc__
    """ pyqtPickleProtocol() -> Optional[int] """
    pass

def pyqtRemoveInputHook(): # real signature unknown; restored from __doc__
    """ pyqtRemoveInputHook() """
    pass

def pyqtRestoreInputHook(): # real signature unknown; restored from __doc__
    """ pyqtRestoreInputHook() """
    pass

def pyqtSetPickleProtocol(a0, p_int=None): # real signature unknown; restored from __doc__
    """ pyqtSetPickleProtocol(a0: Optional[int]) """
    pass

def pyqtSlot(*types, name, p_str=None, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    @pyqtSlot(*types, name: Optional[str], result: Optional[str])
    
    This is a decorator applied to Python methods of a QObject that marks them
    as Qt slots.
    The non-keyword arguments are the types of the slot arguments and each may
    be a Python type object or a string specifying a C++ type.
    name is the name of the slot and defaults to the name of the method.
    result is type of the value returned by the slot.
    """
    pass

def qAbs(t): # real signature unknown; restored from __doc__
    """ qAbs(t: float) -> float """
    return 0.0

def qAddPostRoutine(a0, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """ qAddPostRoutine(a0: Callable[..., None]) """
    pass

def qAddPreRoutine(routine, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """ qAddPreRoutine(routine: Callable[[], None]) """
    pass

def qChecksum(s, PyQt5_sip_array=None, bytes=None): # real signature unknown; restored from __doc__
    """
    qChecksum(s: Optional[PyQt5.sip.array[bytes]]) -> int
    qChecksum(s: Optional[PyQt5.sip.array[bytes]], standard: Qt.ChecksumType) -> int
    """
    return 0

def qCompress(data, QByteArray=None, bytes=None, bytearray=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """ qCompress(data: Union[QByteArray, bytes, bytearray], compressionLevel: int = -1) -> QByteArray """
    pass

def qCritical(msg, p_str=None): # real signature unknown; restored from __doc__
    """ qCritical(msg: Optional[str]) """
    pass

def qDebug(msg, p_str=None): # real signature unknown; restored from __doc__
    """ qDebug(msg: Optional[str]) """
    pass

def qEnvironmentVariable(varName, p_str=None): # real signature unknown; restored from __doc__
    """
    qEnvironmentVariable(varName: Optional[str]) -> str
    qEnvironmentVariable(varName: Optional[str], defaultValue: Optional[str]) -> str
    """
    return ""

def qErrnoWarning(code, msg, p_str=None): # real signature unknown; restored from __doc__
    """
    qErrnoWarning(code: int, msg: Optional[str])
    qErrnoWarning(msg: Optional[str])
    """
    pass

def qFatal(msg, p_str=None): # real signature unknown; restored from __doc__
    """ qFatal(msg: Optional[str]) """
    pass

def qFloatDistance(a, b): # real signature unknown; restored from __doc__
    """ qFloatDistance(a: float, b: float) -> int """
    return 0

def qFormatLogMessage(type, context, buf, p_str=None): # real signature unknown; restored from __doc__
    """ qFormatLogMessage(type: QtMsgType, context: QMessageLogContext, buf: Optional[str]) -> str """
    return ""

def qFuzzyCompare(p1, p2): # real signature unknown; restored from __doc__
    """ qFuzzyCompare(p1: float, p2: float) -> bool """
    return False

def qInf(): # real signature unknown; restored from __doc__
    """ qInf() -> float """
    return 0.0

def qInfo(msg, p_str=None): # real signature unknown; restored from __doc__
    """ qInfo(msg: Optional[str]) """
    pass

def qInstallMessageHandler(a0, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """ qInstallMessageHandler(a0: Optional[Callable[[QtMsgType, QMessageLogContext, Optional[str]], None]]) -> Optional[Callable[[QtMsgType, QMessageLogContext, Optional[str]], None]] """
    pass

def qIsFinite(d): # real signature unknown; restored from __doc__
    """ qIsFinite(d: float) -> bool """
    return False

def qIsInf(d): # real signature unknown; restored from __doc__
    """ qIsInf(d: float) -> bool """
    return False

def qIsNaN(d): # real signature unknown; restored from __doc__
    """ qIsNaN(d: float) -> bool """
    return False

def qIsNull(d): # real signature unknown; restored from __doc__
    """ qIsNull(d: float) -> bool """
    return False

def qQNaN(): # real signature unknown; restored from __doc__
    """ qQNaN() -> float """
    return 0.0

def qrand(): # real signature unknown; restored from __doc__
    """ qrand() -> int """
    return 0

def qRegisterResourceData(a0, a1, bytes=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """ qRegisterResourceData(a0: int, a1: Optional[bytes], a2: Optional[bytes], a3: Optional[bytes]) -> bool """
    pass

def qRemovePostRoutine(a0, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """ qRemovePostRoutine(a0: Callable[..., None]) """
    pass

def qRound(d): # real signature unknown; restored from __doc__
    """ qRound(d: float) -> int """
    return 0

def qRound64(d): # real signature unknown; restored from __doc__
    """ qRound64(d: float) -> int """
    return 0

def qSetFieldWidth(width): # real signature unknown; restored from __doc__
    """ qSetFieldWidth(width: int) -> QTextStreamManipulator """
    return QTextStreamManipulator

def qSetMessagePattern(messagePattern, p_str=None): # real signature unknown; restored from __doc__
    """ qSetMessagePattern(messagePattern: Optional[str]) """
    pass

def qSetPadChar(ch): # real signature unknown; restored from __doc__
    """ qSetPadChar(ch: str) -> QTextStreamManipulator """
    return QTextStreamManipulator

def qSetRealNumberPrecision(precision): # real signature unknown; restored from __doc__
    """ qSetRealNumberPrecision(precision: int) -> QTextStreamManipulator """
    return QTextStreamManipulator

def qSharedBuild(): # real signature unknown; restored from __doc__
    """ qSharedBuild() -> bool """
    return False

def qSNaN(): # real signature unknown; restored from __doc__
    """ qSNaN() -> float """
    return 0.0

def qsrand(seed): # real signature unknown; restored from __doc__
    """ qsrand(seed: int) """
    pass

def QT_TRANSLATE_NOOP(a0, a1): # real signature unknown; restored from __doc__
    """ QT_TRANSLATE_NOOP(a0: str, a1: str) -> str """
    return ""

def QT_TR_NOOP(a0): # real signature unknown; restored from __doc__
    """ QT_TR_NOOP(a0: str) -> str """
    return ""

def QT_TR_NOOP_UTF8(a0): # real signature unknown; restored from __doc__
    """ QT_TR_NOOP_UTF8(a0: str) -> str """
    return ""

def qUncompress(data, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
    """ qUncompress(data: Union[QByteArray, bytes, bytearray]) -> QByteArray """
    return QByteArray

def qUnregisterResourceData(a0, a1, bytes=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """ qUnregisterResourceData(a0: int, a1: Optional[bytes], a2: Optional[bytes], a3: Optional[bytes]) -> bool """
    pass

def qVersion(): # real signature unknown; restored from __doc__
    """ qVersion() -> Optional[str] """
    pass

def qWarning(msg, p_str=None): # real signature unknown; restored from __doc__
    """ qWarning(msg: Optional[str]) """
    pass

def Q_ARG(type, data): # real signature unknown; restored from __doc__
    """ Q_ARG(type: Any, data: Any) -> QGenericArgument """
    return QGenericArgument

def Q_CLASSINFO(name, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """ Q_CLASSINFO(name: Optional[str], value: Optional[str]) """
    pass

def Q_ENUM(a0, type=None, enum_Enum=None): # real signature unknown; restored from __doc__
    """ Q_ENUM(a0: Union[type, enum.Enum]) """
    pass

def Q_ENUMS(*args): # real signature unknown; restored from __doc__
    """ Q_ENUMS(*args: Any) """
    pass

def Q_FLAG(a0, type=None, enum_Enum=None): # real signature unknown; restored from __doc__
    """ Q_FLAG(a0: Union[type, enum.Enum]) """
    pass

def Q_FLAGS(*args): # real signature unknown; restored from __doc__
    """ Q_FLAGS(*args: Any) """
    pass

def Q_RETURN_ARG(type): # real signature unknown; restored from __doc__
    """ Q_RETURN_ARG(type: Any) -> QGenericReturnArgument """
    return QGenericReturnArgument

def reset(s): # real signature unknown; restored from __doc__
    """ reset(s: QTextStream) -> QTextStream """
    return QTextStream

def right(s): # real signature unknown; restored from __doc__
    """ right(s: QTextStream) -> QTextStream """
    return QTextStream

def scientific(s): # real signature unknown; restored from __doc__
    """ scientific(s: QTextStream) -> QTextStream """
    return QTextStream

def showbase(s): # real signature unknown; restored from __doc__
    """ showbase(s: QTextStream) -> QTextStream """
    return QTextStream

def uppercasebase(s): # real signature unknown; restored from __doc__
    """ uppercasebase(s: QTextStream) -> QTextStream """
    return QTextStream

def uppercasedigits(s): # real signature unknown; restored from __doc__
    """ uppercasedigits(s: QTextStream) -> QTextStream """
    return QTextStream

def ws(s): # real signature unknown; restored from __doc__
    """ ws(s: QTextStream) -> QTextStream """
    return QTextStream

# classes

from .pyqtBoundSignal import pyqtBoundSignal
from .pyqtProperty import pyqtProperty
from .pyqtSignal import pyqtSignal
from .QObject import QObject
from .QAbstractAnimation import QAbstractAnimation
from .QAbstractEventDispatcher import QAbstractEventDispatcher
from .QAbstractItemModel import QAbstractItemModel
from .QAbstractListModel import QAbstractListModel
from .QAbstractNativeEventFilter import QAbstractNativeEventFilter
from .QAbstractProxyModel import QAbstractProxyModel
from .QAbstractState import QAbstractState
from .QAbstractTableModel import QAbstractTableModel
from .QAbstractTransition import QAbstractTransition
from .QAnimationGroup import QAnimationGroup
from .QBasicTimer import QBasicTimer
from .QBitArray import QBitArray
from .QIODevice import QIODevice
from .QBuffer import QBuffer
from .QByteArray import QByteArray
from .QByteArrayMatcher import QByteArrayMatcher
from .QCalendar import QCalendar
from .QCborError import QCborError
from .QCborKnownTags import QCborKnownTags
from .QCborSimpleType import QCborSimpleType
from .QCborStreamReader import QCborStreamReader
from .QCborStreamWriter import QCborStreamWriter
from .QEvent import QEvent
from .QChildEvent import QChildEvent
from .QCollator import QCollator
from .QCollatorSortKey import QCollatorSortKey
from .QCommandLineOption import QCommandLineOption
from .QCommandLineParser import QCommandLineParser
from .QConcatenateTablesProxyModel import QConcatenateTablesProxyModel
from .QCoreApplication import QCoreApplication
from .QCryptographicHash import QCryptographicHash
from .QDataStream import QDataStream
from .QDate import QDate
from .QDateTime import QDateTime
from .QDeadlineTimer import QDeadlineTimer
from .QDir import QDir
from .QDirIterator import QDirIterator
from .QDynamicPropertyChangeEvent import QDynamicPropertyChangeEvent
from .QEasingCurve import QEasingCurve
from .QElapsedTimer import QElapsedTimer
from .QEventLoop import QEventLoop
from .QEventLoopLocker import QEventLoopLocker
from .QEventTransition import QEventTransition
from .QFileDevice import QFileDevice
from .QFile import QFile
from .QFileInfo import QFileInfo
from .QFileSelector import QFileSelector
from .QFileSystemWatcher import QFileSystemWatcher
from .QFinalState import QFinalState
from .QGenericArgument import QGenericArgument
from .QGenericReturnArgument import QGenericReturnArgument
from .QHistoryState import QHistoryState
from .QIdentityProxyModel import QIdentityProxyModel
from .QItemSelection import QItemSelection
from .QItemSelectionModel import QItemSelectionModel
from .QItemSelectionRange import QItemSelectionRange
from .QJsonDocument import QJsonDocument
from .QJsonParseError import QJsonParseError
from .QJsonValue import QJsonValue
from .QLibrary import QLibrary
from .QLibraryInfo import QLibraryInfo
from .QLine import QLine
from .QLineF import QLineF
from .QLocale import QLocale
from .QLockFile import QLockFile
from .QLoggingCategory import QLoggingCategory
from .QMargins import QMargins
from .QMarginsF import QMarginsF
from .QMessageAuthenticationCode import QMessageAuthenticationCode
from .QMessageLogContext import QMessageLogContext
from .QMessageLogger import QMessageLogger
from .QMetaClassInfo import QMetaClassInfo
from .QMetaEnum import QMetaEnum
from .QMetaMethod import QMetaMethod
from .QMetaObject import QMetaObject
from .QMetaProperty import QMetaProperty
from .QMetaType import QMetaType
from .QMimeData import QMimeData
from .QMimeDatabase import QMimeDatabase
from .QMimeType import QMimeType
from .QModelIndex import QModelIndex
from .QMutex import QMutex
from .QMutexLocker import QMutexLocker
from .QObjectCleanupHandler import QObjectCleanupHandler
from .QOperatingSystemVersion import QOperatingSystemVersion
from .QParallelAnimationGroup import QParallelAnimationGroup
from .QPauseAnimation import QPauseAnimation
from .QPersistentModelIndex import QPersistentModelIndex
from .QPluginLoader import QPluginLoader
from .QPoint import QPoint
from .QPointF import QPointF
from .QProcess import QProcess
from .QProcessEnvironment import QProcessEnvironment
from .QVariantAnimation import QVariantAnimation
from .QPropertyAnimation import QPropertyAnimation
from .QRandomGenerator import QRandomGenerator
from .QReadLocker import QReadLocker
from .QReadWriteLock import QReadWriteLock
from .QRect import QRect
from .QRectF import QRectF
from .QRecursiveMutex import QRecursiveMutex
from .QRegExp import QRegExp
from .QRegularExpression import QRegularExpression
from .QRegularExpressionMatch import QRegularExpressionMatch
from .QRegularExpressionMatchIterator import QRegularExpressionMatchIterator
from .QResource import QResource
from .QRunnable import QRunnable
from .QSaveFile import QSaveFile
from .QSemaphore import QSemaphore
from .QSemaphoreReleaser import QSemaphoreReleaser
from .QSequentialAnimationGroup import QSequentialAnimationGroup
from .QSettings import QSettings
from .QSharedMemory import QSharedMemory
from .QSignalBlocker import QSignalBlocker
from .QSignalMapper import QSignalMapper
from .QSignalTransition import QSignalTransition
from .QSize import QSize
from .QSizeF import QSizeF
from .QSocketNotifier import QSocketNotifier
from .QSortFilterProxyModel import QSortFilterProxyModel
from .QStandardPaths import QStandardPaths
from .QState import QState
from .QStateMachine import QStateMachine
from .QStorageInfo import QStorageInfo
from .QStringListModel import QStringListModel
from .QSysInfo import QSysInfo
from .QSystemSemaphore import QSystemSemaphore
from .Qt import Qt
from .QTemporaryDir import QTemporaryDir
from .QTemporaryFile import QTemporaryFile
from .QTextBoundaryFinder import QTextBoundaryFinder
from .QTextCodec import QTextCodec
from .QTextDecoder import QTextDecoder
from .QTextEncoder import QTextEncoder
from .QTextStream import QTextStream
from .QTextStreamManipulator import QTextStreamManipulator
from .QThread import QThread
from .QThreadPool import QThreadPool
from .QTime import QTime
from .QTimeLine import QTimeLine
from .QTimer import QTimer
from .QTimerEvent import QTimerEvent
from .QTimeZone import QTimeZone
from .QtMsgType import QtMsgType
from .QTranslator import QTranslator
from .QTransposeProxyModel import QTransposeProxyModel
from .QUrl import QUrl
from .QUrlQuery import QUrlQuery
from .QUuid import QUuid
from .QVariant import QVariant
from .QVersionNumber import QVersionNumber
from .QWaitCondition import QWaitCondition
from .QWinEventNotifier import QWinEventNotifier
from .QWriteLocker import QWriteLocker
from .QXmlStreamAttribute import QXmlStreamAttribute
from .QXmlStreamAttributes import QXmlStreamAttributes
from .QXmlStreamEntityDeclaration import QXmlStreamEntityDeclaration
from .QXmlStreamEntityResolver import QXmlStreamEntityResolver
from .QXmlStreamNamespaceDeclaration import QXmlStreamNamespaceDeclaration
from .QXmlStreamNotationDeclaration import QXmlStreamNotationDeclaration
from .QXmlStreamReader import QXmlStreamReader
from .QXmlStreamWriter import QXmlStreamWriter
# variables with complex values

PYQT_CONFIGURATION = {
    'sip_flags': '-n PyQt5.sip -t Qt_5_15_2 -t WS_WIN',
}




