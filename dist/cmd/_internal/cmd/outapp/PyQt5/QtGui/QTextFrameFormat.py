# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


from .QTextFormat import QTextFormat

class QTextFrameFormat(QTextFormat):
    """
    QTextFrameFormat()
    QTextFrameFormat(a0: QTextFrameFormat)
    """
    def border(self): # real signature unknown; restored from __doc__
        """ border(self) -> float """
        return 0.0

    def borderBrush(self): # real signature unknown; restored from __doc__
        """ borderBrush(self) -> QBrush """
        return QBrush

    def borderStyle(self): # real signature unknown; restored from __doc__
        """ borderStyle(self) -> QTextFrameFormat.BorderStyle """
        pass

    def bottomMargin(self): # real signature unknown; restored from __doc__
        """ bottomMargin(self) -> float """
        return 0.0

    def height(self): # real signature unknown; restored from __doc__
        """ height(self) -> QTextLength """
        return QTextLength

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def leftMargin(self): # real signature unknown; restored from __doc__
        """ leftMargin(self) -> float """
        return 0.0

    def margin(self): # real signature unknown; restored from __doc__
        """ margin(self) -> float """
        return 0.0

    def padding(self): # real signature unknown; restored from __doc__
        """ padding(self) -> float """
        return 0.0

    def pageBreakPolicy(self): # real signature unknown; restored from __doc__
        """ pageBreakPolicy(self) -> QTextFormat.PageBreakFlags """
        pass

    def position(self): # real signature unknown; restored from __doc__
        """ position(self) -> QTextFrameFormat.Position """
        pass

    def rightMargin(self): # real signature unknown; restored from __doc__
        """ rightMargin(self) -> float """
        return 0.0

    def setBorder(self, aborder): # real signature unknown; restored from __doc__
        """ setBorder(self, aborder: float) """
        pass

    def setBorderBrush(self, brush, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setBorderBrush(self, brush: Union[QBrush, Union[QColor, Qt.GlobalColor], QGradient]) """
        pass

    def setBorderStyle(self, style): # real signature unknown; restored from __doc__
        """ setBorderStyle(self, style: QTextFrameFormat.BorderStyle) """
        pass

    def setBottomMargin(self, amargin): # real signature unknown; restored from __doc__
        """ setBottomMargin(self, amargin: float) """
        pass

    def setHeight(self, aheight): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setHeight(self, aheight: float)
        setHeight(self, aheight: QTextLength)
        """
        pass

    def setLeftMargin(self, amargin): # real signature unknown; restored from __doc__
        """ setLeftMargin(self, amargin: float) """
        pass

    def setMargin(self, amargin): # real signature unknown; restored from __doc__
        """ setMargin(self, amargin: float) """
        pass

    def setPadding(self, apadding): # real signature unknown; restored from __doc__
        """ setPadding(self, apadding: float) """
        pass

    def setPageBreakPolicy(self, flags, QTextFormat_PageBreakFlags=None, QTextFormat_PageBreakFlag=None): # real signature unknown; restored from __doc__
        """ setPageBreakPolicy(self, flags: Union[QTextFormat.PageBreakFlags, QTextFormat.PageBreakFlag]) """
        pass

    def setPosition(self, f): # real signature unknown; restored from __doc__
        """ setPosition(self, f: QTextFrameFormat.Position) """
        pass

    def setRightMargin(self, amargin): # real signature unknown; restored from __doc__
        """ setRightMargin(self, amargin: float) """
        pass

    def setTopMargin(self, amargin): # real signature unknown; restored from __doc__
        """ setTopMargin(self, amargin: float) """
        pass

    def setWidth(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setWidth(self, length: QTextLength)
        setWidth(self, awidth: float)
        """
        pass

    def topMargin(self): # real signature unknown; restored from __doc__
        """ topMargin(self) -> float """
        return 0.0

    def width(self): # real signature unknown; restored from __doc__
        """ width(self) -> QTextLength """
        return QTextLength

    def __init__(self, a0=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    BorderStyle_Dashed = 2
    BorderStyle_DotDash = 5
    BorderStyle_DotDotDash = 6
    BorderStyle_Dotted = 1
    BorderStyle_Double = 4
    BorderStyle_Groove = 7
    BorderStyle_Inset = 9
    BorderStyle_None = 0
    BorderStyle_Outset = 10
    BorderStyle_Ridge = 8
    BorderStyle_Solid = 3
    FloatLeft = 1
    FloatRight = 2
    InFlow = 0


