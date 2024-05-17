# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QVector3D(__sip.simplewrapper):
    """
    QVector3D()
    QVector3D(xpos: float, ypos: float, zpos: float)
    QVector3D(point: QPoint)
    QVector3D(point: Union[QPointF, QPoint])
    QVector3D(vector: QVector2D)
    QVector3D(vector: QVector2D, zpos: float)
    QVector3D(vector: QVector4D)
    QVector3D(a0: QVector3D)
    """
    def crossProduct(self, v1, v2): # real signature unknown; restored from __doc__
        """ crossProduct(v1: QVector3D, v2: QVector3D) -> QVector3D """
        return QVector3D

    def distanceToLine(self, point, direction): # real signature unknown; restored from __doc__
        """ distanceToLine(self, point: QVector3D, direction: QVector3D) -> float """
        return 0.0

    def distanceToPlane(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        distanceToPlane(self, plane: QVector3D, normal: QVector3D) -> float
        distanceToPlane(self, plane1: QVector3D, plane2: QVector3D, plane3: QVector3D) -> float
        """
        return 0.0

    def distanceToPoint(self, point): # real signature unknown; restored from __doc__
        """ distanceToPoint(self, point: QVector3D) -> float """
        return 0.0

    def dotProduct(self, v1, v2): # real signature unknown; restored from __doc__
        """ dotProduct(v1: QVector3D, v2: QVector3D) -> float """
        return 0.0

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def length(self): # real signature unknown; restored from __doc__
        """ length(self) -> float """
        return 0.0

    def lengthSquared(self): # real signature unknown; restored from __doc__
        """ lengthSquared(self) -> float """
        return 0.0

    def normal(self, v1, v2, v3=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        normal(v1: QVector3D, v2: QVector3D) -> QVector3D
        normal(v1: QVector3D, v2: QVector3D, v3: QVector3D) -> QVector3D
        """
        return QVector3D

    def normalize(self): # real signature unknown; restored from __doc__
        """ normalize(self) """
        pass

    def normalized(self): # real signature unknown; restored from __doc__
        """ normalized(self) -> QVector3D """
        return QVector3D

    def project(self, modelView, projection, viewport): # real signature unknown; restored from __doc__
        """ project(self, modelView: QMatrix4x4, projection: QMatrix4x4, viewport: QRect) -> QVector3D """
        return QVector3D

    def setX(self, aX): # real signature unknown; restored from __doc__
        """ setX(self, aX: float) """
        pass

    def setY(self, aY): # real signature unknown; restored from __doc__
        """ setY(self, aY: float) """
        pass

    def setZ(self, aZ): # real signature unknown; restored from __doc__
        """ setZ(self, aZ: float) """
        pass

    def toPoint(self): # real signature unknown; restored from __doc__
        """ toPoint(self) -> QPoint """
        pass

    def toPointF(self): # real signature unknown; restored from __doc__
        """ toPointF(self) -> QPointF """
        pass

    def toVector2D(self): # real signature unknown; restored from __doc__
        """ toVector2D(self) -> QVector2D """
        return QVector2D

    def toVector4D(self): # real signature unknown; restored from __doc__
        """ toVector4D(self) -> QVector4D """
        return QVector4D

    def unproject(self, modelView, projection, viewport): # real signature unknown; restored from __doc__
        """ unproject(self, modelView: QMatrix4x4, projection: QMatrix4x4, viewport: QRect) -> QVector3D """
        return QVector3D

    def x(self): # real signature unknown; restored from __doc__
        """ x(self) -> float """
        return 0.0

    def y(self): # real signature unknown; restored from __doc__
        """ y(self) -> float """
        return 0.0

    def z(self): # real signature unknown; restored from __doc__
        """ z(self) -> float """
        return 0.0

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
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


    __hash__ = None


