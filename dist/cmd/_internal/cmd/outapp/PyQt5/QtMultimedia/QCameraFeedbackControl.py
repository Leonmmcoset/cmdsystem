# encoding: utf-8
# module PyQt5.QtMultimedia
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtMultimedia.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


from .QMediaControl import QMediaControl

class QCameraFeedbackControl(QMediaControl):
    """ QCameraFeedbackControl(parent: Optional[QObject] = None) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def isEventFeedbackEnabled(self, a0): # real signature unknown; restored from __doc__
        """ isEventFeedbackEnabled(self, a0: QCameraFeedbackControl.EventType) -> bool """
        return False

    def isEventFeedbackLocked(self, a0): # real signature unknown; restored from __doc__
        """ isEventFeedbackLocked(self, a0: QCameraFeedbackControl.EventType) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def resetEventFeedback(self, a0): # real signature unknown; restored from __doc__
        """ resetEventFeedback(self, a0: QCameraFeedbackControl.EventType) """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setEventFeedbackEnabled(self, a0, a1): # real signature unknown; restored from __doc__
        """ setEventFeedbackEnabled(self, a0: QCameraFeedbackControl.EventType, a1: bool) -> bool """
        return False

    def setEventFeedbackSound(self, a0, filePath, p_str=None): # real signature unknown; restored from __doc__
        """ setEventFeedbackSound(self, a0: QCameraFeedbackControl.EventType, filePath: Optional[str]) -> bool """
        return False

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent, QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    AutoFocusFailed = 11
    AutoFocusInProgress = 9
    AutoFocusLocked = 10
    ImageCaptured = 3
    ImageError = 5
    ImageSaved = 4
    RecordingInProgress = 7
    RecordingStarted = 6
    RecordingStopped = 8
    ViewfinderStarted = 1
    ViewfinderStopped = 2


