# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QPolygon(__sip.simplewrapper):
    """
    QPolygon()
    QPolygon(a: QPolygon)
    QPolygon(points: List[int])
    QPolygon(v: Iterable[QPoint])
    QPolygon(rectangle: QRect, closed: bool = False)
    QPolygon(asize: int)
    QPolygon(variant: Any)
    """
    def append(self, value): # real signature unknown; restored from __doc__
        """ append(self, value: QPoint) """
        pass

    def at(self, i): # real signature unknown; restored from __doc__
        """ at(self, i: int) -> QPoint """
        pass

    def boundingRect(self): # real signature unknown; restored from __doc__
        """ boundingRect(self) -> QRect """
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def contains(self, value): # real signature unknown; restored from __doc__
        """ contains(self, value: QPoint) -> bool """
        return False

    def containsPoint(self, pt, fillRule): # real signature unknown; restored from __doc__
        """ containsPoint(self, pt: QPoint, fillRule: Qt.FillRule) -> bool """
        return False

    def count(self, value=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        count(self, value: QPoint) -> int
        count(self) -> int
        """
        return 0

    def data(self): # real signature unknown; restored from __doc__
        """ data(self) -> Optional[PyQt5.sip.voidptr] """
        pass

    def fill(self, value, size=-1): # real signature unknown; restored from __doc__
        """ fill(self, value: QPoint, size: int = -1) """
        pass

    def first(self): # real signature unknown; restored from __doc__
        """ first(self) -> QPoint """
        pass

    def indexOf(self, value, from_=0): # real signature unknown; restored from __doc__
        """ indexOf(self, value: QPoint, from_: int = 0) -> int """
        return 0

    def insert(self, i, value): # real signature unknown; restored from __doc__
        """ insert(self, i: int, value: QPoint) """
        pass

    def intersected(self, r): # real signature unknown; restored from __doc__
        """ intersected(self, r: QPolygon) -> QPolygon """
        return QPolygon

    def intersects(self, r): # real signature unknown; restored from __doc__
        """ intersects(self, r: QPolygon) -> bool """
        return False

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ isEmpty(self) -> bool """
        return False

    def last(self): # real signature unknown; restored from __doc__
        """ last(self) -> QPoint """
        pass

    def lastIndexOf(self, value, from_=-1): # real signature unknown; restored from __doc__
        """ lastIndexOf(self, value: QPoint, from_: int = -1) -> int """
        return 0

    def mid(self, pos, length=-1): # real signature unknown; restored from __doc__
        """ mid(self, pos: int, length: int = -1) -> QPolygon """
        return QPolygon

    def point(self, index): # real signature unknown; restored from __doc__
        """ point(self, index: int) -> QPoint """
        pass

    def prepend(self, value): # real signature unknown; restored from __doc__
        """ prepend(self, value: QPoint) """
        pass

    def putPoints(self, index, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        putPoints(self, index: int, firstx: int, firsty: int, *args: int)
        putPoints(self, index: int, nPoints: int, fromPolygon: QPolygon, from_: int = 0)
        """
        pass

    def remove(self, i, count=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        remove(self, i: int)
        remove(self, i: int, count: int)
        """
        pass

    def replace(self, i, value): # real signature unknown; restored from __doc__
        """ replace(self, i: int, value: QPoint) """
        pass

    def setPoint(self, index, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setPoint(self, index: int, pt: QPoint)
        setPoint(self, index: int, x: int, y: int)
        """
        pass

    def setPoints(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setPoints(self, points: List[int])
        setPoints(self, firstx: int, firsty: int, *args: int)
        """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ size(self) -> int """
        return 0

    def subtracted(self, r): # real signature unknown; restored from __doc__
        """ subtracted(self, r: QPolygon) -> QPolygon """
        return QPolygon

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: QPolygon) """
        pass

    def translate(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        translate(self, dx: int, dy: int)
        translate(self, offset: QPoint)
        """
        pass

    def translated(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        translated(self, dx: int, dy: int) -> QPolygon
        translated(self, offset: QPoint) -> QPolygon
        """
        return QPolygon

    def united(self, r): # real signature unknown; restored from __doc__
        """ united(self, r: QPolygon) -> QPolygon """
        return QPolygon

    def value(self, i, defaultValue=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        value(self, i: int) -> QPoint
        value(self, i: int, defaultValue: QPoint) -> QPoint
        """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __contains__(self, *args, **kwargs): # real signature unknown
        """ Return key in self. """
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
        """ Implement self+=value. """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lshift__(self, *args, **kwargs): # real signature unknown
        """ Return self<<value. """
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

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __rlshift__(self, *args, **kwargs): # real signature unknown
        """ Return value<<self. """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __setitem__(self, *args, **kwargs): # real signature unknown
        """ Set self[key] to value. """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __hash__ = None


