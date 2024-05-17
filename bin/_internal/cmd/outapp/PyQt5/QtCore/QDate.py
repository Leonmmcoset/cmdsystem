# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


class QDate(__sip.simplewrapper):
    """
    QDate()
    QDate(y: int, m: int, d: int)
    QDate(y: int, m: int, d: int, cal: QCalendar)
    QDate(a0: QDate)
    """
    def addDays(self, days): # real signature unknown; restored from __doc__
        """ addDays(self, days: int) -> QDate """
        return QDate

    def addMonths(self, months, cal=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        addMonths(self, months: int) -> QDate
        addMonths(self, months: int, cal: QCalendar) -> QDate
        """
        return QDate

    def addYears(self, years, cal=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        addYears(self, years: int) -> QDate
        addYears(self, years: int, cal: QCalendar) -> QDate
        """
        return QDate

    def currentDate(self): # real signature unknown; restored from __doc__
        """ currentDate() -> QDate """
        return QDate

    def day(self, cal=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        day(self) -> int
        day(self, cal: QCalendar) -> int
        """
        return 0

    def dayOfWeek(self, cal=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        dayOfWeek(self) -> int
        dayOfWeek(self, cal: QCalendar) -> int
        """
        return 0

    def dayOfYear(self, cal=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        dayOfYear(self) -> int
        dayOfYear(self, cal: QCalendar) -> int
        """
        return 0

    def daysInMonth(self, cal=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        daysInMonth(self) -> int
        daysInMonth(self, cal: QCalendar) -> int
        """
        return 0

    def daysInYear(self, cal=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        daysInYear(self) -> int
        daysInYear(self, cal: QCalendar) -> int
        """
        return 0

    def daysTo(self, a0, QDate=None, datetime_date=None): # real signature unknown; restored from __doc__
        """ daysTo(self, a0: Union[QDate, datetime.date]) -> int """
        return 0

    def endOfDay(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        endOfDay(self, spec: Qt.TimeSpec = Qt.LocalTime, offsetSeconds: int = 0) -> QDateTime
        endOfDay(self, zone: QTimeZone) -> QDateTime
        """
        return QDateTime

    def fromJulianDay(self, jd): # real signature unknown; restored from __doc__
        """ fromJulianDay(jd: int) -> QDate """
        return QDate

    def fromString(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        fromString(string: Optional[str], format: Qt.DateFormat = Qt.TextDate) -> QDate
        fromString(s: Optional[str], format: Optional[str]) -> QDate
        fromString(s: Optional[str], format: Optional[str], cal: QCalendar) -> QDate
        """
        pass

    def getDate(self): # real signature unknown; restored from __doc__
        """ getDate(self) -> (Optional[int], Optional[int], Optional[int]) """
        pass

    def isLeapYear(self, year): # real signature unknown; restored from __doc__
        """ isLeapYear(year: int) -> bool """
        return False

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def isValid(self, y=None, m=None, d=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        isValid(self) -> bool
        isValid(y: int, m: int, d: int) -> bool
        """
        return False

    def longDayName(self, weekday, type=None): # real signature unknown; restored from __doc__
        """ longDayName(weekday: int, type: QDate.MonthNameType = QDate.DateFormat) -> str """
        return ""

    def longMonthName(self, month, type=None): # real signature unknown; restored from __doc__
        """ longMonthName(month: int, type: QDate.MonthNameType = QDate.DateFormat) -> str """
        return ""

    def month(self, cal=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        month(self) -> int
        month(self, cal: QCalendar) -> int
        """
        return 0

    def setDate(self, year, month, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setDate(self, year: int, month: int, date: int) -> bool
        setDate(self, year: int, month: int, day: int, cal: QCalendar) -> bool
        """
        return False

    def shortDayName(self, weekday, type=None): # real signature unknown; restored from __doc__
        """ shortDayName(weekday: int, type: QDate.MonthNameType = QDate.DateFormat) -> str """
        return ""

    def shortMonthName(self, month, type=None): # real signature unknown; restored from __doc__
        """ shortMonthName(month: int, type: QDate.MonthNameType = QDate.DateFormat) -> str """
        return ""

    def startOfDay(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        startOfDay(self, spec: Qt.TimeSpec = Qt.LocalTime, offsetSeconds: int = 0) -> QDateTime
        startOfDay(self, zone: QTimeZone) -> QDateTime
        """
        return QDateTime

    def toJulianDay(self): # real signature unknown; restored from __doc__
        """ toJulianDay(self) -> int """
        return 0

    def toPyDate(self): # real signature unknown; restored from __doc__
        """ toPyDate(self) -> datetime.date """
        pass

    def toString(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        toString(self, format: Qt.DateFormat = Qt.TextDate) -> str
        toString(self, f: Qt.DateFormat, cal: QCalendar) -> str
        toString(self, format: Optional[str]) -> str
        toString(self, format: Optional[str], cal: QCalendar) -> str
        """
        return ""

    def weekNumber(self): # real signature unknown; restored from __doc__
        """ weekNumber(self) -> (int, Optional[int]) """
        pass

    def year(self, cal=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        year(self) -> int
        year(self, cal: QCalendar) -> int
        """
        return 0

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


    DateFormat = 0
    StandaloneFormat = 1


