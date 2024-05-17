# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


from .QSurface import QSurface

class QWindow(__PyQt5_QtCore.QObject, QSurface):
    """
    QWindow(screen: Optional[QScreen] = None)
    QWindow(parent: Optional[QWindow])
    """
    def activeChanged(self, *args, **kwargs): # real signature unknown
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

    def alert(self, msec): # real signature unknown; restored from __doc__
        """ alert(self, msec: int) """
        pass

    def baseSize(self): # real signature unknown; restored from __doc__
        """ baseSize(self) -> QSize """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def close(self): # real signature unknown; restored from __doc__
        """ close(self) -> bool """
        return False

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def contentOrientation(self): # real signature unknown; restored from __doc__
        """ contentOrientation(self) -> Qt.ScreenOrientation """
        pass

    def contentOrientationChanged(self, *args, **kwargs): # real signature unknown
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

    def create(self): # real signature unknown; restored from __doc__
        """ create(self) """
        pass

    def cursor(self): # real signature unknown; restored from __doc__
        """ cursor(self) -> QCursor """
        return QCursor

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def destroy(self): # real signature unknown; restored from __doc__
        """ destroy(self) """
        pass

    def devicePixelRatio(self): # real signature unknown; restored from __doc__
        """ devicePixelRatio(self) -> float """
        return 0.0

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, a0, QEvent=None): # real signature unknown; restored from __doc__
        """ event(self, a0: Optional[QEvent]) -> bool """
        return False

    def exposeEvent(self, a0, QExposeEvent=None): # real signature unknown; restored from __doc__
        """ exposeEvent(self, a0: Optional[QExposeEvent]) """
        pass

    def filePath(self): # real signature unknown; restored from __doc__
        """ filePath(self) -> str """
        return ""

    def flags(self): # real signature unknown; restored from __doc__
        """ flags(self) -> Qt.WindowFlags """
        pass

    def focusInEvent(self, a0, QFocusEvent=None): # real signature unknown; restored from __doc__
        """ focusInEvent(self, a0: Optional[QFocusEvent]) """
        pass

    def focusObject(self): # real signature unknown; restored from __doc__
        """ focusObject(self) -> Optional[QObject] """
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

    def focusOutEvent(self, a0, QFocusEvent=None): # real signature unknown; restored from __doc__
        """ focusOutEvent(self, a0: Optional[QFocusEvent]) """
        pass

    def format(self): # real signature unknown; restored from __doc__
        """ format(self) -> QSurfaceFormat """
        return QSurfaceFormat

    def frameGeometry(self): # real signature unknown; restored from __doc__
        """ frameGeometry(self) -> QRect """
        pass

    def frameMargins(self): # real signature unknown; restored from __doc__
        """ frameMargins(self) -> QMargins """
        pass

    def framePosition(self): # real signature unknown; restored from __doc__
        """ framePosition(self) -> QPoint """
        pass

    def fromWinId(self, id): # real signature unknown; restored from __doc__
        """ fromWinId(id: PyQt5.sip.voidptr) -> Optional[QWindow] """
        pass

    def geometry(self): # real signature unknown; restored from __doc__
        """ geometry(self) -> QRect """
        pass

    def height(self): # real signature unknown; restored from __doc__
        """ height(self) -> int """
        return 0

    def heightChanged(self, *args, **kwargs): # real signature unknown
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

    def hide(self): # real signature unknown; restored from __doc__
        """ hide(self) """
        pass

    def hideEvent(self, a0, QHideEvent=None): # real signature unknown; restored from __doc__
        """ hideEvent(self, a0: Optional[QHideEvent]) """
        pass

    def icon(self): # real signature unknown; restored from __doc__
        """ icon(self) -> QIcon """
        return QIcon

    def isActive(self): # real signature unknown; restored from __doc__
        """ isActive(self) -> bool """
        return False

    def isAncestorOf(self, child, QWindow=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ isAncestorOf(self, child: Optional[QWindow], mode: QWindow.AncestorMode = QWindow.IncludeTransients) -> bool """
        pass

    def isExposed(self): # real signature unknown; restored from __doc__
        """ isExposed(self) -> bool """
        return False

    def isModal(self): # real signature unknown; restored from __doc__
        """ isModal(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def isTopLevel(self): # real signature unknown; restored from __doc__
        """ isTopLevel(self) -> bool """
        return False

    def isVisible(self): # real signature unknown; restored from __doc__
        """ isVisible(self) -> bool """
        return False

    def keyPressEvent(self, a0, QKeyEvent=None): # real signature unknown; restored from __doc__
        """ keyPressEvent(self, a0: Optional[QKeyEvent]) """
        pass

    def keyReleaseEvent(self, a0, QKeyEvent=None): # real signature unknown; restored from __doc__
        """ keyReleaseEvent(self, a0: Optional[QKeyEvent]) """
        pass

    def lower(self): # real signature unknown; restored from __doc__
        """ lower(self) """
        pass

    def mapFromGlobal(self, pos): # real signature unknown; restored from __doc__
        """ mapFromGlobal(self, pos: QPoint) -> QPoint """
        pass

    def mapToGlobal(self, pos): # real signature unknown; restored from __doc__
        """ mapToGlobal(self, pos: QPoint) -> QPoint """
        pass

    def mask(self): # real signature unknown; restored from __doc__
        """ mask(self) -> QRegion """
        return QRegion

    def maximumHeight(self): # real signature unknown; restored from __doc__
        """ maximumHeight(self) -> int """
        return 0

    def maximumHeightChanged(self, *args, **kwargs): # real signature unknown
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

    def maximumSize(self): # real signature unknown; restored from __doc__
        """ maximumSize(self) -> QSize """
        pass

    def maximumWidth(self): # real signature unknown; restored from __doc__
        """ maximumWidth(self) -> int """
        return 0

    def maximumWidthChanged(self, *args, **kwargs): # real signature unknown
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

    def minimumHeight(self): # real signature unknown; restored from __doc__
        """ minimumHeight(self) -> int """
        return 0

    def minimumHeightChanged(self, *args, **kwargs): # real signature unknown
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

    def minimumSize(self): # real signature unknown; restored from __doc__
        """ minimumSize(self) -> QSize """
        pass

    def minimumWidth(self): # real signature unknown; restored from __doc__
        """ minimumWidth(self) -> int """
        return 0

    def minimumWidthChanged(self, *args, **kwargs): # real signature unknown
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

    def modality(self): # real signature unknown; restored from __doc__
        """ modality(self) -> Qt.WindowModality """
        pass

    def modalityChanged(self, *args, **kwargs): # real signature unknown
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

    def mouseDoubleClickEvent(self, a0, QMouseEvent=None): # real signature unknown; restored from __doc__
        """ mouseDoubleClickEvent(self, a0: Optional[QMouseEvent]) """
        pass

    def mouseMoveEvent(self, a0, QMouseEvent=None): # real signature unknown; restored from __doc__
        """ mouseMoveEvent(self, a0: Optional[QMouseEvent]) """
        pass

    def mousePressEvent(self, a0, QMouseEvent=None): # real signature unknown; restored from __doc__
        """ mousePressEvent(self, a0: Optional[QMouseEvent]) """
        pass

    def mouseReleaseEvent(self, a0, QMouseEvent=None): # real signature unknown; restored from __doc__
        """ mouseReleaseEvent(self, a0: Optional[QMouseEvent]) """
        pass

    def moveEvent(self, a0, QMoveEvent=None): # real signature unknown; restored from __doc__
        """ moveEvent(self, a0: Optional[QMoveEvent]) """
        pass

    def opacity(self): # real signature unknown; restored from __doc__
        """ opacity(self) -> float """
        return 0.0

    def opacityChanged(self, *args, **kwargs): # real signature unknown
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

    def parent(self, mode=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        parent(self) -> Optional[QWindow]
        parent(self, mode: QWindow.AncestorMode) -> Optional[QWindow]
        """
        pass

    def position(self): # real signature unknown; restored from __doc__
        """ position(self) -> QPoint """
        pass

    def raise_(self): # real signature unknown; restored from __doc__
        """ raise_(self) """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def reportContentOrientationChange(self, orientation): # real signature unknown; restored from __doc__
        """ reportContentOrientationChange(self, orientation: Qt.ScreenOrientation) """
        pass

    def requestActivate(self): # real signature unknown; restored from __doc__
        """ requestActivate(self) """
        pass

    def requestedFormat(self): # real signature unknown; restored from __doc__
        """ requestedFormat(self) -> QSurfaceFormat """
        return QSurfaceFormat

    def requestUpdate(self): # real signature unknown; restored from __doc__
        """ requestUpdate(self) """
        pass

    def resize(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        resize(self, newSize: QSize)
        resize(self, w: int, h: int)
        """
        pass

    def resizeEvent(self, a0, QResizeEvent=None): # real signature unknown; restored from __doc__
        """ resizeEvent(self, a0: Optional[QResizeEvent]) """
        pass

    def screen(self): # real signature unknown; restored from __doc__
        """ screen(self) -> Optional[QScreen] """
        pass

    def screenChanged(self, *args, **kwargs): # real signature unknown
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

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setBaseSize(self, size): # real signature unknown; restored from __doc__
        """ setBaseSize(self, size: QSize) """
        pass

    def setCursor(self, a0, QCursor=None, Qt_CursorShape=None): # real signature unknown; restored from __doc__
        """ setCursor(self, a0: Union[QCursor, Qt.CursorShape]) """
        pass

    def setFilePath(self, filePath, p_str=None): # real signature unknown; restored from __doc__
        """ setFilePath(self, filePath: Optional[str]) """
        pass

    def setFlag(self, a0, on=True): # real signature unknown; restored from __doc__
        """ setFlag(self, a0: Qt.WindowType, on: bool = True) """
        pass

    def setFlags(self, flags, Qt_WindowFlags=None, Qt_WindowType=None): # real signature unknown; restored from __doc__
        """ setFlags(self, flags: Union[Qt.WindowFlags, Qt.WindowType]) """
        pass

    def setFormat(self, format): # real signature unknown; restored from __doc__
        """ setFormat(self, format: QSurfaceFormat) """
        pass

    def setFramePosition(self, point): # real signature unknown; restored from __doc__
        """ setFramePosition(self, point: QPoint) """
        pass

    def setGeometry(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setGeometry(self, posx: int, posy: int, w: int, h: int)
        setGeometry(self, rect: QRect)
        """
        pass

    def setHeight(self, arg): # real signature unknown; restored from __doc__
        """ setHeight(self, arg: int) """
        pass

    def setIcon(self, icon): # real signature unknown; restored from __doc__
        """ setIcon(self, icon: QIcon) """
        pass

    def setKeyboardGrabEnabled(self, grab): # real signature unknown; restored from __doc__
        """ setKeyboardGrabEnabled(self, grab: bool) -> bool """
        return False

    def setMask(self, region): # real signature unknown; restored from __doc__
        """ setMask(self, region: QRegion) """
        pass

    def setMaximumHeight(self, h): # real signature unknown; restored from __doc__
        """ setMaximumHeight(self, h: int) """
        pass

    def setMaximumSize(self, size): # real signature unknown; restored from __doc__
        """ setMaximumSize(self, size: QSize) """
        pass

    def setMaximumWidth(self, w): # real signature unknown; restored from __doc__
        """ setMaximumWidth(self, w: int) """
        pass

    def setMinimumHeight(self, h): # real signature unknown; restored from __doc__
        """ setMinimumHeight(self, h: int) """
        pass

    def setMinimumSize(self, size): # real signature unknown; restored from __doc__
        """ setMinimumSize(self, size: QSize) """
        pass

    def setMinimumWidth(self, w): # real signature unknown; restored from __doc__
        """ setMinimumWidth(self, w: int) """
        pass

    def setModality(self, modality): # real signature unknown; restored from __doc__
        """ setModality(self, modality: Qt.WindowModality) """
        pass

    def setMouseGrabEnabled(self, grab): # real signature unknown; restored from __doc__
        """ setMouseGrabEnabled(self, grab: bool) -> bool """
        return False

    def setOpacity(self, level): # real signature unknown; restored from __doc__
        """ setOpacity(self, level: float) """
        pass

    def setParent(self, parent, QWindow=None): # real signature unknown; restored from __doc__
        """ setParent(self, parent: Optional[QWindow]) """
        pass

    def setPosition(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setPosition(self, pt: QPoint)
        setPosition(self, posx: int, posy: int)
        """
        pass

    def setScreen(self, screen, QScreen=None): # real signature unknown; restored from __doc__
        """ setScreen(self, screen: Optional[QScreen]) """
        pass

    def setSizeIncrement(self, size): # real signature unknown; restored from __doc__
        """ setSizeIncrement(self, size: QSize) """
        pass

    def setSurfaceType(self, surfaceType): # real signature unknown; restored from __doc__
        """ setSurfaceType(self, surfaceType: QSurface.SurfaceType) """
        pass

    def setTitle(self, a0, p_str=None): # real signature unknown; restored from __doc__
        """ setTitle(self, a0: Optional[str]) """
        pass

    def setTransientParent(self, parent, QWindow=None): # real signature unknown; restored from __doc__
        """ setTransientParent(self, parent: Optional[QWindow]) """
        pass

    def setVisibility(self, v): # real signature unknown; restored from __doc__
        """ setVisibility(self, v: QWindow.Visibility) """
        pass

    def setVisible(self, visible): # real signature unknown; restored from __doc__
        """ setVisible(self, visible: bool) """
        pass

    def setWidth(self, arg): # real signature unknown; restored from __doc__
        """ setWidth(self, arg: int) """
        pass

    def setWindowState(self, state): # real signature unknown; restored from __doc__
        """ setWindowState(self, state: Qt.WindowState) """
        pass

    def setWindowStates(self, states, Qt_WindowStates=None, Qt_WindowState=None): # real signature unknown; restored from __doc__
        """ setWindowStates(self, states: Union[Qt.WindowStates, Qt.WindowState]) """
        pass

    def setX(self, arg): # real signature unknown; restored from __doc__
        """ setX(self, arg: int) """
        pass

    def setY(self, arg): # real signature unknown; restored from __doc__
        """ setY(self, arg: int) """
        pass

    def show(self): # real signature unknown; restored from __doc__
        """ show(self) """
        pass

    def showEvent(self, a0, QShowEvent=None): # real signature unknown; restored from __doc__
        """ showEvent(self, a0: Optional[QShowEvent]) """
        pass

    def showFullScreen(self): # real signature unknown; restored from __doc__
        """ showFullScreen(self) """
        pass

    def showMaximized(self): # real signature unknown; restored from __doc__
        """ showMaximized(self) """
        pass

    def showMinimized(self): # real signature unknown; restored from __doc__
        """ showMinimized(self) """
        pass

    def showNormal(self): # real signature unknown; restored from __doc__
        """ showNormal(self) """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ size(self) -> QSize """
        pass

    def sizeIncrement(self): # real signature unknown; restored from __doc__
        """ sizeIncrement(self) -> QSize """
        pass

    def startSystemMove(self): # real signature unknown; restored from __doc__
        """ startSystemMove(self) -> bool """
        return False

    def startSystemResize(self, edges, Qt_Edges=None, Qt_Edge=None): # real signature unknown; restored from __doc__
        """ startSystemResize(self, edges: Union[Qt.Edges, Qt.Edge]) -> bool """
        return False

    def surfaceType(self): # real signature unknown; restored from __doc__
        """ surfaceType(self) -> QSurface.SurfaceType """
        pass

    def tabletEvent(self, a0, QTabletEvent=None): # real signature unknown; restored from __doc__
        """ tabletEvent(self, a0: Optional[QTabletEvent]) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def title(self): # real signature unknown; restored from __doc__
        """ title(self) -> str """
        return ""

    def touchEvent(self, a0, QTouchEvent=None): # real signature unknown; restored from __doc__
        """ touchEvent(self, a0: Optional[QTouchEvent]) """
        pass

    def transientParent(self): # real signature unknown; restored from __doc__
        """ transientParent(self) -> Optional[QWindow] """
        pass

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> Qt.WindowType """
        pass

    def unsetCursor(self): # real signature unknown; restored from __doc__
        """ unsetCursor(self) """
        pass

    def visibility(self): # real signature unknown; restored from __doc__
        """ visibility(self) -> QWindow.Visibility """
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

    def visibleChanged(self, *args, **kwargs): # real signature unknown
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

    def wheelEvent(self, a0, QWheelEvent=None): # real signature unknown; restored from __doc__
        """ wheelEvent(self, a0: Optional[QWheelEvent]) """
        pass

    def width(self): # real signature unknown; restored from __doc__
        """ width(self) -> int """
        return 0

    def widthChanged(self, *args, **kwargs): # real signature unknown
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

    def windowState(self): # real signature unknown; restored from __doc__
        """ windowState(self) -> Qt.WindowState """
        pass

    def windowStateChanged(self, *args, **kwargs): # real signature unknown
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

    def windowStates(self): # real signature unknown; restored from __doc__
        """ windowStates(self) -> Qt.WindowStates """
        pass

    def windowTitleChanged(self, *args, **kwargs): # real signature unknown
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

    def winId(self): # real signature unknown; restored from __doc__
        """ winId(self) -> PyQt5.sip.voidptr """
        pass

    def x(self): # real signature unknown; restored from __doc__
        """ x(self) -> int """
        return 0

    def xChanged(self, *args, **kwargs): # real signature unknown
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

    def y(self): # real signature unknown; restored from __doc__
        """ y(self) -> int """
        return 0

    def yChanged(self, *args, **kwargs): # real signature unknown
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

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    AutomaticVisibility = 1
    ExcludeTransients = 0
    FullScreen = 5
    Hidden = 0
    IncludeTransients = 1
    Maximized = 4
    Minimized = 3
    Windowed = 2


