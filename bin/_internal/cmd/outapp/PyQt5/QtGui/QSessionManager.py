# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QSessionManager(__PyQt5_QtCore.QObject):
    # no doc
    def allowsErrorInteraction(self): # real signature unknown; restored from __doc__
        """ allowsErrorInteraction(self) -> bool """
        return False

    def allowsInteraction(self): # real signature unknown; restored from __doc__
        """ allowsInteraction(self) -> bool """
        return False

    def cancel(self): # real signature unknown; restored from __doc__
        """ cancel(self) """
        pass

    def discardCommand(self): # real signature unknown; restored from __doc__
        """ discardCommand(self) -> List[str] """
        return []

    def isPhase2(self): # real signature unknown; restored from __doc__
        """ isPhase2(self) -> bool """
        return False

    def release(self): # real signature unknown; restored from __doc__
        """ release(self) """
        pass

    def requestPhase2(self): # real signature unknown; restored from __doc__
        """ requestPhase2(self) """
        pass

    def restartCommand(self): # real signature unknown; restored from __doc__
        """ restartCommand(self) -> List[str] """
        return []

    def restartHint(self): # real signature unknown; restored from __doc__
        """ restartHint(self) -> QSessionManager.RestartHint """
        pass

    def sessionId(self): # real signature unknown; restored from __doc__
        """ sessionId(self) -> str """
        return ""

    def sessionKey(self): # real signature unknown; restored from __doc__
        """ sessionKey(self) -> str """
        return ""

    def setDiscardCommand(self, a0, Optional=None, p_str=None): # real signature unknown; restored from __doc__
        """ setDiscardCommand(self, a0: Iterable[Optional[str]]) """
        pass

    def setManagerProperty(self, name, p_str=None, *args, **kwargs): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setManagerProperty(self, name: Optional[str], value: Optional[str])
        setManagerProperty(self, name: Optional[str], value: Iterable[Optional[str]])
        """
        pass

    def setRestartCommand(self, a0, Optional=None, p_str=None): # real signature unknown; restored from __doc__
        """ setRestartCommand(self, a0: Iterable[Optional[str]]) """
        pass

    def setRestartHint(self, a0): # real signature unknown; restored from __doc__
        """ setRestartHint(self, a0: QSessionManager.RestartHint) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    RestartAnyway = 1
    RestartIfRunning = 0
    RestartImmediately = 2
    RestartNever = 3


