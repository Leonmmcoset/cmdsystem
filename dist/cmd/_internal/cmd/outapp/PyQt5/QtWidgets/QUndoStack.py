# encoding: utf-8
# module PyQt5.QtWidgets
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


class QUndoStack(__PyQt5_QtCore.QObject):
    """ QUndoStack(parent: Optional[QObject] = None) """
    def beginMacro(self, text, p_str=None): # real signature unknown; restored from __doc__
        """ beginMacro(self, text: Optional[str]) """
        pass

    def canRedo(self): # real signature unknown; restored from __doc__
        """ canRedo(self) -> bool """
        return False

    def canRedoChanged(self, *args, **kwargs): # real signature unknown
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

    def canUndo(self): # real signature unknown; restored from __doc__
        """ canUndo(self) -> bool """
        return False

    def canUndoChanged(self, *args, **kwargs): # real signature unknown
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

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def cleanChanged(self, *args, **kwargs): # real signature unknown
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

    def cleanIndex(self): # real signature unknown; restored from __doc__
        """ cleanIndex(self) -> int """
        return 0

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def command(self, index): # real signature unknown; restored from __doc__
        """ command(self, index: int) -> Optional[QUndoCommand] """
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def count(self): # real signature unknown; restored from __doc__
        """ count(self) -> int """
        return 0

    def createRedoAction(self, parent, QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ createRedoAction(self, parent: Optional[QObject], prefix: Optional[str] = '') -> Optional[QAction] """
        pass

    def createUndoAction(self, parent, QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ createUndoAction(self, parent: Optional[QObject], prefix: Optional[str] = '') -> Optional[QAction] """
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def endMacro(self): # real signature unknown; restored from __doc__
        """ endMacro(self) """
        pass

    def index(self): # real signature unknown; restored from __doc__
        """ index(self) -> int """
        return 0

    def indexChanged(self, *args, **kwargs): # real signature unknown
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

    def isActive(self): # real signature unknown; restored from __doc__
        """ isActive(self) -> bool """
        return False

    def isClean(self): # real signature unknown; restored from __doc__
        """ isClean(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def push(self, cmd, QUndoCommand=None): # real signature unknown; restored from __doc__
        """ push(self, cmd: Optional[QUndoCommand]) """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def redo(self): # real signature unknown; restored from __doc__
        """ redo(self) """
        pass

    def redoText(self): # real signature unknown; restored from __doc__
        """ redoText(self) -> str """
        return ""

    def redoTextChanged(self, *args, **kwargs): # real signature unknown
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

    def resetClean(self): # real signature unknown; restored from __doc__
        """ resetClean(self) """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setActive(self, active=True): # real signature unknown; restored from __doc__
        """ setActive(self, active: bool = True) """
        pass

    def setClean(self): # real signature unknown; restored from __doc__
        """ setClean(self) """
        pass

    def setIndex(self, idx): # real signature unknown; restored from __doc__
        """ setIndex(self, idx: int) """
        pass

    def setUndoLimit(self, limit): # real signature unknown; restored from __doc__
        """ setUndoLimit(self, limit: int) """
        pass

    def text(self, idx): # real signature unknown; restored from __doc__
        """ text(self, idx: int) -> str """
        return ""

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def undo(self): # real signature unknown; restored from __doc__
        """ undo(self) """
        pass

    def undoLimit(self): # real signature unknown; restored from __doc__
        """ undoLimit(self) -> int """
        return 0

    def undoText(self): # real signature unknown; restored from __doc__
        """ undoText(self) -> str """
        return ""

    def undoTextChanged(self, *args, **kwargs): # real signature unknown
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

    def __init__(self, parent, QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass


