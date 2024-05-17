# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


class QTimeZone(__sip.simplewrapper):
    """
    QTimeZone()
    QTimeZone(ianaId: Union[QByteArray, bytes, bytearray])
    QTimeZone(offsetSeconds: int)
    QTimeZone(zoneId: Union[QByteArray, bytes, bytearray], offsetSeconds: int, name: Optional[str], abbreviation: Optional[str], country: QLocale.Country = QLocale.AnyCountry, comment: Optional[str] = '')
    QTimeZone(other: QTimeZone)
    """
    def abbreviation(self, atDateTime, QDateTime=None, datetime_datetime=None): # real signature unknown; restored from __doc__
        """ abbreviation(self, atDateTime: Union[QDateTime, datetime.datetime]) -> str """
        return ""

    def availableTimeZoneIds(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        availableTimeZoneIds() -> List[QByteArray]
        availableTimeZoneIds(country: QLocale.Country) -> List[QByteArray]
        availableTimeZoneIds(offsetSeconds: int) -> List[QByteArray]
        """
        return []

    def comment(self): # real signature unknown; restored from __doc__
        """ comment(self) -> str """
        return ""

    def country(self): # real signature unknown; restored from __doc__
        """ country(self) -> QLocale.Country """
        pass

    def daylightTimeOffset(self, atDateTime, QDateTime=None, datetime_datetime=None): # real signature unknown; restored from __doc__
        """ daylightTimeOffset(self, atDateTime: Union[QDateTime, datetime.datetime]) -> int """
        return 0

    def displayName(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        displayName(self, atDateTime: Union[QDateTime, datetime.datetime], nameType: QTimeZone.NameType = QTimeZone.DefaultName, locale: QLocale = QLocale()) -> str
        displayName(self, timeType: QTimeZone.TimeType, nameType: QTimeZone.NameType = QTimeZone.DefaultName, locale: QLocale = QLocale()) -> str
        """
        pass

    def hasDaylightTime(self): # real signature unknown; restored from __doc__
        """ hasDaylightTime(self) -> bool """
        return False

    def hasTransitions(self): # real signature unknown; restored from __doc__
        """ hasTransitions(self) -> bool """
        return False

    def ianaIdToWindowsId(self, ianaId, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ ianaIdToWindowsId(ianaId: Union[QByteArray, bytes, bytearray]) -> QByteArray """
        return QByteArray

    def id(self): # real signature unknown; restored from __doc__
        """ id(self) -> QByteArray """
        return QByteArray

    def isDaylightTime(self, atDateTime, QDateTime=None, datetime_datetime=None): # real signature unknown; restored from __doc__
        """ isDaylightTime(self, atDateTime: Union[QDateTime, datetime.datetime]) -> bool """
        return False

    def isTimeZoneIdAvailable(self, ianaId, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ isTimeZoneIdAvailable(ianaId: Union[QByteArray, bytes, bytearray]) -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def nextTransition(self, afterDateTime, QDateTime=None, datetime_datetime=None): # real signature unknown; restored from __doc__
        """ nextTransition(self, afterDateTime: Union[QDateTime, datetime.datetime]) -> QTimeZone.OffsetData """
        pass

    def offsetData(self, forDateTime, QDateTime=None, datetime_datetime=None): # real signature unknown; restored from __doc__
        """ offsetData(self, forDateTime: Union[QDateTime, datetime.datetime]) -> QTimeZone.OffsetData """
        pass

    def offsetFromUtc(self, atDateTime, QDateTime=None, datetime_datetime=None): # real signature unknown; restored from __doc__
        """ offsetFromUtc(self, atDateTime: Union[QDateTime, datetime.datetime]) -> int """
        return 0

    def previousTransition(self, beforeDateTime, QDateTime=None, datetime_datetime=None): # real signature unknown; restored from __doc__
        """ previousTransition(self, beforeDateTime: Union[QDateTime, datetime.datetime]) -> QTimeZone.OffsetData """
        pass

    def standardTimeOffset(self, atDateTime, QDateTime=None, datetime_datetime=None): # real signature unknown; restored from __doc__
        """ standardTimeOffset(self, atDateTime: Union[QDateTime, datetime.datetime]) -> int """
        return 0

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: QTimeZone) """
        pass

    def systemTimeZone(self): # real signature unknown; restored from __doc__
        """ systemTimeZone() -> QTimeZone """
        return QTimeZone

    def systemTimeZoneId(self): # real signature unknown; restored from __doc__
        """ systemTimeZoneId() -> QByteArray """
        return QByteArray

    def transitions(self, fromDateTime, QDateTime=None, datetime_datetime=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ transitions(self, fromDateTime: Union[QDateTime, datetime.datetime], toDateTime: Union[QDateTime, datetime.datetime]) -> List[QTimeZone.OffsetData] """
        pass

    def utc(self): # real signature unknown; restored from __doc__
        """ utc() -> QTimeZone """
        return QTimeZone

    def windowsIdToDefaultIanaId(self, windowsId, QByteArray=None, bytes=None, bytearray=None, *args=None, **kwargs=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        windowsIdToDefaultIanaId(windowsId: Union[QByteArray, bytes, bytearray]) -> QByteArray
        windowsIdToDefaultIanaId(windowsId: Union[QByteArray, bytes, bytearray], country: QLocale.Country) -> QByteArray
        """
        return QByteArray

    def windowsIdToIanaIds(self, windowsId, QByteArray=None, bytes=None, bytearray=None, *args=None, **kwargs=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        windowsIdToIanaIds(windowsId: Union[QByteArray, bytes, bytearray]) -> List[QByteArray]
        windowsIdToIanaIds(windowsId: Union[QByteArray, bytes, bytearray], country: QLocale.Country) -> List[QByteArray]
        """
        return []

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    DaylightTime = 1
    DefaultName = 0
    GenericTime = 2
    LongName = 1
    OffsetName = 3
    ShortName = 2
    StandardTime = 0
    __hash__ = None


