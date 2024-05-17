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

class QProgressDialog(QDialog):
    """
    QProgressDialog(parent: Optional[QWidget] = None, flags: Union[Qt.WindowFlags, Qt.WindowType] = Qt.WindowFlags())
    QProgressDialog(labelText: Optional[str], cancelButtonText: Optional[str], minimum: int, maximum: int, parent: Optional[QWidget] = None, flags: Union[Qt.WindowFlags, Qt.WindowType] = Qt.WindowFlags())
    """
    def actionEvent(self, *args, **kwargs): # real signature unknown
        pass

    def autoClose(self): # real signature unknown; restored from __doc__
        """ autoClose(self) -> bool """
        return False

    def autoReset(self): # real signature unknown; restored from __doc__
        """ autoReset(self) -> bool """
        return False

    def cancel(self): # real signature unknown; restored from __doc__
        """ cancel(self) """
        pass

    def canceled(self, *args, **kwargs): # real signature unknown
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

    def changeEvent(self, a0, QEvent=None): # real signature unknown; restored from __doc__
        """ changeEvent(self, a0: Optional[QEvent]) """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
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

    def enterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, *args, **kwargs): # real signature unknown
        pass

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

    def forceShow(self): # real signature unknown; restored from __doc__
        """ forceShow(self) """
        pass

    def hideEvent(self, *args, **kwargs): # real signature unknown
        pass

    def initPainter(self, *args, **kwargs): # real signature unknown
        pass

    def inputMethodEvent(self, *args, **kwargs): # real signature unknown
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def keyPressEvent(self, *args, **kwargs): # real signature unknown
        pass

    def keyReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def labelText(self): # real signature unknown; restored from __doc__
        """ labelText(self) -> str """
        return ""

    def leaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def maximum(self): # real signature unknown; restored from __doc__
        """ maximum(self) -> int """
        return 0

    def metric(self, *args, **kwargs): # real signature unknown
        pass

    def minimum(self): # real signature unknown; restored from __doc__
        """ minimum(self) -> int """
        return 0

    def minimumDuration(self): # real signature unknown; restored from __doc__
        """ minimumDuration(self) -> int """
        return 0

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

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def reset(self): # real signature unknown; restored from __doc__
        """ reset(self) """
        pass

    def resizeEvent(self, a0, QResizeEvent=None): # real signature unknown; restored from __doc__
        """ resizeEvent(self, a0: Optional[QResizeEvent]) """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setAutoClose(self, b): # real signature unknown; restored from __doc__
        """ setAutoClose(self, b: bool) """
        pass

    def setAutoReset(self, b): # real signature unknown; restored from __doc__
        """ setAutoReset(self, b: bool) """
        pass

    def setBar(self, bar, QProgressBar=None): # real signature unknown; restored from __doc__
        """ setBar(self, bar: Optional[QProgressBar]) """
        pass

    def setCancelButton(self, button, QPushButton=None): # real signature unknown; restored from __doc__
        """ setCancelButton(self, button: Optional[QPushButton]) """
        pass

    def setCancelButtonText(self, a0, p_str=None): # real signature unknown; restored from __doc__
        """ setCancelButtonText(self, a0: Optional[str]) """
        pass

    def setLabel(self, label, QLabel=None): # real signature unknown; restored from __doc__
        """ setLabel(self, label: Optional[QLabel]) """
        pass

    def setLabelText(self, a0, p_str=None): # real signature unknown; restored from __doc__
        """ setLabelText(self, a0: Optional[str]) """
        pass

    def setMaximum(self, maximum): # real signature unknown; restored from __doc__
        """ setMaximum(self, maximum: int) """
        pass

    def setMinimum(self, minimum): # real signature unknown; restored from __doc__
        """ setMinimum(self, minimum: int) """
        pass

    def setMinimumDuration(self, ms): # real signature unknown; restored from __doc__
        """ setMinimumDuration(self, ms: int) """
        pass

    def setRange(self, minimum, maximum): # real signature unknown; restored from __doc__
        """ setRange(self, minimum: int, maximum: int) """
        pass

    def setValue(self, progress): # real signature unknown; restored from __doc__
        """ setValue(self, progress: int) """
        pass

    def sharedPainter(self, *args, **kwargs): # real signature unknown
        pass

    def showEvent(self, e, QShowEvent=None): # real signature unknown; restored from __doc__
        """ showEvent(self, e: Optional[QShowEvent]) """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> QSize """
        pass

    def tabletEvent(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

    def value(self): # real signature unknown; restored from __doc__
        """ value(self) -> int """
        return 0

    def wasCanceled(self): # real signature unknown; restored from __doc__
        """ wasCanceled(self) -> bool """
        return False

    def wheelEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


