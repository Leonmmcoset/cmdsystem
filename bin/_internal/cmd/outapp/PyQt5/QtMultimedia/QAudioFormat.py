# encoding: utf-8
# module PyQt5.QtMultimedia
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtMultimedia.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QAudioFormat(__sip.simplewrapper):
    """
    QAudioFormat()
    QAudioFormat(other: QAudioFormat)
    """
    def byteOrder(self): # real signature unknown; restored from __doc__
        """ byteOrder(self) -> QAudioFormat.Endian """
        pass

    def bytesForDuration(self, duration): # real signature unknown; restored from __doc__
        """ bytesForDuration(self, duration: int) -> int """
        return 0

    def bytesForFrames(self, frameCount): # real signature unknown; restored from __doc__
        """ bytesForFrames(self, frameCount: int) -> int """
        return 0

    def bytesPerFrame(self): # real signature unknown; restored from __doc__
        """ bytesPerFrame(self) -> int """
        return 0

    def channelCount(self): # real signature unknown; restored from __doc__
        """ channelCount(self) -> int """
        return 0

    def codec(self): # real signature unknown; restored from __doc__
        """ codec(self) -> str """
        return ""

    def durationForBytes(self, byteCount): # real signature unknown; restored from __doc__
        """ durationForBytes(self, byteCount: int) -> int """
        return 0

    def durationForFrames(self, frameCount): # real signature unknown; restored from __doc__
        """ durationForFrames(self, frameCount: int) -> int """
        return 0

    def framesForBytes(self, byteCount): # real signature unknown; restored from __doc__
        """ framesForBytes(self, byteCount: int) -> int """
        return 0

    def framesForDuration(self, duration): # real signature unknown; restored from __doc__
        """ framesForDuration(self, duration: int) -> int """
        return 0

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def sampleRate(self): # real signature unknown; restored from __doc__
        """ sampleRate(self) -> int """
        return 0

    def sampleSize(self): # real signature unknown; restored from __doc__
        """ sampleSize(self) -> int """
        return 0

    def sampleType(self): # real signature unknown; restored from __doc__
        """ sampleType(self) -> QAudioFormat.SampleType """
        pass

    def setByteOrder(self, byteOrder): # real signature unknown; restored from __doc__
        """ setByteOrder(self, byteOrder: QAudioFormat.Endian) """
        pass

    def setChannelCount(self, channelCount): # real signature unknown; restored from __doc__
        """ setChannelCount(self, channelCount: int) """
        pass

    def setCodec(self, codec, p_str=None): # real signature unknown; restored from __doc__
        """ setCodec(self, codec: Optional[str]) """
        pass

    def setSampleRate(self, sampleRate): # real signature unknown; restored from __doc__
        """ setSampleRate(self, sampleRate: int) """
        pass

    def setSampleSize(self, sampleSize): # real signature unknown; restored from __doc__
        """ setSampleSize(self, sampleSize: int) """
        pass

    def setSampleType(self, sampleType): # real signature unknown; restored from __doc__
        """ setSampleType(self, sampleType: QAudioFormat.SampleType) """
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


    BigEndian = 0
    Float = 3
    LittleEndian = 1
    SignedInt = 1
    Unknown = 0
    UnSignedInt = 2
    __hash__ = None


