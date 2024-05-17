# encoding: utf-8
# module PyQt5.QtWidgets
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


class QStylePainter(__PyQt5_QtGui.QPainter):
    """
    QStylePainter()
    QStylePainter(w: Optional[QWidget])
    QStylePainter(pd: Optional[QPaintDevice], w: Optional[QWidget])
    """
    def begin(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        begin(self, w: Optional[QWidget]) -> bool
        begin(self, pd: Optional[QPaintDevice], w: Optional[QWidget]) -> bool
        """
        return False

    def drawComplexControl(self, cc, opt): # real signature unknown; restored from __doc__
        """ drawComplexControl(self, cc: QStyle.ComplexControl, opt: QStyleOptionComplex) """
        pass

    def drawControl(self, ce, opt): # real signature unknown; restored from __doc__
        """ drawControl(self, ce: QStyle.ControlElement, opt: QStyleOption) """
        pass

    def drawItemPixmap(self, r, flags, pixmap): # real signature unknown; restored from __doc__
        """ drawItemPixmap(self, r: QRect, flags: int, pixmap: QPixmap) """
        pass

    def drawItemText(self, rect, flags, pal, enabled, text, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ drawItemText(self, rect: QRect, flags: int, pal: QPalette, enabled: bool, text: Optional[str], textRole: QPalette.ColorRole = QPalette.NoRole) """
        pass

    def drawPrimitive(self, pe, opt): # real signature unknown; restored from __doc__
        """ drawPrimitive(self, pe: QStyle.PrimitiveElement, opt: QStyleOption) """
        pass

    def style(self): # real signature unknown; restored from __doc__
        """ style(self) -> Optional[QStyle] """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


