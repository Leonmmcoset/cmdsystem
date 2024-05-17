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

class QGraphicsColorizeEffect(QGraphicsEffect):
    """ QGraphicsColorizeEffect(parent: Optional[QObject] = None) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def color(self): # real signature unknown; restored from __doc__
        """ color(self) -> QColor """
        pass

    def colorChanged(self, *args, **kwargs): # real signature unknown
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

    def setColor(self, c, QColor=None, Qt_GlobalColor=None): # real signature unknown; restored from __doc__
        """ setColor(self, c: Union[QColor, Qt.GlobalColor]) """
        pass

    def setStrength(self, strength): # real signature unknown; restored from __doc__
        """ setStrength(self, strength: float) """
        pass

    def sourceBoundingRect(self, *args, **kwargs): # real signature unknown
        pass

    def sourceChanged(self, *args, **kwargs): # real signature unknown
        pass

    def sourceIsPixmap(self, *args, **kwargs): # real signature unknown
        pass

    def sourcePixmap(self, *args, **kwargs): # real signature unknown
        pass

    def strength(self): # real signature unknown; restored from __doc__
        """ strength(self) -> float """
        return 0.0

    def strengthChanged(self, *args, **kwargs): # real signature unknown
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

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def updateBoundingRect(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent, QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass


