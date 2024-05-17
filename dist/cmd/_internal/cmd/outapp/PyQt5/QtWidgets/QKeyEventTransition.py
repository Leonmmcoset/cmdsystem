# encoding: utf-8
# module PyQt5.QtWidgets
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


class QKeyEventTransition(__PyQt5_QtCore.QEventTransition):
    """
    QKeyEventTransition(sourceState: Optional[QState] = None)
    QKeyEventTransition(object: Optional[QObject], type: QEvent.Type, key: int, sourceState: Optional[QState] = None)
    """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, *args, **kwargs): # real signature unknown
        pass

    def eventTest(self, event, QEvent=None): # real signature unknown; restored from __doc__
        """ eventTest(self, event: Optional[QEvent]) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def key(self): # real signature unknown; restored from __doc__
        """ key(self) -> int """
        return 0

    def modifierMask(self): # real signature unknown; restored from __doc__
        """ modifierMask(self) -> Qt.KeyboardModifiers """
        pass

    def onTransition(self, event, QEvent=None): # real signature unknown; restored from __doc__
        """ onTransition(self, event: Optional[QEvent]) """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setKey(self, key): # real signature unknown; restored from __doc__
        """ setKey(self, key: int) """
        pass

    def setModifierMask(self, modifiers, Qt_KeyboardModifiers=None, Qt_KeyboardModifier=None): # real signature unknown; restored from __doc__
        """ setModifierMask(self, modifiers: Union[Qt.KeyboardModifiers, Qt.KeyboardModifier]) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


