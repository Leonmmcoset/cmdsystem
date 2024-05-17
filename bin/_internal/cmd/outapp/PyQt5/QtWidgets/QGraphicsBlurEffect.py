# encoding: utf-8
# module PyQt5.QtWidgets
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


from .QGraphicsEffect import QGraphicsEffect

class QGraphicsBlurEffect(QGraphicsEffect):
    """ QGraphicsBlurEffect(parent: Optional[QObject] = None) """
    def blurHints(self): # real signature unknown; restored from __doc__
        """ blurHints(self) -> QGraphicsBlurEffect.BlurHints """
        pass

    def blurHintsChanged(self, *args, **kwargs): # real signature unknown
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

    def blurRadius(self): # real signature unknown; restored from __doc__
        """ blurRadius(self) -> float """
        return 0.0

    def blurRadiusChanged(self, *args, **kwargs): # real signature unknown
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

    def boundingRectFor(self, rect): # real signature unknown; restored from __doc__
        """ boundingRectFor(self, rect: QRectF) -> QRectF """
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

    def drawSource(self, *args, **kwargs): # real signature unknown
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setBlurHints(self, hints, QGraphicsBlurEffect_BlurHints=None, QGraphicsBlurEffect_BlurHint=None): # real signature unknown; restored from __doc__
        """ setBlurHints(self, hints: Union[QGraphicsBlurEffect.BlurHints, QGraphicsBlurEffect.BlurHint]) """
        pass

    def setBlurRadius(self, blurRadius): # real signature unknown; restored from __doc__
        """ setBlurRadius(self, blurRadius: float) """
        pass

    def sourceBoundingRect(self, *args, **kwargs): # real signature unknown
        pass

    def sourceChanged(self, *args, **kwargs): # real signature unknown
        pass

    def sourceIsPixmap(self, *args, **kwargs): # real signature unknown
        pass

    def sourcePixmap(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def updateBoundingRect(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent, QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    AnimationHint = 2
    PerformanceHint = 0
    QualityHint = 1


