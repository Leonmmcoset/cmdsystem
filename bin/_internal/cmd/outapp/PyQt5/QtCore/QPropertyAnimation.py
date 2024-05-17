# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


from .QVariantAnimation import QVariantAnimation

class QPropertyAnimation(QVariantAnimation):
    """
    QPropertyAnimation(parent: Optional[QObject] = None)
    QPropertyAnimation(target: Optional[QObject], propertyName: Union[QByteArray, bytes, bytearray], parent: Optional[QObject] = None)
    """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, event, QEvent=None): # real signature unknown; restored from __doc__
        """ event(self, event: Optional[QEvent]) -> bool """
        return False

    def interpolated(self, *args, **kwargs): # real signature unknown
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def propertyName(self): # real signature unknown; restored from __doc__
        """ propertyName(self) -> QByteArray """
        return QByteArray

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setPropertyName(self, propertyName, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ setPropertyName(self, propertyName: Union[QByteArray, bytes, bytearray]) """
        pass

    def setTargetObject(self, target, QObject=None): # real signature unknown; restored from __doc__
        """ setTargetObject(self, target: Optional[QObject]) """
        pass

    def targetObject(self): # real signature unknown; restored from __doc__
        """ targetObject(self) -> Optional[QObject] """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def updateCurrentTime(self, *args, **kwargs): # real signature unknown
        pass

    def updateCurrentValue(self, value): # real signature unknown; restored from __doc__
        """ updateCurrentValue(self, value: Any) """
        pass

    def updateDirection(self, *args, **kwargs): # real signature unknown
        pass

    def updateState(self, newState, oldState): # real signature unknown; restored from __doc__
        """ updateState(self, newState: QAbstractAnimation.State, oldState: QAbstractAnimation.State) """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


