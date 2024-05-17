# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QOpenGLDebugMessage(__sip.simplewrapper):
    """
    QOpenGLDebugMessage()
    QOpenGLDebugMessage(debugMessage: QOpenGLDebugMessage)
    """
    def createApplicationMessage(self, text, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ createApplicationMessage(text: Optional[str], id: int = 0, severity: QOpenGLDebugMessage.Severity = QOpenGLDebugMessage.NotificationSeverity, type: QOpenGLDebugMessage.Type = QOpenGLDebugMessage.OtherType) -> QOpenGLDebugMessage """
        pass

    def createThirdPartyMessage(self, text, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ createThirdPartyMessage(text: Optional[str], id: int = 0, severity: QOpenGLDebugMessage.Severity = QOpenGLDebugMessage.NotificationSeverity, type: QOpenGLDebugMessage.Type = QOpenGLDebugMessage.OtherType) -> QOpenGLDebugMessage """
        pass

    def id(self): # real signature unknown; restored from __doc__
        """ id(self) -> int """
        return 0

    def message(self): # real signature unknown; restored from __doc__
        """ message(self) -> str """
        return ""

    def severity(self): # real signature unknown; restored from __doc__
        """ severity(self) -> QOpenGLDebugMessage.Severity """
        pass

    def source(self): # real signature unknown; restored from __doc__
        """ source(self) -> QOpenGLDebugMessage.Source """
        pass

    def swap(self, debugMessage): # real signature unknown; restored from __doc__
        """ swap(self, debugMessage: QOpenGLDebugMessage) """
        pass

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> QOpenGLDebugMessage.Type """
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

    def __init__(self, debugMessage=None): # real signature unknown; restored from __doc__ with multiple overloads
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


    AnySeverity = -1
    AnySource = -1
    AnyType = -1
    APISource = 1
    ApplicationSource = 16
    DeprecatedBehaviorType = 2
    ErrorType = 1
    GroupPopType = 256
    GroupPushType = 128
    HighSeverity = 1
    InvalidSeverity = 0
    InvalidSource = 0
    InvalidType = 0
    LowSeverity = 4
    MarkerType = 64
    MediumSeverity = 2
    NotificationSeverity = 8
    OtherSource = 32
    OtherType = 32
    PerformanceType = 16
    PortabilityType = 8
    ShaderCompilerSource = 4
    ThirdPartySource = 8
    UndefinedBehaviorType = 4
    WindowSystemSource = 2
    __hash__ = None


