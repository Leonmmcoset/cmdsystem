# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QTextBlock(__sip.wrapper):
    """
    QTextBlock()
    QTextBlock(o: QTextBlock)
    """
    def begin(self): # real signature unknown; restored from __doc__
        """ begin(self) -> QTextBlock.iterator """
        pass

    def blockFormat(self): # real signature unknown; restored from __doc__
        """ blockFormat(self) -> QTextBlockFormat """
        return QTextBlockFormat

    def blockFormatIndex(self): # real signature unknown; restored from __doc__
        """ blockFormatIndex(self) -> int """
        return 0

    def blockNumber(self): # real signature unknown; restored from __doc__
        """ blockNumber(self) -> int """
        return 0

    def charFormat(self): # real signature unknown; restored from __doc__
        """ charFormat(self) -> QTextCharFormat """
        return QTextCharFormat

    def charFormatIndex(self): # real signature unknown; restored from __doc__
        """ charFormatIndex(self) -> int """
        return 0

    def clearLayout(self): # real signature unknown; restored from __doc__
        """ clearLayout(self) """
        pass

    def contains(self, position): # real signature unknown; restored from __doc__
        """ contains(self, position: int) -> bool """
        return False

    def document(self): # real signature unknown; restored from __doc__
        """ document(self) -> Optional[QTextDocument] """
        pass

    def end(self): # real signature unknown; restored from __doc__
        """ end(self) -> QTextBlock.iterator """
        pass

    def firstLineNumber(self): # real signature unknown; restored from __doc__
        """ firstLineNumber(self) -> int """
        return 0

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def isVisible(self): # real signature unknown; restored from __doc__
        """ isVisible(self) -> bool """
        return False

    def layout(self): # real signature unknown; restored from __doc__
        """ layout(self) -> Optional[QTextLayout] """
        pass

    def length(self): # real signature unknown; restored from __doc__
        """ length(self) -> int """
        return 0

    def lineCount(self): # real signature unknown; restored from __doc__
        """ lineCount(self) -> int """
        return 0

    def next(self): # real signature unknown; restored from __doc__
        """ next(self) -> QTextBlock """
        return QTextBlock

    def position(self): # real signature unknown; restored from __doc__
        """ position(self) -> int """
        return 0

    def previous(self): # real signature unknown; restored from __doc__
        """ previous(self) -> QTextBlock """
        return QTextBlock

    def revision(self): # real signature unknown; restored from __doc__
        """ revision(self) -> int """
        return 0

    def setLineCount(self, count): # real signature unknown; restored from __doc__
        """ setLineCount(self, count: int) """
        pass

    def setRevision(self, rev): # real signature unknown; restored from __doc__
        """ setRevision(self, rev: int) """
        pass

    def setUserData(self, data, QTextBlockUserData=None): # real signature unknown; restored from __doc__
        """ setUserData(self, data: Optional[QTextBlockUserData]) """
        pass

    def setUserState(self, state): # real signature unknown; restored from __doc__
        """ setUserState(self, state: int) """
        pass

    def setVisible(self, visible): # real signature unknown; restored from __doc__
        """ setVisible(self, visible: bool) """
        pass

    def text(self): # real signature unknown; restored from __doc__
        """ text(self) -> str """
        return ""

    def textDirection(self): # real signature unknown; restored from __doc__
        """ textDirection(self) -> Qt.LayoutDirection """
        pass

    def textFormats(self): # real signature unknown; restored from __doc__
        """ textFormats(self) -> List[QTextLayout.FormatRange] """
        return []

    def textList(self): # real signature unknown; restored from __doc__
        """ textList(self) -> Optional[QTextList] """
        pass

    def userData(self): # real signature unknown; restored from __doc__
        """ userData(self) -> Optional[QTextBlockUserData] """
        pass

    def userState(self): # real signature unknown; restored from __doc__
        """ userState(self) -> int """
        return 0

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, o=None): # real signature unknown; restored from __doc__ with multiple overloads
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


