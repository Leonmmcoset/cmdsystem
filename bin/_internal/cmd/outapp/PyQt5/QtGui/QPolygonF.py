# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QPolygonF(__sip.simplewrapper):
    """
    QPolygonF()
    QPolygonF(a: QPolygonF)
    QPolygonF(v: Iterable[Union[QPointF, QPoint]])
    QPolygonF(r: QRectF)
    QPolygonF(a: QPolygon)
    QPolygonF(asize: int)
    """
    def append(self, value, QPointF=None, QPoint=None): # real signature unknown; restored from __doc__
        """ append(self, value: Union[QPointF, QPoint]) """
        pass

    def at(self, i): # real signature unknown; restored from __doc__
        """ at(self, i: int) -> QPointF """
        pass

    def boundingRect(self): # real signature unknown; restored from __doc__
        """ boundingRect(self) -> QRectF """
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def contains(self, value, QPointF=None, QPoint=None): # real signature unknown; restored from __doc__
        """ contains(self, value: Union[QPointF, QPoint]) -> bool """
        return False

    def containsPoint(self, pt, QPointF=None, QPoint=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ containsPoint(self, pt: Union[QPointF, QPoint], fillRule: Qt.FillRule) -> bool """
        pass

    def count(self, value=None, QPointF=None, QPoint=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        count(self, value: Union[QPointF, QPoint]) -> int
        count(self) -> int
        """
        return 0

    def data(self): # real signature unknown; restored from __doc__
        """ data(self) -> Optional[PyQt5.sip.voidptr] """
        pass

    def fill(self, value, QPointF=None, QPoint=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ fill(self, value: Union[QPointF, QPoint], size: int = -1) """
        pass

    def first(self): # real signature unknown; restored from __doc__
        """ first(self) -> QPointF """
        pass

    def indexOf(self, value, QPointF=None, QPoint=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ indexOf(self, value: Union[QPointF, QPoint], from_: int = 0) -> int """
        pass

    def insert(self, i, value, QPointF=None, QPoint=None): # real signature unknown; restored from __doc__
        """ insert(self, i: int, value: Union[QPointF, QPoint]) """
        pass

    def intersected(self, r): # real signature unknown; restored from __doc__
        """ intersected(self, r: QPolygonF) -> QPolygonF """
        return QPolygonF

    def intersects(self, r): # real signature unknown; restored from __doc__
        """ intersects(self, r: QPolygonF) -> bool """
        return False

    def isClosed(self): # real signature unknown; restored from __doc__
        """ isClosed(self) -> bool """
        return False

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ isEmpty(self) -> bool """
        return False

    def last(self): # real signature unknown; restored from __doc__
        """ last(self) -> QPointF """
        pass

    def lastIndexOf(self, value, QPointF=None, QPoint=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ lastIndexOf(self, value: Union[QPointF, QPoint], from_: int = -1) -> int """
        pass

    def mid(self, pos, length=-1): # real signature unknown; restored from __doc__
        """ mid(self, pos: int, length: int = -1) -> QPolygonF """
        return QPolygonF

    def prepend(self, value, QPointF=None, QPoint=None): # real signature unknown; restored from __doc__
        """ prepend(self, value: Union[QPointF, QPoint]) """
        pass

    def remove(self, i, count=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        remove(self, i: int)
        remove(self, i: int, count: int)
        """
        pass

    def replace(self, i, value, QPointF=None, QPoint=None): # real signature unknown; restored from __doc__
        """ replace(self, i: int, value: Union[QPointF, QPoint]) """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ size(self) -> int """
        return 0

    def subtracted(self, r): # real signature unknown; restored from __doc__
        """ subtracted(self, r: QPolygonF) -> QPolygonF """
        return QPolygonF

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: QPolygonF) """
        pass

    def toPolygon(self): # real signature unknown; restored from __doc__
        """ toPolygon(self) -> QPolygon """
        return QPolygon

    def translate(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        translate(self, offset: Union[QPointF, QPoint])
        translate(self, dx: float, dy: float)
        """
        pass

    def translated(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        translated(self, offset: Union[QPointF, QPoint]) -> QPolygonF
        translated(self, dx: float, dy: float) -> QPolygonF
        """
        return QPolygonF

    def united(self, r): # real signature unknown; restored from __doc__
        """ united(self, r: QPolygonF) -> QPolygonF """
        return QPolygonF

    def value(self, i, defaultValue=None, QPointF=None, QPoint=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        value(self, i: int) -> QPointF
        value(self, i: int, defaultValue: Union[QPointF, QPoint]) -> QPointF
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


