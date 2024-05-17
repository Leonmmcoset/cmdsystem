# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QTransform(__sip.simplewrapper):
    """
    QTransform()
    QTransform(m11: float, m12: float, m13: float, m21: float, m22: float, m23: float, m31: float, m32: float, m33: float = 1)
    QTransform(h11: float, h12: float, h13: float, h21: float, h22: float, h23: float)
    QTransform(other: QTransform)
    """
    def adjoint(self): # real signature unknown; restored from __doc__
        """ adjoint(self) -> QTransform """
        return QTransform

    def determinant(self): # real signature unknown; restored from __doc__
        """ determinant(self) -> float """
        return 0.0

    def dx(self): # real signature unknown; restored from __doc__
        """ dx(self) -> float """
        return 0.0

    def dy(self): # real signature unknown; restored from __doc__
        """ dy(self) -> float """
        return 0.0

    def fromScale(self, dx, dy): # real signature unknown; restored from __doc__
        """ fromScale(dx: float, dy: float) -> QTransform """
        return QTransform

    def fromTranslate(self, dx, dy): # real signature unknown; restored from __doc__
        """ fromTranslate(dx: float, dy: float) -> QTransform """
        return QTransform

    def inverted(self): # real signature unknown; restored from __doc__
        """ inverted(self) -> (QTransform, Optional[bool]) """
        pass

    def isAffine(self): # real signature unknown; restored from __doc__
        """ isAffine(self) -> bool """
        return False

    def isIdentity(self): # real signature unknown; restored from __doc__
        """ isIdentity(self) -> bool """
        return False

    def isInvertible(self): # real signature unknown; restored from __doc__
        """ isInvertible(self) -> bool """
        return False

    def isRotating(self): # real signature unknown; restored from __doc__
        """ isRotating(self) -> bool """
        return False

    def isScaling(self): # real signature unknown; restored from __doc__
        """ isScaling(self) -> bool """
        return False

    def isTranslating(self): # real signature unknown; restored from __doc__
        """ isTranslating(self) -> bool """
        return False

    def m11(self): # real signature unknown; restored from __doc__
        """ m11(self) -> float """
        return 0.0

    def m12(self): # real signature unknown; restored from __doc__
        """ m12(self) -> float """
        return 0.0

    def m13(self): # real signature unknown; restored from __doc__
        """ m13(self) -> float """
        return 0.0

    def m21(self): # real signature unknown; restored from __doc__
        """ m21(self) -> float """
        return 0.0

    def m22(self): # real signature unknown; restored from __doc__
        """ m22(self) -> float """
        return 0.0

    def m23(self): # real signature unknown; restored from __doc__
        """ m23(self) -> float """
        return 0.0

    def m31(self): # real signature unknown; restored from __doc__
        """ m31(self) -> float """
        return 0.0

    def m32(self): # real signature unknown; restored from __doc__
        """ m32(self) -> float """
        return 0.0

    def m33(self): # real signature unknown; restored from __doc__
        """ m33(self) -> float """
        return 0.0

    def map(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        map(self, x: int, y: int) -> (Optional[int], Optional[int])
        map(self, x: float, y: float) -> (Optional[float], Optional[float])
        map(self, p: QPoint) -> QPoint
        map(self, p: Union[QPointF, QPoint]) -> QPointF
        map(self, l: QLine) -> QLine
        map(self, l: QLineF) -> QLineF
        map(self, a: QPolygonF) -> QPolygonF
        map(self, a: QPolygon) -> QPolygon
        map(self, r: QRegion) -> QRegion
        map(self, p: QPainterPath) -> QPainterPath
        """
        return QPolygonF or QPolygon or QRegion or QPainterPath

    def mapRect(self, a0): # real signature unknown; restored from __doc__ with multiple overloads
        """
        mapRect(self, a0: QRect) -> QRect
        mapRect(self, a0: QRectF) -> QRectF
        """
        pass

    def mapToPolygon(self, r): # real signature unknown; restored from __doc__
        """ mapToPolygon(self, r: QRect) -> QPolygon """
        return QPolygon

    def quadToQuad(self, one, two, result): # real signature unknown; restored from __doc__
        """ quadToQuad(one: QPolygonF, two: QPolygonF, result: QTransform) -> bool """
        return False

    def quadToSquare(self, quad, result): # real signature unknown; restored from __doc__
        """ quadToSquare(quad: QPolygonF, result: QTransform) -> bool """
        return False

    def reset(self): # real signature unknown; restored from __doc__
        """ reset(self) """
        pass

    def rotate(self, angle, axis=None): # real signature unknown; restored from __doc__
        """ rotate(self, angle: float, axis: Qt.Axis = Qt.ZAxis) -> QTransform """
        return QTransform

    def rotateRadians(self, angle, axis=None): # real signature unknown; restored from __doc__
        """ rotateRadians(self, angle: float, axis: Qt.Axis = Qt.ZAxis) -> QTransform """
        return QTransform

    def scale(self, sx, sy): # real signature unknown; restored from __doc__
        """ scale(self, sx: float, sy: float) -> QTransform """
        return QTransform

    def setMatrix(self, m11, m12, m13, m21, m22, m23, m31, m32, m33): # real signature unknown; restored from __doc__
        """ setMatrix(self, m11: float, m12: float, m13: float, m21: float, m22: float, m23: float, m31: float, m32: float, m33: float) """
        pass

    def shear(self, sh, sv): # real signature unknown; restored from __doc__
        """ shear(self, sh: float, sv: float) -> QTransform """
        return QTransform

    def squareToQuad(self, square, result): # real signature unknown; restored from __doc__
        """ squareToQuad(square: QPolygonF, result: QTransform) -> bool """
        return False

    def translate(self, dx, dy): # real signature unknown; restored from __doc__
        """ translate(self, dx: float, dy: float) -> QTransform """
        return QTransform

    def transposed(self): # real signature unknown; restored from __doc__
        """ transposed(self) -> QTransform """
        return QTransform

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> QTransform.TransformationType """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
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

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __iadd__(self, *args, **kwargs): # real signature unknown
        """ Return self+=value. """
        pass

    def __imatmul__(self, *args, **kwargs): # real signature unknown
        """ Return self@=value. """
        pass

    def __imul__(self, *args, **kwargs): # real signature unknown
        """ Return self*=value. """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __isub__(self, *args, **kwargs): # real signature unknown
        """ Return self-=value. """
        pass

    def __itruediv__(self, *args, **kwargs): # real signature unknown
        """ Return self/=value. """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __matmul__(self, *args, **kwargs): # real signature unknown
        """ Return self@value. """
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __rmatmul__(self, *args, **kwargs): # real signature unknown
        """ Return value@self. """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __rtruediv__(self, *args, **kwargs): # real signature unknown
        """ Return value/self. """
        pass

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    def __truediv__(self, *args, **kwargs): # real signature unknown
        """ Return self/value. """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    TxNone = 0
    TxProject = 16
    TxRotate = 4
    TxScale = 2
    TxShear = 8
    TxTranslate = 1


