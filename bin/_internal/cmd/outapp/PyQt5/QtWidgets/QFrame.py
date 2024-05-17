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

class QFrame(QWidget):
    """ QFrame(parent: Optional[QWidget] = None, flags: Union[Qt.WindowFlags, Qt.WindowType] = Qt.WindowFlags()) """
    def actionEvent(self, *args, **kwargs): # real signature unknown
        pass

    def changeEvent(self, a0, QEvent=None): # real signature unknown; restored from __doc__
        """ changeEvent(self, a0: Optional[QEvent]) """
        pass

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

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def dragEnterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dragLeaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dragMoveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def drawFrame(self, a0, QPainter=None): # real signature unknown; restored from __doc__
        """ drawFrame(self, a0: Optional[QPainter]) """
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

    def frameRect(self): # real signature unknown; restored from __doc__
        """ frameRect(self) -> QRect """
        pass

    def frameShadow(self): # real signature unknown; restored from __doc__
        """ frameShadow(self) -> QFrame.Shadow """
        pass

    def frameShape(self): # real signature unknown; restored from __doc__
        """ frameShape(self) -> QFrame.Shape """
        pass

    def frameStyle(self): # real signature unknown; restored from __doc__
        """ frameStyle(self) -> int """
        return 0

    def frameWidth(self): # real signature unknown; restored from __doc__
        """ frameWidth(self) -> int """
        return 0

    def hideEvent(self, *args, **kwargs): # real signature unknown
        pass

    def initPainter(self, *args, **kwargs): # real signature unknown
        pass

    def initStyleOption(self, option, QStyleOptionFrame=None): # real signature unknown; restored from __doc__
        """ initStyleOption(self, option: Optional[QStyleOptionFrame]) """
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

    def lineWidth(self): # real signature unknown; restored from __doc__
        """ lineWidth(self) -> int """
        return 0

    def metric(self, *args, **kwargs): # real signature unknown
        pass

    def midLineWidth(self): # real signature unknown; restored from __doc__
        """ midLineWidth(self) -> int """
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

    def paintEvent(self, a0, QPaintEvent=None): # real signature unknown; restored from __doc__
        """ paintEvent(self, a0: Optional[QPaintEvent]) """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def resizeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setFrameRect(self, a0): # real signature unknown; restored from __doc__
        """ setFrameRect(self, a0: QRect) """
        pass

    def setFrameShadow(self, a0): # real signature unknown; restored from __doc__
        """ setFrameShadow(self, a0: QFrame.Shadow) """
        pass

    def setFrameShape(self, a0): # real signature unknown; restored from __doc__
        """ setFrameShape(self, a0: QFrame.Shape) """
        pass

    def setFrameStyle(self, a0): # real signature unknown; restored from __doc__
        """ setFrameStyle(self, a0: int) """
        pass

    def setLineWidth(self, a0): # real signature unknown; restored from __doc__
        """ setLineWidth(self, a0: int) """
        pass

    def setMidLineWidth(self, a0): # real signature unknown; restored from __doc__
        """ setMidLineWidth(self, a0: int) """
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

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

    def wheelEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent, QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    Box = 1
    HLine = 4
    NoFrame = 0
    Panel = 2
    Plain = 16
    Raised = 32
    Shadow_Mask = 240
    Shape_Mask = 15
    StyledPanel = 6
    Sunken = 48
    VLine = 5
    WinPanel = 3


