# encoding: utf-8
# module PyQt5.QtWidgets
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


from .QDialog import QDialog

class QWizard(QDialog):
    """ QWizard(parent: Optional[QWidget] = None, flags: Union[Qt.WindowFlags, Qt.WindowType] = Qt.WindowFlags()) """
    def actionEvent(self, *args, **kwargs): # real signature unknown
        pass

    def addPage(self, page, QWizardPage=None): # real signature unknown; restored from __doc__
        """ addPage(self, page: Optional[QWizardPage]) -> int """
        return 0

    def back(self): # real signature unknown; restored from __doc__
        """ back(self) """
        pass

    def button(self, which): # real signature unknown; restored from __doc__
        """ button(self, which: QWizard.WizardButton) -> Optional[QAbstractButton] """
        pass

    def buttonText(self, which): # real signature unknown; restored from __doc__
        """ buttonText(self, which: QWizard.WizardButton) -> str """
        return ""

    def changeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def cleanupPage(self, id): # real signature unknown; restored from __doc__
        """ cleanupPage(self, id: int) """
        pass

    def closeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def contextMenuEvent(self, *args, **kwargs): # real signature unknown
        pass

    def create(self, *args, **kwargs): # real signature unknown
        pass

    def currentId(self): # real signature unknown; restored from __doc__
        """ currentId(self) -> int """
        return 0

    def currentIdChanged(self, *args, **kwargs): # real signature unknown
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

    def currentPage(self): # real signature unknown; restored from __doc__
        """ currentPage(self) -> Optional[QWizardPage] """
        pass

    def customButtonClicked(self, *args, **kwargs): # real signature unknown
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

    def destroy(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def done(self, result): # real signature unknown; restored from __doc__
        """ done(self, result: int) """
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

    def event(self, event, QEvent=None): # real signature unknown; restored from __doc__
        """ event(self, event: Optional[QEvent]) -> bool """
        return False

    def eventFilter(self, *args, **kwargs): # real signature unknown
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

    def hasVisitedPage(self, id): # real signature unknown; restored from __doc__
        """ hasVisitedPage(self, id: int) -> bool """
        return False

    def helpRequested(self, *args, **kwargs): # real signature unknown
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

    def hideEvent(self, *args, **kwargs): # real signature unknown
        pass

    def initializePage(self, id): # real signature unknown; restored from __doc__
        """ initializePage(self, id: int) """
        pass

    def initPainter(self, *args, **kwargs): # real signature unknown
        pass

    def inputMethodEvent(self, *args, **kwargs): # real signature unknown
        pass

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

    def next(self): # real signature unknown; restored from __doc__
        """ next(self) """
        pass

    def nextId(self): # real signature unknown; restored from __doc__
        """ nextId(self) -> int """
        return 0

    def options(self): # real signature unknown; restored from __doc__
        """ options(self) -> QWizard.WizardOptions """
        pass

    def page(self, id): # real signature unknown; restored from __doc__
        """ page(self, id: int) -> Optional[QWizardPage] """
        pass

    def pageAdded(self, *args, **kwargs): # real signature unknown
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

    def pageIds(self): # real signature unknown; restored from __doc__
        """ pageIds(self) -> List[int] """
        return []

    def pageRemoved(self, *args, **kwargs): # real signature unknown
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

    def paintEvent(self, event, QPaintEvent=None): # real signature unknown; restored from __doc__
        """ paintEvent(self, event: Optional[QPaintEvent]) """
        pass

    def pixmap(self, which): # real signature unknown; restored from __doc__
        """ pixmap(self, which: QWizard.WizardPixmap) -> QPixmap """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def removePage(self, id): # real signature unknown; restored from __doc__
        """ removePage(self, id: int) """
        pass

    def resizeEvent(self, event, QResizeEvent=None): # real signature unknown; restored from __doc__
        """ resizeEvent(self, event: Optional[QResizeEvent]) """
        pass

    def restart(self): # real signature unknown; restored from __doc__
        """ restart(self) """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setButton(self, which, button, QAbstractButton=None): # real signature unknown; restored from __doc__
        """ setButton(self, which: QWizard.WizardButton, button: Optional[QAbstractButton]) """
        pass

    def setButtonLayout(self, layout, QWizard_WizardButton=None): # real signature unknown; restored from __doc__
        """ setButtonLayout(self, layout: Iterable[QWizard.WizardButton]) """
        pass

    def setButtonText(self, which, text, p_str=None): # real signature unknown; restored from __doc__
        """ setButtonText(self, which: QWizard.WizardButton, text: Optional[str]) """
        pass

    def setDefaultProperty(self, className, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setDefaultProperty(self, className: Optional[str], property: Optional[str], changedSignal: PYQT_SIGNAL) """
        pass

    def setField(self, name, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setField(self, name: Optional[str], value: Any) """
        pass

    def setOption(self, option, on=True): # real signature unknown; restored from __doc__
        """ setOption(self, option: QWizard.WizardOption, on: bool = True) """
        pass

    def setOptions(self, options, QWizard_WizardOptions=None, QWizard_WizardOption=None): # real signature unknown; restored from __doc__
        """ setOptions(self, options: Union[QWizard.WizardOptions, QWizard.WizardOption]) """
        pass

    def setPage(self, id, page, QWizardPage=None): # real signature unknown; restored from __doc__
        """ setPage(self, id: int, page: Optional[QWizardPage]) """
        pass

    def setPixmap(self, which, pixmap): # real signature unknown; restored from __doc__
        """ setPixmap(self, which: QWizard.WizardPixmap, pixmap: QPixmap) """
        pass

    def setSideWidget(self, widget, QWidget=None): # real signature unknown; restored from __doc__
        """ setSideWidget(self, widget: Optional[QWidget]) """
        pass

    def setStartId(self, id): # real signature unknown; restored from __doc__
        """ setStartId(self, id: int) """
        pass

    def setSubTitleFormat(self, format): # real signature unknown; restored from __doc__
        """ setSubTitleFormat(self, format: Qt.TextFormat) """
        pass

    def setTitleFormat(self, format): # real signature unknown; restored from __doc__
        """ setTitleFormat(self, format: Qt.TextFormat) """
        pass

    def setVisible(self, visible): # real signature unknown; restored from __doc__
        """ setVisible(self, visible: bool) """
        pass

    def setWizardStyle(self, style): # real signature unknown; restored from __doc__
        """ setWizardStyle(self, style: QWizard.WizardStyle) """
        pass

    def sharedPainter(self, *args, **kwargs): # real signature unknown
        pass

    def showEvent(self, *args, **kwargs): # real signature unknown
        pass

    def sideWidget(self): # real signature unknown; restored from __doc__
        """ sideWidget(self) -> Optional[QWidget] """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> QSize """
        pass

    def startId(self): # real signature unknown; restored from __doc__
        """ startId(self) -> int """
        return 0

    def subTitleFormat(self): # real signature unknown; restored from __doc__
        """ subTitleFormat(self) -> Qt.TextFormat """
        pass

    def tabletEvent(self, *args, **kwargs): # real signature unknown
        pass

    def testOption(self, option): # real signature unknown; restored from __doc__
        """ testOption(self, option: QWizard.WizardOption) -> bool """
        return False

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def titleFormat(self): # real signature unknown; restored from __doc__
        """ titleFormat(self) -> Qt.TextFormat """
        pass

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

    def validateCurrentPage(self): # real signature unknown; restored from __doc__
        """ validateCurrentPage(self) -> bool """
        return False

    def visitedIds(self): # real signature unknown; restored from __doc__
        """ visitedIds(self) -> List[int] """
        return []

    def visitedPages(self): # real signature unknown; restored from __doc__
        """ visitedPages(self) -> List[int] """
        return []

    def wheelEvent(self, *args, **kwargs): # real signature unknown
        pass

    def wizardStyle(self): # real signature unknown; restored from __doc__
        """ wizardStyle(self) -> QWizard.WizardStyle """
        pass

    def __init__(self, parent, QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    AeroStyle = 3
    BackButton = 0
    BackgroundPixmap = 3
    BannerPixmap = 2
    CancelButton = 4
    CancelButtonOnLeft = 1024
    ClassicStyle = 0
    CommitButton = 2
    CustomButton1 = 6
    CustomButton2 = 7
    CustomButton3 = 8
    DisabledBackButtonOnLastPage = 64
    ExtendedWatermarkPixmap = 4
    FinishButton = 3
    HaveCustomButton1 = 8192
    HaveCustomButton2 = 16384
    HaveCustomButton3 = 32768
    HaveFinishButtonOnEarlyPages = 256
    HaveHelpButton = 2048
    HaveNextButtonOnLastPage = 128
    HelpButton = 5
    HelpButtonOnRight = 4096
    IgnoreSubTitles = 2
    IndependentPages = 1
    LogoPixmap = 1
    MacStyle = 2
    ModernStyle = 1
    NextButton = 1
    NoBackButtonOnLastPage = 32
    NoBackButtonOnStartPage = 16
    NoCancelButton = 512
    NoCancelButtonOnLastPage = 65536
    NoDefaultButton = 8
    Stretch = 9
    WatermarkPixmap = 0


