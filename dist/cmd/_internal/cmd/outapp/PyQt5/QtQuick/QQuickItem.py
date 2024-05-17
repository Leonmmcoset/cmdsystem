# encoding: utf-8
# module PyQt5.QtQuick
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtQuick.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import PyQt5.QtQml as __PyQt5_QtQml
import sip as __sip


class QQuickItem(__PyQt5_QtCore.QObject, __PyQt5_QtQml.QQmlParserStatus):
    """ QQuickItem(parent: Optional[QQuickItem] = None) """
    def acceptedMouseButtons(self): # real signature unknown; restored from __doc__
        """ acceptedMouseButtons(self) -> Qt.MouseButtons """
        pass

    def acceptHoverEvents(self): # real signature unknown; restored from __doc__
        """ acceptHoverEvents(self) -> bool """
        return False

    def acceptTouchEvents(self): # real signature unknown; restored from __doc__
        """ acceptTouchEvents(self) -> bool """
        return False

    def activeFocusOnTab(self): # real signature unknown; restored from __doc__
        """ activeFocusOnTab(self) -> bool """
        return False

    def antialiasing(self): # real signature unknown; restored from __doc__
        """ antialiasing(self) -> bool """
        return False

    def baselineOffset(self): # real signature unknown; restored from __doc__
        """ baselineOffset(self) -> float """
        return 0.0

    def childAt(self, x, y): # real signature unknown; restored from __doc__
        """ childAt(self, x: float, y: float) -> Optional[QQuickItem] """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def childItems(self): # real signature unknown; restored from __doc__
        """ childItems(self) -> List[QQuickItem] """
        return []

    def childMouseEventFilter(self, a0, QQuickItem=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ childMouseEventFilter(self, a0: Optional[QQuickItem], a1: Optional[QEvent]) -> bool """
        pass

    def childrenRect(self): # real signature unknown; restored from __doc__
        """ childrenRect(self) -> QRectF """
        pass

    def classBegin(self): # real signature unknown; restored from __doc__
        """ classBegin(self) """
        pass

    def clip(self): # real signature unknown; restored from __doc__
        """ clip(self) -> bool """
        return False

    def componentComplete(self): # real signature unknown; restored from __doc__
        """ componentComplete(self) """
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def containmentMask(self): # real signature unknown; restored from __doc__
        """ containmentMask(self) -> Optional[QObject] """
        pass

    def containmentMaskChanged(self, *args, **kwargs): # real signature unknown
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

    def contains(self, point, QPointF=None, QPoint=None): # real signature unknown; restored from __doc__
        """ contains(self, point: Union[QPointF, QPoint]) -> bool """
        return False

    def cursor(self): # real signature unknown; restored from __doc__
        """ cursor(self) -> QCursor """
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def dragEnterEvent(self, a0, QDragEnterEvent=None): # real signature unknown; restored from __doc__
        """ dragEnterEvent(self, a0: Optional[QDragEnterEvent]) """
        pass

    def dragLeaveEvent(self, a0, QDragLeaveEvent=None): # real signature unknown; restored from __doc__
        """ dragLeaveEvent(self, a0: Optional[QDragLeaveEvent]) """
        pass

    def dragMoveEvent(self, a0, QDragMoveEvent=None): # real signature unknown; restored from __doc__
        """ dragMoveEvent(self, a0: Optional[QDragMoveEvent]) """
        pass

    def dropEvent(self, a0, QDropEvent=None): # real signature unknown; restored from __doc__
        """ dropEvent(self, a0: Optional[QDropEvent]) """
        pass

    def event(self, a0, QEvent=None): # real signature unknown; restored from __doc__
        """ event(self, a0: Optional[QEvent]) -> bool """
        return False

    def filtersChildMouseEvents(self): # real signature unknown; restored from __doc__
        """ filtersChildMouseEvents(self) -> bool """
        return False

    def flags(self): # real signature unknown; restored from __doc__
        """ flags(self) -> QQuickItem.Flags """
        pass

    def focusInEvent(self, a0, QFocusEvent=None): # real signature unknown; restored from __doc__
        """ focusInEvent(self, a0: Optional[QFocusEvent]) """
        pass

    def focusOutEvent(self, a0, QFocusEvent=None): # real signature unknown; restored from __doc__
        """ focusOutEvent(self, a0: Optional[QFocusEvent]) """
        pass

    def forceActiveFocus(self, reason=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        forceActiveFocus(self)
        forceActiveFocus(self, reason: Qt.FocusReason)
        """
        pass

    def geometryChanged(self, newGeometry, oldGeometry): # real signature unknown; restored from __doc__
        """ geometryChanged(self, newGeometry: QRectF, oldGeometry: QRectF) """
        pass

    def grabMouse(self): # real signature unknown; restored from __doc__
        """ grabMouse(self) """
        pass

    def grabToImage(self, targetSize=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ grabToImage(self, targetSize: QSize = QSize()) -> Optional[QQuickItemGrabResult] """
        pass

    def grabTouchPoints(self, ids, p_int=None): # real signature unknown; restored from __doc__
        """ grabTouchPoints(self, ids: Iterable[int]) """
        pass

    def hasActiveFocus(self): # real signature unknown; restored from __doc__
        """ hasActiveFocus(self) -> bool """
        return False

    def hasFocus(self): # real signature unknown; restored from __doc__
        """ hasFocus(self) -> bool """
        return False

    def height(self): # real signature unknown; restored from __doc__
        """ height(self) -> float """
        return 0.0

    def heightValid(self): # real signature unknown; restored from __doc__
        """ heightValid(self) -> bool """
        return False

    def hoverEnterEvent(self, event, QHoverEvent=None): # real signature unknown; restored from __doc__
        """ hoverEnterEvent(self, event: Optional[QHoverEvent]) """
        pass

    def hoverLeaveEvent(self, event, QHoverEvent=None): # real signature unknown; restored from __doc__
        """ hoverLeaveEvent(self, event: Optional[QHoverEvent]) """
        pass

    def hoverMoveEvent(self, event, QHoverEvent=None): # real signature unknown; restored from __doc__
        """ hoverMoveEvent(self, event: Optional[QHoverEvent]) """
        pass

    def implicitHeight(self): # real signature unknown; restored from __doc__
        """ implicitHeight(self) -> float """
        return 0.0

    def implicitWidth(self): # real signature unknown; restored from __doc__
        """ implicitWidth(self) -> float """
        return 0.0

    def inputMethodEvent(self, a0, QInputMethodEvent=None): # real signature unknown; restored from __doc__
        """ inputMethodEvent(self, a0: Optional[QInputMethodEvent]) """
        pass

    def inputMethodQuery(self, query): # real signature unknown; restored from __doc__
        """ inputMethodQuery(self, query: Qt.InputMethodQuery) -> Any """
        pass

    def isAncestorOf(self, child, QQuickItem=None): # real signature unknown; restored from __doc__
        """ isAncestorOf(self, child: Optional[QQuickItem]) -> bool """
        return False

    def isComponentComplete(self): # real signature unknown; restored from __doc__
        """ isComponentComplete(self) -> bool """
        return False

    def isEnabled(self): # real signature unknown; restored from __doc__
        """ isEnabled(self) -> bool """
        return False

    def isFocusScope(self): # real signature unknown; restored from __doc__
        """ isFocusScope(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def isTextureProvider(self): # real signature unknown; restored from __doc__
        """ isTextureProvider(self) -> bool """
        return False

    def isVisible(self): # real signature unknown; restored from __doc__
        """ isVisible(self) -> bool """
        return False

    def itemChange(self, a0, a1): # real signature unknown; restored from __doc__
        """ itemChange(self, a0: QQuickItem.ItemChange, a1: QQuickItem.ItemChangeData) """
        pass

    def keepMouseGrab(self): # real signature unknown; restored from __doc__
        """ keepMouseGrab(self) -> bool """
        return False

    def keepTouchGrab(self): # real signature unknown; restored from __doc__
        """ keepTouchGrab(self) -> bool """
        return False

    def keyPressEvent(self, event, QKeyEvent=None): # real signature unknown; restored from __doc__
        """ keyPressEvent(self, event: Optional[QKeyEvent]) """
        pass

    def keyReleaseEvent(self, event, QKeyEvent=None): # real signature unknown; restored from __doc__
        """ keyReleaseEvent(self, event: Optional[QKeyEvent]) """
        pass

    def mapFromGlobal(self, point, QPointF=None, QPoint=None): # real signature unknown; restored from __doc__
        """ mapFromGlobal(self, point: Union[QPointF, QPoint]) -> QPointF """
        pass

    def mapFromItem(self, item, QQuickItem=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ mapFromItem(self, item: Optional[QQuickItem], point: Union[QPointF, QPoint]) -> QPointF """
        pass

    def mapFromScene(self, point, QPointF=None, QPoint=None): # real signature unknown; restored from __doc__
        """ mapFromScene(self, point: Union[QPointF, QPoint]) -> QPointF """
        pass

    def mapRectFromItem(self, item, QQuickItem=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ mapRectFromItem(self, item: Optional[QQuickItem], rect: QRectF) -> QRectF """
        pass

    def mapRectFromScene(self, rect): # real signature unknown; restored from __doc__
        """ mapRectFromScene(self, rect: QRectF) -> QRectF """
        pass

    def mapRectToItem(self, item, QQuickItem=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ mapRectToItem(self, item: Optional[QQuickItem], rect: QRectF) -> QRectF """
        pass

    def mapRectToScene(self, rect): # real signature unknown; restored from __doc__
        """ mapRectToScene(self, rect: QRectF) -> QRectF """
        pass

    def mapToGlobal(self, point, QPointF=None, QPoint=None): # real signature unknown; restored from __doc__
        """ mapToGlobal(self, point: Union[QPointF, QPoint]) -> QPointF """
        pass

    def mapToItem(self, item, QQuickItem=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ mapToItem(self, item: Optional[QQuickItem], point: Union[QPointF, QPoint]) -> QPointF """
        pass

    def mapToScene(self, point, QPointF=None, QPoint=None): # real signature unknown; restored from __doc__
        """ mapToScene(self, point: Union[QPointF, QPoint]) -> QPointF """
        pass

    def mouseDoubleClickEvent(self, event, QMouseEvent=None): # real signature unknown; restored from __doc__
        """ mouseDoubleClickEvent(self, event: Optional[QMouseEvent]) """
        pass

    def mouseMoveEvent(self, event, QMouseEvent=None): # real signature unknown; restored from __doc__
        """ mouseMoveEvent(self, event: Optional[QMouseEvent]) """
        pass

    def mousePressEvent(self, event, QMouseEvent=None): # real signature unknown; restored from __doc__
        """ mousePressEvent(self, event: Optional[QMouseEvent]) """
        pass

    def mouseReleaseEvent(self, event, QMouseEvent=None): # real signature unknown; restored from __doc__
        """ mouseReleaseEvent(self, event: Optional[QMouseEvent]) """
        pass

    def mouseUngrabEvent(self): # real signature unknown; restored from __doc__
        """ mouseUngrabEvent(self) """
        pass

    def nextItemInFocusChain(self, forward=True): # real signature unknown; restored from __doc__
        """ nextItemInFocusChain(self, forward: bool = True) -> Optional[QQuickItem] """
        pass

    def opacity(self): # real signature unknown; restored from __doc__
        """ opacity(self) -> float """
        return 0.0

    def parentItem(self): # real signature unknown; restored from __doc__
        """ parentItem(self) -> Optional[QQuickItem] """
        pass

    def polish(self): # real signature unknown; restored from __doc__
        """ polish(self) """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def releaseResources(self): # real signature unknown; restored from __doc__
        """ releaseResources(self) """
        pass

    def resetAntialiasing(self): # real signature unknown; restored from __doc__
        """ resetAntialiasing(self) """
        pass

    def resetHeight(self): # real signature unknown; restored from __doc__
        """ resetHeight(self) """
        pass

    def resetWidth(self): # real signature unknown; restored from __doc__
        """ resetWidth(self) """
        pass

    def rotation(self): # real signature unknown; restored from __doc__
        """ rotation(self) -> float """
        return 0.0

    def scale(self): # real signature unknown; restored from __doc__
        """ scale(self) -> float """
        return 0.0

    def scopedFocusItem(self): # real signature unknown; restored from __doc__
        """ scopedFocusItem(self) -> Optional[QQuickItem] """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setAcceptedMouseButtons(self, buttons, Qt_MouseButtons=None, Qt_MouseButton=None): # real signature unknown; restored from __doc__
        """ setAcceptedMouseButtons(self, buttons: Union[Qt.MouseButtons, Qt.MouseButton]) """
        pass

    def setAcceptHoverEvents(self, enabled): # real signature unknown; restored from __doc__
        """ setAcceptHoverEvents(self, enabled: bool) """
        pass

    def setAcceptTouchEvents(self, accept): # real signature unknown; restored from __doc__
        """ setAcceptTouchEvents(self, accept: bool) """
        pass

    def setActiveFocusOnTab(self, a0): # real signature unknown; restored from __doc__
        """ setActiveFocusOnTab(self, a0: bool) """
        pass

    def setAntialiasing(self, a0): # real signature unknown; restored from __doc__
        """ setAntialiasing(self, a0: bool) """
        pass

    def setBaselineOffset(self, a0): # real signature unknown; restored from __doc__
        """ setBaselineOffset(self, a0: float) """
        pass

    def setClip(self, a0): # real signature unknown; restored from __doc__
        """ setClip(self, a0: bool) """
        pass

    def setContainmentMask(self, mask, QObject=None): # real signature unknown; restored from __doc__
        """ setContainmentMask(self, mask: Optional[QObject]) """
        pass

    def setCursor(self, cursor, QCursor=None, Qt_CursorShape=None): # real signature unknown; restored from __doc__
        """ setCursor(self, cursor: Union[QCursor, Qt.CursorShape]) """
        pass

    def setEnabled(self, a0): # real signature unknown; restored from __doc__
        """ setEnabled(self, a0: bool) """
        pass

    def setFiltersChildMouseEvents(self, filter): # real signature unknown; restored from __doc__
        """ setFiltersChildMouseEvents(self, filter: bool) """
        pass

    def setFlag(self, flag, enabled=True): # real signature unknown; restored from __doc__
        """ setFlag(self, flag: QQuickItem.Flag, enabled: bool = True) """
        pass

    def setFlags(self, flags, QQuickItem_Flags=None, QQuickItem_Flag=None): # real signature unknown; restored from __doc__
        """ setFlags(self, flags: Union[QQuickItem.Flags, QQuickItem.Flag]) """
        pass

    def setFocus(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setFocus(self, a0: bool)
        setFocus(self, focus: bool, reason: Qt.FocusReason)
        """
        pass

    def setHeight(self, a0): # real signature unknown; restored from __doc__
        """ setHeight(self, a0: float) """
        pass

    def setImplicitHeight(self, a0): # real signature unknown; restored from __doc__
        """ setImplicitHeight(self, a0: float) """
        pass

    def setImplicitWidth(self, a0): # real signature unknown; restored from __doc__
        """ setImplicitWidth(self, a0: float) """
        pass

    def setKeepMouseGrab(self, a0): # real signature unknown; restored from __doc__
        """ setKeepMouseGrab(self, a0: bool) """
        pass

    def setKeepTouchGrab(self, a0): # real signature unknown; restored from __doc__
        """ setKeepTouchGrab(self, a0: bool) """
        pass

    def setOpacity(self, a0): # real signature unknown; restored from __doc__
        """ setOpacity(self, a0: float) """
        pass

    def setParentItem(self, parent, QQuickItem=None): # real signature unknown; restored from __doc__
        """ setParentItem(self, parent: Optional[QQuickItem]) """
        pass

    def setRotation(self, a0): # real signature unknown; restored from __doc__
        """ setRotation(self, a0: float) """
        pass

    def setScale(self, a0): # real signature unknown; restored from __doc__
        """ setScale(self, a0: float) """
        pass

    def setSmooth(self, a0): # real signature unknown; restored from __doc__
        """ setSmooth(self, a0: bool) """
        pass

    def setState(self, a0, p_str=None): # real signature unknown; restored from __doc__
        """ setState(self, a0: Optional[str]) """
        pass

    def setTransformOrigin(self, a0): # real signature unknown; restored from __doc__
        """ setTransformOrigin(self, a0: QQuickItem.TransformOrigin) """
        pass

    def setVisible(self, a0): # real signature unknown; restored from __doc__
        """ setVisible(self, a0: bool) """
        pass

    def setWidth(self, a0): # real signature unknown; restored from __doc__
        """ setWidth(self, a0: float) """
        pass

    def setX(self, a0): # real signature unknown; restored from __doc__
        """ setX(self, a0: float) """
        pass

    def setY(self, a0): # real signature unknown; restored from __doc__
        """ setY(self, a0: float) """
        pass

    def setZ(self, a0): # real signature unknown; restored from __doc__
        """ setZ(self, a0: float) """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ size(self) -> QSizeF """
        pass

    def smooth(self): # real signature unknown; restored from __doc__
        """ smooth(self) -> bool """
        return False

    def stackAfter(self, a0, QQuickItem=None): # real signature unknown; restored from __doc__
        """ stackAfter(self, a0: Optional[QQuickItem]) """
        pass

    def stackBefore(self, a0, QQuickItem=None): # real signature unknown; restored from __doc__
        """ stackBefore(self, a0: Optional[QQuickItem]) """
        pass

    def state(self): # real signature unknown; restored from __doc__
        """ state(self) -> str """
        return ""

    def textureProvider(self): # real signature unknown; restored from __doc__
        """ textureProvider(self) -> Optional[QSGTextureProvider] """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def touchEvent(self, event, QTouchEvent=None): # real signature unknown; restored from __doc__
        """ touchEvent(self, event: Optional[QTouchEvent]) """
        pass

    def touchUngrabEvent(self): # real signature unknown; restored from __doc__
        """ touchUngrabEvent(self) """
        pass

    def transformOrigin(self): # real signature unknown; restored from __doc__
        """ transformOrigin(self) -> QQuickItem.TransformOrigin """
        pass

    def ungrabMouse(self): # real signature unknown; restored from __doc__
        """ ungrabMouse(self) """
        pass

    def ungrabTouchPoints(self): # real signature unknown; restored from __doc__
        """ ungrabTouchPoints(self) """
        pass

    def unsetCursor(self): # real signature unknown; restored from __doc__
        """ unsetCursor(self) """
        pass

    def update(self): # real signature unknown; restored from __doc__
        """ update(self) """
        pass

    def updateInputMethod(self, queries, Qt_InputMethodQueries=None, Qt_InputMethodQuery=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ updateInputMethod(self, queries: Union[Qt.InputMethodQueries, Qt.InputMethodQuery] = Qt.InputMethodQuery.ImQueryInput) """
        pass

    def updatePaintNode(self, a0, QSGNode=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ updatePaintNode(self, a0: Optional[QSGNode], a1: Optional[QQuickItem.UpdatePaintNodeData]) -> Optional[QSGNode] """
        pass

    def updatePolish(self): # real signature unknown; restored from __doc__
        """ updatePolish(self) """
        pass

    def wheelEvent(self, event, QWheelEvent=None): # real signature unknown; restored from __doc__
        """ wheelEvent(self, event: Optional[QWheelEvent]) """
        pass

    def width(self): # real signature unknown; restored from __doc__
        """ width(self) -> float """
        return 0.0

    def widthValid(self): # real signature unknown; restored from __doc__
        """ widthValid(self) -> bool """
        return False

    def window(self): # real signature unknown; restored from __doc__
        """ window(self) -> Optional[QQuickWindow] """
        pass

    def windowChanged(self, *args, **kwargs): # real signature unknown
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

    def x(self): # real signature unknown; restored from __doc__
        """ x(self) -> float """
        return 0.0

    def y(self): # real signature unknown; restored from __doc__
        """ y(self) -> float """
        return 0.0

    def z(self): # real signature unknown; restored from __doc__
        """ z(self) -> float """
        return 0.0

    def __init__(self, parent, QQuickItem=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    Bottom = 7
    BottomLeft = 6
    BottomRight = 8
    Center = 4
    ItemAcceptsDrops = 16
    ItemAcceptsInputMethod = 2
    ItemActiveFocusHasChanged = 6
    ItemAntialiasingHasChanged = 8
    ItemChildAddedChange = 0
    ItemChildRemovedChange = 1
    ItemClipsChildrenToShape = 1
    ItemDevicePixelRatioHasChanged = 9
    ItemEnabledHasChanged = 10
    ItemHasContents = 8
    ItemIsFocusScope = 4
    ItemOpacityHasChanged = 5
    ItemParentHasChanged = 4
    ItemRotationHasChanged = 7
    ItemSceneChange = 2
    ItemVisibleHasChanged = 3
    Left = 3
    Right = 5
    Top = 1
    TopLeft = 0
    TopRight = 2


