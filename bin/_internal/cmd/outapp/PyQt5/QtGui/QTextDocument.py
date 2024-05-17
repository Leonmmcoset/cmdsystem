# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QTextDocument(__PyQt5_QtCore.QObject):
    """
    QTextDocument(parent: Optional[QObject] = None)
    QTextDocument(text: Optional[str], parent: Optional[QObject] = None)
    """
    def addResource(self, type, name, resource): # real signature unknown; restored from __doc__
        """ addResource(self, type: int, name: QUrl, resource: Any) """
        pass

    def adjustSize(self): # real signature unknown; restored from __doc__
        """ adjustSize(self) """
        pass

    def allFormats(self): # real signature unknown; restored from __doc__
        """ allFormats(self) -> List[QTextFormat] """
        return []

    def availableRedoSteps(self): # real signature unknown; restored from __doc__
        """ availableRedoSteps(self) -> int """
        return 0

    def availableUndoSteps(self): # real signature unknown; restored from __doc__
        """ availableUndoSteps(self) -> int """
        return 0

    def baseUrl(self): # real signature unknown; restored from __doc__
        """ baseUrl(self) -> QUrl """
        pass

    def baseUrlChanged(self, *args, **kwargs): # real signature unknown
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
        pass

    def begin(self): # real signature unknown; restored from __doc__
        """ begin(self) -> QTextBlock """
        return QTextBlock

    def blockCount(self): # real signature unknown; restored from __doc__
        """ blockCount(self) -> int """
        return 0

    def blockCountChanged(self, *args, **kwargs): # real signature unknown
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
        pass

    def characterAt(self, pos): # real signature unknown; restored from __doc__
        """ characterAt(self, pos: int) -> str """
        return ""

    def characterCount(self): # real signature unknown; restored from __doc__
        """ characterCount(self) -> int """
        return 0

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def clearUndoRedoStacks(self, stacks=None): # real signature unknown; restored from __doc__
        """ clearUndoRedoStacks(self, stacks: QTextDocument.Stacks = QTextDocument.UndoAndRedoStacks) """
        pass

    def clone(self, parent, QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ clone(self, parent: Optional[QObject] = None) -> Optional[QTextDocument] """
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def contentsChange(self, *args, **kwargs): # real signature unknown
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
        pass

    def contentsChanged(self, *args, **kwargs): # real signature unknown
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
        pass

    def createObject(self, f): # real signature unknown; restored from __doc__
        """ createObject(self, f: QTextFormat) -> Optional[QTextObject] """
        pass

    def cursorPositionChanged(self, *args, **kwargs): # real signature unknown
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def defaultCursorMoveStyle(self): # real signature unknown; restored from __doc__
        """ defaultCursorMoveStyle(self) -> Qt.CursorMoveStyle """
        pass

    def defaultFont(self): # real signature unknown; restored from __doc__
        """ defaultFont(self) -> QFont """
        return QFont

    def defaultStyleSheet(self): # real signature unknown; restored from __doc__
        """ defaultStyleSheet(self) -> str """
        return ""

    def defaultTextOption(self): # real signature unknown; restored from __doc__
        """ defaultTextOption(self) -> QTextOption """
        return QTextOption

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def documentLayout(self): # real signature unknown; restored from __doc__
        """ documentLayout(self) -> Optional[QAbstractTextDocumentLayout] """
        pass

    def documentLayoutChanged(self, *args, **kwargs): # real signature unknown
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
        pass

    def documentMargin(self): # real signature unknown; restored from __doc__
        """ documentMargin(self) -> float """
        return 0.0

    def drawContents(self, p, QPainter=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ drawContents(self, p: Optional[QPainter], rect: QRectF = QRectF()) """
        pass

    def end(self): # real signature unknown; restored from __doc__
        """ end(self) -> QTextBlock """
        return QTextBlock

    def find(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        find(self, subString: Optional[str], position: int = 0, options: QTextDocument.FindFlags = 0) -> QTextCursor
        find(self, expr: QRegExp, position: int = 0, options: QTextDocument.FindFlags = 0) -> QTextCursor
        find(self, expr: QRegularExpression, position: int = 0, options: QTextDocument.FindFlags = 0) -> QTextCursor
        find(self, subString: Optional[str], cursor: QTextCursor, options: QTextDocument.FindFlags = 0) -> QTextCursor
        find(self, expr: QRegExp, cursor: QTextCursor, options: QTextDocument.FindFlags = 0) -> QTextCursor
        find(self, expr: QRegularExpression, cursor: QTextCursor, options: QTextDocument.FindFlags = 0) -> QTextCursor
        """
        return QTextCursor

    def findBlock(self, pos): # real signature unknown; restored from __doc__
        """ findBlock(self, pos: int) -> QTextBlock """
        return QTextBlock

    def findBlockByLineNumber(self, blockNumber): # real signature unknown; restored from __doc__
        """ findBlockByLineNumber(self, blockNumber: int) -> QTextBlock """
        return QTextBlock

    def findBlockByNumber(self, blockNumber): # real signature unknown; restored from __doc__
        """ findBlockByNumber(self, blockNumber: int) -> QTextBlock """
        return QTextBlock

    def firstBlock(self): # real signature unknown; restored from __doc__
        """ firstBlock(self) -> QTextBlock """
        return QTextBlock

    def idealWidth(self): # real signature unknown; restored from __doc__
        """ idealWidth(self) -> float """
        return 0.0

    def indentWidth(self): # real signature unknown; restored from __doc__
        """ indentWidth(self) -> float """
        return 0.0

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ isEmpty(self) -> bool """
        return False

    def isModified(self): # real signature unknown; restored from __doc__
        """ isModified(self) -> bool """
        return False

    def isRedoAvailable(self): # real signature unknown; restored from __doc__
        """ isRedoAvailable(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def isUndoAvailable(self): # real signature unknown; restored from __doc__
        """ isUndoAvailable(self) -> bool """
        return False

    def isUndoRedoEnabled(self): # real signature unknown; restored from __doc__
        """ isUndoRedoEnabled(self) -> bool """
        return False

    def lastBlock(self): # real signature unknown; restored from __doc__
        """ lastBlock(self) -> QTextBlock """
        return QTextBlock

    def lineCount(self): # real signature unknown; restored from __doc__
        """ lineCount(self) -> int """
        return 0

    def loadResource(self, type, name): # real signature unknown; restored from __doc__
        """ loadResource(self, type: int, name: QUrl) -> Any """
        pass

    def markContentsDirty(self, from_, length): # real signature unknown; restored from __doc__
        """ markContentsDirty(self, from_: int, length: int) """
        pass

    def maximumBlockCount(self): # real signature unknown; restored from __doc__
        """ maximumBlockCount(self) -> int """
        return 0

    def metaInformation(self, info): # real signature unknown; restored from __doc__
        """ metaInformation(self, info: QTextDocument.MetaInformation) -> str """
        return ""

    def modificationChanged(self, *args, **kwargs): # real signature unknown
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
        pass

    def object(self, objectIndex): # real signature unknown; restored from __doc__
        """ object(self, objectIndex: int) -> Optional[QTextObject] """
        pass

    def objectForFormat(self, a0): # real signature unknown; restored from __doc__
        """ objectForFormat(self, a0: QTextFormat) -> Optional[QTextObject] """
        pass

    def pageCount(self): # real signature unknown; restored from __doc__
        """ pageCount(self) -> int """
        return 0

    def pageSize(self): # real signature unknown; restored from __doc__
        """ pageSize(self) -> QSizeF """
        pass

    def print(self, printer, QPagedPaintDevice=None): # real signature unknown; restored from __doc__
        """ print(self, printer: Optional[QPagedPaintDevice]) """
        pass

    def print_(self, printer, QPagedPaintDevice=None): # real signature unknown; restored from __doc__
        """ print_(self, printer: Optional[QPagedPaintDevice]) """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def redo(self, cursor=None, QTextCursor=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        redo(self)
        redo(self, cursor: Optional[QTextCursor])
        """
        pass

    def redoAvailable(self, *args, **kwargs): # real signature unknown
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
        pass

    def resource(self, type, name): # real signature unknown; restored from __doc__
        """ resource(self, type: int, name: QUrl) -> Any """
        pass

    def revision(self): # real signature unknown; restored from __doc__
        """ revision(self) -> int """
        return 0

    def rootFrame(self): # real signature unknown; restored from __doc__
        """ rootFrame(self) -> Optional[QTextFrame] """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setBaseUrl(self, url): # real signature unknown; restored from __doc__
        """ setBaseUrl(self, url: QUrl) """
        pass

    def setDefaultCursorMoveStyle(self, style): # real signature unknown; restored from __doc__
        """ setDefaultCursorMoveStyle(self, style: Qt.CursorMoveStyle) """
        pass

    def setDefaultFont(self, font): # real signature unknown; restored from __doc__
        """ setDefaultFont(self, font: QFont) """
        pass

    def setDefaultStyleSheet(self, sheet, p_str=None): # real signature unknown; restored from __doc__
        """ setDefaultStyleSheet(self, sheet: Optional[str]) """
        pass

    def setDefaultTextOption(self, option): # real signature unknown; restored from __doc__
        """ setDefaultTextOption(self, option: QTextOption) """
        pass

    def setDocumentLayout(self, layout, QAbstractTextDocumentLayout=None): # real signature unknown; restored from __doc__
        """ setDocumentLayout(self, layout: Optional[QAbstractTextDocumentLayout]) """
        pass

    def setDocumentMargin(self, margin): # real signature unknown; restored from __doc__
        """ setDocumentMargin(self, margin: float) """
        pass

    def setHtml(self, html, p_str=None): # real signature unknown; restored from __doc__
        """ setHtml(self, html: Optional[str]) """
        pass

    def setIndentWidth(self, width): # real signature unknown; restored from __doc__
        """ setIndentWidth(self, width: float) """
        pass

    def setMarkdown(self, markdown, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setMarkdown(self, markdown: Optional[str], features: Union[QTextDocument.MarkdownFeatures, QTextDocument.MarkdownFeature] = QTextDocument.MarkdownDialectGitHub) """
        pass

    def setMaximumBlockCount(self, maximum): # real signature unknown; restored from __doc__
        """ setMaximumBlockCount(self, maximum: int) """
        pass

    def setMetaInformation(self, info, a1, p_str=None): # real signature unknown; restored from __doc__
        """ setMetaInformation(self, info: QTextDocument.MetaInformation, a1: Optional[str]) """
        pass

    def setModified(self, on=True): # real signature unknown; restored from __doc__
        """ setModified(self, on: bool = True) """
        pass

    def setPageSize(self, size): # real signature unknown; restored from __doc__
        """ setPageSize(self, size: QSizeF) """
        pass

    def setPlainText(self, text, p_str=None): # real signature unknown; restored from __doc__
        """ setPlainText(self, text: Optional[str]) """
        pass

    def setTextWidth(self, width): # real signature unknown; restored from __doc__
        """ setTextWidth(self, width: float) """
        pass

    def setUndoRedoEnabled(self, enable): # real signature unknown; restored from __doc__
        """ setUndoRedoEnabled(self, enable: bool) """
        pass

    def setUseDesignMetrics(self, b): # real signature unknown; restored from __doc__
        """ setUseDesignMetrics(self, b: bool) """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ size(self) -> QSizeF """
        pass

    def textWidth(self): # real signature unknown; restored from __doc__
        """ textWidth(self) -> float """
        return 0.0

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def toHtml(self, encoding, QByteArray=None, bytes=None, bytearray=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ toHtml(self, encoding: Union[QByteArray, bytes, bytearray] = QByteArray()) -> str """
        pass

    def toMarkdown(self, features, QTextDocument_MarkdownFeatures=None, QTextDocument_MarkdownFeature=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ toMarkdown(self, features: Union[QTextDocument.MarkdownFeatures, QTextDocument.MarkdownFeature] = QTextDocument.MarkdownDialectGitHub) -> str """
        pass

    def toPlainText(self): # real signature unknown; restored from __doc__
        """ toPlainText(self) -> str """
        return ""

    def toRawText(self): # real signature unknown; restored from __doc__
        """ toRawText(self) -> str """
        return ""

    def undo(self, cursor=None, QTextCursor=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        undo(self)
        undo(self, cursor: Optional[QTextCursor])
        """
        pass

    def undoAvailable(self, *args, **kwargs): # real signature unknown
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
        pass

    def undoCommandAdded(self, *args, **kwargs): # real signature unknown
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
        pass

    def useDesignMetrics(self): # real signature unknown; restored from __doc__
        """ useDesignMetrics(self) -> bool """
        return False

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    DocumentTitle = 0
    DocumentUrl = 1
    FindBackward = 1
    FindCaseSensitively = 2
    FindWholeWords = 4
    HtmlResource = 1
    ImageResource = 2
    MarkdownDialectCommonMark = 0
    MarkdownDialectGitHub = 3852
    MarkdownNoHTML = 96
    MarkdownResource = 4
    RedoStack = 2
    StyleSheetResource = 3
    UndoAndRedoStacks = 3
    UndoStack = 1
    UnknownResource = 0
    UserResource = 100


