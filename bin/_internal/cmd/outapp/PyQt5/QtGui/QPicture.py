# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


from .QPaintDevice import QPaintDevice

class QPicture(QPaintDevice):
    """
    QPicture(formatVersion: int = -1)
    QPicture(a0: QPicture)
    """
    def boundingRect(self): # real signature unknown; restored from __doc__
        """ boundingRect(self) -> QRect """
        pass

    def data(self): # real signature unknown; restored from __doc__
        """ data(self) -> Optional[bytes] """
        pass

    def detach(self): # real signature unknown; restored from __doc__
        """ detach(self) """
        pass

    def devType(self): # real signature unknown; restored from __doc__
        """ devType(self) -> int """
        return 0

    def isDetached(self): # real signature unknown; restored from __doc__
        """ isDetached(self) -> bool """
        return False

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def load(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        load(self, dev: Optional[QIODevice], format: Optional[str] = None) -> bool
        load(self, fileName: Optional[str], format: Optional[str] = None) -> bool
        """
        pass

    def metric(self, m): # real signature unknown; restored from __doc__
        """ metric(self, m: QPaintDevice.PaintDeviceMetric) -> int """
        return 0

    def paintEngine(self): # real signature unknown; restored from __doc__
        """ paintEngine(self) -> Optional[QPaintEngine] """
        pass

    def play(self, p, QPainter=None): # real signature unknown; restored from __doc__
        """ play(self, p: Optional[QPainter]) -> bool """
        return False

    def save(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        save(self, dev: Optional[QIODevice], format: Optional[str] = None) -> bool
        save(self, fileName: Optional[str], format: Optional[str] = None) -> bool
        """
        pass

    def setBoundingRect(self, r): # real signature unknown; restored from __doc__
        """ setBoundingRect(self, r: QRect) """
        pass

    def setData(self, data, PyQt5_sip_array=None, bytes=None): # real signature unknown; restored from __doc__
        """ setData(self, data: Optional[PyQt5.sip.array[bytes]]) """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ size(self) -> int """
        return 0

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: QPicture) """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


