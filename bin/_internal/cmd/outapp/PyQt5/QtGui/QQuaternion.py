# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QQuaternion(__sip.simplewrapper):
    """
    QQuaternion()
    QQuaternion(aScalar: float, xpos: float, ypos: float, zpos: float)
    QQuaternion(aScalar: float, aVector: QVector3D)
    QQuaternion(aVector: QVector4D)
    QQuaternion(a0: QQuaternion)
    """
    def conjugate(self): # real signature unknown; restored from __doc__
        """ conjugate(self) -> QQuaternion """
        return QQuaternion

    def conjugated(self): # real signature unknown; restored from __doc__
        """ conjugated(self) -> QQuaternion """
        return QQuaternion

    def dotProduct(self, q1, q2): # real signature unknown; restored from __doc__
        """ dotProduct(q1: QQuaternion, q2: QQuaternion) -> float """
        return 0.0

    def fromAxes(self, xAxis, yAxis, zAxis): # real signature unknown; restored from __doc__
        """ fromAxes(xAxis: QVector3D, yAxis: QVector3D, zAxis: QVector3D) -> QQuaternion """
        return QQuaternion

    def fromAxisAndAngle(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        fromAxisAndAngle(axis: QVector3D, angle: float) -> QQuaternion
        fromAxisAndAngle(x: float, y: float, z: float, angle: float) -> QQuaternion
        """
        return QQuaternion

    def fromDirection(self, direction, up): # real signature unknown; restored from __doc__
        """ fromDirection(direction: QVector3D, up: QVector3D) -> QQuaternion """
        return QQuaternion

    def fromEulerAngles(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        fromEulerAngles(pitch: float, yaw: float, roll: float) -> QQuaternion
        fromEulerAngles(eulerAngles: QVector3D) -> QQuaternion
        """
        return QQuaternion

    def fromRotationMatrix(self, rot3x3): # real signature unknown; restored from __doc__
        """ fromRotationMatrix(rot3x3: QMatrix3x3) -> QQuaternion """
        return QQuaternion

    def getAxes(self): # real signature unknown; restored from __doc__
        """ getAxes(self) -> (Optional[QVector3D], Optional[QVector3D], Optional[QVector3D]) """
        pass

    def getAxisAndAngle(self): # real signature unknown; restored from __doc__
        """ getAxisAndAngle(self) -> (Optional[QVector3D], Optional[float]) """
        pass

    def getEulerAngles(self): # real signature unknown; restored from __doc__
        """ getEulerAngles(self) -> (Optional[float], Optional[float], Optional[float]) """
        pass

    def inverted(self): # real signature unknown; restored from __doc__
        """ inverted(self) -> QQuaternion """
        return QQuaternion

    def isIdentity(self): # real signature unknown; restored from __doc__
        """ isIdentity(self) -> bool """
        return False

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def length(self): # real signature unknown; restored from __doc__
        """ length(self) -> float """
        return 0.0

    def lengthSquared(self): # real signature unknown; restored from __doc__
        """ lengthSquared(self) -> float """
        return 0.0

    def nlerp(self, q1, q2, t): # real signature unknown; restored from __doc__
        """ nlerp(q1: QQuaternion, q2: QQuaternion, t: float) -> QQuaternion """
        return QQuaternion

    def normalize(self): # real signature unknown; restored from __doc__
        """ normalize(self) """
        pass

    def normalized(self): # real signature unknown; restored from __doc__
        """ normalized(self) -> QQuaternion """
        return QQuaternion

    def rotatedVector(self, vector): # real signature unknown; restored from __doc__
        """ rotatedVector(self, vector: QVector3D) -> QVector3D """
        return QVector3D

    def rotationTo(self, from_, to): # real signature unknown; restored from __doc__
        """ rotationTo(from_: QVector3D, to: QVector3D) -> QQuaternion """
        return QQuaternion

    def scalar(self): # real signature unknown; restored from __doc__
        """ scalar(self) -> float """
        return 0.0

    def setScalar(self, aScalar): # real signature unknown; restored from __doc__
        """ setScalar(self, aScalar: float) """
        pass

    def setVector(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setVector(self, aVector: QVector3D)
        setVector(self, aX: float, aY: float, aZ: float)
        """
        pass

    def setX(self, aX): # real signature unknown; restored from __doc__
        """ setX(self, aX: float) """
        pass

    def setY(self, aY): # real signature unknown; restored from __doc__
        """ setY(self, aY: float) """
        pass

    def setZ(self, aZ): # real signature unknown; restored from __doc__
        """ setZ(self, aZ: float) """
        pass

    def slerp(self, q1, q2, t): # real signature unknown; restored from __doc__
        """ slerp(q1: QQuaternion, q2: QQuaternion, t: float) -> QQuaternion """
        return QQuaternion

    def toEulerAngles(self): # real signature unknown; restored from __doc__
        """ toEulerAngles(self) -> QVector3D """
        return QVector3D

    def toRotationMatrix(self): # real signature unknown; restored from __doc__
        """ toRotationMatrix(self) -> QMatrix3x3 """
        return QMatrix3x3

    def toVector4D(self): # real signature unknown; restored from __doc__
        """ toVector4D(self) -> QVector4D """
        return QVector4D

    def vector(self): # real signature unknown; restored from __doc__
        """ vector(self) -> QVector3D """
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


