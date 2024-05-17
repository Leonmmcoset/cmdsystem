# encoding: utf-8
# module PyQt5.QtMultimedia
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtMultimedia.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QVideoEncoderSettings(__sip.simplewrapper):
    """
    QVideoEncoderSettings()
    QVideoEncoderSettings(other: QVideoEncoderSettings)
    """
    def bitRate(self): # real signature unknown; restored from __doc__
        """ bitRate(self) -> int """
        return 0

    def codec(self): # real signature unknown; restored from __doc__
        """ codec(self) -> str """
        return ""

    def encodingMode(self): # real signature unknown; restored from __doc__
        """ encodingMode(self) -> QMultimedia.EncodingMode """
        pass

    def encodingOption(self, option, p_str=None): # real signature unknown; restored from __doc__
        """ encodingOption(self, option: Optional[str]) -> Any """
        pass

    def encodingOptions(self): # real signature unknown; restored from __doc__
        """ encodingOptions(self) -> Dict[str, Any] """
        return {}

    def frameRate(self): # real signature unknown; restored from __doc__
        """ frameRate(self) -> float """
        return 0.0

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def quality(self): # real signature unknown; restored from __doc__
        """ quality(self) -> QMultimedia.EncodingQuality """
        pass

    def resolution(self): # real signature unknown; restored from __doc__
        """ resolution(self) -> QSize """
        pass

    def setBitRate(self, bitrate): # real signature unknown; restored from __doc__
        """ setBitRate(self, bitrate: int) """
        pass

    def setCodec(self, a0, p_str=None): # real signature unknown; restored from __doc__
        """ setCodec(self, a0: Optional[str]) """
        pass

    def setEncodingMode(self, a0): # real signature unknown; restored from __doc__
        """ setEncodingMode(self, a0: QMultimedia.EncodingMode) """
        pass

    def setEncodingOption(self, option, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setEncodingOption(self, option: Optional[str], value: Any) """
        pass

    def setEncodingOptions(self, options, p_str=None, Any=None): # real signature unknown; restored from __doc__
        """ setEncodingOptions(self, options: Dict[str, Any]) """
        pass

    def setFrameRate(self, rate): # real signature unknown; restored from __doc__
        """ setFrameRate(self, rate: float) """
        pass

    def setQuality(self, quality): # real signature unknown; restored from __doc__
        """ setQuality(self, quality: QMultimedia.EncodingQuality) """
        pass

    def setResolution(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setResolution(self, a0: QSize)
        setResolution(self, width: int, height: int)
        """
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

    def __init__(self, other=None): # real signature unknown; restored from __doc__ with multiple overloads
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


