# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QColorTransform(__sip.simplewrapper):
    """
    QColorTransform()
    QColorTransform(colorTransform: QColorTransform)
    """
    def map(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        map(self, argb: int) -> int
        map(self, rgba64: QRgba64) -> QRgba64
        map(self, color: Union[QColor, Qt.GlobalColor]) -> QColor
        """
        return 0 or QRgba64 or QColor

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: QColorTransform) """
        pass

    def __init__(self, colorTransform=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



