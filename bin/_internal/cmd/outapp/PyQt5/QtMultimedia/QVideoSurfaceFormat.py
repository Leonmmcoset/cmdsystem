# encoding: utf-8
# module PyQt5.QtMultimedia
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtMultimedia.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QVideoSurfaceFormat(__sip.simplewrapper):
    """
    QVideoSurfaceFormat()
    QVideoSurfaceFormat(size: QSize, format: QVideoFrame.PixelFormat, type: QAbstractVideoBuffer.HandleType = QAbstractVideoBuffer.NoHandle)
    QVideoSurfaceFormat(format: QVideoSurfaceFormat)
    """
    def frameHeight(self): # real signature unknown; restored from __doc__
        """ frameHeight(self) -> int """
        return 0

    def frameRate(self): # real signature unknown; restored from __doc__
        """ frameRate(self) -> float """
        return 0.0

    def frameSize(self): # real signature unknown; restored from __doc__
        """ frameSize(self) -> QSize """
        pass

    def frameWidth(self): # real signature unknown; restored from __doc__
        """ frameWidth(self) -> int """
        return 0

    def handleType(self): # real signature unknown; restored from __doc__
        """ handleType(self) -> QAbstractVideoBuffer.HandleType """
        pass

    def isMirrored(self): # real signature unknown; restored from __doc__
        """ isMirrored(self) -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def pixelAspectRatio(self): # real signature unknown; restored from __doc__
        """ pixelAspectRatio(self) -> QSize """
        pass

    def pixelFormat(self): # real signature unknown; restored from __doc__
        """ pixelFormat(self) -> QVideoFrame.PixelFormat """
        pass

    def property(self, name, p_str=None): # real signature unknown; restored from __doc__
        """ property(self, name: Optional[str]) -> Any """
        pass

    def propertyNames(self): # real signature unknown; restored from __doc__
        """ propertyNames(self) -> List[QByteArray] """
        return []

    def scanLineDirection(self): # real signature unknown; restored from __doc__
        """ scanLineDirection(self) -> QVideoSurfaceFormat.Direction """
        pass

    def setFrameRate(self, rate): # real signature unknown; restored from __doc__
        """ setFrameRate(self, rate: float) """
        pass

    def setFrameSize(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setFrameSize(self, size: QSize)
        setFrameSize(self, width: int, height: int)
        """
        pass

    def setMirrored(self, mirrored): # real signature unknown; restored from __doc__
        """ setMirrored(self, mirrored: bool) """
        pass

    def setPixelAspectRatio(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setPixelAspectRatio(self, ratio: QSize)
        setPixelAspectRatio(self, width: int, height: int)
        """
        pass

    def setProperty(self, name, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setProperty(self, name: Optional[str], value: Any) """
        pass

    def setScanLineDirection(self, direction): # real signature unknown; restored from __doc__
        """ setScanLineDirection(self, direction: QVideoSurfaceFormat.Direction) """
        pass

    def setViewport(self, viewport): # real signature unknown; restored from __doc__
        """ setViewport(self, viewport: QRect) """
        pass

    def setYCbCrColorSpace(self, colorSpace): # real signature unknown; restored from __doc__
        """ setYCbCrColorSpace(self, colorSpace: QVideoSurfaceFormat.YCbCrColorSpace) """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> QSize """
        pass

    def viewport(self): # real signature unknown; restored from __doc__
        """ viewport(self) -> QRect """
        pass

    def yCbCrColorSpace(self): # real signature unknown; restored from __doc__
        """ yCbCrColorSpace(self) -> QVideoSurfaceFormat.YCbCrColorSpace """
        pass

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


    BottomToTop = 1
    TopToBottom = 0
    YCbCr_BT601 = 1
    YCbCr_BT709 = 2
    YCbCr_JPEG = 5
    YCbCr_Undefined = 0
    YCbCr_xvYCC601 = 3
    YCbCr_xvYCC709 = 4
    __hash__ = None


