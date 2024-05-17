# encoding: utf-8
# module PyQt5.QtWidgets
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


from .QTreeView import QTreeView

class QTreeWidget(QTreeView):
    """ QTreeWidget(parent: Optional[QWidget] = None) """
    def actionEvent(self, *args, **kwargs): # real signature unknown
        pass

    def addTopLevelItem(self, item, QTreeWidgetItem=None): # real signature unknown; restored from __doc__
        """ addTopLevelItem(self, item: Optional[QTreeWidgetItem]) """
        pass

    def addTopLevelItems(self, items, QTreeWidgetItem=None): # real signature unknown; restored from __doc__
        """ addTopLevelItems(self, items: Iterable[QTreeWidgetItem]) """
        pass

    def changeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def closeEditor(self, *args, **kwargs): # real signature unknown
        pass

    def closeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def closePersistentEditor(self, item, QTreeWidgetItem=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ closePersistentEditor(self, item: Optional[QTreeWidgetItem], column: int = 0) """
        pass

    def collapseItem(self, item, QTreeWidgetItem=None): # real signature unknown; restored from __doc__
        """ collapseItem(self, item: Optional[QTreeWidgetItem]) """
        pass

    def columnCount(self): # real signature unknown; restored from __doc__
        """ columnCount(self) -> int """
        return 0

    def columnCountChanged(self, *args, **kwargs): # real signature unknown
        pass

    def columnMoved(self, *args, **kwargs): # real signature unknown
        pass

    def columnResized(self, *args, **kwargs): # real signature unknown
        pass

    def commitData(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def contextMenuEvent(self, *args, **kwargs): # real signature unknown
        pass

    def create(self, *args, **kwargs): # real signature unknown
        pass

    def currentChanged(self, *args, **kwargs): # real signature unknown
        pass

    def currentColumn(self): # real signature unknown; restored from __doc__
        """ currentColumn(self) -> int """
        return 0

    def currentItem(self): # real signature unknown; restored from __doc__
        """ currentItem(self) -> Optional[QTreeWidgetItem] """
        pass

    def currentItemChanged(self, *args, **kwargs): # real signature unknown
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

    def customEvent(self, *args, **kwargs): # real signature unknown
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

    def drawBranches(self, *args, **kwargs): # real signature unknown
        pass

    def drawFrame(self, *args, **kwargs): # real signature unknown
        pass

    def drawRow(self, *args, **kwargs): # real signature unknown
        pass

    def drawTree(self, *args, **kwargs): # real signature unknown
        pass

    def dropEvent(self, event, QDropEvent=None): # real signature unknown; restored from __doc__
        """ dropEvent(self, event: Optional[QDropEvent]) """
        pass

    def dropIndicatorPosition(self, *args, **kwargs): # real signature unknown
        pass

    def dropMimeData(self, parent, QTreeWidgetItem=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ dropMimeData(self, parent: Optional[QTreeWidgetItem], index: int, data: Optional[QMimeData], action: Qt.DropAction) -> bool """
        pass

    def edit(self, *args, **kwargs): # real signature unknown
        pass

    def editItem(self, item, QTreeWidgetItem=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ editItem(self, item: Optional[QTreeWidgetItem], column: int = 0) """
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

    def expandItem(self, item, QTreeWidgetItem=None): # real signature unknown; restored from __doc__
        """ expandItem(self, item: Optional[QTreeWidgetItem]) """
        pass

    def findItems(self, text, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ findItems(self, text: Optional[str], flags: Union[Qt.MatchFlags, Qt.MatchFlag], column: int = 0) -> List[QTreeWidgetItem] """
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

    def headerItem(self): # real signature unknown; restored from __doc__
        """ headerItem(self) -> Optional[QTreeWidgetItem] """
        pass

    def hideEvent(self, *args, **kwargs): # real signature unknown
        pass

    def horizontalOffset(self, *args, **kwargs): # real signature unknown
        pass

    def horizontalScrollbarAction(self, *args, **kwargs): # real signature unknown
        pass

    def horizontalScrollbarValueChanged(self, *args, **kwargs): # real signature unknown
        pass

    def indexFromItem(self, item, QTreeWidgetItem=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ indexFromItem(self, item: Optional[QTreeWidgetItem], column: int = 0) -> QModelIndex """
        pass

    def indexOfTopLevelItem(self, item, QTreeWidgetItem=None): # real signature unknown; restored from __doc__
        """ indexOfTopLevelItem(self, item: Optional[QTreeWidgetItem]) -> int """
        return 0

    def indexRowSizeHint(self, *args, **kwargs): # real signature unknown
        pass

    def initPainter(self, *args, **kwargs): # real signature unknown
        pass

    def initStyleOption(self, *args, **kwargs): # real signature unknown
        pass

    def inputMethodEvent(self, *args, **kwargs): # real signature unknown
        pass

    def insertTopLevelItem(self, index, item, QTreeWidgetItem=None): # real signature unknown; restored from __doc__
        """ insertTopLevelItem(self, index: int, item: Optional[QTreeWidgetItem]) """
        pass

    def insertTopLevelItems(self, index, items, QTreeWidgetItem=None): # real signature unknown; restored from __doc__
        """ insertTopLevelItems(self, index: int, items: Iterable[QTreeWidgetItem]) """
        pass

    def invisibleRootItem(self): # real signature unknown; restored from __doc__
        """ invisibleRootItem(self) -> Optional[QTreeWidgetItem] """
        pass

    def isFirstItemColumnSpanned(self, item, QTreeWidgetItem=None): # real signature unknown; restored from __doc__
        """ isFirstItemColumnSpanned(self, item: Optional[QTreeWidgetItem]) -> bool """
        return False

    def isIndexHidden(self, *args, **kwargs): # real signature unknown
        pass

    def isPersistentEditorOpen(self, item, QTreeWidgetItem=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ isPersistentEditorOpen(self, item: Optional[QTreeWidgetItem], column: int = 0) -> bool """
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def itemAbove(self, item, QTreeWidgetItem=None): # real signature unknown; restored from __doc__
        """ itemAbove(self, item: Optional[QTreeWidgetItem]) -> Optional[QTreeWidgetItem] """
        pass

    def itemActivated(self, *args, **kwargs): # real signature unknown
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

    def itemAt(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        itemAt(self, p: QPoint) -> Optional[QTreeWidgetItem]
        itemAt(self, ax: int, ay: int) -> Optional[QTreeWidgetItem]
        """
        pass

    def itemBelow(self, item, QTreeWidgetItem=None): # real signature unknown; restored from __doc__
        """ itemBelow(self, item: Optional[QTreeWidgetItem]) -> Optional[QTreeWidgetItem] """
        pass

    def itemChanged(self, *args, **kwargs): # real signature unknown
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

    def itemClicked(self, *args, **kwargs): # real signature unknown
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

    def itemCollapsed(self, *args, **kwargs): # real signature unknown
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

    def itemDoubleClicked(self, *args, **kwargs): # real signature unknown
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

    def itemEntered(self, *args, **kwargs): # real signature unknown
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

    def itemExpanded(self, *args, **kwargs): # real signature unknown
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

    def itemFromIndex(self, index): # real signature unknown; restored from __doc__
        """ itemFromIndex(self, index: QModelIndex) -> Optional[QTreeWidgetItem] """
        pass

    def itemPressed(self, *args, **kwargs): # real signature unknown
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

    def itemSelectionChanged(self, *args, **kwargs): # real signature unknown
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

    def itemWidget(self, item, QTreeWidgetItem=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ itemWidget(self, item: Optional[QTreeWidgetItem], column: int) -> Optional[QWidget] """
        pass

    def keyPressEvent(self, *args, **kwargs): # real signature unknown
        pass

    def keyReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def leaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def metric(self, *args, **kwargs): # real signature unknown
        pass

    def mimeData(self, items, QTreeWidgetItem=None): # real signature unknown; restored from __doc__
        """ mimeData(self, items: Iterable[QTreeWidgetItem]) -> Optional[QMimeData] """
        pass

    def mimeTypes(self): # real signature unknown; restored from __doc__
        """ mimeTypes(self) -> List[str] """
        return []

    def mouseDoubleClickEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mouseMoveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mousePressEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mouseReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def moveCursor(self, *args, **kwargs): # real signature unknown
        pass

    def moveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def nativeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def openPersistentEditor(self, item, QTreeWidgetItem=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ openPersistentEditor(self, item: Optional[QTreeWidgetItem], column: int = 0) """
        pass

    def paintEvent(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def reexpand(self, *args, **kwargs): # real signature unknown
        pass

    def removeItemWidget(self, item, QTreeWidgetItem=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ removeItemWidget(self, item: Optional[QTreeWidgetItem], column: int) """
        pass

    def resizeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def rowHeight(self, *args, **kwargs): # real signature unknown
        pass

    def rowsAboutToBeRemoved(self, *args, **kwargs): # real signature unknown
        pass

    def rowsInserted(self, *args, **kwargs): # real signature unknown
        pass

    def rowsRemoved(self, *args, **kwargs): # real signature unknown
        pass

    def scheduleDelayedItemsLayout(self, *args, **kwargs): # real signature unknown
        pass

    def scrollContentsBy(self, *args, **kwargs): # real signature unknown
        pass

    def scrollDirtyRegion(self, *args, **kwargs): # real signature unknown
        pass

    def scrollToItem(self, item, QTreeWidgetItem=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ scrollToItem(self, item: Optional[QTreeWidgetItem], hint: QAbstractItemView.ScrollHint = QAbstractItemView.EnsureVisible) """
        pass

    def selectedIndexes(self, *args, **kwargs): # real signature unknown
        pass

    def selectedItems(self): # real signature unknown; restored from __doc__
        """ selectedItems(self) -> List[QTreeWidgetItem] """
        return []

    def selectionChanged(self, *args, **kwargs): # real signature unknown
        pass

    def selectionCommand(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setColumnCount(self, columns): # real signature unknown; restored from __doc__
        """ setColumnCount(self, columns: int) """
        pass

    def setCurrentItem(self, item, QTreeWidgetItem=None, *args=None, **kwargs=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setCurrentItem(self, item: Optional[QTreeWidgetItem])
        setCurrentItem(self, item: Optional[QTreeWidgetItem], column: int)
        setCurrentItem(self, item: Optional[QTreeWidgetItem], column: int, command: Union[QItemSelectionModel.SelectionFlags, QItemSelectionModel.SelectionFlag])
        """
        pass

    def setDirtyRegion(self, *args, **kwargs): # real signature unknown
        pass

    def setFirstItemColumnSpanned(self, item, QTreeWidgetItem=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setFirstItemColumnSpanned(self, item: Optional[QTreeWidgetItem], span: bool) """
        pass

    def setHeaderItem(self, item, QTreeWidgetItem=None): # real signature unknown; restored from __doc__
        """ setHeaderItem(self, item: Optional[QTreeWidgetItem]) """
        pass

    def setHeaderLabel(self, alabel, p_str=None): # real signature unknown; restored from __doc__
        """ setHeaderLabel(self, alabel: Optional[str]) """
        pass

    def setHeaderLabels(self, labels, Optional=None, p_str=None): # real signature unknown; restored from __doc__
        """ setHeaderLabels(self, labels: Iterable[Optional[str]]) """
        pass

    def setItemWidget(self, item, QTreeWidgetItem=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setItemWidget(self, item: Optional[QTreeWidgetItem], column: int, widget: Optional[QWidget]) """
        pass

    def setModel(self, *args, **kwargs): # real signature unknown
        pass

    def setSelection(self, *args, **kwargs): # real signature unknown
        pass

    def setSelectionModel(self, selectionModel, QItemSelectionModel=None): # real signature unknown; restored from __doc__
        """ setSelectionModel(self, selectionModel: Optional[QItemSelectionModel]) """
        pass

    def setState(self, *args, **kwargs): # real signature unknown
        pass

    def setViewportMargins(self, *args, **kwargs): # real signature unknown
        pass

    def sharedPainter(self, *args, **kwargs): # real signature unknown
        pass

    def showEvent(self, *args, **kwargs): # real signature unknown
        pass

    def sizeHintForColumn(self, *args, **kwargs): # real signature unknown
        pass

    def sortColumn(self): # real signature unknown; restored from __doc__
        """ sortColumn(self) -> int """
        return 0

    def sortItems(self, column, order): # real signature unknown; restored from __doc__
        """ sortItems(self, column: int, order: Qt.SortOrder) """
        pass

    def startDrag(self, *args, **kwargs): # real signature unknown
        pass

    def state(self, *args, **kwargs): # real signature unknown
        pass

    def supportedDropActions(self): # real signature unknown; restored from __doc__
        """ supportedDropActions(self) -> Qt.DropActions """
        pass

    def tabletEvent(self, *args, **kwargs): # real signature unknown
        pass

    def takeTopLevelItem(self, index): # real signature unknown; restored from __doc__
        """ takeTopLevelItem(self, index: int) -> Optional[QTreeWidgetItem] """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def topLevelItem(self, index): # real signature unknown; restored from __doc__
        """ topLevelItem(self, index: int) -> Optional[QTreeWidgetItem] """
        pass

    def topLevelItemCount(self): # real signature unknown; restored from __doc__
        """ topLevelItemCount(self) -> int """
        return 0

    def updateEditorData(self, *args, **kwargs): # real signature unknown
        pass

    def updateEditorGeometries(self, *args, **kwargs): # real signature unknown
        pass

    def updateGeometries(self, *args, **kwargs): # real signature unknown
        pass

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

    def verticalOffset(self, *args, **kwargs): # real signature unknown
        pass

    def verticalScrollbarAction(self, *args, **kwargs): # real signature unknown
        pass

    def verticalScrollbarValueChanged(self, *args, **kwargs): # real signature unknown
        pass

    def viewOptions(self, *args, **kwargs): # real signature unknown
        pass

    def viewportEvent(self, *args, **kwargs): # real signature unknown
        pass

    def viewportMargins(self, *args, **kwargs): # real signature unknown
        pass

    def viewportSizeHint(self, *args, **kwargs): # real signature unknown
        pass

    def visualItemRect(self, item, QTreeWidgetItem=None): # real signature unknown; restored from __doc__
        """ visualItemRect(self, item: Optional[QTreeWidgetItem]) -> QRect """
        pass

    def visualRegionForSelection(self, *args, **kwargs): # real signature unknown
        pass

    def wheelEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent, QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass


