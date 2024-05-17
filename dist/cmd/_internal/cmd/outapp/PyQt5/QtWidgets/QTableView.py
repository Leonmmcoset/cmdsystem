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

class QTableView(QAbstractItemView):
    """ QTableView(parent: Optional[QWidget] = None) """
    def actionEvent(self, *args, **kwargs): # real signature unknown
        pass

    def changeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def clearSpans(self): # real signature unknown; restored from __doc__
        """ clearSpans(self) """
        pass

    def closeEditor(self, *args, **kwargs): # real signature unknown
        pass

    def closeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def columnAt(self, x): # real signature unknown; restored from __doc__
        """ columnAt(self, x: int) -> int """
        return 0

    def columnCountChanged(self, oldCount, newCount): # real signature unknown; restored from __doc__
        """ columnCountChanged(self, oldCount: int, newCount: int) """
        pass

    def columnMoved(self, column, oldIndex, newIndex): # real signature unknown; restored from __doc__
        """ columnMoved(self, column: int, oldIndex: int, newIndex: int) """
        pass

    def columnResized(self, column, oldWidth, newWidth): # real signature unknown; restored from __doc__
        """ columnResized(self, column: int, oldWidth: int, newWidth: int) """
        pass

    def columnSpan(self, row, column): # real signature unknown; restored from __doc__
        """ columnSpan(self, row: int, column: int) -> int """
        return 0

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

    def dataChanged(self, *args, **kwargs): # real signature unknown
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

    def dragMoveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def drawFrame(self, *args, **kwargs): # real signature unknown
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

    def gridStyle(self): # real signature unknown; restored from __doc__
        """ gridStyle(self) -> Qt.PenStyle """
        pass

    def hideColumn(self, column): # real signature unknown; restored from __doc__
        """ hideColumn(self, column: int) """
        pass

    def hideEvent(self, *args, **kwargs): # real signature unknown
        pass

    def hideRow(self, row): # real signature unknown; restored from __doc__
        """ hideRow(self, row: int) """
        pass

    def horizontalHeader(self): # real signature unknown; restored from __doc__
        """ horizontalHeader(self) -> Optional[QHeaderView] """
        pass

    def horizontalOffset(self): # real signature unknown; restored from __doc__
        """ horizontalOffset(self) -> int """
        return 0

    def horizontalScrollbarAction(self, action): # real signature unknown; restored from __doc__
        """ horizontalScrollbarAction(self, action: int) """
        pass

    def horizontalScrollbarValueChanged(self, *args, **kwargs): # real signature unknown
        pass

    def indexAt(self, p): # real signature unknown; restored from __doc__
        """ indexAt(self, p: QPoint) -> QModelIndex """
        pass

    def initPainter(self, *args, **kwargs): # real signature unknown
        pass

    def initStyleOption(self, *args, **kwargs): # real signature unknown
        pass

    def inputMethodEvent(self, *args, **kwargs): # real signature unknown
        pass

    def isColumnHidden(self, column): # real signature unknown; restored from __doc__
        """ isColumnHidden(self, column: int) -> bool """
        return False

    def isCornerButtonEnabled(self): # real signature unknown; restored from __doc__
        """ isCornerButtonEnabled(self) -> bool """
        return False

    def isIndexHidden(self, index): # real signature unknown; restored from __doc__
        """ isIndexHidden(self, index: QModelIndex) -> bool """
        return False

    def isRowHidden(self, row): # real signature unknown; restored from __doc__
        """ isRowHidden(self, row: int) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def isSortingEnabled(self): # real signature unknown; restored from __doc__
        """ isSortingEnabled(self) -> bool """
        return False

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

    def resizeColumnsToContents(self): # real signature unknown; restored from __doc__
        """ resizeColumnsToContents(self) """
        pass

    def resizeColumnToContents(self, column): # real signature unknown; restored from __doc__
        """ resizeColumnToContents(self, column: int) """
        pass

    def resizeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def resizeRowsToContents(self): # real signature unknown; restored from __doc__
        """ resizeRowsToContents(self) """
        pass

    def resizeRowToContents(self, row): # real signature unknown; restored from __doc__
        """ resizeRowToContents(self, row: int) """
        pass

    def rowAt(self, y): # real signature unknown; restored from __doc__
        """ rowAt(self, y: int) -> int """
        return 0

    def rowCountChanged(self, oldCount, newCount): # real signature unknown; restored from __doc__
        """ rowCountChanged(self, oldCount: int, newCount: int) """
        pass

    def rowHeight(self, row): # real signature unknown; restored from __doc__
        """ rowHeight(self, row: int) -> int """
        return 0

    def rowMoved(self, row, oldIndex, newIndex): # real signature unknown; restored from __doc__
        """ rowMoved(self, row: int, oldIndex: int, newIndex: int) """
        pass

    def rowResized(self, row, oldHeight, newHeight): # real signature unknown; restored from __doc__
        """ rowResized(self, row: int, oldHeight: int, newHeight: int) """
        pass

    def rowsAboutToBeRemoved(self, *args, **kwargs): # real signature unknown
        pass

    def rowsInserted(self, *args, **kwargs): # real signature unknown
        pass

    def rowSpan(self, row, column): # real signature unknown; restored from __doc__
        """ rowSpan(self, row: int, column: int) -> int """
        return 0

    def rowViewportPosition(self, row): # real signature unknown; restored from __doc__
        """ rowViewportPosition(self, row: int) -> int """
        return 0

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

    def selectColumn(self, column): # real signature unknown; restored from __doc__
        """ selectColumn(self, column: int) """
        pass

    def selectedIndexes(self): # real signature unknown; restored from __doc__
        """ selectedIndexes(self) -> List[QModelIndex] """
        return []

    def selectionChanged(self, selected, deselected): # real signature unknown; restored from __doc__
        """ selectionChanged(self, selected: QItemSelection, deselected: QItemSelection) """
        pass

    def selectionCommand(self, *args, **kwargs): # real signature unknown
        pass

    def selectRow(self, row): # real signature unknown; restored from __doc__
        """ selectRow(self, row: int) """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setColumnHidden(self, column, hide): # real signature unknown; restored from __doc__
        """ setColumnHidden(self, column: int, hide: bool) """
        pass

    def setColumnWidth(self, column, width): # real signature unknown; restored from __doc__
        """ setColumnWidth(self, column: int, width: int) """
        pass

    def setCornerButtonEnabled(self, enable): # real signature unknown; restored from __doc__
        """ setCornerButtonEnabled(self, enable: bool) """
        pass

    def setDirtyRegion(self, *args, **kwargs): # real signature unknown
        pass

    def setGridStyle(self, style): # real signature unknown; restored from __doc__
        """ setGridStyle(self, style: Qt.PenStyle) """
        pass

    def setHorizontalHeader(self, header, QHeaderView=None): # real signature unknown; restored from __doc__
        """ setHorizontalHeader(self, header: Optional[QHeaderView]) """
        pass

    def setModel(self, model, QAbstractItemModel=None): # real signature unknown; restored from __doc__
        """ setModel(self, model: Optional[QAbstractItemModel]) """
        pass

    def setRootIndex(self, index): # real signature unknown; restored from __doc__
        """ setRootIndex(self, index: QModelIndex) """
        pass

    def setRowHeight(self, row, height): # real signature unknown; restored from __doc__
        """ setRowHeight(self, row: int, height: int) """
        pass

    def setRowHidden(self, row, hide): # real signature unknown; restored from __doc__
        """ setRowHidden(self, row: int, hide: bool) """
        pass

    def setSelection(self, rect, command, QItemSelectionModel_SelectionFlags=None, QItemSelectionModel_SelectionFlag=None): # real signature unknown; restored from __doc__
        """ setSelection(self, rect: QRect, command: Union[QItemSelectionModel.SelectionFlags, QItemSelectionModel.SelectionFlag]) """
        pass

    def setSelectionModel(self, selectionModel, QItemSelectionModel=None): # real signature unknown; restored from __doc__
        """ setSelectionModel(self, selectionModel: Optional[QItemSelectionModel]) """
        pass

    def setShowGrid(self, show): # real signature unknown; restored from __doc__
        """ setShowGrid(self, show: bool) """
        pass

    def setSortingEnabled(self, enable): # real signature unknown; restored from __doc__
        """ setSortingEnabled(self, enable: bool) """
        pass

    def setSpan(self, row, column, rowSpan, columnSpan): # real signature unknown; restored from __doc__
        """ setSpan(self, row: int, column: int, rowSpan: int, columnSpan: int) """
        pass

    def setState(self, *args, **kwargs): # real signature unknown
        pass

    def setVerticalHeader(self, header, QHeaderView=None): # real signature unknown; restored from __doc__
        """ setVerticalHeader(self, header: Optional[QHeaderView]) """
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

    def showGrid(self): # real signature unknown; restored from __doc__
        """ showGrid(self) -> bool """
        return False

    def showRow(self, row): # real signature unknown; restored from __doc__
        """ showRow(self, row: int) """
        pass

    def sizeHintForColumn(self, column): # real signature unknown; restored from __doc__
        """ sizeHintForColumn(self, column: int) -> int """
        return 0

    def sizeHintForRow(self, row): # real signature unknown; restored from __doc__
        """ sizeHintForRow(self, row: int) -> int """
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

    def updateEditorData(self, *args, **kwargs): # real signature unknown
        pass

    def updateEditorGeometries(self, *args, **kwargs): # real signature unknown
        pass

    def updateGeometries(self): # real signature unknown; restored from __doc__
        """ updateGeometries(self) """
        pass

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

    def verticalHeader(self): # real signature unknown; restored from __doc__
        """ verticalHeader(self) -> Optional[QHeaderView] """
        pass

    def verticalOffset(self): # real signature unknown; restored from __doc__
        """ verticalOffset(self) -> int """
        return 0

    def verticalScrollbarAction(self, action): # real signature unknown; restored from __doc__
        """ verticalScrollbarAction(self, action: int) """
        pass

    def verticalScrollbarValueChanged(self, *args, **kwargs): # real signature unknown
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

    def wheelEvent(self, *args, **kwargs): # real signature unknown
        pass

    def wordWrap(self): # real signature unknown; restored from __doc__
        """ wordWrap(self) -> bool """
        return False

    def __init__(self, parent, QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass


