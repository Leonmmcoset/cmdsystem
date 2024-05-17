# encoding: utf-8
# module PyQt5.QtWidgets
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


from .QGraphicsObject import QGraphicsObject

from .QGraphicsLayoutItem import QGraphicsLayoutItem

class QGraphicsWidget(QGraphicsObject, QGraphicsLayoutItem):
    """ QGraphicsWidget(parent: Optional[QGraphicsItem] = None, flags: Union[Qt.WindowFlags, Qt.WindowType] = Qt.WindowFlags()) """
    def actions(self): # real signature unknown; restored from __doc__
        """ actions(self) -> List[QAction] """
        return []

    def addAction(self, action, QAction=None): # real signature unknown; restored from __doc__
        """ addAction(self, action: Optional[QAction]) """
        pass

    def addActions(self, actions, QAction=None): # real signature unknown; restored from __doc__
        """ addActions(self, actions: Iterable[QAction]) """
        pass

    def adjustSize(self): # real signature unknown; restored from __doc__
        """ adjustSize(self) """
        pass

    def autoFillBackground(self): # real signature unknown; restored from __doc__
        """ autoFillBackground(self) -> bool """
        return False

    def boundingRect(self): # real signature unknown; restored from __doc__
        """ boundingRect(self) -> QRectF """
        pass

    def changeEvent(self, event, QEvent=None): # real signature unknown; restored from __doc__
        """ changeEvent(self, event: Optional[QEvent]) """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def close(self): # real signature unknown; restored from __doc__
        """ close(self) -> bool """
        return False

    def closeEvent(self, event, QCloseEvent=None): # real signature unknown; restored from __doc__
        """ closeEvent(self, event: Optional[QCloseEvent]) """
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def contextMenuEvent(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def dragEnterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dragLeaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dragMoveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dropEvent(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, event, QEvent=None): # real signature unknown; restored from __doc__
        """ event(self, event: Optional[QEvent]) -> bool """
        return False

    def focusInEvent(self, event, QFocusEvent=None): # real signature unknown; restored from __doc__
        """ focusInEvent(self, event: Optional[QFocusEvent]) """
        pass

    def focusNextPrevChild(self, next): # real signature unknown; restored from __doc__
        """ focusNextPrevChild(self, next: bool) -> bool """
        return False

    def focusOutEvent(self, event, QFocusEvent=None): # real signature unknown; restored from __doc__
        """ focusOutEvent(self, event: Optional[QFocusEvent]) """
        pass

    def focusPolicy(self): # real signature unknown; restored from __doc__
        """ focusPolicy(self) -> Qt.FocusPolicy """
        pass

    def focusWidget(self): # real signature unknown; restored from __doc__
        """ focusWidget(self) -> Optional[QGraphicsWidget] """
        pass

    def font(self): # real signature unknown; restored from __doc__
        """ font(self) -> QFont """
        pass

    def geometryChanged(self, *args, **kwargs): # real signature unknown
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

    def getContentsMargins(self): # real signature unknown; restored from __doc__
        """ getContentsMargins(self) -> (Optional[float], Optional[float], Optional[float], Optional[float]) """
        pass

    def getWindowFrameMargins(self): # real signature unknown; restored from __doc__
        """ getWindowFrameMargins(self) -> (Optional[float], Optional[float], Optional[float], Optional[float]) """
        pass

    def grabKeyboardEvent(self, event, QEvent=None): # real signature unknown; restored from __doc__
        """ grabKeyboardEvent(self, event: Optional[QEvent]) """
        pass

    def grabMouseEvent(self, event, QEvent=None): # real signature unknown; restored from __doc__
        """ grabMouseEvent(self, event: Optional[QEvent]) """
        pass

    def grabShortcut(self, sequence, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ grabShortcut(self, sequence: Union[QKeySequence, QKeySequence.StandardKey, Optional[str], int], context: Qt.ShortcutContext = Qt.WindowShortcut) -> int """
        pass

    def hideEvent(self, event, QHideEvent=None): # real signature unknown; restored from __doc__
        """ hideEvent(self, event: Optional[QHideEvent]) """
        pass

    def hoverEnterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def hoverLeaveEvent(self, event, QGraphicsSceneHoverEvent=None): # real signature unknown; restored from __doc__
        """ hoverLeaveEvent(self, event: Optional[QGraphicsSceneHoverEvent]) """
        pass

    def hoverMoveEvent(self, event, QGraphicsSceneHoverEvent=None): # real signature unknown; restored from __doc__
        """ hoverMoveEvent(self, event: Optional[QGraphicsSceneHoverEvent]) """
        pass

    def initStyleOption(self, option, QStyleOption=None): # real signature unknown; restored from __doc__
        """ initStyleOption(self, option: Optional[QStyleOption]) """
        pass

    def inputMethodEvent(self, *args, **kwargs): # real signature unknown
        pass

    def inputMethodQuery(self, *args, **kwargs): # real signature unknown
        pass

    def insertAction(self, before, QAction=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ insertAction(self, before: Optional[QAction], action: Optional[QAction]) """
        pass

    def insertActions(self, before, QAction=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ insertActions(self, before: Optional[QAction], actions: Iterable[QAction]) """
        pass

    def isActiveWindow(self): # real signature unknown; restored from __doc__
        """ isActiveWindow(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def itemChange(self, change, value): # real signature unknown; restored from __doc__
        """ itemChange(self, change: QGraphicsItem.GraphicsItemChange, value: Any) -> Any """
        pass

    def keyPressEvent(self, *args, **kwargs): # real signature unknown
        pass

    def keyReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def layout(self): # real signature unknown; restored from __doc__
        """ layout(self) -> Optional[QGraphicsLayout] """
        pass

    def layoutDirection(self): # real signature unknown; restored from __doc__
        """ layoutDirection(self) -> Qt.LayoutDirection """
        pass

    def mouseDoubleClickEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mouseMoveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mousePressEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mouseReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def moveEvent(self, event, QGraphicsSceneMoveEvent=None): # real signature unknown; restored from __doc__
        """ moveEvent(self, event: Optional[QGraphicsSceneMoveEvent]) """
        pass

    def paint(self, painter, QPainter=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ paint(self, painter: Optional[QPainter], option: Optional[QStyleOptionGraphicsItem], widget: Optional[QWidget] = None) """
        pass

    def paintWindowFrame(self, painter, QPainter=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ paintWindowFrame(self, painter: Optional[QPainter], option: Optional[QStyleOptionGraphicsItem], widget: Optional[QWidget] = None) """
        pass

    def palette(self): # real signature unknown; restored from __doc__
        """ palette(self) -> QPalette """
        pass

    def polishEvent(self): # real signature unknown; restored from __doc__
        """ polishEvent(self) """
        pass

    def prepareGeometryChange(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def rect(self): # real signature unknown; restored from __doc__
        """ rect(self) -> QRectF """
        pass

    def releaseShortcut(self, id): # real signature unknown; restored from __doc__
        """ releaseShortcut(self, id: int) """
        pass

    def removeAction(self, action, QAction=None): # real signature unknown; restored from __doc__
        """ removeAction(self, action: Optional[QAction]) """
        pass

    def resize(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        resize(self, size: QSizeF)
        resize(self, w: float, h: float)
        """
        pass

    def resizeEvent(self, event, QGraphicsSceneResizeEvent=None): # real signature unknown; restored from __doc__
        """ resizeEvent(self, event: Optional[QGraphicsSceneResizeEvent]) """
        pass

    def sceneEvent(self, event, QEvent=None): # real signature unknown; restored from __doc__
        """ sceneEvent(self, event: Optional[QEvent]) -> bool """
        return False

    def sceneEventFilter(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setAttribute(self, attribute, on=True): # real signature unknown; restored from __doc__
        """ setAttribute(self, attribute: Qt.WidgetAttribute, on: bool = True) """
        pass

    def setAutoFillBackground(self, enabled): # real signature unknown; restored from __doc__
        """ setAutoFillBackground(self, enabled: bool) """
        pass

    def setContentsMargins(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setContentsMargins(self, margins: QMarginsF)
        setContentsMargins(self, left: float, top: float, right: float, bottom: float)
        """
        pass

    def setFocusPolicy(self, policy): # real signature unknown; restored from __doc__
        """ setFocusPolicy(self, policy: Qt.FocusPolicy) """
        pass

    def setFont(self, font): # real signature unknown; restored from __doc__
        """ setFont(self, font: QFont) """
        pass

    def setGeometry(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setGeometry(self, rect: QRectF)
        setGeometry(self, ax: float, ay: float, aw: float, ah: float)
        """
        pass

    def setGraphicsItem(self, *args, **kwargs): # real signature unknown
        pass

    def setLayout(self, layout, QGraphicsLayout=None): # real signature unknown; restored from __doc__
        """ setLayout(self, layout: Optional[QGraphicsLayout]) """
        pass

    def setLayoutDirection(self, direction): # real signature unknown; restored from __doc__
        """ setLayoutDirection(self, direction: Qt.LayoutDirection) """
        pass

    def setOwnedByLayout(self, *args, **kwargs): # real signature unknown
        pass

    def setPalette(self, palette): # real signature unknown; restored from __doc__
        """ setPalette(self, palette: QPalette) """
        pass

    def setShortcutAutoRepeat(self, id, enabled=True): # real signature unknown; restored from __doc__
        """ setShortcutAutoRepeat(self, id: int, enabled: bool = True) """
        pass

    def setShortcutEnabled(self, id, enabled=True): # real signature unknown; restored from __doc__
        """ setShortcutEnabled(self, id: int, enabled: bool = True) """
        pass

    def setStyle(self, style, QStyle=None): # real signature unknown; restored from __doc__
        """ setStyle(self, style: Optional[QStyle]) """
        pass

    def setTabOrder(self, first, QGraphicsWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setTabOrder(first: Optional[QGraphicsWidget], second: Optional[QGraphicsWidget]) """
        pass

    def setWindowFlags(self, wFlags, Qt_WindowFlags=None, Qt_WindowType=None): # real signature unknown; restored from __doc__
        """ setWindowFlags(self, wFlags: Union[Qt.WindowFlags, Qt.WindowType]) """
        pass

    def setWindowFrameMargins(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setWindowFrameMargins(self, margins: QMarginsF)
        setWindowFrameMargins(self, left: float, top: float, right: float, bottom: float)
        """
        pass

    def setWindowTitle(self, title, p_str=None): # real signature unknown; restored from __doc__
        """ setWindowTitle(self, title: Optional[str]) """
        pass

    def shape(self): # real signature unknown; restored from __doc__
        """ shape(self) -> QPainterPath """
        pass

    def showEvent(self, event, QShowEvent=None): # real signature unknown; restored from __doc__
        """ showEvent(self, event: Optional[QShowEvent]) """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ size(self) -> QSizeF """
        pass

    def sizeHint(self, which, constraint=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ sizeHint(self, which: Qt.SizeHint, constraint: QSizeF = QSizeF()) -> QSizeF """
        pass

    def style(self): # real signature unknown; restored from __doc__
        """ style(self) -> Optional[QStyle] """
        pass

    def testAttribute(self, attribute): # real signature unknown; restored from __doc__
        """ testAttribute(self, attribute: Qt.WidgetAttribute) -> bool """
        return False

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> int """
        return 0

    def ungrabKeyboardEvent(self, event, QEvent=None): # real signature unknown; restored from __doc__
        """ ungrabKeyboardEvent(self, event: Optional[QEvent]) """
        pass

    def ungrabMouseEvent(self, event, QEvent=None): # real signature unknown; restored from __doc__
        """ ungrabMouseEvent(self, event: Optional[QEvent]) """
        pass

    def unsetLayoutDirection(self): # real signature unknown; restored from __doc__
        """ unsetLayoutDirection(self) """
        pass

    def unsetWindowFrameMargins(self): # real signature unknown; restored from __doc__
        """ unsetWindowFrameMargins(self) """
        pass

    def updateGeometry(self): # real signature unknown; restored from __doc__
        """ updateGeometry(self) """
        pass

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

    def wheelEvent(self, *args, **kwargs): # real signature unknown
        pass

    def windowFlags(self): # real signature unknown; restored from __doc__
        """ windowFlags(self) -> Qt.WindowFlags """
        pass

    def windowFrameEvent(self, e, QEvent=None): # real signature unknown; restored from __doc__
        """ windowFrameEvent(self, e: Optional[QEvent]) -> bool """
        return False

    def windowFrameGeometry(self): # real signature unknown; restored from __doc__
        """ windowFrameGeometry(self) -> QRectF """
        pass

    def windowFrameRect(self): # real signature unknown; restored from __doc__
        """ windowFrameRect(self) -> QRectF """
        pass

    def windowFrameSectionAt(self, pos, QPointF=None, QPoint=None): # real signature unknown; restored from __doc__
        """ windowFrameSectionAt(self, pos: Union[QPointF, QPoint]) -> Qt.WindowFrameSection """
        pass

    def windowTitle(self): # real signature unknown; restored from __doc__
        """ windowTitle(self) -> str """
        return ""

    def windowType(self): # real signature unknown; restored from __doc__
        """ windowType(self) -> Qt.WindowType """
        pass

    def __init__(self, parent, QGraphicsItem=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass


