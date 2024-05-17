# encoding: utf-8
# module PyQt5.QtMultimedia
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtMultimedia.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


from .QMediaControl import QMediaControl

class QCameraImageProcessingControl(QMediaControl):
    """ QCameraImageProcessingControl(parent: Optional[QObject] = None) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def isParameterSupported(self, a0): # real signature unknown; restored from __doc__
        """ isParameterSupported(self, a0: QCameraImageProcessingControl.ProcessingParameter) -> bool """
        return False

    def isParameterValueSupported(self, parameter, value): # real signature unknown; restored from __doc__
        """ isParameterValueSupported(self, parameter: QCameraImageProcessingControl.ProcessingParameter, value: Any) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def parameter(self, parameter): # real signature unknown; restored from __doc__
        """ parameter(self, parameter: QCameraImageProcessingControl.ProcessingParameter) -> Any """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setParameter(self, parameter, value): # real signature unknown; restored from __doc__
        """ setParameter(self, parameter: QCameraImageProcessingControl.ProcessingParameter, value: Any) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent, QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    Brightness = 4
    BrightnessAdjustment = 9
    ColorFilter = 12
    ColorTemperature = 1
    Contrast = 2
    ContrastAdjustment = 7
    Denoising = 6
    DenoisingAdjustment = 11
    ExtendedParameter = 1000
    Saturation = 3
    SaturationAdjustment = 8
    Sharpening = 5
    SharpeningAdjustment = 10
    WhiteBalancePreset = 0


