# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QStandardItem(__sip.wrapper):
    """
    QStandardItem()
    QStandardItem(text: Optional[str])
    QStandardItem(icon: QIcon, text: Optional[str])
    QStandardItem(rows: int, columns: int = 1)
    QStandardItem(other: QStandardItem)
    """
    def accessibleDescription(self): # real signature unknown; restored from __doc__
        """ accessibleDescription(self) -> str """
        return ""

    def accessibleText(self): # real signature unknown; restored from __doc__
        """ accessibleText(self) -> str """
        return ""

    def appendColumn(self, items, QStandardItem=None): # real signature unknown; restored from __doc__
        """ appendColumn(self, items: Iterable[QStandardItem]) """
        pass

    def appendRow(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        appendRow(self, items: Iterable[QStandardItem])
        appendRow(self, aitem: Optional[QStandardItem])
        """
        pass

    def appendRows(self, items, QStandardItem=None): # real signature unknown; restored from __doc__
        """ appendRows(self, items: Iterable[QStandardItem]) """
        pass

    def background(self): # real signature unknown; restored from __doc__
        """ background(self) -> QBrush """
        return QBrush

    def checkState(self): # real signature unknown; restored from __doc__
        """ checkState(self) -> Qt.CheckState """
        pass

    def child(self, row, column=0): # real signature unknown; restored from __doc__
        """ child(self, row: int, column: int = 0) -> Optional[QStandardItem] """
        pass

    def clearData(self): # real signature unknown; restored from __doc__
        """ clearData(self) """
        pass

    def clone(self): # real signature unknown; restored from __doc__
        """ clone(self) -> Optional[QStandardItem] """
        pass

    def column(self): # real signature unknown; restored from __doc__
        """ column(self) -> int """
        return 0

    def columnCount(self): # real signature unknown; restored from __doc__
        """ columnCount(self) -> int """
        return 0

    def data(self, role=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ data(self, role: int = Qt.UserRole+1) -> Any """
        pass

    def emitDataChanged(self): # real signature unknown; restored from __doc__
        """ emitDataChanged(self) """
        pass

    def flags(self): # real signature unknown; restored from __doc__
        """ flags(self) -> Qt.ItemFlags """
        pass

    def font(self): # real signature unknown; restored from __doc__
        """ font(self) -> QFont """
        return QFont

    def foreground(self): # real signature unknown; restored from __doc__
        """ foreground(self) -> QBrush """
        return QBrush

    def hasChildren(self): # real signature unknown; restored from __doc__
        """ hasChildren(self) -> bool """
        return False

    def icon(self): # real signature unknown; restored from __doc__
        """ icon(self) -> QIcon """
        return QIcon

    def index(self): # real signature unknown; restored from __doc__
        """ index(self) -> QModelIndex """
        pass

    def insertColumn(self, column, items, QStandardItem=None): # real signature unknown; restored from __doc__
        """ insertColumn(self, column: int, items: Iterable[QStandardItem]) """
        pass

    def insertColumns(self, column, count): # real signature unknown; restored from __doc__
        """ insertColumns(self, column: int, count: int) """
        pass

    def insertRow(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        insertRow(self, row: int, items: Iterable[QStandardItem])
        insertRow(self, arow: int, aitem: Optional[QStandardItem])
        """
        pass

    def insertRows(self, row, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        insertRows(self, row: int, count: int)
        insertRows(self, row: int, items: Iterable[QStandardItem])
        """
        pass

    def isAutoTristate(self): # real signature unknown; restored from __doc__
        """ isAutoTristate(self) -> bool """
        return False

    def isCheckable(self): # real signature unknown; restored from __doc__
        """ isCheckable(self) -> bool """
        return False

    def isDragEnabled(self): # real signature unknown; restored from __doc__
        """ isDragEnabled(self) -> bool """
        return False

    def isDropEnabled(self): # real signature unknown; restored from __doc__
        """ isDropEnabled(self) -> bool """
        return False

    def isEditable(self): # real signature unknown; restored from __doc__
        """ isEditable(self) -> bool """
        return False

    def isEnabled(self): # real signature unknown; restored from __doc__
        """ isEnabled(self) -> bool """
        return False

    def isSelectable(self): # real signature unknown; restored from __doc__
        """ isSelectable(self) -> bool """
        return False

    def isTristate(self): # real signature unknown; restored from __doc__
        """ isTristate(self) -> bool """
        return False

    def isUserTristate(self): # real signature unknown; restored from __doc__
        """ isUserTristate(self) -> bool """
        return False

    def model(self): # real signature unknown; restored from __doc__
        """ model(self) -> Optional[QStandardItemModel] """
        pass

    def parent(self): # real signature unknown; restored from __doc__
        """ parent(self) -> Optional[QStandardItem] """
        pass

    def read(self, in_): # real signature unknown; restored from __doc__
        """ read(self, in_: QDataStream) """
        pass

    def removeColumn(self, column): # real signature unknown; restored from __doc__
        """ removeColumn(self, column: int) """
        pass

    def removeColumns(self, column, count): # real signature unknown; restored from __doc__
        """ removeColumns(self, column: int, count: int) """
        pass

    def removeRow(self, row): # real signature unknown; restored from __doc__
        """ removeRow(self, row: int) """
        pass

    def removeRows(self, row, count): # real signature unknown; restored from __doc__
        """ removeRows(self, row: int, count: int) """
        pass

    def row(self): # real signature unknown; restored from __doc__
        """ row(self) -> int """
        return 0

    def rowCount(self): # real signature unknown; restored from __doc__
        """ rowCount(self) -> int """
        return 0

    def setAccessibleDescription(self, aaccessibleDescription, p_str=None): # real signature unknown; restored from __doc__
        """ setAccessibleDescription(self, aaccessibleDescription: Optional[str]) """
        pass

    def setAccessibleText(self, aaccessibleText, p_str=None): # real signature unknown; restored from __doc__
        """ setAccessibleText(self, aaccessibleText: Optional[str]) """
        pass

    def setAutoTristate(self, tristate): # real signature unknown; restored from __doc__
        """ setAutoTristate(self, tristate: bool) """
        pass

    def setBackground(self, abrush, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setBackground(self, abrush: Union[QBrush, Union[QColor, Qt.GlobalColor], QGradient]) """
        pass

    def setCheckable(self, checkable): # real signature unknown; restored from __doc__
        """ setCheckable(self, checkable: bool) """
        pass

    def setCheckState(self, acheckState): # real signature unknown; restored from __doc__
        """ setCheckState(self, acheckState: Qt.CheckState) """
        pass

    def setChild(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setChild(self, row: int, column: int, item: Optional[QStandardItem])
        setChild(self, arow: int, aitem: Optional[QStandardItem])
        """
        pass

    def setColumnCount(self, columns): # real signature unknown; restored from __doc__
        """ setColumnCount(self, columns: int) """
        pass

    def setData(self, value, role=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setData(self, value: Any, role: int = Qt.UserRole+1) """
        pass

    def setDragEnabled(self, dragEnabled): # real signature unknown; restored from __doc__
        """ setDragEnabled(self, dragEnabled: bool) """
        pass

    def setDropEnabled(self, dropEnabled): # real signature unknown; restored from __doc__
        """ setDropEnabled(self, dropEnabled: bool) """
        pass

    def setEditable(self, editable): # real signature unknown; restored from __doc__
        """ setEditable(self, editable: bool) """
        pass

    def setEnabled(self, enabled): # real signature unknown; restored from __doc__
        """ setEnabled(self, enabled: bool) """
        pass

    def setFlags(self, flags, Qt_ItemFlags=None, Qt_ItemFlag=None): # real signature unknown; restored from __doc__
        """ setFlags(self, flags: Union[Qt.ItemFlags, Qt.ItemFlag]) """
        pass

    def setFont(self, afont): # real signature unknown; restored from __doc__
        """ setFont(self, afont: QFont) """
        pass

    def setForeground(self, abrush, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setForeground(self, abrush: Union[QBrush, Union[QColor, Qt.GlobalColor], QGradient]) """
        pass

    def setIcon(self, aicon): # real signature unknown; restored from __doc__
        """ setIcon(self, aicon: QIcon) """
        pass

    def setRowCount(self, rows): # real signature unknown; restored from __doc__
        """ setRowCount(self, rows: int) """
        pass

    def setSelectable(self, selectable): # real signature unknown; restored from __doc__
        """ setSelectable(self, selectable: bool) """
        pass

    def setSizeHint(self, asizeHint): # real signature unknown; restored from __doc__
        """ setSizeHint(self, asizeHint: QSize) """
        pass

    def setStatusTip(self, astatusTip, p_str=None): # real signature unknown; restored from __doc__
        """ setStatusTip(self, astatusTip: Optional[str]) """
        pass

    def setText(self, atext, p_str=None): # real signature unknown; restored from __doc__
        """ setText(self, atext: Optional[str]) """
        pass

    def setTextAlignment(self, atextAlignment, Qt_Alignment=None, Qt_AlignmentFlag=None): # real signature unknown; restored from __doc__
        """ setTextAlignment(self, atextAlignment: Union[Qt.Alignment, Qt.AlignmentFlag]) """
        pass

    def setToolTip(self, atoolTip, p_str=None): # real signature unknown; restored from __doc__
        """ setToolTip(self, atoolTip: Optional[str]) """
        pass

    def setTristate(self, tristate): # real signature unknown; restored from __doc__
        """ setTristate(self, tristate: bool) """
        pass

    def setUserTristate(self, tristate): # real signature unknown; restored from __doc__
        """ setUserTristate(self, tristate: bool) """
        pass

    def setWhatsThis(self, awhatsThis, p_str=None): # real signature unknown; restored from __doc__
        """ setWhatsThis(self, awhatsThis: Optional[str]) """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> QSize """
        pass

    def sortChildren(self, column, order=None): # real signature unknown; restored from __doc__
        """ sortChildren(self, column: int, order: Qt.SortOrder = Qt.AscendingOrder) """
        pass

    def statusTip(self): # real signature unknown; restored from __doc__
        """ statusTip(self) -> str """
        return ""

    def takeChild(self, row, column=0): # real signature unknown; restored from __doc__
        """ takeChild(self, row: int, column: int = 0) -> Optional[QStandardItem] """
        pass

    def takeColumn(self, column): # real signature unknown; restored from __doc__
        """ takeColumn(self, column: int) -> List[QStandardItem] """
        return []

    def takeRow(self, row): # real signature unknown; restored from __doc__
        """ takeRow(self, row: int) -> List[QStandardItem] """
        return []

    def text(self): # real signature unknown; restored from __doc__
        """ text(self) -> str """
        return ""

    def textAlignment(self): # real signature unknown; restored from __doc__
        """ textAlignment(self) -> Qt.Alignment """
        pass

    def toolTip(self): # real signature unknown; restored from __doc__
        """ toolTip(self) -> str """
        return ""

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> int """
        return 0

    def whatsThis(self): # real signature unknown; restored from __doc__
        """ whatsThis(self) -> str """
        return ""

    def write(self, out): # real signature unknown; restored from __doc__
        """ write(self, out: QDataStream) """
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


    Type = 0
    UserType = 1000
    __hash__ = None


