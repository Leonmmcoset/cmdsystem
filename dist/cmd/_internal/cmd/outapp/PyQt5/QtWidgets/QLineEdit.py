# encoding: utf-8
# module PyQt5.QtWidgets
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


from .QWidget import QWidget

class QLineEdit(QWidget):
    """
    QLineEdit(parent: Optional[QWidget] = None)
    QLineEdit(contents: Optional[str], parent: Optional[QWidget] = None)
    """
    def actionEvent(self, *args, **kwargs): # real signature unknown
        pass

    def addAction(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        addAction(self, action: Optional[QAction])
        addAction(self, action: Optional[QAction], position: QLineEdit.ActionPosition)
        addAction(self, icon: QIcon, position: QLineEdit.ActionPosition) -> Optional[QAction]
        """
        pass

    def alignment(self): # real signature unknown; restored from __doc__
        """ alignment(self) -> Qt.Alignment """
        pass

    def backspace(self): # real signature unknown; restored from __doc__
        """ backspace(self) """
        pass

    def changeEvent(self, a0, QEvent=None): # real signature unknown; restored from __doc__
        """ changeEvent(self, a0: Optional[QEvent]) """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def closeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def completer(self): # real signature unknown; restored from __doc__
        """ completer(self) -> Optional[QCompleter] """
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def contextMenuEvent(self, a0, QContextMenuEvent=None): # real signature unknown; restored from __doc__
        """ contextMenuEvent(self, a0: Optional[QContextMenuEvent]) """
        pass

    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) """
        pass

    def create(self, *args, **kwargs): # real signature unknown
        pass

    def createStandardContextMenu(self): # real signature unknown; restored from __doc__
        """ createStandardContextMenu(self) -> Optional[QMenu] """
        pass

    def cursorBackward(self, mark, steps=1): # real signature unknown; restored from __doc__
        """ cursorBackward(self, mark: bool, steps: int = 1) """
        pass

    def cursorForward(self, mark, steps=1): # real signature unknown; restored from __doc__
        """ cursorForward(self, mark: bool, steps: int = 1) """
        pass

    def cursorMoveStyle(self): # real signature unknown; restored from __doc__
        """ cursorMoveStyle(self) -> Qt.CursorMoveStyle """
        pass

    def cursorPosition(self): # real signature unknown; restored from __doc__
        """ cursorPosition(self) -> int """
        return 0

    def cursorPositionAt(self, pos): # real signature unknown; restored from __doc__
        """ cursorPositionAt(self, pos: QPoint) -> int """
        return 0

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

    def cursorRect(self): # real signature unknown; restored from __doc__
        """ cursorRect(self) -> QRect """
        pass

    def cursorWordBackward(self, mark): # real signature unknown; restored from __doc__
        """ cursorWordBackward(self, mark: bool) """
        pass

    def cursorWordForward(self, mark): # real signature unknown; restored from __doc__
        """ cursorWordForward(self, mark: bool) """
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def cut(self): # real signature unknown; restored from __doc__
        """ cut(self) """
        pass

    def del_(self): # real signature unknown; restored from __doc__
        """ del_(self) """
        pass

    def deselect(self): # real signature unknown; restored from __doc__
        """ deselect(self) """
        pass

    def destroy(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def displayText(self): # real signature unknown; restored from __doc__
        """ displayText(self) -> str """
        return ""

    def dragEnabled(self): # real signature unknown; restored from __doc__
        """ dragEnabled(self) -> bool """
        return False

    def dragEnterEvent(self, a0, QDragEnterEvent=None): # real signature unknown; restored from __doc__
        """ dragEnterEvent(self, a0: Optional[QDragEnterEvent]) """
        pass

    def dragLeaveEvent(self, e, QDragLeaveEvent=None): # real signature unknown; restored from __doc__
        """ dragLeaveEvent(self, e: Optional[QDragLeaveEvent]) """
        pass

    def dragMoveEvent(self, e, QDragMoveEvent=None): # real signature unknown; restored from __doc__
        """ dragMoveEvent(self, e: Optional[QDragMoveEvent]) """
        pass

    def dropEvent(self, a0, QDropEvent=None): # real signature unknown; restored from __doc__
        """ dropEvent(self, a0: Optional[QDropEvent]) """
        pass

    def echoMode(self): # real signature unknown; restored from __doc__
        """ echoMode(self) -> QLineEdit.EchoMode """
        pass

    def editingFinished(self, *args, **kwargs): # real signature unknown
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

    def end(self, mark): # real signature unknown; restored from __doc__
        """ end(self, mark: bool) """
        pass

    def enterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, a0, QEvent=None): # real signature unknown; restored from __doc__
        """ event(self, a0: Optional[QEvent]) -> bool """
        return False

    def focusInEvent(self, a0, QFocusEvent=None): # real signature unknown; restored from __doc__
        """ focusInEvent(self, a0: Optional[QFocusEvent]) """
        pass

    def focusNextChild(self, *args, **kwargs): # real signature unknown
        pass

    def focusNextPrevChild(self, *args, **kwargs): # real signature unknown
        pass

    def focusOutEvent(self, a0, QFocusEvent=None): # real signature unknown; restored from __doc__
        """ focusOutEvent(self, a0: Optional[QFocusEvent]) """
        pass

    def focusPreviousChild(self, *args, **kwargs): # real signature unknown
        pass

    def getTextMargins(self): # real signature unknown; restored from __doc__
        """ getTextMargins(self) -> (Optional[int], Optional[int], Optional[int], Optional[int]) """
        pass

    def hasAcceptableInput(self): # real signature unknown; restored from __doc__
        """ hasAcceptableInput(self) -> bool """
        return False

    def hasFrame(self): # real signature unknown; restored from __doc__
        """ hasFrame(self) -> bool """
        return False

    def hasSelectedText(self): # real signature unknown; restored from __doc__
        """ hasSelectedText(self) -> bool """
        return False

    def hideEvent(self, *args, **kwargs): # real signature unknown
        pass

    def home(self, mark): # real signature unknown; restored from __doc__
        """ home(self, mark: bool) """
        pass

    def initPainter(self, *args, **kwargs): # real signature unknown
        pass

    def initStyleOption(self, option, QStyleOptionFrame=None): # real signature unknown; restored from __doc__
        """ initStyleOption(self, option: Optional[QStyleOptionFrame]) """
        pass

    def inputMask(self): # real signature unknown; restored from __doc__
        """ inputMask(self) -> str """
        return ""

    def inputMethodEvent(self, a0, QInputMethodEvent=None): # real signature unknown; restored from __doc__
        """ inputMethodEvent(self, a0: Optional[QInputMethodEvent]) """
        pass

    def inputMethodQuery(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        inputMethodQuery(self, a0: Qt.InputMethodQuery) -> Any
        inputMethodQuery(self, property: Qt.InputMethodQuery, argument: Any) -> Any
        """
        pass

    def inputRejected(self, *args, **kwargs): # real signature unknown
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

    def insert(self, a0, p_str=None): # real signature unknown; restored from __doc__
        """ insert(self, a0: Optional[str]) """
        pass

    def isClearButtonEnabled(self): # real signature unknown; restored from __doc__
        """ isClearButtonEnabled(self) -> bool """
        return False

    def isModified(self): # real signature unknown; restored from __doc__
        """ isModified(self) -> bool """
        return False

    def isReadOnly(self): # real signature unknown; restored from __doc__
        """ isReadOnly(self) -> bool """
        return False

    def isRedoAvailable(self): # real signature unknown; restored from __doc__
        """ isRedoAvailable(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def isUndoAvailable(self): # real signature unknown; restored from __doc__
        """ isUndoAvailable(self) -> bool """
        return False

    def keyPressEvent(self, a0, QKeyEvent=None): # real signature unknown; restored from __doc__
        """ keyPressEvent(self, a0: Optional[QKeyEvent]) """
        pass

    def keyReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def leaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def maxLength(self): # real signature unknown; restored from __doc__
        """ maxLength(self) -> int """
        return 0

    def metric(self, *args, **kwargs): # real signature unknown
        pass

    def minimumSizeHint(self): # real signature unknown; restored from __doc__
        """ minimumSizeHint(self) -> QSize """
        pass

    def mouseDoubleClickEvent(self, a0, QMouseEvent=None): # real signature unknown; restored from __doc__
        """ mouseDoubleClickEvent(self, a0: Optional[QMouseEvent]) """
        pass

    def mouseMoveEvent(self, a0, QMouseEvent=None): # real signature unknown; restored from __doc__
        """ mouseMoveEvent(self, a0: Optional[QMouseEvent]) """
        pass

    def mousePressEvent(self, a0, QMouseEvent=None): # real signature unknown; restored from __doc__
        """ mousePressEvent(self, a0: Optional[QMouseEvent]) """
        pass

    def mouseReleaseEvent(self, a0, QMouseEvent=None): # real signature unknown; restored from __doc__
        """ mouseReleaseEvent(self, a0: Optional[QMouseEvent]) """
        pass

    def moveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def nativeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def paintEvent(self, a0, QPaintEvent=None): # real signature unknown; restored from __doc__
        """ paintEvent(self, a0: Optional[QPaintEvent]) """
        pass

    def paste(self): # real signature unknown; restored from __doc__
        """ paste(self) """
        pass

    def placeholderText(self): # real signature unknown; restored from __doc__
        """ placeholderText(self) -> str """
        return ""

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def redo(self): # real signature unknown; restored from __doc__
        """ redo(self) """
        pass

    def resizeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def returnPressed(self, *args, **kwargs): # real signature unknown
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

    def selectAll(self): # real signature unknown; restored from __doc__
        """ selectAll(self) """
        pass

    def selectedText(self): # real signature unknown; restored from __doc__
        """ selectedText(self) -> str """
        return ""

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

    def selectionEnd(self): # real signature unknown; restored from __doc__
        """ selectionEnd(self) -> int """
        return 0

    def selectionLength(self): # real signature unknown; restored from __doc__
        """ selectionLength(self) -> int """
        return 0

    def selectionStart(self): # real signature unknown; restored from __doc__
        """ selectionStart(self) -> int """
        return 0

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setAlignment(self, flag, Qt_Alignment=None, Qt_AlignmentFlag=None): # real signature unknown; restored from __doc__
        """ setAlignment(self, flag: Union[Qt.Alignment, Qt.AlignmentFlag]) """
        pass

    def setClearButtonEnabled(self, enable): # real signature unknown; restored from __doc__
        """ setClearButtonEnabled(self, enable: bool) """
        pass

    def setCompleter(self, completer, QCompleter=None): # real signature unknown; restored from __doc__
        """ setCompleter(self, completer: Optional[QCompleter]) """
        pass

    def setCursorMoveStyle(self, style): # real signature unknown; restored from __doc__
        """ setCursorMoveStyle(self, style: Qt.CursorMoveStyle) """
        pass

    def setCursorPosition(self, a0): # real signature unknown; restored from __doc__
        """ setCursorPosition(self, a0: int) """
        pass

    def setDragEnabled(self, b): # real signature unknown; restored from __doc__
        """ setDragEnabled(self, b: bool) """
        pass

    def setEchoMode(self, a0): # real signature unknown; restored from __doc__
        """ setEchoMode(self, a0: QLineEdit.EchoMode) """
        pass

    def setFrame(self, a0): # real signature unknown; restored from __doc__
        """ setFrame(self, a0: bool) """
        pass

    def setInputMask(self, inputMask, p_str=None): # real signature unknown; restored from __doc__
        """ setInputMask(self, inputMask: Optional[str]) """
        pass

    def setMaxLength(self, a0): # real signature unknown; restored from __doc__
        """ setMaxLength(self, a0: int) """
        pass

    def setModified(self, a0): # real signature unknown; restored from __doc__
        """ setModified(self, a0: bool) """
        pass

    def setPlaceholderText(self, a0, p_str=None): # real signature unknown; restored from __doc__
        """ setPlaceholderText(self, a0: Optional[str]) """
        pass

    def setReadOnly(self, a0): # real signature unknown; restored from __doc__
        """ setReadOnly(self, a0: bool) """
        pass

    def setSelection(self, a0, a1): # real signature unknown; restored from __doc__
        """ setSelection(self, a0: int, a1: int) """
        pass

    def setText(self, a0, p_str=None): # real signature unknown; restored from __doc__
        """ setText(self, a0: Optional[str]) """
        pass

    def setTextMargins(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setTextMargins(self, left: int, top: int, right: int, bottom: int)
        setTextMargins(self, margins: QMargins)
        """
        pass

    def setValidator(self, a0, QValidator=None): # real signature unknown; restored from __doc__
        """ setValidator(self, a0: Optional[QValidator]) """
        pass

    def sharedPainter(self, *args, **kwargs): # real signature unknown
        pass

    def showEvent(self, *args, **kwargs): # real signature unknown
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> QSize """
        pass

    def tabletEvent(self, *args, **kwargs): # real signature unknown
        pass

    def text(self): # real signature unknown; restored from __doc__
        """ text(self) -> str """
        return ""

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

    def textEdited(self, *args, **kwargs): # real signature unknown
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

    def textMargins(self): # real signature unknown; restored from __doc__
        """ textMargins(self) -> QMargins """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def undo(self): # real signature unknown; restored from __doc__
        """ undo(self) """
        pass

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

    def validator(self): # real signature unknown; restored from __doc__
        """ validator(self) -> Optional[QValidator] """
        pass

    def wheelEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    LeadingPosition = 0
    NoEcho = 1
    Normal = 0
    Password = 2
    PasswordEchoOnEdit = 3
    TrailingPosition = 1


