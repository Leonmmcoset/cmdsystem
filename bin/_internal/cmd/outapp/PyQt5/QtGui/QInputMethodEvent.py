# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QInputMethodEvent(__PyQt5_QtCore.QEvent):
    """
    QInputMethodEvent()
    QInputMethodEvent(preeditText: Optional[str], attributes: Iterable[QInputMethodEvent.Attribute])
    QInputMethodEvent(other: QInputMethodEvent)
    """
    def attributes(self): # real signature unknown; restored from __doc__
        """ attributes(self) -> List[QInputMethodEvent.Attribute] """
        return []

    def commitString(self): # real signature unknown; restored from __doc__
        """ commitString(self) -> str """
        return ""

    def preeditString(self): # real signature unknown; restored from __doc__
        """ preeditString(self) -> str """
        return ""

    def replacementLength(self): # real signature unknown; restored from __doc__
        """ replacementLength(self) -> int """
        return 0

    def replacementStart(self): # real signature unknown; restored from __doc__
        """ replacementStart(self) -> int """
        return 0

    def setCommitString(self, commitString, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setCommitString(self, commitString: Optional[str], from_: int = 0, length: int = 0) """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    Cursor = 1
    Language = 2
    Ruby = 3
    Selection = 4
    TextFormat = 0


