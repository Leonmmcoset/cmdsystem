# encoding: utf-8
# module PyQt5.QtWidgets
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


from .QWidget import QWidget

class QCalendarWidget(QWidget):
    """ QCalendarWidget(parent: Optional[QWidget] = None) """
    def actionEvent(self, *args, **kwargs): # real signature unknown
        pass

    def activated(self, *args, **kwargs): # real signature unknown
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

    def calendar(self): # real signature unknown; restored from __doc__
        """ calendar(self) -> QCalendar """
        pass

    def changeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def clicked(self, *args, **kwargs): # real signature unknown
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

    def closeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def contextMenuEvent(self, *args, **kwargs): # real signature unknown
        pass

    def create(self, *args, **kwargs): # real signature unknown
        pass

    def currentPageChanged(self, *args, **kwargs): # real signature unknown
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

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dateEditAcceptDelay(self): # real signature unknown; restored from __doc__
        """ dateEditAcceptDelay(self) -> int """
        return 0

    def dateTextFormat(self, date=None, QDate=None, datetime_date=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        dateTextFormat(self) -> Dict[QDate, QTextCharFormat]
        dateTextFormat(self, date: Union[QDate, datetime.date]) -> QTextCharFormat
        """
        return {}

    def destroy(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

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

    def event(self, event, QEvent=None): # real signature unknown; restored from __doc__
        """ event(self, event: Optional[QEvent]) -> bool """
        return False

    def eventFilter(self, watched, QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ eventFilter(self, watched: Optional[QObject], event: Optional[QEvent]) -> bool """
        pass

    def firstDayOfWeek(self): # real signature unknown; restored from __doc__
        """ firstDayOfWeek(self) -> Qt.DayOfWeek """
        pass

    def focusInEvent(self, *args, **kwargs): # real signature unknown
        pass

    def focusNextChild(self, *args, **kwargs): # real signature unknown
        pass

    def focusNextPrevChild(self, *args, **kwargs): # real signature unknown
        pass

    def focusOutEvent(self, *args, **kwargs): # real signature unknown
        pass

    def focusPreviousChild(self, *args, **kwargs): # real signature unknown
        pass

    def headerTextFormat(self): # real signature unknown; restored from __doc__
        """ headerTextFormat(self) -> QTextCharFormat """
        pass

    def hideEvent(self, *args, **kwargs): # real signature unknown
        pass

    def horizontalHeaderFormat(self): # real signature unknown; restored from __doc__
        """ horizontalHeaderFormat(self) -> QCalendarWidget.HorizontalHeaderFormat """
        pass

    def initPainter(self, *args, **kwargs): # real signature unknown
        pass

    def inputMethodEvent(self, *args, **kwargs): # real signature unknown
        pass

    def isDateEditEnabled(self): # real signature unknown; restored from __doc__
        """ isDateEditEnabled(self) -> bool """
        return False

    def isGridVisible(self): # real signature unknown; restored from __doc__
        """ isGridVisible(self) -> bool """
        return False

    def isNavigationBarVisible(self): # real signature unknown; restored from __doc__
        """ isNavigationBarVisible(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def keyPressEvent(self, event, QKeyEvent=None): # real signature unknown; restored from __doc__
        """ keyPressEvent(self, event: Optional[QKeyEvent]) """
        pass

    def keyReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def leaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def maximumDate(self): # real signature unknown; restored from __doc__
        """ maximumDate(self) -> QDate """
        pass

    def metric(self, *args, **kwargs): # real signature unknown
        pass

    def minimumDate(self): # real signature unknown; restored from __doc__
        """ minimumDate(self) -> QDate """
        pass

    def minimumSizeHint(self): # real signature unknown; restored from __doc__
        """ minimumSizeHint(self) -> QSize """
        pass

    def monthShown(self): # real signature unknown; restored from __doc__
        """ monthShown(self) -> int """
        return 0

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

    def paintCell(self, painter, QPainter=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ paintCell(self, painter: Optional[QPainter], rect: QRect, date: Union[QDate, datetime.date]) """
        pass

    def paintEvent(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def resizeEvent(self, event, QResizeEvent=None): # real signature unknown; restored from __doc__
        """ resizeEvent(self, event: Optional[QResizeEvent]) """
        pass

    def selectedDate(self): # real signature unknown; restored from __doc__
        """ selectedDate(self) -> QDate """
        pass

    def selectionChanged(self, *args, **kwargs): # real signature unknown
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

    def selectionMode(self): # real signature unknown; restored from __doc__
        """ selectionMode(self) -> QCalendarWidget.SelectionMode """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setCalendar(self, calendar): # real signature unknown; restored from __doc__
        """ setCalendar(self, calendar: QCalendar) """
        pass

    def setCurrentPage(self, year, month): # real signature unknown; restored from __doc__
        """ setCurrentPage(self, year: int, month: int) """
        pass

    def setDateEditAcceptDelay(self, delay): # real signature unknown; restored from __doc__
        """ setDateEditAcceptDelay(self, delay: int) """
        pass

    def setDateEditEnabled(self, enable): # real signature unknown; restored from __doc__
        """ setDateEditEnabled(self, enable: bool) """
        pass

    def setDateRange(self, min, QDate=None, datetime_date=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setDateRange(self, min: Union[QDate, datetime.date], max: Union[QDate, datetime.date]) """
        pass

    def setDateTextFormat(self, date, QDate=None, datetime_date=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setDateTextFormat(self, date: Union[QDate, datetime.date], color: QTextCharFormat) """
        pass

    def setFirstDayOfWeek(self, dayOfWeek): # real signature unknown; restored from __doc__
        """ setFirstDayOfWeek(self, dayOfWeek: Qt.DayOfWeek) """
        pass

    def setGridVisible(self, show): # real signature unknown; restored from __doc__
        """ setGridVisible(self, show: bool) """
        pass

    def setHeaderTextFormat(self, format): # real signature unknown; restored from __doc__
        """ setHeaderTextFormat(self, format: QTextCharFormat) """
        pass

    def setHorizontalHeaderFormat(self, format): # real signature unknown; restored from __doc__
        """ setHorizontalHeaderFormat(self, format: QCalendarWidget.HorizontalHeaderFormat) """
        pass

    def setMaximumDate(self, date, QDate=None, datetime_date=None): # real signature unknown; restored from __doc__
        """ setMaximumDate(self, date: Union[QDate, datetime.date]) """
        pass

    def setMinimumDate(self, date, QDate=None, datetime_date=None): # real signature unknown; restored from __doc__
        """ setMinimumDate(self, date: Union[QDate, datetime.date]) """
        pass

    def setNavigationBarVisible(self, visible): # real signature unknown; restored from __doc__
        """ setNavigationBarVisible(self, visible: bool) """
        pass

    def setSelectedDate(self, date, QDate=None, datetime_date=None): # real signature unknown; restored from __doc__
        """ setSelectedDate(self, date: Union[QDate, datetime.date]) """
        pass

    def setSelectionMode(self, mode): # real signature unknown; restored from __doc__
        """ setSelectionMode(self, mode: QCalendarWidget.SelectionMode) """
        pass

    def setVerticalHeaderFormat(self, format): # real signature unknown; restored from __doc__
        """ setVerticalHeaderFormat(self, format: QCalendarWidget.VerticalHeaderFormat) """
        pass

    def setWeekdayTextFormat(self, dayOfWeek, format): # real signature unknown; restored from __doc__
        """ setWeekdayTextFormat(self, dayOfWeek: Qt.DayOfWeek, format: QTextCharFormat) """
        pass

    def sharedPainter(self, *args, **kwargs): # real signature unknown
        pass

    def showEvent(self, *args, **kwargs): # real signature unknown
        pass

    def showNextMonth(self): # real signature unknown; restored from __doc__
        """ showNextMonth(self) """
        pass

    def showNextYear(self): # real signature unknown; restored from __doc__
        """ showNextYear(self) """
        pass

    def showPreviousMonth(self): # real signature unknown; restored from __doc__
        """ showPreviousMonth(self) """
        pass

    def showPreviousYear(self): # real signature unknown; restored from __doc__
        """ showPreviousYear(self) """
        pass

    def showSelectedDate(self): # real signature unknown; restored from __doc__
        """ showSelectedDate(self) """
        pass

    def showToday(self): # real signature unknown; restored from __doc__
        """ showToday(self) """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> QSize """
        pass

    def tabletEvent(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def updateCell(self, date, QDate=None, datetime_date=None): # real signature unknown; restored from __doc__
        """ updateCell(self, date: Union[QDate, datetime.date]) """
        pass

    def updateCells(self): # real signature unknown; restored from __doc__
        """ updateCells(self) """
        pass

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

    def verticalHeaderFormat(self): # real signature unknown; restored from __doc__
        """ verticalHeaderFormat(self) -> QCalendarWidget.VerticalHeaderFormat """
        pass

    def weekdayTextFormat(self, dayOfWeek): # real signature unknown; restored from __doc__
        """ weekdayTextFormat(self, dayOfWeek: Qt.DayOfWeek) -> QTextCharFormat """
        pass

    def wheelEvent(self, *args, **kwargs): # real signature unknown
        pass

    def yearShown(self): # real signature unknown; restored from __doc__
        """ yearShown(self) -> int """
        return 0

    def __init__(self, parent, QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    ISOWeekNumbers = 1
    LongDayNames = 3
    NoHorizontalHeader = 0
    NoSelection = 0
    NoVerticalHeader = 0
    ShortDayNames = 2
    SingleLetterDayNames = 1
    SingleSelection = 1


