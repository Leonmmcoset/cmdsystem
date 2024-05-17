# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


from .QAbstractTransition import QAbstractTransition

class QSignalTransition(QAbstractTransition):
    """
    QSignalTransition(sourceState: Optional[QState] = None)
    QSignalTransition(signal: pyqtBoundSignal, sourceState: Optional[QState] = None)
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

    def eventTest(self, event, QEvent=None): # real signature unknown; restored from __doc__
        """ eventTest(self, event: Optional[QEvent]) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def onTransition(self, event, QEvent=None): # real signature unknown; restored from __doc__
        """ onTransition(self, event: Optional[QEvent]) """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderObject(self): # real signature unknown; restored from __doc__
        """ senderObject(self) -> Optional[QObject] """
        pass

    def senderObjectChanged(self, *args, **kwargs): # real signature unknown
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

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setSenderObject(self, sender, QObject=None): # real signature unknown; restored from __doc__
        """ setSenderObject(self, sender: Optional[QObject]) """
        pass

    def setSignal(self, signal, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ setSignal(self, signal: Union[QByteArray, bytes, bytearray]) """
        pass

    def signal(self): # real signature unknown; restored from __doc__
        """ signal(self) -> QByteArray """
        return QByteArray

    def signalChanged(self, *args, **kwargs): # real signature unknown
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

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


