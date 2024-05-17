# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


from .QAbstractAnimation import QAbstractAnimation

class QAnimationGroup(QAbstractAnimation):
    """ QAnimationGroup(parent: Optional[QObject] = None) """
    def addAnimation(self, animation, QAbstractAnimation=None): # real signature unknown; restored from __doc__
        """ addAnimation(self, animation: Optional[QAbstractAnimation]) """
        pass

    def animationAt(self, index): # real signature unknown; restored from __doc__
        """ animationAt(self, index: int) -> Optional[QAbstractAnimation] """
        pass

    def animationCount(self): # real signature unknown; restored from __doc__
        """ animationCount(self) -> int """
        return 0

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
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

    def indexOfAnimation(self, animation, QAbstractAnimation=None): # real signature unknown; restored from __doc__
        """ indexOfAnimation(self, animation: Optional[QAbstractAnimation]) -> int """
        return 0

    def insertAnimation(self, index, animation, QAbstractAnimation=None): # real signature unknown; restored from __doc__
        """ insertAnimation(self, index: int, animation: Optional[QAbstractAnimation]) """
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def removeAnimation(self, animation, QAbstractAnimation=None): # real signature unknown; restored from __doc__
        """ removeAnimation(self, animation: Optional[QAbstractAnimation]) """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def takeAnimation(self, index): # real signature unknown; restored from __doc__
        """ takeAnimation(self, index: int) -> Optional[QAbstractAnimation] """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def updateCurrentTime(self, *args, **kwargs): # real signature unknown
        pass

    def updateDirection(self, *args, **kwargs): # real signature unknown
        pass

    def updateState(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent, QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass


