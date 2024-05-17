# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


class QRect(__sip.simplewrapper):
    """
    QRect()
    QRect(aleft: int, atop: int, awidth: int, aheight: int)
    QRect(atopLeft: QPoint, abottomRight: QPoint)
    QRect(atopLeft: QPoint, asize: QSize)
    QRect(a0: QRect)
    """
    def adjust(self, dx1, dy1, dx2, dy2): # real signature unknown; restored from __doc__
        """ adjust(self, dx1: int, dy1: int, dx2: int, dy2: int) """
        pass

    def adjusted(self, xp1, yp1, xp2, yp2): # real signature unknown; restored from __doc__
        """ adjusted(self, xp1: int, yp1: int, xp2: int, yp2: int) -> QRect """
        return QRect

    def bottom(self): # real signature unknown; restored from __doc__
        """ bottom(self) -> int """
        return 0

    def bottomLeft(self): # real signature unknown; restored from __doc__
        """ bottomLeft(self) -> QPoint """
        return QPoint

    def bottomRight(self): # real signature unknown; restored from __doc__
        """ bottomRight(self) -> QPoint """
        return QPoint

    def center(self): # real signature unknown; restored from __doc__
        """ center(self) -> QPoint """
        return QPoint

    def contains(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        contains(self, point: QPoint, proper: bool = False) -> bool
        contains(self, rectangle: QRect, proper: bool = False) -> bool
        contains(self, ax: int, ay: int, aproper: bool) -> bool
        contains(self, ax: int, ay: int) -> bool
        """
        return False

    def getCoords(self): # real signature unknown; restored from __doc__
        """ getCoords(self) -> (Optional[int], Optional[int], Optional[int], Optional[int]) """
        pass

    def getRect(self): # real signature unknown; restored from __doc__
        """ getRect(self) -> (Optional[int], Optional[int], Optional[int], Optional[int]) """
        pass

    def height(self): # real signature unknown; restored from __doc__
        """ height(self) -> int """
        return 0

    def intersected(self, other): # real signature unknown; restored from __doc__
        """ intersected(self, other: QRect) -> QRect """
        return QRect

    def intersects(self, r): # real signature unknown; restored from __doc__
        """ intersects(self, r: QRect) -> bool """
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
        """ left(self) -> int """
        return 0

    def marginsAdded(self, margins): # real signature unknown; restored from __doc__
        """ marginsAdded(self, margins: QMargins) -> QRect """
        return QRect

    def marginsRemoved(self, margins): # real signature unknown; restored from __doc__
        """ marginsRemoved(self, margins: QMargins) -> QRect """
        return QRect

    def moveBottom(self, pos): # real signature unknown; restored from __doc__
        """ moveBottom(self, pos: int) """
        pass

    def moveBottomLeft(self, p): # real signature unknown; restored from __doc__
        """ moveBottomLeft(self, p: QPoint) """
        pass

    def moveBottomRight(self, p): # real signature unknown; restored from __doc__
        """ moveBottomRight(self, p: QPoint) """
        pass

    def moveCenter(self, p): # real signature unknown; restored from __doc__
        """ moveCenter(self, p: QPoint) """
        pass

    def moveLeft(self, pos): # real signature unknown; restored from __doc__
        """ moveLeft(self, pos: int) """
        pass

    def moveRight(self, pos): # real signature unknown; restored from __doc__
        """ moveRight(self, pos: int) """
        pass

    def moveTo(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        moveTo(self, ax: int, ay: int)
        moveTo(self, p: QPoint)
        """
        pass

    def moveTop(self, pos): # real signature unknown; restored from __doc__
        """ moveTop(self, pos: int) """
        pass

    def moveTopLeft(self, p): # real signature unknown; restored from __doc__
        """ moveTopLeft(self, p: QPoint) """
        pass

    def moveTopRight(self, p): # real signature unknown; restored from __doc__
        """ moveTopRight(self, p: QPoint) """
        pass

    def normalized(self): # real signature unknown; restored from __doc__
        """ normalized(self) -> QRect """
        return QRect

    def right(self): # real signature unknown; restored from __doc__
        """ right(self) -> int """
        return 0

    def setBottom(self, pos): # real signature unknown; restored from __doc__
        """ setBottom(self, pos: int) """
        pass

    def setBottomLeft(self, p): # real signature unknown; restored from __doc__
        """ setBottomLeft(self, p: QPoint) """
        pass

    def setBottomRight(self, p): # real signature unknown; restored from __doc__
        """ setBottomRight(self, p: QPoint) """
        pass

    def setCoords(self, xp1, yp1, xp2, yp2): # real signature unknown; restored from __doc__
        """ setCoords(self, xp1: int, yp1: int, xp2: int, yp2: int) """
        pass

    def setHeight(self, h): # real signature unknown; restored from __doc__
        """ setHeight(self, h: int) """
        pass

    def setLeft(self, pos): # real signature unknown; restored from __doc__
        """ setLeft(self, pos: int) """
        pass

    def setRect(self, ax, ay, aw, ah): # real signature unknown; restored from __doc__
        """ setRect(self, ax: int, ay: int, aw: int, ah: int) """
        pass

    def setRight(self, pos): # real signature unknown; restored from __doc__
        """ setRight(self, pos: int) """
        pass

    def setSize(self, s): # real signature unknown; restored from __doc__
        """ setSize(self, s: QSize) """
        pass

    def setTop(self, pos): # real signature unknown; restored from __doc__
        """ setTop(self, pos: int) """
        pass

    def setTopLeft(self, p): # real signature unknown; restored from __doc__
        """ setTopLeft(self, p: QPoint) """
        pass

    def setTopRight(self, p): # real signature unknown; restored from __doc__
        """ setTopRight(self, p: QPoint) """
        pass

    def setWidth(self, w): # real signature unknown; restored from __doc__
        """ setWidth(self, w: int) """
        pass

    def setX(self, ax): # real signature unknown; restored from __doc__
        """ setX(self, ax: int) """
        pass

    def setY(self, ay): # real signature unknown; restored from __doc__
        """ setY(self, ay: int) """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ size(self) -> QSize """
        return QSize

    def top(self): # real signature unknown; restored from __doc__
        """ top(self) -> int """
        return 0

    def topLeft(self): # real signature unknown; restored from __doc__
        """ topLeft(self) -> QPoint """
        return QPoint

    def topRight(self): # real signature unknown; restored from __doc__
        """ topRight(self) -> QPoint """
        return QPoint

    def translate(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        translate(self, dx: int, dy: int)
        translate(self, p: QPoint)
        """
        pass

    def translated(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        translated(self, dx: int, dy: int) -> QRect
        translated(self, p: QPoint) -> QRect
        """
        return QRect

    def transposed(self): # real signature unknown; restored from __doc__
        """ transposed(self) -> QRect """
        return QRect

    def united(self, r): # real signature unknown; restored from __doc__
        """ united(self, r: QRect) -> QRect """
        return QRect

    def width(self): # real signature unknown; restored from __doc__
        """ width(self) -> int """
        return 0

    def x(self): # real signature unknown; restored from __doc__
        """ x(self) -> int """
        return 0

    def y(self): # real signature unknown; restored from __doc__
        """ y(self) -> int """
        return 0

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


