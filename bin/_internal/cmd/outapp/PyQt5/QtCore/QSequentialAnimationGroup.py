# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


from .QAnimationGroup import QAnimationGroup

class QSequentialAnimationGroup(QAnimationGroup):
    """ QSequentialAnimationGroup(parent: Optional[QObject] = None) """
    def addPause(self, msecs): # real signature unknown; restored from __doc__
        """ addPause(self, msecs: int) -> Optional[QPauseAnimation] """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def currentAnimation(self): # real signature unknown; restored from __doc__
        """ currentAnimation(self) -> Optional[QAbstractAnimation] """
        pass

    def currentAnimationChanged(self, *args, **kwargs): # real signature unknown
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def duration(self): # real signature unknown; restored from __doc__
        """ duration(self) -> int """
        return 0

    def event(self, event, QEvent=None): # real signature unknown; restored from __doc__
        """ event(self, event: Optional[QEvent]) -> bool """
        return False

    def insertPause(self, index, msecs): # real signature unknown; restored from __doc__
        """ insertPause(self, index: int, msecs: int) -> Optional[QPauseAnimation] """
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def updateCurrentTime(self, a0): # real signature unknown; restored from __doc__
        """ updateCurrentTime(self, a0: int) """
        pass

    def updateDirection(self, direction): # real signature unknown; restored from __doc__
        """ updateDirection(self, direction: QAbstractAnimation.Direction) """
        pass

    def updateState(self, newState, oldState): # real signature unknown; restored from __doc__
        """ updateState(self, newState: QAbstractAnimation.State, oldState: QAbstractAnimation.State) """
        pass

    def __init__(self, parent, QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass


