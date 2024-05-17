# encoding: utf-8
# module PyQt5.QtWidgets
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


from .QWidget import QWidget

class QWizardPage(QWidget):
    """ QWizardPage(parent: Optional[QWidget] = None) """
    def actionEvent(self, *args, **kwargs): # real signature unknown
        pass

    def buttonText(self, which): # real signature unknown; restored from __doc__
        """ buttonText(self, which: QWizard.WizardButton) -> str """
        return ""

    def changeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def cleanupPage(self): # real signature unknown; restored from __doc__
        """ cleanupPage(self) """
        pass

    def closeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def completeChanged(self, *args, **kwargs): # real signature unknown
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

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def contextMenuEvent(self, *args, **kwargs): # real signature unknown
        pass

    def create(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def destroy(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def dragEnterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dragLeaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dragMoveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dropEvent(self, *args, **kwargs): # real signature unknown
        pass

    def enterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, *args, **kwargs): # real signature unknown
        pass

    def field(self, name, p_str=None): # real signature unknown; restored from __doc__
        """ field(self, name: Optional[str]) -> Any """
        pass

    def focusInEvent(self, *args, **kwargs): # real signature unknown
        pass

    def focusNextChild(self, *args, **kwargs): # real signature unknown
        pass

    def focusNextPrevChild(self, *args, **kwargs): # real signature unknown
        pass

    def focusOutEvent(self, *args, **kwargs): # real signature unknown
        pass

    def focusPreviousChild(self, *args, **kwargs): # real signature unknown
        pass

    def hideEvent(self, *args, **kwargs): # real signature unknown
        pass

    def initializePage(self): # real signature unknown; restored from __doc__
        """ initializePage(self) """
        pass

    def initPainter(self, *args, **kwargs): # real signature unknown
        pass

    def inputMethodEvent(self, *args, **kwargs): # real signature unknown
        pass

    def isCommitPage(self): # real signature unknown; restored from __doc__
        """ isCommitPage(self) -> bool """
        return False

    def isComplete(self): # real signature unknown; restored from __doc__
        """ isComplete(self) -> bool """
        return False

    def isFinalPage(self): # real signature unknown; restored from __doc__
        """ isFinalPage(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def keyPressEvent(self, *args, **kwargs): # real signature unknown
        pass

    def keyReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def leaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def metric(self, *args, **kwargs): # real signature unknown
        pass

    def mouseDoubleClickEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mouseMoveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mousePressEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mouseReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def moveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def nativeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def nextId(self): # real signature unknown; restored from __doc__
        """ nextId(self) -> int """
        return 0

    def paintEvent(self, *args, **kwargs): # real signature unknown
        pass

    def pixmap(self, which): # real signature unknown; restored from __doc__
        """ pixmap(self, which: QWizard.WizardPixmap) -> QPixmap """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def registerField(self, name, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ registerField(self, name: Optional[str], widget: Optional[QWidget], property: Optional[str] = None, changedSignal: PYQT_SIGNAL = None) """
        pass

    def resizeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setButtonText(self, which, text, p_str=None): # real signature unknown; restored from __doc__
        """ setButtonText(self, which: QWizard.WizardButton, text: Optional[str]) """
        pass

    def setCommitPage(self, commitPage): # real signature unknown; restored from __doc__
        """ setCommitPage(self, commitPage: bool) """
        pass

    def setField(self, name, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setField(self, name: Optional[str], value: Any) """
        pass

    def setFinalPage(self, finalPage): # real signature unknown; restored from __doc__
        """ setFinalPage(self, finalPage: bool) """
        pass

    def setPixmap(self, which, pixmap): # real signature unknown; restored from __doc__
        """ setPixmap(self, which: QWizard.WizardPixmap, pixmap: QPixmap) """
        pass

    def setSubTitle(self, subTitle, p_str=None): # real signature unknown; restored from __doc__
        """ setSubTitle(self, subTitle: Optional[str]) """
        pass

    def setTitle(self, title, p_str=None): # real signature unknown; restored from __doc__
        """ setTitle(self, title: Optional[str]) """
        pass

    def sharedPainter(self, *args, **kwargs): # real signature unknown
        pass

    def showEvent(self, *args, **kwargs): # real signature unknown
        pass

    def subTitle(self): # real signature unknown; restored from __doc__
        """ subTitle(self) -> str """
        return ""

    def tabletEvent(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def title(self): # real signature unknown; restored from __doc__
        """ title(self) -> str """
        return ""

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

    def validatePage(self): # real signature unknown; restored from __doc__
        """ validatePage(self) -> bool """
        return False

    def wheelEvent(self, *args, **kwargs): # real signature unknown
        pass

    def wizard(self): # real signature unknown; restored from __doc__
        """ wizard(self) -> Optional[QWizard] """
        pass

    def __init__(self, parent, QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass


