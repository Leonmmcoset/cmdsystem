# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


from .QAbstractTransition import QAbstractTransition

class QEventTransition(QAbstractTransition):
    """
    QEventTransition(sourceState: Optional[QState] = None)
    QEventTransition(object: Optional[QObject], type: QEvent.Type, sourceState: Optional[QState] = None)
    """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, e, QEvent=None): # real signature unknown; restored from __doc__
        """ event(self, e: Optional[QEvent]) -> bool """
        return False

    def eventSource(self): # real signature unknown; restored from __doc__
        """ eventSource(self) -> Optional[QObject] """
        pass

    def eventTest(self, event, QEvent=None): # real signature unknown; restored from __doc__
        """ eventTest(self, event: Optional[QEvent]) -> bool """
        return False

    def eventType(self): # real signature unknown; restored from __doc__
        """ eventType(self) -> QEvent.Type """
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
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

    def setEventSource(self, p_object, QObject=None): # real signature unknown; restored from __doc__
        """ setEventSource(self, object: Optional[QObject]) """
        pass

    def setEventType(self, type): # real signature unknown; restored from __doc__
        """ setEventType(self, type: QEvent.Type) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


