# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


from .QPaintDevice import QPaintDevice

class QPixmap(QPaintDevice):
    """
    QPixmap()
    QPixmap(w: int, h: int)
    QPixmap(a0: QSize)
    QPixmap(fileName: Optional[str], format: Optional[str] = None, flags: Union[Qt.ImageConversionFlags, Qt.ImageConversionFlag] = Qt.ImageConversionFlag.AutoColor)
    QPixmap(xpm: List[str])
    QPixmap(a0: QPixmap)
    QPixmap(variant: Any)
    """
    def cacheKey(self): # real signature unknown; restored from __doc__
        """ cacheKey(self) -> int """
        return 0

    def convertFromImage(self, img, flags, Qt_ImageConversionFlags=None, Qt_ImageConversionFlag=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ convertFromImage(self, img: QImage, flags: Union[Qt.ImageConversionFlags, Qt.ImageConversionFlag] = Qt.AutoColor) -> bool """
        pass

    def copy(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        copy(self, rect: QRect = QRect()) -> QPixmap
        copy(self, ax: int, ay: int, awidth: int, aheight: int) -> QPixmap
        """
        return QPixmap

    def createHeuristicMask(self, clipTight=True): # real signature unknown; restored from __doc__
        """ createHeuristicMask(self, clipTight: bool = True) -> QBitmap """
        return QBitmap

    def createMaskFromColor(self, maskColor, QColor=None, Qt_GlobalColor=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ createMaskFromColor(self, maskColor: Union[QColor, Qt.GlobalColor], mode: Qt.MaskMode = Qt.MaskInColor) -> QBitmap """
        pass

    def defaultDepth(self): # real signature unknown; restored from __doc__
        """ defaultDepth() -> int """
        return 0

    def depth(self): # real signature unknown; restored from __doc__
        """ depth(self) -> int """
        return 0

    def detach(self): # real signature unknown; restored from __doc__
        """ detach(self) """
        pass

    def devicePixelRatio(self): # real signature unknown; restored from __doc__
        """ devicePixelRatio(self) -> float """
        return 0.0

    def devType(self): # real signature unknown; restored from __doc__
        """ devType(self) -> int """
        return 0

    def fill(self, color, QColor=None, Qt_GlobalColor=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ fill(self, color: Union[QColor, Qt.GlobalColor] = Qt.GlobalColor.white) """
        pass

    def fromImage(self, image, flags, Qt_ImageConversionFlags=None, Qt_ImageConversionFlag=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ fromImage(image: QImage, flags: Union[Qt.ImageConversionFlags, Qt.ImageConversionFlag] = Qt.AutoColor) -> QPixmap """
        pass

    def fromImageReader(self, imageReader, QImageReader=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ fromImageReader(imageReader: Optional[QImageReader], flags: Union[Qt.ImageConversionFlags, Qt.ImageConversionFlag] = Qt.AutoColor) -> QPixmap """
        pass

    def hasAlpha(self): # real signature unknown; restored from __doc__
        """ hasAlpha(self) -> bool """
        return False

    def hasAlphaChannel(self): # real signature unknown; restored from __doc__
        """ hasAlphaChannel(self) -> bool """
        return False

    def height(self): # real signature unknown; restored from __doc__
        """ height(self) -> int """
        return 0

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def isQBitmap(self): # real signature unknown; restored from __doc__
        """ isQBitmap(self) -> bool """
        return False

    def load(self, fileName, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ load(self, fileName: Optional[str], format: Optional[str] = None, flags: Union[Qt.ImageConversionFlags, Qt.ImageConversionFlag] = Qt.AutoColor) -> bool """
        pass

    def loadFromData(self, buf, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        loadFromData(self, buf: Optional[PyQt5.sip.array[bytes]], format: Optional[str] = None, flags: Union[Qt.ImageConversionFlags, Qt.ImageConversionFlag] = Qt.AutoColor) -> bool
        loadFromData(self, buf: Union[QByteArray, bytes, bytearray], format: Optional[str] = None, flags: Union[Qt.ImageConversionFlags, Qt.ImageConversionFlag] = Qt.AutoColor) -> bool
        """
        pass

    def mask(self): # real signature unknown; restored from __doc__
        """ mask(self) -> QBitmap """
        return QBitmap

    def metric(self, a0): # real signature unknown; restored from __doc__
        """ metric(self, a0: QPaintDevice.PaintDeviceMetric) -> int """
        return 0

    def paintEngine(self): # real signature unknown; restored from __doc__
        """ paintEngine(self) -> Optional[QPaintEngine] """
        pass

    def rect(self): # real signature unknown; restored from __doc__
        """ rect(self) -> QRect """
        pass

    def save(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        save(self, fileName: Optional[str], format: Optional[str] = None, quality: int = -1) -> bool
        save(self, device: Optional[QIODevice], format: Optional[str] = None, quality: int = -1) -> bool
        """
        pass

    def scaled(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        scaled(self, width: int, height: int, aspectRatioMode: Qt.AspectRatioMode = Qt.IgnoreAspectRatio, transformMode: Qt.TransformationMode = Qt.FastTransformation) -> QPixmap
        scaled(self, size: QSize, aspectRatioMode: Qt.AspectRatioMode = Qt.IgnoreAspectRatio, transformMode: Qt.TransformationMode = Qt.FastTransformation) -> QPixmap
        """
        return QPixmap

    def scaledToHeight(self, height, mode=None): # real signature unknown; restored from __doc__
        """ scaledToHeight(self, height: int, mode: Qt.TransformationMode = Qt.FastTransformation) -> QPixmap """
        return QPixmap

    def scaledToWidth(self, width, mode=None): # real signature unknown; restored from __doc__
        """ scaledToWidth(self, width: int, mode: Qt.TransformationMode = Qt.FastTransformation) -> QPixmap """
        return QPixmap

    def scroll(self, dx, dy, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        scroll(self, dx: int, dy: int, rect: QRect) -> Optional[QRegion]
        scroll(self, dx: int, dy: int, x: int, y: int, width: int, height: int) -> Optional[QRegion]
        """
        pass

    def setDevicePixelRatio(self, scaleFactor): # real signature unknown; restored from __doc__
        """ setDevicePixelRatio(self, scaleFactor: float) """
        pass

    def setMask(self, a0): # real signature unknown; restored from __doc__
        """ setMask(self, a0: QBitmap) """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ size(self) -> QSize """
        pass

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: QPixmap) """
        pass

    def toImage(self): # real signature unknown; restored from __doc__
        """ toImage(self) -> QImage """
        return QImage

    def transformed(self, transform, mode=None): # real signature unknown; restored from __doc__
        """ transformed(self, transform: QTransform, mode: Qt.TransformationMode = Qt.FastTransformation) -> QPixmap """
        return QPixmap

    def trueMatrix(self, m, w, h): # real signature unknown; restored from __doc__
        """ trueMatrix(m: QTransform, w: int, h: int) -> QTransform """
        return QTransform

    def width(self): # real signature unknown; restored from __doc__
        """ width(self) -> int """
        return 0

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


