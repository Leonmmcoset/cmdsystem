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

class QTabWidget(QWidget):
    """ QTabWidget(parent: Optional[QWidget] = None) """
    def actionEvent(self, *args, **kwargs): # real signature unknown
        pass

    def addTab(self, widget, QWidget=None, *args, **kwargs): # real signature unknown; restored from __doc__ with multiple overloads
        """
        addTab(self, widget: Optional[QWidget], a1: Optional[str]) -> int
        addTab(self, widget: Optional[QWidget], icon: QIcon, label: Optional[str]) -> int
        """
        pass

    def changeEvent(self, a0, QEvent=None): # real signature unknown; restored from __doc__
        """ changeEvent(self, a0: Optional[QEvent]) """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def closeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def contextMenuEvent(self, *args, **kwargs): # real signature unknown
        pass

    def cornerWidget(self, corner=None): # real signature unknown; restored from __doc__
        """ cornerWidget(self, corner: Qt.Corner = Qt.TopRightCorner) -> Optional[QWidget] """
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

    def currentWidget(self): # real signature unknown; restored from __doc__
        """ currentWidget(self) -> Optional[QWidget] """
        pass

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

    def hasHeightForWidth(self): # real signature unknown; restored from __doc__
        """ hasHeightForWidth(self) -> bool """
        return False

    def heightForWidth(self, width): # real signature unknown; restored from __doc__
        """ heightForWidth(self, width: int) -> int """
        return 0

    def hideEvent(self, *args, **kwargs): # real signature unknown
        pass

    def iconSize(self): # real signature unknown; restored from __doc__
        """ iconSize(self) -> QSize """
        pass

    def indexOf(self, widget, QWidget=None): # real signature unknown; restored from __doc__
        """ indexOf(self, widget: Optional[QWidget]) -> int """
        return 0

    def initPainter(self, *args, **kwargs): # real signature unknown
        pass

    def initStyleOption(self, option, QStyleOptionTabWidgetFrame=None): # real signature unknown; restored from __doc__
        """ initStyleOption(self, option: Optional[QStyleOptionTabWidgetFrame]) """
        pass

    def inputMethodEvent(self, *args, **kwargs): # real signature unknown
        pass

    def insertTab(self, index, widget, QWidget=None, *args, **kwargs): # real signature unknown; restored from __doc__ with multiple overloads
        """
        insertTab(self, index: int, widget: Optional[QWidget], a2: Optional[str]) -> int
        insertTab(self, index: int, widget: Optional[QWidget], icon: QIcon, label: Optional[str]) -> int
        """
        pass

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

    def mouseDoubleClickEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mouseMoveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mousePressEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mouseReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def moveEvent(self, *args, **kwargs): # real signature unknown
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

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setCornerWidget(self, widget, QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setCornerWidget(self, widget: Optional[QWidget], corner: Qt.Corner = Qt.TopRightCorner) """
        pass

    def setCurrentIndex(self, index): # real signature unknown; restored from __doc__
        """ setCurrentIndex(self, index: int) """
        pass

    def setCurrentWidget(self, widget, QWidget=None): # real signature unknown; restored from __doc__
        """ setCurrentWidget(self, widget: Optional[QWidget]) """
        pass

    def setDocumentMode(self, set): # real signature unknown; restored from __doc__
        """ setDocumentMode(self, set: bool) """
        pass

    def setElideMode(self, a0): # real signature unknown; restored from __doc__
        """ setElideMode(self, a0: Qt.TextElideMode) """
        pass

    def setIconSize(self, size): # real signature unknown; restored from __doc__
        """ setIconSize(self, size: QSize) """
        pass

    def setMovable(self, movable): # real signature unknown; restored from __doc__
        """ setMovable(self, movable: bool) """
        pass

    def setTabBar(self, a0, QTabBar=None): # real signature unknown; restored from __doc__
        """ setTabBar(self, a0: Optional[QTabBar]) """
        pass

    def setTabBarAutoHide(self, enabled): # real signature unknown; restored from __doc__
        """ setTabBarAutoHide(self, enabled: bool) """
        pass

    def setTabEnabled(self, index, a1): # real signature unknown; restored from __doc__
        """ setTabEnabled(self, index: int, a1: bool) """
        pass

    def setTabIcon(self, index, icon): # real signature unknown; restored from __doc__
        """ setTabIcon(self, index: int, icon: QIcon) """
        pass

    def setTabPosition(self, a0): # real signature unknown; restored from __doc__
        """ setTabPosition(self, a0: QTabWidget.TabPosition) """
        pass

    def setTabsClosable(self, closeable): # real signature unknown; restored from __doc__
        """ setTabsClosable(self, closeable: bool) """
        pass

    def setTabShape(self, s): # real signature unknown; restored from __doc__
        """ setTabShape(self, s: QTabWidget.TabShape) """
        pass

    def setTabText(self, index, a1, p_str=None): # real signature unknown; restored from __doc__
        """ setTabText(self, index: int, a1: Optional[str]) """
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

    def sharedPainter(self, *args, **kwargs): # real signature unknown
        pass

    def showEvent(self, a0, QShowEvent=None): # real signature unknown; restored from __doc__
        """ showEvent(self, a0: Optional[QShowEvent]) """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> QSize """
        pass

    def tabBar(self): # real signature unknown; restored from __doc__
        """ tabBar(self) -> Optional[QTabBar] """
        pass

    def tabBarAutoHide(self): # real signature unknown; restored from __doc__
        """ tabBarAutoHide(self) -> bool """
        return False

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

    def tabIcon(self, index): # real signature unknown; restored from __doc__
        """ tabIcon(self, index: int) -> QIcon """
        pass

    def tabInserted(self, index): # real signature unknown; restored from __doc__
        """ tabInserted(self, index: int) """
        pass

    def tabletEvent(self, *args, **kwargs): # real signature unknown
        pass

    def tabPosition(self): # real signature unknown; restored from __doc__
        """ tabPosition(self) -> QTabWidget.TabPosition """
        pass

    def tabRemoved(self, index): # real signature unknown; restored from __doc__
        """ tabRemoved(self, index: int) """
        pass

    def tabsClosable(self): # real signature unknown; restored from __doc__
        """ tabsClosable(self) -> bool """
        return False

    def tabShape(self): # real signature unknown; restored from __doc__
        """ tabShape(self) -> QTabWidget.TabShape """
        pass

    def tabText(self, index): # real signature unknown; restored from __doc__
        """ tabText(self, index: int) -> str """
        return ""

    def tabToolTip(self, index): # real signature unknown; restored from __doc__
        """ tabToolTip(self, index: int) -> str """
        return ""

    def tabWhatsThis(self, index): # real signature unknown; restored from __doc__
        """ tabWhatsThis(self, index: int) -> str """
        return ""

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

    def usesScrollButtons(self): # real signature unknown; restored from __doc__
        """ usesScrollButtons(self) -> bool """
        return False

    def wheelEvent(self, *args, **kwargs): # real signature unknown
        pass

    def widget(self, index): # real signature unknown; restored from __doc__
        """ widget(self, index: int) -> Optional[QWidget] """
        pass

    def __init__(self, parent, QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    East = 3
    North = 0
    Rounded = 0
    South = 1
    Triangular = 1
    West = 2


