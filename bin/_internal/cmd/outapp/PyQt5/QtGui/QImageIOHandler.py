# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QImageIOHandler(__sip.simplewrapper):
    """ QImageIOHandler() """
    def canRead(self): # real signature unknown; restored from __doc__
        """ canRead(self) -> bool """
        return False

    def currentImageNumber(self): # real signature unknown; restored from __doc__
        """ currentImageNumber(self) -> int """
        return 0

    def currentImageRect(self): # real signature unknown; restored from __doc__
        """ currentImageRect(self) -> QRect """
        pass

    def device(self): # real signature unknown; restored from __doc__
        """ device(self) -> Optional[QIODevice] """
        pass

    def format(self): # real signature unknown; restored from __doc__
        """ format(self) -> QByteArray """
        pass

    def imageCount(self): # real signature unknown; restored from __doc__
        """ imageCount(self) -> int """
        return 0

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

    def option(self, option): # real signature unknown; restored from __doc__
        """ option(self, option: QImageIOHandler.ImageOption) -> Any """
        pass

    def read(self, image, QImage=None): # real signature unknown; restored from __doc__
        """ read(self, image: Optional[QImage]) -> bool """
        return False

    def setDevice(self, device, QIODevice=None): # real signature unknown; restored from __doc__
        """ setDevice(self, device: Optional[QIODevice]) """
        pass

    def setFormat(self, format, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ setFormat(self, format: Union[QByteArray, bytes, bytearray]) """
        pass

    def setOption(self, option, value): # real signature unknown; restored from __doc__
        """ setOption(self, option: QImageIOHandler.ImageOption, value: Any) """
        pass

    def supportsOption(self, option): # real signature unknown; restored from __doc__
        """ supportsOption(self, option: QImageIOHandler.ImageOption) -> bool """
        return False

    def write(self, image): # real signature unknown; restored from __doc__
        """ write(self, image: QImage) -> bool """
        return False

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    Animation = 12
    BackgroundColor = 13
    ClipRect = 1
    CompressionRatio = 5
    Description = 2
    Endianness = 11
    Gamma = 6
    ImageTransformation = 18
    IncrementalReading = 10
    Name = 8
    OptimizedWrite = 16
    ProgressiveScanWrite = 17
    Quality = 7
    ScaledClipRect = 3
    ScaledSize = 4
    Size = 0
    SubType = 9
    SupportedSubTypes = 15
    TransformationFlip = 2
    TransformationFlipAndRotate90 = 6
    TransformationMirror = 1
    TransformationMirrorAndRotate90 = 5
    TransformationNone = 0
    TransformationRotate180 = 3
    TransformationRotate270 = 7
    TransformationRotate90 = 4
    TransformedByDefault = 19


