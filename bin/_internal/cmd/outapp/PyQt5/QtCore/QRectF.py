# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


class QRectF(__sip.simplewrapper):
    """
    QRectF()
    QRectF(atopLeft: Union[QPointF, QPoint], asize: QSizeF)
    QRectF(atopLeft: Union[QPointF, QPoint], abottomRight: Union[QPointF, QPoint])
    QRectF(aleft: float, atop: float, awidth: float, aheight: float)
    QRectF(r: QRect)
    QRectF(a0: QRectF)
    """
    def adjust(self, xp1, yp1, xp2, yp2): # real signature unknown; restored from __doc__
        """ adjust(self, xp1: float, yp1: float, xp2: float, yp2: float) """
        pass

    def adjusted(self, xp1, yp1, xp2, yp2): # real signature unknown; restored from __doc__
        """ adjusted(self, xp1: float, yp1: float, xp2: float, yp2: float) -> QRectF """
        return QRectF

    def bottom(self): # real signature unknown; restored from __doc__
        """ bottom(self) -> float """
        return 0.0

    def bottomLeft(self): # real signature unknown; restored from __doc__
        """ bottomLeft(self) -> QPointF """
        return QPointF

    def bottomRight(self): # real signature unknown; restored from __doc__
        """ bottomRight(self) -> QPointF """
        return QPointF

    def center(self): # real signature unknown; restored from __doc__
        """ center(self) -> QPointF """
        return QPointF

    def contains(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        contains(self, p: Union[QPointF, QPoint]) -> bool
        contains(self, r: QRectF) -> bool
        contains(self, ax: float, ay: float) -> bool
        """
        return False

    def getCoords(self): # real signature unknown; restored from __doc__
        """ getCoords(self) -> (Optional[float], Optional[float], Optional[float], Optional[float]) """
        pass

    def getRect(self): # real signature unknown; restored from __doc__
        """ getRect(self) -> (Optional[float], Optional[float], Optional[float], Optional[float]) """
        pass

    def height(self): # real signature unknown; restored from __doc__
        """ height(self) -> float """
        return 0.0

    def intersected(self, r): # real signature unknown; restored from __doc__
        """ intersected(self, r: QRectF) -> QRectF """
        return QRectF

    def intersects(self, r): # real signature unknown; restored from __doc__
        """ intersects(self, r: QRectF) -> bool """
        return False

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ isEmpty(self) -> bool """
        return False

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def left(self): # real signature unknown; restored from __doc__
        """ left(self) -> float """
        return 0.0

    def marginsAdded(self, margins): # real signature unknown; restored from __doc__
        """ marginsAdded(self, margins: QMarginsF) -> QRectF """
        return QRectF

    def marginsRemoved(self, margins): # real signature unknown; restored from __doc__
        """ marginsRemoved(self, margins: QMarginsF) -> QRectF """
        return QRectF

    def moveBottom(self, pos): # real signature unknown; restored from __doc__
        """ moveBottom(self, pos: float) """
        pass

    def moveBottomLeft(self, p, QPointF=None, QPoint=None): # real signature unknown; restored from __doc__
        """ moveBottomLeft(self, p: Union[QPointF, QPoint]) """
        pass

    def moveBottomRight(self, p, QPointF=None, QPoint=None): # real signature unknown; restored from __doc__
        """ moveBottomRight(self, p: Union[QPointF, QPoint]) """
        pass

    def moveCenter(self, p, QPointF=None, QPoint=None): # real signature unknown; restored from __doc__
        """ moveCenter(self, p: Union[QPointF, QPoint]) """
        pass

    def moveLeft(self, pos): # real signature unknown; restored from __doc__
        """ moveLeft(self, pos: float) """
        pass

    def moveRight(self, pos): # real signature unknown; restored from __doc__
        """ moveRight(self, pos: float) """
        pass

    def moveTo(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        moveTo(self, ax: float, ay: float)
        moveTo(self, p: Union[QPointF, QPoint])
        """
        pass

    def moveTop(self, pos): # real signature unknown; restored from __doc__
        """ moveTop(self, pos: float) """
        pass

    def moveTopLeft(self, p, QPointF=None, QPoint=None): # real signature unknown; restored from __doc__
        """ moveTopLeft(self, p: Union[QPointF, QPoint]) """
        pass

    def moveTopRight(self, p, QPointF=None, QPoint=None): # real signature unknown; restored from __doc__
        """ moveTopRight(self, p: Union[QPointF, QPoint]) """
        pass

    def normalized(self): # real signature unknown; restored from __doc__
        """ normalized(self) -> QRectF """
        return QRectF

    def right(self): # real signature unknown; restored from __doc__
        """ right(self) -> float """
        return 0.0

    def setBottom(self, pos): # real signature unknown; restored from __doc__
        """ setBottom(self, pos: float) """
        pass

    def setBottomLeft(self, p, QPointF=None, QPoint=None): # real signature unknown; restored from __doc__
        """ setBottomLeft(self, p: Union[QPointF, QPoint]) """
        pass

    def setBottomRight(self, p, QPointF=None, QPoint=None): # real signature unknown; restored from __doc__
        """ setBottomRight(self, p: Union[QPointF, QPoint]) """
        pass

    def setCoords(self, xp1, yp1, xp2, yp2): # real signature unknown; restored from __doc__
        """ setCoords(self, xp1: float, yp1: float, xp2: float, yp2: float) """
        pass

    def setHeight(self, ah): # real signature unknown; restored from __doc__
        """ setHeight(self, ah: float) """
        pass

    def setLeft(self, pos): # real signature unknown; restored from __doc__
        """ setLeft(self, pos: float) """
        pass

    def setRect(self, ax, ay, aaw, aah): # real signature unknown; restored from __doc__
        """ setRect(self, ax: float, ay: float, aaw: float, aah: float) """
        pass

    def setRight(self, pos): # real signature unknown; restored from __doc__
        """ setRight(self, pos: float) """
        pass

    def setSize(self, s): # real signature unknown; restored from __doc__
        """ setSize(self, s: QSizeF) """
        pass

    def setTop(self, pos): # real signature unknown; restored from __doc__
        """ setTop(self, pos: float) """
        pass

    def setTopLeft(self, p, QPointF=None, QPoint=None): # real signature unknown; restored from __doc__
        """ setTopLeft(self, p: Union[QPointF, QPoint]) """
        pass

    def setTopRight(self, p, QPointF=None, QPoint=None): # real signature unknown; restored from __doc__
        """ setTopRight(self, p: Union[QPointF, QPoint]) """
        pass

    def setWidth(self, aw): # real signature unknown; restored from __doc__
        """ setWidth(self, aw: float) """
        pass

    def setX(self, pos): # real signature unknown; restored from __doc__
        """ setX(self, pos: float) """
        pass

    def setY(self, pos): # real signature unknown; restored from __doc__
        """ setY(self, pos: float) """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ size(self) -> QSizeF """
        return QSizeF

    def toAlignedRect(self): # real signature unknown; restored from __doc__
        """ toAlignedRect(self) -> QRect """
        return QRect

    def top(self): # real signature unknown; restored from __doc__
        """ top(self) -> float """
        return 0.0

    def topLeft(self): # real signature unknown; restored from __doc__
        """ topLeft(self) -> QPointF """
        return QPointF

    def topRight(self): # real signature unknown; restored from __doc__
        """ topRight(self) -> QPointF """
        return QPointF

    def toRect(self): # real signature unknown; restored from __doc__
        """ toRect(self) -> QRect """
        return QRect

    def translate(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        translate(self, dx: float, dy: float)
        translate(self, p: Union[QPointF, QPoint])
        """
        pass

    def translated(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        translated(self, dx: float, dy: float) -> QRectF
        translated(self, p: Union[QPointF, QPoint]) -> QRectF
        """
        return QRectF

    def transposed(self): # real signature unknown; restored from __doc__
        """ transposed(self) -> QRectF """
        return QRectF

    def united(self, r): # real signature unknown; restored from __doc__
        """ united(self, r: QRectF) -> QRectF """
        return QRectF

    def width(self): # real signature unknown; restored from __doc__
        """ width(self) -> float """
        return 0.0

    def x(self): # real signature unknown; restored from __doc__
        """ x(self) -> float """
        return 0.0

    def y(self): # real signature unknown; restored from __doc__
        """ y(self) -> float """
        return 0.0

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __and__(self, *args, **kwargs): # real signature unknown
        """ Return self&value. """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ True if self else False """
        pass

    def __contains__(self, *args, **kwargs): # real signature unknown
        """ Return key in self. """
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

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
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


    __hash__ = None


