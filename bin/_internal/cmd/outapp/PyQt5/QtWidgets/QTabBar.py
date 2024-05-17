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

class QTabBar(QWidget):
    """ QTabBar(parent: Optional[QWidget] = None) """
    def accessibleTabName(self, index): # real signature unknown; restored from __doc__
        """ accessibleTabName(self, index: int) -> str """
        return ""

    def actionEvent(self, *args, **kwargs): # real signature unknown
        pass

    def addTab(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        addTab(self, text: Optional[str]) -> int
        addTab(self, icon: QIcon, text: Optional[str]) -> int
        """
        return 0

    def autoHide(self): # real signature unknown; restored from __doc__
        """ autoHide(self) -> bool """
        return False

    def changeCurrentOnDrag(self): # real signature unknown; restored from __doc__
        """ changeCurrentOnDrag(self) -> bool """
        return False

    def changeEvent(self, a0, QEvent=None): # real signature unknown; restored from __doc__
        """ changeEvent(self, a0: Optional[QEvent]) """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def closeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def contextMenuEvent(self, *args, **kwargs): # real signature unknown
        pass

    def count(self): # real signature unknown; restored from __doc__
        """ count(self) -> int """
        return 0

    def create(self, *args, **kwargs): # real signature unknown
        pass

    def currentChanged(self, *args, **kwargs): # real signature unknown
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

    def currentIndex(self): # real signature unknown; restored from __doc__
        """ currentIndex(self) -> int """
        return 0

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def destroy(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def documentMode(self): # real signature unknown; restored from __doc__
        """ documentMode(self) -> bool """
        return False

    def dragEnterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dragLeaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dragMoveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def drawBase(self): # real signature unknown; restored from __doc__
        """ drawBase(self) -> bool """
        return False

    def dropEvent(self, *args, **kwargs): # real signature unknown
        pass

    def elideMode(self): # real signature unknown; restored from __doc__
        """ elideMode(self) -> Qt.TextElideMode """
        pass

    def enterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, a0, QEvent=None): # real signature unknown; restored from __doc__
        """ event(self, a0: Optional[QEvent]) -> bool """
        return False

    def expanding(self): # real signature unknown; restored from __doc__
        """ expanding(self) -> bool """
        return False

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

    def hideEvent(self, a0, QHideEvent=None): # real signature unknown; restored from __doc__
        """ hideEvent(self, a0: Optional[QHideEvent]) """
        pass

    def iconSize(self): # real signature unknown; restored from __doc__
        """ iconSize(self) -> QSize """
        pass

    def initPainter(self, *args, **kwargs): # real signature unknown
        pass

    def initStyleOption(self, option, QStyleOptionTab=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ initStyleOption(self, option: Optional[QStyleOptionTab], tabIndex: int) """
        pass

    def inputMethodEvent(self, *args, **kwargs): # real signature unknown
        pass

    def insertTab(self, index, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        insertTab(self, index: int, text: Optional[str]) -> int
        insertTab(self, index: int, icon: QIcon, text: Optional[str]) -> int
        """
        return 0

    def isMovable(self): # real signature unknown; restored from __doc__
        """ isMovable(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def isTabEnabled(self, index): # real signature unknown; restored from __doc__
        """ isTabEnabled(self, index: int) -> bool """
        return False

    def isTabVisible(self, index): # real signature unknown; restored from __doc__
        """ isTabVisible(self, index: int) -> bool """
        return False

    def keyPressEvent(self, a0, QKeyEvent=None): # real signature unknown; restored from __doc__
        """ keyPressEvent(self, a0: Optional[QKeyEvent]) """
        pass

    def keyReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def leaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def metric(self, *args, **kwargs): # real signature unknown
        pass

    def minimumSizeHint(self): # real signature unknown; restored from __doc__
        """ minimumSizeHint(self) -> QSize """
        pass

    def minimumTabSizeHint(self, index): # real signature unknown; restored from __doc__
        """ minimumTabSizeHint(self, index: int) -> QSize """
        pass

    def mouseDoubleClickEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mouseMoveEvent(self, a0, QMouseEvent=None): # real signature unknown; restored from __doc__
        """ mouseMoveEvent(self, a0: Optional[QMouseEvent]) """
        pass

    def mousePressEvent(self, a0, QMouseEvent=None): # real signature unknown; restored from __doc__
        """ mousePressEvent(self, a0: Optional[QMouseEvent]) """
        pass

    def mouseReleaseEvent(self, a0, QMouseEvent=None): # real signature unknown; restored from __doc__
        """ mouseReleaseEvent(self, a0: Optional[QMouseEvent]) """
        pass

    def moveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def moveTab(self, from_, to): # real signature unknown; restored from __doc__
        """ moveTab(self, from_: int, to: int) """
        pass

    def nativeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def paintEvent(self, a0, QPaintEvent=None): # real signature unknown; restored from __doc__
        """ paintEvent(self, a0: Optional[QPaintEvent]) """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def removeTab(self, index): # real signature unknown; restored from __doc__
        """ removeTab(self, index: int) """
        pass

    def resizeEvent(self, a0, QResizeEvent=None): # real signature unknown; restored from __doc__
        """ resizeEvent(self, a0: Optional[QResizeEvent]) """
        pass

    def selectionBehaviorOnRemove(self): # real signature unknown; restored from __doc__
        """ selectionBehaviorOnRemove(self) -> QTabBar.SelectionBehavior """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setAccessibleTabName(self, index, name, p_str=None): # real signature unknown; restored from __doc__
        """ setAccessibleTabName(self, index: int, name: Optional[str]) """
        pass

    def setAutoHide(self, hide): # real signature unknown; restored from __doc__
        """ setAutoHide(self, hide: bool) """
        pass

    def setChangeCurrentOnDrag(self, change): # real signature unknown; restored from __doc__
        """ setChangeCurrentOnDrag(self, change: bool) """
        pass

    def setCurrentIndex(self, index): # real signature unknown; restored from __doc__
        """ setCurrentIndex(self, index: int) """
        pass

    def setDocumentMode(self, set): # real signature unknown; restored from __doc__
        """ setDocumentMode(self, set: bool) """
        pass

    def setDrawBase(self, drawTheBase): # real signature unknown; restored from __doc__
        """ setDrawBase(self, drawTheBase: bool) """
        pass

    def setElideMode(self, a0): # real signature unknown; restored from __doc__
        """ setElideMode(self, a0: Qt.TextElideMode) """
        pass

    def setExpanding(self, enabled): # real signature unknown; restored from __doc__
        """ setExpanding(self, enabled: bool) """
        pass

    def setIconSize(self, size): # real signature unknown; restored from __doc__
        """ setIconSize(self, size: QSize) """
        pass

    def setMovable(self, movable): # real signature unknown; restored from __doc__
        """ setMovable(self, movable: bool) """
        pass

    def setSelectionBehaviorOnRemove(self, behavior): # real signature unknown; restored from __doc__
        """ setSelectionBehaviorOnRemove(self, behavior: QTabBar.SelectionBehavior) """
        pass

    def setShape(self, shape): # real signature unknown; restored from __doc__
        """ setShape(self, shape: QTabBar.Shape) """
        pass

    def setTabButton(self, index, position, widget, QWidget=None): # real signature unknown; restored from __doc__
        """ setTabButton(self, index: int, position: QTabBar.ButtonPosition, widget: Optional[QWidget]) """
        pass

    def setTabData(self, index, data): # real signature unknown; restored from __doc__
        """ setTabData(self, index: int, data: Any) """
        pass

    def setTabEnabled(self, index, a1): # real signature unknown; restored from __doc__
        """ setTabEnabled(self, index: int, a1: bool) """
        pass

    def setTabIcon(self, index, icon): # real signature unknown; restored from __doc__
        """ setTabIcon(self, index: int, icon: QIcon) """
        pass

    def setTabsClosable(self, closable): # real signature unknown; restored from __doc__
        """ setTabsClosable(self, closable: bool) """
        pass

    def setTabText(self, index, text, p_str=None): # real signature unknown; restored from __doc__
        """ setTabText(self, index: int, text: Optional[str]) """
        pass

    def setTabTextColor(self, index, color, QColor=None, Qt_GlobalColor=None): # real signature unknown; restored from __doc__
        """ setTabTextColor(self, index: int, color: Union[QColor, Qt.GlobalColor]) """
        pass

    def setTabToolTip(self, index, tip, p_str=None): # real signature unknown; restored from __doc__
        """ setTabToolTip(self, index: int, tip: Optional[str]) """
        pass

    def setTabVisible(self, index, visible): # real signature unknown; restored from __doc__
        """ setTabVisible(self, index: int, visible: bool) """
        pass

    def setTabWhatsThis(self, index, text, p_str=None): # real signature unknown; restored from __doc__
        """ setTabWhatsThis(self, index: int, text: Optional[str]) """
        pass

    def setUsesScrollButtons(self, useButtons): # real signature unknown; restored from __doc__
        """ setUsesScrollButtons(self, useButtons: bool) """
        pass

    def shape(self): # real signature unknown; restored from __doc__
        """ shape(self) -> QTabBar.Shape """
        pass

    def sharedPainter(self, *args, **kwargs): # real signature unknown
        pass

    def showEvent(self, a0, QShowEvent=None): # real signature unknown; restored from __doc__
        """ showEvent(self, a0: Optional[QShowEvent]) """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> QSize """
        pass

    def tabAt(self, pos): # real signature unknown; restored from __doc__
        """ tabAt(self, pos: QPoint) -> int """
        return 0

    def tabBarClicked(self, *args, **kwargs): # real signature unknown
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

    def tabBarDoubleClicked(self, *args, **kwargs): # real signature unknown
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

    def tabButton(self, index, position): # real signature unknown; restored from __doc__
        """ tabButton(self, index: int, position: QTabBar.ButtonPosition) -> Optional[QWidget] """
        pass

    def tabCloseRequested(self, *args, **kwargs): # real signature unknown
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

    def tabData(self, index): # real signature unknown; restored from __doc__
        """ tabData(self, index: int) -> Any """
        pass

    def tabIcon(self, index): # real signature unknown; restored from __doc__
        """ tabIcon(self, index: int) -> QIcon """
        pass

    def tabInserted(self, index): # real signature unknown; restored from __doc__
        """ tabInserted(self, index: int) """
        pass

    def tabLayoutChange(self): # real signature unknown; restored from __doc__
        """ tabLayoutChange(self) """
        pass

    def tabletEvent(self, *args, **kwargs): # real signature unknown
        pass

    def tabMoved(self, *args, **kwargs): # real signature unknown
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

    def tabRect(self, index): # real signature unknown; restored from __doc__
        """ tabRect(self, index: int) -> QRect """
        pass

    def tabRemoved(self, index): # real signature unknown; restored from __doc__
        """ tabRemoved(self, index: int) """
        pass

    def tabsClosable(self): # real signature unknown; restored from __doc__
        """ tabsClosable(self) -> bool """
        return False

    def tabSizeHint(self, index): # real signature unknown; restored from __doc__
        """ tabSizeHint(self, index: int) -> QSize """
        pass

    def tabText(self, index): # real signature unknown; restored from __doc__
        """ tabText(self, index: int) -> str """
        return ""

    def tabTextColor(self, index): # real signature unknown; restored from __doc__
        """ tabTextColor(self, index: int) -> QColor """
        pass

    def tabToolTip(self, index): # real signature unknown; restored from __doc__
        """ tabToolTip(self, index: int) -> str """
        return ""

    def tabWhatsThis(self, index): # real signature unknown; restored from __doc__
        """ tabWhatsThis(self, index: int) -> str """
        return ""

    def timerEvent(self, event, QTimerEvent=None): # real signature unknown; restored from __doc__
        """ timerEvent(self, event: Optional[QTimerEvent]) """
        pass

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

    def usesScrollButtons(self): # real signature unknown; restored from __doc__
        """ usesScrollButtons(self) -> bool """
        return False

    def wheelEvent(self, event, QWheelEvent=None): # real signature unknown; restored from __doc__
        """ wheelEvent(self, event: Optional[QWheelEvent]) """
        pass

    def __init__(self, parent, QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    LeftSide = 0
    RightSide = 1
    RoundedEast = 3
    RoundedNorth = 0
    RoundedSouth = 1
    RoundedWest = 2
    SelectLeftTab = 0
    SelectPreviousTab = 2
    SelectRightTab = 1
    TriangularEast = 7
    TriangularNorth = 4
    TriangularSouth = 5
    TriangularWest = 6


