# encoding: utf-8
# module PyQt5.QtMultimedia
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtMultimedia.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


from .QMediaControl import QMediaControl

class QVideoEncoderSettingsControl(QMediaControl):
    """ QVideoEncoderSettingsControl(parent: Optional[QObject] = None) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setVideoSettings(self, settings): # real signature unknown; restored from __doc__
        """ setVideoSettings(self, settings: QVideoEncoderSettings) """
        pass

    def supportedFrameRates(self, settings): # real signature unknown; restored from __doc__
        """ supportedFrameRates(self, settings: QVideoEncoderSettings) -> (List[float], Optional[bool]) """
        pass

    def supportedResolutions(self, settings): # real signature unknown; restored from __doc__
        """ supportedResolutions(self, settings: QVideoEncoderSettings) -> (List[QSize], Optional[bool]) """
        pass

    def supportedVideoCodecs(self): # real signature unknown; restored from __doc__
        """ supportedVideoCodecs(self) -> List[str] """
        return []

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def videoCodecDescription(self, codec, p_str=None): # real signature unknown; restored from __doc__
        """ videoCodecDescription(self, codec: Optional[str]) -> str """
        return ""

    def videoSettings(self): # real signature unknown; restored from __doc__
        """ videoSettings(self) -> QVideoEncoderSettings """
        return QVideoEncoderSettings

    def __init__(self, parent, QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass


