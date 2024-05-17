# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QImageWriter(__sip.simplewrapper):
    """
    QImageWriter()
    QImageWriter(device: Optional[QIODevice], format: Union[QByteArray, bytes, bytearray])
    QImageWriter(fileName: Optional[str], format: Union[QByteArray, bytes, bytearray] = QByteArray())
    """
    def canWrite(self): # real signature unknown; restored from __doc__
        """ canWrite(self) -> bool """
        return False

    def compression(self): # real signature unknown; restored from __doc__
        """ compression(self) -> int """
        return 0

    def device(self): # real signature unknown; restored from __doc__
        """ device(self) -> Optional[QIODevice] """
        pass

    def error(self): # real signature unknown; restored from __doc__
        """ error(self) -> QImageWriter.ImageWriterError """
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

    def imageFormatsForMimeType(self, mimeType, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ imageFormatsForMimeType(mimeType: Union[QByteArray, bytes, bytearray]) -> List[QByteArray] """
        return []

    def optimizedWrite(self): # real signature unknown; restored from __doc__
        """ optimizedWrite(self) -> bool """
        return False

    def progressiveScanWrite(self): # real signature unknown; restored from __doc__
        """ progressiveScanWrite(self) -> bool """
        return False

    def quality(self): # real signature unknown; restored from __doc__
        """ quality(self) -> int """
        return 0

    def setCompression(self, compression): # real signature unknown; restored from __doc__
        """ setCompression(self, compression: int) """
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

    def setOptimizedWrite(self, optimize): # real signature unknown; restored from __doc__
        """ setOptimizedWrite(self, optimize: bool) """
        pass

    def setProgressiveScanWrite(self, progressive): # real signature unknown; restored from __doc__
        """ setProgressiveScanWrite(self, progressive: bool) """
        pass

    def setQuality(self, quality): # real signature unknown; restored from __doc__
        """ setQuality(self, quality: int) """
        pass

    def setSubType(self, type, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ setSubType(self, type: Union[QByteArray, bytes, bytearray]) """
        pass

    def setText(self, key, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setText(self, key: Optional[str], text: Optional[str]) """
        pass

    def setTransformation(self, orientation, QImageIOHandler_Transformations=None, QImageIOHandler_Transformation=None): # real signature unknown; restored from __doc__
        """ setTransformation(self, orientation: Union[QImageIOHandler.Transformations, QImageIOHandler.Transformation]) """
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

    def supportsOption(self, option): # real signature unknown; restored from __doc__
        """ supportsOption(self, option: QImageIOHandler.ImageOption) -> bool """
        return False

    def transformation(self): # real signature unknown; restored from __doc__
        """ transformation(self) -> QImageIOHandler.Transformations """
        pass

    def write(self, image): # real signature unknown; restored from __doc__
        """ write(self, image: QImage) -> bool """
        return False

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    DeviceError = 1
    InvalidImageError = 3
    UnknownError = 0
    UnsupportedFormatError = 2


