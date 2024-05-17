# encoding: utf-8
# module PyQt5.QtWidgets
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


from .QAbstractSpinBox import QAbstractSpinBox

class QDateTimeEdit(QAbstractSpinBox):
    """
    QDateTimeEdit(parent: Optional[QWidget] = None)
    QDateTimeEdit(datetime: Union[QDateTime, datetime.datetime], parent: Optional[QWidget] = None)
    QDateTimeEdit(date: Union[QDate, datetime.date], parent: Optional[QWidget] = None)
    QDateTimeEdit(time: Union[QTime, datetime.time], parent: Optional[QWidget] = None)
    """
    def actionEvent(self, *args, **kwargs): # real signature unknown
        pass

    def calendar(self): # real signature unknown; restored from __doc__
        """ calendar(self) -> QCalendar """
        pass

    def calendarPopup(self): # real signature unknown; restored from __doc__
        """ calendarPopup(self) -> bool """
        return False

    def calendarWidget(self): # real signature unknown; restored from __doc__
        """ calendarWidget(self) -> Optional[QCalendarWidget] """
        pass

    def changeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def clearMaximumDate(self): # real signature unknown; restored from __doc__
        """ clearMaximumDate(self) """
        pass

    def clearMaximumDateTime(self): # real signature unknown; restored from __doc__
        """ clearMaximumDateTime(self) """
        pass

    def clearMaximumTime(self): # real signature unknown; restored from __doc__
        """ clearMaximumTime(self) """
        pass

    def clearMinimumDate(self): # real signature unknown; restored from __doc__
        """ clearMinimumDate(self) """
        pass

    def clearMinimumDateTime(self): # real signature unknown; restored from __doc__
        """ clearMinimumDateTime(self) """
        pass

    def clearMinimumTime(self): # real signature unknown; restored from __doc__
        """ clearMinimumTime(self) """
        pass

    def closeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def contextMenuEvent(self, *args, **kwargs): # real signature unknown
        pass

    def create(self, *args, **kwargs): # real signature unknown
        pass

    def currentSection(self): # real signature unknown; restored from __doc__
        """ currentSection(self) -> QDateTimeEdit.Section """
        pass

    def currentSectionIndex(self): # real signature unknown; restored from __doc__
        """ currentSectionIndex(self) -> int """
        return 0

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def date(self): # real signature unknown; restored from __doc__
        """ date(self) -> QDate """
        pass

    def dateChanged(self, *args, **kwargs): # real signature unknown
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

    def dateTime(self): # real signature unknown; restored from __doc__
        """ dateTime(self) -> QDateTime """
        pass

    def dateTimeChanged(self, *args, **kwargs): # real signature unknown
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

    def dateTimeFromText(self, text, p_str=None): # real signature unknown; restored from __doc__
        """ dateTimeFromText(self, text: Optional[str]) -> QDateTime """
        pass

    def destroy(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def displayedSections(self): # real signature unknown; restored from __doc__
        """ displayedSections(self) -> QDateTimeEdit.Sections """
        pass

    def displayFormat(self): # real signature unknown; restored from __doc__
        """ displayFormat(self) -> str """
        return ""

    def dragEnterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dragLeaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dragMoveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dropEvent(self, *args, **kwargs): # real signature unknown
        pass

    def enterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, e, QEvent=None): # real signature unknown; restored from __doc__
        """ event(self, e: Optional[QEvent]) -> bool """
        return False

    def fixup(self, input, p_str=None): # real signature unknown; restored from __doc__
        """ fixup(self, input: Optional[str]) -> str """
        return ""

    def focusInEvent(self, e, QFocusEvent=None): # real signature unknown; restored from __doc__
        """ focusInEvent(self, e: Optional[QFocusEvent]) """
        pass

    def focusNextChild(self, *args, **kwargs): # real signature unknown
        pass

    def focusNextPrevChild(self, next): # real signature unknown; restored from __doc__
        """ focusNextPrevChild(self, next: bool) -> bool """
        return False

    def focusOutEvent(self, *args, **kwargs): # real signature unknown
        pass

    def focusPreviousChild(self, *args, **kwargs): # real signature unknown
        pass

    def hideEvent(self, *args, **kwargs): # real signature unknown
        pass

    def initPainter(self, *args, **kwargs): # real signature unknown
        pass

    def initStyleOption(self, option, QStyleOptionSpinBox=None): # real signature unknown; restored from __doc__
        """ initStyleOption(self, option: Optional[QStyleOptionSpinBox]) """
        pass

    def inputMethodEvent(self, *args, **kwargs): # real signature unknown
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def keyPressEvent(self, e, QKeyEvent=None): # real signature unknown; restored from __doc__
        """ keyPressEvent(self, e: Optional[QKeyEvent]) """
        pass

    def keyReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def leaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def lineEdit(self, *args, **kwargs): # real signature unknown
        pass

    def maximumDate(self): # real signature unknown; restored from __doc__
        """ maximumDate(self) -> QDate """
        pass

    def maximumDateTime(self): # real signature unknown; restored from __doc__
        """ maximumDateTime(self) -> QDateTime """
        pass

    def maximumTime(self): # real signature unknown; restored from __doc__
        """ maximumTime(self) -> QTime """
        pass

    def metric(self, *args, **kwargs): # real signature unknown
        pass

    def minimumDate(self): # real signature unknown; restored from __doc__
        """ minimumDate(self) -> QDate """
        pass

    def minimumDateTime(self): # real signature unknown; restored from __doc__
        """ minimumDateTime(self) -> QDateTime """
        pass

    def minimumTime(self): # real signature unknown; restored from __doc__
        """ minimumTime(self) -> QTime """
        pass

    def mouseDoubleClickEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mouseMoveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mousePressEvent(self, event, QMouseEvent=None): # real signature unknown; restored from __doc__
        """ mousePressEvent(self, event: Optional[QMouseEvent]) """
        pass

    def mouseReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def moveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def nativeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def paintEvent(self, event, QPaintEvent=None): # real signature unknown; restored from __doc__
        """ paintEvent(self, event: Optional[QPaintEvent]) """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def resizeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def sectionAt(self, index): # real signature unknown; restored from __doc__
        """ sectionAt(self, index: int) -> QDateTimeEdit.Section """
        pass

    def sectionCount(self): # real signature unknown; restored from __doc__
        """ sectionCount(self) -> int """
        return 0

    def sectionText(self, s): # real signature unknown; restored from __doc__
        """ sectionText(self, s: QDateTimeEdit.Section) -> str """
        return ""

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setCalendar(self, calendar): # real signature unknown; restored from __doc__
        """ setCalendar(self, calendar: QCalendar) """
        pass

    def setCalendarPopup(self, enable): # real signature unknown; restored from __doc__
        """ setCalendarPopup(self, enable: bool) """
        pass

    def setCalendarWidget(self, calendarWidget, QCalendarWidget=None): # real signature unknown; restored from __doc__
        """ setCalendarWidget(self, calendarWidget: Optional[QCalendarWidget]) """
        pass

    def setCurrentSection(self, section): # real signature unknown; restored from __doc__
        """ setCurrentSection(self, section: QDateTimeEdit.Section) """
        pass

    def setCurrentSectionIndex(self, index): # real signature unknown; restored from __doc__
        """ setCurrentSectionIndex(self, index: int) """
        pass

    def setDate(self, date, QDate=None, datetime_date=None): # real signature unknown; restored from __doc__
        """ setDate(self, date: Union[QDate, datetime.date]) """
        pass

    def setDateRange(self, min, QDate=None, datetime_date=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setDateRange(self, min: Union[QDate, datetime.date], max: Union[QDate, datetime.date]) """
        pass

    def setDateTime(self, dateTime, QDateTime=None, datetime_datetime=None): # real signature unknown; restored from __doc__
        """ setDateTime(self, dateTime: Union[QDateTime, datetime.datetime]) """
        pass

    def setDateTimeRange(self, min, QDateTime=None, datetime_datetime=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setDateTimeRange(self, min: Union[QDateTime, datetime.datetime], max: Union[QDateTime, datetime.datetime]) """
        pass

    def setDisplayFormat(self, format, p_str=None): # real signature unknown; restored from __doc__
        """ setDisplayFormat(self, format: Optional[str]) """
        pass

    def setLineEdit(self, *args, **kwargs): # real signature unknown
        pass

    def setMaximumDate(self, max, QDate=None, datetime_date=None): # real signature unknown; restored from __doc__
        """ setMaximumDate(self, max: Union[QDate, datetime.date]) """
        pass

    def setMaximumDateTime(self, dt, QDateTime=None, datetime_datetime=None): # real signature unknown; restored from __doc__
        """ setMaximumDateTime(self, dt: Union[QDateTime, datetime.datetime]) """
        pass

    def setMaximumTime(self, max, QTime=None, datetime_time=None): # real signature unknown; restored from __doc__
        """ setMaximumTime(self, max: Union[QTime, datetime.time]) """
        pass

    def setMinimumDate(self, min, QDate=None, datetime_date=None): # real signature unknown; restored from __doc__
        """ setMinimumDate(self, min: Union[QDate, datetime.date]) """
        pass

    def setMinimumDateTime(self, dt, QDateTime=None, datetime_datetime=None): # real signature unknown; restored from __doc__
        """ setMinimumDateTime(self, dt: Union[QDateTime, datetime.datetime]) """
        pass

    def setMinimumTime(self, min, QTime=None, datetime_time=None): # real signature unknown; restored from __doc__
        """ setMinimumTime(self, min: Union[QTime, datetime.time]) """
        pass

    def setSelectedSection(self, section): # real signature unknown; restored from __doc__
        """ setSelectedSection(self, section: QDateTimeEdit.Section) """
        pass

    def setTime(self, time, QTime=None, datetime_time=None): # real signature unknown; restored from __doc__
        """ setTime(self, time: Union[QTime, datetime.time]) """
        pass

    def setTimeRange(self, min, QTime=None, datetime_time=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setTimeRange(self, min: Union[QTime, datetime.time], max: Union[QTime, datetime.time]) """
        pass

    def setTimeSpec(self, spec): # real signature unknown; restored from __doc__
        """ setTimeSpec(self, spec: Qt.TimeSpec) """
        pass

    def sharedPainter(self, *args, **kwargs): # real signature unknown
        pass

    def showEvent(self, *args, **kwargs): # real signature unknown
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> QSize """
        pass

    def stepBy(self, steps): # real signature unknown; restored from __doc__
        """ stepBy(self, steps: int) """
        pass

    def stepEnabled(self): # real signature unknown; restored from __doc__
        """ stepEnabled(self) -> QAbstractSpinBox.StepEnabled """
        pass

    def tabletEvent(self, *args, **kwargs): # real signature unknown
        pass

    def textFromDateTime(self, dt, QDateTime=None, datetime_datetime=None): # real signature unknown; restored from __doc__
        """ textFromDateTime(self, dt: Union[QDateTime, datetime.datetime]) -> str """
        return ""

    def time(self): # real signature unknown; restored from __doc__
        """ time(self) -> QTime """
        pass

    def timeChanged(self, *args, **kwargs): # real signature unknown
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

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def timeSpec(self): # real signature unknown; restored from __doc__
        """ timeSpec(self) -> Qt.TimeSpec """
        pass

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

    def validate(self, input, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ validate(self, input: Optional[str], pos: int) -> (QValidator.State, str, int) """
        pass

    def wheelEvent(self, e, QWheelEvent=None): # real signature unknown; restored from __doc__
        """ wheelEvent(self, e: Optional[QWheelEvent]) """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    AmPmSection = 1
    DateSections_Mask = 1792
    DaySection = 256
    HourSection = 16
    MinuteSection = 8
    MonthSection = 512
    MSecSection = 2
    NoSection = 0
    SecondSection = 4
    TimeSections_Mask = 31
    YearSection = 1024


