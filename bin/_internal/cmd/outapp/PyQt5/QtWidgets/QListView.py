# encoding: utf-8
# module PyQt5.QtWidgets
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


from .QAbstractItemView import QAbstractItemView

class QListView(QAbstractItemView):
    """ QListView(parent: Optional[QWidget] = None) """
    def actionEvent(self, *args, **kwargs): # real signature unknown
        pass

    def batchSize(self): # real signature unknown; restored from __doc__
        """ batchSize(self) -> int """
        return 0

    def changeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def clearPropertyFlags(self): # real signature unknown; restored from __doc__
        """ clearPropertyFlags(self) """
        pass

    def closeEditor(self, *args, **kwargs): # real signature unknown
        pass

    def closeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def commitData(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def contextMenuEvent(self, *args, **kwargs): # real signature unknown
        pass

    def create(self, *args, **kwargs): # real signature unknown
        pass

    def currentChanged(self, current, previous): # real signature unknown; restored from __doc__
        """ currentChanged(self, current: QModelIndex, previous: QModelIndex) """
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dataChanged(self, topLeft, bottomRight, roles, p_int=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ dataChanged(self, topLeft: QModelIndex, bottomRight: QModelIndex, roles: Iterable[int] = []) """
        pass

    def destroy(self, *args, **kwargs): # real signature unknown
        pass

    def dirtyRegionOffset(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def dragEnterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dragLeaveEvent(self, e, QDragLeaveEvent=None): # real signature unknown; restored from __doc__
        """ dragLeaveEvent(self, e: Optional[QDragLeaveEvent]) """
        pass

    def dragMoveEvent(self, e, QDragMoveEvent=None): # real signature unknown; restored from __doc__
        """ dragMoveEvent(self, e: Optional[QDragMoveEvent]) """
        pass

    def drawFrame(self, *args, **kwargs): # real signature unknown
        pass

    def dropEvent(self, e, QDropEvent=None): # real signature unknown; restored from __doc__
        """ dropEvent(self, e: Optional[QDropEvent]) """
        pass

    def dropIndicatorPosition(self, *args, **kwargs): # real signature unknown
        pass

    def edit(self, *args, **kwargs): # real signature unknown
        pass

    def editorDestroyed(self, *args, **kwargs): # real signature unknown
        pass

    def enterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, e, QEvent=None): # real signature unknown; restored from __doc__
        """ event(self, e: Optional[QEvent]) -> bool """
        return False

    def eventFilter(self, *args, **kwargs): # real signature unknown
        pass

    def executeDelayedItemsLayout(self, *args, **kwargs): # real signature unknown
        pass

    def flow(self): # real signature unknown; restored from __doc__
        """ flow(self) -> QListView.Flow """
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

    def gridSize(self): # real signature unknown; restored from __doc__
        """ gridSize(self) -> QSize """
        pass

    def hideEvent(self, *args, **kwargs): # real signature unknown
        pass

    def horizontalOffset(self): # real signature unknown; restored from __doc__
        """ horizontalOffset(self) -> int """
        return 0

    def horizontalScrollbarAction(self, *args, **kwargs): # real signature unknown
        pass

    def horizontalScrollbarValueChanged(self, *args, **kwargs): # real signature unknown
        pass

    def indexAt(self, p): # real signature unknown; restored from __doc__
        """ indexAt(self, p: QPoint) -> QModelIndex """
        pass

    def indexesMoved(self, *args, **kwargs): # real signature unknown
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

    def initPainter(self, *args, **kwargs): # real signature unknown
        pass

    def initStyleOption(self, *args, **kwargs): # real signature unknown
        pass

    def inputMethodEvent(self, *args, **kwargs): # real signature unknown
        pass

    def isIndexHidden(self, index): # real signature unknown; restored from __doc__
        """ isIndexHidden(self, index: QModelIndex) -> bool """
        return False

    def isRowHidden(self, row): # real signature unknown; restored from __doc__
        """ isRowHidden(self, row: int) -> bool """
        return False

    def isSelectionRectVisible(self): # real signature unknown; restored from __doc__
        """ isSelectionRectVisible(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def isWrapping(self): # real signature unknown; restored from __doc__
        """ isWrapping(self) -> bool """
        return False

    def itemAlignment(self): # real signature unknown; restored from __doc__
        """ itemAlignment(self) -> Qt.Alignment """
        pass

    def keyPressEvent(self, *args, **kwargs): # real signature unknown
        pass

    def keyReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def layoutMode(self): # real signature unknown; restored from __doc__
        """ layoutMode(self) -> QListView.LayoutMode """
        pass

    def leaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def metric(self, *args, **kwargs): # real signature unknown
        pass

    def modelColumn(self): # real signature unknown; restored from __doc__
        """ modelColumn(self) -> int """
        return 0

    def mouseDoubleClickEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mouseMoveEvent(self, e, QMouseEvent=None): # real signature unknown; restored from __doc__
        """ mouseMoveEvent(self, e: Optional[QMouseEvent]) """
        pass

    def mousePressEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mouseReleaseEvent(self, e, QMouseEvent=None): # real signature unknown; restored from __doc__
        """ mouseReleaseEvent(self, e: Optional[QMouseEvent]) """
        pass

    def moveCursor(self, cursorAction, modifiers, Qt_KeyboardModifiers=None, Qt_KeyboardModifier=None): # real signature unknown; restored from __doc__
        """ moveCursor(self, cursorAction: QAbstractItemView.CursorAction, modifiers: Union[Qt.KeyboardModifiers, Qt.KeyboardModifier]) -> QModelIndex """
        pass

    def moveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def movement(self): # real signature unknown; restored from __doc__
        """ movement(self) -> QListView.Movement """
        pass

    def nativeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def paintEvent(self, e, QPaintEvent=None): # real signature unknown; restored from __doc__
        """ paintEvent(self, e: Optional[QPaintEvent]) """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def rectForIndex(self, index): # real signature unknown; restored from __doc__
        """ rectForIndex(self, index: QModelIndex) -> QRect """
        pass

    def reset(self): # real signature unknown; restored from __doc__
        """ reset(self) """
        pass

    def resizeEvent(self, e, QResizeEvent=None): # real signature unknown; restored from __doc__
        """ resizeEvent(self, e: Optional[QResizeEvent]) """
        pass

    def resizeMode(self): # real signature unknown; restored from __doc__
        """ resizeMode(self) -> QListView.ResizeMode """
        pass

    def rowsAboutToBeRemoved(self, parent, start, end): # real signature unknown; restored from __doc__
        """ rowsAboutToBeRemoved(self, parent: QModelIndex, start: int, end: int) """
        pass

    def rowsInserted(self, parent, start, end): # real signature unknown; restored from __doc__
        """ rowsInserted(self, parent: QModelIndex, start: int, end: int) """
        pass

    def scheduleDelayedItemsLayout(self, *args, **kwargs): # real signature unknown
        pass

    def scrollContentsBy(self, dx, dy): # real signature unknown; restored from __doc__
        """ scrollContentsBy(self, dx: int, dy: int) """
        pass

    def scrollDirtyRegion(self, *args, **kwargs): # real signature unknown
        pass

    def scrollTo(self, index, hint=None): # real signature unknown; restored from __doc__
        """ scrollTo(self, index: QModelIndex, hint: QAbstractItemView.ScrollHint = QAbstractItemView.EnsureVisible) """
        pass

    def selectedIndexes(self): # real signature unknown; restored from __doc__
        """ selectedIndexes(self) -> List[QModelIndex] """
        return []

    def selectionChanged(self, selected, deselected): # real signature unknown; restored from __doc__
        """ selectionChanged(self, selected: QItemSelection, deselected: QItemSelection) """
        pass

    def selectionCommand(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setBatchSize(self, batchSize): # real signature unknown; restored from __doc__
        """ setBatchSize(self, batchSize: int) """
        pass

    def setDirtyRegion(self, *args, **kwargs): # real signature unknown
        pass

    def setFlow(self, flow): # real signature unknown; restored from __doc__
        """ setFlow(self, flow: QListView.Flow) """
        pass

    def setGridSize(self, size): # real signature unknown; restored from __doc__
        """ setGridSize(self, size: QSize) """
        pass

    def setItemAlignment(self, alignment, Qt_Alignment=None, Qt_AlignmentFlag=None): # real signature unknown; restored from __doc__
        """ setItemAlignment(self, alignment: Union[Qt.Alignment, Qt.AlignmentFlag]) """
        pass

    def setLayoutMode(self, mode): # real signature unknown; restored from __doc__
        """ setLayoutMode(self, mode: QListView.LayoutMode) """
        pass

    def setModelColumn(self, column): # real signature unknown; restored from __doc__
        """ setModelColumn(self, column: int) """
        pass

    def setMovement(self, movement): # real signature unknown; restored from __doc__
        """ setMovement(self, movement: QListView.Movement) """
        pass

    def setPositionForIndex(self, position, index): # real signature unknown; restored from __doc__
        """ setPositionForIndex(self, position: QPoint, index: QModelIndex) """
        pass

    def setResizeMode(self, mode): # real signature unknown; restored from __doc__
        """ setResizeMode(self, mode: QListView.ResizeMode) """
        pass

    def setRootIndex(self, index): # real signature unknown; restored from __doc__
        """ setRootIndex(self, index: QModelIndex) """
        pass

    def setRowHidden(self, row, hide): # real signature unknown; restored from __doc__
        """ setRowHidden(self, row: int, hide: bool) """
        pass

    def setSelection(self, rect, command, QItemSelectionModel_SelectionFlags=None, QItemSelectionModel_SelectionFlag=None): # real signature unknown; restored from __doc__
        """ setSelection(self, rect: QRect, command: Union[QItemSelectionModel.SelectionFlags, QItemSelectionModel.SelectionFlag]) """
        pass

    def setSelectionRectVisible(self, show): # real signature unknown; restored from __doc__
        """ setSelectionRectVisible(self, show: bool) """
        pass

    def setSpacing(self, space): # real signature unknown; restored from __doc__
        """ setSpacing(self, space: int) """
        pass

    def setState(self, *args, **kwargs): # real signature unknown
        pass

    def setUniformItemSizes(self, enable): # real signature unknown; restored from __doc__
        """ setUniformItemSizes(self, enable: bool) """
        pass

    def setViewMode(self, mode): # real signature unknown; restored from __doc__
        """ setViewMode(self, mode: QListView.ViewMode) """
        pass

    def setViewportMargins(self, *args, **kwargs): # real signature unknown
        pass

    def setWordWrap(self, on): # real signature unknown; restored from __doc__
        """ setWordWrap(self, on: bool) """
        pass

    def setWrapping(self, enable): # real signature unknown; restored from __doc__
        """ setWrapping(self, enable: bool) """
        pass

    def sharedPainter(self, *args, **kwargs): # real signature unknown
        pass

    def showEvent(self, *args, **kwargs): # real signature unknown
        pass

    def spacing(self): # real signature unknown; restored from __doc__
        """ spacing(self) -> int """
        return 0

    def startDrag(self, supportedActions, Qt_DropActions=None, Qt_DropAction=None): # real signature unknown; restored from __doc__
        """ startDrag(self, supportedActions: Union[Qt.DropActions, Qt.DropAction]) """
        pass

    def state(self, *args, **kwargs): # real signature unknown
        pass

    def tabletEvent(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, e, QTimerEvent=None): # real signature unknown; restored from __doc__
        """ timerEvent(self, e: Optional[QTimerEvent]) """
        pass

    def uniformItemSizes(self): # real signature unknown; restored from __doc__
        """ uniformItemSizes(self) -> bool """
        return False

    def updateEditorData(self, *args, **kwargs): # real signature unknown
        pass

    def updateEditorGeometries(self, *args, **kwargs): # real signature unknown
        pass

    def updateGeometries(self): # real signature unknown; restored from __doc__
        """ updateGeometries(self) """
        pass

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

    def verticalOffset(self): # real signature unknown; restored from __doc__
        """ verticalOffset(self) -> int """
        return 0

    def verticalScrollbarAction(self, *args, **kwargs): # real signature unknown
        pass

    def verticalScrollbarValueChanged(self, *args, **kwargs): # real signature unknown
        pass

    def viewMode(self): # real signature unknown; restored from __doc__
        """ viewMode(self) -> QListView.ViewMode """
        pass

    def viewOptions(self): # real signature unknown; restored from __doc__
        """ viewOptions(self) -> QStyleOptionViewItem """
        return QStyleOptionViewItem

    def viewportEvent(self, *args, **kwargs): # real signature unknown
        pass

    def viewportMargins(self, *args, **kwargs): # real signature unknown
        pass

    def viewportSizeHint(self): # real signature unknown; restored from __doc__
        """ viewportSizeHint(self) -> QSize """
        pass

    def visualRect(self, index): # real signature unknown; restored from __doc__
        """ visualRect(self, index: QModelIndex) -> QRect """
        pass

    def visualRegionForSelection(self, selection): # real signature unknown; restored from __doc__
        """ visualRegionForSelection(self, selection: QItemSelection) -> QRegion """
        pass

    def wheelEvent(self, e, QWheelEvent=None): # real signature unknown; restored from __doc__
        """ wheelEvent(self, e: Optional[QWheelEvent]) """
        pass

    def wordWrap(self): # real signature unknown; restored from __doc__
        """ wordWrap(self) -> bool """
        return False

    def __init__(self, parent, QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    Adjust = 1
    Batched = 1
    Fixed = 0
    Free = 1
    IconMode = 1
    LeftToRight = 0
    ListMode = 0
    SinglePass = 0
    Snap = 2
    Static = 0
    TopToBottom = 1


