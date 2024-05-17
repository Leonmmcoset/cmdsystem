# encoding: utf-8
# module PyQt5.QtWidgets
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


class QGestureRecognizer(__sip.wrapper):
    """
    QGestureRecognizer()
    QGestureRecognizer(a0: QGestureRecognizer)
    """
    def create(self, target, QObject=None): # real signature unknown; restored from __doc__
        """ create(self, target: Optional[QObject]) -> Optional[QGesture] """
        pass

    def recognize(self, state, QGesture=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ recognize(self, state: Optional[QGesture], watched: Optional[QObject], event: Optional[QEvent]) -> QGestureRecognizer.Result """
        pass

    def registerRecognizer(self, recognizer, QGestureRecognizer=None): # real signature unknown; restored from __doc__
        """ registerRecognizer(recognizer: Optional[QGestureRecognizer]) -> Qt.GestureType """
        pass

    def reset(self, state, QGesture=None): # real signature unknown; restored from __doc__
        """ reset(self, state: Optional[QGesture]) """
        pass

    def unregisterRecognizer(self, type): # real signature unknown; restored from __doc__
        """ unregisterRecognizer(type: Qt.GestureType) """
        pass

    def __init__(self, a0=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    CancelGesture = 16
    ConsumeEventHint = 256
    FinishGesture = 8
    Ignore = 1
    MayBeGesture = 2
    TriggerGesture = 4


