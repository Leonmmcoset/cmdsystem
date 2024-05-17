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

class QAbstractSpinBox(QWidget):
    """ QAbstractSpinBox(parent: Optional[QWidget] = None) """
    def actionEvent(self, *args, **kwargs): # real signature unknown
        pass

    def alignment(self): # real signature unknown; restored from __doc__
        """ alignment(self) -> Qt.Alignment """
        pass

    def buttonSymbols(self): # real signature unknown; restored from __doc__
        """ buttonSymbols(self) -> QAbstractSpinBox.ButtonSymbols """
        pass

    def changeEvent(self, e, QEvent=None): # real signature unknown; restored from __doc__
        """ changeEvent(self, e: Optional[QEvent]) """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def closeEvent(self, e, QCloseEvent=None): # real signature unknown; restored from __doc__
        """ closeEvent(self, e: Optional[QCloseEvent]) """
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def contextMenuEvent(self, e, QContextMenuEvent=None): # real signature unknown; restored from __doc__
        """ contextMenuEvent(self, e: Optional[QContextMenuEvent]) """
        pass

    def correctionMode(self): # real signature unknown; restored from __doc__
        """ correctionMode(self) -> QAbstractSpinBox.CorrectionMode """
        pass

    def create(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def destroy(self, *args, **kwargs): # real signature unknown
        pass

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

    def enterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, event, QEvent=None): # real signature unknown; restored from __doc__
        """ event(self, event: Optional[QEvent]) -> bool """
        return False

    def fixup(self, input, p_str=None): # real signature unknown; restored from __doc__
        """ fixup(self, input: Optional[str]) -> str """
        return ""

    def focusInEvent(self, e, QFocusEvent=None): # real signature unknown; restored from __doc__
        """ focusInEvent(self, e: Optional[QFocusEvent]) """
        pass

    def focusNextChild(self, *args, **kwargs): # real signature unknown
        pass

    def focusNextPrevChild(self, *args, **kwargs): # real signature unknown
        pass

    def focusOutEvent(self, e, QFocusEvent=None): # real signature unknown; restored from __doc__
        """ focusOutEvent(self, e: Optional[QFocusEvent]) """
        pass

    def focusPreviousChild(self, *args, **kwargs): # real signature unknown
        pass

    def hasAcceptableInput(self): # real signature unknown; restored from __doc__
        """ hasAcceptableInput(self) -> bool """
        return False

    def hasFrame(self): # real signature unknown; restored from __doc__
        """ hasFrame(self) -> bool """
        return False

    def hideEvent(self, e, QHideEvent=None): # real signature unknown; restored from __doc__
        """ hideEvent(self, e: Optional[QHideEvent]) """
        pass

    def initPainter(self, *args, **kwargs): # real signature unknown
        pass

    def initStyleOption(self, option, QStyleOptionSpinBox=None): # real signature unknown; restored from __doc__
        """ initStyleOption(self, option: Optional[QStyleOptionSpinBox]) """
        pass

    def inputMethodEvent(self, *args, **kwargs): # real signature unknown
        pass

    def inputMethodQuery(self, a0): # real signature unknown; restored from __doc__
        """ inputMethodQuery(self, a0: Qt.InputMethodQuery) -> Any """
        pass

    def interpretText(self): # real signature unknown; restored from __doc__
        """ interpretText(self) """
        pass

    def isAccelerated(self): # real signature unknown; restored from __doc__
        """ isAccelerated(self) -> bool """
        return False

    def isGroupSeparatorShown(self): # real signature unknown; restored from __doc__
        """ isGroupSeparatorShown(self) -> bool """
        return False

    def isReadOnly(self): # real signature unknown; restored from __doc__
        """ isReadOnly(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def keyboardTracking(self): # real signature unknown; restored from __doc__
        """ keyboardTracking(self) -> bool """
        return False

    def keyPressEvent(self, e, QKeyEvent=None): # real signature unknown; restored from __doc__
        """ keyPressEvent(self, e: Optional[QKeyEvent]) """
        pass

    def keyReleaseEvent(self, e, QKeyEvent=None): # real signature unknown; restored from __doc__
        """ keyReleaseEvent(self, e: Optional[QKeyEvent]) """
        pass

    def leaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def lineEdit(self): # real signature unknown; restored from __doc__
        """ lineEdit(self) -> Optional[QLineEdit] """
        pass

    def metric(self, *args, **kwargs): # real signature unknown
        pass

    def minimumSizeHint(self): # real signature unknown; restored from __doc__
        """ minimumSizeHint(self) -> QSize """
        pass

    def mouseDoubleClickEvent(self, *args, **kwargs): # real signature unknown
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

    def moveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def nativeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def paintEvent(self, e, QPaintEvent=None): # real signature unknown; restored from __doc__
        """ paintEvent(self, e: Optional[QPaintEvent]) """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def resizeEvent(self, e, QResizeEvent=None): # real signature unknown; restored from __doc__
        """ resizeEvent(self, e: Optional[QResizeEvent]) """
        pass

    def selectAll(self): # real signature unknown; restored from __doc__
        """ selectAll(self) """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setAccelerated(self, on): # real signature unknown; restored from __doc__
        """ setAccelerated(self, on: bool) """
        pass

    def setAlignment(self, flag, Qt_Alignment=None, Qt_AlignmentFlag=None): # real signature unknown; restored from __doc__
        """ setAlignment(self, flag: Union[Qt.Alignment, Qt.AlignmentFlag]) """
        pass

    def setButtonSymbols(self, bs): # real signature unknown; restored from __doc__
        """ setButtonSymbols(self, bs: QAbstractSpinBox.ButtonSymbols) """
        pass

    def setCorrectionMode(self, cm): # real signature unknown; restored from __doc__
        """ setCorrectionMode(self, cm: QAbstractSpinBox.CorrectionMode) """
        pass

    def setFrame(self, a0): # real signature unknown; restored from __doc__
        """ setFrame(self, a0: bool) """
        pass

    def setGroupSeparatorShown(self, shown): # real signature unknown; restored from __doc__
        """ setGroupSeparatorShown(self, shown: bool) """
        pass

    def setKeyboardTracking(self, kt): # real signature unknown; restored from __doc__
        """ setKeyboardTracking(self, kt: bool) """
        pass

    def setLineEdit(self, e, QLineEdit=None): # real signature unknown; restored from __doc__
        """ setLineEdit(self, e: Optional[QLineEdit]) """
        pass

    def setReadOnly(self, r): # real signature unknown; restored from __doc__
        """ setReadOnly(self, r: bool) """
        pass

    def setSpecialValueText(self, s, p_str=None): # real signature unknown; restored from __doc__
        """ setSpecialValueText(self, s: Optional[str]) """
        pass

    def setWrapping(self, w): # real signature unknown; restored from __doc__
        """ setWrapping(self, w: bool) """
        pass

    def sharedPainter(self, *args, **kwargs): # real signature unknown
        pass

    def showEvent(self, e, QShowEvent=None): # real signature unknown; restored from __doc__
        """ showEvent(self, e: Optional[QShowEvent]) """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> QSize """
        pass

    def specialValueText(self): # real signature unknown; restored from __doc__
        """ specialValueText(self) -> str """
        return ""

    def stepBy(self, steps): # real signature unknown; restored from __doc__
        """ stepBy(self, steps: int) """
        pass

    def stepDown(self): # real signature unknown; restored from __doc__
        """ stepDown(self) """
        pass

    def stepEnabled(self): # real signature unknown; restored from __doc__
        """ stepEnabled(self) -> QAbstractSpinBox.StepEnabled """
        pass

    def stepUp(self): # real signature unknown; restored from __doc__
        """ stepUp(self) """
        pass

    def tabletEvent(self, *args, **kwargs): # real signature unknown
        pass

    def text(self): # real signature unknown; restored from __doc__
        """ text(self) -> str """
        return ""

    def timerEvent(self, e, QTimerEvent=None): # real signature unknown; restored from __doc__
        """ timerEvent(self, e: Optional[QTimerEvent]) """
        pass

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

    def validate(self, input, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ validate(self, input: Optional[str], pos: int) -> (QValidator.State, str, int) """
        pass

    def wheelEvent(self, e, QWheelEvent=None): # real signature unknown; restored from __doc__
        """ wheelEvent(self, e: Optional[QWheelEvent]) """
        pass

    def wrapping(self): # real signature unknown; restored from __doc__
        """ wrapping(self) -> bool """
        return False

    def __init__(self, parent, QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    AdaptiveDecimalStepType = 1
    CorrectToNearestValue = 1
    CorrectToPreviousValue = 0
    DefaultStepType = 0
    NoButtons = 2
    PlusMinus = 1
    StepDownEnabled = 2
    StepNone = 0
    StepUpEnabled = 1
    UpDownArrows = 0


