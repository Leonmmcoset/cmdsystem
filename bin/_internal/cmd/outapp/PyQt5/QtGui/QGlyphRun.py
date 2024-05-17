# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QGlyphRun(__sip.simplewrapper):
    """
    QGlyphRun()
    QGlyphRun(other: QGlyphRun)
    """
    def boundingRect(self): # real signature unknown; restored from __doc__
        """ boundingRect(self) -> QRectF """
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def flags(self): # real signature unknown; restored from __doc__
        """ flags(self) -> QGlyphRun.GlyphRunFlags """
        pass

    def glyphIndexes(self): # real signature unknown; restored from __doc__
        """ glyphIndexes(self) -> List[int] """
        return []

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ isEmpty(self) -> bool """
        return False

    def isRightToLeft(self): # real signature unknown; restored from __doc__
        """ isRightToLeft(self) -> bool """
        return False

    def overline(self): # real signature unknown; restored from __doc__
        """ overline(self) -> bool """
        return False

    def positions(self): # real signature unknown; restored from __doc__
        """ positions(self) -> List[QPointF] """
        return []

    def rawFont(self): # real signature unknown; restored from __doc__
        """ rawFont(self) -> QRawFont """
        return QRawFont

    def setBoundingRect(self, boundingRect): # real signature unknown; restored from __doc__
        """ setBoundingRect(self, boundingRect: QRectF) """
        pass

    def setFlag(self, flag, enabled=True): # real signature unknown; restored from __doc__
        """ setFlag(self, flag: QGlyphRun.GlyphRunFlag, enabled: bool = True) """
        pass

    def setFlags(self, flags, QGlyphRun_GlyphRunFlags=None, QGlyphRun_GlyphRunFlag=None): # real signature unknown; restored from __doc__
        """ setFlags(self, flags: Union[QGlyphRun.GlyphRunFlags, QGlyphRun.GlyphRunFlag]) """
        pass

    def setGlyphIndexes(self, glyphIndexes, p_int=None): # real signature unknown; restored from __doc__
        """ setGlyphIndexes(self, glyphIndexes: Iterable[int]) """
        pass

    def setOverline(self, overline): # real signature unknown; restored from __doc__
        """ setOverline(self, overline: bool) """
        pass

    def setPositions(self, positions, Union=None, QPointF=None, QPoint=None): # real signature unknown; restored from __doc__
        """ setPositions(self, positions: Iterable[Union[QPointF, QPoint]]) """
        pass

    def setRawFont(self, rawFont): # real signature unknown; restored from __doc__
        """ setRawFont(self, rawFont: QRawFont) """
        pass

    def setRightToLeft(self, on): # real signature unknown; restored from __doc__
        """ setRightToLeft(self, on: bool) """
        pass

    def setStrikeOut(self, strikeOut): # real signature unknown; restored from __doc__
        """ setStrikeOut(self, strikeOut: bool) """
        pass

    def setUnderline(self, underline): # real signature unknown; restored from __doc__
        """ setUnderline(self, underline: bool) """
        pass

    def strikeOut(self): # real signature unknown; restored from __doc__
        """ strikeOut(self) -> bool """
        return False

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: QGlyphRun) """
        pass

    def underline(self): # real signature unknown; restored from __doc__
        """ underline(self) -> bool """
        return False

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, other=None): # real signature unknown; restored from __doc__ with multiple overloads
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


    Overline = 1
    RightToLeft = 8
    SplitLigature = 16
    StrikeOut = 4
    Underline = 2
    __hash__ = None


