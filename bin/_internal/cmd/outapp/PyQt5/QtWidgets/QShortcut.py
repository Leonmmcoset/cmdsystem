# encoding: utf-8
# module PyQt5.QtWidgets
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


class QShortcut(__PyQt5_QtCore.QObject):
    """
    QShortcut(parent: Optional[QWidget])
    QShortcut(key: Union[QKeySequence, QKeySequence.StandardKey, Optional[str], int], parent: Optional[QWidget], member: PYQT_SLOT = None, ambiguousMember: PYQT_SLOT = None, context: Qt.ShortcutContext = Qt.WindowShortcut)
    """
    def activated(self, *args, **kwargs): # real signature unknown
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

    def activatedAmbiguously(self, *args, **kwargs): # real signature unknown
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

    def autoRepeat(self): # real signature unknown; restored from __doc__
        """ autoRepeat(self) -> bool """
        return False

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def context(self): # real signature unknown; restored from __doc__
        """ context(self) -> Qt.ShortcutContext """
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, e, QEvent=None): # real signature unknown; restored from __doc__
        """ event(self, e: Optional[QEvent]) -> bool """
        return False

    def id(self): # real signature unknown; restored from __doc__
        """ id(self) -> int """
        return 0

    def isEnabled(self): # real signature unknown; restored from __doc__
        """ isEnabled(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def key(self): # real signature unknown; restored from __doc__
        """ key(self) -> QKeySequence """
        pass

    def parentWidget(self): # real signature unknown; restored from __doc__
        """ parentWidget(self) -> Optional[QWidget] """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setAutoRepeat(self, on): # real signature unknown; restored from __doc__
        """ setAutoRepeat(self, on: bool) """
        pass

    def setContext(self, context): # real signature unknown; restored from __doc__
        """ setContext(self, context: Qt.ShortcutContext) """
        pass

    def setEnabled(self, enable): # real signature unknown; restored from __doc__
        """ setEnabled(self, enable: bool) """
        pass

    def setKey(self, key, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setKey(self, key: Union[QKeySequence, QKeySequence.StandardKey, Optional[str], int]) """
        pass

    def setWhatsThis(self, text, p_str=None): # real signature unknown; restored from __doc__
        """ setWhatsThis(self, text: Optional[str]) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def whatsThis(self): # real signature unknown; restored from __doc__
        """ whatsThis(self) -> str """
        return ""

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


