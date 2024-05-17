# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QBrush(__sip.simplewrapper):
    """
    QBrush()
    QBrush(bs: Qt.BrushStyle)
    QBrush(color: Union[QColor, Qt.GlobalColor], style: Qt.BrushStyle = Qt.SolidPattern)
    QBrush(color: Union[QColor, Qt.GlobalColor], pixmap: QPixmap)
    QBrush(pixmap: QPixmap)
    QBrush(image: QImage)
    QBrush(brush: Union[QBrush, Union[QColor, Qt.GlobalColor], QGradient])
    QBrush(variant: Any)
    """
    def color(self): # real signature unknown; restored from __doc__
        """ color(self) -> QColor """
        return QColor

    def gradient(self): # real signature unknown; restored from __doc__
        """ gradient(self) -> Optional[QGradient] """
        pass

    def isOpaque(self): # real signature unknown; restored from __doc__
        """ isOpaque(self) -> bool """
        return False

    def setColor(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setColor(self, color: Union[QColor, Qt.GlobalColor])
        setColor(self, acolor: Qt.GlobalColor)
        """
        pass

    def setStyle(self, a0): # real signature unknown; restored from __doc__
        """ setStyle(self, a0: Qt.BrushStyle) """
        pass

    def setTexture(self, pixmap): # real signature unknown; restored from __doc__
        """ setTexture(self, pixmap: QPixmap) """
        pass

    def setTextureImage(self, image): # real signature unknown; restored from __doc__
        """ setTextureImage(self, image: QImage) """
        pass

    def setTransform(self, a0): # real signature unknown; restored from __doc__
        """ setTransform(self, a0: QTransform) """
        pass

    def style(self): # real signature unknown; restored from __doc__
        """ style(self) -> Qt.BrushStyle """
        pass

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: QBrush) """
        pass

    def texture(self): # real signature unknown; restored from __doc__
        """ texture(self) -> QPixmap """
        return QPixmap

    def textureImage(self): # real signature unknown; restored from __doc__
        """ textureImage(self) -> QImage """
        return QImage

    def transform(self): # real signature unknown; restored from __doc__
        """ transform(self) -> QTransform """
        return QTransform

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __hash__ = None


