# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QShortcutEvent(__PyQt5_QtCore.QEvent):
    """
    QShortcutEvent(key: Union[QKeySequence, QKeySequence.StandardKey, Optional[str], int], id: int, ambiguous: bool = False)
    QShortcutEvent(a0: QShortcutEvent)
    """
    def isAmbiguous(self): # real signature unknown; restored from __doc__
        """ isAmbiguous(self) -> bool """
        return False

    def key(self): # real signature unknown; restored from __doc__
        """ key(self) -> QKeySequence """
        return QKeySequence

    def shortcutId(self): # real signature unknown; restored from __doc__
        """ shortcutId(self) -> int """
        return 0

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


