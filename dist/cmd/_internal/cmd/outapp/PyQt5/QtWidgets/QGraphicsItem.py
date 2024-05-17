# encoding: utf-8
# module PyQt5.QtWidgets
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


class QGraphicsItem(__sip.wrapper):
    """ QGraphicsItem(parent: Optional[QGraphicsItem] = None) """
    def acceptDrops(self): # real signature unknown; restored from __doc__
        """ acceptDrops(self) -> bool """
        return False

    def acceptedMouseButtons(self): # real signature unknown; restored from __doc__
        """ acceptedMouseButtons(self) -> Qt.MouseButtons """
        pass

    def acceptHoverEvents(self): # real signature unknown; restored from __doc__
        """ acceptHoverEvents(self) -> bool """
        return False

    def acceptTouchEvents(self): # real signature unknown; restored from __doc__
        """ acceptTouchEvents(self) -> bool """
        return False

    def advance(self, phase): # real signature unknown; restored from __doc__
        """ advance(self, phase: int) """
        pass

    def boundingRect(self): # real signature unknown; restored from __doc__
        """ boundingRect(self) -> QRectF """
        pass

    def boundingRegion(self, itemToDeviceTransform): # real signature unknown; restored from __doc__
        """ boundingRegion(self, itemToDeviceTransform: QTransform) -> QRegion """
        pass

    def boundingRegionGranularity(self): # real signature unknown; restored from __doc__
        """ boundingRegionGranularity(self) -> float """
        return 0.0

    def cacheMode(self): # real signature unknown; restored from __doc__
        """ cacheMode(self) -> QGraphicsItem.CacheMode """
        pass

    def childItems(self): # real signature unknown; restored from __doc__
        """ childItems(self) -> List[QGraphicsItem] """
        return []

    def childrenBoundingRect(self): # real signature unknown; restored from __doc__
        """ childrenBoundingRect(self) -> QRectF """
        pass

    def clearFocus(self): # real signature unknown; restored from __doc__
        """ clearFocus(self) """
        pass

    def clipPath(self): # real signature unknown; restored from __doc__
        """ clipPath(self) -> QPainterPath """
        pass

    def collidesWithItem(self, other, QGraphicsItem=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ collidesWithItem(self, other: Optional[QGraphicsItem], mode: Qt.ItemSelectionMode = Qt.IntersectsItemShape) -> bool """
        pass

    def collidesWithPath(self, path, mode=None): # real signature unknown; restored from __doc__
        """ collidesWithPath(self, path: QPainterPath, mode: Qt.ItemSelectionMode = Qt.IntersectsItemShape) -> bool """
        return False

    def collidingItems(self, mode=None): # real signature unknown; restored from __doc__
        """ collidingItems(self, mode: Qt.ItemSelectionMode = Qt.IntersectsItemShape) -> List[QGraphicsItem] """
        return []

    def commonAncestorItem(self, other, QGraphicsItem=None): # real signature unknown; restored from __doc__
        """ commonAncestorItem(self, other: Optional[QGraphicsItem]) -> Optional[QGraphicsItem] """
        pass

    def contains(self, point, QPointF=None, QPoint=None): # real signature unknown; restored from __doc__
        """ contains(self, point: Union[QPointF, QPoint]) -> bool """
        return False

    def contextMenuEvent(self, event, QGraphicsSceneContextMenuEvent=None): # real signature unknown; restored from __doc__
        """ contextMenuEvent(self, event: Optional[QGraphicsSceneContextMenuEvent]) """
        pass

    def cursor(self): # real signature unknown; restored from __doc__
        """ cursor(self) -> QCursor """
        pass

    def data(self, key): # real signature unknown; restored from __doc__
        """ data(self, key: int) -> Any """
        pass

    def deviceTransform(self, viewportTransform): # real signature unknown; restored from __doc__
        """ deviceTransform(self, viewportTransform: QTransform) -> QTransform """
        pass

    def dragEnterEvent(self, event, QGraphicsSceneDragDropEvent=None): # real signature unknown; restored from __doc__
        """ dragEnterEvent(self, event: Optional[QGraphicsSceneDragDropEvent]) """
        pass

    def dragLeaveEvent(self, event, QGraphicsSceneDragDropEvent=None): # real signature unknown; restored from __doc__
        """ dragLeaveEvent(self, event: Optional[QGraphicsSceneDragDropEvent]) """
        pass

    def dragMoveEvent(self, event, QGraphicsSceneDragDropEvent=None): # real signature unknown; restored from __doc__
        """ dragMoveEvent(self, event: Optional[QGraphicsSceneDragDropEvent]) """
        pass

    def dropEvent(self, event, QGraphicsSceneDragDropEvent=None): # real signature unknown; restored from __doc__
        """ dropEvent(self, event: Optional[QGraphicsSceneDragDropEvent]) """
        pass

    def effectiveOpacity(self): # real signature unknown; restored from __doc__
        """ effectiveOpacity(self) -> float """
        return 0.0

    def ensureVisible(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        ensureVisible(self, rect: QRectF = QRectF(), xMargin: int = 50, yMargin: int = 50)
        ensureVisible(self, x: float, y: float, w: float, h: float, xMargin: int = 50, yMargin: int = 50)
        """
        pass

    def filtersChildEvents(self): # real signature unknown; restored from __doc__
        """ filtersChildEvents(self) -> bool """
        return False

    def flags(self): # real signature unknown; restored from __doc__
        """ flags(self) -> QGraphicsItem.GraphicsItemFlags """
        pass

    def focusInEvent(self, event, QFocusEvent=None): # real signature unknown; restored from __doc__
        """ focusInEvent(self, event: Optional[QFocusEvent]) """
        pass

    def focusItem(self): # real signature unknown; restored from __doc__
        """ focusItem(self) -> Optional[QGraphicsItem] """
        pass

    def focusOutEvent(self, event, QFocusEvent=None): # real signature unknown; restored from __doc__
        """ focusOutEvent(self, event: Optional[QFocusEvent]) """
        pass

    def focusProxy(self): # real signature unknown; restored from __doc__
        """ focusProxy(self) -> Optional[QGraphicsItem] """
        pass

    def grabKeyboard(self): # real signature unknown; restored from __doc__
        """ grabKeyboard(self) """
        pass

    def grabMouse(self): # real signature unknown; restored from __doc__
        """ grabMouse(self) """
        pass

    def graphicsEffect(self): # real signature unknown; restored from __doc__
        """ graphicsEffect(self) -> Optional[QGraphicsEffect] """
        pass

    def group(self): # real signature unknown; restored from __doc__
        """ group(self) -> Optional[QGraphicsItemGroup] """
        pass

    def hasCursor(self): # real signature unknown; restored from __doc__
        """ hasCursor(self) -> bool """
        return False

    def hasFocus(self): # real signature unknown; restored from __doc__
        """ hasFocus(self) -> bool """
        return False

    def hide(self): # real signature unknown; restored from __doc__
        """ hide(self) """
        pass

    def hoverEnterEvent(self, event, QGraphicsSceneHoverEvent=None): # real signature unknown; restored from __doc__
        """ hoverEnterEvent(self, event: Optional[QGraphicsSceneHoverEvent]) """
        pass

    def hoverLeaveEvent(self, event, QGraphicsSceneHoverEvent=None): # real signature unknown; restored from __doc__
        """ hoverLeaveEvent(self, event: Optional[QGraphicsSceneHoverEvent]) """
        pass

    def hoverMoveEvent(self, event, QGraphicsSceneHoverEvent=None): # real signature unknown; restored from __doc__
        """ hoverMoveEvent(self, event: Optional[QGraphicsSceneHoverEvent]) """
        pass

    def inputMethodEvent(self, event, QInputMethodEvent=None): # real signature unknown; restored from __doc__
        """ inputMethodEvent(self, event: Optional[QInputMethodEvent]) """
        pass

    def inputMethodHints(self): # real signature unknown; restored from __doc__
        """ inputMethodHints(self) -> Qt.InputMethodHints """
        pass

    def inputMethodQuery(self, query): # real signature unknown; restored from __doc__
        """ inputMethodQuery(self, query: Qt.InputMethodQuery) -> Any """
        pass

    def installSceneEventFilter(self, filterItem, QGraphicsItem=None): # real signature unknown; restored from __doc__
        """ installSceneEventFilter(self, filterItem: Optional[QGraphicsItem]) """
        pass

    def isActive(self): # real signature unknown; restored from __doc__
        """ isActive(self) -> bool """
        return False

    def isAncestorOf(self, child, QGraphicsItem=None): # real signature unknown; restored from __doc__
        """ isAncestorOf(self, child: Optional[QGraphicsItem]) -> bool """
        return False

    def isBlockedByModalPanel(self): # real signature unknown; restored from __doc__
        """ isBlockedByModalPanel(self) -> (bool, Optional[QGraphicsItem]) """
        pass

    def isClipped(self): # real signature unknown; restored from __doc__
        """ isClipped(self) -> bool """
        return False

    def isEnabled(self): # real signature unknown; restored from __doc__
        """ isEnabled(self) -> bool """
        return False

    def isObscured(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        isObscured(self, rect: QRectF = QRectF()) -> bool
        isObscured(self, ax: float, ay: float, w: float, h: float) -> bool
        """
        return False

    def isObscuredBy(self, item, QGraphicsItem=None): # real signature unknown; restored from __doc__
        """ isObscuredBy(self, item: Optional[QGraphicsItem]) -> bool """
        return False

    def isPanel(self): # real signature unknown; restored from __doc__
        """ isPanel(self) -> bool """
        return False

    def isSelected(self): # real signature unknown; restored from __doc__
        """ isSelected(self) -> bool """
        return False

    def isUnderMouse(self): # real signature unknown; restored from __doc__
        """ isUnderMouse(self) -> bool """
        return False

    def isVisible(self): # real signature unknown; restored from __doc__
        """ isVisible(self) -> bool """
        return False

    def isVisibleTo(self, parent, QGraphicsItem=None): # real signature unknown; restored from __doc__
        """ isVisibleTo(self, parent: Optional[QGraphicsItem]) -> bool """
        return False

    def isWidget(self): # real signature unknown; restored from __doc__
        """ isWidget(self) -> bool """
        return False

    def isWindow(self): # real signature unknown; restored from __doc__
        """ isWindow(self) -> bool """
        return False

    def itemChange(self, change, value): # real signature unknown; restored from __doc__
        """ itemChange(self, change: QGraphicsItem.GraphicsItemChange, value: Any) -> Any """
        pass

    def itemTransform(self, other, QGraphicsItem=None): # real signature unknown; restored from __doc__
        """ itemTransform(self, other: Optional[QGraphicsItem]) -> (QTransform, Optional[bool]) """
        pass

    def keyPressEvent(self, event, QKeyEvent=None): # real signature unknown; restored from __doc__
        """ keyPressEvent(self, event: Optional[QKeyEvent]) """
        pass

    def keyReleaseEvent(self, event, QKeyEvent=None): # real signature unknown; restored from __doc__
        """ keyReleaseEvent(self, event: Optional[QKeyEvent]) """
        pass

    def mapFromItem(self, item, QGraphicsItem=None, *args, **kwargs): # real signature unknown; restored from __doc__ with multiple overloads
        """
        mapFromItem(self, item: Optional[QGraphicsItem], point: Union[QPointF, QPoint]) -> QPointF
        mapFromItem(self, item: Optional[QGraphicsItem], rect: QRectF) -> QPolygonF
        mapFromItem(self, item: Optional[QGraphicsItem], polygon: QPolygonF) -> QPolygonF
        mapFromItem(self, item: Optional[QGraphicsItem], path: QPainterPath) -> QPainterPath
        mapFromItem(self, item: Optional[QGraphicsItem], ax: float, ay: float) -> QPointF
        mapFromItem(self, item: Optional[QGraphicsItem], ax: float, ay: float, w: float, h: float) -> QPolygonF
        """
        pass

    def mapFromParent(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        mapFromParent(self, point: Union[QPointF, QPoint]) -> QPointF
        mapFromParent(self, rect: QRectF) -> QPolygonF
        mapFromParent(self, polygon: QPolygonF) -> QPolygonF
        mapFromParent(self, path: QPainterPath) -> QPainterPath
        mapFromParent(self, ax: float, ay: float) -> QPointF
        mapFromParent(self, ax: float, ay: float, w: float, h: float) -> QPolygonF
        """
        pass

    def mapFromScene(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        mapFromScene(self, point: Union[QPointF, QPoint]) -> QPointF
        mapFromScene(self, rect: QRectF) -> QPolygonF
        mapFromScene(self, polygon: QPolygonF) -> QPolygonF
        mapFromScene(self, path: QPainterPath) -> QPainterPath
        mapFromScene(self, ax: float, ay: float) -> QPointF
        mapFromScene(self, ax: float, ay: float, w: float, h: float) -> QPolygonF
        """
        pass

    def mapRectFromItem(self, item, QGraphicsItem=None, *args, **kwargs): # real signature unknown; restored from __doc__ with multiple overloads
        """
        mapRectFromItem(self, item: Optional[QGraphicsItem], rect: QRectF) -> QRectF
        mapRectFromItem(self, item: Optional[QGraphicsItem], ax: float, ay: float, w: float, h: float) -> QRectF
        """
        pass

    def mapRectFromParent(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        mapRectFromParent(self, rect: QRectF) -> QRectF
        mapRectFromParent(self, ax: float, ay: float, w: float, h: float) -> QRectF
        """
        pass

    def mapRectFromScene(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        mapRectFromScene(self, rect: QRectF) -> QRectF
        mapRectFromScene(self, ax: float, ay: float, w: float, h: float) -> QRectF
        """
        pass

    def mapRectToItem(self, item, QGraphicsItem=None, *args, **kwargs): # real signature unknown; restored from __doc__ with multiple overloads
        """
        mapRectToItem(self, item: Optional[QGraphicsItem], rect: QRectF) -> QRectF
        mapRectToItem(self, item: Optional[QGraphicsItem], ax: float, ay: float, w: float, h: float) -> QRectF
        """
        pass

    def mapRectToParent(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        mapRectToParent(self, rect: QRectF) -> QRectF
        mapRectToParent(self, ax: float, ay: float, w: float, h: float) -> QRectF
        """
        pass

    def mapRectToScene(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        mapRectToScene(self, rect: QRectF) -> QRectF
        mapRectToScene(self, ax: float, ay: float, w: float, h: float) -> QRectF
        """
        pass

    def mapToItem(self, item, QGraphicsItem=None, *args, **kwargs): # real signature unknown; restored from __doc__ with multiple overloads
        """
        mapToItem(self, item: Optional[QGraphicsItem], point: Union[QPointF, QPoint]) -> QPointF
        mapToItem(self, item: Optional[QGraphicsItem], rect: QRectF) -> QPolygonF
        mapToItem(self, item: Optional[QGraphicsItem], polygon: QPolygonF) -> QPolygonF
        mapToItem(self, item: Optional[QGraphicsItem], path: QPainterPath) -> QPainterPath
        mapToItem(self, item: Optional[QGraphicsItem], ax: float, ay: float) -> QPointF
        mapToItem(self, item: Optional[QGraphicsItem], ax: float, ay: float, w: float, h: float) -> QPolygonF
        """
        pass

    def mapToParent(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        mapToParent(self, point: Union[QPointF, QPoint]) -> QPointF
        mapToParent(self, rect: QRectF) -> QPolygonF
        mapToParent(self, polygon: QPolygonF) -> QPolygonF
        mapToParent(self, path: QPainterPath) -> QPainterPath
        mapToParent(self, ax: float, ay: float) -> QPointF
        mapToParent(self, ax: float, ay: float, w: float, h: float) -> QPolygonF
        """
        pass

    def mapToScene(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        mapToScene(self, point: Union[QPointF, QPoint]) -> QPointF
        mapToScene(self, rect: QRectF) -> QPolygonF
        mapToScene(self, polygon: QPolygonF) -> QPolygonF
        mapToScene(self, path: QPainterPath) -> QPainterPath
        mapToScene(self, ax: float, ay: float) -> QPointF
        mapToScene(self, ax: float, ay: float, w: float, h: float) -> QPolygonF
        """
        pass

    def mouseDoubleClickEvent(self, event, QGraphicsSceneMouseEvent=None): # real signature unknown; restored from __doc__
        """ mouseDoubleClickEvent(self, event: Optional[QGraphicsSceneMouseEvent]) """
        pass

    def mouseMoveEvent(self, event, QGraphicsSceneMouseEvent=None): # real signature unknown; restored from __doc__
        """ mouseMoveEvent(self, event: Optional[QGraphicsSceneMouseEvent]) """
        pass

    def mousePressEvent(self, event, QGraphicsSceneMouseEvent=None): # real signature unknown; restored from __doc__
        """ mousePressEvent(self, event: Optional[QGraphicsSceneMouseEvent]) """
        pass

    def mouseReleaseEvent(self, event, QGraphicsSceneMouseEvent=None): # real signature unknown; restored from __doc__
        """ mouseReleaseEvent(self, event: Optional[QGraphicsSceneMouseEvent]) """
        pass

    def moveBy(self, dx, dy): # real signature unknown; restored from __doc__
        """ moveBy(self, dx: float, dy: float) """
        pass

    def opacity(self): # real signature unknown; restored from __doc__
        """ opacity(self) -> float """
        return 0.0

    def opaqueArea(self): # real signature unknown; restored from __doc__
        """ opaqueArea(self) -> QPainterPath """
        pass

    def paint(self, painter, QPainter=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ paint(self, painter: Optional[QPainter], option: Optional[QStyleOptionGraphicsItem], widget: Optional[QWidget] = None) """
        pass

    def panel(self): # real signature unknown; restored from __doc__
        """ panel(self) -> Optional[QGraphicsItem] """
        pass

    def panelModality(self): # real signature unknown; restored from __doc__
        """ panelModality(self) -> QGraphicsItem.PanelModality """
        pass

    def parentItem(self): # real signature unknown; restored from __doc__
        """ parentItem(self) -> Optional[QGraphicsItem] """
        pass

    def parentObject(self): # real signature unknown; restored from __doc__
        """ parentObject(self) -> Optional[QGraphicsObject] """
        pass

    def parentWidget(self): # real signature unknown; restored from __doc__
        """ parentWidget(self) -> Optional[QGraphicsWidget] """
        pass

    def pos(self): # real signature unknown; restored from __doc__
        """ pos(self) -> QPointF """
        pass

    def prepareGeometryChange(self): # real signature unknown; restored from __doc__
        """ prepareGeometryChange(self) """
        pass

    def removeSceneEventFilter(self, filterItem, QGraphicsItem=None): # real signature unknown; restored from __doc__
        """ removeSceneEventFilter(self, filterItem: Optional[QGraphicsItem]) """
        pass

    def resetTransform(self): # real signature unknown; restored from __doc__
        """ resetTransform(self) """
        pass

    def rotation(self): # real signature unknown; restored from __doc__
        """ rotation(self) -> float """
        return 0.0

    def scale(self): # real signature unknown; restored from __doc__
        """ scale(self) -> float """
        return 0.0

    def scene(self): # real signature unknown; restored from __doc__
        """ scene(self) -> Optional[QGraphicsScene] """
        pass

    def sceneBoundingRect(self): # real signature unknown; restored from __doc__
        """ sceneBoundingRect(self) -> QRectF """
        pass

    def sceneEvent(self, event, QEvent=None): # real signature unknown; restored from __doc__
        """ sceneEvent(self, event: Optional[QEvent]) -> bool """
        return False

    def sceneEventFilter(self, watched, QGraphicsItem=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ sceneEventFilter(self, watched: Optional[QGraphicsItem], event: Optional[QEvent]) -> bool """
        pass

    def scenePos(self): # real signature unknown; restored from __doc__
        """ scenePos(self) -> QPointF """
        pass

    def sceneTransform(self): # real signature unknown; restored from __doc__
        """ sceneTransform(self) -> QTransform """
        pass

    def scroll(self, dx, dy, rect=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ scroll(self, dx: float, dy: float, rect: QRectF = QRectF()) """
        pass

    def setAcceptDrops(self, on): # real signature unknown; restored from __doc__
        """ setAcceptDrops(self, on: bool) """
        pass

    def setAcceptedMouseButtons(self, buttons, Qt_MouseButtons=None, Qt_MouseButton=None): # real signature unknown; restored from __doc__
        """ setAcceptedMouseButtons(self, buttons: Union[Qt.MouseButtons, Qt.MouseButton]) """
        pass

    def setAcceptHoverEvents(self, enabled): # real signature unknown; restored from __doc__
        """ setAcceptHoverEvents(self, enabled: bool) """
        pass

    def setAcceptTouchEvents(self, enabled): # real signature unknown; restored from __doc__
        """ setAcceptTouchEvents(self, enabled: bool) """
        pass

    def setActive(self, active): # real signature unknown; restored from __doc__
        """ setActive(self, active: bool) """
        pass

    def setBoundingRegionGranularity(self, granularity): # real signature unknown; restored from __doc__
        """ setBoundingRegionGranularity(self, granularity: float) """
        pass

    def setCacheMode(self, mode, logicalCacheSize=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setCacheMode(self, mode: QGraphicsItem.CacheMode, logicalCacheSize: QSize = QSize()) """
        pass

    def setCursor(self, cursor, QCursor=None, Qt_CursorShape=None): # real signature unknown; restored from __doc__
        """ setCursor(self, cursor: Union[QCursor, Qt.CursorShape]) """
        pass

    def setData(self, key, value): # real signature unknown; restored from __doc__
        """ setData(self, key: int, value: Any) """
        pass

    def setEnabled(self, enabled): # real signature unknown; restored from __doc__
        """ setEnabled(self, enabled: bool) """
        pass

    def setFiltersChildEvents(self, enabled): # real signature unknown; restored from __doc__
        """ setFiltersChildEvents(self, enabled: bool) """
        pass

    def setFlag(self, flag, enabled=True): # real signature unknown; restored from __doc__
        """ setFlag(self, flag: QGraphicsItem.GraphicsItemFlag, enabled: bool = True) """
        pass

    def setFlags(self, flags, QGraphicsItem_GraphicsItemFlags=None, QGraphicsItem_GraphicsItemFlag=None): # real signature unknown; restored from __doc__
        """ setFlags(self, flags: Union[QGraphicsItem.GraphicsItemFlags, QGraphicsItem.GraphicsItemFlag]) """
        pass

    def setFocus(self, focusReason=None): # real signature unknown; restored from __doc__
        """ setFocus(self, focusReason: Qt.FocusReason = Qt.OtherFocusReason) """
        pass

    def setFocusProxy(self, item, QGraphicsItem=None): # real signature unknown; restored from __doc__
        """ setFocusProxy(self, item: Optional[QGraphicsItem]) """
        pass

    def setGraphicsEffect(self, effect, QGraphicsEffect=None): # real signature unknown; restored from __doc__
        """ setGraphicsEffect(self, effect: Optional[QGraphicsEffect]) """
        pass

    def setGroup(self, group, QGraphicsItemGroup=None): # real signature unknown; restored from __doc__
        """ setGroup(self, group: Optional[QGraphicsItemGroup]) """
        pass

    def setInputMethodHints(self, hints, Qt_InputMethodHints=None, Qt_InputMethodHint=None): # real signature unknown; restored from __doc__
        """ setInputMethodHints(self, hints: Union[Qt.InputMethodHints, Qt.InputMethodHint]) """
        pass

    def setOpacity(self, opacity): # real signature unknown; restored from __doc__
        """ setOpacity(self, opacity: float) """
        pass

    def setPanelModality(self, panelModality): # real signature unknown; restored from __doc__
        """ setPanelModality(self, panelModality: QGraphicsItem.PanelModality) """
        pass

    def setParentItem(self, parent, QGraphicsItem=None): # real signature unknown; restored from __doc__
        """ setParentItem(self, parent: Optional[QGraphicsItem]) """
        pass

    def setPos(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setPos(self, pos: Union[QPointF, QPoint])
        setPos(self, ax: float, ay: float)
        """
        pass

    def setRotation(self, angle): # real signature unknown; restored from __doc__
        """ setRotation(self, angle: float) """
        pass

    def setScale(self, scale): # real signature unknown; restored from __doc__
        """ setScale(self, scale: float) """
        pass

    def setSelected(self, selected): # real signature unknown; restored from __doc__
        """ setSelected(self, selected: bool) """
        pass

    def setToolTip(self, toolTip, p_str=None): # real signature unknown; restored from __doc__
        """ setToolTip(self, toolTip: Optional[str]) """
        pass

    def setTransform(self, matrix, combine=False): # real signature unknown; restored from __doc__
        """ setTransform(self, matrix: QTransform, combine: bool = False) """
        pass

    def setTransformations(self, transformations, QGraphicsTransform=None): # real signature unknown; restored from __doc__
        """ setTransformations(self, transformations: Iterable[QGraphicsTransform]) """
        pass

    def setTransformOriginPoint(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setTransformOriginPoint(self, origin: Union[QPointF, QPoint])
        setTransformOriginPoint(self, ax: float, ay: float)
        """
        pass

    def setVisible(self, visible): # real signature unknown; restored from __doc__
        """ setVisible(self, visible: bool) """
        pass

    def setX(self, x): # real signature unknown; restored from __doc__
        """ setX(self, x: float) """
        pass

    def setY(self, y): # real signature unknown; restored from __doc__
        """ setY(self, y: float) """
        pass

    def setZValue(self, z): # real signature unknown; restored from __doc__
        """ setZValue(self, z: float) """
        pass

    def shape(self): # real signature unknown; restored from __doc__
        """ shape(self) -> QPainterPath """
        pass

    def show(self): # real signature unknown; restored from __doc__
        """ show(self) """
        pass

    def stackBefore(self, sibling, QGraphicsItem=None): # real signature unknown; restored from __doc__
        """ stackBefore(self, sibling: Optional[QGraphicsItem]) """
        pass

    def toGraphicsObject(self): # real signature unknown; restored from __doc__
        """ toGraphicsObject(self) -> Optional[QGraphicsObject] """
        pass

    def toolTip(self): # real signature unknown; restored from __doc__
        """ toolTip(self) -> str """
        return ""

    def topLevelItem(self): # real signature unknown; restored from __doc__
        """ topLevelItem(self) -> Optional[QGraphicsItem] """
        pass

    def topLevelWidget(self): # real signature unknown; restored from __doc__
        """ topLevelWidget(self) -> Optional[QGraphicsWidget] """
        pass

    def transform(self): # real signature unknown; restored from __doc__
        """ transform(self) -> QTransform """
        pass

    def transformations(self): # real signature unknown; restored from __doc__
        """ transformations(self) -> List[QGraphicsTransform] """
        return []

    def transformOriginPoint(self): # real signature unknown; restored from __doc__
        """ transformOriginPoint(self) -> QPointF """
        pass

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> int """
        return 0

    def ungrabKeyboard(self): # real signature unknown; restored from __doc__
        """ ungrabKeyboard(self) """
        pass

    def ungrabMouse(self): # real signature unknown; restored from __doc__
        """ ungrabMouse(self) """
        pass

    def unsetCursor(self): # real signature unknown; restored from __doc__
        """ unsetCursor(self) """
        pass

    def update(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        update(self, rect: QRectF = QRectF())
        update(self, ax: float, ay: float, width: float, height: float)
        """
        pass

    def updateMicroFocus(self): # real signature unknown; restored from __doc__
        """ updateMicroFocus(self) """
        pass

    def wheelEvent(self, event, QGraphicsSceneWheelEvent=None): # real signature unknown; restored from __doc__
        """ wheelEvent(self, event: Optional[QGraphicsSceneWheelEvent]) """
        pass

    def window(self): # real signature unknown; restored from __doc__
        """ window(self) -> Optional[QGraphicsWidget] """
        pass

    def x(self): # real signature unknown; restored from __doc__
        """ x(self) -> float """
        return 0.0

    def y(self): # real signature unknown; restored from __doc__
        """ y(self) -> float """
        return 0.0

    def zValue(self): # real signature unknown; restored from __doc__
        """ zValue(self) -> float """
        return 0.0

    def __init__(self, parent, QGraphicsItem=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    DeviceCoordinateCache = 2
    ItemAcceptsInputMethod = 4096
    ItemChildAddedChange = 6
    ItemChildRemovedChange = 7
    ItemClipsChildrenToShape = 16
    ItemClipsToShape = 8
    ItemContainsChildrenInShape = 524288
    ItemCoordinateCache = 1
    ItemCursorChange = 17
    ItemCursorHasChanged = 18
    ItemDoesntPropagateOpacityToChildren = 128
    ItemEnabledChange = 3
    ItemEnabledHasChanged = 13
    ItemFlagsChange = 21
    ItemFlagsHaveChanged = 22
    ItemHasNoContents = 1024
    ItemIgnoresParentOpacity = 64
    ItemIgnoresTransformations = 32
    ItemIsFocusable = 4
    ItemIsMovable = 1
    ItemIsPanel = 16384
    ItemIsSelectable = 2
    ItemMatrixChange = 1
    ItemNegativeZStacksBehindParent = 8192
    ItemOpacityChange = 25
    ItemOpacityHasChanged = 26
    ItemParentChange = 5
    ItemParentHasChanged = 15
    ItemPositionChange = 0
    ItemPositionHasChanged = 9
    ItemRotationChange = 28
    ItemRotationHasChanged = 29
    ItemScaleChange = 30
    ItemScaleHasChanged = 31
    ItemSceneChange = 11
    ItemSceneHasChanged = 16
    ItemScenePositionHasChanged = 27
    ItemSelectedChange = 4
    ItemSelectedHasChanged = 14
    ItemSendsGeometryChanges = 2048
    ItemSendsScenePositionChanges = 65536
    ItemStacksBehindParent = 256
    ItemToolTipChange = 19
    ItemToolTipHasChanged = 20
    ItemTransformChange = 8
    ItemTransformHasChanged = 10
    ItemTransformOriginPointChange = 32
    ItemTransformOriginPointHasChanged = 33
    ItemUsesExtendedStyleOption = 512
    ItemVisibleChange = 2
    ItemVisibleHasChanged = 12
    ItemZValueChange = 23
    ItemZValueHasChanged = 24
    NoCache = 0
    NonModal = 0
    PanelModal = 1
    SceneModal = 2
    Type = 1
    UserType = 65536


