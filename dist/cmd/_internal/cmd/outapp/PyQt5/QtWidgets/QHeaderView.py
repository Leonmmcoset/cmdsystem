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

class QHeaderView(QAbstractItemView):
    """ QHeaderView(orientation: Qt.Orientation, parent: Optional[QWidget] = None) """
    def actionEvent(self, *args, **kwargs): # real signature unknown
        pass

    def cascadingSectionResizes(self): # real signature unknown; restored from __doc__
        """ cascadingSectionResizes(self) -> bool """
        return False

    def changeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
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

    def count(self): # real signature unknown; restored from __doc__
        """ count(self) -> int """
        return 0

    def create(self, *args, **kwargs): # real signature unknown
        pass

    def currentChanged(self, current, old): # real signature unknown; restored from __doc__
        """ currentChanged(self, current: QModelIndex, old: QModelIndex) """
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dataChanged(self, topLeft, bottomRight, roles, p_int=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ dataChanged(self, topLeft: QModelIndex, bottomRight: QModelIndex, roles: Iterable[int] = []) """
        pass

    def defaultAlignment(self): # real signature unknown; restored from __doc__
        """ defaultAlignment(self) -> Qt.Alignment """
        pass

    def defaultSectionSize(self): # real signature unknown; restored from __doc__
        """ defaultSectionSize(self) -> int """
        return 0

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

    def event(self, e, QEvent=None): # real signature unknown; restored from __doc__
        """ event(self, e: Optional[QEvent]) -> bool """
        return False

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

    def geometriesChanged(self, *args, **kwargs): # real signature unknown
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

    def headerDataChanged(self, orientation, logicalFirst, logicalLast): # real signature unknown; restored from __doc__
        """ headerDataChanged(self, orientation: Qt.Orientation, logicalFirst: int, logicalLast: int) """
        pass

    def hiddenSectionCount(self): # real signature unknown; restored from __doc__
        """ hiddenSectionCount(self) -> int """
        return 0

    def hideEvent(self, *args, **kwargs): # real signature unknown
        pass

    def hideSection(self, alogicalIndex): # real signature unknown; restored from __doc__
        """ hideSection(self, alogicalIndex: int) """
        pass

    def highlightSections(self): # real signature unknown; restored from __doc__
        """ highlightSections(self) -> bool """
        return False

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

    def initialize(self): # real signature unknown; restored from __doc__
        """ initialize(self) """
        pass

    def initializeSections(self, start=None, end=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        initializeSections(self)
        initializeSections(self, start: int, end: int)
        """
        pass

    def initPainter(self, *args, **kwargs): # real signature unknown
        pass

    def initStyleOption(self, option, QStyleOptionHeader=None): # real signature unknown; restored from __doc__
        """ initStyleOption(self, option: Optional[QStyleOptionHeader]) """
        pass

    def inputMethodEvent(self, *args, **kwargs): # real signature unknown
        pass

    def isFirstSectionMovable(self): # real signature unknown; restored from __doc__
        """ isFirstSectionMovable(self) -> bool """
        return False

    def isIndexHidden(self, index): # real signature unknown; restored from __doc__
        """ isIndexHidden(self, index: QModelIndex) -> bool """
        return False

    def isSectionHidden(self, logicalIndex): # real signature unknown; restored from __doc__
        """ isSectionHidden(self, logicalIndex: int) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def isSortIndicatorShown(self): # real signature unknown; restored from __doc__
        """ isSortIndicatorShown(self) -> bool """
        return False

    def keyPressEvent(self, *args, **kwargs): # real signature unknown
        pass

    def keyReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def leaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def length(self): # real signature unknown; restored from __doc__
        """ length(self) -> int """
        return 0

    def logicalIndex(self, visualIndex): # real signature unknown; restored from __doc__
        """ logicalIndex(self, visualIndex: int) -> int """
        return 0

    def logicalIndexAt(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        logicalIndexAt(self, position: int) -> int
        logicalIndexAt(self, ax: int, ay: int) -> int
        logicalIndexAt(self, apos: QPoint) -> int
        """
        return 0

    def maximumSectionSize(self): # real signature unknown; restored from __doc__
        """ maximumSectionSize(self) -> int """
        return 0

    def metric(self, *args, **kwargs): # real signature unknown
        pass

    def minimumSectionSize(self): # real signature unknown; restored from __doc__
        """ minimumSectionSize(self) -> int """
        return 0

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

    def moveCursor(self, a0, a1, Qt_KeyboardModifiers=None, Qt_KeyboardModifier=None): # real signature unknown; restored from __doc__
        """ moveCursor(self, a0: QAbstractItemView.CursorAction, a1: Union[Qt.KeyboardModifiers, Qt.KeyboardModifier]) -> QModelIndex """
        pass

    def moveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def moveSection(self, from_, to): # real signature unknown; restored from __doc__
        """ moveSection(self, from_: int, to: int) """
        pass

    def nativeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def offset(self): # real signature unknown; restored from __doc__
        """ offset(self) -> int """
        return 0

    def orientation(self): # real signature unknown; restored from __doc__
        """ orientation(self) -> Qt.Orientation """
        pass

    def paintEvent(self, e, QPaintEvent=None): # real signature unknown; restored from __doc__
        """ paintEvent(self, e: Optional[QPaintEvent]) """
        pass

    def paintSection(self, painter, QPainter=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ paintSection(self, painter: Optional[QPainter], rect: QRect, logicalIndex: int) """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def reset(self): # real signature unknown; restored from __doc__
        """ reset(self) """
        pass

    def resetDefaultSectionSize(self): # real signature unknown; restored from __doc__
        """ resetDefaultSectionSize(self) """
        pass

    def resizeContentsPrecision(self): # real signature unknown; restored from __doc__
        """ resizeContentsPrecision(self) -> int """
        return 0

    def resizeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def resizeSection(self, logicalIndex, size): # real signature unknown; restored from __doc__
        """ resizeSection(self, logicalIndex: int, size: int) """
        pass

    def resizeSections(self, mode=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        resizeSections(self)
        resizeSections(self, mode: QHeaderView.ResizeMode)
        """
        pass

    def restoreState(self, state, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ restoreState(self, state: Union[QByteArray, bytes, bytearray]) -> bool """
        return False

    def rowsAboutToBeRemoved(self, *args, **kwargs): # real signature unknown
        pass

    def rowsInserted(self, parent, start, end): # real signature unknown; restored from __doc__
        """ rowsInserted(self, parent: QModelIndex, start: int, end: int) """
        pass

    def saveState(self): # real signature unknown; restored from __doc__
        """ saveState(self) -> QByteArray """
        pass

    def scheduleDelayedItemsLayout(self, *args, **kwargs): # real signature unknown
        pass

    def scrollContentsBy(self, dx, dy): # real signature unknown; restored from __doc__
        """ scrollContentsBy(self, dx: int, dy: int) """
        pass

    def scrollDirtyRegion(self, *args, **kwargs): # real signature unknown
        pass

    def scrollTo(self, index, hint): # real signature unknown; restored from __doc__
        """ scrollTo(self, index: QModelIndex, hint: QAbstractItemView.ScrollHint) """
        pass

    def sectionClicked(self, *args, **kwargs): # real signature unknown
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

    def sectionCountChanged(self, *args, **kwargs): # real signature unknown
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

    def sectionDoubleClicked(self, *args, **kwargs): # real signature unknown
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

    def sectionEntered(self, *args, **kwargs): # real signature unknown
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

    def sectionHandleDoubleClicked(self, *args, **kwargs): # real signature unknown
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

    def sectionMoved(self, *args, **kwargs): # real signature unknown
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

    def sectionPosition(self, logicalIndex): # real signature unknown; restored from __doc__
        """ sectionPosition(self, logicalIndex: int) -> int """
        return 0

    def sectionPressed(self, *args, **kwargs): # real signature unknown
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

    def sectionResized(self, *args, **kwargs): # real signature unknown
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

    def sectionResizeMode(self, logicalIndex): # real signature unknown; restored from __doc__
        """ sectionResizeMode(self, logicalIndex: int) -> QHeaderView.ResizeMode """
        pass

    def sectionsAboutToBeRemoved(self, parent, logicalFirst, logicalLast): # real signature unknown; restored from __doc__
        """ sectionsAboutToBeRemoved(self, parent: QModelIndex, logicalFirst: int, logicalLast: int) """
        pass

    def sectionsClickable(self): # real signature unknown; restored from __doc__
        """ sectionsClickable(self) -> bool """
        return False

    def sectionsHidden(self): # real signature unknown; restored from __doc__
        """ sectionsHidden(self) -> bool """
        return False

    def sectionsInserted(self, parent, logicalFirst, logicalLast): # real signature unknown; restored from __doc__
        """ sectionsInserted(self, parent: QModelIndex, logicalFirst: int, logicalLast: int) """
        pass

    def sectionSize(self, logicalIndex): # real signature unknown; restored from __doc__
        """ sectionSize(self, logicalIndex: int) -> int """
        return 0

    def sectionSizeFromContents(self, logicalIndex): # real signature unknown; restored from __doc__
        """ sectionSizeFromContents(self, logicalIndex: int) -> QSize """
        pass

    def sectionSizeHint(self, logicalIndex): # real signature unknown; restored from __doc__
        """ sectionSizeHint(self, logicalIndex: int) -> int """
        return 0

    def sectionsMovable(self): # real signature unknown; restored from __doc__
        """ sectionsMovable(self) -> bool """
        return False

    def sectionsMoved(self): # real signature unknown; restored from __doc__
        """ sectionsMoved(self) -> bool """
        return False

    def sectionViewportPosition(self, logicalIndex): # real signature unknown; restored from __doc__
        """ sectionViewportPosition(self, logicalIndex: int) -> int """
        return 0

    def selectedIndexes(self, *args, **kwargs): # real signature unknown
        pass

    def selectionChanged(self, *args, **kwargs): # real signature unknown
        pass

    def selectionCommand(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setCascadingSectionResizes(self, enable): # real signature unknown; restored from __doc__
        """ setCascadingSectionResizes(self, enable: bool) """
        pass

    def setDefaultAlignment(self, alignment, Qt_Alignment=None, Qt_AlignmentFlag=None): # real signature unknown; restored from __doc__
        """ setDefaultAlignment(self, alignment: Union[Qt.Alignment, Qt.AlignmentFlag]) """
        pass

    def setDefaultSectionSize(self, size): # real signature unknown; restored from __doc__
        """ setDefaultSectionSize(self, size: int) """
        pass

    def setDirtyRegion(self, *args, **kwargs): # real signature unknown
        pass

    def setFirstSectionMovable(self, movable): # real signature unknown; restored from __doc__
        """ setFirstSectionMovable(self, movable: bool) """
        pass

    def setHighlightSections(self, highlight): # real signature unknown; restored from __doc__
        """ setHighlightSections(self, highlight: bool) """
        pass

    def setMaximumSectionSize(self, size): # real signature unknown; restored from __doc__
        """ setMaximumSectionSize(self, size: int) """
        pass

    def setMinimumSectionSize(self, size): # real signature unknown; restored from __doc__
        """ setMinimumSectionSize(self, size: int) """
        pass

    def setModel(self, model, QAbstractItemModel=None): # real signature unknown; restored from __doc__
        """ setModel(self, model: Optional[QAbstractItemModel]) """
        pass

    def setOffset(self, offset): # real signature unknown; restored from __doc__
        """ setOffset(self, offset: int) """
        pass

    def setOffsetToLastSection(self): # real signature unknown; restored from __doc__
        """ setOffsetToLastSection(self) """
        pass

    def setOffsetToSectionPosition(self, visualIndex): # real signature unknown; restored from __doc__
        """ setOffsetToSectionPosition(self, visualIndex: int) """
        pass

    def setResizeContentsPrecision(self, precision): # real signature unknown; restored from __doc__
        """ setResizeContentsPrecision(self, precision: int) """
        pass

    def setSectionHidden(self, logicalIndex, hide): # real signature unknown; restored from __doc__
        """ setSectionHidden(self, logicalIndex: int, hide: bool) """
        pass

    def setSectionResizeMode(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setSectionResizeMode(self, logicalIndex: int, mode: QHeaderView.ResizeMode)
        setSectionResizeMode(self, mode: QHeaderView.ResizeMode)
        """
        pass

    def setSectionsClickable(self, clickable): # real signature unknown; restored from __doc__
        """ setSectionsClickable(self, clickable: bool) """
        pass

    def setSectionsMovable(self, movable): # real signature unknown; restored from __doc__
        """ setSectionsMovable(self, movable: bool) """
        pass

    def setSelection(self, rect, flags, QItemSelectionModel_SelectionFlags=None, QItemSelectionModel_SelectionFlag=None): # real signature unknown; restored from __doc__
        """ setSelection(self, rect: QRect, flags: Union[QItemSelectionModel.SelectionFlags, QItemSelectionModel.SelectionFlag]) """
        pass

    def setSortIndicator(self, logicalIndex, order): # real signature unknown; restored from __doc__
        """ setSortIndicator(self, logicalIndex: int, order: Qt.SortOrder) """
        pass

    def setSortIndicatorShown(self, show): # real signature unknown; restored from __doc__
        """ setSortIndicatorShown(self, show: bool) """
        pass

    def setState(self, *args, **kwargs): # real signature unknown
        pass

    def setStretchLastSection(self, stretch): # real signature unknown; restored from __doc__
        """ setStretchLastSection(self, stretch: bool) """
        pass

    def setViewportMargins(self, *args, **kwargs): # real signature unknown
        pass

    def setVisible(self, v): # real signature unknown; restored from __doc__
        """ setVisible(self, v: bool) """
        pass

    def sharedPainter(self, *args, **kwargs): # real signature unknown
        pass

    def showEvent(self, *args, **kwargs): # real signature unknown
        pass

    def showSection(self, alogicalIndex): # real signature unknown; restored from __doc__
        """ showSection(self, alogicalIndex: int) """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> QSize """
        pass

    def sortIndicatorChanged(self, *args, **kwargs): # real signature unknown
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

    def sortIndicatorOrder(self): # real signature unknown; restored from __doc__
        """ sortIndicatorOrder(self) -> Qt.SortOrder """
        pass

    def sortIndicatorSection(self): # real signature unknown; restored from __doc__
        """ sortIndicatorSection(self) -> int """
        return 0

    def startDrag(self, *args, **kwargs): # real signature unknown
        pass

    def state(self, *args, **kwargs): # real signature unknown
        pass

    def stretchLastSection(self): # real signature unknown; restored from __doc__
        """ stretchLastSection(self) -> bool """
        return False

    def stretchSectionCount(self): # real signature unknown; restored from __doc__
        """ stretchSectionCount(self) -> int """
        return 0

    def swapSections(self, first, second): # real signature unknown; restored from __doc__
        """ swapSections(self, first: int, second: int) """
        pass

    def tabletEvent(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
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

    def updateSection(self, logicalIndex): # real signature unknown; restored from __doc__
        """ updateSection(self, logicalIndex: int) """
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

    def viewportEvent(self, e, QEvent=None): # real signature unknown; restored from __doc__
        """ viewportEvent(self, e: Optional[QEvent]) -> bool """
        return False

    def viewportMargins(self, *args, **kwargs): # real signature unknown
        pass

    def viewportSizeHint(self, *args, **kwargs): # real signature unknown
        pass

    def visualIndex(self, logicalIndex): # real signature unknown; restored from __doc__
        """ visualIndex(self, logicalIndex: int) -> int """
        return 0

    def visualIndexAt(self, position): # real signature unknown; restored from __doc__
        """ visualIndexAt(self, position: int) -> int """
        return 0

    def visualRect(self, index): # real signature unknown; restored from __doc__
        """ visualRect(self, index: QModelIndex) -> QRect """
        pass

    def visualRegionForSelection(self, selection): # real signature unknown; restored from __doc__
        """ visualRegionForSelection(self, selection: QItemSelection) -> QRegion """
        pass

    def wheelEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, orientation, parent, QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    Custom = 2
    Fixed = 2
    Interactive = 0
    ResizeToContents = 3
    Stretch = 1


