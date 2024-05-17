# encoding: utf-8
# module PyQt5.QtWidgets
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


from .QAbstractScrollArea import QAbstractScrollArea

class QAbstractItemView(QAbstractScrollArea):
    """ QAbstractItemView(parent: Optional[QWidget] = None) """
    def actionEvent(self, *args, **kwargs): # real signature unknown
        pass

    def activated(self, *args, **kwargs): # real signature unknown
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

    def alternatingRowColors(self): # real signature unknown; restored from __doc__
        """ alternatingRowColors(self) -> bool """
        return False

    def autoScrollMargin(self): # real signature unknown; restored from __doc__
        """ autoScrollMargin(self) -> int """
        return 0

    def changeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def clearSelection(self): # real signature unknown; restored from __doc__
        """ clearSelection(self) """
        pass

    def clicked(self, *args, **kwargs): # real signature unknown
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

    def closeEditor(self, editor, QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ closeEditor(self, editor: Optional[QWidget], hint: QAbstractItemDelegate.EndEditHint) """
        pass

    def closeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def closePersistentEditor(self, index): # real signature unknown; restored from __doc__
        """ closePersistentEditor(self, index: QModelIndex) """
        pass

    def commitData(self, editor, QWidget=None): # real signature unknown; restored from __doc__
        """ commitData(self, editor: Optional[QWidget]) """
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

    def currentIndex(self): # real signature unknown; restored from __doc__
        """ currentIndex(self) -> QModelIndex """
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dataChanged(self, topLeft, bottomRight, roles, p_int=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ dataChanged(self, topLeft: QModelIndex, bottomRight: QModelIndex, roles: Iterable[int] = []) """
        pass

    def defaultDropAction(self): # real signature unknown; restored from __doc__
        """ defaultDropAction(self) -> Qt.DropAction """
        pass

    def destroy(self, *args, **kwargs): # real signature unknown
        pass

    def dirtyRegionOffset(self): # real signature unknown; restored from __doc__
        """ dirtyRegionOffset(self) -> QPoint """
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def doubleClicked(self, *args, **kwargs): # real signature unknown
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

    def dragDropMode(self): # real signature unknown; restored from __doc__
        """ dragDropMode(self) -> QAbstractItemView.DragDropMode """
        pass

    def dragDropOverwriteMode(self): # real signature unknown; restored from __doc__
        """ dragDropOverwriteMode(self) -> bool """
        return False

    def dragEnabled(self): # real signature unknown; restored from __doc__
        """ dragEnabled(self) -> bool """
        return False

    def dragEnterEvent(self, e, QDragEnterEvent=None): # real signature unknown; restored from __doc__
        """ dragEnterEvent(self, e: Optional[QDragEnterEvent]) """
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

    def dropIndicatorPosition(self): # real signature unknown; restored from __doc__
        """ dropIndicatorPosition(self) -> QAbstractItemView.DropIndicatorPosition """
        pass

    def edit(self, index, trigger=None, event=None, QEvent=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        edit(self, index: QModelIndex)
        edit(self, index: QModelIndex, trigger: QAbstractItemView.EditTrigger, event: Optional[QEvent]) -> bool
        """
        return False

    def editorDestroyed(self, editor, QObject=None): # real signature unknown; restored from __doc__
        """ editorDestroyed(self, editor: Optional[QObject]) """
        pass

    def editTriggers(self): # real signature unknown; restored from __doc__
        """ editTriggers(self) -> QAbstractItemView.EditTriggers """
        pass

    def entered(self, *args, **kwargs): # real signature unknown
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

    def enterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, event, QEvent=None): # real signature unknown; restored from __doc__
        """ event(self, event: Optional[QEvent]) -> bool """
        return False

    def eventFilter(self, p_object, QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ eventFilter(self, object: Optional[QObject], event: Optional[QEvent]) -> bool """
        pass

    def executeDelayedItemsLayout(self): # real signature unknown; restored from __doc__
        """ executeDelayedItemsLayout(self) """
        pass

    def focusInEvent(self, e, QFocusEvent=None): # real signature unknown; restored from __doc__
        """ focusInEvent(self, e: Optional[QFocusEvent]) """
        pass

    def focusNextChild(self, *args, **kwargs): # real signature unknown
        pass

    def focusNextPrevChild(self, next): # real signature unknown; restored from __doc__
        """ focusNextPrevChild(self, next: bool) -> bool """
        return False

    def focusOutEvent(self, e, QFocusEvent=None): # real signature unknown; restored from __doc__
        """ focusOutEvent(self, e: Optional[QFocusEvent]) """
        pass

    def focusPreviousChild(self, *args, **kwargs): # real signature unknown
        pass

    def hasAutoScroll(self): # real signature unknown; restored from __doc__
        """ hasAutoScroll(self) -> bool """
        return False

    def hideEvent(self, *args, **kwargs): # real signature unknown
        pass

    def horizontalOffset(self): # real signature unknown; restored from __doc__
        """ horizontalOffset(self) -> int """
        return 0

    def horizontalScrollbarAction(self, action): # real signature unknown; restored from __doc__
        """ horizontalScrollbarAction(self, action: int) """
        pass

    def horizontalScrollbarValueChanged(self, value): # real signature unknown; restored from __doc__
        """ horizontalScrollbarValueChanged(self, value: int) """
        pass

    def horizontalScrollMode(self): # real signature unknown; restored from __doc__
        """ horizontalScrollMode(self) -> QAbstractItemView.ScrollMode """
        pass

    def iconSize(self): # real signature unknown; restored from __doc__
        """ iconSize(self) -> QSize """
        pass

    def iconSizeChanged(self, *args, **kwargs): # real signature unknown
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

    def indexAt(self, p): # real signature unknown; restored from __doc__
        """ indexAt(self, p: QPoint) -> QModelIndex """
        pass

    def indexWidget(self, index): # real signature unknown; restored from __doc__
        """ indexWidget(self, index: QModelIndex) -> Optional[QWidget] """
        pass

    def initPainter(self, *args, **kwargs): # real signature unknown
        pass

    def initStyleOption(self, *args, **kwargs): # real signature unknown
        pass

    def inputMethodEvent(self, event, QInputMethodEvent=None): # real signature unknown; restored from __doc__
        """ inputMethodEvent(self, event: Optional[QInputMethodEvent]) """
        pass

    def inputMethodQuery(self, query): # real signature unknown; restored from __doc__
        """ inputMethodQuery(self, query: Qt.InputMethodQuery) -> Any """
        pass

    def isIndexHidden(self, index): # real signature unknown; restored from __doc__
        """ isIndexHidden(self, index: QModelIndex) -> bool """
        return False

    def isPersistentEditorOpen(self, index): # real signature unknown; restored from __doc__
        """ isPersistentEditorOpen(self, index: QModelIndex) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def itemDelegate(self, index=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        itemDelegate(self) -> Optional[QAbstractItemDelegate]
        itemDelegate(self, index: QModelIndex) -> Optional[QAbstractItemDelegate]
        """
        pass

    def itemDelegateForColumn(self, column): # real signature unknown; restored from __doc__
        """ itemDelegateForColumn(self, column: int) -> Optional[QAbstractItemDelegate] """
        pass

    def itemDelegateForRow(self, row): # real signature unknown; restored from __doc__
        """ itemDelegateForRow(self, row: int) -> Optional[QAbstractItemDelegate] """
        pass

    def keyboardSearch(self, search, p_str=None): # real signature unknown; restored from __doc__
        """ keyboardSearch(self, search: Optional[str]) """
        pass

    def keyPressEvent(self, e, QKeyEvent=None): # real signature unknown; restored from __doc__
        """ keyPressEvent(self, e: Optional[QKeyEvent]) """
        pass

    def keyReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def leaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def metric(self, *args, **kwargs): # real signature unknown
        pass

    def model(self): # real signature unknown; restored from __doc__
        """ model(self) -> Optional[QAbstractItemModel] """
        pass

    def mouseDoubleClickEvent(self, e, QMouseEvent=None): # real signature unknown; restored from __doc__
        """ mouseDoubleClickEvent(self, e: Optional[QMouseEvent]) """
        pass

    def mouseMoveEvent(self, e, QMouseEvent=None): # real signature unknown; restored from __doc__
        """ mouseMoveEvent(self, e: Optional[QMouseEvent]) """
        pass

    def mousePressEvent(self, e, QMouseEvent=None): # real signature unknown; restored from __doc__
        """ mousePressEvent(self, e: Optional[QMouseEvent]) """
        pass

    def mouseReleaseEvent(self, e, QMouseEvent=None): # real signature unknown; restored from __doc__
        """ mouseReleaseEvent(self, e: Optional[QMouseEvent]) """
        pass

    def moveCursor(self, cursorAction, modifiers, Qt_KeyboardModifiers=None, Qt_KeyboardModifier=None): # real signature unknown; restored from __doc__
        """ moveCursor(self, cursorAction: QAbstractItemView.CursorAction, modifiers: Union[Qt.KeyboardModifiers, Qt.KeyboardModifier]) -> QModelIndex """
        pass

    def moveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def nativeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def openPersistentEditor(self, index): # real signature unknown; restored from __doc__
        """ openPersistentEditor(self, index: QModelIndex) """
        pass

    def paintEvent(self, *args, **kwargs): # real signature unknown
        pass

    def pressed(self, *args, **kwargs): # real signature unknown
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

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def reset(self): # real signature unknown; restored from __doc__
        """ reset(self) """
        pass

    def resetHorizontalScrollMode(self): # real signature unknown; restored from __doc__
        """ resetHorizontalScrollMode(self) """
        pass

    def resetVerticalScrollMode(self): # real signature unknown; restored from __doc__
        """ resetVerticalScrollMode(self) """
        pass

    def resizeEvent(self, e, QResizeEvent=None): # real signature unknown; restored from __doc__
        """ resizeEvent(self, e: Optional[QResizeEvent]) """
        pass

    def rootIndex(self): # real signature unknown; restored from __doc__
        """ rootIndex(self) -> QModelIndex """
        pass

    def rowsAboutToBeRemoved(self, parent, start, end): # real signature unknown; restored from __doc__
        """ rowsAboutToBeRemoved(self, parent: QModelIndex, start: int, end: int) """
        pass

    def rowsInserted(self, parent, start, end): # real signature unknown; restored from __doc__
        """ rowsInserted(self, parent: QModelIndex, start: int, end: int) """
        pass

    def scheduleDelayedItemsLayout(self): # real signature unknown; restored from __doc__
        """ scheduleDelayedItemsLayout(self) """
        pass

    def scrollContentsBy(self, *args, **kwargs): # real signature unknown
        pass

    def scrollDirtyRegion(self, dx, dy): # real signature unknown; restored from __doc__
        """ scrollDirtyRegion(self, dx: int, dy: int) """
        pass

    def scrollTo(self, index, hint=None): # real signature unknown; restored from __doc__
        """ scrollTo(self, index: QModelIndex, hint: QAbstractItemView.ScrollHint = QAbstractItemView.EnsureVisible) """
        pass

    def scrollToBottom(self): # real signature unknown; restored from __doc__
        """ scrollToBottom(self) """
        pass

    def scrollToTop(self): # real signature unknown; restored from __doc__
        """ scrollToTop(self) """
        pass

    def selectAll(self): # real signature unknown; restored from __doc__
        """ selectAll(self) """
        pass

    def selectedIndexes(self): # real signature unknown; restored from __doc__
        """ selectedIndexes(self) -> List[QModelIndex] """
        return []

    def selectionBehavior(self): # real signature unknown; restored from __doc__
        """ selectionBehavior(self) -> QAbstractItemView.SelectionBehavior """
        pass

    def selectionChanged(self, selected, deselected): # real signature unknown; restored from __doc__
        """ selectionChanged(self, selected: QItemSelection, deselected: QItemSelection) """
        pass

    def selectionCommand(self, index, event, QEvent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ selectionCommand(self, index: QModelIndex, event: Optional[QEvent] = None) -> QItemSelectionModel.SelectionFlags """
        pass

    def selectionMode(self): # real signature unknown; restored from __doc__
        """ selectionMode(self) -> QAbstractItemView.SelectionMode """
        pass

    def selectionModel(self): # real signature unknown; restored from __doc__
        """ selectionModel(self) -> Optional[QItemSelectionModel] """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setAlternatingRowColors(self, enable): # real signature unknown; restored from __doc__
        """ setAlternatingRowColors(self, enable: bool) """
        pass

    def setAutoScroll(self, enable): # real signature unknown; restored from __doc__
        """ setAutoScroll(self, enable: bool) """
        pass

    def setAutoScrollMargin(self, margin): # real signature unknown; restored from __doc__
        """ setAutoScrollMargin(self, margin: int) """
        pass

    def setCurrentIndex(self, index): # real signature unknown; restored from __doc__
        """ setCurrentIndex(self, index: QModelIndex) """
        pass

    def setDefaultDropAction(self, dropAction): # real signature unknown; restored from __doc__
        """ setDefaultDropAction(self, dropAction: Qt.DropAction) """
        pass

    def setDirtyRegion(self, region): # real signature unknown; restored from __doc__
        """ setDirtyRegion(self, region: QRegion) """
        pass

    def setDragDropMode(self, behavior): # real signature unknown; restored from __doc__
        """ setDragDropMode(self, behavior: QAbstractItemView.DragDropMode) """
        pass

    def setDragDropOverwriteMode(self, overwrite): # real signature unknown; restored from __doc__
        """ setDragDropOverwriteMode(self, overwrite: bool) """
        pass

    def setDragEnabled(self, enable): # real signature unknown; restored from __doc__
        """ setDragEnabled(self, enable: bool) """
        pass

    def setDropIndicatorShown(self, enable): # real signature unknown; restored from __doc__
        """ setDropIndicatorShown(self, enable: bool) """
        pass

    def setEditTriggers(self, triggers, QAbstractItemView_EditTriggers=None, QAbstractItemView_EditTrigger=None): # real signature unknown; restored from __doc__
        """ setEditTriggers(self, triggers: Union[QAbstractItemView.EditTriggers, QAbstractItemView.EditTrigger]) """
        pass

    def setHorizontalScrollMode(self, mode): # real signature unknown; restored from __doc__
        """ setHorizontalScrollMode(self, mode: QAbstractItemView.ScrollMode) """
        pass

    def setIconSize(self, size): # real signature unknown; restored from __doc__
        """ setIconSize(self, size: QSize) """
        pass

    def setIndexWidget(self, index, widget, QWidget=None): # real signature unknown; restored from __doc__
        """ setIndexWidget(self, index: QModelIndex, widget: Optional[QWidget]) """
        pass

    def setItemDelegate(self, delegate, QAbstractItemDelegate=None): # real signature unknown; restored from __doc__
        """ setItemDelegate(self, delegate: Optional[QAbstractItemDelegate]) """
        pass

    def setItemDelegateForColumn(self, column, delegate, QAbstractItemDelegate=None): # real signature unknown; restored from __doc__
        """ setItemDelegateForColumn(self, column: int, delegate: Optional[QAbstractItemDelegate]) """
        pass

    def setItemDelegateForRow(self, row, delegate, QAbstractItemDelegate=None): # real signature unknown; restored from __doc__
        """ setItemDelegateForRow(self, row: int, delegate: Optional[QAbstractItemDelegate]) """
        pass

    def setModel(self, model, QAbstractItemModel=None): # real signature unknown; restored from __doc__
        """ setModel(self, model: Optional[QAbstractItemModel]) """
        pass

    def setRootIndex(self, index): # real signature unknown; restored from __doc__
        """ setRootIndex(self, index: QModelIndex) """
        pass

    def setSelection(self, rect, command, QItemSelectionModel_SelectionFlags=None, QItemSelectionModel_SelectionFlag=None): # real signature unknown; restored from __doc__
        """ setSelection(self, rect: QRect, command: Union[QItemSelectionModel.SelectionFlags, QItemSelectionModel.SelectionFlag]) """
        pass

    def setSelectionBehavior(self, behavior): # real signature unknown; restored from __doc__
        """ setSelectionBehavior(self, behavior: QAbstractItemView.SelectionBehavior) """
        pass

    def setSelectionMode(self, mode): # real signature unknown; restored from __doc__
        """ setSelectionMode(self, mode: QAbstractItemView.SelectionMode) """
        pass

    def setSelectionModel(self, selectionModel, QItemSelectionModel=None): # real signature unknown; restored from __doc__
        """ setSelectionModel(self, selectionModel: Optional[QItemSelectionModel]) """
        pass

    def setState(self, state): # real signature unknown; restored from __doc__
        """ setState(self, state: QAbstractItemView.State) """
        pass

    def setTabKeyNavigation(self, enable): # real signature unknown; restored from __doc__
        """ setTabKeyNavigation(self, enable: bool) """
        pass

    def setTextElideMode(self, mode): # real signature unknown; restored from __doc__
        """ setTextElideMode(self, mode: Qt.TextElideMode) """
        pass

    def setVerticalScrollMode(self, mode): # real signature unknown; restored from __doc__
        """ setVerticalScrollMode(self, mode: QAbstractItemView.ScrollMode) """
        pass

    def setViewportMargins(self, *args, **kwargs): # real signature unknown
        pass

    def sharedPainter(self, *args, **kwargs): # real signature unknown
        pass

    def showDropIndicator(self): # real signature unknown; restored from __doc__
        """ showDropIndicator(self) -> bool """
        return False

    def showEvent(self, *args, **kwargs): # real signature unknown
        pass

    def sizeHintForColumn(self, column): # real signature unknown; restored from __doc__
        """ sizeHintForColumn(self, column: int) -> int """
        return 0

    def sizeHintForIndex(self, index): # real signature unknown; restored from __doc__
        """ sizeHintForIndex(self, index: QModelIndex) -> QSize """
        pass

    def sizeHintForRow(self, row): # real signature unknown; restored from __doc__
        """ sizeHintForRow(self, row: int) -> int """
        return 0

    def startDrag(self, supportedActions, Qt_DropActions=None, Qt_DropAction=None): # real signature unknown; restored from __doc__
        """ startDrag(self, supportedActions: Union[Qt.DropActions, Qt.DropAction]) """
        pass

    def state(self): # real signature unknown; restored from __doc__
        """ state(self) -> QAbstractItemView.State """
        pass

    def tabKeyNavigation(self): # real signature unknown; restored from __doc__
        """ tabKeyNavigation(self) -> bool """
        return False

    def tabletEvent(self, *args, **kwargs): # real signature unknown
        pass

    def textElideMode(self): # real signature unknown; restored from __doc__
        """ textElideMode(self) -> Qt.TextElideMode """
        pass

    def timerEvent(self, e, QTimerEvent=None): # real signature unknown; restored from __doc__
        """ timerEvent(self, e: Optional[QTimerEvent]) """
        pass

    def update(self, index=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        update(self)
        update(self, index: QModelIndex)
        """
        pass

    def updateEditorData(self): # real signature unknown; restored from __doc__
        """ updateEditorData(self) """
        pass

    def updateEditorGeometries(self): # real signature unknown; restored from __doc__
        """ updateEditorGeometries(self) """
        pass

    def updateGeometries(self): # real signature unknown; restored from __doc__
        """ updateGeometries(self) """
        pass

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

    def verticalOffset(self): # real signature unknown; restored from __doc__
        """ verticalOffset(self) -> int """
        return 0

    def verticalScrollbarAction(self, action): # real signature unknown; restored from __doc__
        """ verticalScrollbarAction(self, action: int) """
        pass

    def verticalScrollbarValueChanged(self, value): # real signature unknown; restored from __doc__
        """ verticalScrollbarValueChanged(self, value: int) """
        pass

    def verticalScrollMode(self): # real signature unknown; restored from __doc__
        """ verticalScrollMode(self) -> QAbstractItemView.ScrollMode """
        pass

    def viewOptions(self): # real signature unknown; restored from __doc__
        """ viewOptions(self) -> QStyleOptionViewItem """
        return QStyleOptionViewItem

    def viewportEntered(self, *args, **kwargs): # real signature unknown
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

    def viewportEvent(self, e, QEvent=None): # real signature unknown; restored from __doc__
        """ viewportEvent(self, e: Optional[QEvent]) -> bool """
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

    def __init__(self, parent, QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    AboveItem = 1
    AllEditTriggers = 31
    AnimatingState = 6
    AnyKeyPressed = 16
    BelowItem = 2
    CollapsingState = 5
    ContiguousSelection = 4
    CurrentChanged = 1
    DoubleClicked = 2
    DragDrop = 3
    DraggingState = 1
    DragOnly = 1
    DragSelectingState = 2
    DropOnly = 2
    EditingState = 3
    EditKeyPressed = 8
    EnsureVisible = 0
    ExpandingState = 4
    ExtendedSelection = 3
    InternalMove = 4
    MoveDown = 1
    MoveEnd = 5
    MoveHome = 4
    MoveLeft = 2
    MoveNext = 8
    MovePageDown = 7
    MovePageUp = 6
    MovePrevious = 9
    MoveRight = 3
    MoveUp = 0
    MultiSelection = 2
    NoDragDrop = 0
    NoEditTriggers = 0
    NoSelection = 0
    NoState = 0
    OnItem = 0
    OnViewport = 3
    PositionAtBottom = 2
    PositionAtCenter = 3
    PositionAtTop = 1
    ScrollPerItem = 0
    ScrollPerPixel = 1
    SelectColumns = 2
    SelectedClicked = 4
    SelectItems = 0
    SelectRows = 1
    SingleSelection = 1


