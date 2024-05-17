# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QTextLine(__sip.simplewrapper):
    """
    QTextLine()
    QTextLine(a0: QTextLine)
    """
    def ascent(self): # real signature unknown; restored from __doc__
        """ ascent(self) -> float """
        return 0.0

    def cursorToX(self, cursorPos, p_int=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ cursorToX(self, cursorPos: Optional[int], edge: QTextLine.Edge = QTextLine.Leading) -> (float, Optional[int]) """
        pass

    def descent(self): # real signature unknown; restored from __doc__
        """ descent(self) -> float """
        return 0.0

    def draw(self, painter, QPainter=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ draw(self, painter: Optional[QPainter], position: Union[QPointF, QPoint], selection: Optional[QTextLayout.FormatRange] = None) """
        pass

    def glyphRuns(self, from_=-1, length=-1): # real signature unknown; restored from __doc__
        """ glyphRuns(self, from_: int = -1, length: int = -1) -> List[QGlyphRun] """
        return []

    def height(self): # real signature unknown; restored from __doc__
        """ height(self) -> float """
        return 0.0

    def horizontalAdvance(self): # real signature unknown; restored from __doc__
        """ horizontalAdvance(self) -> float """
        return 0.0

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def leading(self): # real signature unknown; restored from __doc__
        """ leading(self) -> float """
        return 0.0

    def leadingIncluded(self): # real signature unknown; restored from __doc__
        """ leadingIncluded(self) -> bool """
        return False

    def lineNumber(self): # real signature unknown; restored from __doc__
        """ lineNumber(self) -> int """
        return 0

    def naturalTextRect(self): # real signature unknown; restored from __doc__
        """ naturalTextRect(self) -> QRectF """
        pass

    def naturalTextWidth(self): # real signature unknown; restored from __doc__
        """ naturalTextWidth(self) -> float """
        return 0.0

    def position(self): # real signature unknown; restored from __doc__
        """ position(self) -> QPointF """
        pass

    def rect(self): # real signature unknown; restored from __doc__
        """ rect(self) -> QRectF """
        pass

    def setLeadingIncluded(self, included): # real signature unknown; restored from __doc__
        """ setLeadingIncluded(self, included: bool) """
        pass

    def setLineWidth(self, width): # real signature unknown; restored from __doc__
        """ setLineWidth(self, width: float) """
        pass

    def setNumColumns(self, columns, alignmentWidth=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setNumColumns(self, columns: int)
        setNumColumns(self, columns: int, alignmentWidth: float)
        """
        pass

    def setPosition(self, pos, QPointF=None, QPoint=None): # real signature unknown; restored from __doc__
        """ setPosition(self, pos: Union[QPointF, QPoint]) """
        pass

    def textLength(self): # real signature unknown; restored from __doc__
        """ textLength(self) -> int """
        return 0

    def textStart(self): # real signature unknown; restored from __doc__
        """ textStart(self) -> int """
        return 0

    def width(self): # real signature unknown; restored from __doc__
        """ width(self) -> float """
        return 0.0

    def x(self): # real signature unknown; restored from __doc__
        """ x(self) -> float """
        return 0.0

    def xToCursor(self, x, edge=None): # real signature unknown; restored from __doc__
        """ xToCursor(self, x: float, edge: QTextLine.CursorPosition = QTextLine.CursorBetweenCharacters) -> int """
        return 0

    def y(self): # real signature unknown; restored from __doc__
        """ y(self) -> float """
        return 0.0

    def __init__(self, a0=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    CursorBetweenCharacters = 0
    CursorOnCharacter = 1
    Leading = 0
    Trailing = 1


