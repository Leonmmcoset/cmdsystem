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

class QGraphicsEllipseItem(QAbstractGraphicsShapeItem):
    """
    QGraphicsEllipseItem(parent: Optional[QGraphicsItem] = None)
    QGraphicsEllipseItem(rect: QRectF, parent: Optional[QGraphicsItem] = None)
    QGraphicsEllipseItem(x: float, y: float, w: float, h: float, parent: Optional[QGraphicsItem] = None)
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

    def prepareGeometryChange(self, *args, **kwargs): # real signature unknown
        pass

    def rect(self): # real signature unknown; restored from __doc__
        """ rect(self) -> QRectF """
        pass

    def sceneEvent(self, *args, **kwargs): # real signature unknown
        pass

    def sceneEventFilter(self, *args, **kwargs): # real signature unknown
        pass

    def setRect(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setRect(self, rect: QRectF)
        setRect(self, ax: float, ay: float, w: float, h: float)
        """
        pass

    def setSpanAngle(self, angle): # real signature unknown; restored from __doc__
        """ setSpanAngle(self, angle: int) """
        pass

    def setStartAngle(self, angle): # real signature unknown; restored from __doc__
        """ setStartAngle(self, angle: int) """
        pass

    def shape(self): # real signature unknown; restored from __doc__
        """ shape(self) -> QPainterPath """
        pass

    def spanAngle(self): # real signature unknown; restored from __doc__
        """ spanAngle(self) -> int """
        return 0

    def startAngle(self): # real signature unknown; restored from __doc__
        """ startAngle(self) -> int """
        return 0

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> int """
        return 0

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

    def wheelEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


