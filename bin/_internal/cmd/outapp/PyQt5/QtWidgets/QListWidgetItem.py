# encoding: utf-8
# module PyQt5.QtWidgets
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


class QListWidgetItem(__sip.wrapper):
    """
    QListWidgetItem(parent: Optional[QListWidget] = None, type: int = QListWidgetItem.Type)
    QListWidgetItem(text: Optional[str], parent: Optional[QListWidget] = None, type: int = QListWidgetItem.Type)
    QListWidgetItem(icon: QIcon, text: Optional[str], parent: Optional[QListWidget] = None, type: int = QListWidgetItem.Type)
    QListWidgetItem(other: QListWidgetItem)
    """
    def background(self): # real signature unknown; restored from __doc__
        """ background(self) -> QBrush """
        pass

    def checkState(self): # real signature unknown; restored from __doc__
        """ checkState(self) -> Qt.CheckState """
        pass

    def clone(self): # real signature unknown; restored from __doc__
        """ clone(self) -> Optional[QListWidgetItem] """
        pass

    def data(self, role): # real signature unknown; restored from __doc__
        """ data(self, role: int) -> Any """
        pass

    def flags(self): # real signature unknown; restored from __doc__
        """ flags(self) -> Qt.ItemFlags """
        pass

    def font(self): # real signature unknown; restored from __doc__
        """ font(self) -> QFont """
        pass

    def foreground(self): # real signature unknown; restored from __doc__
        """ foreground(self) -> QBrush """
        pass

    def icon(self): # real signature unknown; restored from __doc__
        """ icon(self) -> QIcon """
        pass

    def isHidden(self): # real signature unknown; restored from __doc__
        """ isHidden(self) -> bool """
        return False

    def isSelected(self): # real signature unknown; restored from __doc__
        """ isSelected(self) -> bool """
        return False

    def listWidget(self): # real signature unknown; restored from __doc__
        """ listWidget(self) -> Optional[QListWidget] """
        pass

    def read(self, in_): # real signature unknown; restored from __doc__
        """ read(self, in_: QDataStream) """
        pass

    def setBackground(self, brush, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setBackground(self, brush: Union[QBrush, Union[QColor, Qt.GlobalColor], QGradient]) """
        pass

    def setCheckState(self, state): # real signature unknown; restored from __doc__
        """ setCheckState(self, state: Qt.CheckState) """
        pass

    def setData(self, role, value): # real signature unknown; restored from __doc__
        """ setData(self, role: int, value: Any) """
        pass

    def setFlags(self, aflags, Qt_ItemFlags=None, Qt_ItemFlag=None): # real signature unknown; restored from __doc__
        """ setFlags(self, aflags: Union[Qt.ItemFlags, Qt.ItemFlag]) """
        pass

    def setFont(self, afont): # real signature unknown; restored from __doc__
        """ setFont(self, afont: QFont) """
        pass

    def setForeground(self, brush, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setForeground(self, brush: Union[QBrush, Union[QColor, Qt.GlobalColor], QGradient]) """
        pass

    def setHidden(self, ahide): # real signature unknown; restored from __doc__
        """ setHidden(self, ahide: bool) """
        pass

    def setIcon(self, aicon): # real signature unknown; restored from __doc__
        """ setIcon(self, aicon: QIcon) """
        pass

    def setSelected(self, aselect): # real signature unknown; restored from __doc__
        """ setSelected(self, aselect: bool) """
        pass

    def setSizeHint(self, size): # real signature unknown; restored from __doc__
        """ setSizeHint(self, size: QSize) """
        pass

    def setStatusTip(self, astatusTip, p_str=None): # real signature unknown; restored from __doc__
        """ setStatusTip(self, astatusTip: Optional[str]) """
        pass

    def setText(self, atext, p_str=None): # real signature unknown; restored from __doc__
        """ setText(self, atext: Optional[str]) """
        pass

    def setTextAlignment(self, alignment): # real signature unknown; restored from __doc__
        """ setTextAlignment(self, alignment: int) """
        pass

    def setToolTip(self, atoolTip, p_str=None): # real signature unknown; restored from __doc__
        """ setToolTip(self, atoolTip: Optional[str]) """
        pass

    def setWhatsThis(self, awhatsThis, p_str=None): # real signature unknown; restored from __doc__
        """ setWhatsThis(self, awhatsThis: Optional[str]) """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> QSize """
        pass

    def statusTip(self): # real signature unknown; restored from __doc__
        """ statusTip(self) -> str """
        return ""

    def text(self): # real signature unknown; restored from __doc__
        """ text(self) -> str """
        return ""

    def textAlignment(self): # real signature unknown; restored from __doc__
        """ textAlignment(self) -> int """
        return 0

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


