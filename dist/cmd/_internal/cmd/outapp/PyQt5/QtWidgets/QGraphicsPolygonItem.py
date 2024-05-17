# encoding: utf-8
# module PyQt5.QtWidgets
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


from .QAbstractGraphicsShapeItem import QAbstractGraphicsShapeItem

class QGraphicsPolygonItem(QAbstractGraphicsShapeItem):
    """
    QGraphicsPolygonItem(parent: Optional[QGraphicsItem] = None)
    QGraphicsPolygonItem(polygon: QPolygonF, parent: Optional[QGraphicsItem] = None)
    """
    def boundingRect(self): # real signature unknown; restored from __doc__
        """ boundingRect(self) -> QRectF """
        pass

    def contains(self, point, QPointF=None, QPoint=None): # real signature unknown; restored from __doc__
        """ contains(self, point: Union[QPointF, QPoint]) -> bool """
        return False

    def contextMenuEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dragEnterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dragLeaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dragMoveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dropEvent(self, *args, **kwargs): # real signature unknown
        pass

    def fillRule(self): # real signature unknown; restored from __doc__
        """ fillRule(self) -> Qt.FillRule """
        pass

    def focusInEvent(self, *args, **kwargs): # real signature unknown
        pass

    def focusOutEvent(self, *args, **kwargs): # real signature unknown
        pass

    def hoverEnterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def hoverLeaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def hoverMoveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def inputMethodEvent(self, *args, **kwargs): # real signature unknown
        pass

    def inputMethodQuery(self, *args, **kwargs): # real signature unknown
        pass

    def isObscuredBy(self, item, QGraphicsItem=None): # real signature unknown; restored from __doc__
        """ isObscuredBy(self, item: Optional[QGraphicsItem]) -> bool """
        return False

    def itemChange(self, *args, **kwargs): # real signature unknown
        pass

    def keyPressEvent(self, *args, **kwargs): # real signature unknown
        pass

    def keyReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mouseDoubleClickEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mouseMoveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mousePressEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mouseReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def opaqueArea(self): # real signature unknown; restored from __doc__
        """ opaqueArea(self) -> QPainterPath """
        pass

    def paint(self, painter, QPainter=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ paint(self, painter: Optional[QPainter], option: Optional[QStyleOptionGraphicsItem], widget: Optional[QWidget] = None) """
        pass

    def polygon(self): # real signature unknown; restored from __doc__
        """ polygon(self) -> QPolygonF """
        pass

    def prepareGeometryChange(self, *args, **kwargs): # real signature unknown
        pass

    def sceneEvent(self, *args, **kwargs): # real signature unknown
        pass

    def sceneEventFilter(self, *args, **kwargs): # real signature unknown
        pass

    def setFillRule(self, rule): # real signature unknown; restored from __doc__
        """ setFillRule(self, rule: Qt.FillRule) """
        pass

    def setPolygon(self, polygon): # real signature unknown; restored from __doc__
        """ setPolygon(self, polygon: QPolygonF) """
        pass

    def shape(self): # real signature unknown; restored from __doc__
        """ shape(self) -> QPainterPath """
        pass

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> int """
        return 0

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

    def wheelEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


