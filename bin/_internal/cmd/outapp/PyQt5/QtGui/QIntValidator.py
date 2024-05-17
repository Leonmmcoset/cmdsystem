# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


from .QValidator import QValidator

class QIntValidator(QValidator):
    """
    QIntValidator(parent: Optional[QObject] = None)
    QIntValidator(bottom: int, top: int, parent: Optional[QObject] = None)
    """
    def bottom(self): # real signature unknown; restored from __doc__
        """ bottom(self) -> int """
        return 0

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def fixup(self, input, p_str=None): # real signature unknown; restored from __doc__
        """ fixup(self, input: Optional[str]) -> str """
        return ""

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setBottom(self, a0): # real signature unknown; restored from __doc__
        """ setBottom(self, a0: int) """
        pass

    def setRange(self, bottom, top): # real signature unknown; restored from __doc__
        """ setRange(self, bottom: int, top: int) """
        pass

    def setTop(self, a0): # real signature unknown; restored from __doc__
        """ setTop(self, a0: int) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def top(self): # real signature unknown; restored from __doc__
        """ top(self) -> int """
        return 0

    def validate(self, a0, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ validate(self, a0: Optional[str], a1: int) -> (QValidator.State, str, int) """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


