# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QImageReader(__sip.simplewrapper):
    """
    QImageReader()
    QImageReader(device: Optional[QIODevice], format: Union[QByteArray, bytes, bytearray] = QByteArray())
    QImageReader(fileName: Optional[str], format: Union[QByteArray, bytes, bytearray] = QByteArray())
    """
    def autoDetectImageFormat(self): # real signature unknown; restored from __doc__
        """ autoDetectImageFormat(self) -> bool """
        return False

    def autoTransform(self): # real signature unknown; restored from __doc__
        """ autoTransform(self) -> bool """
        return False

    def backgroundColor(self): # real signature unknown; restored from __doc__
        """ backgroundColor(self) -> QColor """
        return QColor

    def canRead(self): # real signature unknown; restored from __doc__
        """ canRead(self) -> bool """
        return False

    def clipRect(self): # real signature unknown; restored from __doc__
        """ clipRect(self) -> QRect """
        pass

    def currentImageNumber(self): # real signature unknown; restored from __doc__
        """ currentImageNumber(self) -> int """
        return 0

    def currentImageRect(self): # real signature unknown; restored from __doc__
        """ currentImageRect(self) -> QRect """
        pass

    def decideFormatFromContent(self): # real signature unknown; restored from __doc__
        """ decideFormatFromContent(self) -> bool """
        return False

    def device(self): # real signature unknown; restored from __doc__
        """ device(self) -> Optional[QIODevice] """
        pass

    def error(self): # real signature unknown; restored from __doc__
        """ error(self) -> QImageReader.ImageReaderError """
        pass

    def errorString(self): # real signature unknown; restored from __doc__
        """ errorString(self) -> str """
        return ""

    def fileName(self): # real signature unknown; restored from __doc__
        """ fileName(self) -> str """
        return ""

    def format(self): # real signature unknown; restored from __doc__
        """ format(self) -> QByteArray """
        pass

    def gamma(self): # real signature unknown; restored from __doc__
        """ gamma(self) -> float """
        return 0.0

    def imageCount(self): # real signature unknown; restored from __doc__
        """ imageCount(self) -> int """
        return 0

    def imageFormat(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        imageFormat(fileName: Optional[str]) -> QByteArray
        imageFormat(device: Optional[QIODevice]) -> QByteArray
        imageFormat(self) -> QImage.Format
        """
        pass

    def imageFormatsForMimeType(self, mimeType, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ imageFormatsForMimeType(mimeType: Union[QByteArray, bytes, bytearray]) -> List[QByteArray] """
        return []

    def jumpToImage(self, imageNumber): # real signature unknown; restored from __doc__
        """ jumpToImage(self, imageNumber: int) -> bool """
        return False

    def jumpToNextImage(self): # real signature unknown; restored from __doc__
        """ jumpToNextImage(self) -> bool """
        return False

    def loopCount(self): # real signature unknown; restored from __doc__
        """ loopCount(self) -> int """
        return 0

    def nextImageDelay(self): # real signature unknown; restored from __doc__
        """ nextImageDelay(self) -> int """
        return 0

    def quality(self): # real signature unknown; restored from __doc__
        """ quality(self) -> int """
        return 0

    def read(self, image=None, QImage=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        read(self) -> QImage
        read(self, image: Optional[QImage]) -> bool
        """
        return QImage or False

    def scaledClipRect(self): # real signature unknown; restored from __doc__
        """ scaledClipRect(self) -> QRect """
        pass

    def scaledSize(self): # real signature unknown; restored from __doc__
        """ scaledSize(self) -> QSize """
        pass

    def setAutoDetectImageFormat(self, enabled): # real signature unknown; restored from __doc__
        """ setAutoDetectImageFormat(self, enabled: bool) """
        pass

    def setAutoTransform(self, enabled): # real signature unknown; restored from __doc__
        """ setAutoTransform(self, enabled: bool) """
        pass

    def setBackgroundColor(self, color, QColor=None, Qt_GlobalColor=None): # real signature unknown; restored from __doc__
        """ setBackgroundColor(self, color: Union[QColor, Qt.GlobalColor]) """
        pass

    def setClipRect(self, rect): # real signature unknown; restored from __doc__
        """ setClipRect(self, rect: QRect) """
        pass

    def setDecideFormatFromContent(self, ignored): # real signature unknown; restored from __doc__
        """ setDecideFormatFromContent(self, ignored: bool) """
        pass

    def setDevice(self, device, QIODevice=None): # real signature unknown; restored from __doc__
        """ setDevice(self, device: Optional[QIODevice]) """
        pass

    def setFileName(self, fileName, p_str=None): # real signature unknown; restored from __doc__
        """ setFileName(self, fileName: Optional[str]) """
        pass

    def setFormat(self, format, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ setFormat(self, format: Union[QByteArray, bytes, bytearray]) """
        pass

    def setGamma(self, gamma): # real signature unknown; restored from __doc__
        """ setGamma(self, gamma: float) """
        pass

    def setQuality(self, quality): # real signature unknown; restored from __doc__
        """ setQuality(self, quality: int) """
        pass

    def setScaledClipRect(self, rect): # real signature unknown; restored from __doc__
        """ setScaledClipRect(self, rect: QRect) """
        pass

    def setScaledSize(self, size): # real signature unknown; restored from __doc__
        """ setScaledSize(self, size: QSize) """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ size(self) -> QSize """
        pass

    def subType(self): # real signature unknown; restored from __doc__
        """ subType(self) -> QByteArray """
        pass

    def supportedImageFormats(self): # real signature unknown; restored from __doc__
        """ supportedImageFormats() -> List[QByteArray] """
        return []

    def supportedMimeTypes(self): # real signature unknown; restored from __doc__
        """ supportedMimeTypes() -> List[QByteArray] """
        return []

    def supportedSubTypes(self): # real signature unknown; restored from __doc__
        """ supportedSubTypes(self) -> List[QByteArray] """
        return []

    def supportsAnimation(self): # real signature unknown; restored from __doc__
        """ supportsAnimation(self) -> bool """
        return False

    def supportsOption(self, option): # real signature unknown; restored from __doc__
        """ supportsOption(self, option: QImageIOHandler.ImageOption) -> bool """
        return False

    def text(self, key, p_str=None): # real signature unknown; restored from __doc__
        """ text(self, key: Optional[str]) -> str """
        return ""

    def textKeys(self): # real signature unknown; restored from __doc__
        """ textKeys(self) -> List[str] """
        return []

    def transformation(self): # real signature unknown; restored from __doc__
        """ transformation(self) -> QImageIOHandler.Transformations """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    DeviceError = 2
    FileNotFoundError = 1
    InvalidDataError = 4
    UnknownError = 0
    UnsupportedFormatError = 3


