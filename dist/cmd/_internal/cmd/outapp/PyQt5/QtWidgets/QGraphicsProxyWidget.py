# encoding: utf-8
# module PyQt5.QtWidgets
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


from .QGraphicsWidget import QGraphicsWidget

class QGraphicsProxyWidget(QGraphicsWidget):
    """ QGraphicsProxyWidget(parent: Optional[QGraphicsItem] = None, flags: Union[Qt.WindowFlags, Qt.WindowType] = Qt.WindowFlags()) """
    def changeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def closeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def contextMenuEvent(self, event, QGraphicsSceneContextMenuEvent=None): # real signature unknown; restored from __doc__
        """ contextMenuEvent(self, event: Optional[QGraphicsSceneContextMenuEvent]) """
        pass

    def createProxyForChildWidget(self, child, QWidget=None): # real signature unknown; restored from __doc__
        """ createProxyForChildWidget(self, child: Optional[QWidget]) -> Optional[QGraphicsProxyWidget] """
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
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

    def event(self, event, QEvent=None): # real signature unknown; restored from __doc__
        """ event(self, event: Optional[QEvent]) -> bool """
        return False

    def eventFilter(self, p_object, QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ eventFilter(self, object: Optional[QObject], event: Optional[QEvent]) -> bool """
        pass

    def focusInEvent(self, event, QFocusEvent=None): # real signature unknown; restored from __doc__
        """ focusInEvent(self, event: Optional[QFocusEvent]) """
        pass

    def focusNextPrevChild(self, next): # real signature unknown; restored from __doc__
        """ focusNextPrevChild(self, next: bool) -> bool """
        return False

    def focusOutEvent(self, event, QFocusEvent=None): # real signature unknown; restored from __doc__
        """ focusOutEvent(self, event: Optional[QFocusEvent]) """
        pass

    def grabKeyboardEvent(self, *args, **kwargs): # real signature unknown
        pass

    def grabMouseEvent(self, event, QEvent=None): # real signature unknown; restored from __doc__
        """ grabMouseEvent(self, event: Optional[QEvent]) """
        pass

    def hideEvent(self, event, QHideEvent=None): # real signature unknown; restored from __doc__
        """ hideEvent(self, event: Optional[QHideEvent]) """
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

    def initStyleOption(self, *args, **kwargs): # real signature unknown
        pass

    def inputMethodEvent(self, event, QInputMethodEvent=None): # real signature unknown; restored from __doc__
        """ inputMethodEvent(self, event: Optional[QInputMethodEvent]) """
        pass

    def inputMethodQuery(self, query): # real signature unknown; restored from __doc__
        """ inputMethodQuery(self, query: Qt.InputMethodQuery) -> Any """
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def itemChange(self, change, value): # real signature unknown; restored from __doc__
        """ itemChange(self, change: QGraphicsItem.GraphicsItemChange, value: Any) -> Any """
        pass

    def keyPressEvent(self, event, QKeyEvent=None): # real signature unknown; restored from __doc__
        """ keyPressEvent(self, event: Optional[QKeyEvent]) """
        pass

    def keyReleaseEvent(self, event, QKeyEvent=None): # real signature unknown; restored from __doc__
        """ keyReleaseEvent(self, event: Optional[QKeyEvent]) """
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

    def moveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def newProxyWidget(self, a0, QWidget=None): # real signature unknown; restored from __doc__
        """ newProxyWidget(self, a0: Optional[QWidget]) -> Optional[QGraphicsProxyWidget] """
        pass

    def paint(self, painter, QPainter=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ paint(self, painter: Optional[QPainter], option: Optional[QStyleOptionGraphicsItem], widget: Optional[QWidget]) """
        pass

    def polishEvent(self, *args, **kwargs): # real signature unknown
        pass

    def prepareGeometryChange(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def resizeEvent(self, event, QGraphicsSceneResizeEvent=None): # real signature unknown; restored from __doc__
        """ resizeEvent(self, event: Optional[QGraphicsSceneResizeEvent]) """
        pass

    def sceneEvent(self, *args, **kwargs): # real signature unknown
        pass

    def sceneEventFilter(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setGeometry(self, rect): # real signature unknown; restored from __doc__
        """ setGeometry(self, rect: QRectF) """
        pass

    def setGraphicsItem(self, *args, **kwargs): # real signature unknown
        pass

    def setOwnedByLayout(self, *args, **kwargs): # real signature unknown
        pass

    def setWidget(self, widget, QWidget=None): # real signature unknown; restored from __doc__
        """ setWidget(self, widget: Optional[QWidget]) """
        pass

    def showEvent(self, event, QShowEvent=None): # real signature unknown; restored from __doc__
        """ showEvent(self, event: Optional[QShowEvent]) """
        pass

    def sizeHint(self, which, constraint=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ sizeHint(self, which: Qt.SizeHint, constraint: QSizeF = QSizeF()) -> QSizeF """
        pass

    def subWidgetRect(self, widget, QWidget=None): # real signature unknown; restored from __doc__
        """ subWidgetRect(self, widget: Optional[QWidget]) -> QRectF """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> int """
        return 0

    def ungrabKeyboardEvent(self, *args, **kwargs): # real signature unknown
        pass

    def ungrabMouseEvent(self, event, QEvent=None): # real signature unknown; restored from __doc__
        """ ungrabMouseEvent(self, event: Optional[QEvent]) """
        pass

    def updateGeometry(self, *args, **kwargs): # real signature unknown
        pass

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

    def wheelEvent(self, event, QGraphicsSceneWheelEvent=None): # real signature unknown; restored from __doc__
        """ wheelEvent(self, event: Optional[QGraphicsSceneWheelEvent]) """
        pass

    def widget(self): # real signature unknown; restored from __doc__
        """ widget(self) -> Optional[QWidget] """
        pass

    def windowFrameEvent(self, *args, **kwargs): # real signature unknown
        pass

    def windowFrameSectionAt(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent, QGraphicsItem=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass


