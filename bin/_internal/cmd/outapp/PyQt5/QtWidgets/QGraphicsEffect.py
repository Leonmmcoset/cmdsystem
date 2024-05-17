# encoding: utf-8
# module PyQt5.QtWidgets
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


class QGraphicsEffect(__PyQt5_QtCore.QObject):
    """ QGraphicsEffect(parent: Optional[QObject] = None) """
    def boundingRect(self): # real signature unknown; restored from __doc__
        """ boundingRect(self) -> QRectF """
        pass

    def boundingRectFor(self, sourceRect): # real signature unknown; restored from __doc__
        """ boundingRectFor(self, sourceRect: QRectF) -> QRectF """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def draw(self, painter, QPainter=None): # real signature unknown; restored from __doc__
        """ draw(self, painter: Optional[QPainter]) """
        pass

    def drawSource(self, painter, QPainter=None): # real signature unknown; restored from __doc__
        """ drawSource(self, painter: Optional[QPainter]) """
        pass

    def enabledChanged(self, *args, **kwargs): # real signature unknown
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

    def isEnabled(self): # real signature unknown; restored from __doc__
        """ isEnabled(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setEnabled(self, enable): # real signature unknown; restored from __doc__
        """ setEnabled(self, enable: bool) """
        pass

    def sourceBoundingRect(self, system=None): # real signature unknown; restored from __doc__
        """ sourceBoundingRect(self, system: Qt.CoordinateSystem = Qt.LogicalCoordinates) -> QRectF """
        pass

    def sourceChanged(self, flags, QGraphicsEffect_ChangeFlags=None, QGraphicsEffect_ChangeFlag=None): # real signature unknown; restored from __doc__
        """ sourceChanged(self, flags: Union[QGraphicsEffect.ChangeFlags, QGraphicsEffect.ChangeFlag]) """
        pass

    def sourceIsPixmap(self): # real signature unknown; restored from __doc__
        """ sourceIsPixmap(self) -> bool """
        return False

    def sourcePixmap(self, system=None, mode=None): # real signature unknown; restored from __doc__
        """ sourcePixmap(self, system: Qt.CoordinateSystem = Qt.LogicalCoordinates, mode: QGraphicsEffect.PixmapPadMode = QGraphicsEffect.PadToEffectiveBoundingRect) -> (QPixmap, Optional[QPoint]) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def update(self): # real signature unknown; restored from __doc__
        """ update(self) """
        pass

    def updateBoundingRect(self): # real signature unknown; restored from __doc__
        """ updateBoundingRect(self) """
        pass

    def __init__(self, parent, QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    NoPad = 0
    PadToEffectiveBoundingRect = 2
    PadToTransparentBorder = 1
    SourceAttached = 1
    SourceBoundingRectChanged = 4
    SourceDetached = 2
    SourceInvalidated = 8


