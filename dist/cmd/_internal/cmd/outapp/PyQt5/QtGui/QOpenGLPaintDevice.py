# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


from .QPaintDevice import QPaintDevice

class QOpenGLPaintDevice(QPaintDevice):
    """
    QOpenGLPaintDevice()
    QOpenGLPaintDevice(size: QSize)
    QOpenGLPaintDevice(width: int, height: int)
    """
    def context(self): # real signature unknown; restored from __doc__
        """ context(self) -> Optional[QOpenGLContext] """
        pass

    def dotsPerMeterX(self): # real signature unknown; restored from __doc__
        """ dotsPerMeterX(self) -> float """
        return 0.0

    def dotsPerMeterY(self): # real signature unknown; restored from __doc__
        """ dotsPerMeterY(self) -> float """
        return 0.0

    def ensureActiveTarget(self): # real signature unknown; restored from __doc__
        """ ensureActiveTarget(self) """
        pass

    def metric(self, metric): # real signature unknown; restored from __doc__
        """ metric(self, metric: QPaintDevice.PaintDeviceMetric) -> int """
        return 0

    def paintEngine(self): # real signature unknown; restored from __doc__
        """ paintEngine(self) -> Optional[QPaintEngine] """
        pass

    def paintFlipped(self): # real signature unknown; restored from __doc__
        """ paintFlipped(self) -> bool """
        return False

    def setDevicePixelRatio(self, devicePixelRatio): # real signature unknown; restored from __doc__
        """ setDevicePixelRatio(self, devicePixelRatio: float) """
        pass

    def setDotsPerMeterX(self, a0): # real signature unknown; restored from __doc__
        """ setDotsPerMeterX(self, a0: float) """
        pass

    def setDotsPerMeterY(self, a0): # real signature unknown; restored from __doc__
        """ setDotsPerMeterY(self, a0: float) """
        pass

    def setPaintFlipped(self, flipped): # real signature unknown; restored from __doc__
        """ setPaintFlipped(self, flipped: bool) """
        pass

    def setSize(self, size): # real signature unknown; restored from __doc__
        """ setSize(self, size: QSize) """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ size(self) -> QSize """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


