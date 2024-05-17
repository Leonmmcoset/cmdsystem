# encoding: utf-8
# module PyQt5.QtWidgets
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


from .QDialog import QDialog

class QMessageBox(QDialog):
    """
    QMessageBox(parent: Optional[QWidget] = None)
    QMessageBox(icon: QMessageBox.Icon, title: Optional[str], text: Optional[str], buttons: Union[QMessageBox.StandardButtons, QMessageBox.StandardButton] = QMessageBox.NoButton, parent: Optional[QWidget] = None, flags: Union[Qt.WindowFlags, Qt.WindowType] = Qt.Dialog|Qt.MSWindowsFixedSizeDialogHint)
    """
    def about(self, parent, QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ about(parent: Optional[QWidget], caption: Optional[str], text: Optional[str]) """
        pass

    def aboutQt(self, parent, QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ aboutQt(parent: Optional[QWidget], title: Optional[str] = '') """
        pass

    def actionEvent(self, *args, **kwargs): # real signature unknown
        pass

    def addButton(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        addButton(self, button: Optional[QAbstractButton], role: QMessageBox.ButtonRole)
        addButton(self, text: Optional[str], role: QMessageBox.ButtonRole) -> Optional[QPushButton]
        addButton(self, button: QMessageBox.StandardButton) -> Optional[QPushButton]
        """
        pass

    def button(self, which): # real signature unknown; restored from __doc__
        """ button(self, which: QMessageBox.StandardButton) -> Optional[QAbstractButton] """
        pass

    def buttonClicked(self, *args, **kwargs): # real signature unknown
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

    def buttonRole(self, button, QAbstractButton=None): # real signature unknown; restored from __doc__
        """ buttonRole(self, button: Optional[QAbstractButton]) -> QMessageBox.ButtonRole """
        pass

    def buttons(self): # real signature unknown; restored from __doc__
        """ buttons(self) -> List[QAbstractButton] """
        return []

    def changeEvent(self, a0, QEvent=None): # real signature unknown; restored from __doc__
        """ changeEvent(self, a0: Optional[QEvent]) """
        pass

    def checkBox(self): # real signature unknown; restored from __doc__
        """ checkBox(self) -> Optional[QCheckBox] """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def clickedButton(self): # real signature unknown; restored from __doc__
        """ clickedButton(self) -> Optional[QAbstractButton] """
        pass

    def closeEvent(self, a0, QCloseEvent=None): # real signature unknown; restored from __doc__
        """ closeEvent(self, a0: Optional[QCloseEvent]) """
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def contextMenuEvent(self, *args, **kwargs): # real signature unknown
        pass

    def create(self, *args, **kwargs): # real signature unknown
        pass

    def critical(self, parent, QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ critical(parent: Optional[QWidget], title: Optional[str], text: Optional[str], buttons: Union[QMessageBox.StandardButtons, QMessageBox.StandardButton] = QMessageBox.Ok, defaultButton: QMessageBox.StandardButton = QMessageBox.NoButton) -> QMessageBox.StandardButton """
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def defaultButton(self): # real signature unknown; restored from __doc__
        """ defaultButton(self) -> Optional[QPushButton] """
        pass

    def destroy(self, *args, **kwargs): # real signature unknown
        pass

    def detailedText(self): # real signature unknown; restored from __doc__
        """ detailedText(self) -> str """
        return ""

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def dragEnterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dragLeaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dragMoveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dropEvent(self, *args, **kwargs): # real signature unknown
        pass

    def enterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def escapeButton(self): # real signature unknown; restored from __doc__
        """ escapeButton(self) -> Optional[QAbstractButton] """
        pass

    def event(self, e, QEvent=None): # real signature unknown; restored from __doc__
        """ event(self, e: Optional[QEvent]) -> bool """
        return False

    def eventFilter(self, *args, **kwargs): # real signature unknown
        pass

    def focusInEvent(self, *args, **kwargs): # real signature unknown
        pass

    def focusNextChild(self, *args, **kwargs): # real signature unknown
        pass

    def focusNextPrevChild(self, *args, **kwargs): # real signature unknown
        pass

    def focusOutEvent(self, *args, **kwargs): # real signature unknown
        pass

    def focusPreviousChild(self, *args, **kwargs): # real signature unknown
        pass

    def hideEvent(self, *args, **kwargs): # real signature unknown
        pass

    def icon(self): # real signature unknown; restored from __doc__
        """ icon(self) -> QMessageBox.Icon """
        pass

    def iconPixmap(self): # real signature unknown; restored from __doc__
        """ iconPixmap(self) -> QPixmap """
        pass

    def information(self, parent, QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ information(parent: Optional[QWidget], title: Optional[str], text: Optional[str], buttons: Union[QMessageBox.StandardButtons, QMessageBox.StandardButton] = QMessageBox.Ok, defaultButton: QMessageBox.StandardButton = QMessageBox.NoButton) -> QMessageBox.StandardButton """
        pass

    def informativeText(self): # real signature unknown; restored from __doc__
        """ informativeText(self) -> str """
        return ""

    def initPainter(self, *args, **kwargs): # real signature unknown
        pass

    def inputMethodEvent(self, *args, **kwargs): # real signature unknown
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def keyPressEvent(self, a0, QKeyEvent=None): # real signature unknown; restored from __doc__
        """ keyPressEvent(self, a0: Optional[QKeyEvent]) """
        pass

    def keyReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def leaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def metric(self, *args, **kwargs): # real signature unknown
        pass

    def mouseDoubleClickEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mouseMoveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mousePressEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mouseReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def moveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def nativeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def open(self, slot=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        open(self)
        open(self, slot: PYQT_SLOT)
        """
        pass

    def paintEvent(self, *args, **kwargs): # real signature unknown
        pass

    def question(self, parent, QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ question(parent: Optional[QWidget], title: Optional[str], text: Optional[str], buttons: Union[QMessageBox.StandardButtons, QMessageBox.StandardButton] = QMessageBox.StandardButtons(QMessageBox.Yes|QMessageBox.No), defaultButton: QMessageBox.StandardButton = QMessageBox.NoButton) -> QMessageBox.StandardButton """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def removeButton(self, button, QAbstractButton=None): # real signature unknown; restored from __doc__
        """ removeButton(self, button: Optional[QAbstractButton]) """
        pass

    def resizeEvent(self, a0, QResizeEvent=None): # real signature unknown; restored from __doc__
        """ resizeEvent(self, a0: Optional[QResizeEvent]) """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setCheckBox(self, cb, QCheckBox=None): # real signature unknown; restored from __doc__
        """ setCheckBox(self, cb: Optional[QCheckBox]) """
        pass

    def setDefaultButton(self, button, QPushButton=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setDefaultButton(self, button: Optional[QPushButton])
        setDefaultButton(self, button: QMessageBox.StandardButton)
        """
        pass

    def setDetailedText(self, text, p_str=None): # real signature unknown; restored from __doc__
        """ setDetailedText(self, text: Optional[str]) """
        pass

    def setEscapeButton(self, button, QAbstractButton=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setEscapeButton(self, button: Optional[QAbstractButton])
        setEscapeButton(self, button: QMessageBox.StandardButton)
        """
        pass

    def setIcon(self, a0): # real signature unknown; restored from __doc__
        """ setIcon(self, a0: QMessageBox.Icon) """
        pass

    def setIconPixmap(self, a0): # real signature unknown; restored from __doc__
        """ setIconPixmap(self, a0: QPixmap) """
        pass

    def setInformativeText(self, text, p_str=None): # real signature unknown; restored from __doc__
        """ setInformativeText(self, text: Optional[str]) """
        pass

    def setStandardButtons(self, buttons, QMessageBox_StandardButtons=None, QMessageBox_StandardButton=None): # real signature unknown; restored from __doc__
        """ setStandardButtons(self, buttons: Union[QMessageBox.StandardButtons, QMessageBox.StandardButton]) """
        pass

    def setText(self, a0, p_str=None): # real signature unknown; restored from __doc__
        """ setText(self, a0: Optional[str]) """
        pass

    def setTextFormat(self, a0): # real signature unknown; restored from __doc__
        """ setTextFormat(self, a0: Qt.TextFormat) """
        pass

    def setTextInteractionFlags(self, flags, Qt_TextInteractionFlags=None, Qt_TextInteractionFlag=None): # real signature unknown; restored from __doc__
        """ setTextInteractionFlags(self, flags: Union[Qt.TextInteractionFlags, Qt.TextInteractionFlag]) """
        pass

    def setWindowModality(self, windowModality): # real signature unknown; restored from __doc__
        """ setWindowModality(self, windowModality: Qt.WindowModality) """
        pass

    def setWindowTitle(self, title, p_str=None): # real signature unknown; restored from __doc__
        """ setWindowTitle(self, title: Optional[str]) """
        pass

    def sharedPainter(self, *args, **kwargs): # real signature unknown
        pass

    def showEvent(self, a0, QShowEvent=None): # real signature unknown; restored from __doc__
        """ showEvent(self, a0: Optional[QShowEvent]) """
        pass

    def standardButton(self, button, QAbstractButton=None): # real signature unknown; restored from __doc__
        """ standardButton(self, button: Optional[QAbstractButton]) -> QMessageBox.StandardButton """
        pass

    def standardButtons(self): # real signature unknown; restored from __doc__
        """ standardButtons(self) -> QMessageBox.StandardButtons """
        pass

    def standardIcon(self, icon): # real signature unknown; restored from __doc__
        """ standardIcon(icon: QMessageBox.Icon) -> QPixmap """
        pass

    def tabletEvent(self, *args, **kwargs): # real signature unknown
        pass

    def text(self): # real signature unknown; restored from __doc__
        """ text(self) -> str """
        return ""

    def textFormat(self): # real signature unknown; restored from __doc__
        """ textFormat(self) -> Qt.TextFormat """
        pass

    def textInteractionFlags(self): # real signature unknown; restored from __doc__
        """ textInteractionFlags(self) -> Qt.TextInteractionFlags """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

    def warning(self, parent, QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ warning(parent: Optional[QWidget], title: Optional[str], text: Optional[str], buttons: Union[QMessageBox.StandardButtons, QMessageBox.StandardButton] = QMessageBox.Ok, defaultButton: QMessageBox.StandardButton = QMessageBox.NoButton) -> QMessageBox.StandardButton """
        pass

    def wheelEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    Abort = 262144
    AcceptRole = 0
    ActionRole = 3
    Apply = 33554432
    ApplyRole = 8
    ButtonMask = -769
    Cancel = 4194304
    Close = 2097152
    Critical = 3
    Default = 256
    DestructiveRole = 2
    Discard = 8388608
    Escape = 512
    FirstButton = 1024
    FlagMask = 768
    Help = 16777216
    HelpRole = 4
    Ignore = 1048576
    Information = 1
    InvalidRole = -1
    LastButton = 134217728
    No = 65536
    NoAll = 131072
    NoButton = 0
    NoIcon = 0
    NoRole = 6
    NoToAll = 131072
    Ok = 1024
    Open = 8192
    Question = 4
    RejectRole = 1
    Reset = 67108864
    ResetRole = 7
    RestoreDefaults = 134217728
    Retry = 524288
    Save = 2048
    SaveAll = 4096
    Warning = 2
    Yes = 16384
    YesAll = 32768
    YesRole = 5
    YesToAll = 32768


