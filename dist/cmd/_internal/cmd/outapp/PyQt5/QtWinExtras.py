# encoding: utf-8
# module PyQt5.QtWinExtras
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtWinExtras.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


# no functions
# classes

class QtWin(__sip.simplewrapper):
    # no doc
    def colorizationColor(self): # real signature unknown; restored from __doc__
        """ colorizationColor() -> (QColor, Optional[bool]) """
        pass

    def createMask(self, bitmap): # real signature unknown; restored from __doc__
        """ createMask(bitmap: QBitmap) -> Optional[PyQt5.sip.voidptr] """
        pass

    def disableBlurBehindWindow(self, window, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        disableBlurBehindWindow(window: Optional[QWindow])
        disableBlurBehindWindow(window: Optional[QWidget])
        """
        pass

    def enableBlurBehindWindow(self, window, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        enableBlurBehindWindow(window: Optional[QWindow], region: QRegion)
        enableBlurBehindWindow(window: Optional[QWindow])
        enableBlurBehindWindow(window: Optional[QWidget], region: QRegion)
        enableBlurBehindWindow(window: Optional[QWidget])
        """
        pass

    def errorStringFromHresult(self, hresult): # real signature unknown; restored from __doc__
        """ errorStringFromHresult(hresult: int) -> str """
        return ""

    def extendFrameIntoClientArea(self, window, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        extendFrameIntoClientArea(window: Optional[QWindow], left: int, top: int, right: int, bottom: int)
        extendFrameIntoClientArea(window: Optional[QWindow], margins: QMargins)
        extendFrameIntoClientArea(window: Optional[QWidget], margins: QMargins)
        extendFrameIntoClientArea(window: Optional[QWidget], left: int, top: int, right: int, bottom: int)
        """
        pass

    def fromHBITMAP(self, bitmap, PyQt5_sip_voidptr=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ fromHBITMAP(bitmap: Optional[PyQt5.sip.voidptr], format: QtWin.HBitmapFormat = QtWin.HBitmapNoAlpha) -> QPixmap """
        pass

    def fromHICON(self, icon, PyQt5_sip_voidptr=None): # real signature unknown; restored from __doc__
        """ fromHICON(icon: Optional[PyQt5.sip.voidptr]) -> QPixmap """
        pass

    def fromHRGN(self, hrgn, PyQt5_sip_voidptr=None): # real signature unknown; restored from __doc__
        """ fromHRGN(hrgn: Optional[PyQt5.sip.voidptr]) -> QRegion """
        pass

    def imageFromHBITMAP(self, hdc, PyQt5_sip_voidptr=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ imageFromHBITMAP(hdc: Optional[PyQt5.sip.voidptr], bitmap: Optional[PyQt5.sip.voidptr], width: int, height: int) -> QImage """
        pass

    def isCompositionEnabled(self): # real signature unknown; restored from __doc__
        """ isCompositionEnabled() -> bool """
        return False

    def isCompositionOpaque(self): # real signature unknown; restored from __doc__
        """ isCompositionOpaque() -> bool """
        return False

    def isWindowExcludedFromPeek(self, window, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        isWindowExcludedFromPeek(window: Optional[QWindow]) -> bool
        isWindowExcludedFromPeek(window: Optional[QWidget]) -> bool
        """
        return False

    def isWindowPeekDisallowed(self, window, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        isWindowPeekDisallowed(window: Optional[QWindow]) -> bool
        isWindowPeekDisallowed(window: Optional[QWidget]) -> bool
        """
        return False

    def markFullscreenWindow(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        markFullscreenWindow(a0: Optional[QWindow], fullscreen: bool = True)
        markFullscreenWindow(window: Optional[QWidget], fullscreen: bool = True)
        """
        pass

    def realColorizationColor(self): # real signature unknown; restored from __doc__
        """ realColorizationColor() -> QColor """
        pass

    def resetExtendedFrame(self, window, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        resetExtendedFrame(window: Optional[QWindow])
        resetExtendedFrame(window: Optional[QWidget])
        """
        pass

    def setCompositionEnabled(self, enabled): # real signature unknown; restored from __doc__
        """ setCompositionEnabled(enabled: bool) """
        pass

    def setCurrentProcessExplicitAppUserModelID(self, id, p_str=None): # real signature unknown; restored from __doc__
        """ setCurrentProcessExplicitAppUserModelID(id: Optional[str]) """
        pass

    def setWindowDisallowPeek(self, window, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setWindowDisallowPeek(window: Optional[QWindow], disallow: bool)
        setWindowDisallowPeek(window: Optional[QWidget], disallow: bool)
        """
        pass

    def setWindowExcludedFromPeek(self, window, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setWindowExcludedFromPeek(window: Optional[QWindow], exclude: bool)
        setWindowExcludedFromPeek(window: Optional[QWidget], exclude: bool)
        """
        pass

    def setWindowFlip3DPolicy(self, window, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setWindowFlip3DPolicy(window: Optional[QWindow], policy: QtWin.WindowFlip3DPolicy)
        setWindowFlip3DPolicy(window: Optional[QWidget], policy: QtWin.WindowFlip3DPolicy)
        """
        pass

    def stringFromHresult(self, hresult): # real signature unknown; restored from __doc__
        """ stringFromHresult(hresult: int) -> str """
        return ""

    def taskbarActivateTab(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        taskbarActivateTab(a0: Optional[QWindow])
        taskbarActivateTab(window: Optional[QWidget])
        """
        pass

    def taskbarActivateTabAlt(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        taskbarActivateTabAlt(a0: Optional[QWindow])
        taskbarActivateTabAlt(window: Optional[QWidget])
        """
        pass

    def taskbarAddTab(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        taskbarAddTab(a0: Optional[QWindow])
        taskbarAddTab(window: Optional[QWidget])
        """
        pass

    def taskbarDeleteTab(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        taskbarDeleteTab(a0: Optional[QWindow])
        taskbarDeleteTab(window: Optional[QWidget])
        """
        pass

    def toHBITMAP(self, p, format=None): # real signature unknown; restored from __doc__
        """ toHBITMAP(p: QPixmap, format: QtWin.HBitmapFormat = QtWin.HBitmapNoAlpha) -> Optional[PyQt5.sip.voidptr] """
        pass

    def toHICON(self, p): # real signature unknown; restored from __doc__
        """ toHICON(p: QPixmap) -> Optional[PyQt5.sip.voidptr] """
        pass

    def toHRGN(self, region): # real signature unknown; restored from __doc__
        """ toHRGN(region: QRegion) -> Optional[PyQt5.sip.voidptr] """
        pass

    def windowFlip3DPolicy(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        windowFlip3DPolicy(a0: Optional[QWindow]) -> QtWin.WindowFlip3DPolicy
        windowFlip3DPolicy(window: Optional[QWidget]) -> QtWin.WindowFlip3DPolicy
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    FlipDefault = 0
    FlipExcludeAbove = 2
    FlipExcludeBelow = 1
    HBitmapAlpha = 2
    HBitmapNoAlpha = 0
    HBitmapPremultipliedAlpha = 1


class QWinJumpList(__PyQt5_QtCore.QObject):
    """ QWinJumpList(parent: Optional[QObject] = None) """
    def addCategory(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        addCategory(self, category: Optional[QWinJumpListCategory])
        addCategory(self, title: Optional[str], items: Iterable[QWinJumpListItem] = []) -> Optional[QWinJumpListCategory]
        """
        pass

    def categories(self): # real signature unknown; restored from __doc__
        """ categories(self) -> List[QWinJumpListCategory] """
        return []

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

    def frequent(self): # real signature unknown; restored from __doc__
        """ frequent(self) -> Optional[QWinJumpListCategory] """
        pass

    def identifier(self): # real signature unknown; restored from __doc__
        """ identifier(self) -> str """
        return ""

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def recent(self): # real signature unknown; restored from __doc__
        """ recent(self) -> Optional[QWinJumpListCategory] """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setIdentifier(self, identifier, p_str=None): # real signature unknown; restored from __doc__
        """ setIdentifier(self, identifier: Optional[str]) """
        pass

    def tasks(self): # real signature unknown; restored from __doc__
        """ tasks(self) -> Optional[QWinJumpListCategory] """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent, QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass


class QWinJumpListCategory(__sip.wrapper):
    """ QWinJumpListCategory(title: Optional[str] = '') """
    def addDestination(self, filePath, p_str=None): # real signature unknown; restored from __doc__
        """ addDestination(self, filePath: Optional[str]) -> Optional[QWinJumpListItem] """
        pass

    def addItem(self, item, QWinJumpListItem=None): # real signature unknown; restored from __doc__
        """ addItem(self, item: Optional[QWinJumpListItem]) """
        pass

    def addLink(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        addLink(self, title: Optional[str], executablePath: Optional[str], arguments: Iterable[Optional[str]] = []) -> Optional[QWinJumpListItem]
        addLink(self, icon: QIcon, title: Optional[str], executablePath: Optional[str], arguments: Iterable[Optional[str]] = []) -> Optional[QWinJumpListItem]
        """
        pass

    def addSeparator(self): # real signature unknown; restored from __doc__
        """ addSeparator(self) -> Optional[QWinJumpListItem] """
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def count(self): # real signature unknown; restored from __doc__
        """ count(self) -> int """
        return 0

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ isEmpty(self) -> bool """
        return False

    def isVisible(self): # real signature unknown; restored from __doc__
        """ isVisible(self) -> bool """
        return False

    def items(self): # real signature unknown; restored from __doc__
        """ items(self) -> List[QWinJumpListItem] """
        return []

    def setTitle(self, title, p_str=None): # real signature unknown; restored from __doc__
        """ setTitle(self, title: Optional[str]) """
        pass

    def setVisible(self, visible): # real signature unknown; restored from __doc__
        """ setVisible(self, visible: bool) """
        pass

    def title(self): # real signature unknown; restored from __doc__
        """ title(self) -> str """
        return ""

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> QWinJumpListCategory.Type """
        pass

    def __init__(self, title, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    Custom = 0
    Frequent = 2
    Recent = 1
    Tasks = 3


class QWinJumpListItem(__sip.wrapper):
    """ QWinJumpListItem(type: QWinJumpListItem.Type) """
    def arguments(self): # real signature unknown; restored from __doc__
        """ arguments(self) -> List[str] """
        return []

    def description(self): # real signature unknown; restored from __doc__
        """ description(self) -> str """
        return ""

    def filePath(self): # real signature unknown; restored from __doc__
        """ filePath(self) -> str """
        return ""

    def icon(self): # real signature unknown; restored from __doc__
        """ icon(self) -> QIcon """
        pass

    def setArguments(self, arguments, Optional=None, p_str=None): # real signature unknown; restored from __doc__
        """ setArguments(self, arguments: Iterable[Optional[str]]) """
        pass

    def setDescription(self, description, p_str=None): # real signature unknown; restored from __doc__
        """ setDescription(self, description: Optional[str]) """
        pass

    def setFilePath(self, filePath, p_str=None): # real signature unknown; restored from __doc__
        """ setFilePath(self, filePath: Optional[str]) """
        pass

    def setIcon(self, icon): # real signature unknown; restored from __doc__
        """ setIcon(self, icon: QIcon) """
        pass

    def setTitle(self, title, p_str=None): # real signature unknown; restored from __doc__
        """ setTitle(self, title: Optional[str]) """
        pass

    def setType(self, type): # real signature unknown; restored from __doc__
        """ setType(self, type: QWinJumpListItem.Type) """
        pass

    def setWorkingDirectory(self, workingDirectory, p_str=None): # real signature unknown; restored from __doc__
        """ setWorkingDirectory(self, workingDirectory: Optional[str]) """
        pass

    def title(self): # real signature unknown; restored from __doc__
        """ title(self) -> str """
        return ""

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> QWinJumpListItem.Type """
        pass

    def workingDirectory(self): # real signature unknown; restored from __doc__
        """ workingDirectory(self) -> str """
        return ""

    def __init__(self, type): # real signature unknown; restored from __doc__
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    Destination = 0
    Link = 1
    Separator = 2


class QWinTaskbarButton(__PyQt5_QtCore.QObject):
    """ QWinTaskbarButton(parent: Optional[QObject] = None) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def clearOverlayIcon(self): # real signature unknown; restored from __doc__
        """ clearOverlayIcon(self) """
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def eventFilter(self, a0, QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ eventFilter(self, a0: Optional[QObject], a1: Optional[QEvent]) -> bool """
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def overlayAccessibleDescription(self): # real signature unknown; restored from __doc__
        """ overlayAccessibleDescription(self) -> str """
        return ""

    def overlayIcon(self): # real signature unknown; restored from __doc__
        """ overlayIcon(self) -> QIcon """
        pass

    def progress(self): # real signature unknown; restored from __doc__
        """ progress(self) -> Optional[QWinTaskbarProgress] """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setOverlayAccessibleDescription(self, description, p_str=None): # real signature unknown; restored from __doc__
        """ setOverlayAccessibleDescription(self, description: Optional[str]) """
        pass

    def setOverlayIcon(self, icon): # real signature unknown; restored from __doc__
        """ setOverlayIcon(self, icon: QIcon) """
        pass

    def setWindow(self, window, QWindow=None): # real signature unknown; restored from __doc__
        """ setWindow(self, window: Optional[QWindow]) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def window(self): # real signature unknown; restored from __doc__
        """ window(self) -> Optional[QWindow] """
        pass

    def __init__(self, parent, QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass


class QWinTaskbarProgress(__PyQt5_QtCore.QObject):
    """ QWinTaskbarProgress(parent: Optional[QObject] = None) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def hide(self): # real signature unknown; restored from __doc__
        """ hide(self) """
        pass

    def isPaused(self): # real signature unknown; restored from __doc__
        """ isPaused(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def isStopped(self): # real signature unknown; restored from __doc__
        """ isStopped(self) -> bool """
        return False

    def isVisible(self): # real signature unknown; restored from __doc__
        """ isVisible(self) -> bool """
        return False

    def maximum(self): # real signature unknown; restored from __doc__
        """ maximum(self) -> int """
        return 0

    def maximumChanged(self, *args, **kwargs): # real signature unknown
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

    def minimum(self): # real signature unknown; restored from __doc__
        """ minimum(self) -> int """
        return 0

    def minimumChanged(self, *args, **kwargs): # real signature unknown
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

    def pause(self): # real signature unknown; restored from __doc__
        """ pause(self) """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def reset(self): # real signature unknown; restored from __doc__
        """ reset(self) """
        pass

    def resume(self): # real signature unknown; restored from __doc__
        """ resume(self) """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setMaximum(self, maximum): # real signature unknown; restored from __doc__
        """ setMaximum(self, maximum: int) """
        pass

    def setMinimum(self, minimum): # real signature unknown; restored from __doc__
        """ setMinimum(self, minimum: int) """
        pass

    def setPaused(self, paused): # real signature unknown; restored from __doc__
        """ setPaused(self, paused: bool) """
        pass

    def setRange(self, minimum, maximum): # real signature unknown; restored from __doc__
        """ setRange(self, minimum: int, maximum: int) """
        pass

    def setValue(self, value): # real signature unknown; restored from __doc__
        """ setValue(self, value: int) """
        pass

    def setVisible(self, visible): # real signature unknown; restored from __doc__
        """ setVisible(self, visible: bool) """
        pass

    def show(self): # real signature unknown; restored from __doc__
        """ show(self) """
        pass

    def stop(self): # real signature unknown; restored from __doc__
        """ stop(self) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def value(self): # real signature unknown; restored from __doc__
        """ value(self) -> int """
        return 0

    def valueChanged(self, *args, **kwargs): # real signature unknown
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

    def visibilityChanged(self, *args, **kwargs): # real signature unknown
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


class QWinThumbnailToolBar(__PyQt5_QtCore.QObject):
    """ QWinThumbnailToolBar(parent: Optional[QObject] = None) """
    def addButton(self, button, QWinThumbnailToolButton=None): # real signature unknown; restored from __doc__
        """ addButton(self, button: Optional[QWinThumbnailToolButton]) """
        pass

    def buttons(self): # real signature unknown; restored from __doc__
        """ buttons(self) -> List[QWinThumbnailToolButton] """
        return []

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def count(self): # real signature unknown; restored from __doc__
        """ count(self) -> int """
        return 0

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def iconicLivePreviewPixmap(self): # real signature unknown; restored from __doc__
        """ iconicLivePreviewPixmap(self) -> QPixmap """
        pass

    def iconicLivePreviewPixmapRequested(self, *args, **kwargs): # real signature unknown
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

    def iconicPixmapNotificationsEnabled(self): # real signature unknown; restored from __doc__
        """ iconicPixmapNotificationsEnabled(self) -> bool """
        return False

    def iconicThumbnailPixmap(self): # real signature unknown; restored from __doc__
        """ iconicThumbnailPixmap(self) -> QPixmap """
        pass

    def iconicThumbnailPixmapRequested(self, *args, **kwargs): # real signature unknown
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

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def removeButton(self, button, QWinThumbnailToolButton=None): # real signature unknown; restored from __doc__
        """ removeButton(self, button: Optional[QWinThumbnailToolButton]) """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setButtons(self, buttons, QWinThumbnailToolButton=None): # real signature unknown; restored from __doc__
        """ setButtons(self, buttons: Iterable[QWinThumbnailToolButton]) """
        pass

    def setIconicLivePreviewPixmap(self, a0): # real signature unknown; restored from __doc__
        """ setIconicLivePreviewPixmap(self, a0: QPixmap) """
        pass

    def setIconicPixmapNotificationsEnabled(self, enabled): # real signature unknown; restored from __doc__
        """ setIconicPixmapNotificationsEnabled(self, enabled: bool) """
        pass

    def setIconicThumbnailPixmap(self, a0): # real signature unknown; restored from __doc__
        """ setIconicThumbnailPixmap(self, a0: QPixmap) """
        pass

    def setWindow(self, window, QWindow=None): # real signature unknown; restored from __doc__
        """ setWindow(self, window: Optional[QWindow]) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def window(self): # real signature unknown; restored from __doc__
        """ window(self) -> Optional[QWindow] """
        pass

    def __init__(self, parent, QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass


class QWinThumbnailToolButton(__PyQt5_QtCore.QObject):
    """ QWinThumbnailToolButton(parent: Optional[QObject] = None) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def click(self): # real signature unknown; restored from __doc__
        """ click(self) """
        pass

    def clicked(self, *args, **kwargs): # real signature unknown
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

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def dismissOnClick(self): # real signature unknown; restored from __doc__
        """ dismissOnClick(self) -> bool """
        return False

    def icon(self): # real signature unknown; restored from __doc__
        """ icon(self) -> QIcon """
        pass

    def isEnabled(self): # real signature unknown; restored from __doc__
        """ isEnabled(self) -> bool """
        return False

    def isFlat(self): # real signature unknown; restored from __doc__
        """ isFlat(self) -> bool """
        return False

    def isInteractive(self): # real signature unknown; restored from __doc__
        """ isInteractive(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def isVisible(self): # real signature unknown; restored from __doc__
        """ isVisible(self) -> bool """
        return False

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setDismissOnClick(self, dismiss): # real signature unknown; restored from __doc__
        """ setDismissOnClick(self, dismiss: bool) """
        pass

    def setEnabled(self, enabled): # real signature unknown; restored from __doc__
        """ setEnabled(self, enabled: bool) """
        pass

    def setFlat(self, flat): # real signature unknown; restored from __doc__
        """ setFlat(self, flat: bool) """
        pass

    def setIcon(self, icon): # real signature unknown; restored from __doc__
        """ setIcon(self, icon: QIcon) """
        pass

    def setInteractive(self, interactive): # real signature unknown; restored from __doc__
        """ setInteractive(self, interactive: bool) """
        pass

    def setToolTip(self, toolTip, p_str=None): # real signature unknown; restored from __doc__
        """ setToolTip(self, toolTip: Optional[str]) """
        pass

    def setVisible(self, visible): # real signature unknown; restored from __doc__
        """ setVisible(self, visible: bool) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def toolTip(self): # real signature unknown; restored from __doc__
        """ toolTip(self) -> str """
        return ""

    def __init__(self, parent, QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass


# variables with complex values



