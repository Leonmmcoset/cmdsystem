# encoding: utf-8
# module PyQt5.QtWidgets
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


from .QFrame import QFrame

class QToolBox(QFrame):
    """ QToolBox(parent: Optional[QWidget] = None, flags: Union[Qt.WindowFlags, Qt.WindowType] = Qt.WindowFlags()) """
    def actionEvent(self, *args, **kwargs): # real signature unknown
        pass

    def addItem(self, item, QWidget=None, *args, **kwargs): # real signature unknown; restored from __doc__ with multiple overloads
        """
        addItem(self, item: Optional[QWidget], text: Optional[str]) -> int
        addItem(self, item: Optional[QWidget], iconSet: QIcon, text: Optional[str]) -> int
        """
        pass

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

    def currentWidget(self): # real signature unknown; restored from __doc__
        """ currentWidget(self) -> Optional[QWidget] """
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
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

    def drawFrame(self, *args, **kwargs): # real signature unknown
        pass

    def dropEvent(self, *args, **kwargs): # real signature unknown
        pass

    def enterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, e, QEvent=None): # real signature unknown; restored from __doc__
        """ event(self, e: Optional[QEvent]) -> bool """
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

    def hideEvent(self, *args, **kwargs): # real signature unknown
        pass

    def indexOf(self, widget, QWidget=None): # real signature unknown; restored from __doc__
        """ indexOf(self, widget: Optional[QWidget]) -> int """
        return 0

    def initPainter(self, *args, **kwargs): # real signature unknown
        pass

    def initStyleOption(self, *args, **kwargs): # real signature unknown
        pass

    def inputMethodEvent(self, *args, **kwargs): # real signature unknown
        pass

    def insertItem(self, index, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        insertItem(self, index: int, item: Optional[QWidget], text: Optional[str]) -> int
        insertItem(self, index: int, widget: Optional[QWidget], icon: QIcon, text: Optional[str]) -> int
        """
        pass

    def isItemEnabled(self, index): # real signature unknown; restored from __doc__
        """ isItemEnabled(self, index: int) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def itemIcon(self, index): # real signature unknown; restored from __doc__
        """ itemIcon(self, index: int) -> QIcon """
        pass

    def itemInserted(self, index): # real signature unknown; restored from __doc__
        """ itemInserted(self, index: int) """
        pass

    def itemRemoved(self, index): # real signature unknown; restored from __doc__
        """ itemRemoved(self, index: int) """
        pass

    def itemText(self, index): # real signature unknown; restored from __doc__
        """ itemText(self, index: int) -> str """
        return ""

    def itemToolTip(self, index): # real signature unknown; restored from __doc__
        """ itemToolTip(self, index: int) -> str """
        return ""

    def keyPressEvent(self, *args, **kwargs): # real signature unknown
        pass

    def keyReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def leaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def metric(self, *args, **kwargs): # real signature unknown
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

    def paintEvent(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def removeItem(self, index): # real signature unknown; restored from __doc__
        """ removeItem(self, index: int) """
        pass

    def resizeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setCurrentIndex(self, index): # real signature unknown; restored from __doc__
        """ setCurrentIndex(self, index: int) """
        pass

    def setCurrentWidget(self, widget, QWidget=None): # real signature unknown; restored from __doc__
        """ setCurrentWidget(self, widget: Optional[QWidget]) """
        pass

    def setItemEnabled(self, index, enabled): # real signature unknown; restored from __doc__
        """ setItemEnabled(self, index: int, enabled: bool) """
        pass

    def setItemIcon(self, index, icon): # real signature unknown; restored from __doc__
        """ setItemIcon(self, index: int, icon: QIcon) """
        pass

    def setItemText(self, index, text, p_str=None): # real signature unknown; restored from __doc__
        """ setItemText(self, index: int, text: Optional[str]) """
        pass

    def setItemToolTip(self, index, toolTip, p_str=None): # real signature unknown; restored from __doc__
        """ setItemToolTip(self, index: int, toolTip: Optional[str]) """
        pass

    def sharedPainter(self, *args, **kwargs): # real signature unknown
        pass

    def showEvent(self, e, QShowEvent=None): # real signature unknown; restored from __doc__
        """ showEvent(self, e: Optional[QShowEvent]) """
        pass

    def tabletEvent(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

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


