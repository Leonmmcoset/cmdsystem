# encoding: utf-8
# module PyQt5.QtMultimedia
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtMultimedia.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


from .QMediaControl import QMediaControl

class QCameraViewfinderSettingsControl(QMediaControl):
    """ QCameraViewfinderSettingsControl(parent: Optional[QObject] = None) """
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

    def isViewfinderParameterSupported(self, parameter): # real signature unknown; restored from __doc__
        """ isViewfinderParameterSupported(self, parameter: QCameraViewfinderSettingsControl.ViewfinderParameter) -> bool """
        return False

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setViewfinderParameter(self, parameter, value): # real signature unknown; restored from __doc__
        """ setViewfinderParameter(self, parameter: QCameraViewfinderSettingsControl.ViewfinderParameter, value: Any) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def viewfinderParameter(self, parameter): # real signature unknown; restored from __doc__
        """ viewfinderParameter(self, parameter: QCameraViewfinderSettingsControl.ViewfinderParameter) -> Any """
        pass

    def __init__(self, parent, QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    MaximumFrameRate = 3
    MinimumFrameRate = 2
    PixelAspectRatio = 1
    PixelFormat = 4
    Resolution = 0
    UserParameter = 1000


