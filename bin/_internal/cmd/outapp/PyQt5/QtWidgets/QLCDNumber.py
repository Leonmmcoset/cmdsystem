# encoding: utf-8
# module PyQt5.QtWidgets
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


from .QFrame import QFrame

class QLCDNumber(QFrame):
    """
    QLCDNumber(parent: Optional[QWidget] = None)
    QLCDNumber(numDigits: int, parent: Optional[QWidget] = None)
    """
    def actionEvent(self, *args, **kwargs): # real signature unknown
        pass

    def changeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def checkOverflow(self, num): # real signature unknown; restored from __doc__ with multiple overloads
        """
        checkOverflow(self, num: float) -> bool
        checkOverflow(self, num: int) -> bool
        """
        return False

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

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

    def digitCount(self): # real signature unknown; restored from __doc__
        """ digitCount(self) -> int """
        return 0

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def display(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        display(self, str: Optional[str])
        display(self, num: float)
        display(self, num: int)
        """
        pass

    def dragEnterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dragLeaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dragMoveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def drawFrame(self, *args, **kwargs): # real signature unknown
        pass

    def dropEvent(self, *args, **kwargs): # real signature unknown
        pass

    def enterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, e, QEvent=None): # real signature unknown; restored from __doc__
        """ event(self, e: Optional[QEvent]) -> bool """
        return False

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

    def intValue(self): # real signature unknown; restored from __doc__
        """ intValue(self) -> int """
        return 0

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def keyPressEvent(self, *args, **kwargs): # real signature unknown
        pass

    def keyReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def leaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def metric(self, *args, **kwargs): # real signature unknown
        pass

    def mode(self): # real signature unknown; restored from __doc__
        """ mode(self) -> QLCDNumber.Mode """
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

    def overflow(self, *args, **kwargs): # real signature unknown
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

    def paintEvent(self, a0, QPaintEvent=None): # real signature unknown; restored from __doc__
        """ paintEvent(self, a0: Optional[QPaintEvent]) """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def resizeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def segmentStyle(self): # real signature unknown; restored from __doc__
        """ segmentStyle(self) -> QLCDNumber.SegmentStyle """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setBinMode(self): # real signature unknown; restored from __doc__
        """ setBinMode(self) """
        pass

    def setDecMode(self): # real signature unknown; restored from __doc__
        """ setDecMode(self) """
        pass

    def setDigitCount(self, nDigits): # real signature unknown; restored from __doc__
        """ setDigitCount(self, nDigits: int) """
        pass

    def setHexMode(self): # real signature unknown; restored from __doc__
        """ setHexMode(self) """
        pass

    def setMode(self, a0): # real signature unknown; restored from __doc__
        """ setMode(self, a0: QLCDNumber.Mode) """
        pass

    def setNumDigits(self, nDigits): # real signature unknown; restored from __doc__
        """ setNumDigits(self, nDigits: int) """
        pass

    def setOctMode(self): # real signature unknown; restored from __doc__
        """ setOctMode(self) """
        pass

    def setSegmentStyle(self, a0): # real signature unknown; restored from __doc__
        """ setSegmentStyle(self, a0: QLCDNumber.SegmentStyle) """
        pass

    def setSmallDecimalPoint(self, a0): # real signature unknown; restored from __doc__
        """ setSmallDecimalPoint(self, a0: bool) """
        pass

    def sharedPainter(self, *args, **kwargs): # real signature unknown
        pass

    def showEvent(self, *args, **kwargs): # real signature unknown
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> QSize """
        pass

    def smallDecimalPoint(self): # real signature unknown; restored from __doc__
        """ smallDecimalPoint(self) -> bool """
        return False

    def tabletEvent(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

    def value(self): # real signature unknown; restored from __doc__
        """ value(self) -> float """
        return 0.0

    def wheelEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    Bin = 3
    Dec = 1
    Filled = 1
    Flat = 2
    Hex = 0
    Oct = 2
    Outline = 0


