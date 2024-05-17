# encoding: utf-8
# module PyQt5.QtMultimedia
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtMultimedia.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QVideoFrame(__sip.simplewrapper):
    """
    QVideoFrame()
    QVideoFrame(buffer: Optional[QAbstractVideoBuffer], size: QSize, format: QVideoFrame.PixelFormat)
    QVideoFrame(bytes: int, size: QSize, bytesPerLine: int, format: QVideoFrame.PixelFormat)
    QVideoFrame(image: QImage)
    QVideoFrame(other: QVideoFrame)
    """
    def availableMetaData(self): # real signature unknown; restored from __doc__
        """ availableMetaData(self) -> Dict[str, Any] """
        return {}

    def bits(self, plane=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        bits(self) -> PyQt5.sip.voidptr
        bits(self, plane: int) -> Optional[PyQt5.sip.voidptr]
        """
        pass

    def buffer(self): # real signature unknown; restored from __doc__
        """ buffer(self) -> Optional[QAbstractVideoBuffer] """
        pass

    def bytesPerLine(self, plane=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        bytesPerLine(self) -> int
        bytesPerLine(self, plane: int) -> int
        """
        return 0

    def endTime(self): # real signature unknown; restored from __doc__
        """ endTime(self) -> int """
        return 0

    def fieldType(self): # real signature unknown; restored from __doc__
        """ fieldType(self) -> QVideoFrame.FieldType """
        pass

    def handle(self): # real signature unknown; restored from __doc__
        """ handle(self) -> Any """
        pass

    def handleType(self): # real signature unknown; restored from __doc__
        """ handleType(self) -> QAbstractVideoBuffer.HandleType """
        pass

    def height(self): # real signature unknown; restored from __doc__
        """ height(self) -> int """
        return 0

    def image(self): # real signature unknown; restored from __doc__
        """ image(self) -> QImage """
        pass

    def imageFormatFromPixelFormat(self, format): # real signature unknown; restored from __doc__
        """ imageFormatFromPixelFormat(format: QVideoFrame.PixelFormat) -> QImage.Format """
        pass

    def isMapped(self): # real signature unknown; restored from __doc__
        """ isMapped(self) -> bool """
        return False

    def isReadable(self): # real signature unknown; restored from __doc__
        """ isReadable(self) -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def isWritable(self): # real signature unknown; restored from __doc__
        """ isWritable(self) -> bool """
        return False

    def map(self, mode): # real signature unknown; restored from __doc__
        """ map(self, mode: QAbstractVideoBuffer.MapMode) -> bool """
        return False

    def mapMode(self): # real signature unknown; restored from __doc__
        """ mapMode(self) -> QAbstractVideoBuffer.MapMode """
        pass

    def mappedBytes(self): # real signature unknown; restored from __doc__
        """ mappedBytes(self) -> int """
        return 0

    def metaData(self, key, p_str=None): # real signature unknown; restored from __doc__
        """ metaData(self, key: Optional[str]) -> Any """
        pass

    def pixelFormat(self): # real signature unknown; restored from __doc__
        """ pixelFormat(self) -> QVideoFrame.PixelFormat """
        pass

    def pixelFormatFromImageFormat(self, format): # real signature unknown; restored from __doc__
        """ pixelFormatFromImageFormat(format: QImage.Format) -> QVideoFrame.PixelFormat """
        pass

    def planeCount(self): # real signature unknown; restored from __doc__
        """ planeCount(self) -> int """
        return 0

    def setEndTime(self, time): # real signature unknown; restored from __doc__
        """ setEndTime(self, time: int) """
        pass

    def setFieldType(self, a0): # real signature unknown; restored from __doc__
        """ setFieldType(self, a0: QVideoFrame.FieldType) """
        pass

    def setMetaData(self, key, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setMetaData(self, key: Optional[str], value: Any) """
        pass

    def setStartTime(self, time): # real signature unknown; restored from __doc__
        """ setStartTime(self, time: int) """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ size(self) -> QSize """
        pass

    def startTime(self): # real signature unknown; restored from __doc__
        """ startTime(self) -> int """
        return 0

    def unmap(self): # real signature unknown; restored from __doc__
        """ unmap(self) """
        pass

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

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    BottomField = 2
    Format_ABGR32 = 33
    Format_AdobeDng = 32
    Format_ARGB32 = 1
    Format_ARGB32_Premultiplied = 2
    Format_ARGB8565_Premultiplied = 7
    Format_AYUV444 = 15
    Format_AYUV444_Premultiplied = 16
    Format_BGR24 = 11
    Format_BGR32 = 10
    Format_BGR555 = 13
    Format_BGR565 = 12
    Format_BGRA32 = 8
    Format_BGRA32_Premultiplied = 9
    Format_BGRA5658_Premultiplied = 14
    Format_CameraRaw = 31
    Format_IMC1 = 24
    Format_IMC2 = 25
    Format_IMC3 = 26
    Format_IMC4 = 27
    Format_Invalid = 0
    Format_Jpeg = 30
    Format_NV12 = 22
    Format_NV21 = 23
    Format_RGB24 = 4
    Format_RGB32 = 3
    Format_RGB555 = 6
    Format_RGB565 = 5
    Format_User = 1000
    Format_UYVY = 20
    Format_Y16 = 29
    Format_Y8 = 28
    Format_YUV420P = 18
    Format_YUV422P = 34
    Format_YUV444 = 17
    Format_YUYV = 21
    Format_YV12 = 19
    InterlacedFrame = 3
    ProgressiveFrame = 0
    TopField = 1
    __hash__ = None


