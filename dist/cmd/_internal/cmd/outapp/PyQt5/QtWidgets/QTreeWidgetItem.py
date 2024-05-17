# encoding: utf-8
# module PyQt5.QtWidgets
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


class QTreeWidgetItem(__sip.wrapper):
    """
    QTreeWidgetItem(type: int = QTreeWidgetItem.Type)
    QTreeWidgetItem(strings: Iterable[Optional[str]], type: int = QTreeWidgetItem.Type)
    QTreeWidgetItem(parent: Optional[QTreeWidget], type: int = QTreeWidgetItem.Type)
    QTreeWidgetItem(parent: Optional[QTreeWidget], strings: Iterable[Optional[str]], type: int = QTreeWidgetItem.Type)
    QTreeWidgetItem(parent: Optional[QTreeWidget], preceding: Optional[QTreeWidgetItem], type: int = QTreeWidgetItem.Type)
    QTreeWidgetItem(parent: Optional[QTreeWidgetItem], type: int = QTreeWidgetItem.Type)
    QTreeWidgetItem(parent: Optional[QTreeWidgetItem], strings: Iterable[Optional[str]], type: int = QTreeWidgetItem.Type)
    QTreeWidgetItem(parent: Optional[QTreeWidgetItem], preceding: Optional[QTreeWidgetItem], type: int = QTreeWidgetItem.Type)
    QTreeWidgetItem(other: QTreeWidgetItem)
    """
    def addChild(self, child, QTreeWidgetItem=None): # real signature unknown; restored from __doc__
        """ addChild(self, child: Optional[QTreeWidgetItem]) """
        pass

    def addChildren(self, children, QTreeWidgetItem=None): # real signature unknown; restored from __doc__
        """ addChildren(self, children: Iterable[QTreeWidgetItem]) """
        pass

    def background(self, column): # real signature unknown; restored from __doc__
        """ background(self, column: int) -> QBrush """
        pass

    def checkState(self, column): # real signature unknown; restored from __doc__
        """ checkState(self, column: int) -> Qt.CheckState """
        pass

    def child(self, index): # real signature unknown; restored from __doc__
        """ child(self, index: int) -> Optional[QTreeWidgetItem] """
        pass

    def childCount(self): # real signature unknown; restored from __doc__
        """ childCount(self) -> int """
        return 0

    def childIndicatorPolicy(self): # real signature unknown; restored from __doc__
        """ childIndicatorPolicy(self) -> QTreeWidgetItem.ChildIndicatorPolicy """
        pass

    def clone(self): # real signature unknown; restored from __doc__
        """ clone(self) -> Optional[QTreeWidgetItem] """
        pass

    def columnCount(self): # real signature unknown; restored from __doc__
        """ columnCount(self) -> int """
        return 0

    def data(self, column, role): # real signature unknown; restored from __doc__
        """ data(self, column: int, role: int) -> Any """
        pass

    def emitDataChanged(self): # real signature unknown; restored from __doc__
        """ emitDataChanged(self) """
        pass

    def flags(self): # real signature unknown; restored from __doc__
        """ flags(self) -> Qt.ItemFlags """
        pass

    def font(self, column): # real signature unknown; restored from __doc__
        """ font(self, column: int) -> QFont """
        pass

    def foreground(self, column): # real signature unknown; restored from __doc__
        """ foreground(self, column: int) -> QBrush """
        pass

    def icon(self, column): # real signature unknown; restored from __doc__
        """ icon(self, column: int) -> QIcon """
        pass

    def indexOfChild(self, achild, QTreeWidgetItem=None): # real signature unknown; restored from __doc__
        """ indexOfChild(self, achild: Optional[QTreeWidgetItem]) -> int """
        return 0

    def insertChild(self, index, child, QTreeWidgetItem=None): # real signature unknown; restored from __doc__
        """ insertChild(self, index: int, child: Optional[QTreeWidgetItem]) """
        pass

    def insertChildren(self, index, children, QTreeWidgetItem=None): # real signature unknown; restored from __doc__
        """ insertChildren(self, index: int, children: Iterable[QTreeWidgetItem]) """
        pass

    def isDisabled(self): # real signature unknown; restored from __doc__
        """ isDisabled(self) -> bool """
        return False

    def isExpanded(self): # real signature unknown; restored from __doc__
        """ isExpanded(self) -> bool """
        return False

    def isFirstColumnSpanned(self): # real signature unknown; restored from __doc__
        """ isFirstColumnSpanned(self) -> bool """
        return False

    def isHidden(self): # real signature unknown; restored from __doc__
        """ isHidden(self) -> bool """
        return False

    def isSelected(self): # real signature unknown; restored from __doc__
        """ isSelected(self) -> bool """
        return False

    def parent(self): # real signature unknown; restored from __doc__
        """ parent(self) -> Optional[QTreeWidgetItem] """
        pass

    def read(self, in_): # real signature unknown; restored from __doc__
        """ read(self, in_: QDataStream) """
        pass

    def removeChild(self, child, QTreeWidgetItem=None): # real signature unknown; restored from __doc__
        """ removeChild(self, child: Optional[QTreeWidgetItem]) """
        pass

    def setBackground(self, column, brush, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setBackground(self, column: int, brush: Union[QBrush, Union[QColor, Qt.GlobalColor], QGradient]) """
        pass

    def setCheckState(self, column, state): # real signature unknown; restored from __doc__
        """ setCheckState(self, column: int, state: Qt.CheckState) """
        pass

    def setChildIndicatorPolicy(self, policy): # real signature unknown; restored from __doc__
        """ setChildIndicatorPolicy(self, policy: QTreeWidgetItem.ChildIndicatorPolicy) """
        pass

    def setData(self, column, role, value): # real signature unknown; restored from __doc__
        """ setData(self, column: int, role: int, value: Any) """
        pass

    def setDisabled(self, disabled): # real signature unknown; restored from __doc__
        """ setDisabled(self, disabled: bool) """
        pass

    def setExpanded(self, aexpand): # real signature unknown; restored from __doc__
        """ setExpanded(self, aexpand: bool) """
        pass

    def setFirstColumnSpanned(self, aspan): # real signature unknown; restored from __doc__
        """ setFirstColumnSpanned(self, aspan: bool) """
        pass

    def setFlags(self, aflags, Qt_ItemFlags=None, Qt_ItemFlag=None): # real signature unknown; restored from __doc__
        """ setFlags(self, aflags: Union[Qt.ItemFlags, Qt.ItemFlag]) """
        pass

    def setFont(self, column, afont): # real signature unknown; restored from __doc__
        """ setFont(self, column: int, afont: QFont) """
        pass

    def setForeground(self, column, brush, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setForeground(self, column: int, brush: Union[QBrush, Union[QColor, Qt.GlobalColor], QGradient]) """
        pass

    def setHidden(self, ahide): # real signature unknown; restored from __doc__
        """ setHidden(self, ahide: bool) """
        pass

    def setIcon(self, column, aicon): # real signature unknown; restored from __doc__
        """ setIcon(self, column: int, aicon: QIcon) """
        pass

    def setSelected(self, aselect): # real signature unknown; restored from __doc__
        """ setSelected(self, aselect: bool) """
        pass

    def setSizeHint(self, column, size): # real signature unknown; restored from __doc__
        """ setSizeHint(self, column: int, size: QSize) """
        pass

    def setStatusTip(self, column, astatusTip, p_str=None): # real signature unknown; restored from __doc__
        """ setStatusTip(self, column: int, astatusTip: Optional[str]) """
        pass

    def setText(self, column, atext, p_str=None): # real signature unknown; restored from __doc__
        """ setText(self, column: int, atext: Optional[str]) """
        pass

    def setTextAlignment(self, column, alignment): # real signature unknown; restored from __doc__
        """ setTextAlignment(self, column: int, alignment: int) """
        pass

    def setToolTip(self, column, atoolTip, p_str=None): # real signature unknown; restored from __doc__
        """ setToolTip(self, column: int, atoolTip: Optional[str]) """
        pass

    def setWhatsThis(self, column, awhatsThis, p_str=None): # real signature unknown; restored from __doc__
        """ setWhatsThis(self, column: int, awhatsThis: Optional[str]) """
        pass

    def sizeHint(self, column): # real signature unknown; restored from __doc__
        """ sizeHint(self, column: int) -> QSize """
        pass

    def sortChildren(self, column, order): # real signature unknown; restored from __doc__
        """ sortChildren(self, column: int, order: Qt.SortOrder) """
        pass

    def statusTip(self, column): # real signature unknown; restored from __doc__
        """ statusTip(self, column: int) -> str """
        return ""

    def takeChild(self, index): # real signature unknown; restored from __doc__
        """ takeChild(self, index: int) -> Optional[QTreeWidgetItem] """
        pass

    def takeChildren(self): # real signature unknown; restored from __doc__
        """ takeChildren(self) -> List[QTreeWidgetItem] """
        return []

    def text(self, column): # real signature unknown; restored from __doc__
        """ text(self, column: int) -> str """
        return ""

    def textAlignment(self, column): # real signature unknown; restored from __doc__
        """ textAlignment(self, column: int) -> int """
        return 0

    def toolTip(self, column): # real signature unknown; restored from __doc__
        """ toolTip(self, column: int) -> str """
        return ""

    def treeWidget(self): # real signature unknown; restored from __doc__
        """ treeWidget(self) -> Optional[QTreeWidget] """
        pass

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> int """
        return 0

    def whatsThis(self, column): # real signature unknown; restored from __doc__
        """ whatsThis(self, column: int) -> str """
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


    DontShowIndicator = 1
    DontShowIndicatorWhenChildless = 2
    ShowIndicator = 0
    Type = 0
    UserType = 1000
    __hash__ = None


