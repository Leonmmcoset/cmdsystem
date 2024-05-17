# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QTextLayout(__sip.simplewrapper):
    """
    QTextLayout()
    QTextLayout(text: Optional[str])
    QTextLayout(text: Optional[str], font: QFont, paintDevice: Optional[QPaintDevice] = None)
    QTextLayout(b: QTextBlock)
    """
    def additionalFormats(self): # real signature unknown; restored from __doc__
        """ additionalFormats(self) -> List[QTextLayout.FormatRange] """
        return []

    def beginLayout(self): # real signature unknown; restored from __doc__
        """ beginLayout(self) """
        pass

    def boundingRect(self): # real signature unknown; restored from __doc__
        """ boundingRect(self) -> QRectF """
        pass

    def cacheEnabled(self): # real signature unknown; restored from __doc__
        """ cacheEnabled(self) -> bool """
        return False

    def clearAdditionalFormats(self): # real signature unknown; restored from __doc__
        """ clearAdditionalFormats(self) """
        pass

    def clearFormats(self): # real signature unknown; restored from __doc__
        """ clearFormats(self) """
        pass

    def clearLayout(self): # real signature unknown; restored from __doc__
        """ clearLayout(self) """
        pass

    def createLine(self): # real signature unknown; restored from __doc__
        """ createLine(self) -> QTextLine """
        return QTextLine

    def cursorMoveStyle(self): # real signature unknown; restored from __doc__
        """ cursorMoveStyle(self) -> Qt.CursorMoveStyle """
        pass

    def draw(self, p, QPainter=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ draw(self, p: Optional[QPainter], pos: Union[QPointF, QPoint], selections: Iterable[QTextLayout.FormatRange] = [], clip: QRectF = QRectF()) """
        pass

    def drawCursor(self, p, QPainter=None, *args, **kwargs): # real signature unknown; restored from __doc__ with multiple overloads
        """
        drawCursor(self, p: Optional[QPainter], pos: Union[QPointF, QPoint], cursorPosition: int)
        drawCursor(self, p: Optional[QPainter], pos: Union[QPointF, QPoint], cursorPosition: int, width: int)
        """
        pass

    def endLayout(self): # real signature unknown; restored from __doc__
        """ endLayout(self) """
        pass

    def font(self): # real signature unknown; restored from __doc__
        """ font(self) -> QFont """
        return QFont

    def formats(self): # real signature unknown; restored from __doc__
        """ formats(self) -> List[QTextLayout.FormatRange] """
        return []

    def glyphRuns(self, from_=-1, length=-1): # real signature unknown; restored from __doc__
        """ glyphRuns(self, from_: int = -1, length: int = -1) -> List[QGlyphRun] """
        return []

    def isValidCursorPosition(self, pos): # real signature unknown; restored from __doc__
        """ isValidCursorPosition(self, pos: int) -> bool """
        return False

    def leftCursorPosition(self, oldPos): # real signature unknown; restored from __doc__
        """ leftCursorPosition(self, oldPos: int) -> int """
        return 0

    def lineAt(self, i): # real signature unknown; restored from __doc__
        """ lineAt(self, i: int) -> QTextLine """
        return QTextLine

    def lineCount(self): # real signature unknown; restored from __doc__
        """ lineCount(self) -> int """
        return 0

    def lineForTextPosition(self, pos): # real signature unknown; restored from __doc__
        """ lineForTextPosition(self, pos: int) -> QTextLine """
        return QTextLine

    def maximumWidth(self): # real signature unknown; restored from __doc__
        """ maximumWidth(self) -> float """
        return 0.0

    def minimumWidth(self): # real signature unknown; restored from __doc__
        """ minimumWidth(self) -> float """
        return 0.0

    def nextCursorPosition(self, oldPos, mode=None): # real signature unknown; restored from __doc__
        """ nextCursorPosition(self, oldPos: int, mode: QTextLayout.CursorMode = QTextLayout.SkipCharacters) -> int """
        return 0

    def position(self): # real signature unknown; restored from __doc__
        """ position(self) -> QPointF """
        pass

    def preeditAreaPosition(self): # real signature unknown; restored from __doc__
        """ preeditAreaPosition(self) -> int """
        return 0

    def preeditAreaText(self): # real signature unknown; restored from __doc__
        """ preeditAreaText(self) -> str """
        return ""

    def previousCursorPosition(self, oldPos, mode=None): # real signature unknown; restored from __doc__
        """ previousCursorPosition(self, oldPos: int, mode: QTextLayout.CursorMode = QTextLayout.SkipCharacters) -> int """
        return 0

    def rightCursorPosition(self, oldPos): # real signature unknown; restored from __doc__
        """ rightCursorPosition(self, oldPos: int) -> int """
        return 0

    def setAdditionalFormats(self, overrides, QTextLayout_FormatRange=None): # real signature unknown; restored from __doc__
        """ setAdditionalFormats(self, overrides: Iterable[QTextLayout.FormatRange]) """
        pass

    def setCacheEnabled(self, enable): # real signature unknown; restored from __doc__
        """ setCacheEnabled(self, enable: bool) """
        pass

    def setCursorMoveStyle(self, style): # real signature unknown; restored from __doc__
        """ setCursorMoveStyle(self, style: Qt.CursorMoveStyle) """
        pass

    def setFont(self, f): # real signature unknown; restored from __doc__
        """ setFont(self, f: QFont) """
        pass

    def setFormats(self, overrides, QTextLayout_FormatRange=None): # real signature unknown; restored from __doc__
        """ setFormats(self, overrides: Iterable[QTextLayout.FormatRange]) """
        pass

    def setPosition(self, p, QPointF=None, QPoint=None): # real signature unknown; restored from __doc__
        """ setPosition(self, p: Union[QPointF, QPoint]) """
        pass

    def setPreeditArea(self, position, text, p_str=None): # real signature unknown; restored from __doc__
        """ setPreeditArea(self, position: int, text: Optional[str]) """
        pass

    def setText(self, string, p_str=None): # real signature unknown; restored from __doc__
        """ setText(self, string: Optional[str]) """
        pass

    def setTextOption(self, option): # real signature unknown; restored from __doc__
        """ setTextOption(self, option: QTextOption) """
        pass

    def text(self): # real signature unknown; restored from __doc__
        """ text(self) -> str """
        return ""

    def textOption(self): # real signature unknown; restored from __doc__
        """ textOption(self) -> QTextOption """
        return QTextOption

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    SkipCharacters = 0
    SkipWords = 1


