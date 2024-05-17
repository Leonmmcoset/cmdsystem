# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


class QSize(__sip.simplewrapper):
    """
    QSize()
    QSize(w: int, h: int)
    QSize(a0: QSize)
    """
    def boundedTo(self, otherSize): # real signature unknown; restored from __doc__
        """ boundedTo(self, otherSize: QSize) -> QSize """
        return QSize

    def expandedTo(self, otherSize): # real signature unknown; restored from __doc__
        """ expandedTo(self, otherSize: QSize) -> QSize """
        return QSize

    def grownBy(self, m): # real signature unknown; restored from __doc__
        """ grownBy(self, m: QMargins) -> QSize """
        return QSize

    def height(self): # real signature unknown; restored from __doc__
        """ height(self) -> int """
        return 0

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ isEmpty(self) -> bool """
        return False

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def scale(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        scale(self, s: QSize, mode: Qt.AspectRatioMode)
        scale(self, w: int, h: int, mode: Qt.AspectRatioMode)
        """
        pass

    def scaled(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        scaled(self, s: QSize, mode: Qt.AspectRatioMode) -> QSize
        scaled(self, w: int, h: int, mode: Qt.AspectRatioMode) -> QSize
        """
        return QSize

    def setHeight(self, h): # real signature unknown; restored from __doc__
        """ setHeight(self, h: int) """
        pass

    def setWidth(self, w): # real signature unknown; restored from __doc__
        """ setWidth(self, w: int) """
        pass

    def shrunkBy(self, m): # real signature unknown; restored from __doc__
        """ shrunkBy(self, m: QMargins) -> QSize """
        return QSize

    def transpose(self): # real signature unknown; restored from __doc__
        """ transpose(self) """
        pass

    def transposed(self): # real signature unknown; restored from __doc__
        """ transposed(self) -> QSize """
        return QSize

    def width(self): # real signature unknown; restored from __doc__
        """ width(self) -> int """
        return 0

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

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


