# encoding: utf-8
# module PyQt5.QtMultimedia
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtMultimedia.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


from .QMediaControl import QMediaControl

class QImageEncoderControl(QMediaControl):
    """ QImageEncoderControl(parent: Optional[QObject] = None) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def imageCodecDescription(self, codec, p_str=None): # real signature unknown; restored from __doc__
        """ imageCodecDescription(self, codec: Optional[str]) -> str """
        return ""

    def imageSettings(self): # real signature unknown; restored from __doc__
        """ imageSettings(self) -> QImageEncoderSettings """
        return QImageEncoderSettings

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setImageSettings(self, settings): # real signature unknown; restored from __doc__
        """ setImageSettings(self, settings: QImageEncoderSettings) """
        pass

    def supportedImageCodecs(self): # real signature unknown; restored from __doc__
        """ supportedImageCodecs(self) -> List[str] """
        return []

    def supportedResolutions(self, settings): # real signature unknown; restored from __doc__
        """ supportedResolutions(self, settings: QImageEncoderSettings) -> (List[QSize], Optional[bool]) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent, QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass


