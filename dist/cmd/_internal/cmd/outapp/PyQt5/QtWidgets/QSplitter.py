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

class QSplitter(QFrame):
    """
    QSplitter(parent: Optional[QWidget] = None)
    QSplitter(orientation: Qt.Orientation, parent: Optional[QWidget] = None)
    """
    def actionEvent(self, *args, **kwargs): # real signature unknown
        pass

    def addWidget(self, widget, QWidget=None): # real signature unknown; restored from __doc__
        """ addWidget(self, widget: Optional[QWidget]) """
        pass

    def changeEvent(self, a0, QEvent=None): # real signature unknown; restored from __doc__
        """ changeEvent(self, a0: Optional[QEvent]) """
        pass

    def childEvent(self, a0, QChildEvent=None): # real signature unknown; restored from __doc__
        """ childEvent(self, a0: Optional[QChildEvent]) """
        pass

    def childrenCollapsible(self): # real signature unknown; restored from __doc__
        """ childrenCollapsible(self) -> bool """
        return False

    def closeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def closestLegalPosition(self, a0, a1): # real signature unknown; restored from __doc__
        """ closestLegalPosition(self, a0: int, a1: int) -> int """
        return 0

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def contextMenuEvent(self, *args, **kwargs): # real signature unknown
        pass

    def count(self): # real signature unknown; restored from __doc__
        """ count(self) -> int """
        return 0

    def create(self, *args, **kwargs): # real signature unknown
        pass

    def createHandle(self): # real signature unknown; restored from __doc__
        """ createHandle(self) -> Optional[QSplitterHandle] """
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

    def getRange(self, index): # real signature unknown; restored from __doc__
        """ getRange(self, index: int) -> (Optional[int], Optional[int]) """
        pass

    def handle(self, index): # real signature unknown; restored from __doc__
        """ handle(self, index: int) -> Optional[QSplitterHandle] """
        pass

    def handleWidth(self): # real signature unknown; restored from __doc__
        """ handleWidth(self) -> int """
        return 0

    def hideEvent(self, *args, **kwargs): # real signature unknown
        pass

    def indexOf(self, w, QWidget=None): # real signature unknown; restored from __doc__
        """ indexOf(self, w: Optional[QWidget]) -> int """
        return 0

    def initPainter(self, *args, **kwargs): # real signature unknown
        pass

    def initStyleOption(self, *args, **kwargs): # real signature unknown
        pass

    def inputMethodEvent(self, *args, **kwargs): # real signature unknown
        pass

    def insertWidget(self, index, widget, QWidget=None): # real signature unknown; restored from __doc__
        """ insertWidget(self, index: int, widget: Optional[QWidget]) """
        pass

    def isCollapsible(self, index): # real signature unknown; restored from __doc__
        """ isCollapsible(self, index: int) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def keyPressEvent(self, *args, **kwargs): # real signature unknown
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

    def moveSplitter(self, pos, index): # real signature unknown; restored from __doc__
        """ moveSplitter(self, pos: int, index: int) """
        pass

    def nativeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def opaqueResize(self): # real signature unknown; restored from __doc__
        """ opaqueResize(self) -> bool """
        return False

    def orientation(self): # real signature unknown; restored from __doc__
        """ orientation(self) -> Qt.Orientation """
        pass

    def paintEvent(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def refresh(self): # real signature unknown; restored from __doc__
        """ refresh(self) """
        pass

    def replaceWidget(self, index, widget, QWidget=None): # real signature unknown; restored from __doc__
        """ replaceWidget(self, index: int, widget: Optional[QWidget]) -> Optional[QWidget] """
        pass

    def resizeEvent(self, a0, QResizeEvent=None): # real signature unknown; restored from __doc__
        """ resizeEvent(self, a0: Optional[QResizeEvent]) """
        pass

    def restoreState(self, state, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ restoreState(self, state: Union[QByteArray, bytes, bytearray]) -> bool """
        return False

    def saveState(self): # real signature unknown; restored from __doc__
        """ saveState(self) -> QByteArray """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setChildrenCollapsible(self, a0): # real signature unknown; restored from __doc__
        """ setChildrenCollapsible(self, a0: bool) """
        pass

    def setCollapsible(self, index, a1): # real signature unknown; restored from __doc__
        """ setCollapsible(self, index: int, a1: bool) """
        pass

    def setHandleWidth(self, a0): # real signature unknown; restored from __doc__
        """ setHandleWidth(self, a0: int) """
        pass

    def setOpaqueResize(self, opaque=True): # real signature unknown; restored from __doc__
        """ setOpaqueResize(self, opaque: bool = True) """
        pass

    def setOrientation(self, a0): # real signature unknown; restored from __doc__
        """ setOrientation(self, a0: Qt.Orientation) """
        pass

    def setRubberBand(self, position): # real signature unknown; restored from __doc__
        """ setRubberBand(self, position: int) """
        pass

    def setSizes(self, p_list, p_int=None): # real signature unknown; restored from __doc__
        """ setSizes(self, list: Iterable[int]) """
        pass

    def setStretchFactor(self, index, stretch): # real signature unknown; restored from __doc__
        """ setStretchFactor(self, index: int, stretch: int) """
        pass

    def sharedPainter(self, *args, **kwargs): # real signature unknown
        pass

    def showEvent(self, *args, **kwargs): # real signature unknown
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> QSize """
        pass

    def sizes(self): # real signature unknown; restored from __doc__
        """ sizes(self) -> List[int] """
        return []

    def splitterMoved(self, *args, **kwargs): # real signature unknown
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

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass


