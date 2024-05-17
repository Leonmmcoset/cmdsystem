# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QTextCursor(__sip.simplewrapper):
    """
    QTextCursor()
    QTextCursor(document: Optional[QTextDocument])
    QTextCursor(frame: Optional[QTextFrame])
    QTextCursor(block: QTextBlock)
    QTextCursor(cursor: QTextCursor)
    """
    def anchor(self): # real signature unknown; restored from __doc__
        """ anchor(self) -> int """
        return 0

    def atBlockEnd(self): # real signature unknown; restored from __doc__
        """ atBlockEnd(self) -> bool """
        return False

    def atBlockStart(self): # real signature unknown; restored from __doc__
        """ atBlockStart(self) -> bool """
        return False

    def atEnd(self): # real signature unknown; restored from __doc__
        """ atEnd(self) -> bool """
        return False

    def atStart(self): # real signature unknown; restored from __doc__
        """ atStart(self) -> bool """
        return False

    def beginEditBlock(self): # real signature unknown; restored from __doc__
        """ beginEditBlock(self) """
        pass

    def block(self): # real signature unknown; restored from __doc__
        """ block(self) -> QTextBlock """
        return QTextBlock

    def blockCharFormat(self): # real signature unknown; restored from __doc__
        """ blockCharFormat(self) -> QTextCharFormat """
        return QTextCharFormat

    def blockFormat(self): # real signature unknown; restored from __doc__
        """ blockFormat(self) -> QTextBlockFormat """
        return QTextBlockFormat

    def blockNumber(self): # real signature unknown; restored from __doc__
        """ blockNumber(self) -> int """
        return 0

    def charFormat(self): # real signature unknown; restored from __doc__
        """ charFormat(self) -> QTextCharFormat """
        return QTextCharFormat

    def clearSelection(self): # real signature unknown; restored from __doc__
        """ clearSelection(self) """
        pass

    def columnNumber(self): # real signature unknown; restored from __doc__
        """ columnNumber(self) -> int """
        return 0

    def createList(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        createList(self, format: QTextListFormat) -> Optional[QTextList]
        createList(self, style: QTextListFormat.Style) -> Optional[QTextList]
        """
        pass

    def currentFrame(self): # real signature unknown; restored from __doc__
        """ currentFrame(self) -> Optional[QTextFrame] """
        pass

    def currentList(self): # real signature unknown; restored from __doc__
        """ currentList(self) -> Optional[QTextList] """
        pass

    def currentTable(self): # real signature unknown; restored from __doc__
        """ currentTable(self) -> Optional[QTextTable] """
        pass

    def deleteChar(self): # real signature unknown; restored from __doc__
        """ deleteChar(self) """
        pass

    def deletePreviousChar(self): # real signature unknown; restored from __doc__
        """ deletePreviousChar(self) """
        pass

    def document(self): # real signature unknown; restored from __doc__
        """ document(self) -> Optional[QTextDocument] """
        pass

    def endEditBlock(self): # real signature unknown; restored from __doc__
        """ endEditBlock(self) """
        pass

    def hasComplexSelection(self): # real signature unknown; restored from __doc__
        """ hasComplexSelection(self) -> bool """
        return False

    def hasSelection(self): # real signature unknown; restored from __doc__
        """ hasSelection(self) -> bool """
        return False

    def insertBlock(self, format=None, charFormat=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        insertBlock(self)
        insertBlock(self, format: QTextBlockFormat)
        insertBlock(self, format: QTextBlockFormat, charFormat: QTextCharFormat)
        """
        pass

    def insertFragment(self, fragment): # real signature unknown; restored from __doc__
        """ insertFragment(self, fragment: QTextDocumentFragment) """
        pass

    def insertFrame(self, format): # real signature unknown; restored from __doc__
        """ insertFrame(self, format: QTextFrameFormat) -> Optional[QTextFrame] """
        pass

    def insertHtml(self, html, p_str=None): # real signature unknown; restored from __doc__
        """ insertHtml(self, html: Optional[str]) """
        pass

    def insertImage(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        insertImage(self, format: QTextImageFormat)
        insertImage(self, format: QTextImageFormat, alignment: QTextFrameFormat.Position)
        insertImage(self, name: Optional[str])
        insertImage(self, image: QImage, name: Optional[str] = '')
        """
        pass

    def insertList(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        insertList(self, format: QTextListFormat) -> Optional[QTextList]
        insertList(self, style: QTextListFormat.Style) -> Optional[QTextList]
        """
        pass

    def insertTable(self, rows, cols, format=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        insertTable(self, rows: int, cols: int, format: QTextTableFormat) -> Optional[QTextTable]
        insertTable(self, rows: int, cols: int) -> Optional[QTextTable]
        """
        pass

    def insertText(self, text, p_str=None, *args=None, **kwargs=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        insertText(self, text: Optional[str])
        insertText(self, text: Optional[str], format: QTextCharFormat)
        """
        pass

    def isCopyOf(self, other): # real signature unknown; restored from __doc__
        """ isCopyOf(self, other: QTextCursor) -> bool """
        return False

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def joinPreviousEditBlock(self): # real signature unknown; restored from __doc__
        """ joinPreviousEditBlock(self) """
        pass

    def keepPositionOnInsert(self): # real signature unknown; restored from __doc__
        """ keepPositionOnInsert(self) -> bool """
        return False

    def mergeBlockCharFormat(self, modifier): # real signature unknown; restored from __doc__
        """ mergeBlockCharFormat(self, modifier: QTextCharFormat) """
        pass

    def mergeBlockFormat(self, modifier): # real signature unknown; restored from __doc__
        """ mergeBlockFormat(self, modifier: QTextBlockFormat) """
        pass

    def mergeCharFormat(self, modifier): # real signature unknown; restored from __doc__
        """ mergeCharFormat(self, modifier: QTextCharFormat) """
        pass

    def movePosition(self, op, mode=None, n=1): # real signature unknown; restored from __doc__
        """ movePosition(self, op: QTextCursor.MoveOperation, mode: QTextCursor.MoveMode = QTextCursor.MoveAnchor, n: int = 1) -> bool """
        return False

    def position(self): # real signature unknown; restored from __doc__
        """ position(self) -> int """
        return 0

    def positionInBlock(self): # real signature unknown; restored from __doc__
        """ positionInBlock(self) -> int """
        return 0

    def removeSelectedText(self): # real signature unknown; restored from __doc__
        """ removeSelectedText(self) """
        pass

    def select(self, selection): # real signature unknown; restored from __doc__
        """ select(self, selection: QTextCursor.SelectionType) """
        pass

    def selectedTableCells(self): # real signature unknown; restored from __doc__
        """ selectedTableCells(self) -> (Optional[int], Optional[int], Optional[int], Optional[int]) """
        pass

    def selectedText(self): # real signature unknown; restored from __doc__
        """ selectedText(self) -> str """
        return ""

    def selection(self): # real signature unknown; restored from __doc__
        """ selection(self) -> QTextDocumentFragment """
        return QTextDocumentFragment

    def selectionEnd(self): # real signature unknown; restored from __doc__
        """ selectionEnd(self) -> int """
        return 0

    def selectionStart(self): # real signature unknown; restored from __doc__
        """ selectionStart(self) -> int """
        return 0

    def setBlockCharFormat(self, format): # real signature unknown; restored from __doc__
        """ setBlockCharFormat(self, format: QTextCharFormat) """
        pass

    def setBlockFormat(self, format): # real signature unknown; restored from __doc__
        """ setBlockFormat(self, format: QTextBlockFormat) """
        pass

    def setCharFormat(self, format): # real signature unknown; restored from __doc__
        """ setCharFormat(self, format: QTextCharFormat) """
        pass

    def setKeepPositionOnInsert(self, b): # real signature unknown; restored from __doc__
        """ setKeepPositionOnInsert(self, b: bool) """
        pass

    def setPosition(self, pos, mode=None): # real signature unknown; restored from __doc__
        """ setPosition(self, pos: int, mode: QTextCursor.MoveMode = QTextCursor.MoveAnchor) """
        pass

    def setVerticalMovementX(self, x): # real signature unknown; restored from __doc__
        """ setVerticalMovementX(self, x: int) """
        pass

    def setVisualNavigation(self, b): # real signature unknown; restored from __doc__
        """ setVisualNavigation(self, b: bool) """
        pass

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: QTextCursor) """
        pass

    def verticalMovementX(self): # real signature unknown; restored from __doc__
        """ verticalMovementX(self) -> int """
        return 0

    def visualNavigation(self): # real signature unknown; restored from __doc__
        """ visualNavigation(self) -> bool """
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


    BlockUnderCursor = 2
    Document = 3
    Down = 12
    End = 11
    EndOfBlock = 15
    EndOfLine = 13
    EndOfWord = 14
    KeepAnchor = 1
    Left = 9
    LineUnderCursor = 1
    MoveAnchor = 0
    NextBlock = 16
    NextCell = 21
    NextCharacter = 17
    NextRow = 23
    NextWord = 18
    NoMove = 0
    PreviousBlock = 6
    PreviousCell = 22
    PreviousCharacter = 7
    PreviousRow = 24
    PreviousWord = 8
    Right = 19
    Start = 1
    StartOfBlock = 4
    StartOfLine = 3
    StartOfWord = 5
    Up = 2
    WordLeft = 10
    WordRight = 20
    WordUnderCursor = 0
    __hash__ = None


