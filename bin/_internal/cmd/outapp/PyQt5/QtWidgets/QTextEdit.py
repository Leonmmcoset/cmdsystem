# encoding: utf-8
# module PyQt5.QtWidgets
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


from .QAbstractScrollArea import QAbstractScrollArea

class QTextEdit(QAbstractScrollArea):
    """
    QTextEdit(parent: Optional[QWidget] = None)
    QTextEdit(text: Optional[str], parent: Optional[QWidget] = None)
    """
    def acceptRichText(self): # real signature unknown; restored from __doc__
        """ acceptRichText(self) -> bool """
        return False

    def actionEvent(self, *args, **kwargs): # real signature unknown
        pass

    def alignment(self): # real signature unknown; restored from __doc__
        """ alignment(self) -> Qt.Alignment """
        pass

    def anchorAt(self, pos): # real signature unknown; restored from __doc__
        """ anchorAt(self, pos: QPoint) -> str """
        return ""

    def append(self, text, p_str=None): # real signature unknown; restored from __doc__
        """ append(self, text: Optional[str]) """
        pass

    def autoFormatting(self): # real signature unknown; restored from __doc__
        """ autoFormatting(self) -> QTextEdit.AutoFormatting """
        pass

    def canInsertFromMimeData(self, source, QMimeData=None): # real signature unknown; restored from __doc__
        """ canInsertFromMimeData(self, source: Optional[QMimeData]) -> bool """
        return False

    def canPaste(self): # real signature unknown; restored from __doc__
        """ canPaste(self) -> bool """
        return False

    def changeEvent(self, e, QEvent=None): # real signature unknown; restored from __doc__
        """ changeEvent(self, e: Optional[QEvent]) """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def closeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def contextMenuEvent(self, e, QContextMenuEvent=None): # real signature unknown; restored from __doc__
        """ contextMenuEvent(self, e: Optional[QContextMenuEvent]) """
        pass

    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) """
        pass

    def copyAvailable(self, *args, **kwargs): # real signature unknown
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

    def create(self, *args, **kwargs): # real signature unknown
        pass

    def createMimeDataFromSelection(self): # real signature unknown; restored from __doc__
        """ createMimeDataFromSelection(self) -> Optional[QMimeData] """
        pass

    def createStandardContextMenu(self, position=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        createStandardContextMenu(self) -> Optional[QMenu]
        createStandardContextMenu(self, position: QPoint) -> Optional[QMenu]
        """
        pass

    def currentCharFormat(self): # real signature unknown; restored from __doc__
        """ currentCharFormat(self) -> QTextCharFormat """
        pass

    def currentCharFormatChanged(self, *args, **kwargs): # real signature unknown
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

    def currentFont(self): # real signature unknown; restored from __doc__
        """ currentFont(self) -> QFont """
        pass

    def cursorForPosition(self, pos): # real signature unknown; restored from __doc__
        """ cursorForPosition(self, pos: QPoint) -> QTextCursor """
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

    def cursorRect(self, cursor=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        cursorRect(self, cursor: QTextCursor) -> QRect
        cursorRect(self) -> QRect
        """
        pass

    def cursorWidth(self): # real signature unknown; restored from __doc__
        """ cursorWidth(self) -> int """
        return 0

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def cut(self): # real signature unknown; restored from __doc__
        """ cut(self) """
        pass

    def destroy(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def document(self): # real signature unknown; restored from __doc__
        """ document(self) -> Optional[QTextDocument] """
        pass

    def documentTitle(self): # real signature unknown; restored from __doc__
        """ documentTitle(self) -> str """
        return ""

    def dragEnterEvent(self, e, QDragEnterEvent=None): # real signature unknown; restored from __doc__
        """ dragEnterEvent(self, e: Optional[QDragEnterEvent]) """
        pass

    def dragLeaveEvent(self, e, QDragLeaveEvent=None): # real signature unknown; restored from __doc__
        """ dragLeaveEvent(self, e: Optional[QDragLeaveEvent]) """
        pass

    def dragMoveEvent(self, e, QDragMoveEvent=None): # real signature unknown; restored from __doc__
        """ dragMoveEvent(self, e: Optional[QDragMoveEvent]) """
        pass

    def drawFrame(self, *args, **kwargs): # real signature unknown
        pass

    def dropEvent(self, e, QDropEvent=None): # real signature unknown; restored from __doc__
        """ dropEvent(self, e: Optional[QDropEvent]) """
        pass

    def ensureCursorVisible(self): # real signature unknown; restored from __doc__
        """ ensureCursorVisible(self) """
        pass

    def enterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, e, QEvent=None): # real signature unknown; restored from __doc__
        """ event(self, e: Optional[QEvent]) -> bool """
        return False

    def eventFilter(self, *args, **kwargs): # real signature unknown
        pass

    def extraSelections(self): # real signature unknown; restored from __doc__
        """ extraSelections(self) -> List[QTextEdit.ExtraSelection] """
        return []

    def find(self, exp, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        find(self, exp: Optional[str], options: Union[QTextDocument.FindFlags, QTextDocument.FindFlag] = QTextDocument.FindFlags()) -> bool
        find(self, exp: QRegExp, options: Union[QTextDocument.FindFlags, QTextDocument.FindFlag] = QTextDocument.FindFlags()) -> bool
        find(self, exp: QRegularExpression, options: Union[QTextDocument.FindFlags, QTextDocument.FindFlag] = QTextDocument.FindFlags()) -> bool
        """
        pass

    def focusInEvent(self, e, QFocusEvent=None): # real signature unknown; restored from __doc__
        """ focusInEvent(self, e: Optional[QFocusEvent]) """
        pass

    def focusNextChild(self, *args, **kwargs): # real signature unknown
        pass

    def focusNextPrevChild(self, next): # real signature unknown; restored from __doc__
        """ focusNextPrevChild(self, next: bool) -> bool """
        return False

    def focusOutEvent(self, e, QFocusEvent=None): # real signature unknown; restored from __doc__
        """ focusOutEvent(self, e: Optional[QFocusEvent]) """
        pass

    def focusPreviousChild(self, *args, **kwargs): # real signature unknown
        pass

    def fontFamily(self): # real signature unknown; restored from __doc__
        """ fontFamily(self) -> str """
        return ""

    def fontItalic(self): # real signature unknown; restored from __doc__
        """ fontItalic(self) -> bool """
        return False

    def fontPointSize(self): # real signature unknown; restored from __doc__
        """ fontPointSize(self) -> float """
        return 0.0

    def fontUnderline(self): # real signature unknown; restored from __doc__
        """ fontUnderline(self) -> bool """
        return False

    def fontWeight(self): # real signature unknown; restored from __doc__
        """ fontWeight(self) -> int """
        return 0

    def hideEvent(self, *args, **kwargs): # real signature unknown
        pass

    def initPainter(self, *args, **kwargs): # real signature unknown
        pass

    def initStyleOption(self, *args, **kwargs): # real signature unknown
        pass

    def inputMethodEvent(self, a0, QInputMethodEvent=None): # real signature unknown; restored from __doc__
        """ inputMethodEvent(self, a0: Optional[QInputMethodEvent]) """
        pass

    def inputMethodQuery(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        inputMethodQuery(self, property: Qt.InputMethodQuery) -> Any
        inputMethodQuery(self, query: Qt.InputMethodQuery, argument: Any) -> Any
        """
        pass

    def insertFromMimeData(self, source, QMimeData=None): # real signature unknown; restored from __doc__
        """ insertFromMimeData(self, source: Optional[QMimeData]) """
        pass

    def insertHtml(self, text, p_str=None): # real signature unknown; restored from __doc__
        """ insertHtml(self, text: Optional[str]) """
        pass

    def insertPlainText(self, text, p_str=None): # real signature unknown; restored from __doc__
        """ insertPlainText(self, text: Optional[str]) """
        pass

    def isReadOnly(self): # real signature unknown; restored from __doc__
        """ isReadOnly(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def isUndoRedoEnabled(self): # real signature unknown; restored from __doc__
        """ isUndoRedoEnabled(self) -> bool """
        return False

    def keyPressEvent(self, e, QKeyEvent=None): # real signature unknown; restored from __doc__
        """ keyPressEvent(self, e: Optional[QKeyEvent]) """
        pass

    def keyReleaseEvent(self, e, QKeyEvent=None): # real signature unknown; restored from __doc__
        """ keyReleaseEvent(self, e: Optional[QKeyEvent]) """
        pass

    def leaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def lineWrapColumnOrWidth(self): # real signature unknown; restored from __doc__
        """ lineWrapColumnOrWidth(self) -> int """
        return 0

    def lineWrapMode(self): # real signature unknown; restored from __doc__
        """ lineWrapMode(self) -> QTextEdit.LineWrapMode """
        pass

    def loadResource(self, type, name): # real signature unknown; restored from __doc__
        """ loadResource(self, type: int, name: QUrl) -> Any """
        pass

    def mergeCurrentCharFormat(self, modifier): # real signature unknown; restored from __doc__
        """ mergeCurrentCharFormat(self, modifier: QTextCharFormat) """
        pass

    def metric(self, *args, **kwargs): # real signature unknown
        pass

    def mouseDoubleClickEvent(self, e, QMouseEvent=None): # real signature unknown; restored from __doc__
        """ mouseDoubleClickEvent(self, e: Optional[QMouseEvent]) """
        pass

    def mouseMoveEvent(self, e, QMouseEvent=None): # real signature unknown; restored from __doc__
        """ mouseMoveEvent(self, e: Optional[QMouseEvent]) """
        pass

    def mousePressEvent(self, e, QMouseEvent=None): # real signature unknown; restored from __doc__
        """ mousePressEvent(self, e: Optional[QMouseEvent]) """
        pass

    def mouseReleaseEvent(self, e, QMouseEvent=None): # real signature unknown; restored from __doc__
        """ mouseReleaseEvent(self, e: Optional[QMouseEvent]) """
        pass

    def moveCursor(self, operation, mode=None): # real signature unknown; restored from __doc__
        """ moveCursor(self, operation: QTextCursor.MoveOperation, mode: QTextCursor.MoveMode = QTextCursor.MoveAnchor) """
        pass

    def moveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def nativeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def overwriteMode(self): # real signature unknown; restored from __doc__
        """ overwriteMode(self) -> bool """
        return False

    def paintEvent(self, e, QPaintEvent=None): # real signature unknown; restored from __doc__
        """ paintEvent(self, e: Optional[QPaintEvent]) """
        pass

    def paste(self): # real signature unknown; restored from __doc__
        """ paste(self) """
        pass

    def placeholderText(self): # real signature unknown; restored from __doc__
        """ placeholderText(self) -> str """
        return ""

    def print(self, printer, QPagedPaintDevice=None): # real signature unknown; restored from __doc__
        """ print(self, printer: Optional[QPagedPaintDevice]) """
        pass

    def print_(self, printer, QPagedPaintDevice=None): # real signature unknown; restored from __doc__
        """ print_(self, printer: Optional[QPagedPaintDevice]) """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def redo(self): # real signature unknown; restored from __doc__
        """ redo(self) """
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

    def resizeEvent(self, a0, QResizeEvent=None): # real signature unknown; restored from __doc__
        """ resizeEvent(self, a0: Optional[QResizeEvent]) """
        pass

    def scrollContentsBy(self, dx, dy): # real signature unknown; restored from __doc__
        """ scrollContentsBy(self, dx: int, dy: int) """
        pass

    def scrollToAnchor(self, name, p_str=None): # real signature unknown; restored from __doc__
        """ scrollToAnchor(self, name: Optional[str]) """
        pass

    def selectAll(self): # real signature unknown; restored from __doc__
        """ selectAll(self) """
        pass

    def selectionChanged(self, *args, **kwargs): # real signature unknown
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

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setAcceptRichText(self, accept): # real signature unknown; restored from __doc__
        """ setAcceptRichText(self, accept: bool) """
        pass

    def setAlignment(self, a, Qt_Alignment=None, Qt_AlignmentFlag=None): # real signature unknown; restored from __doc__
        """ setAlignment(self, a: Union[Qt.Alignment, Qt.AlignmentFlag]) """
        pass

    def setAutoFormatting(self, features, QTextEdit_AutoFormatting=None, QTextEdit_AutoFormattingFlag=None): # real signature unknown; restored from __doc__
        """ setAutoFormatting(self, features: Union[QTextEdit.AutoFormatting, QTextEdit.AutoFormattingFlag]) """
        pass

    def setCurrentCharFormat(self, format): # real signature unknown; restored from __doc__
        """ setCurrentCharFormat(self, format: QTextCharFormat) """
        pass

    def setCurrentFont(self, f): # real signature unknown; restored from __doc__
        """ setCurrentFont(self, f: QFont) """
        pass

    def setCursorWidth(self, width): # real signature unknown; restored from __doc__
        """ setCursorWidth(self, width: int) """
        pass

    def setDocument(self, document, QTextDocument=None): # real signature unknown; restored from __doc__
        """ setDocument(self, document: Optional[QTextDocument]) """
        pass

    def setDocumentTitle(self, title, p_str=None): # real signature unknown; restored from __doc__
        """ setDocumentTitle(self, title: Optional[str]) """
        pass

    def setExtraSelections(self, selections, QTextEdit_ExtraSelection=None): # real signature unknown; restored from __doc__
        """ setExtraSelections(self, selections: Iterable[QTextEdit.ExtraSelection]) """
        pass

    def setFontFamily(self, fontFamily, p_str=None): # real signature unknown; restored from __doc__
        """ setFontFamily(self, fontFamily: Optional[str]) """
        pass

    def setFontItalic(self, b): # real signature unknown; restored from __doc__
        """ setFontItalic(self, b: bool) """
        pass

    def setFontPointSize(self, s): # real signature unknown; restored from __doc__
        """ setFontPointSize(self, s: float) """
        pass

    def setFontUnderline(self, b): # real signature unknown; restored from __doc__
        """ setFontUnderline(self, b: bool) """
        pass

    def setFontWeight(self, w): # real signature unknown; restored from __doc__
        """ setFontWeight(self, w: int) """
        pass

    def setHtml(self, text, p_str=None): # real signature unknown; restored from __doc__
        """ setHtml(self, text: Optional[str]) """
        pass

    def setLineWrapColumnOrWidth(self, w): # real signature unknown; restored from __doc__
        """ setLineWrapColumnOrWidth(self, w: int) """
        pass

    def setLineWrapMode(self, mode): # real signature unknown; restored from __doc__
        """ setLineWrapMode(self, mode: QTextEdit.LineWrapMode) """
        pass

    def setMarkdown(self, markdown, p_str=None): # real signature unknown; restored from __doc__
        """ setMarkdown(self, markdown: Optional[str]) """
        pass

    def setOverwriteMode(self, overwrite): # real signature unknown; restored from __doc__
        """ setOverwriteMode(self, overwrite: bool) """
        pass

    def setPlaceholderText(self, placeholderText, p_str=None): # real signature unknown; restored from __doc__
        """ setPlaceholderText(self, placeholderText: Optional[str]) """
        pass

    def setPlainText(self, text, p_str=None): # real signature unknown; restored from __doc__
        """ setPlainText(self, text: Optional[str]) """
        pass

    def setReadOnly(self, ro): # real signature unknown; restored from __doc__
        """ setReadOnly(self, ro: bool) """
        pass

    def setTabChangesFocus(self, b): # real signature unknown; restored from __doc__
        """ setTabChangesFocus(self, b: bool) """
        pass

    def setTabStopDistance(self, distance): # real signature unknown; restored from __doc__
        """ setTabStopDistance(self, distance: float) """
        pass

    def setTabStopWidth(self, width): # real signature unknown; restored from __doc__
        """ setTabStopWidth(self, width: int) """
        pass

    def setText(self, text, p_str=None): # real signature unknown; restored from __doc__
        """ setText(self, text: Optional[str]) """
        pass

    def setTextBackgroundColor(self, c, QColor=None, Qt_GlobalColor=None): # real signature unknown; restored from __doc__
        """ setTextBackgroundColor(self, c: Union[QColor, Qt.GlobalColor]) """
        pass

    def setTextColor(self, c, QColor=None, Qt_GlobalColor=None): # real signature unknown; restored from __doc__
        """ setTextColor(self, c: Union[QColor, Qt.GlobalColor]) """
        pass

    def setTextCursor(self, cursor): # real signature unknown; restored from __doc__
        """ setTextCursor(self, cursor: QTextCursor) """
        pass

    def setTextInteractionFlags(self, flags, Qt_TextInteractionFlags=None, Qt_TextInteractionFlag=None): # real signature unknown; restored from __doc__
        """ setTextInteractionFlags(self, flags: Union[Qt.TextInteractionFlags, Qt.TextInteractionFlag]) """
        pass

    def setUndoRedoEnabled(self, enable): # real signature unknown; restored from __doc__
        """ setUndoRedoEnabled(self, enable: bool) """
        pass

    def setViewportMargins(self, *args, **kwargs): # real signature unknown
        pass

    def setWordWrapMode(self, policy): # real signature unknown; restored from __doc__
        """ setWordWrapMode(self, policy: QTextOption.WrapMode) """
        pass

    def sharedPainter(self, *args, **kwargs): # real signature unknown
        pass

    def showEvent(self, a0, QShowEvent=None): # real signature unknown; restored from __doc__
        """ showEvent(self, a0: Optional[QShowEvent]) """
        pass

    def tabChangesFocus(self): # real signature unknown; restored from __doc__
        """ tabChangesFocus(self) -> bool """
        return False

    def tabletEvent(self, *args, **kwargs): # real signature unknown
        pass

    def tabStopDistance(self): # real signature unknown; restored from __doc__
        """ tabStopDistance(self) -> float """
        return 0.0

    def tabStopWidth(self): # real signature unknown; restored from __doc__
        """ tabStopWidth(self) -> int """
        return 0

    def textBackgroundColor(self): # real signature unknown; restored from __doc__
        """ textBackgroundColor(self) -> QColor """
        pass

    def textChanged(self, *args, **kwargs): # real signature unknown
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

    def textColor(self): # real signature unknown; restored from __doc__
        """ textColor(self) -> QColor """
        pass

    def textCursor(self): # real signature unknown; restored from __doc__
        """ textCursor(self) -> QTextCursor """
        pass

    def textInteractionFlags(self): # real signature unknown; restored from __doc__
        """ textInteractionFlags(self) -> Qt.TextInteractionFlags """
        pass

    def timerEvent(self, e, QTimerEvent=None): # real signature unknown; restored from __doc__
        """ timerEvent(self, e: Optional[QTimerEvent]) """
        pass

    def toHtml(self): # real signature unknown; restored from __doc__
        """ toHtml(self) -> str """
        return ""

    def toMarkdown(self, features, QTextDocument_MarkdownFeatures=None, QTextDocument_MarkdownFeature=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ toMarkdown(self, features: Union[QTextDocument.MarkdownFeatures, QTextDocument.MarkdownFeature] = QTextDocument.MarkdownDialectGitHub) -> str """
        pass

    def toPlainText(self): # real signature unknown; restored from __doc__
        """ toPlainText(self) -> str """
        return ""

    def undo(self): # real signature unknown; restored from __doc__
        """ undo(self) """
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

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

    def viewportEvent(self, *args, **kwargs): # real signature unknown
        pass

    def viewportMargins(self, *args, **kwargs): # real signature unknown
        pass

    def viewportSizeHint(self, *args, **kwargs): # real signature unknown
        pass

    def wheelEvent(self, e, QWheelEvent=None): # real signature unknown; restored from __doc__
        """ wheelEvent(self, e: Optional[QWheelEvent]) """
        pass

    def wordWrapMode(self): # real signature unknown; restored from __doc__
        """ wordWrapMode(self) -> QTextOption.WrapMode """
        pass

    def zoomIn(self, range=1): # real signature unknown; restored from __doc__
        """ zoomIn(self, range: int = 1) """
        pass

    def zoomOut(self, range=1): # real signature unknown; restored from __doc__
        """ zoomOut(self, range: int = 1) """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    AutoAll = -1
    AutoBulletList = 1
    AutoNone = 0
    FixedColumnWidth = 3
    FixedPixelWidth = 2
    NoWrap = 0
    WidgetWidth = 1


