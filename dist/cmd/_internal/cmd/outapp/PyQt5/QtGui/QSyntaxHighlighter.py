# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QSyntaxHighlighter(__PyQt5_QtCore.QObject):
    """
    QSyntaxHighlighter(parent: Optional[QTextDocument])
    QSyntaxHighlighter(parent: Optional[QObject])
    """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def currentBlock(self): # real signature unknown; restored from __doc__
        """ currentBlock(self) -> QTextBlock """
        return QTextBlock

    def currentBlockState(self): # real signature unknown; restored from __doc__
        """ currentBlockState(self) -> int """
        return 0

    def currentBlockUserData(self): # real signature unknown; restored from __doc__
        """ currentBlockUserData(self) -> Optional[QTextBlockUserData] """
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def document(self): # real signature unknown; restored from __doc__
        """ document(self) -> Optional[QTextDocument] """
        pass

    def format(self, pos): # real signature unknown; restored from __doc__
        """ format(self, pos: int) -> QTextCharFormat """
        return QTextCharFormat

    def highlightBlock(self, text, p_str=None): # real signature unknown; restored from __doc__
        """ highlightBlock(self, text: Optional[str]) """
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def previousBlockState(self): # real signature unknown; restored from __doc__
        """ previousBlockState(self) -> int """
        return 0

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def rehighlight(self): # real signature unknown; restored from __doc__
        """ rehighlight(self) """
        pass

    def rehighlightBlock(self, block): # real signature unknown; restored from __doc__
        """ rehighlightBlock(self, block: QTextBlock) """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setCurrentBlockState(self, newState): # real signature unknown; restored from __doc__
        """ setCurrentBlockState(self, newState: int) """
        pass

    def setCurrentBlockUserData(self, data, QTextBlockUserData=None): # real signature unknown; restored from __doc__
        """ setCurrentBlockUserData(self, data: Optional[QTextBlockUserData]) """
        pass

    def setDocument(self, doc, QTextDocument=None): # real signature unknown; restored from __doc__
        """ setDocument(self, doc: Optional[QTextDocument]) """
        pass

    def setFormat(self, start, count, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setFormat(self, start: int, count: int, format: QTextCharFormat)
        setFormat(self, start: int, count: int, color: Union[QColor, Qt.GlobalColor])
        setFormat(self, start: int, count: int, font: QFont)
        """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


