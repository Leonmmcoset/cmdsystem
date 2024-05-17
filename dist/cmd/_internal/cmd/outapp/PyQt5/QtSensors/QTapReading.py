# encoding: utf-8
# module PyQt5.QtSensors
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtSensors.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


from .QSensorReading import QSensorReading

class QTapReading(QSensorReading):
    # no doc
    def isDoubleTap(self): # real signature unknown; restored from __doc__
        """ isDoubleTap(self) -> bool """
        return False

    def setDoubleTap(self, doubleTap): # real signature unknown; restored from __doc__
        """ setDoubleTap(self, doubleTap: bool) """
        pass

    def setTapDirection(self, tapDirection): # real signature unknown; restored from __doc__
        """ setTapDirection(self, tapDirection: QTapReading.TapDirection) """
        pass

    def tapDirection(self): # real signature unknown; restored from __doc__
        """ tapDirection(self) -> QTapReading.TapDirection """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    Undefined = 0
    X = 1
    X_Both = 273
    X_Neg = 257
    X_Pos = 17
    Y = 2
    Y_Both = 546
    Y_Neg = 514
    Y_Pos = 34
    Z = 4
    Z_Both = 1092
    Z_Neg = 1028
    Z_Pos = 68


