# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QPainterPath(__sip.simplewrapper):
    """
    QPainterPath()
    QPainterPath(startPoint: Union[QPointF, QPoint])
    QPainterPath(other: QPainterPath)
    """
    def addEllipse(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        addEllipse(self, rect: QRectF)
        addEllipse(self, x: float, y: float, w: float, h: float)
        addEllipse(self, center: Union[QPointF, QPoint], rx: float, ry: float)
        """
        pass

    def addPath(self, path): # real signature unknown; restored from __doc__
        """ addPath(self, path: QPainterPath) """
        pass

    def addPolygon(self, polygon): # real signature unknown; restored from __doc__
        """ addPolygon(self, polygon: QPolygonF) """
        pass

    def addRect(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        addRect(self, rect: QRectF)
        addRect(self, x: float, y: float, w: float, h: float)
        """
        pass

    def addRegion(self, region): # real signature unknown; restored from __doc__
        """ addRegion(self, region: QRegion) """
        pass

    def addRoundedRect(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        addRoundedRect(self, rect: QRectF, xRadius: float, yRadius: float, mode: Qt.SizeMode = Qt.AbsoluteSize)
        addRoundedRect(self, x: float, y: float, w: float, h: float, xRadius: float, yRadius: float, mode: Qt.SizeMode = Qt.AbsoluteSize)
        """
        pass

    def addText(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        addText(self, point: Union[QPointF, QPoint], f: QFont, text: Optional[str])
        addText(self, x: float, y: float, f: QFont, text: Optional[str])
        """
        pass

    def angleAtPercent(self, t): # real signature unknown; restored from __doc__
        """ angleAtPercent(self, t: float) -> float """
        return 0.0

    def arcMoveTo(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        arcMoveTo(self, rect: QRectF, angle: float)
        arcMoveTo(self, x: float, y: float, w: float, h: float, angle: float)
        """
        pass

    def arcTo(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        arcTo(self, rect: QRectF, startAngle: float, arcLength: float)
        arcTo(self, x: float, y: float, w: float, h: float, startAngle: float, arcLenght: float)
        """
        pass

    def boundingRect(self): # real signature unknown; restored from __doc__
        """ boundingRect(self) -> QRectF """
        pass

    def capacity(self): # real signature unknown; restored from __doc__
        """ capacity(self) -> int """
        return 0

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def closeSubpath(self): # real signature unknown; restored from __doc__
        """ closeSubpath(self) """
        pass

    def connectPath(self, path): # real signature unknown; restored from __doc__
        """ connectPath(self, path: QPainterPath) """
        pass

    def contains(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        contains(self, pt: Union[QPointF, QPoint]) -> bool
        contains(self, rect: QRectF) -> bool
        contains(self, p: QPainterPath) -> bool
        """
        return False

    def controlPointRect(self): # real signature unknown; restored from __doc__
        """ controlPointRect(self) -> QRectF """
        pass

    def cubicTo(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        cubicTo(self, ctrlPt1: Union[QPointF, QPoint], ctrlPt2: Union[QPointF, QPoint], endPt: Union[QPointF, QPoint])
        cubicTo(self, ctrlPt1x: float, ctrlPt1y: float, ctrlPt2x: float, ctrlPt2y: float, endPtx: float, endPty: float)
        """
        pass

    def currentPosition(self): # real signature unknown; restored from __doc__
        """ currentPosition(self) -> QPointF """
        pass

    def elementAt(self, i): # real signature unknown; restored from __doc__
        """ elementAt(self, i: int) -> QPainterPath.Element """
        pass

    def elementCount(self): # real signature unknown; restored from __doc__
        """ elementCount(self) -> int """
        return 0

    def fillRule(self): # real signature unknown; restored from __doc__
        """ fillRule(self) -> Qt.FillRule """
        pass

    def intersected(self, r): # real signature unknown; restored from __doc__
        """ intersected(self, r: QPainterPath) -> QPainterPath """
        return QPainterPath

    def intersects(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        intersects(self, rect: QRectF) -> bool
        intersects(self, p: QPainterPath) -> bool
        """
        return False

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ isEmpty(self) -> bool """
        return False

    def length(self): # real signature unknown; restored from __doc__
        """ length(self) -> float """
        return 0.0

    def lineTo(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        lineTo(self, p: Union[QPointF, QPoint])
        lineTo(self, x: float, y: float)
        """
        pass

    def moveTo(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        moveTo(self, p: Union[QPointF, QPoint])
        moveTo(self, x: float, y: float)
        """
        pass

    def percentAtLength(self, t): # real signature unknown; restored from __doc__
        """ percentAtLength(self, t: float) -> float """
        return 0.0

    def pointAtPercent(self, t): # real signature unknown; restored from __doc__
        """ pointAtPercent(self, t: float) -> QPointF """
        pass

    def quadTo(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        quadTo(self, ctrlPt: Union[QPointF, QPoint], endPt: Union[QPointF, QPoint])
        quadTo(self, ctrlPtx: float, ctrlPty: float, endPtx: float, endPty: float)
        """
        pass

    def reserve(self, size): # real signature unknown; restored from __doc__
        """ reserve(self, size: int) """
        pass

    def setElementPositionAt(self, i, x, y): # real signature unknown; restored from __doc__
        """ setElementPositionAt(self, i: int, x: float, y: float) """
        pass

    def setFillRule(self, fillRule): # real signature unknown; restored from __doc__
        """ setFillRule(self, fillRule: Qt.FillRule) """
        pass

    def simplified(self): # real signature unknown; restored from __doc__
        """ simplified(self) -> QPainterPath """
        return QPainterPath

    def slopeAtPercent(self, t): # real signature unknown; restored from __doc__
        """ slopeAtPercent(self, t: float) -> float """
        return 0.0

    def subtracted(self, r): # real signature unknown; restored from __doc__
        """ subtracted(self, r: QPainterPath) -> QPainterPath """
        return QPainterPath

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: QPainterPath) """
        pass

    def toFillPolygon(self, matrix=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        toFillPolygon(self) -> QPolygonF
        toFillPolygon(self, matrix: QTransform) -> QPolygonF
        """
        return QPolygonF

    def toFillPolygons(self, matrix=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        toFillPolygons(self) -> List[QPolygonF]
        toFillPolygons(self, matrix: QTransform) -> List[QPolygonF]
        """
        return []

    def toReversed(self): # real signature unknown; restored from __doc__
        """ toReversed(self) -> QPainterPath """
        return QPainterPath

    def toSubpathPolygons(self, matrix=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        toSubpathPolygons(self) -> List[QPolygonF]
        toSubpathPolygons(self, matrix: QTransform) -> List[QPolygonF]
        """
        return []

    def translate(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        translate(self, dx: float, dy: float)
        translate(self, offset: Union[QPointF, QPoint])
        """
        pass

    def translated(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        translated(self, dx: float, dy: float) -> QPainterPath
        translated(self, offset: Union[QPointF, QPoint]) -> QPainterPath
        """
        return QPainterPath

    def united(self, r): # real signature unknown; restored from __doc__
        """ united(self, r: QPainterPath) -> QPainterPath """
        return QPainterPath

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __and__(self, *args, **kwargs): # real signature unknown
        """ Return self&value. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __iadd__(self, *args, **kwargs): # real signature unknown
        """ Return self+=value. """
        pass

    def __iand__(self, *args, **kwargs): # real signature unknown
        """ Return self&=value. """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __ior__(self, *args, **kwargs): # real signature unknown
        """ Return self|=value. """
        pass

    def __isub__(self, *args, **kwargs): # real signature unknown
        """ Return self-=value. """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __or__(self, *args, **kwargs): # real signature unknown
        """ Return self|value. """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __rand__(self, *args, **kwargs): # real signature unknown
        """ Return value&self. """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __ror__(self, *args, **kwargs): # real signature unknown
        """ Return value|self. """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    CurveToDataElement = 3
    CurveToElement = 2
    LineToElement = 1
    MoveToElement = 0
    __hash__ = None


