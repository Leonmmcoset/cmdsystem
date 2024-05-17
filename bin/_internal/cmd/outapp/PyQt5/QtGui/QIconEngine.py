# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QIconEngine(__sip.wrapper):
    """
    QIconEngine()
    QIconEngine(other: QIconEngine)
    """
    def actualSize(self, size, mode, state): # real signature unknown; restored from __doc__
        """ actualSize(self, size: QSize, mode: QIcon.Mode, state: QIcon.State) -> QSize """
        pass

    def addFile(self, fileName, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ addFile(self, fileName: Optional[str], size: QSize, mode: QIcon.Mode, state: QIcon.State) """
        pass

    def addPixmap(self, pixmap, mode, state): # real signature unknown; restored from __doc__
        """ addPixmap(self, pixmap: QPixmap, mode: QIcon.Mode, state: QIcon.State) """
        pass

    def availableSizes(self, mode=None, state=None): # real signature unknown; restored from __doc__
        """ availableSizes(self, mode: QIcon.Mode = QIcon.Normal, state: QIcon.State = QIcon.Off) -> List[QSize] """
        return []

    def clone(self): # real signature unknown; restored from __doc__
        """ clone(self) -> Optional[QIconEngine] """
        pass

    def iconName(self): # real signature unknown; restored from __doc__
        """ iconName(self) -> str """
        return ""

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def key(self): # real signature unknown; restored from __doc__
        """ key(self) -> str """
        return ""

    def paint(self, painter, QPainter=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ paint(self, painter: Optional[QPainter], rect: QRect, mode: QIcon.Mode, state: QIcon.State) """
        pass

    def pixmap(self, size, mode, state): # real signature unknown; restored from __doc__
        """ pixmap(self, size: QSize, mode: QIcon.Mode, state: QIcon.State) -> QPixmap """
        return QPixmap

    def read(self, in_): # real signature unknown; restored from __doc__
        """ read(self, in_: QDataStream) -> bool """
        return False

    def scaledPixmap(self, size, mode, state, scale): # real signature unknown; restored from __doc__
        """ scaledPixmap(self, size: QSize, mode: QIcon.Mode, state: QIcon.State, scale: float) -> QPixmap """
        return QPixmap

    def write(self, out): # real signature unknown; restored from __doc__
        """ write(self, out: QDataStream) -> bool """
        return False

    def __init__(self, other=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    AvailableSizesHook = 1
    IconNameHook = 2
    IsNullHook = 3
    ScaledPixmapHook = 4


