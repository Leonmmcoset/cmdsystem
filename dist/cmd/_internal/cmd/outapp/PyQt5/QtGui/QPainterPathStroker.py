# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QPainterPathStroker(__sip.simplewrapper):
    """
    QPainterPathStroker()
    QPainterPathStroker(pen: Union[QPen, Union[QColor, Qt.GlobalColor]])
    """
    def capStyle(self): # real signature unknown; restored from __doc__
        """ capStyle(self) -> Qt.PenCapStyle """
        pass

    def createStroke(self, path): # real signature unknown; restored from __doc__
        """ createStroke(self, path: QPainterPath) -> QPainterPath """
        return QPainterPath

    def curveThreshold(self): # real signature unknown; restored from __doc__
        """ curveThreshold(self) -> float """
        return 0.0

    def dashOffset(self): # real signature unknown; restored from __doc__
        """ dashOffset(self) -> float """
        return 0.0

    def dashPattern(self): # real signature unknown; restored from __doc__
        """ dashPattern(self) -> List[float] """
        return []

    def joinStyle(self): # real signature unknown; restored from __doc__
        """ joinStyle(self) -> Qt.PenJoinStyle """
        pass

    def miterLimit(self): # real signature unknown; restored from __doc__
        """ miterLimit(self) -> float """
        return 0.0

    def setCapStyle(self, style): # real signature unknown; restored from __doc__
        """ setCapStyle(self, style: Qt.PenCapStyle) """
        pass

    def setCurveThreshold(self, threshold): # real signature unknown; restored from __doc__
        """ setCurveThreshold(self, threshold: float) """
        pass

    def setDashOffset(self, offset): # real signature unknown; restored from __doc__
        """ setDashOffset(self, offset: float) """
        pass

    def setDashPattern(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setDashPattern(self, a0: Qt.PenStyle)
        setDashPattern(self, dashPattern: Iterable[float])
        """
        pass

    def setJoinStyle(self, style): # real signature unknown; restored from __doc__
        """ setJoinStyle(self, style: Qt.PenJoinStyle) """
        pass

    def setMiterLimit(self, length): # real signature unknown; restored from __doc__
        """ setMiterLimit(self, length: float) """
        pass

    def setWidth(self, width): # real signature unknown; restored from __doc__
        """ setWidth(self, width: float) """
        pass

    def width(self): # real signature unknown; restored from __doc__
        """ width(self) -> float """
        return 0.0

    def __init__(self, pen=None, QPen=None, Union=None, QColor=None, Qt_GlobalColor=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



