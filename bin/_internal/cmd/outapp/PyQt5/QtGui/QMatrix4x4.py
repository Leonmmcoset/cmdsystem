# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QMatrix4x4(__sip.simplewrapper):
    """
    QMatrix4x4()
    QMatrix4x4(values: Sequence[float])
    QMatrix4x4(m11: float, m12: float, m13: float, m14: float, m21: float, m22: float, m23: float, m24: float, m31: float, m32: float, m33: float, m34: float, m41: float, m42: float, m43: float, m44: float)
    QMatrix4x4(transform: QTransform)
    QMatrix4x4(a0: QMatrix4x4)
    """
    def column(self, index): # real signature unknown; restored from __doc__
        """ column(self, index: int) -> QVector4D """
        return QVector4D

    def copyDataTo(self): # real signature unknown; restored from __doc__
        """ copyDataTo(self) -> List[float] """
        return []

    def data(self): # real signature unknown; restored from __doc__
        """ data(self) -> List[float] """
        return []

    def determinant(self): # real signature unknown; restored from __doc__
        """ determinant(self) -> float """
        return 0.0

    def fill(self, value): # real signature unknown; restored from __doc__
        """ fill(self, value: float) """
        pass

    def frustum(self, left, right, bottom, top, nearPlane, farPlane): # real signature unknown; restored from __doc__
        """ frustum(self, left: float, right: float, bottom: float, top: float, nearPlane: float, farPlane: float) """
        pass

    def inverted(self): # real signature unknown; restored from __doc__
        """ inverted(self) -> (QMatrix4x4, Optional[bool]) """
        pass

    def isAffine(self): # real signature unknown; restored from __doc__
        """ isAffine(self) -> bool """
        return False

    def isIdentity(self): # real signature unknown; restored from __doc__
        """ isIdentity(self) -> bool """
        return False

    def lookAt(self, eye, center, up): # real signature unknown; restored from __doc__
        """ lookAt(self, eye: QVector3D, center: QVector3D, up: QVector3D) """
        pass

    def map(self, point, QPointF=None, QPoint=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        map(self, point: QPoint) -> QPoint
        map(self, point: Union[QPointF, QPoint]) -> QPointF
        map(self, point: QVector3D) -> QVector3D
        map(self, point: QVector4D) -> QVector4D
        """
        return QVector3D or QVector4D

    def mapRect(self, rect): # real signature unknown; restored from __doc__ with multiple overloads
        """
        mapRect(self, rect: QRect) -> QRect
        mapRect(self, rect: QRectF) -> QRectF
        """
        pass

    def mapVector(self, vector): # real signature unknown; restored from __doc__
        """ mapVector(self, vector: QVector3D) -> QVector3D """
        return QVector3D

    def normalMatrix(self): # real signature unknown; restored from __doc__
        """ normalMatrix(self) -> QMatrix3x3 """
        return QMatrix3x3

    def optimize(self): # real signature unknown; restored from __doc__
        """ optimize(self) """
        pass

    def ortho(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        ortho(self, rect: QRect)
        ortho(self, rect: QRectF)
        ortho(self, left: float, right: float, bottom: float, top: float, nearPlane: float, farPlane: float)
        """
        pass

    def perspective(self, angle, aspect, nearPlane, farPlane): # real signature unknown; restored from __doc__
        """ perspective(self, angle: float, aspect: float, nearPlane: float, farPlane: float) """
        pass

    def rotate(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        rotate(self, angle: float, vector: QVector3D)
        rotate(self, angle: float, x: float, y: float, z: float = 0)
        rotate(self, quaternion: QQuaternion)
        """
        pass

    def row(self, index): # real signature unknown; restored from __doc__
        """ row(self, index: int) -> QVector4D """
        return QVector4D

    def scale(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        scale(self, vector: QVector3D)
        scale(self, x: float, y: float)
        scale(self, x: float, y: float, z: float)
        scale(self, factor: float)
        """
        pass

    def setColumn(self, index, value): # real signature unknown; restored from __doc__
        """ setColumn(self, index: int, value: QVector4D) """
        pass

    def setRow(self, index, value): # real signature unknown; restored from __doc__
        """ setRow(self, index: int, value: QVector4D) """
        pass

    def setToIdentity(self): # real signature unknown; restored from __doc__
        """ setToIdentity(self) """
        pass

    def toTransform(self, distanceToPlane=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        toTransform(self) -> QTransform
        toTransform(self, distanceToPlane: float) -> QTransform
        """
        return QTransform

    def translate(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        translate(self, vector: QVector3D)
        translate(self, x: float, y: float)
        translate(self, x: float, y: float, z: float)
        """
        pass

    def transposed(self): # real signature unknown; restored from __doc__
        """ transposed(self) -> QMatrix4x4 """
        return QMatrix4x4

    def viewport(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        viewport(self, left: float, bottom: float, width: float, height: float, nearPlane: float = 0, farPlane: float = 1)
        viewport(self, rect: QRectF)
        """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __delitem__(self, *args, **kwargs): # real signature unknown
        """ Delete self[key]. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
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

    def __neg__(self, *args, **kwargs): # real signature unknown
        """ -self """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
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

    def __setitem__(self, *args, **kwargs): # real signature unknown
        """ Set self[key] to value. """
        pass

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    def __truediv__(self, *args, **kwargs): # real signature unknown
        """ Return self/value. """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __hash__ = None


