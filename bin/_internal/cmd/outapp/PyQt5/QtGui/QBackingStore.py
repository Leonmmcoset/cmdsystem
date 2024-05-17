# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QBackingStore(__sip.simplewrapper):
    """ QBackingStore(window: Optional[QWindow]) """
    def beginPaint(self, a0): # real signature unknown; restored from __doc__
        """ beginPaint(self, a0: QRegion) """
        pass

    def endPaint(self): # real signature unknown; restored from __doc__
        """ endPaint(self) """
        pass

    def flush(self, region, window, QWindow=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ flush(self, region: QRegion, window: Optional[QWindow] = None, offset: QPoint = QPoint()) """
        pass

    def hasStaticContents(self): # real signature unknown; restored from __doc__
        """ hasStaticContents(self) -> bool """
        return False

    def paintDevice(self): # real signature unknown; restored from __doc__
        """ paintDevice(self) -> Optional[QPaintDevice] """
        pass

    def resize(self, size): # real signature unknown; restored from __doc__
        """ resize(self, size: QSize) """
        pass

    def scroll(self, area, dx, dy): # real signature unknown; restored from __doc__
        """ scroll(self, area: QRegion, dx: int, dy: int) -> bool """
        return False

    def setStaticContents(self, region): # real signature unknown; restored from __doc__
        """ setStaticContents(self, region: QRegion) """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ size(self) -> QSize """
        pass

    def staticContents(self): # real signature unknown; restored from __doc__
        """ staticContents(self) -> QRegion """
        return QRegion

    def window(self): # real signature unknown; restored from __doc__
        """ window(self) -> Optional[QWindow] """
        pass

    def __init__(self, window, QWindow=None): # real signature unknown; restored from __doc__
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



