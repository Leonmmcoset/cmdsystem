# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QPen(__sip.simplewrapper):
    """
    QPen()
    QPen(a0: Qt.PenStyle)
    QPen(brush: Union[QBrush, Union[QColor, Qt.GlobalColor], QGradient], width: float, style: Qt.PenStyle = Qt.SolidLine, cap: Qt.PenCapStyle = Qt.SquareCap, join: Qt.PenJoinStyle = Qt.BevelJoin)
    QPen(pen: Union[QPen, Union[QColor, Qt.GlobalColor]])
    QPen(variant: Any)
    """
    def brush(self): # real signature unknown; restored from __doc__
        """ brush(self) -> QBrush """
        return QBrush

    def capStyle(self): # real signature unknown; restored from __doc__
        """ capStyle(self) -> Qt.PenCapStyle """
        pass

    def color(self): # real signature unknown; restored from __doc__
        """ color(self) -> QColor """
        return QColor

    def dashOffset(self): # real signature unknown; restored from __doc__
        """ dashOffset(self) -> float """
        return 0.0

    def dashPattern(self): # real signature unknown; restored from __doc__
        """ dashPattern(self) -> List[float] """
        return []

    def isCosmetic(self): # real signature unknown; restored from __doc__
        """ isCosmetic(self) -> bool """
        return False

    def isSolid(self): # real signature unknown; restored from __doc__
        """ isSolid(self) -> bool """
        return False

    def joinStyle(self): # real signature unknown; restored from __doc__
        """ joinStyle(self) -> Qt.PenJoinStyle """
        pass

    def miterLimit(self): # real signature unknown; restored from __doc__
        """ miterLimit(self) -> float """
        return 0.0

    def setBrush(self, brush, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setBrush(self, brush: Union[QBrush, Union[QColor, Qt.GlobalColor], QGradient]) """
        pass

    def setCapStyle(self, pcs): # real signature unknown; restored from __doc__
        """ setCapStyle(self, pcs: Qt.PenCapStyle) """
        pass

    def setColor(self, color, QColor=None, Qt_GlobalColor=None): # real signature unknown; restored from __doc__
        """ setColor(self, color: Union[QColor, Qt.GlobalColor]) """
        pass

    def setCosmetic(self, cosmetic): # real signature unknown; restored from __doc__
        """ setCosmetic(self, cosmetic: bool) """
        pass

    def setDashOffset(self, doffset): # real signature unknown; restored from __doc__
        """ setDashOffset(self, doffset: float) """
        pass

    def setDashPattern(self, pattern, p_float=None): # real signature unknown; restored from __doc__
        """ setDashPattern(self, pattern: Iterable[float]) """
        pass

    def setJoinStyle(self, pcs): # real signature unknown; restored from __doc__
        """ setJoinStyle(self, pcs: Qt.PenJoinStyle) """
        pass

    def setMiterLimit(self, limit): # real signature unknown; restored from __doc__
        """ setMiterLimit(self, limit: float) """
        pass

    def setStyle(self, a0): # real signature unknown; restored from __doc__
        """ setStyle(self, a0: Qt.PenStyle) """
        pass

    def setWidth(self, width): # real signature unknown; restored from __doc__
        """ setWidth(self, width: int) """
        pass

    def setWidthF(self, width): # real signature unknown; restored from __doc__
        """ setWidthF(self, width: float) """
        pass

    def style(self): # real signature unknown; restored from __doc__
        """ style(self) -> Qt.PenStyle """
        pass

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: QPen) """
        pass

    def width(self): # real signature unknown; restored from __doc__
        """ width(self) -> int """
        return 0

    def widthF(self): # real signature unknown; restored from __doc__
        """ widthF(self) -> float """
        return 0.0

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
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

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __hash__ = None


