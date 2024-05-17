# encoding: utf-8
# module PyQt5.QtWidgets
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


class QActionGroup(__PyQt5_QtCore.QObject):
    """ QActionGroup(parent: Optional[QObject]) """
    def actions(self): # real signature unknown; restored from __doc__
        """ actions(self) -> List[QAction] """
        return []

    def addAction(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        addAction(self, a: Optional[QAction]) -> Optional[QAction]
        addAction(self, text: Optional[str]) -> Optional[QAction]
        addAction(self, icon: QIcon, text: Optional[str]) -> Optional[QAction]
        """
        pass

    def checkedAction(self): # real signature unknown; restored from __doc__
        """ checkedAction(self) -> Optional[QAction] """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def exclusionPolicy(self): # real signature unknown; restored from __doc__
        """ exclusionPolicy(self) -> QActionGroup.ExclusionPolicy """
        pass

    def hovered(self, *args, **kwargs): # real signature unknown
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

    def isEnabled(self): # real signature unknown; restored from __doc__
        """ isEnabled(self) -> bool """
        return False

    def isExclusive(self): # real signature unknown; restored from __doc__
        """ isExclusive(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def isVisible(self): # real signature unknown; restored from __doc__
        """ isVisible(self) -> bool """
        return False

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def removeAction(self, a, QAction=None): # real signature unknown; restored from __doc__
        """ removeAction(self, a: Optional[QAction]) """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setDisabled(self, b): # real signature unknown; restored from __doc__
        """ setDisabled(self, b: bool) """
        pass

    def setEnabled(self, a0): # real signature unknown; restored from __doc__
        """ setEnabled(self, a0: bool) """
        pass

    def setExclusionPolicy(self, policy): # real signature unknown; restored from __doc__
        """ setExclusionPolicy(self, policy: QActionGroup.ExclusionPolicy) """
        pass

    def setExclusive(self, a0): # real signature unknown; restored from __doc__
        """ setExclusive(self, a0: bool) """
        pass

    def setVisible(self, a0): # real signature unknown; restored from __doc__
        """ setVisible(self, a0: bool) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
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

    def __init__(self, parent, QObject=None): # real signature unknown; restored from __doc__
        pass



