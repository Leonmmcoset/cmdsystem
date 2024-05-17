# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QFontMetricsF(__sip.simplewrapper):
    """
    QFontMetricsF(a0: QFont)
    QFontMetricsF(a0: QFont, pd: Optional[QPaintDevice])
    QFontMetricsF(a0: QFontMetrics)
    QFontMetricsF(a0: QFontMetricsF)
    """
    def ascent(self): # real signature unknown; restored from __doc__
        """ ascent(self) -> float """
        return 0.0

    def averageCharWidth(self): # real signature unknown; restored from __doc__
        """ averageCharWidth(self) -> float """
        return 0.0

    def boundingRect(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        boundingRect(self, string: Optional[str]) -> QRectF
        boundingRect(self, rect: QRectF, flags: int, text: Optional[str], tabStops: int = 0, tabArray: Optional[List[int]] = None) -> QRectF
        """
        pass

    def boundingRectChar(self, a0): # real signature unknown; restored from __doc__
        """ boundingRectChar(self, a0: str) -> QRectF """
        pass

    def capHeight(self): # real signature unknown; restored from __doc__
        """ capHeight(self) -> float """
        return 0.0

    def descent(self): # real signature unknown; restored from __doc__
        """ descent(self) -> float """
        return 0.0

    def elidedText(self, text, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ elidedText(self, text: Optional[str], mode: Qt.TextElideMode, width: float, flags: int = 0) -> str """
        pass

    def fontDpi(self): # real signature unknown; restored from __doc__
        """ fontDpi(self) -> float """
        return 0.0

    def height(self): # real signature unknown; restored from __doc__
        """ height(self) -> float """
        return 0.0

    def horizontalAdvance(self, string, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ horizontalAdvance(self, string: Optional[str], length: int = -1) -> float """
        pass

    def inFont(self, a0): # real signature unknown; restored from __doc__
        """ inFont(self, a0: str) -> bool """
        return False

    def inFontUcs4(self, character): # real signature unknown; restored from __doc__
        """ inFontUcs4(self, character: int) -> bool """
        return False

    def leading(self): # real signature unknown; restored from __doc__
        """ leading(self) -> float """
        return 0.0

    def leftBearing(self, a0): # real signature unknown; restored from __doc__
        """ leftBearing(self, a0: str) -> float """
        return 0.0

    def lineSpacing(self): # real signature unknown; restored from __doc__
        """ lineSpacing(self) -> float """
        return 0.0

    def lineWidth(self): # real signature unknown; restored from __doc__
        """ lineWidth(self) -> float """
        return 0.0

    def maxWidth(self): # real signature unknown; restored from __doc__
        """ maxWidth(self) -> float """
        return 0.0

    def minLeftBearing(self): # real signature unknown; restored from __doc__
        """ minLeftBearing(self) -> float """
        return 0.0

    def minRightBearing(self): # real signature unknown; restored from __doc__
        """ minRightBearing(self) -> float """
        return 0.0

    def overlinePos(self): # real signature unknown; restored from __doc__
        """ overlinePos(self) -> float """
        return 0.0

    def rightBearing(self, a0): # real signature unknown; restored from __doc__
        """ rightBearing(self, a0: str) -> float """
        return 0.0

    def size(self, flags, text, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ size(self, flags: int, text: Optional[str], tabStops: int = 0, tabArray: Optional[List[int]] = None) -> QSizeF """
        pass

    def strikeOutPos(self): # real signature unknown; restored from __doc__
        """ strikeOutPos(self) -> float """
        return 0.0

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: QFontMetricsF) """
        pass

    def tightBoundingRect(self, text, p_str=None): # real signature unknown; restored from __doc__
        """ tightBoundingRect(self, text: Optional[str]) -> QRectF """
        pass

    def underlinePos(self): # real signature unknown; restored from __doc__
        """ underlinePos(self) -> float """
        return 0.0

    def width(self, string, p_str=None): # real signature unknown; restored from __doc__
        """ width(self, string: Optional[str]) -> float """
        return 0.0

    def widthChar(self, a0): # real signature unknown; restored from __doc__
        """ widthChar(self, a0: str) -> float """
        return 0.0

    def xHeight(self): # real signature unknown; restored from __doc__
        """ xHeight(self) -> float """
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

    def __init__(self, a0, pd=None, QPaintDevice=None): # real signature unknown; restored from __doc__ with multiple overloads
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


