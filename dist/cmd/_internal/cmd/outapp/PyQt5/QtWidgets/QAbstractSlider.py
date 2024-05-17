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

class QAbstractSlider(QWidget):
    """ QAbstractSlider(parent: Optional[QWidget] = None) """
    def actionEvent(self, *args, **kwargs): # real signature unknown
        pass

    def actionTriggered(self, *args, **kwargs): # real signature unknown
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

    def changeEvent(self, e, QEvent=None): # real signature unknown; restored from __doc__
        """ changeEvent(self, e: Optional[QEvent]) """
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

    def hasTracking(self): # real signature unknown; restored from __doc__
        """ hasTracking(self) -> bool """
        return False

    def hideEvent(self, *args, **kwargs): # real signature unknown
        pass

    def initPainter(self, *args, **kwargs): # real signature unknown
        pass

    def inputMethodEvent(self, *args, **kwargs): # real signature unknown
        pass

    def invertedAppearance(self): # real signature unknown; restored from __doc__
        """ invertedAppearance(self) -> bool """
        return False

    def invertedControls(self): # real signature unknown; restored from __doc__
        """ invertedControls(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def isSliderDown(self): # real signature unknown; restored from __doc__
        """ isSliderDown(self) -> bool """
        return False

    def keyPressEvent(self, ev, QKeyEvent=None): # real signature unknown; restored from __doc__
        """ keyPressEvent(self, ev: Optional[QKeyEvent]) """
        pass

    def keyReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

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

    def orientation(self): # real signature unknown; restored from __doc__
        """ orientation(self) -> Qt.Orientation """
        pass

    def pageStep(self): # real signature unknown; restored from __doc__
        """ pageStep(self) -> int """
        return 0

    def paintEvent(self, *args, **kwargs): # real signature unknown
        pass

    def rangeChanged(self, *args, **kwargs): # real signature unknown
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

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def repeatAction(self): # real signature unknown; restored from __doc__
        """ repeatAction(self) -> QAbstractSlider.SliderAction """
        pass

    def resizeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setInvertedAppearance(self, a0): # real signature unknown; restored from __doc__
        """ setInvertedAppearance(self, a0: bool) """
        pass

    def setInvertedControls(self, a0): # real signature unknown; restored from __doc__
        """ setInvertedControls(self, a0: bool) """
        pass

    def setMaximum(self, a0): # real signature unknown; restored from __doc__
        """ setMaximum(self, a0: int) """
        pass

    def setMinimum(self, a0): # real signature unknown; restored from __doc__
        """ setMinimum(self, a0: int) """
        pass

    def setOrientation(self, a0): # real signature unknown; restored from __doc__
        """ setOrientation(self, a0: Qt.Orientation) """
        pass

    def setPageStep(self, a0): # real signature unknown; restored from __doc__
        """ setPageStep(self, a0: int) """
        pass

    def setRange(self, min, max): # real signature unknown; restored from __doc__
        """ setRange(self, min: int, max: int) """
        pass

    def setRepeatAction(self, action, thresholdTime=500, repeatTime=50): # real signature unknown; restored from __doc__
        """ setRepeatAction(self, action: QAbstractSlider.SliderAction, thresholdTime: int = 500, repeatTime: int = 50) """
        pass

    def setSingleStep(self, a0): # real signature unknown; restored from __doc__
        """ setSingleStep(self, a0: int) """
        pass

    def setSliderDown(self, a0): # real signature unknown; restored from __doc__
        """ setSliderDown(self, a0: bool) """
        pass

    def setSliderPosition(self, a0): # real signature unknown; restored from __doc__
        """ setSliderPosition(self, a0: int) """
        pass

    def setTracking(self, enable): # real signature unknown; restored from __doc__
        """ setTracking(self, enable: bool) """
        pass

    def setValue(self, a0): # real signature unknown; restored from __doc__
        """ setValue(self, a0: int) """
        pass

    def sharedPainter(self, *args, **kwargs): # real signature unknown
        pass

    def showEvent(self, *args, **kwargs): # real signature unknown
        pass

    def singleStep(self): # real signature unknown; restored from __doc__
        """ singleStep(self) -> int """
        return 0

    def sliderChange(self, change): # real signature unknown; restored from __doc__
        """ sliderChange(self, change: QAbstractSlider.SliderChange) """
        pass

    def sliderMoved(self, *args, **kwargs): # real signature unknown
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

    def sliderPosition(self): # real signature unknown; restored from __doc__
        """ sliderPosition(self) -> int """
        return 0

    def sliderPressed(self, *args, **kwargs): # real signature unknown
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

    def sliderReleased(self, *args, **kwargs): # real signature unknown
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

    def tabletEvent(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, a0, QTimerEvent=None): # real signature unknown; restored from __doc__
        """ timerEvent(self, a0: Optional[QTimerEvent]) """
        pass

    def triggerAction(self, action): # real signature unknown; restored from __doc__
        """ triggerAction(self, action: QAbstractSlider.SliderAction) """
        pass

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
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

    def wheelEvent(self, e, QWheelEvent=None): # real signature unknown; restored from __doc__
        """ wheelEvent(self, e: Optional[QWheelEvent]) """
        pass

    def __init__(self, parent, QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    SliderMove = 7
    SliderNoAction = 0
    SliderOrientationChange = 1
    SliderPageStepAdd = 3
    SliderPageStepSub = 4
    SliderRangeChange = 0
    SliderSingleStepAdd = 1
    SliderSingleStepSub = 2
    SliderStepsChange = 2
    SliderToMaximum = 6
    SliderToMinimum = 5
    SliderValueChange = 3


