# encoding: utf-8
# module PyQt5.QtWidgets
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


class QAction(__PyQt5_QtCore.QObject):
    """
    QAction(parent: Optional[QObject] = None)
    QAction(text: Optional[str], parent: Optional[QObject] = None)
    QAction(icon: QIcon, text: Optional[str], parent: Optional[QObject] = None)
    """
    def actionGroup(self): # real signature unknown; restored from __doc__
        """ actionGroup(self) -> Optional[QActionGroup] """
        pass

    def activate(self, event): # real signature unknown; restored from __doc__
        """ activate(self, event: QAction.ActionEvent) """
        pass

    def associatedGraphicsWidgets(self): # real signature unknown; restored from __doc__
        """ associatedGraphicsWidgets(self) -> List[QGraphicsWidget] """
        return []

    def associatedWidgets(self): # real signature unknown; restored from __doc__
        """ associatedWidgets(self) -> List[QWidget] """
        return []

    def autoRepeat(self): # real signature unknown; restored from __doc__
        """ autoRepeat(self) -> bool """
        return False

    def changed(self, *args, **kwargs): # real signature unknown
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

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def data(self): # real signature unknown; restored from __doc__
        """ data(self) -> Any """
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, a0, QEvent=None): # real signature unknown; restored from __doc__
        """ event(self, a0: Optional[QEvent]) -> bool """
        return False

    def font(self): # real signature unknown; restored from __doc__
        """ font(self) -> QFont """
        pass

    def hover(self): # real signature unknown; restored from __doc__
        """ hover(self) """
        pass

    def hovered(self, *args, **kwargs): # real signature unknown
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

    def icon(self): # real signature unknown; restored from __doc__
        """ icon(self) -> QIcon """
        pass

    def iconText(self): # real signature unknown; restored from __doc__
        """ iconText(self) -> str """
        return ""

    def isCheckable(self): # real signature unknown; restored from __doc__
        """ isCheckable(self) -> bool """
        return False

    def isChecked(self): # real signature unknown; restored from __doc__
        """ isChecked(self) -> bool """
        return False

    def isEnabled(self): # real signature unknown; restored from __doc__
        """ isEnabled(self) -> bool """
        return False

    def isIconVisibleInMenu(self): # real signature unknown; restored from __doc__
        """ isIconVisibleInMenu(self) -> bool """
        return False

    def isSeparator(self): # real signature unknown; restored from __doc__
        """ isSeparator(self) -> bool """
        return False

    def isShortcutVisibleInContextMenu(self): # real signature unknown; restored from __doc__
        """ isShortcutVisibleInContextMenu(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def isVisible(self): # real signature unknown; restored from __doc__
        """ isVisible(self) -> bool """
        return False

    def menu(self): # real signature unknown; restored from __doc__
        """ menu(self) -> Optional[QMenu] """
        pass

    def menuRole(self): # real signature unknown; restored from __doc__
        """ menuRole(self) -> QAction.MenuRole """
        pass

    def parentWidget(self): # real signature unknown; restored from __doc__
        """ parentWidget(self) -> Optional[QWidget] """
        pass

    def priority(self): # real signature unknown; restored from __doc__
        """ priority(self) -> QAction.Priority """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setActionGroup(self, group, QActionGroup=None): # real signature unknown; restored from __doc__
        """ setActionGroup(self, group: Optional[QActionGroup]) """
        pass

    def setAutoRepeat(self, a0): # real signature unknown; restored from __doc__
        """ setAutoRepeat(self, a0: bool) """
        pass

    def setCheckable(self, a0): # real signature unknown; restored from __doc__
        """ setCheckable(self, a0: bool) """
        pass

    def setChecked(self, a0): # real signature unknown; restored from __doc__
        """ setChecked(self, a0: bool) """
        pass

    def setData(self, var): # real signature unknown; restored from __doc__
        """ setData(self, var: Any) """
        pass

    def setDisabled(self, b): # real signature unknown; restored from __doc__
        """ setDisabled(self, b: bool) """
        pass

    def setEnabled(self, a0): # real signature unknown; restored from __doc__
        """ setEnabled(self, a0: bool) """
        pass

    def setFont(self, font): # real signature unknown; restored from __doc__
        """ setFont(self, font: QFont) """
        pass

    def setIcon(self, icon): # real signature unknown; restored from __doc__
        """ setIcon(self, icon: QIcon) """
        pass

    def setIconText(self, text, p_str=None): # real signature unknown; restored from __doc__
        """ setIconText(self, text: Optional[str]) """
        pass

    def setIconVisibleInMenu(self, visible): # real signature unknown; restored from __doc__
        """ setIconVisibleInMenu(self, visible: bool) """
        pass

    def setMenu(self, menu, QMenu=None): # real signature unknown; restored from __doc__
        """ setMenu(self, menu: Optional[QMenu]) """
        pass

    def setMenuRole(self, menuRole): # real signature unknown; restored from __doc__
        """ setMenuRole(self, menuRole: QAction.MenuRole) """
        pass

    def setPriority(self, priority): # real signature unknown; restored from __doc__
        """ setPriority(self, priority: QAction.Priority) """
        pass

    def setSeparator(self, b): # real signature unknown; restored from __doc__
        """ setSeparator(self, b: bool) """
        pass

    def setShortcut(self, shortcut, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setShortcut(self, shortcut: Union[QKeySequence, QKeySequence.StandardKey, Optional[str], int]) """
        pass

    def setShortcutContext(self, context): # real signature unknown; restored from __doc__
        """ setShortcutContext(self, context: Qt.ShortcutContext) """
        pass

    def setShortcuts(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setShortcuts(self, shortcuts: Iterable[Union[QKeySequence, QKeySequence.StandardKey, Optional[str], int]])
        setShortcuts(self, a0: QKeySequence.StandardKey)
        """
        pass

    def setShortcutVisibleInContextMenu(self, show): # real signature unknown; restored from __doc__
        """ setShortcutVisibleInContextMenu(self, show: bool) """
        pass

    def setStatusTip(self, statusTip, p_str=None): # real signature unknown; restored from __doc__
        """ setStatusTip(self, statusTip: Optional[str]) """
        pass

    def setText(self, text, p_str=None): # real signature unknown; restored from __doc__
        """ setText(self, text: Optional[str]) """
        pass

    def setToolTip(self, tip, p_str=None): # real signature unknown; restored from __doc__
        """ setToolTip(self, tip: Optional[str]) """
        pass

    def setVisible(self, a0): # real signature unknown; restored from __doc__
        """ setVisible(self, a0: bool) """
        pass

    def setWhatsThis(self, what, p_str=None): # real signature unknown; restored from __doc__
        """ setWhatsThis(self, what: Optional[str]) """
        pass

    def shortcut(self): # real signature unknown; restored from __doc__
        """ shortcut(self) -> QKeySequence """
        pass

    def shortcutContext(self): # real signature unknown; restored from __doc__
        """ shortcutContext(self) -> Qt.ShortcutContext """
        pass

    def shortcuts(self): # real signature unknown; restored from __doc__
        """ shortcuts(self) -> List[QKeySequence] """
        return []

    def showStatusText(self, widget, QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ showStatusText(self, widget: Optional[QWidget] = None) -> bool """
        pass

    def statusTip(self): # real signature unknown; restored from __doc__
        """ statusTip(self) -> str """
        return ""

    def text(self): # real signature unknown; restored from __doc__
        """ text(self) -> str """
        return ""

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def toggle(self): # real signature unknown; restored from __doc__
        """ toggle(self) """
        pass

    def toggled(self, *args, **kwargs): # real signature unknown
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

    def toolTip(self): # real signature unknown; restored from __doc__
        """ toolTip(self) -> str """
        return ""

    def trigger(self): # real signature unknown; restored from __doc__
        """ trigger(self) """
        pass

    def triggered(self, *args, **kwargs): # real signature unknown
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

    def whatsThis(self): # real signature unknown; restored from __doc__
        """ whatsThis(self) -> str """
        return ""

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    AboutQtRole = 3
    AboutRole = 4
    ApplicationSpecificRole = 2
    HighPriority = 256
    Hover = 1
    LowPriority = 0
    NormalPriority = 128
    NoRole = 0
    PreferencesRole = 5
    QuitRole = 6
    TextHeuristicRole = 1
    Trigger = 0


