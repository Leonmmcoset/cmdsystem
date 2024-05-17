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

class QTreeView(QAbstractItemView):
    """ QTreeView(parent: Optional[QWidget] = None) """
    def actionEvent(self, *args, **kwargs): # real signature unknown
        pass

    def allColumnsShowFocus(self): # real signature unknown; restored from __doc__
        """ allColumnsShowFocus(self) -> bool """
        return False

    def autoExpandDelay(self): # real signature unknown; restored from __doc__
        """ autoExpandDelay(self) -> int """
        return 0

    def changeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def closeEditor(self, *args, **kwargs): # real signature unknown
        pass

    def closeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def collapse(self, index): # real signature unknown; restored from __doc__
        """ collapse(self, index: QModelIndex) """
        pass

    def collapseAll(self): # real signature unknown; restored from __doc__
        """ collapseAll(self) """
        pass

    def collapsed(self, *args, **kwargs): # real signature unknown
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

    def columnAt(self, x): # real signature unknown; restored from __doc__
        """ columnAt(self, x: int) -> int """
        return 0

    def columnCountChanged(self, oldCount, newCount): # real signature unknown; restored from __doc__
        """ columnCountChanged(self, oldCount: int, newCount: int) """
        pass

    def columnMoved(self): # real signature unknown; restored from __doc__
        """ columnMoved(self) """
        pass

    def columnResized(self, column, oldSize, newSize): # real signature unknown; restored from __doc__
        """ columnResized(self, column: int, oldSize: int, newSize: int) """
        pass

    def columnViewportPosition(self, column): # real signature unknown; restored from __doc__
        """ columnViewportPosition(self, column: int) -> int """
        return 0

    def columnWidth(self, column): # real signature unknown; restored from __doc__
        """ columnWidth(self, column: int) -> int """
        return 0

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

    def dragLeaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dragMoveEvent(self, event, QDragMoveEvent=None): # real signature unknown; restored from __doc__
        """ dragMoveEvent(self, event: Optional[QDragMoveEvent]) """
        pass

    def drawBranches(self, painter, QPainter=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ drawBranches(self, painter: Optional[QPainter], rect: QRect, index: QModelIndex) """
        pass

    def drawFrame(self, *args, **kwargs): # real signature unknown
        pass

    def drawRow(self, painter, QPainter=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ drawRow(self, painter: Optional[QPainter], options: QStyleOptionViewItem, index: QModelIndex) """
        pass

    def drawTree(self, painter, QPainter=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ drawTree(self, painter: Optional[QPainter], region: QRegion) """
        pass

    def dropEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dropIndicatorPosition(self, *args, **kwargs): # real signature unknown
        pass

    def edit(self, *args, **kwargs): # real signature unknown
        pass

    def editorDestroyed(self, *args, **kwargs): # real signature unknown
        pass

    def enterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, *args, **kwargs): # real signature unknown
        pass

    def eventFilter(self, *args, **kwargs): # real signature unknown
        pass

    def executeDelayedItemsLayout(self, *args, **kwargs): # real signature unknown
        pass

    def expand(self, index): # real signature unknown; restored from __doc__
        """ expand(self, index: QModelIndex) """
        pass

    def expandAll(self): # real signature unknown; restored from __doc__
        """ expandAll(self) """
        pass

    def expanded(self, *args, **kwargs): # real signature unknown
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

    def expandRecursively(self, index, depth=-1): # real signature unknown; restored from __doc__
        """ expandRecursively(self, index: QModelIndex, depth: int = -1) """
        pass

    def expandsOnDoubleClick(self): # real signature unknown; restored from __doc__
        """ expandsOnDoubleClick(self) -> bool """
        return False

    def expandToDepth(self, depth): # real signature unknown; restored from __doc__
        """ expandToDepth(self, depth: int) """
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

    def header(self): # real signature unknown; restored from __doc__
        """ header(self) -> Optional[QHeaderView] """
        pass

    def hideColumn(self, column): # real signature unknown; restored from __doc__
        """ hideColumn(self, column: int) """
        pass

    def hideEvent(self, *args, **kwargs): # real signature unknown
        pass

    def horizontalOffset(self): # real signature unknown; restored from __doc__
        """ horizontalOffset(self) -> int """
        return 0

    def horizontalScrollbarAction(self, action): # real signature unknown; restored from __doc__
        """ horizontalScrollbarAction(self, action: int) """
        pass

    def horizontalScrollbarValueChanged(self, *args, **kwargs): # real signature unknown
        pass

    def indentation(self): # real signature unknown; restored from __doc__
        """ indentation(self) -> int """
        return 0

    def indexAbove(self, index): # real signature unknown; restored from __doc__
        """ indexAbove(self, index: QModelIndex) -> QModelIndex """
        pass

    def indexAt(self, p): # real signature unknown; restored from __doc__
        """ indexAt(self, p: QPoint) -> QModelIndex """
        pass

    def indexBelow(self, index): # real signature unknown; restored from __doc__
        """ indexBelow(self, index: QModelIndex) -> QModelIndex """
        pass

    def indexRowSizeHint(self, index): # real signature unknown; restored from __doc__
        """ indexRowSizeHint(self, index: QModelIndex) -> int """
        return 0

    def initPainter(self, *args, **kwargs): # real signature unknown
        pass

    def initStyleOption(self, *args, **kwargs): # real signature unknown
        pass

    def inputMethodEvent(self, *args, **kwargs): # real signature unknown
        pass

    def isAnimated(self): # real signature unknown; restored from __doc__
        """ isAnimated(self) -> bool """
        return False

    def isColumnHidden(self, column): # real signature unknown; restored from __doc__
        """ isColumnHidden(self, column: int) -> bool """
        return False

    def isExpanded(self, index): # real signature unknown; restored from __doc__
        """ isExpanded(self, index: QModelIndex) -> bool """
        return False

    def isFirstColumnSpanned(self, row, parent): # real signature unknown; restored from __doc__
        """ isFirstColumnSpanned(self, row: int, parent: QModelIndex) -> bool """
        return False

    def isHeaderHidden(self): # real signature unknown; restored from __doc__
        """ isHeaderHidden(self) -> bool """
        return False

    def isIndexHidden(self, index): # real signature unknown; restored from __doc__
        """ isIndexHidden(self, index: QModelIndex) -> bool """
        return False

    def isRowHidden(self, row, parent): # real signature unknown; restored from __doc__
        """ isRowHidden(self, row: int, parent: QModelIndex) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def isSortingEnabled(self): # real signature unknown; restored from __doc__
        """ isSortingEnabled(self) -> bool """
        return False

    def itemsExpandable(self): # real signature unknown; restored from __doc__
        """ itemsExpandable(self) -> bool """
        return False

    def keyboardSearch(self, search, p_str=None): # real signature unknown; restored from __doc__
        """ keyboardSearch(self, search: Optional[str]) """
        pass

    def keyPressEvent(self, event, QKeyEvent=None): # real signature unknown; restored from __doc__
        """ keyPressEvent(self, event: Optional[QKeyEvent]) """
        pass

    def keyReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def leaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def metric(self, *args, **kwargs): # real signature unknown
        pass

    def mouseDoubleClickEvent(self, e, QMouseEvent=None): # real signature unknown; restored from __doc__
        """ mouseDoubleClickEvent(self, e: Optional[QMouseEvent]) """
        pass

    def mouseMoveEvent(self, event, QMouseEvent=None): # real signature unknown; restored from __doc__
        """ mouseMoveEvent(self, event: Optional[QMouseEvent]) """
        pass

    def mousePressEvent(self, e, QMouseEvent=None): # real signature unknown; restored from __doc__
        """ mousePressEvent(self, e: Optional[QMouseEvent]) """
        pass

    def mouseReleaseEvent(self, event, QMouseEvent=None): # real signature unknown; restored from __doc__
        """ mouseReleaseEvent(self, event: Optional[QMouseEvent]) """
        pass

    def moveCursor(self, cursorAction, modifiers, Qt_KeyboardModifiers=None, Qt_KeyboardModifier=None): # real signature unknown; restored from __doc__
        """ moveCursor(self, cursorAction: QAbstractItemView.CursorAction, modifiers: Union[Qt.KeyboardModifiers, Qt.KeyboardModifier]) -> QModelIndex """
        pass

    def moveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def nativeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def paintEvent(self, e, QPaintEvent=None): # real signature unknown; restored from __doc__
        """ paintEvent(self, e: Optional[QPaintEvent]) """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def reexpand(self): # real signature unknown; restored from __doc__
        """ reexpand(self) """
        pass

    def reset(self): # real signature unknown; restored from __doc__
        """ reset(self) """
        pass

    def resetIndentation(self): # real signature unknown; restored from __doc__
        """ resetIndentation(self) """
        pass

    def resizeColumnToContents(self, column): # real signature unknown; restored from __doc__
        """ resizeColumnToContents(self, column: int) """
        pass

    def resizeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def rootIsDecorated(self): # real signature unknown; restored from __doc__
        """ rootIsDecorated(self) -> bool """
        return False

    def rowHeight(self, index): # real signature unknown; restored from __doc__
        """ rowHeight(self, index: QModelIndex) -> int """
        return 0

    def rowsAboutToBeRemoved(self, parent, start, end): # real signature unknown; restored from __doc__
        """ rowsAboutToBeRemoved(self, parent: QModelIndex, start: int, end: int) """
        pass

    def rowsInserted(self, parent, start, end): # real signature unknown; restored from __doc__
        """ rowsInserted(self, parent: QModelIndex, start: int, end: int) """
        pass

    def rowsRemoved(self, parent, first, last): # real signature unknown; restored from __doc__
        """ rowsRemoved(self, parent: QModelIndex, first: int, last: int) """
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

    def selectAll(self): # real signature unknown; restored from __doc__
        """ selectAll(self) """
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

    def setAllColumnsShowFocus(self, enable): # real signature unknown; restored from __doc__
        """ setAllColumnsShowFocus(self, enable: bool) """
        pass

    def setAnimated(self, enable): # real signature unknown; restored from __doc__
        """ setAnimated(self, enable: bool) """
        pass

    def setAutoExpandDelay(self, delay): # real signature unknown; restored from __doc__
        """ setAutoExpandDelay(self, delay: int) """
        pass

    def setColumnHidden(self, column, hide): # real signature unknown; restored from __doc__
        """ setColumnHidden(self, column: int, hide: bool) """
        pass

    def setColumnWidth(self, column, width): # real signature unknown; restored from __doc__
        """ setColumnWidth(self, column: int, width: int) """
        pass

    def setDirtyRegion(self, *args, **kwargs): # real signature unknown
        pass

    def setExpanded(self, index, expand): # real signature unknown; restored from __doc__
        """ setExpanded(self, index: QModelIndex, expand: bool) """
        pass

    def setExpandsOnDoubleClick(self, enable): # real signature unknown; restored from __doc__
        """ setExpandsOnDoubleClick(self, enable: bool) """
        pass

    def setFirstColumnSpanned(self, row, parent, span): # real signature unknown; restored from __doc__
        """ setFirstColumnSpanned(self, row: int, parent: QModelIndex, span: bool) """
        pass

    def setHeader(self, header, QHeaderView=None): # real signature unknown; restored from __doc__
        """ setHeader(self, header: Optional[QHeaderView]) """
        pass

    def setHeaderHidden(self, hide): # real signature unknown; restored from __doc__
        """ setHeaderHidden(self, hide: bool) """
        pass

    def setIndentation(self, i): # real signature unknown; restored from __doc__
        """ setIndentation(self, i: int) """
        pass

    def setItemsExpandable(self, enable): # real signature unknown; restored from __doc__
        """ setItemsExpandable(self, enable: bool) """
        pass

    def setModel(self, model, QAbstractItemModel=None): # real signature unknown; restored from __doc__
        """ setModel(self, model: Optional[QAbstractItemModel]) """
        pass

    def setRootIndex(self, index): # real signature unknown; restored from __doc__
        """ setRootIndex(self, index: QModelIndex) """
        pass

    def setRootIsDecorated(self, show): # real signature unknown; restored from __doc__
        """ setRootIsDecorated(self, show: bool) """
        pass

    def setRowHidden(self, row, parent, hide): # real signature unknown; restored from __doc__
        """ setRowHidden(self, row: int, parent: QModelIndex, hide: bool) """
        pass

    def setSelection(self, rect, command, QItemSelectionModel_SelectionFlags=None, QItemSelectionModel_SelectionFlag=None): # real signature unknown; restored from __doc__
        """ setSelection(self, rect: QRect, command: Union[QItemSelectionModel.SelectionFlags, QItemSelectionModel.SelectionFlag]) """
        pass

    def setSelectionModel(self, selectionModel, QItemSelectionModel=None): # real signature unknown; restored from __doc__
        """ setSelectionModel(self, selectionModel: Optional[QItemSelectionModel]) """
        pass

    def setSortingEnabled(self, enable): # real signature unknown; restored from __doc__
        """ setSortingEnabled(self, enable: bool) """
        pass

    def setState(self, *args, **kwargs): # real signature unknown
        pass

    def setTreePosition(self, logicalIndex): # real signature unknown; restored from __doc__
        """ setTreePosition(self, logicalIndex: int) """
        pass

    def setUniformRowHeights(self, uniform): # real signature unknown; restored from __doc__
        """ setUniformRowHeights(self, uniform: bool) """
        pass

    def setViewportMargins(self, *args, **kwargs): # real signature unknown
        pass

    def setWordWrap(self, on): # real signature unknown; restored from __doc__
        """ setWordWrap(self, on: bool) """
        pass

    def sharedPainter(self, *args, **kwargs): # real signature unknown
        pass

    def showColumn(self, column): # real signature unknown; restored from __doc__
        """ showColumn(self, column: int) """
        pass

    def showEvent(self, *args, **kwargs): # real signature unknown
        pass

    def sizeHintForColumn(self, column): # real signature unknown; restored from __doc__
        """ sizeHintForColumn(self, column: int) -> int """
        return 0

    def sortByColumn(self, column, order): # real signature unknown; restored from __doc__
        """ sortByColumn(self, column: int, order: Qt.SortOrder) """
        pass

    def startDrag(self, *args, **kwargs): # real signature unknown
        pass

    def state(self, *args, **kwargs): # real signature unknown
        pass

    def tabletEvent(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, event, QTimerEvent=None): # real signature unknown; restored from __doc__
        """ timerEvent(self, event: Optional[QTimerEvent]) """
        pass

    def treePosition(self): # real signature unknown; restored from __doc__
        """ treePosition(self) -> int """
        return 0

    def uniformRowHeights(self): # real signature unknown; restored from __doc__
        """ uniformRowHeights(self) -> bool """
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

    def viewOptions(self, *args, **kwargs): # real signature unknown
        pass

    def viewportEvent(self, event, QEvent=None): # real signature unknown; restored from __doc__
        """ viewportEvent(self, event: Optional[QEvent]) -> bool """
        return False

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

    def wheelEvent(self, *args, **kwargs): # real signature unknown
        pass

    def wordWrap(self): # real signature unknown; restored from __doc__
        """ wordWrap(self) -> bool """
        return False

    def __init__(self, parent, QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass


