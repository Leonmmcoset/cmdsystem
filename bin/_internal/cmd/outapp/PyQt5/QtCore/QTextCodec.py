# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


class QTextCodec(__sip.wrapper):
    """ QTextCodec() """
    def aliases(self): # real signature unknown; restored from __doc__
        """ aliases(self) -> List[QByteArray] """
        return []

    def availableCodecs(self): # real signature unknown; restored from __doc__
        """ availableCodecs() -> List[QByteArray] """
        return []

    def availableMibs(self): # real signature unknown; restored from __doc__
        """ availableMibs() -> List[int] """
        return []

    def canEncode(self, a0, p_str=None): # real signature unknown; restored from __doc__
        """ canEncode(self, a0: Optional[str]) -> bool """
        return False

    def codecForHtml(self, ba, QByteArray=None, bytes=None, bytearray=None, *args=None, **kwargs=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        codecForHtml(ba: Union[QByteArray, bytes, bytearray]) -> Optional[QTextCodec]
        codecForHtml(ba: Union[QByteArray, bytes, bytearray], defaultCodec: Optional[QTextCodec]) -> Optional[QTextCodec]
        """
        pass

    def codecForLocale(self): # real signature unknown; restored from __doc__
        """ codecForLocale() -> Optional[QTextCodec] """
        pass

    def codecForMib(self, mib): # real signature unknown; restored from __doc__
        """ codecForMib(mib: int) -> Optional[QTextCodec] """
        pass

    def codecForName(self, name, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        codecForName(name: Union[QByteArray, bytes, bytearray]) -> Optional[QTextCodec]
        codecForName(name: Optional[str]) -> Optional[QTextCodec]
        """
        pass

    def codecForUtfText(self, ba, QByteArray=None, bytes=None, bytearray=None, *args=None, **kwargs=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        codecForUtfText(ba: Union[QByteArray, bytes, bytearray]) -> Optional[QTextCodec]
        codecForUtfText(ba: Union[QByteArray, bytes, bytearray], defaultCodec: Optional[QTextCodec]) -> Optional[QTextCodec]
        """
        pass

    def convertFromUnicode(self, in_, PyQt5_sip_array=None, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ convertFromUnicode(self, in_: Optional[PyQt5.sip.array[str]], state: Optional[QTextCodec.ConverterState]) -> QByteArray """
        pass

    def convertToUnicode(self, in_, PyQt5_sip_array=None, bytes=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ convertToUnicode(self, in_: Optional[PyQt5.sip.array[bytes]], state: Optional[QTextCodec.ConverterState]) -> str """
        pass

    def fromUnicode(self, uc, p_str=None): # real signature unknown; restored from __doc__
        """ fromUnicode(self, uc: Optional[str]) -> QByteArray """
        return QByteArray

    def makeDecoder(self, flags, QTextCodec_ConversionFlags=None, QTextCodec_ConversionFlag=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ makeDecoder(self, flags: Union[QTextCodec.ConversionFlags, QTextCodec.ConversionFlag] = QTextCodec.DefaultConversion) -> Optional[QTextDecoder] """
        pass

    def makeEncoder(self, flags, QTextCodec_ConversionFlags=None, QTextCodec_ConversionFlag=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ makeEncoder(self, flags: Union[QTextCodec.ConversionFlags, QTextCodec.ConversionFlag] = QTextCodec.DefaultConversion) -> Optional[QTextEncoder] """
        pass

    def mibEnum(self): # real signature unknown; restored from __doc__
        """ mibEnum(self) -> int """
        return 0

    def name(self): # real signature unknown; restored from __doc__
        """ name(self) -> QByteArray """
        return QByteArray

    def setCodecForLocale(self, c, QTextCodec=None): # real signature unknown; restored from __doc__
        """ setCodecForLocale(c: Optional[QTextCodec]) """
        pass

    def toUnicode(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        toUnicode(self, a0: Union[QByteArray, bytes, bytearray]) -> str
        toUnicode(self, chars: Optional[bytes]) -> str
        toUnicode(self, in_: Optional[PyQt5.sip.array[bytes]], state: Optional[QTextCodec.ConverterState] = None) -> str
        """
        return ""

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    ConvertInvalidToNull = -2147483648
    DefaultConversion = 0
    IgnoreHeader = 1


