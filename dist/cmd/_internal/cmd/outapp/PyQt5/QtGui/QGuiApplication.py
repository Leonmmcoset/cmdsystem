# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QGuiApplication(__PyQt5_QtCore.QCoreApplication):
    """ QGuiApplication(argv: List[str]) """
    def allWindows(self): # real signature unknown; restored from __doc__
        """ allWindows() -> List[QWindow] """
        return []

    def applicationDisplayName(self): # real signature unknown; restored from __doc__
        """ applicationDisplayName() -> str """
        return ""

    def applicationDisplayNameChanged(self, *args, **kwargs): # real signature unknown
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

    def applicationState(self): # real signature unknown; restored from __doc__
        """ applicationState() -> Qt.ApplicationState """
        pass

    def applicationStateChanged(self, *args, **kwargs): # real signature unknown
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

    def changeOverrideCursor(self, a0, QCursor=None, Qt_CursorShape=None): # real signature unknown; restored from __doc__
        """ changeOverrideCursor(a0: Union[QCursor, Qt.CursorShape]) """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def clipboard(self): # real signature unknown; restored from __doc__
        """ clipboard() -> Optional[QClipboard] """
        pass

    def commitDataRequest(self, *args, **kwargs): # real signature unknown
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

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def desktopFileName(self): # real signature unknown; restored from __doc__
        """ desktopFileName() -> str """
        return ""

    def desktopSettingsAware(self): # real signature unknown; restored from __doc__
        """ desktopSettingsAware() -> bool """
        return False

    def devicePixelRatio(self): # real signature unknown; restored from __doc__
        """ devicePixelRatio(self) -> float """
        return 0.0

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, a0, QEvent=None): # real signature unknown; restored from __doc__
        """ event(self, a0: Optional[QEvent]) -> bool """
        return False

    def exec(self): # real signature unknown; restored from __doc__
        """ exec() -> int """
        return 0

    def exec_(self): # real signature unknown; restored from __doc__
        """ exec_() -> int """
        return 0

    def focusObject(self): # real signature unknown; restored from __doc__
        """ focusObject() -> Optional[QObject] """
        pass

    def focusObjectChanged(self, *args, **kwargs): # real signature unknown
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

    def focusWindow(self): # real signature unknown; restored from __doc__
        """ focusWindow() -> Optional[QWindow] """
        pass

    def focusWindowChanged(self, *args, **kwargs): # real signature unknown
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

    def font(self): # real signature unknown; restored from __doc__
        """ font() -> QFont """
        return QFont

    def fontChanged(self, *args, **kwargs): # real signature unknown
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

    def fontDatabaseChanged(self, *args, **kwargs): # real signature unknown
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

    def highDpiScaleFactorRoundingPolicy(self): # real signature unknown; restored from __doc__
        """ highDpiScaleFactorRoundingPolicy() -> Qt.HighDpiScaleFactorRoundingPolicy """
        pass

    def inputMethod(self): # real signature unknown; restored from __doc__
        """ inputMethod() -> Optional[QInputMethod] """
        pass

    def isFallbackSessionManagementEnabled(self): # real signature unknown; restored from __doc__
        """ isFallbackSessionManagementEnabled() -> bool """
        return False

    def isLeftToRight(self): # real signature unknown; restored from __doc__
        """ isLeftToRight() -> bool """
        return False

    def isRightToLeft(self): # real signature unknown; restored from __doc__
        """ isRightToLeft() -> bool """
        return False

    def isSavingSession(self): # real signature unknown; restored from __doc__
        """ isSavingSession(self) -> bool """
        return False

    def isSessionRestored(self): # real signature unknown; restored from __doc__
        """ isSessionRestored(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def keyboardModifiers(self): # real signature unknown; restored from __doc__
        """ keyboardModifiers() -> Qt.KeyboardModifiers """
        pass

    def lastWindowClosed(self, *args, **kwargs): # real signature unknown
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

    def layoutDirection(self): # real signature unknown; restored from __doc__
        """ layoutDirection() -> Qt.LayoutDirection """
        pass

    def layoutDirectionChanged(self, *args, **kwargs): # real signature unknown
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

    def modalWindow(self): # real signature unknown; restored from __doc__
        """ modalWindow() -> Optional[QWindow] """
        pass

    def mouseButtons(self): # real signature unknown; restored from __doc__
        """ mouseButtons() -> Qt.MouseButtons """
        pass

    def notify(self, a0, QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ notify(self, a0: Optional[QObject], a1: Optional[QEvent]) -> bool """
        pass

    def overrideCursor(self): # real signature unknown; restored from __doc__
        """ overrideCursor() -> Optional[QCursor] """
        pass

    def palette(self): # real signature unknown; restored from __doc__
        """ palette() -> QPalette """
        return QPalette

    def paletteChanged(self, *args, **kwargs): # real signature unknown
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

    def platformName(self): # real signature unknown; restored from __doc__
        """ platformName() -> str """
        return ""

    def primaryScreen(self): # real signature unknown; restored from __doc__
        """ primaryScreen() -> Optional[QScreen] """
        pass

    def primaryScreenChanged(self, *args, **kwargs): # real signature unknown
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

    def queryKeyboardModifiers(self): # real signature unknown; restored from __doc__
        """ queryKeyboardModifiers() -> Qt.KeyboardModifiers """
        pass

    def quitOnLastWindowClosed(self): # real signature unknown; restored from __doc__
        """ quitOnLastWindowClosed() -> bool """
        return False

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def restoreOverrideCursor(self): # real signature unknown; restored from __doc__
        """ restoreOverrideCursor() """
        pass

    def saveStateRequest(self, *args, **kwargs): # real signature unknown
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

    def screenAdded(self, *args, **kwargs): # real signature unknown
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

    def screenAt(self, point): # real signature unknown; restored from __doc__
        """ screenAt(point: QPoint) -> Optional[QScreen] """
        pass

    def screenRemoved(self, *args, **kwargs): # real signature unknown
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

    def screens(self): # real signature unknown; restored from __doc__
        """ screens() -> List[QScreen] """
        return []

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def sessionId(self): # real signature unknown; restored from __doc__
        """ sessionId(self) -> str """
        return ""

    def sessionKey(self): # real signature unknown; restored from __doc__
        """ sessionKey(self) -> str """
        return ""

    def setApplicationDisplayName(self, name, p_str=None): # real signature unknown; restored from __doc__
        """ setApplicationDisplayName(name: Optional[str]) """
        pass

    def setDesktopFileName(self, name, p_str=None): # real signature unknown; restored from __doc__
        """ setDesktopFileName(name: Optional[str]) """
        pass

    def setDesktopSettingsAware(self, on): # real signature unknown; restored from __doc__
        """ setDesktopSettingsAware(on: bool) """
        pass

    def setFallbackSessionManagementEnabled(self, a0): # real signature unknown; restored from __doc__
        """ setFallbackSessionManagementEnabled(a0: bool) """
        pass

    def setFont(self, a0): # real signature unknown; restored from __doc__
        """ setFont(a0: QFont) """
        pass

    def setHighDpiScaleFactorRoundingPolicy(self, policy): # real signature unknown; restored from __doc__
        """ setHighDpiScaleFactorRoundingPolicy(policy: Qt.HighDpiScaleFactorRoundingPolicy) """
        pass

    def setLayoutDirection(self, direction): # real signature unknown; restored from __doc__
        """ setLayoutDirection(direction: Qt.LayoutDirection) """
        pass

    def setOverrideCursor(self, a0, QCursor=None, Qt_CursorShape=None): # real signature unknown; restored from __doc__
        """ setOverrideCursor(a0: Union[QCursor, Qt.CursorShape]) """
        pass

    def setPalette(self, pal): # real signature unknown; restored from __doc__
        """ setPalette(pal: QPalette) """
        pass

    def setQuitOnLastWindowClosed(self, quit): # real signature unknown; restored from __doc__
        """ setQuitOnLastWindowClosed(quit: bool) """
        pass

    def setWindowIcon(self, icon): # real signature unknown; restored from __doc__
        """ setWindowIcon(icon: QIcon) """
        pass

    def styleHints(self): # real signature unknown; restored from __doc__
        """ styleHints() -> Optional[QStyleHints] """
        pass

    def sync(self): # real signature unknown; restored from __doc__
        """ sync() """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def topLevelAt(self, pos): # real signature unknown; restored from __doc__
        """ topLevelAt(pos: QPoint) -> Optional[QWindow] """
        pass

    def topLevelWindows(self): # real signature unknown; restored from __doc__
        """ topLevelWindows() -> List[QWindow] """
        return []

    def windowIcon(self): # real signature unknown; restored from __doc__
        """ windowIcon() -> QIcon """
        return QIcon

    def __init__(self, argv, p_str=None): # real signature unknown; restored from __doc__
        pass


