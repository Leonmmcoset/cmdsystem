# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


from .QObject import QObject

class QAbstractTransition(QObject):
    """ QAbstractTransition(sourceState: Optional[QState] = None) """
    def addAnimation(self, animation, QAbstractAnimation=None): # real signature unknown; restored from __doc__
        """ addAnimation(self, animation: Optional[QAbstractAnimation]) """
        pass

    def animations(self): # real signature unknown; restored from __doc__
        """ animations(self) -> List[QAbstractAnimation] """
        return []

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

    def eventTest(self, event, QEvent=None): # real signature unknown; restored from __doc__
        """ eventTest(self, event: Optional[QEvent]) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def machine(self): # real signature unknown; restored from __doc__
        """ machine(self) -> Optional[QStateMachine] """
        pass

    def onTransition(self, event, QEvent=None): # real signature unknown; restored from __doc__
        """ onTransition(self, event: Optional[QEvent]) """
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

    def setTargetState(self, target, QAbstractState=None): # real signature unknown; restored from __doc__
        """ setTargetState(self, target: Optional[QAbstractState]) """
        pass

    def setTargetStates(self, targets, QAbstractState=None): # real signature unknown; restored from __doc__
        """ setTargetStates(self, targets: Iterable[QAbstractState]) """
        pass

    def setTransitionType(self, type): # real signature unknown; restored from __doc__
        """ setTransitionType(self, type: QAbstractTransition.TransitionType) """
        pass

    def sourceState(self): # real signature unknown; restored from __doc__
        """ sourceState(self) -> Optional[QState] """
        pass

    def targetState(self): # real signature unknown; restored from __doc__
        """ targetState(self) -> Optional[QAbstractState] """
        pass

    def targetStateChanged(self, *args, **kwargs): # real signature unknown
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

    def targetStates(self): # real signature unknown; restored from __doc__
        """ targetStates(self) -> List[QAbstractState] """
        return []

    def targetStatesChanged(self, *args, **kwargs): # real signature unknown
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

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def transitionType(self): # real signature unknown; restored from __doc__
        """ transitionType(self) -> QAbstractTransition.TransitionType """
        pass

    def triggered(self, *args, **kwargs): # real signature unknown
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

    def __init__(self, sourceState, QState=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    ExternalTransition = 0
    InternalTransition = 1


