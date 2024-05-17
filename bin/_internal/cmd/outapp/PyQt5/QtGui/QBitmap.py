# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


from .QPixmap import QPixmap

class QBitmap(QPixmap):
    """
    QBitmap()
    QBitmap(other: QBitmap)
    QBitmap(a0: QPixmap)
    QBitmap(w: int, h: int)
    QBitmap(a0: QSize)
    QBitmap(fileName: Optional[str], format: Optional[str] = None)
    QBitmap(variant: Any)
    """
    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def fromData(self, size, bits, bytes=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ fromData(size: QSize, bits: Optional[bytes], format: QImage.Format = QImage.Format_MonoLSB) -> QBitmap """
        pass

    def fromImage(self, image, flags, Qt_ImageConversionFlags=None, Qt_ImageConversionFlag=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ fromImage(image: QImage, flags: Union[Qt.ImageConversionFlags, Qt.ImageConversionFlag] = Qt.ImageConversionFlag.AutoColor) -> QBitmap """
        pass

    def metric(self, *args, **kwargs): # real signature unknown
        pass

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: QBitmap) """
        pass

    def transformed(self, matrix): # real signature unknown; restored from __doc__
        """ transformed(self, matrix: QTransform) -> QBitmap """
        return QBitmap

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


