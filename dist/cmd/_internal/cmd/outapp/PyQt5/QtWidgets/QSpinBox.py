# encoding: utf-8
# module PyQt5.QtWidgets
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


from .QAbstractSpinBox import QAbstractSpinBox

class QSpinBox(QAbstractSpinBox):
    """ QSpinBox(parent: Optional[QWidget] = None) """
    def actionEvent(self, *args, **kwargs): # real signature unknown
        pass

    def changeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def cleanText(self): # real signature unknown; restored from __doc__
        """ cleanText(self) -> str """
        return ""

    def closeEvent(self, *args, **kwargs): # real signature unknown
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

    def displayIntegerBase(self): # real signature unknown; restored from __doc__
        """ displayIntegerBase(self) -> int """
        return 0

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

    def event(self, e, QEvent=None): # real signature unknown; restored from __doc__
        """ event(self, e: Optional[QEvent]) -> bool """
        return False

    def fixup(self, p_str, p_str=None): # real signature unknown; restored from __doc__
        """ fixup(self, str: Optional[str]) -> str """
        return ""

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

    def initPainter(self, *args, **kwargs): # real signature unknown
        pass

    def initStyleOption(self, *args, **kwargs): # real signature unknown
        pass

    def inputMethodEvent(self, *args, **kwargs): # real signature unknown
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def keyPressEvent(self, *args, **kwargs): # real signature unknown
        pass

    def keyReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def leaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def lineEdit(self, *args, **kwargs): # real signature unknown
        pass

    def maximum(self): # real signature unknown; restored from __doc__
        """ maximum(self) -> int """
        return 0

    def metric(self, *args, **kwargs): # real signature unknown
        pass

    def minimum(self): # real signature unknown; restored from __doc__
        """ minimum(self) -> int """
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

    def paintEvent(self, *args, **kwargs): # real signature unknown
        pass

    def prefix(self): # real signature unknown; restored from __doc__
        """ prefix(self) -> str """
        return ""

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def resizeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setDisplayIntegerBase(self, base): # real signature unknown; restored from __doc__
        """ setDisplayIntegerBase(self, base: int) """
        pass

    def setLineEdit(self, *args, **kwargs): # real signature unknown
        pass

    def setMaximum(self, max): # real signature unknown; restored from __doc__
        """ setMaximum(self, max: int) """
        pass

    def setMinimum(self, min): # real signature unknown; restored from __doc__
        """ setMinimum(self, min: int) """
        pass

    def setPrefix(self, p, p_str=None): # real signature unknown; restored from __doc__
        """ setPrefix(self, p: Optional[str]) """
        pass

    def setRange(self, min, max): # real signature unknown; restored from __doc__
        """ setRange(self, min: int, max: int) """
        pass

    def setSingleStep(self, val): # real signature unknown; restored from __doc__
        """ setSingleStep(self, val: int) """
        pass

    def setStepType(self, stepType): # real signature unknown; restored from __doc__
        """ setStepType(self, stepType: QAbstractSpinBox.StepType) """
        pass

    def setSuffix(self, s, p_str=None): # real signature unknown; restored from __doc__
        """ setSuffix(self, s: Optional[str]) """
        pass

    def setValue(self, val): # real signature unknown; restored from __doc__
        """ setValue(self, val: int) """
        pass

    def sharedPainter(self, *args, **kwargs): # real signature unknown
        pass

    def showEvent(self, *args, **kwargs): # real signature unknown
        pass

    def singleStep(self): # real signature unknown; restored from __doc__
        """ singleStep(self) -> int """
        return 0

    def stepEnabled(self, *args, **kwargs): # real signature unknown
        pass

    def stepType(self): # real signature unknown; restored from __doc__
        """ stepType(self) -> QAbstractSpinBox.StepType """
        pass

    def suffix(self): # real signature unknown; restored from __doc__
        """ suffix(self) -> str """
        return ""

    def tabletEvent(self, *args, **kwargs): # real signature unknown
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

    def textFromValue(self, v): # real signature unknown; restored from __doc__
        """ textFromValue(self, v: int) -> str """
        return ""

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

    def validate(self, input, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ validate(self, input: Optional[str], pos: int) -> (QValidator.State, str, int) """
        pass

    def value(self): # real signature unknown; restored from __doc__
        """ value(self) -> int """
        return 0

    def valueChanged(self, *args, **kwargs): # real signature unknown
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

    def valueFromText(self, text, p_str=None): # real signature unknown; restored from __doc__
        """ valueFromText(self, text: Optional[str]) -> int """
        return 0

    def wheelEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent, QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass


