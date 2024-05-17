# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


class QCalendar(__sip.simplewrapper):
    """
    QCalendar()
    QCalendar(system: QCalendar.System)
    QCalendar(name: Optional[str])
    QCalendar(a0: QCalendar)
    """
    def availableCalendars(self): # real signature unknown; restored from __doc__
        """ availableCalendars() -> List[str] """
        return []

    def dateFromParts(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        dateFromParts(self, year: int, month: int, day: int) -> QDate
        dateFromParts(self, parts: QCalendar.YearMonthDay) -> QDate
        """
        return QDate

    def dateTimeToString(self, format, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ dateTimeToString(self, format: Optional[str], datetime: Union[QDateTime, datetime.datetime], dateOnly: Union[QDate, datetime.date], timeOnly: Union[QTime, datetime.time], locale: QLocale) -> str """
        pass

    def dayOfWeek(self, date, QDate=None, datetime_date=None): # real signature unknown; restored from __doc__
        """ dayOfWeek(self, date: Union[QDate, datetime.date]) -> int """
        return 0

    def daysInMonth(self, month, year=None): # real signature unknown; restored from __doc__
        """ daysInMonth(self, month: int, year: int = QCalendar.Unspecified) -> int """
        return 0

    def daysInYear(self, year): # real signature unknown; restored from __doc__
        """ daysInYear(self, year: int) -> int """
        return 0

    def hasYearZero(self): # real signature unknown; restored from __doc__
        """ hasYearZero(self) -> bool """
        return False

    def isDateValid(self, year, month, day): # real signature unknown; restored from __doc__
        """ isDateValid(self, year: int, month: int, day: int) -> bool """
        return False

    def isGregorian(self): # real signature unknown; restored from __doc__
        """ isGregorian(self) -> bool """
        return False

    def isLeapYear(self, year): # real signature unknown; restored from __doc__
        """ isLeapYear(self, year: int) -> bool """
        return False

    def isLunar(self): # real signature unknown; restored from __doc__
        """ isLunar(self) -> bool """
        return False

    def isLuniSolar(self): # real signature unknown; restored from __doc__
        """ isLuniSolar(self) -> bool """
        return False

    def isProleptic(self): # real signature unknown; restored from __doc__
        """ isProleptic(self) -> bool """
        return False

    def isSolar(self): # real signature unknown; restored from __doc__
        """ isSolar(self) -> bool """
        return False

    def maximumDaysInMonth(self): # real signature unknown; restored from __doc__
        """ maximumDaysInMonth(self) -> int """
        return 0

    def maximumMonthsInYear(self): # real signature unknown; restored from __doc__
        """ maximumMonthsInYear(self) -> int """
        return 0

    def minimumDaysInMonth(self): # real signature unknown; restored from __doc__
        """ minimumDaysInMonth(self) -> int """
        return 0

    def monthName(self, locale, month, year=None, format=None): # real signature unknown; restored from __doc__
        """ monthName(self, locale: QLocale, month: int, year: int = QCalendar.Unspecified, format: QLocale.FormatType = QLocale.LongFormat) -> str """
        return ""

    def monthsInYear(self, year): # real signature unknown; restored from __doc__
        """ monthsInYear(self, year: int) -> int """
        return 0

    def name(self): # real signature unknown; restored from __doc__
        """ name(self) -> str """
        return ""

    def partsFromDate(self, date, QDate=None, datetime_date=None): # real signature unknown; restored from __doc__
        """ partsFromDate(self, date: Union[QDate, datetime.date]) -> QCalendar.YearMonthDay """
        pass

    def standaloneMonthName(self, locale, month, year=None, format=None): # real signature unknown; restored from __doc__
        """ standaloneMonthName(self, locale: QLocale, month: int, year: int = QCalendar.Unspecified, format: QLocale.FormatType = QLocale.LongFormat) -> str """
        return ""

    def standaloneWeekDayName(self, locale, day, format=None): # real signature unknown; restored from __doc__
        """ standaloneWeekDayName(self, locale: QLocale, day: int, format: QLocale.FormatType = QLocale.LongFormat) -> str """
        return ""

    def weekDayName(self, locale, day, format=None): # real signature unknown; restored from __doc__
        """ weekDayName(self, locale: QLocale, day: int, format: QLocale.FormatType = QLocale.LongFormat) -> str """
        return ""

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    Unspecified = -2147483648


