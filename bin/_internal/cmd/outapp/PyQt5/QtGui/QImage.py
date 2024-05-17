# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


from .QPaintDevice import QPaintDevice

class QImage(QPaintDevice):
    """
    QImage()
    QImage(size: QSize, format: QImage.Format)
    QImage(width: int, height: int, format: QImage.Format)
    QImage(data: Optional[bytes], width: int, height: int, format: QImage.Format)
    QImage(data: Optional[PyQt5.sip.voidptr], width: int, height: int, format: QImage.Format)
    QImage(data: Optional[bytes], width: int, height: int, bytesPerLine: int, format: QImage.Format)
    QImage(data: Optional[PyQt5.sip.voidptr], width: int, height: int, bytesPerLine: int, format: QImage.Format)
    QImage(xpm: List[str])
    QImage(fileName: Optional[str], format: Optional[str] = None)
    QImage(a0: QImage)
    QImage(variant: Any)
    """
    def allGray(self): # real signature unknown; restored from __doc__
        """ allGray(self) -> bool """
        return False

    def applyColorTransform(self, transform): # real signature unknown; restored from __doc__
        """ applyColorTransform(self, transform: QColorTransform) """
        pass

    def bitPlaneCount(self): # real signature unknown; restored from __doc__
        """ bitPlaneCount(self) -> int """
        return 0

    def bits(self): # real signature unknown; restored from __doc__
        """ bits(self) -> Optional[PyQt5.sip.voidptr] """
        pass

    def byteCount(self): # real signature unknown; restored from __doc__
        """ byteCount(self) -> int """
        return 0

    def bytesPerLine(self): # real signature unknown; restored from __doc__
        """ bytesPerLine(self) -> int """
        return 0

    def cacheKey(self): # real signature unknown; restored from __doc__
        """ cacheKey(self) -> int """
        return 0

    def color(self, i): # real signature unknown; restored from __doc__
        """ color(self, i: int) -> int """
        return 0

    def colorCount(self): # real signature unknown; restored from __doc__
        """ colorCount(self) -> int """
        return 0

    def colorSpace(self): # real signature unknown; restored from __doc__
        """ colorSpace(self) -> QColorSpace """
        return QColorSpace

    def colorTable(self): # real signature unknown; restored from __doc__
        """ colorTable(self) -> List[int] """
        return []

    def constBits(self): # real signature unknown; restored from __doc__
        """ constBits(self) -> Optional[PyQt5.sip.voidptr] """
        pass

    def constScanLine(self, a0): # real signature unknown; restored from __doc__
        """ constScanLine(self, a0: int) -> Optional[PyQt5.sip.voidptr] """
        pass

    def convertedToColorSpace(self, a0): # real signature unknown; restored from __doc__
        """ convertedToColorSpace(self, a0: QColorSpace) -> QImage """
        return QImage

    def convertTo(self, f, flags, Qt_ImageConversionFlags=None, Qt_ImageConversionFlag=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ convertTo(self, f: QImage.Format, flags: Union[Qt.ImageConversionFlags, Qt.ImageConversionFlag] = Qt.ImageConversionFlag.AutoColor) """
        pass

    def convertToColorSpace(self, a0): # real signature unknown; restored from __doc__
        """ convertToColorSpace(self, a0: QColorSpace) """
        pass

    def convertToFormat(self, f, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        convertToFormat(self, f: QImage.Format, flags: Union[Qt.ImageConversionFlags, Qt.ImageConversionFlag] = Qt.ImageConversionFlag.AutoColor) -> QImage
        convertToFormat(self, f: QImage.Format, colorTable: Iterable[int], flags: Union[Qt.ImageConversionFlags, Qt.ImageConversionFlag] = Qt.ImageConversionFlag.AutoColor) -> QImage
        """
        pass

    def copy(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        copy(self, rect: QRect = QRect()) -> QImage
        copy(self, x: int, y: int, w: int, h: int) -> QImage
        """
        return QImage

    def createAlphaMask(self, flags, Qt_ImageConversionFlags=None, Qt_ImageConversionFlag=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ createAlphaMask(self, flags: Union[Qt.ImageConversionFlags, Qt.ImageConversionFlag] = Qt.ImageConversionFlag.AutoColor) -> QImage """
        pass

    def createHeuristicMask(self, clipTight=True): # real signature unknown; restored from __doc__
        """ createHeuristicMask(self, clipTight: bool = True) -> QImage """
        return QImage

    def createMaskFromColor(self, color, mode=None): # real signature unknown; restored from __doc__
        """ createMaskFromColor(self, color: int, mode: Qt.MaskMode = Qt.MaskInColor) -> QImage """
        return QImage

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

    def dotsPerMeterX(self): # real signature unknown; restored from __doc__
        """ dotsPerMeterX(self) -> int """
        return 0

    def dotsPerMeterY(self): # real signature unknown; restored from __doc__
        """ dotsPerMeterY(self) -> int """
        return 0

    def fill(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        fill(self, color: Qt.GlobalColor)
        fill(self, color: Union[QColor, Qt.GlobalColor])
        fill(self, pixel: int)
        """
        pass

    def format(self): # real signature unknown; restored from __doc__
        """ format(self) -> QImage.Format """
        pass

    def fromData(self, data, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        fromData(data: Optional[PyQt5.sip.array[bytes]], format: Optional[str] = None) -> QImage
        fromData(data: Union[QByteArray, bytes, bytearray], format: Optional[str] = None) -> QImage
        """
        pass

    def hasAlphaChannel(self): # real signature unknown; restored from __doc__
        """ hasAlphaChannel(self) -> bool """
        return False

    def height(self): # real signature unknown; restored from __doc__
        """ height(self) -> int """
        return 0

    def invertPixels(self, mode=None): # real signature unknown; restored from __doc__
        """ invertPixels(self, mode: QImage.InvertMode = QImage.InvertRgb) """
        pass

    def isDetached(self): # real signature unknown; restored from __doc__
        """ isDetached(self) -> bool """
        return False

    def isGrayscale(self): # real signature unknown; restored from __doc__
        """ isGrayscale(self) -> bool """
        return False

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def load(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        load(self, device: Optional[QIODevice], format: Optional[str]) -> bool
        load(self, fileName: Optional[str], format: Optional[str] = None) -> bool
        """
        pass

    def loadFromData(self, data, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        loadFromData(self, data: Optional[PyQt5.sip.array[bytes]], format: Optional[str] = None) -> bool
        loadFromData(self, data: Union[QByteArray, bytes, bytearray], format: Optional[str] = None) -> bool
        """
        pass

    def metric(self, metric): # real signature unknown; restored from __doc__
        """ metric(self, metric: QPaintDevice.PaintDeviceMetric) -> int """
        return 0

    def mirrored(self, horizontal=False, vertical=True): # real signature unknown; restored from __doc__
        """ mirrored(self, horizontal: bool = False, vertical: bool = True) -> QImage """
        return QImage

    def offset(self): # real signature unknown; restored from __doc__
        """ offset(self) -> QPoint """
        pass

    def paintEngine(self): # real signature unknown; restored from __doc__
        """ paintEngine(self) -> Optional[QPaintEngine] """
        pass

    def pixel(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        pixel(self, pt: QPoint) -> int
        pixel(self, x: int, y: int) -> int
        """
        return 0

    def pixelColor(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        pixelColor(self, x: int, y: int) -> QColor
        pixelColor(self, pt: QPoint) -> QColor
        """
        return QColor

    def pixelFormat(self): # real signature unknown; restored from __doc__
        """ pixelFormat(self) -> QPixelFormat """
        return QPixelFormat

    def pixelIndex(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        pixelIndex(self, pt: QPoint) -> int
        pixelIndex(self, x: int, y: int) -> int
        """
        return 0

    def rect(self): # real signature unknown; restored from __doc__
        """ rect(self) -> QRect """
        pass

    def reinterpretAsFormat(self, f): # real signature unknown; restored from __doc__
        """ reinterpretAsFormat(self, f: QImage.Format) -> bool """
        return False

    def rgbSwapped(self): # real signature unknown; restored from __doc__
        """ rgbSwapped(self) -> QImage """
        return QImage

    def save(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        save(self, fileName: Optional[str], format: Optional[str] = None, quality: int = -1) -> bool
        save(self, device: Optional[QIODevice], format: Optional[str] = None, quality: int = -1) -> bool
        """
        pass

    def scaled(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        scaled(self, width: int, height: int, aspectRatioMode: Qt.AspectRatioMode = Qt.IgnoreAspectRatio, transformMode: Qt.TransformationMode = Qt.FastTransformation) -> QImage
        scaled(self, size: QSize, aspectRatioMode: Qt.AspectRatioMode = Qt.IgnoreAspectRatio, transformMode: Qt.TransformationMode = Qt.FastTransformation) -> QImage
        """
        return QImage

    def scaledToHeight(self, height, mode=None): # real signature unknown; restored from __doc__
        """ scaledToHeight(self, height: int, mode: Qt.TransformationMode = Qt.FastTransformation) -> QImage """
        return QImage

    def scaledToWidth(self, width, mode=None): # real signature unknown; restored from __doc__
        """ scaledToWidth(self, width: int, mode: Qt.TransformationMode = Qt.FastTransformation) -> QImage """
        return QImage

    def scanLine(self, a0): # real signature unknown; restored from __doc__
        """ scanLine(self, a0: int) -> Optional[PyQt5.sip.voidptr] """
        pass

    def setAlphaChannel(self, alphaChannel): # real signature unknown; restored from __doc__
        """ setAlphaChannel(self, alphaChannel: QImage) """
        pass

    def setColor(self, i, c): # real signature unknown; restored from __doc__
        """ setColor(self, i: int, c: int) """
        pass

    def setColorCount(self, a0): # real signature unknown; restored from __doc__
        """ setColorCount(self, a0: int) """
        pass

    def setColorSpace(self, a0): # real signature unknown; restored from __doc__
        """ setColorSpace(self, a0: QColorSpace) """
        pass

    def setColorTable(self, colors, p_int=None): # real signature unknown; restored from __doc__
        """ setColorTable(self, colors: Iterable[int]) """
        pass

    def setDevicePixelRatio(self, scaleFactor): # real signature unknown; restored from __doc__
        """ setDevicePixelRatio(self, scaleFactor: float) """
        pass

    def setDotsPerMeterX(self, a0): # real signature unknown; restored from __doc__
        """ setDotsPerMeterX(self, a0: int) """
        pass

    def setDotsPerMeterY(self, a0): # real signature unknown; restored from __doc__
        """ setDotsPerMeterY(self, a0: int) """
        pass

    def setOffset(self, a0): # real signature unknown; restored from __doc__
        """ setOffset(self, a0: QPoint) """
        pass

    def setPixel(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setPixel(self, pt: QPoint, index_or_rgb: int)
        setPixel(self, x: int, y: int, index_or_rgb: int)
        """
        pass

    def setPixelColor(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setPixelColor(self, x: int, y: int, c: Union[QColor, Qt.GlobalColor])
        setPixelColor(self, pt: QPoint, c: Union[QColor, Qt.GlobalColor])
        """
        pass

    def setText(self, key, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setText(self, key: Optional[str], value: Optional[str]) """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ size(self) -> QSize """
        pass

    def sizeInBytes(self): # real signature unknown; restored from __doc__
        """ sizeInBytes(self) -> int """
        return 0

    def smoothScaled(self, w, h): # real signature unknown; restored from __doc__
        """ smoothScaled(self, w: int, h: int) -> QImage """
        return QImage

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: QImage) """
        pass

    def text(self, key, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ text(self, key: Optional[str] = '') -> str """
        pass

    def textKeys(self): # real signature unknown; restored from __doc__
        """ textKeys(self) -> List[str] """
        return []

    def toImageFormat(self, format): # real signature unknown; restored from __doc__
        """ toImageFormat(format: QPixelFormat) -> QImage.Format """
        pass

    def toPixelFormat(self, format): # real signature unknown; restored from __doc__
        """ toPixelFormat(format: QImage.Format) -> QPixelFormat """
        return QPixelFormat

    def transformed(self, matrix, mode=None): # real signature unknown; restored from __doc__
        """ transformed(self, matrix: QTransform, mode: Qt.TransformationMode = Qt.FastTransformation) -> QImage """
        return QImage

    def trueMatrix(self, a0, w, h): # real signature unknown; restored from __doc__
        """ trueMatrix(a0: QTransform, w: int, h: int) -> QTransform """
        return QTransform

    def valid(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        valid(self, pt: QPoint) -> bool
        valid(self, x: int, y: int) -> bool
        """
        return False

    def width(self): # real signature unknown; restored from __doc__
        """ width(self) -> int """
        return 0

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

    Format_A2BGR30_Premultiplied = 20
    Format_A2RGB30_Premultiplied = 22
    Format_Alpha8 = 23
    Format_ARGB32 = 5
    Format_ARGB32_Premultiplied = 6
    Format_ARGB4444_Premultiplied = 15
    Format_ARGB6666_Premultiplied = 10
    Format_ARGB8555_Premultiplied = 12
    Format_ARGB8565_Premultiplied = 8
    Format_BGR30 = 19
    Format_BGR888 = 29
    Format_Grayscale16 = 28
    Format_Grayscale8 = 24
    Format_Indexed8 = 3
    Format_Invalid = 0
    Format_Mono = 1
    Format_MonoLSB = 2
    Format_RGB16 = 7
    Format_RGB30 = 21
    Format_RGB32 = 4
    Format_RGB444 = 14
    Format_RGB555 = 11
    Format_RGB666 = 9
    Format_RGB888 = 13
    Format_RGBA64 = 26
    Format_RGBA64_Premultiplied = 27
    Format_RGBA8888 = 17
    Format_RGBA8888_Premultiplied = 18
    Format_RGBX64 = 25
    Format_RGBX8888 = 16
    InvertRgb = 0
    InvertRgba = 1
    __hash__ = None


