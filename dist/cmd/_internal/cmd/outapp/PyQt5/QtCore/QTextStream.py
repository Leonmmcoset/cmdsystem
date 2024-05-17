# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


class QTextStream(__sip.simplewrapper):
    """
    QTextStream()
    QTextStream(device: Optional[QIODevice])
    QTextStream(array: Optional[QByteArray], mode: Union[QIODevice.OpenMode, QIODevice.OpenModeFlag] = QIODevice.ReadWrite)
    """
    def atEnd(self): # real signature unknown; restored from __doc__
        """ atEnd(self) -> bool """
        return False

    def autoDetectUnicode(self): # real signature unknown; restored from __doc__
        """ autoDetectUnicode(self) -> bool """
        return False

    def codec(self): # real signature unknown; restored from __doc__
        """ codec(self) -> Optional[QTextCodec] """
        pass

    def device(self): # real signature unknown; restored from __doc__
        """ device(self) -> Optional[QIODevice] """
        pass

    def fieldAlignment(self): # real signature unknown; restored from __doc__
        """ fieldAlignment(self) -> QTextStream.FieldAlignment """
        pass

    def fieldWidth(self): # real signature unknown; restored from __doc__
        """ fieldWidth(self) -> int """
        return 0

    def flush(self): # real signature unknown; restored from __doc__
        """ flush(self) """
        pass

    def generateByteOrderMark(self): # real signature unknown; restored from __doc__
        """ generateByteOrderMark(self) -> bool """
        return False

    def integerBase(self): # real signature unknown; restored from __doc__
        """ integerBase(self) -> int """
        return 0

    def locale(self): # real signature unknown; restored from __doc__
        """ locale(self) -> QLocale """
        return QLocale

    def numberFlags(self): # real signature unknown; restored from __doc__
        """ numberFlags(self) -> QTextStream.NumberFlags """
        pass

    def padChar(self): # real signature unknown; restored from __doc__
        """ padChar(self) -> str """
        return ""

    def pos(self): # real signature unknown; restored from __doc__
        """ pos(self) -> int """
        return 0

    def read(self, maxlen): # real signature unknown; restored from __doc__
        """ read(self, maxlen: int) -> str """
        return ""

    def readAll(self): # real signature unknown; restored from __doc__
        """ readAll(self) -> str """
        return ""

    def readLine(self, maxLength=0): # real signature unknown; restored from __doc__
        """ readLine(self, maxLength: int = 0) -> str """
        return ""

    def realNumberNotation(self): # real signature unknown; restored from __doc__
        """ realNumberNotation(self) -> QTextStream.RealNumberNotation """
        pass

    def realNumberPrecision(self): # real signature unknown; restored from __doc__
        """ realNumberPrecision(self) -> int """
        return 0

    def reset(self): # real signature unknown; restored from __doc__
        """ reset(self) """
        pass

    def resetStatus(self): # real signature unknown; restored from __doc__
        """ resetStatus(self) """
        pass

    def seek(self, pos): # real signature unknown; restored from __doc__
        """ seek(self, pos: int) -> bool """
        return False

    def setAutoDetectUnicode(self, enabled): # real signature unknown; restored from __doc__
        """ setAutoDetectUnicode(self, enabled: bool) """
        pass

    def setCodec(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setCodec(self, codec: Optional[QTextCodec])
        setCodec(self, codecName: Optional[str])
        """
        pass

    def setDevice(self, device, QIODevice=None): # real signature unknown; restored from __doc__
        """ setDevice(self, device: Optional[QIODevice]) """
        pass

    def setFieldAlignment(self, alignment): # real signature unknown; restored from __doc__
        """ setFieldAlignment(self, alignment: QTextStream.FieldAlignment) """
        pass

    def setFieldWidth(self, width): # real signature unknown; restored from __doc__
        """ setFieldWidth(self, width: int) """
        pass

    def setGenerateByteOrderMark(self, generate): # real signature unknown; restored from __doc__
        """ setGenerateByteOrderMark(self, generate: bool) """
        pass

    def setIntegerBase(self, base): # real signature unknown; restored from __doc__
        """ setIntegerBase(self, base: int) """
        pass

    def setLocale(self, locale): # real signature unknown; restored from __doc__
        """ setLocale(self, locale: QLocale) """
        pass

    def setNumberFlags(self, flags, QTextStream_NumberFlags=None, QTextStream_NumberFlag=None): # real signature unknown; restored from __doc__
        """ setNumberFlags(self, flags: Union[QTextStream.NumberFlags, QTextStream.NumberFlag]) """
        pass

    def setPadChar(self, ch): # real signature unknown; restored from __doc__
        """ setPadChar(self, ch: str) """
        pass

    def setRealNumberNotation(self, notation): # real signature unknown; restored from __doc__
        """ setRealNumberNotation(self, notation: QTextStream.RealNumberNotation) """
        pass

    def setRealNumberPrecision(self, precision): # real signature unknown; restored from __doc__
        """ setRealNumberPrecision(self, precision: int) """
        pass

    def setStatus(self, status): # real signature unknown; restored from __doc__
        """ setStatus(self, status: QTextStream.Status) """
        pass

    def skipWhiteSpace(self): # real signature unknown; restored from __doc__
        """ skipWhiteSpace(self) """
        pass

    def status(self): # real signature unknown; restored from __doc__
        """ status(self) -> QTextStream.Status """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __lshift__(self, *args, **kwargs): # real signature unknown
        """ Return self<<value. """
        pass

    def __rlshift__(self, *args, **kwargs): # real signature unknown
        """ Return value<<self. """
        pass

    def __rrshift__(self, *args, **kwargs): # real signature unknown
        """ Return value>>self. """
        pass

    def __rshift__(self, *args, **kwargs): # real signature unknown
        """ Return self>>value. """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    AlignAccountingStyle = 3
    AlignCenter = 2
    AlignLeft = 0
    AlignRight = 1
    FixedNotation = 1
    ForcePoint = 2
    ForceSign = 4
    Ok = 0
    ReadCorruptData = 2
    ReadPastEnd = 1
    ScientificNotation = 2
    ShowBase = 1
    SmartNotation = 0
    UppercaseBase = 8
    UppercaseDigits = 16
    WriteFailed = 3


