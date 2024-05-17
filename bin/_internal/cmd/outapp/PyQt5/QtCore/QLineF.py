# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


class QLineF(__sip.simplewrapper):
    """
    QLineF(line: QLine)
    QLineF()
    QLineF(apt1: Union[QPointF, QPoint], apt2: Union[QPointF, QPoint])
    QLineF(x1pos: float, y1pos: float, x2pos: float, y2pos: float)
    QLineF(a0: QLineF)
    """
    def angle(self): # real signature unknown; restored from __doc__
        """ angle(self) -> float """
        return 0.0

    def angleTo(self, l): # real signature unknown; restored from __doc__
        """ angleTo(self, l: QLineF) -> float """
        return 0.0

    def center(self): # real signature unknown; restored from __doc__
        """ center(self) -> QPointF """
        return QPointF

    def dx(self): # real signature unknown; restored from __doc__
        """ dx(self) -> float """
        return 0.0

    def dy(self): # real signature unknown; restored from __doc__
        """ dy(self) -> float """
        return 0.0

    def fromPolar(self, length, angle): # real signature unknown; restored from __doc__
        """ fromPolar(length: float, angle: float) -> QLineF """
        return QLineF

    def intersect(self, l, intersectionPoint, Union=None, QPointF=None, QPoint=None): # real signature unknown; restored from __doc__
        """ intersect(self, l: QLineF, intersectionPoint: Optional[Union[QPointF, QPoint]]) -> QLineF.IntersectType """
        pass

    def intersects(self, l): # real signature unknown; restored from __doc__
        """ intersects(self, l: QLineF) -> (QLineF.IntersectType, Optional[QPointF]) """
        pass

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def length(self): # real signature unknown; restored from __doc__
        """ length(self) -> float """
        return 0.0

    def normalVector(self): # real signature unknown; restored from __doc__
        """ normalVector(self) -> QLineF """
        return QLineF

    def p1(self): # real signature unknown; restored from __doc__
        """ p1(self) -> QPointF """
        return QPointF

    def p2(self): # real signature unknown; restored from __doc__
        """ p2(self) -> QPointF """
        return QPointF

    def pointAt(self, t): # real signature unknown; restored from __doc__
        """ pointAt(self, t: float) -> QPointF """
        return QPointF

    def setAngle(self, angle): # real signature unknown; restored from __doc__
        """ setAngle(self, angle: float) """
        pass

    def setLength(self, len): # real signature unknown; restored from __doc__
        """ setLength(self, len: float) """
        pass

    def setLine(self, aX1, aY1, aX2, aY2): # real signature unknown; restored from __doc__
        """ setLine(self, aX1: float, aY1: float, aX2: float, aY2: float) """
        pass

    def setP1(self, aP1, QPointF=None, QPoint=None): # real signature unknown; restored from __doc__
        """ setP1(self, aP1: Union[QPointF, QPoint]) """
        pass

    def setP2(self, aP2, QPointF=None, QPoint=None): # real signature unknown; restored from __doc__
        """ setP2(self, aP2: Union[QPointF, QPoint]) """
        pass

    def setPoints(self, aP1, QPointF=None, QPoint=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setPoints(self, aP1: Union[QPointF, QPoint], aP2: Union[QPointF, QPoint]) """
        pass

    def toLine(self): # real signature unknown; restored from __doc__
        """ toLine(self) -> QLine """
        return QLine

    def translate(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        translate(self, point: Union[QPointF, QPoint])
        translate(self, adx: float, ady: float)
        """
        pass

    def translated(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        translated(self, p: Union[QPointF, QPoint]) -> QLineF
        translated(self, adx: float, ady: float) -> QLineF
        """
        return QLineF

    def unitVector(self): # real signature unknown; restored from __doc__
        """ unitVector(self) -> QLineF """
        return QLineF

    def x1(self): # real signature unknown; restored from __doc__
        """ x1(self) -> float """
        return 0.0

    def x2(self): # real signature unknown; restored from __doc__
        """ x2(self) -> float """
        return 0.0

    def y1(self): # real signature unknown; restored from __doc__
        """ y1(self) -> float """
        return 0.0

    def y2(self): # real signature unknown; restored from __doc__
        """ y2(self) -> float """
        return 0.0

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ True if self else False """
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

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    BoundedIntersection = 1
    NoIntersection = 0
    UnboundedIntersection = 2
    __hash__ = None


