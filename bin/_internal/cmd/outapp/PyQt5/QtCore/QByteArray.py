# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


class QByteArray(__sip.simplewrapper):
    """
    QByteArray()
    QByteArray(size: int, c: str)
    QByteArray(a: Union[QByteArray, bytes, bytearray])
    """
    def append(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        append(self, a: Union[QByteArray, bytes, bytearray]) -> QByteArray
        append(self, s: Optional[str]) -> QByteArray
        append(self, count: int, c: bytes) -> QByteArray
        """
        return QByteArray

    def at(self, i): # real signature unknown; restored from __doc__
        """ at(self, i: int) -> bytes """
        return b""

    def capacity(self): # real signature unknown; restored from __doc__
        """ capacity(self) -> int """
        return 0

    def chop(self, n): # real signature unknown; restored from __doc__
        """ chop(self, n: int) """
        pass

    def chopped(self, len): # real signature unknown; restored from __doc__
        """ chopped(self, len: int) -> QByteArray """
        return QByteArray

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def compare(self, a, QByteArray=None, bytes=None, bytearray=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ compare(self, a: Union[QByteArray, bytes, bytearray], cs: Qt.CaseSensitivity = Qt.CaseSensitive) -> int """
        pass

    def contains(self, a, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ contains(self, a: Union[QByteArray, bytes, bytearray]) -> bool """
        return False

    def count(self, a=None, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        count(self, a: Union[QByteArray, bytes, bytearray]) -> int
        count(self) -> int
        """
        return 0

    def data(self): # real signature unknown; restored from __doc__
        """ data(self) -> bytes """
        return b""

    def endsWith(self, a, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ endsWith(self, a: Union[QByteArray, bytes, bytearray]) -> bool """
        return False

    def fill(self, ch, size=-1): # real signature unknown; restored from __doc__
        """ fill(self, ch: str, size: int = -1) -> QByteArray """
        return QByteArray

    def fromBase64(self, base64, QByteArray=None, bytes=None, bytearray=None, *args=None, **kwargs=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        fromBase64(base64: Union[QByteArray, bytes, bytearray]) -> QByteArray
        fromBase64(base64: Union[QByteArray, bytes, bytearray], options: Union[QByteArray.Base64Options, QByteArray.Base64Option]) -> QByteArray
        """
        return QByteArray

    def fromBase64Encoding(self, base64, QByteArray=None, bytes=None, bytearray=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ fromBase64Encoding(base64: Union[QByteArray, bytes, bytearray], options: Union[QByteArray.Base64Options, QByteArray.Base64Option] = QByteArray.Base64Encoding) -> QByteArray.FromBase64Result """
        pass

    def fromHex(self, hexEncoded, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ fromHex(hexEncoded: Union[QByteArray, bytes, bytearray]) -> QByteArray """
        return QByteArray

    def fromPercentEncoding(self, input, QByteArray=None, bytes=None, bytearray=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ fromPercentEncoding(input: Union[QByteArray, bytes, bytearray], percent: str = '%') -> QByteArray """
        pass

    def fromRawData(self, a0, PyQt5_sip_array=None, bytes=None): # real signature unknown; restored from __doc__
        """ fromRawData(a0: Optional[PyQt5.sip.array[bytes]]) -> QByteArray """
        return QByteArray

    def indexOf(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        indexOf(self, ba: Union[QByteArray, bytes, bytearray], from_: int = 0) -> int
        indexOf(self, str: Optional[str], from_: int = 0) -> int
        """
        pass

    def insert(self, i, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        insert(self, i: int, a: Union[QByteArray, bytes, bytearray]) -> QByteArray
        insert(self, i: int, s: Optional[str]) -> QByteArray
        insert(self, i: int, count: int, c: bytes) -> QByteArray
        """
        return QByteArray

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ isEmpty(self) -> bool """
        return False

    def isLower(self): # real signature unknown; restored from __doc__
        """ isLower(self) -> bool """
        return False

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def isUpper(self): # real signature unknown; restored from __doc__
        """ isUpper(self) -> bool """
        return False

    def lastIndexOf(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        lastIndexOf(self, ba: Union[QByteArray, bytes, bytearray], from_: int = -1) -> int
        lastIndexOf(self, str: Optional[str], from_: int = -1) -> int
        """
        pass

    def left(self, len): # real signature unknown; restored from __doc__
        """ left(self, len: int) -> QByteArray """
        return QByteArray

    def leftJustified(self, width, fill=' ', truncate=False): # real signature unknown; restored from __doc__
        """ leftJustified(self, width: int, fill: str = ' ', truncate: bool = False) -> QByteArray """
        return QByteArray

    def length(self): # real signature unknown; restored from __doc__
        """ length(self) -> int """
        return 0

    def mid(self, pos, length=-1): # real signature unknown; restored from __doc__
        """ mid(self, pos: int, length: int = -1) -> QByteArray """
        return QByteArray

    def number(self, n, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        number(n: float, format: str = 'g', precision: int = 6) -> QByteArray
        number(n: int, base: int = 10) -> QByteArray
        """
        return QByteArray

    def prepend(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        prepend(self, a: Union[QByteArray, bytes, bytearray]) -> QByteArray
        prepend(self, count: int, c: bytes) -> QByteArray
        """
        return QByteArray

    def push_back(self, a, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ push_back(self, a: Union[QByteArray, bytes, bytearray]) """
        pass

    def push_front(self, a, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ push_front(self, a: Union[QByteArray, bytes, bytearray]) """
        pass

    def remove(self, index, len): # real signature unknown; restored from __doc__
        """ remove(self, index: int, len: int) -> QByteArray """
        return QByteArray

    def repeated(self, times): # real signature unknown; restored from __doc__
        """ repeated(self, times: int) -> QByteArray """
        return QByteArray

    def replace(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        replace(self, index: int, len: int, s: Union[QByteArray, bytes, bytearray]) -> QByteArray
        replace(self, before: Union[QByteArray, bytes, bytearray], after: Union[QByteArray, bytes, bytearray]) -> QByteArray
        replace(self, before: Optional[str], after: Union[QByteArray, bytes, bytearray]) -> QByteArray
        """
        return QByteArray

    def reserve(self, size): # real signature unknown; restored from __doc__
        """ reserve(self, size: int) """
        pass

    def resize(self, size): # real signature unknown; restored from __doc__
        """ resize(self, size: int) """
        pass

    def right(self, len): # real signature unknown; restored from __doc__
        """ right(self, len: int) -> QByteArray """
        return QByteArray

    def rightJustified(self, width, fill=' ', truncate=False): # real signature unknown; restored from __doc__
        """ rightJustified(self, width: int, fill: str = ' ', truncate: bool = False) -> QByteArray """
        return QByteArray

    def setNum(self, n, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setNum(self, n: float, format: str = 'g', precision: int = 6) -> QByteArray
        setNum(self, n: int, base: int = 10) -> QByteArray
        """
        return QByteArray

    def simplified(self): # real signature unknown; restored from __doc__
        """ simplified(self) -> QByteArray """
        return QByteArray

    def size(self): # real signature unknown; restored from __doc__
        """ size(self) -> int """
        return 0

    def split(self, sep): # real signature unknown; restored from __doc__
        """ split(self, sep: str) -> List[QByteArray] """
        return []

    def squeeze(self): # real signature unknown; restored from __doc__
        """ squeeze(self) """
        pass

    def startsWith(self, a, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ startsWith(self, a: Union[QByteArray, bytes, bytearray]) -> bool """
        return False

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: QByteArray) """
        pass

    def toBase64(self, options=None, QByteArray_Base64Options=None, QByteArray_Base64Option=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        toBase64(self) -> QByteArray
        toBase64(self, options: Union[QByteArray.Base64Options, QByteArray.Base64Option]) -> QByteArray
        """
        return QByteArray

    def toDouble(self): # real signature unknown; restored from __doc__
        """ toDouble(self) -> (float, Optional[bool]) """
        pass

    def toFloat(self): # real signature unknown; restored from __doc__
        """ toFloat(self) -> (float, Optional[bool]) """
        pass

    def toHex(self, separator=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        toHex(self) -> QByteArray
        toHex(self, separator: str) -> QByteArray
        """
        return QByteArray

    def toInt(self, base=10): # real signature unknown; restored from __doc__
        """ toInt(self, base: int = 10) -> (int, Optional[bool]) """
        pass

    def toLong(self, base=10): # real signature unknown; restored from __doc__
        """ toLong(self, base: int = 10) -> (int, Optional[bool]) """
        pass

    def toLongLong(self, base=10): # real signature unknown; restored from __doc__
        """ toLongLong(self, base: int = 10) -> (int, Optional[bool]) """
        pass

    def toLower(self): # real signature unknown; restored from __doc__
        """ toLower(self) -> QByteArray """
        return QByteArray

    def toPercentEncoding(self, exclude, QByteArray=None, bytes=None, bytearray=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ toPercentEncoding(self, exclude: Union[QByteArray, bytes, bytearray] = QByteArray(), include: Union[QByteArray, bytes, bytearray] = QByteArray(), percent: str = '%') -> QByteArray """
        pass

    def toShort(self, base=10): # real signature unknown; restored from __doc__
        """ toShort(self, base: int = 10) -> (int, Optional[bool]) """
        pass

    def toUInt(self, base=10): # real signature unknown; restored from __doc__
        """ toUInt(self, base: int = 10) -> (int, Optional[bool]) """
        pass

    def toULong(self, base=10): # real signature unknown; restored from __doc__
        """ toULong(self, base: int = 10) -> (int, Optional[bool]) """
        pass

    def toULongLong(self, base=10): # real signature unknown; restored from __doc__
        """ toULongLong(self, base: int = 10) -> (int, Optional[bool]) """
        pass

    def toUpper(self): # real signature unknown; restored from __doc__
        """ toUpper(self) -> QByteArray """
        return QByteArray

    def toUShort(self, base=10): # real signature unknown; restored from __doc__
        """ toUShort(self, base: int = 10) -> (int, Optional[bool]) """
        pass

    def trimmed(self): # real signature unknown; restored from __doc__
        """ trimmed(self) -> QByteArray """
        return QByteArray

    def truncate(self, pos): # real signature unknown; restored from __doc__
        """ truncate(self, pos: int) """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __contains__(self, *args, **kwargs): # real signature unknown
        """ Return key in self. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __iadd__(self, *args, **kwargs): # real signature unknown
        """ Implement self+=value. """
        pass

    def __imul__(self, *args, **kwargs): # real signature unknown
        """ Implement self*=value. """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    AbortOnBase64DecodingErrors = 4
    Base64Encoding = 0
    Base64UrlEncoding = 1
    IgnoreBase64DecodingErrors = 0
    KeepTrailingEquals = 0
    OmitTrailingEquals = 2


