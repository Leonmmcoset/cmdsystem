# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QRegion(__sip.simplewrapper):
    """
    QRegion()
    QRegion(x: int, y: int, w: int, h: int, type: QRegion.RegionType = QRegion.Rectangle)
    QRegion(r: QRect, type: QRegion.RegionType = QRegion.Rectangle)
    QRegion(a: QPolygon, fillRule: Qt.FillRule = Qt.OddEvenFill)
    QRegion(bitmap: QBitmap)
    QRegion(region: QRegion)
    QRegion(variant: Any)
    """
    def boundingRect(self): # real signature unknown; restored from __doc__
        """ boundingRect(self) -> QRect """
        pass

    def contains(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        contains(self, p: QPoint) -> bool
        contains(self, r: QRect) -> bool
        """
        return False

    def intersected(self, r): # real signature unknown; restored from __doc__ with multiple overloads
        """
        intersected(self, r: QRegion) -> QRegion
        intersected(self, r: QRect) -> QRegion
        """
        return QRegion

    def intersects(self, r): # real signature unknown; restored from __doc__ with multiple overloads
        """
        intersects(self, r: QRegion) -> bool
        intersects(self, r: QRect) -> bool
        """
        return False

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ isEmpty(self) -> bool """
        return False

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def rectCount(self): # real signature unknown; restored from __doc__
        """ rectCount(self) -> int """
        return 0

    def rects(self): # real signature unknown; restored from __doc__
        """ rects(self) -> List[QRect] """
        return []

    def setRects(self, a0, QRect=None): # real signature unknown; restored from __doc__
        """ setRects(self, a0: Iterable[QRect]) """
        pass

    def subtracted(self, r): # real signature unknown; restored from __doc__
        """ subtracted(self, r: QRegion) -> QRegion """
        return QRegion

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: QRegion) """
        pass

    def translate(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        translate(self, dx: int, dy: int)
        translate(self, p: QPoint)
        """
        pass

    def translated(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        translated(self, dx: int, dy: int) -> QRegion
        translated(self, p: QPoint) -> QRegion
        """
        return QRegion

    def united(self, r): # real signature unknown; restored from __doc__ with multiple overloads
        """
        united(self, r: QRegion) -> QRegion
        united(self, r: QRect) -> QRegion
        """
        return QRegion

    def xored(self, r): # real signature unknown; restored from __doc__
        """ xored(self, r: QRegion) -> QRegion """
        return QRegion

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

    def __ixor__(self, *args, **kwargs): # real signature unknown
        """ Return self^=value. """
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

    def __rxor__(self, *args, **kwargs): # real signature unknown
        """ Return value^self. """
        pass

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    def __xor__(self, *args, **kwargs): # real signature unknown
        """ Return self^value. """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    Ellipse = 1
    Rectangle = 0
    __hash__ = None


