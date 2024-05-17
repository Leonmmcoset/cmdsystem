# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


class QDateTime(__sip.simplewrapper):
    """
    QDateTime()
    QDateTime(other: Union[QDateTime, datetime.datetime])
    QDateTime(a0: Union[QDate, datetime.date])
    QDateTime(date: Union[QDate, datetime.date], time: Union[QTime, datetime.time], timeSpec: Qt.TimeSpec = Qt.LocalTime)
    QDateTime(year: int, month: int, day: int, hour: int, minute: int, second: int = 0, msec: int = 0, timeSpec: int = 0)
    QDateTime(date: Union[QDate, datetime.date], time: Union[QTime, datetime.time], spec: Qt.TimeSpec, offsetSeconds: int)
    QDateTime(date: Union[QDate, datetime.date], time: Union[QTime, datetime.time], timeZone: QTimeZone)
    """
    def addDays(self, days): # real signature unknown; restored from __doc__
        """ addDays(self, days: int) -> QDateTime """
        return QDateTime

    def addMonths(self, months): # real signature unknown; restored from __doc__
        """ addMonths(self, months: int) -> QDateTime """
        return QDateTime

    def addMSecs(self, msecs): # real signature unknown; restored from __doc__
        """ addMSecs(self, msecs: int) -> QDateTime """
        return QDateTime

    def addSecs(self, secs): # real signature unknown; restored from __doc__
        """ addSecs(self, secs: int) -> QDateTime """
        return QDateTime

    def addYears(self, years): # real signature unknown; restored from __doc__
        """ addYears(self, years: int) -> QDateTime """
        return QDateTime

    def currentDateTime(self): # real signature unknown; restored from __doc__
        """ currentDateTime() -> QDateTime """
        return QDateTime

    def currentDateTimeUtc(self): # real signature unknown; restored from __doc__
        """ currentDateTimeUtc() -> QDateTime """
        return QDateTime

    def currentMSecsSinceEpoch(self): # real signature unknown; restored from __doc__
        """ currentMSecsSinceEpoch() -> int """
        return 0

    def currentSecsSinceEpoch(self): # real signature unknown; restored from __doc__
        """ currentSecsSinceEpoch() -> int """
        return 0

    def date(self): # real signature unknown; restored from __doc__
        """ date(self) -> QDate """
        return QDate

    def daysTo(self, a0, QDateTime=None, datetime_datetime=None): # real signature unknown; restored from __doc__
        """ daysTo(self, a0: Union[QDateTime, datetime.datetime]) -> int """
        return 0

    def fromMSecsSinceEpoch(self, msecs, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        fromMSecsSinceEpoch(msecs: int) -> QDateTime
        fromMSecsSinceEpoch(msecs: int, spec: Qt.TimeSpec, offsetSeconds: int = 0) -> QDateTime
        fromMSecsSinceEpoch(msecs: int, timeZone: QTimeZone) -> QDateTime
        """
        return QDateTime

    def fromSecsSinceEpoch(self, secs, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        fromSecsSinceEpoch(secs: int, spec: Qt.TimeSpec = Qt.LocalTime, offsetSeconds: int = 0) -> QDateTime
        fromSecsSinceEpoch(secs: int, timeZone: QTimeZone) -> QDateTime
        """
        return QDateTime

    def fromString(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        fromString(string: Optional[str], format: Qt.DateFormat = Qt.TextDate) -> QDateTime
        fromString(s: Optional[str], format: Optional[str]) -> QDateTime
        fromString(s: Optional[str], format: Optional[str], cal: QCalendar) -> QDateTime
        """
        pass

    def fromTime_t(self, secsSince1Jan1970UTC, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        fromTime_t(secsSince1Jan1970UTC: int) -> QDateTime
        fromTime_t(secsSince1Jan1970UTC: int, spec: Qt.TimeSpec, offsetSeconds: int = 0) -> QDateTime
        fromTime_t(secsSince1Jan1970UTC: int, timeZone: QTimeZone) -> QDateTime
        """
        return QDateTime

    def isDaylightTime(self): # real signature unknown; restored from __doc__
        """ isDaylightTime(self) -> bool """
        return False

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def msecsTo(self, a0, QDateTime=None, datetime_datetime=None): # real signature unknown; restored from __doc__
        """ msecsTo(self, a0: Union[QDateTime, datetime.datetime]) -> int """
        return 0

    def offsetFromUtc(self): # real signature unknown; restored from __doc__
        """ offsetFromUtc(self) -> int """
        return 0

    def secsTo(self, a0, QDateTime=None, datetime_datetime=None): # real signature unknown; restored from __doc__
        """ secsTo(self, a0: Union[QDateTime, datetime.datetime]) -> int """
        return 0

    def setDate(self, date, QDate=None, datetime_date=None): # real signature unknown; restored from __doc__
        """ setDate(self, date: Union[QDate, datetime.date]) """
        pass

    def setMSecsSinceEpoch(self, msecs): # real signature unknown; restored from __doc__
        """ setMSecsSinceEpoch(self, msecs: int) """
        pass

    def setOffsetFromUtc(self, offsetSeconds): # real signature unknown; restored from __doc__
        """ setOffsetFromUtc(self, offsetSeconds: int) """
        pass

    def setSecsSinceEpoch(self, secs): # real signature unknown; restored from __doc__
        """ setSecsSinceEpoch(self, secs: int) """
        pass

    def setTime(self, time, QTime=None, datetime_time=None): # real signature unknown; restored from __doc__
        """ setTime(self, time: Union[QTime, datetime.time]) """
        pass

    def setTimeSpec(self, spec): # real signature unknown; restored from __doc__
        """ setTimeSpec(self, spec: Qt.TimeSpec) """
        pass

    def setTimeZone(self, toZone): # real signature unknown; restored from __doc__
        """ setTimeZone(self, toZone: QTimeZone) """
        pass

    def setTime_t(self, secsSince1Jan1970UTC): # real signature unknown; restored from __doc__
        """ setTime_t(self, secsSince1Jan1970UTC: int) """
        pass

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: QDateTime) """
        pass

    def time(self): # real signature unknown; restored from __doc__
        """ time(self) -> QTime """
        return QTime

    def timeSpec(self): # real signature unknown; restored from __doc__
        """ timeSpec(self) -> Qt.TimeSpec """
        pass

    def timeZone(self): # real signature unknown; restored from __doc__
        """ timeZone(self) -> QTimeZone """
        return QTimeZone

    def timeZoneAbbreviation(self): # real signature unknown; restored from __doc__
        """ timeZoneAbbreviation(self) -> str """
        return ""

    def toLocalTime(self): # real signature unknown; restored from __doc__
        """ toLocalTime(self) -> QDateTime """
        return QDateTime

    def toMSecsSinceEpoch(self): # real signature unknown; restored from __doc__
        """ toMSecsSinceEpoch(self) -> int """
        return 0

    def toOffsetFromUtc(self, offsetSeconds): # real signature unknown; restored from __doc__
        """ toOffsetFromUtc(self, offsetSeconds: int) -> QDateTime """
        return QDateTime

    def toPyDateTime(self): # real signature unknown; restored from __doc__
        """ toPyDateTime(self) -> datetime.datetime """
        pass

    def toSecsSinceEpoch(self): # real signature unknown; restored from __doc__
        """ toSecsSinceEpoch(self) -> int """
        return 0

    def toString(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        toString(self, format: Qt.DateFormat = Qt.TextDate) -> str
        toString(self, format: Optional[str]) -> str
        toString(self, format: Optional[str], cal: QCalendar) -> str
        """
        return ""

    def toTimeSpec(self, spec): # real signature unknown; restored from __doc__
        """ toTimeSpec(self, spec: Qt.TimeSpec) -> QDateTime """
        return QDateTime

    def toTimeZone(self, toZone): # real signature unknown; restored from __doc__
        """ toTimeZone(self, toZone: QTimeZone) -> QDateTime """
        return QDateTime

    def toTime_t(self): # real signature unknown; restored from __doc__
        """ toTime_t(self) -> int """
        return 0

    def toUTC(self): # real signature unknown; restored from __doc__
        """ toUTC(self) -> QDateTime """
        return QDateTime

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ True if self else False """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
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

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""




