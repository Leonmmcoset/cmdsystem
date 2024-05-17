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

class QGraphicsView(QAbstractScrollArea):
    """
    QGraphicsView(parent: Optional[QWidget] = None)
    QGraphicsView(scene: Optional[QGraphicsScene], parent: Optional[QWidget] = None)
    """
    def actionEvent(self, *args, **kwargs): # real signature unknown
        pass

    def alignment(self): # real signature unknown; restored from __doc__
        """ alignment(self) -> Qt.Alignment """
        pass

    def backgroundBrush(self): # real signature unknown; restored from __doc__
        """ backgroundBrush(self) -> QBrush """
        pass

    def cacheMode(self): # real signature unknown; restored from __doc__
        """ cacheMode(self) -> QGraphicsView.CacheMode """
        pass

    def centerOn(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        centerOn(self, pos: Union[QPointF, QPoint])
        centerOn(self, item: Optional[QGraphicsItem])
        centerOn(self, ax: float, ay: float)
        """
        pass

    def changeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def closeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def contextMenuEvent(self, event, QContextMenuEvent=None): # real signature unknown; restored from __doc__
        """ contextMenuEvent(self, event: Optional[QContextMenuEvent]) """
        pass

    def create(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def destroy(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def dragEnterEvent(self, event, QDragEnterEvent=None): # real signature unknown; restored from __doc__
        """ dragEnterEvent(self, event: Optional[QDragEnterEvent]) """
        pass

    def dragLeaveEvent(self, event, QDragLeaveEvent=None): # real signature unknown; restored from __doc__
        """ dragLeaveEvent(self, event: Optional[QDragLeaveEvent]) """
        pass

    def dragMode(self): # real signature unknown; restored from __doc__
        """ dragMode(self) -> QGraphicsView.DragMode """
        pass

    def dragMoveEvent(self, event, QDragMoveEvent=None): # real signature unknown; restored from __doc__
        """ dragMoveEvent(self, event: Optional[QDragMoveEvent]) """
        pass

    def drawBackground(self, painter, QPainter=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ drawBackground(self, painter: Optional[QPainter], rect: QRectF) """
        pass

    def drawForeground(self, painter, QPainter=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ drawForeground(self, painter: Optional[QPainter], rect: QRectF) """
        pass

    def drawFrame(self, *args, **kwargs): # real signature unknown
        pass

    def dropEvent(self, event, QDropEvent=None): # real signature unknown; restored from __doc__
        """ dropEvent(self, event: Optional[QDropEvent]) """
        pass

    def ensureVisible(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        ensureVisible(self, rect: QRectF, xMargin: int = 50, yMargin: int = 50)
        ensureVisible(self, item: Optional[QGraphicsItem], xMargin: int = 50, yMargin: int = 50)
        ensureVisible(self, x: float, y: float, w: float, h: float, xMargin: int = 50, yMargin: int = 50)
        """
        pass

    def enterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, event, QEvent=None): # real signature unknown; restored from __doc__
        """ event(self, event: Optional[QEvent]) -> bool """
        return False

    def eventFilter(self, *args, **kwargs): # real signature unknown
        pass

    def fitInView(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        fitInView(self, rect: QRectF, mode: Qt.AspectRatioMode = Qt.IgnoreAspectRatio)
        fitInView(self, item: Optional[QGraphicsItem], mode: Qt.AspectRatioMode = Qt.IgnoreAspectRatio)
        fitInView(self, x: float, y: float, w: float, h: float, mode: Qt.AspectRatioMode = Qt.IgnoreAspectRatio)
        """
        pass

    def focusInEvent(self, event, QFocusEvent=None): # real signature unknown; restored from __doc__
        """ focusInEvent(self, event: Optional[QFocusEvent]) """
        pass

    def focusNextChild(self, *args, **kwargs): # real signature unknown
        pass

    def focusNextPrevChild(self, next): # real signature unknown; restored from __doc__
        """ focusNextPrevChild(self, next: bool) -> bool """
        return False

    def focusOutEvent(self, event, QFocusEvent=None): # real signature unknown; restored from __doc__
        """ focusOutEvent(self, event: Optional[QFocusEvent]) """
        pass

    def focusPreviousChild(self, *args, **kwargs): # real signature unknown
        pass

    def foregroundBrush(self): # real signature unknown; restored from __doc__
        """ foregroundBrush(self) -> QBrush """
        pass

    def hideEvent(self, *args, **kwargs): # real signature unknown
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

    def invalidateScene(self, rect=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ invalidateScene(self, rect: QRectF = QRectF(), layers: Union[QGraphicsScene.SceneLayers, QGraphicsScene.SceneLayer] = QGraphicsScene.AllLayers) """
        pass

    def isInteractive(self): # real signature unknown; restored from __doc__
        """ isInteractive(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def isTransformed(self): # real signature unknown; restored from __doc__
        """ isTransformed(self) -> bool """
        return False

    def itemAt(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        itemAt(self, pos: QPoint) -> Optional[QGraphicsItem]
        itemAt(self, ax: int, ay: int) -> Optional[QGraphicsItem]
        """
        pass

    def items(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        items(self) -> List[QGraphicsItem]
        items(self, pos: QPoint) -> List[QGraphicsItem]
        items(self, x: int, y: int) -> List[QGraphicsItem]
        items(self, x: int, y: int, w: int, h: int, mode: Qt.ItemSelectionMode = Qt.IntersectsItemShape) -> List[QGraphicsItem]
        items(self, rect: QRect, mode: Qt.ItemSelectionMode = Qt.IntersectsItemShape) -> List[QGraphicsItem]
        items(self, polygon: QPolygon, mode: Qt.ItemSelectionMode = Qt.IntersectsItemShape) -> List[QGraphicsItem]
        items(self, path: QPainterPath, mode: Qt.ItemSelectionMode = Qt.IntersectsItemShape) -> List[QGraphicsItem]
        """
        return []

    def keyPressEvent(self, event, QKeyEvent=None): # real signature unknown; restored from __doc__
        """ keyPressEvent(self, event: Optional[QKeyEvent]) """
        pass

    def keyReleaseEvent(self, event, QKeyEvent=None): # real signature unknown; restored from __doc__
        """ keyReleaseEvent(self, event: Optional[QKeyEvent]) """
        pass

    def leaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mapFromScene(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        mapFromScene(self, point: Union[QPointF, QPoint]) -> QPoint
        mapFromScene(self, rect: QRectF) -> QPolygon
        mapFromScene(self, polygon: QPolygonF) -> QPolygon
        mapFromScene(self, path: QPainterPath) -> QPainterPath
        mapFromScene(self, ax: float, ay: float) -> QPoint
        mapFromScene(self, ax: float, ay: float, w: float, h: float) -> QPolygon
        """
        pass

    def mapToScene(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        mapToScene(self, point: QPoint) -> QPointF
        mapToScene(self, rect: QRect) -> QPolygonF
        mapToScene(self, polygon: QPolygon) -> QPolygonF
        mapToScene(self, path: QPainterPath) -> QPainterPath
        mapToScene(self, ax: int, ay: int) -> QPointF
        mapToScene(self, ax: int, ay: int, w: int, h: int) -> QPolygonF
        """
        pass

    def metric(self, *args, **kwargs): # real signature unknown
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

    def moveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def nativeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def optimizationFlags(self): # real signature unknown; restored from __doc__
        """ optimizationFlags(self) -> QGraphicsView.OptimizationFlags """
        pass

    def paintEvent(self, event, QPaintEvent=None): # real signature unknown; restored from __doc__
        """ paintEvent(self, event: Optional[QPaintEvent]) """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def render(self, painter, QPainter=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ render(self, painter: Optional[QPainter], target: QRectF = QRectF(), source: QRect = QRect(), mode: Qt.AspectRatioMode = Qt.KeepAspectRatio) """
        pass

    def renderHints(self): # real signature unknown; restored from __doc__
        """ renderHints(self) -> QPainter.RenderHints """
        pass

    def resetCachedContent(self): # real signature unknown; restored from __doc__
        """ resetCachedContent(self) """
        pass

    def resetTransform(self): # real signature unknown; restored from __doc__
        """ resetTransform(self) """
        pass

    def resizeAnchor(self): # real signature unknown; restored from __doc__
        """ resizeAnchor(self) -> QGraphicsView.ViewportAnchor """
        pass

    def resizeEvent(self, event, QResizeEvent=None): # real signature unknown; restored from __doc__
        """ resizeEvent(self, event: Optional[QResizeEvent]) """
        pass

    def rotate(self, angle): # real signature unknown; restored from __doc__
        """ rotate(self, angle: float) """
        pass

    def rubberBandChanged(self, *args, **kwargs): # real signature unknown
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

    def rubberBandRect(self): # real signature unknown; restored from __doc__
        """ rubberBandRect(self) -> QRect """
        pass

    def rubberBandSelectionMode(self): # real signature unknown; restored from __doc__
        """ rubberBandSelectionMode(self) -> Qt.ItemSelectionMode """
        pass

    def scale(self, sx, sy): # real signature unknown; restored from __doc__
        """ scale(self, sx: float, sy: float) """
        pass

    def scene(self): # real signature unknown; restored from __doc__
        """ scene(self) -> Optional[QGraphicsScene] """
        pass

    def sceneRect(self): # real signature unknown; restored from __doc__
        """ sceneRect(self) -> QRectF """
        pass

    def scrollContentsBy(self, dx, dy): # real signature unknown; restored from __doc__
        """ scrollContentsBy(self, dx: int, dy: int) """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setAlignment(self, alignment, Qt_Alignment=None, Qt_AlignmentFlag=None): # real signature unknown; restored from __doc__
        """ setAlignment(self, alignment: Union[Qt.Alignment, Qt.AlignmentFlag]) """
        pass

    def setBackgroundBrush(self, brush, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setBackgroundBrush(self, brush: Union[QBrush, Union[QColor, Qt.GlobalColor], QGradient]) """
        pass

    def setCacheMode(self, mode, QGraphicsView_CacheMode=None, QGraphicsView_CacheModeFlag=None): # real signature unknown; restored from __doc__
        """ setCacheMode(self, mode: Union[QGraphicsView.CacheMode, QGraphicsView.CacheModeFlag]) """
        pass

    def setDragMode(self, mode): # real signature unknown; restored from __doc__
        """ setDragMode(self, mode: QGraphicsView.DragMode) """
        pass

    def setForegroundBrush(self, brush, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setForegroundBrush(self, brush: Union[QBrush, Union[QColor, Qt.GlobalColor], QGradient]) """
        pass

    def setInteractive(self, allowed): # real signature unknown; restored from __doc__
        """ setInteractive(self, allowed: bool) """
        pass

    def setOptimizationFlag(self, flag, enabled=True): # real signature unknown; restored from __doc__
        """ setOptimizationFlag(self, flag: QGraphicsView.OptimizationFlag, enabled: bool = True) """
        pass

    def setOptimizationFlags(self, flags, QGraphicsView_OptimizationFlags=None, QGraphicsView_OptimizationFlag=None): # real signature unknown; restored from __doc__
        """ setOptimizationFlags(self, flags: Union[QGraphicsView.OptimizationFlags, QGraphicsView.OptimizationFlag]) """
        pass

    def setRenderHint(self, hint, on=True): # real signature unknown; restored from __doc__
        """ setRenderHint(self, hint: QPainter.RenderHint, on: bool = True) """
        pass

    def setRenderHints(self, hints, QPainter_RenderHints=None, QPainter_RenderHint=None): # real signature unknown; restored from __doc__
        """ setRenderHints(self, hints: Union[QPainter.RenderHints, QPainter.RenderHint]) """
        pass

    def setResizeAnchor(self, anchor): # real signature unknown; restored from __doc__
        """ setResizeAnchor(self, anchor: QGraphicsView.ViewportAnchor) """
        pass

    def setRubberBandSelectionMode(self, mode): # real signature unknown; restored from __doc__
        """ setRubberBandSelectionMode(self, mode: Qt.ItemSelectionMode) """
        pass

    def setScene(self, scene, QGraphicsScene=None): # real signature unknown; restored from __doc__
        """ setScene(self, scene: Optional[QGraphicsScene]) """
        pass

    def setSceneRect(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setSceneRect(self, rect: QRectF)
        setSceneRect(self, ax: float, ay: float, aw: float, ah: float)
        """
        pass

    def setTransform(self, matrix, combine=False): # real signature unknown; restored from __doc__
        """ setTransform(self, matrix: QTransform, combine: bool = False) """
        pass

    def setTransformationAnchor(self, anchor): # real signature unknown; restored from __doc__
        """ setTransformationAnchor(self, anchor: QGraphicsView.ViewportAnchor) """
        pass

    def setupViewport(self, widget, QWidget=None): # real signature unknown; restored from __doc__
        """ setupViewport(self, widget: Optional[QWidget]) """
        pass

    def setViewportMargins(self, *args, **kwargs): # real signature unknown
        pass

    def setViewportUpdateMode(self, mode): # real signature unknown; restored from __doc__
        """ setViewportUpdateMode(self, mode: QGraphicsView.ViewportUpdateMode) """
        pass

    def sharedPainter(self, *args, **kwargs): # real signature unknown
        pass

    def shear(self, sh, sv): # real signature unknown; restored from __doc__
        """ shear(self, sh: float, sv: float) """
        pass

    def showEvent(self, event, QShowEvent=None): # real signature unknown; restored from __doc__
        """ showEvent(self, event: Optional[QShowEvent]) """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> QSize """
        pass

    def tabletEvent(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def transform(self): # real signature unknown; restored from __doc__
        """ transform(self) -> QTransform """
        pass

    def transformationAnchor(self): # real signature unknown; restored from __doc__
        """ transformationAnchor(self) -> QGraphicsView.ViewportAnchor """
        pass

    def translate(self, dx, dy): # real signature unknown; restored from __doc__
        """ translate(self, dx: float, dy: float) """
        pass

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

    def updateScene(self, rects, QRectF=None): # real signature unknown; restored from __doc__
        """ updateScene(self, rects: Iterable[QRectF]) """
        pass

    def updateSceneRect(self, rect): # real signature unknown; restored from __doc__
        """ updateSceneRect(self, rect: QRectF) """
        pass

    def viewportEvent(self, event, QEvent=None): # real signature unknown; restored from __doc__
        """ viewportEvent(self, event: Optional[QEvent]) -> bool """
        return False

    def viewportMargins(self, *args, **kwargs): # real signature unknown
        pass

    def viewportSizeHint(self, *args, **kwargs): # real signature unknown
        pass

    def viewportTransform(self): # real signature unknown; restored from __doc__
        """ viewportTransform(self) -> QTransform """
        pass

    def viewportUpdateMode(self): # real signature unknown; restored from __doc__
        """ viewportUpdateMode(self) -> QGraphicsView.ViewportUpdateMode """
        pass

    def wheelEvent(self, event, QWheelEvent=None): # real signature unknown; restored from __doc__
        """ wheelEvent(self, event: Optional[QWheelEvent]) """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    AnchorUnderMouse = 2
    AnchorViewCenter = 1
    BoundingRectViewportUpdate = 4
    CacheBackground = 1
    CacheNone = 0
    DontAdjustForAntialiasing = 4
    DontClipPainter = 1
    DontSavePainterState = 2
    FullViewportUpdate = 0
    MinimalViewportUpdate = 1
    NoAnchor = 0
    NoDrag = 0
    NoViewportUpdate = 3
    RubberBandDrag = 2
    ScrollHandDrag = 1
    SmartViewportUpdate = 2


