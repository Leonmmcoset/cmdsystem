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

class QMenu(QWidget):
    """
    QMenu(parent: Optional[QWidget] = None)
    QMenu(title: Optional[str], parent: Optional[QWidget] = None)
    """
    def aboutToHide(self, *args, **kwargs): # real signature unknown
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

    def aboutToShow(self, *args, **kwargs): # real signature unknown
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

    def actionAt(self, a0): # real signature unknown; restored from __doc__
        """ actionAt(self, a0: QPoint) -> Optional[QAction] """
        pass

    def actionEvent(self, a0, QActionEvent=None): # real signature unknown; restored from __doc__
        """ actionEvent(self, a0: Optional[QActionEvent]) """
        pass

    def actionGeometry(self, a0, QAction=None): # real signature unknown; restored from __doc__
        """ actionGeometry(self, a0: Optional[QAction]) -> QRect """
        pass

    def activeAction(self): # real signature unknown; restored from __doc__
        """ activeAction(self) -> Optional[QAction] """
        pass

    def addAction(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        addAction(self, action: Optional[QAction])
        addAction(self, text: Optional[str]) -> Optional[QAction]
        addAction(self, icon: QIcon, text: Optional[str]) -> Optional[QAction]
        addAction(self, text: Optional[str], slot: PYQT_SLOT, shortcut: Union[QKeySequence, QKeySequence.StandardKey, Optional[str], int] = 0) -> Optional[QAction]
        addAction(self, icon: QIcon, text: Optional[str], slot: PYQT_SLOT, shortcut: Union[QKeySequence, QKeySequence.StandardKey, Optional[str], int] = 0) -> Optional[QAction]
        """
        pass

    def addMenu(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        addMenu(self, menu: Optional[QMenu]) -> Optional[QAction]
        addMenu(self, title: Optional[str]) -> Optional[QMenu]
        addMenu(self, icon: QIcon, title: Optional[str]) -> Optional[QMenu]
        """
        pass

    def addSection(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        addSection(self, text: Optional[str]) -> Optional[QAction]
        addSection(self, icon: QIcon, text: Optional[str]) -> Optional[QAction]
        """
        pass

    def addSeparator(self): # real signature unknown; restored from __doc__
        """ addSeparator(self) -> Optional[QAction] """
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

    def columnCount(self): # real signature unknown; restored from __doc__
        """ columnCount(self) -> int """
        return 0

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def contextMenuEvent(self, *args, **kwargs): # real signature unknown
        pass

    def create(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def defaultAction(self): # real signature unknown; restored from __doc__
        """ defaultAction(self) -> Optional[QAction] """
        pass

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

    def enterEvent(self, a0, QEvent=None): # real signature unknown; restored from __doc__
        """ enterEvent(self, a0: Optional[QEvent]) """
        pass

    def event(self, a0, QEvent=None): # real signature unknown; restored from __doc__
        """ event(self, a0: Optional[QEvent]) -> bool """
        return False

    def exec(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        exec(self) -> Optional[QAction]
        exec(self, pos: QPoint, action: Optional[QAction] = None) -> Optional[QAction]
        exec(actions: Iterable[QAction], pos: QPoint, at: Optional[QAction] = None, parent: Optional[QWidget] = None) -> Optional[QAction]
        """
        pass

    def exec_(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        exec_(self) -> Optional[QAction]
        exec_(self, p: QPoint, action: Optional[QAction] = None) -> Optional[QAction]
        exec_(actions: Iterable[QAction], pos: QPoint, at: Optional[QAction] = None, parent: Optional[QWidget] = None) -> Optional[QAction]
        """
        pass

    def focusInEvent(self, *args, **kwargs): # real signature unknown
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

    def hideEvent(self, a0, QHideEvent=None): # real signature unknown; restored from __doc__
        """ hideEvent(self, a0: Optional[QHideEvent]) """
        pass

    def hideTearOffMenu(self): # real signature unknown; restored from __doc__
        """ hideTearOffMenu(self) """
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

    def initPainter(self, *args, **kwargs): # real signature unknown
        pass

    def initStyleOption(self, option, QStyleOptionMenuItem=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ initStyleOption(self, option: Optional[QStyleOptionMenuItem], action: Optional[QAction]) """
        pass

    def inputMethodEvent(self, *args, **kwargs): # real signature unknown
        pass

    def insertMenu(self, before, QAction=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ insertMenu(self, before: Optional[QAction], menu: Optional[QMenu]) -> Optional[QAction] """
        pass

    def insertSection(self, before, QAction=None, *args, **kwargs): # real signature unknown; restored from __doc__ with multiple overloads
        """
        insertSection(self, before: Optional[QAction], text: Optional[str]) -> Optional[QAction]
        insertSection(self, before: Optional[QAction], icon: QIcon, text: Optional[str]) -> Optional[QAction]
        """
        pass

    def insertSeparator(self, before, QAction=None): # real signature unknown; restored from __doc__
        """ insertSeparator(self, before: Optional[QAction]) -> Optional[QAction] """
        pass

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ isEmpty(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def isTearOffEnabled(self): # real signature unknown; restored from __doc__
        """ isTearOffEnabled(self) -> bool """
        return False

    def isTearOffMenuVisible(self): # real signature unknown; restored from __doc__
        """ isTearOffMenuVisible(self) -> bool """
        return False

    def keyPressEvent(self, a0, QKeyEvent=None): # real signature unknown; restored from __doc__
        """ keyPressEvent(self, a0: Optional[QKeyEvent]) """
        pass

    def keyReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def leaveEvent(self, a0, QEvent=None): # real signature unknown; restored from __doc__
        """ leaveEvent(self, a0: Optional[QEvent]) """
        pass

    def menuAction(self): # real signature unknown; restored from __doc__
        """ menuAction(self) -> Optional[QAction] """
        pass

    def metric(self, *args, **kwargs): # real signature unknown
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

    def nativeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def paintEvent(self, a0, QPaintEvent=None): # real signature unknown; restored from __doc__
        """ paintEvent(self, a0: Optional[QPaintEvent]) """
        pass

    def popup(self, p, action, QAction=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ popup(self, p: QPoint, action: Optional[QAction] = None) """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def resizeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def separatorsCollapsible(self): # real signature unknown; restored from __doc__
        """ separatorsCollapsible(self) -> bool """
        return False

    def setActiveAction(self, act, QAction=None): # real signature unknown; restored from __doc__
        """ setActiveAction(self, act: Optional[QAction]) """
        pass

    def setDefaultAction(self, a0, QAction=None): # real signature unknown; restored from __doc__
        """ setDefaultAction(self, a0: Optional[QAction]) """
        pass

    def setIcon(self, icon): # real signature unknown; restored from __doc__
        """ setIcon(self, icon: QIcon) """
        pass

    def setNoReplayFor(self, widget, QWidget=None): # real signature unknown; restored from __doc__
        """ setNoReplayFor(self, widget: Optional[QWidget]) """
        pass

    def setSeparatorsCollapsible(self, collapse): # real signature unknown; restored from __doc__
        """ setSeparatorsCollapsible(self, collapse: bool) """
        pass

    def setTearOffEnabled(self, a0): # real signature unknown; restored from __doc__
        """ setTearOffEnabled(self, a0: bool) """
        pass

    def setTitle(self, title, p_str=None): # real signature unknown; restored from __doc__
        """ setTitle(self, title: Optional[str]) """
        pass

    def setToolTipsVisible(self, visible): # real signature unknown; restored from __doc__
        """ setToolTipsVisible(self, visible: bool) """
        pass

    def sharedPainter(self, *args, **kwargs): # real signature unknown
        pass

    def showEvent(self, *args, **kwargs): # real signature unknown
        pass

    def showTearOffMenu(self, pos=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        showTearOffMenu(self)
        showTearOffMenu(self, pos: QPoint)
        """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> QSize """
        pass

    def tabletEvent(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, a0, QTimerEvent=None): # real signature unknown; restored from __doc__
        """ timerEvent(self, a0: Optional[QTimerEvent]) """
        pass

    def title(self): # real signature unknown; restored from __doc__
        """ title(self) -> str """
        return ""

    def toolTipsVisible(self): # real signature unknown; restored from __doc__
        """ toolTipsVisible(self) -> bool """
        return False

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

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

    def wheelEvent(self, a0, QWheelEvent=None): # real signature unknown; restored from __doc__
        """ wheelEvent(self, a0: Optional[QWheelEvent]) """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


