# encoding: utf-8
# module PyQt5.QtWidgets
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


from .QCommonStyle import QCommonStyle

class QProxyStyle(QCommonStyle):
    """
    QProxyStyle(style: Optional[QStyle] = None)
    QProxyStyle(key: Optional[str])
    """
    def baseStyle(self): # real signature unknown; restored from __doc__
        """ baseStyle(self) -> Optional[QStyle] """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def drawComplexControl(self, control, option, QStyleOptionComplex=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ drawComplexControl(self, control: QStyle.ComplexControl, option: Optional[QStyleOptionComplex], painter: Optional[QPainter], widget: Optional[QWidget] = None) """
        pass

    def drawControl(self, element, option, QStyleOption=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ drawControl(self, element: QStyle.ControlElement, option: Optional[QStyleOption], painter: Optional[QPainter], widget: Optional[QWidget] = None) """
        pass

    def drawItemPixmap(self, painter, QPainter=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ drawItemPixmap(self, painter: Optional[QPainter], rect: QRect, alignment: int, pixmap: QPixmap) """
        pass

    def drawItemText(self, painter, QPainter=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ drawItemText(self, painter: Optional[QPainter], rect: QRect, flags: int, pal: QPalette, enabled: bool, text: Optional[str], textRole: QPalette.ColorRole = QPalette.NoRole) """
        pass

    def drawPrimitive(self, element, option, QStyleOption=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ drawPrimitive(self, element: QStyle.PrimitiveElement, option: Optional[QStyleOption], painter: Optional[QPainter], widget: Optional[QWidget] = None) """
        pass

    def event(self, e, QEvent=None): # real signature unknown; restored from __doc__
        """ event(self, e: Optional[QEvent]) -> bool """
        return False

    def generatedIconPixmap(self, iconMode, pixmap, opt, QStyleOption=None): # real signature unknown; restored from __doc__
        """ generatedIconPixmap(self, iconMode: QIcon.Mode, pixmap: QPixmap, opt: Optional[QStyleOption]) -> QPixmap """
        pass

    def hitTestComplexControl(self, control, option, QStyleOptionComplex=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ hitTestComplexControl(self, control: QStyle.ComplexControl, option: Optional[QStyleOptionComplex], pos: QPoint, widget: Optional[QWidget] = None) -> QStyle.SubControl """
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def itemPixmapRect(self, r, flags, pixmap): # real signature unknown; restored from __doc__
        """ itemPixmapRect(self, r: QRect, flags: int, pixmap: QPixmap) -> QRect """
        pass

    def itemTextRect(self, fm, r, flags, enabled, text, p_str=None): # real signature unknown; restored from __doc__
        """ itemTextRect(self, fm: QFontMetrics, r: QRect, flags: int, enabled: bool, text: Optional[str]) -> QRect """
        pass

    def layoutSpacing(self, control1, control2, orientation, option, QStyleOption=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ layoutSpacing(self, control1: QSizePolicy.ControlType, control2: QSizePolicy.ControlType, orientation: Qt.Orientation, option: Optional[QStyleOption] = None, widget: Optional[QWidget] = None) -> int """
        pass

    def pixelMetric(self, metric, option, QStyleOption=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ pixelMetric(self, metric: QStyle.PixelMetric, option: Optional[QStyleOption] = None, widget: Optional[QWidget] = None) -> int """
        pass

    def polish(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        polish(self, widget: Optional[QWidget])
        polish(self, pal: QPalette) -> QPalette
        polish(self, app: Optional[QApplication])
        """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setBaseStyle(self, style, QStyle=None): # real signature unknown; restored from __doc__
        """ setBaseStyle(self, style: Optional[QStyle]) """
        pass

    def sizeFromContents(self, type, option, QStyleOption=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ sizeFromContents(self, type: QStyle.ContentsType, option: Optional[QStyleOption], size: QSize, widget: Optional[QWidget]) -> QSize """
        pass

    def standardIcon(self, standardIcon, option, QStyleOption=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ standardIcon(self, standardIcon: QStyle.StandardPixmap, option: Optional[QStyleOption] = None, widget: Optional[QWidget] = None) -> QIcon """
        pass

    def standardPalette(self): # real signature unknown; restored from __doc__
        """ standardPalette(self) -> QPalette """
        pass

    def standardPixmap(self, standardPixmap, opt, QStyleOption=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ standardPixmap(self, standardPixmap: QStyle.StandardPixmap, opt: Optional[QStyleOption], widget: Optional[QWidget] = None) -> QPixmap """
        pass

    def styleHint(self, hint, option, QStyleOption=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ styleHint(self, hint: QStyle.StyleHint, option: Optional[QStyleOption] = None, widget: Optional[QWidget] = None, returnData: Optional[QStyleHintReturn] = None) -> int """
        pass

    def subControlRect(self, cc, opt, QStyleOptionComplex=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ subControlRect(self, cc: QStyle.ComplexControl, opt: Optional[QStyleOptionComplex], sc: QStyle.SubControl, widget: Optional[QWidget]) -> QRect """
        pass

    def subElementRect(self, element, option, QStyleOption=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ subElementRect(self, element: QStyle.SubElement, option: Optional[QStyleOption], widget: Optional[QWidget]) -> QRect """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def unpolish(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        unpolish(self, widget: Optional[QWidget])
        unpolish(self, app: Optional[QApplication])
        """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


