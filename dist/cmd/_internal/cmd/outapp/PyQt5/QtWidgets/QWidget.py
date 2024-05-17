# encoding: utf-8
# module PyQt5.QtWidgets
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


class QWidget(__PyQt5_QtCore.QObject, __PyQt5_QtGui.QPaintDevice):
    """ QWidget(parent: Optional[QWidget] = None, flags: Union[Qt.WindowFlags, Qt.WindowType] = Qt.WindowFlags()) """
    def acceptDrops(self): # real signature unknown; restored from __doc__
        """ acceptDrops(self) -> bool """
        return False

    def accessibleDescription(self): # real signature unknown; restored from __doc__
        """ accessibleDescription(self) -> str """
        return ""

    def accessibleName(self): # real signature unknown; restored from __doc__
        """ accessibleName(self) -> str """
        return ""

    def actionEvent(self, a0, QActionEvent=None): # real signature unknown; restored from __doc__
        """ actionEvent(self, a0: Optional[QActionEvent]) """
        pass

    def actions(self): # real signature unknown; restored from __doc__
        """ actions(self) -> List[QAction] """
        return []

    def activateWindow(self): # real signature unknown; restored from __doc__
        """ activateWindow(self) """
        pass

    def addAction(self, action, QAction=None): # real signature unknown; restored from __doc__
        """ addAction(self, action: Optional[QAction]) """
        pass

    def addActions(self, actions, QAction=None): # real signature unknown; restored from __doc__
        """ addActions(self, actions: Iterable[QAction]) """
        pass

    def adjustSize(self): # real signature unknown; restored from __doc__
        """ adjustSize(self) """
        pass

    def autoFillBackground(self): # real signature unknown; restored from __doc__
        """ autoFillBackground(self) -> bool """
        return False

    def backgroundRole(self): # real signature unknown; restored from __doc__
        """ backgroundRole(self) -> QPalette.ColorRole """
        pass

    def baseSize(self): # real signature unknown; restored from __doc__
        """ baseSize(self) -> QSize """
        pass

    def changeEvent(self, a0, QEvent=None): # real signature unknown; restored from __doc__
        """ changeEvent(self, a0: Optional[QEvent]) """
        pass

    def childAt(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        childAt(self, p: QPoint) -> Optional[QWidget]
        childAt(self, ax: int, ay: int) -> Optional[QWidget]
        """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def childrenRect(self): # real signature unknown; restored from __doc__
        """ childrenRect(self) -> QRect """
        pass

    def childrenRegion(self): # real signature unknown; restored from __doc__
        """ childrenRegion(self) -> QRegion """
        pass

    def clearFocus(self): # real signature unknown; restored from __doc__
        """ clearFocus(self) """
        pass

    def clearMask(self): # real signature unknown; restored from __doc__
        """ clearMask(self) """
        pass

    def close(self): # real signature unknown; restored from __doc__
        """ close(self) -> bool """
        return False

    def closeEvent(self, a0, QCloseEvent=None): # real signature unknown; restored from __doc__
        """ closeEvent(self, a0: Optional[QCloseEvent]) """
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def contentsMargins(self): # real signature unknown; restored from __doc__
        """ contentsMargins(self) -> QMargins """
        pass

    def contentsRect(self): # real signature unknown; restored from __doc__
        """ contentsRect(self) -> QRect """
        pass

    def contextMenuEvent(self, a0, QContextMenuEvent=None): # real signature unknown; restored from __doc__
        """ contextMenuEvent(self, a0: Optional[QContextMenuEvent]) """
        pass

    def contextMenuPolicy(self): # real signature unknown; restored from __doc__
        """ contextMenuPolicy(self) -> Qt.ContextMenuPolicy """
        pass

    def create(self, window=None, initializeWindow=True, destroyOldWindow=True): # real signature unknown; restored from __doc__
        """ create(self, window: PyQt5.sip.voidptr = None, initializeWindow: bool = True, destroyOldWindow: bool = True) """
        pass

    def createWindowContainer(self, window, QWindow=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ createWindowContainer(window: Optional[QWindow], parent: Optional[QWidget] = None, flags: Union[Qt.WindowFlags, Qt.WindowType] = 0) -> QWidget """
        pass

    def cursor(self): # real signature unknown; restored from __doc__
        """ cursor(self) -> QCursor """
        pass

    def customContextMenuRequested(self, *args, **kwargs): # real signature unknown
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

    def destroy(self, destroyWindow=True, destroySubWindows=True): # real signature unknown; restored from __doc__
        """ destroy(self, destroyWindow: bool = True, destroySubWindows: bool = True) """
        pass

    def devType(self): # real signature unknown; restored from __doc__
        """ devType(self) -> int """
        return 0

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def dragEnterEvent(self, a0, QDragEnterEvent=None): # real signature unknown; restored from __doc__
        """ dragEnterEvent(self, a0: Optional[QDragEnterEvent]) """
        pass

    def dragLeaveEvent(self, a0, QDragLeaveEvent=None): # real signature unknown; restored from __doc__
        """ dragLeaveEvent(self, a0: Optional[QDragLeaveEvent]) """
        pass

    def dragMoveEvent(self, a0, QDragMoveEvent=None): # real signature unknown; restored from __doc__
        """ dragMoveEvent(self, a0: Optional[QDragMoveEvent]) """
        pass

    def dropEvent(self, a0, QDropEvent=None): # real signature unknown; restored from __doc__
        """ dropEvent(self, a0: Optional[QDropEvent]) """
        pass

    def effectiveWinId(self): # real signature unknown; restored from __doc__
        """ effectiveWinId(self) -> PyQt5.sip.voidptr """
        pass

    def ensurePolished(self): # real signature unknown; restored from __doc__
        """ ensurePolished(self) """
        pass

    def enterEvent(self, a0, QEvent=None): # real signature unknown; restored from __doc__
        """ enterEvent(self, a0: Optional[QEvent]) """
        pass

    def event(self, a0, QEvent=None): # real signature unknown; restored from __doc__
        """ event(self, a0: Optional[QEvent]) -> bool """
        return False

    def find(self, a0): # real signature unknown; restored from __doc__
        """ find(a0: PyQt5.sip.voidptr) -> Optional[QWidget] """
        pass

    def focusInEvent(self, a0, QFocusEvent=None): # real signature unknown; restored from __doc__
        """ focusInEvent(self, a0: Optional[QFocusEvent]) """
        pass

    def focusNextChild(self): # real signature unknown; restored from __doc__
        """ focusNextChild(self) -> bool """
        return False

    def focusNextPrevChild(self, next): # real signature unknown; restored from __doc__
        """ focusNextPrevChild(self, next: bool) -> bool """
        return False

    def focusOutEvent(self, a0, QFocusEvent=None): # real signature unknown; restored from __doc__
        """ focusOutEvent(self, a0: Optional[QFocusEvent]) """
        pass

    def focusPolicy(self): # real signature unknown; restored from __doc__
        """ focusPolicy(self) -> Qt.FocusPolicy """
        pass

    def focusPreviousChild(self): # real signature unknown; restored from __doc__
        """ focusPreviousChild(self) -> bool """
        return False

    def focusProxy(self): # real signature unknown; restored from __doc__
        """ focusProxy(self) -> Optional[QWidget] """
        pass

    def focusWidget(self): # real signature unknown; restored from __doc__
        """ focusWidget(self) -> Optional[QWidget] """
        pass

    def font(self): # real signature unknown; restored from __doc__
        """ font(self) -> QFont """
        pass

    def fontInfo(self): # real signature unknown; restored from __doc__
        """ fontInfo(self) -> QFontInfo """
        pass

    def fontMetrics(self): # real signature unknown; restored from __doc__
        """ fontMetrics(self) -> QFontMetrics """
        pass

    def foregroundRole(self): # real signature unknown; restored from __doc__
        """ foregroundRole(self) -> QPalette.ColorRole """
        pass

    def frameGeometry(self): # real signature unknown; restored from __doc__
        """ frameGeometry(self) -> QRect """
        pass

    def frameSize(self): # real signature unknown; restored from __doc__
        """ frameSize(self) -> QSize """
        pass

    def geometry(self): # real signature unknown; restored from __doc__
        """ geometry(self) -> QRect """
        pass

    def getContentsMargins(self): # real signature unknown; restored from __doc__
        """ getContentsMargins(self) -> (Optional[int], Optional[int], Optional[int], Optional[int]) """
        pass

    def grab(self, rectangle=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ grab(self, rectangle: QRect = QRect(QPoint(0, 0), QSize(-1, -1))) -> QPixmap """
        pass

    def grabGesture(self, type, flags, Qt_GestureFlags=None, Qt_GestureFlag=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ grabGesture(self, type: Qt.GestureType, flags: Union[Qt.GestureFlags, Qt.GestureFlag] = Qt.GestureFlags()) """
        pass

    def grabKeyboard(self): # real signature unknown; restored from __doc__
        """ grabKeyboard(self) """
        pass

    def grabMouse(self, a0=None, QCursor=None, Qt_CursorShape=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        grabMouse(self)
        grabMouse(self, a0: Union[QCursor, Qt.CursorShape])
        """
        pass

    def grabShortcut(self, key, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ grabShortcut(self, key: Union[QKeySequence, QKeySequence.StandardKey, Optional[str], int], context: Qt.ShortcutContext = Qt.WindowShortcut) -> int """
        pass

    def graphicsEffect(self): # real signature unknown; restored from __doc__
        """ graphicsEffect(self) -> Optional[QGraphicsEffect] """
        pass

    def graphicsProxyWidget(self): # real signature unknown; restored from __doc__
        """ graphicsProxyWidget(self) -> Optional[QGraphicsProxyWidget] """
        pass

    def hasFocus(self): # real signature unknown; restored from __doc__
        """ hasFocus(self) -> bool """
        return False

    def hasHeightForWidth(self): # real signature unknown; restored from __doc__
        """ hasHeightForWidth(self) -> bool """
        return False

    def hasMouseTracking(self): # real signature unknown; restored from __doc__
        """ hasMouseTracking(self) -> bool """
        return False

    def hasTabletTracking(self): # real signature unknown; restored from __doc__
        """ hasTabletTracking(self) -> bool """
        return False

    def height(self): # real signature unknown; restored from __doc__
        """ height(self) -> int """
        return 0

    def heightForWidth(self, a0): # real signature unknown; restored from __doc__
        """ heightForWidth(self, a0: int) -> int """
        return 0

    def hide(self): # real signature unknown; restored from __doc__
        """ hide(self) """
        pass

    def hideEvent(self, a0, QHideEvent=None): # real signature unknown; restored from __doc__
        """ hideEvent(self, a0: Optional[QHideEvent]) """
        pass

    def initPainter(self, painter, QPainter=None): # real signature unknown; restored from __doc__
        """ initPainter(self, painter: Optional[QPainter]) """
        pass

    def inputMethodEvent(self, a0, QInputMethodEvent=None): # real signature unknown; restored from __doc__
        """ inputMethodEvent(self, a0: Optional[QInputMethodEvent]) """
        pass

    def inputMethodHints(self): # real signature unknown; restored from __doc__
        """ inputMethodHints(self) -> Qt.InputMethodHints """
        pass

    def inputMethodQuery(self, a0): # real signature unknown; restored from __doc__
        """ inputMethodQuery(self, a0: Qt.InputMethodQuery) -> Any """
        pass

    def insertAction(self, before, QAction=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ insertAction(self, before: Optional[QAction], action: Optional[QAction]) """
        pass

    def insertActions(self, before, QAction=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ insertActions(self, before: Optional[QAction], actions: Iterable[QAction]) """
        pass

    def isActiveWindow(self): # real signature unknown; restored from __doc__
        """ isActiveWindow(self) -> bool """
        return False

    def isAncestorOf(self, child, QWidget=None): # real signature unknown; restored from __doc__
        """ isAncestorOf(self, child: Optional[QWidget]) -> bool """
        return False

    def isEnabled(self): # real signature unknown; restored from __doc__
        """ isEnabled(self) -> bool """
        return False

    def isEnabledTo(self, a0, QWidget=None): # real signature unknown; restored from __doc__
        """ isEnabledTo(self, a0: Optional[QWidget]) -> bool """
        return False

    def isFullScreen(self): # real signature unknown; restored from __doc__
        """ isFullScreen(self) -> bool """
        return False

    def isHidden(self): # real signature unknown; restored from __doc__
        """ isHidden(self) -> bool """
        return False

    def isLeftToRight(self): # real signature unknown; restored from __doc__
        """ isLeftToRight(self) -> bool """
        return False

    def isMaximized(self): # real signature unknown; restored from __doc__
        """ isMaximized(self) -> bool """
        return False

    def isMinimized(self): # real signature unknown; restored from __doc__
        """ isMinimized(self) -> bool """
        return False

    def isModal(self): # real signature unknown; restored from __doc__
        """ isModal(self) -> bool """
        return False

    def isRightToLeft(self): # real signature unknown; restored from __doc__
        """ isRightToLeft(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def isVisible(self): # real signature unknown; restored from __doc__
        """ isVisible(self) -> bool """
        return False

    def isVisibleTo(self, a0, QWidget=None): # real signature unknown; restored from __doc__
        """ isVisibleTo(self, a0: Optional[QWidget]) -> bool """
        return False

    def isWindow(self): # real signature unknown; restored from __doc__
        """ isWindow(self) -> bool """
        return False

    def isWindowModified(self): # real signature unknown; restored from __doc__
        """ isWindowModified(self) -> bool """
        return False

    def keyboardGrabber(self): # real signature unknown; restored from __doc__
        """ keyboardGrabber() -> Optional[QWidget] """
        pass

    def keyPressEvent(self, a0, QKeyEvent=None): # real signature unknown; restored from __doc__
        """ keyPressEvent(self, a0: Optional[QKeyEvent]) """
        pass

    def keyReleaseEvent(self, a0, QKeyEvent=None): # real signature unknown; restored from __doc__
        """ keyReleaseEvent(self, a0: Optional[QKeyEvent]) """
        pass

    def layout(self): # real signature unknown; restored from __doc__
        """ layout(self) -> Optional[QLayout] """
        pass

    def layoutDirection(self): # real signature unknown; restored from __doc__
        """ layoutDirection(self) -> Qt.LayoutDirection """
        pass

    def leaveEvent(self, a0, QEvent=None): # real signature unknown; restored from __doc__
        """ leaveEvent(self, a0: Optional[QEvent]) """
        pass

    def locale(self): # real signature unknown; restored from __doc__
        """ locale(self) -> QLocale """
        pass

    def lower(self): # real signature unknown; restored from __doc__
        """ lower(self) """
        pass

    def mapFrom(self, a0, QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ mapFrom(self, a0: Optional[QWidget], a1: QPoint) -> QPoint """
        pass

    def mapFromGlobal(self, a0): # real signature unknown; restored from __doc__
        """ mapFromGlobal(self, a0: QPoint) -> QPoint """
        pass

    def mapFromParent(self, a0): # real signature unknown; restored from __doc__
        """ mapFromParent(self, a0: QPoint) -> QPoint """
        pass

    def mapTo(self, a0, QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ mapTo(self, a0: Optional[QWidget], a1: QPoint) -> QPoint """
        pass

    def mapToGlobal(self, a0): # real signature unknown; restored from __doc__
        """ mapToGlobal(self, a0: QPoint) -> QPoint """
        pass

    def mapToParent(self, a0): # real signature unknown; restored from __doc__
        """ mapToParent(self, a0: QPoint) -> QPoint """
        pass

    def mask(self): # real signature unknown; restored from __doc__
        """ mask(self) -> QRegion """
        pass

    def maximumHeight(self): # real signature unknown; restored from __doc__
        """ maximumHeight(self) -> int """
        return 0

    def maximumSize(self): # real signature unknown; restored from __doc__
        """ maximumSize(self) -> QSize """
        pass

    def maximumWidth(self): # real signature unknown; restored from __doc__
        """ maximumWidth(self) -> int """
        return 0

    def metric(self, a0): # real signature unknown; restored from __doc__
        """ metric(self, a0: QPaintDevice.PaintDeviceMetric) -> int """
        return 0

    def minimumHeight(self): # real signature unknown; restored from __doc__
        """ minimumHeight(self) -> int """
        return 0

    def minimumSize(self): # real signature unknown; restored from __doc__
        """ minimumSize(self) -> QSize """
        pass

    def minimumSizeHint(self): # real signature unknown; restored from __doc__
        """ minimumSizeHint(self) -> QSize """
        pass

    def minimumWidth(self): # real signature unknown; restored from __doc__
        """ minimumWidth(self) -> int """
        return 0

    def mouseDoubleClickEvent(self, a0, QMouseEvent=None): # real signature unknown; restored from __doc__
        """ mouseDoubleClickEvent(self, a0: Optional[QMouseEvent]) """
        pass

    def mouseGrabber(self): # real signature unknown; restored from __doc__
        """ mouseGrabber() -> Optional[QWidget] """
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

    def move(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        move(self, a0: QPoint)
        move(self, ax: int, ay: int)
        """
        pass

    def moveEvent(self, a0, QMoveEvent=None): # real signature unknown; restored from __doc__
        """ moveEvent(self, a0: Optional[QMoveEvent]) """
        pass

    def nativeEvent(self, eventType, QByteArray=None, bytes=None, bytearray=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ nativeEvent(self, eventType: Union[QByteArray, bytes, bytearray], message: Optional[PyQt5.sip.voidptr]) -> (bool, Optional[int]) """
        pass

    def nativeParentWidget(self): # real signature unknown; restored from __doc__
        """ nativeParentWidget(self) -> Optional[QWidget] """
        pass

    def nextInFocusChain(self): # real signature unknown; restored from __doc__
        """ nextInFocusChain(self) -> Optional[QWidget] """
        pass

    def normalGeometry(self): # real signature unknown; restored from __doc__
        """ normalGeometry(self) -> QRect """
        pass

    def overrideWindowFlags(self, type, Qt_WindowFlags=None, Qt_WindowType=None): # real signature unknown; restored from __doc__
        """ overrideWindowFlags(self, type: Union[Qt.WindowFlags, Qt.WindowType]) """
        pass

    def overrideWindowState(self, state, Qt_WindowStates=None, Qt_WindowState=None): # real signature unknown; restored from __doc__
        """ overrideWindowState(self, state: Union[Qt.WindowStates, Qt.WindowState]) """
        pass

    def paintEngine(self): # real signature unknown; restored from __doc__
        """ paintEngine(self) -> Optional[QPaintEngine] """
        pass

    def paintEvent(self, a0, QPaintEvent=None): # real signature unknown; restored from __doc__
        """ paintEvent(self, a0: Optional[QPaintEvent]) """
        pass

    def palette(self): # real signature unknown; restored from __doc__
        """ palette(self) -> QPalette """
        pass

    def parentWidget(self): # real signature unknown; restored from __doc__
        """ parentWidget(self) -> Optional[QWidget] """
        pass

    def pos(self): # real signature unknown; restored from __doc__
        """ pos(self) -> QPoint """
        pass

    def previousInFocusChain(self): # real signature unknown; restored from __doc__
        """ previousInFocusChain(self) -> Optional[QWidget] """
        pass

    def raise_(self): # real signature unknown; restored from __doc__
        """ raise_(self) """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def rect(self): # real signature unknown; restored from __doc__
        """ rect(self) -> QRect """
        pass

    def releaseKeyboard(self): # real signature unknown; restored from __doc__
        """ releaseKeyboard(self) """
        pass

    def releaseMouse(self): # real signature unknown; restored from __doc__
        """ releaseMouse(self) """
        pass

    def releaseShortcut(self, id): # real signature unknown; restored from __doc__
        """ releaseShortcut(self, id: int) """
        pass

    def removeAction(self, action, QAction=None): # real signature unknown; restored from __doc__
        """ removeAction(self, action: Optional[QAction]) """
        pass

    def render(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        render(self, target: Optional[QPaintDevice], targetOffset: QPoint = QPoint(), sourceRegion: QRegion = QRegion(), flags: Union[QWidget.RenderFlags, QWidget.RenderFlag] = QWidget.RenderFlags(QWidget.RenderFlag.DrawWindowBackground|QWidget.RenderFlag.DrawChildren))
        render(self, painter: Optional[QPainter], targetOffset: QPoint = QPoint(), sourceRegion: QRegion = QRegion(), flags: Union[QWidget.RenderFlags, QWidget.RenderFlag] = QWidget.RenderFlags(QWidget.RenderFlag.DrawWindowBackground|QWidget.RenderFlag.DrawChildren))
        """
        pass

    def repaint(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        repaint(self)
        repaint(self, x: int, y: int, w: int, h: int)
        repaint(self, a0: QRect)
        repaint(self, a0: QRegion)
        """
        pass

    def resize(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        resize(self, a0: QSize)
        resize(self, w: int, h: int)
        """
        pass

    def resizeEvent(self, a0, QResizeEvent=None): # real signature unknown; restored from __doc__
        """ resizeEvent(self, a0: Optional[QResizeEvent]) """
        pass

    def restoreGeometry(self, geometry, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ restoreGeometry(self, geometry: Union[QByteArray, bytes, bytearray]) -> bool """
        return False

    def saveGeometry(self): # real signature unknown; restored from __doc__
        """ saveGeometry(self) -> QByteArray """
        pass

    def screen(self): # real signature unknown; restored from __doc__
        """ screen(self) -> Optional[QScreen] """
        pass

    def scroll(self, dx, dy, a2=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        scroll(self, dx: int, dy: int)
        scroll(self, dx: int, dy: int, a2: QRect)
        """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setAcceptDrops(self, on): # real signature unknown; restored from __doc__
        """ setAcceptDrops(self, on: bool) """
        pass

    def setAccessibleDescription(self, description, p_str=None): # real signature unknown; restored from __doc__
        """ setAccessibleDescription(self, description: Optional[str]) """
        pass

    def setAccessibleName(self, name, p_str=None): # real signature unknown; restored from __doc__
        """ setAccessibleName(self, name: Optional[str]) """
        pass

    def setAttribute(self, attribute, on=True): # real signature unknown; restored from __doc__
        """ setAttribute(self, attribute: Qt.WidgetAttribute, on: bool = True) """
        pass

    def setAutoFillBackground(self, enabled): # real signature unknown; restored from __doc__
        """ setAutoFillBackground(self, enabled: bool) """
        pass

    def setBackgroundRole(self, a0): # real signature unknown; restored from __doc__
        """ setBackgroundRole(self, a0: QPalette.ColorRole) """
        pass

    def setBaseSize(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setBaseSize(self, basew: int, baseh: int)
        setBaseSize(self, s: QSize)
        """
        pass

    def setContentsMargins(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setContentsMargins(self, left: int, top: int, right: int, bottom: int)
        setContentsMargins(self, margins: QMargins)
        """
        pass

    def setContextMenuPolicy(self, policy): # real signature unknown; restored from __doc__
        """ setContextMenuPolicy(self, policy: Qt.ContextMenuPolicy) """
        pass

    def setCursor(self, a0, QCursor=None, Qt_CursorShape=None): # real signature unknown; restored from __doc__
        """ setCursor(self, a0: Union[QCursor, Qt.CursorShape]) """
        pass

    def setDisabled(self, a0): # real signature unknown; restored from __doc__
        """ setDisabled(self, a0: bool) """
        pass

    def setEnabled(self, a0): # real signature unknown; restored from __doc__
        """ setEnabled(self, a0: bool) """
        pass

    def setFixedHeight(self, h): # real signature unknown; restored from __doc__
        """ setFixedHeight(self, h: int) """
        pass

    def setFixedSize(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setFixedSize(self, a0: QSize)
        setFixedSize(self, w: int, h: int)
        """
        pass

    def setFixedWidth(self, w): # real signature unknown; restored from __doc__
        """ setFixedWidth(self, w: int) """
        pass

    def setFocus(self, reason=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setFocus(self)
        setFocus(self, reason: Qt.FocusReason)
        """
        pass

    def setFocusPolicy(self, policy): # real signature unknown; restored from __doc__
        """ setFocusPolicy(self, policy: Qt.FocusPolicy) """
        pass

    def setFocusProxy(self, a0, QWidget=None): # real signature unknown; restored from __doc__
        """ setFocusProxy(self, a0: Optional[QWidget]) """
        pass

    def setFont(self, a0): # real signature unknown; restored from __doc__
        """ setFont(self, a0: QFont) """
        pass

    def setForegroundRole(self, a0): # real signature unknown; restored from __doc__
        """ setForegroundRole(self, a0: QPalette.ColorRole) """
        pass

    def setGeometry(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setGeometry(self, a0: QRect)
        setGeometry(self, ax: int, ay: int, aw: int, ah: int)
        """
        pass

    def setGraphicsEffect(self, effect, QGraphicsEffect=None): # real signature unknown; restored from __doc__
        """ setGraphicsEffect(self, effect: Optional[QGraphicsEffect]) """
        pass

    def setHidden(self, hidden): # real signature unknown; restored from __doc__
        """ setHidden(self, hidden: bool) """
        pass

    def setInputMethodHints(self, hints, Qt_InputMethodHints=None, Qt_InputMethodHint=None): # real signature unknown; restored from __doc__
        """ setInputMethodHints(self, hints: Union[Qt.InputMethodHints, Qt.InputMethodHint]) """
        pass

    def setLayout(self, a0, QLayout=None): # real signature unknown; restored from __doc__
        """ setLayout(self, a0: Optional[QLayout]) """
        pass

    def setLayoutDirection(self, direction): # real signature unknown; restored from __doc__
        """ setLayoutDirection(self, direction: Qt.LayoutDirection) """
        pass

    def setLocale(self, locale): # real signature unknown; restored from __doc__
        """ setLocale(self, locale: QLocale) """
        pass

    def setMask(self, a0): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setMask(self, a0: QBitmap)
        setMask(self, a0: QRegion)
        """
        pass

    def setMaximumHeight(self, maxh): # real signature unknown; restored from __doc__
        """ setMaximumHeight(self, maxh: int) """
        pass

    def setMaximumSize(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setMaximumSize(self, maxw: int, maxh: int)
        setMaximumSize(self, s: QSize)
        """
        pass

    def setMaximumWidth(self, maxw): # real signature unknown; restored from __doc__
        """ setMaximumWidth(self, maxw: int) """
        pass

    def setMinimumHeight(self, minh): # real signature unknown; restored from __doc__
        """ setMinimumHeight(self, minh: int) """
        pass

    def setMinimumSize(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setMinimumSize(self, minw: int, minh: int)
        setMinimumSize(self, s: QSize)
        """
        pass

    def setMinimumWidth(self, minw): # real signature unknown; restored from __doc__
        """ setMinimumWidth(self, minw: int) """
        pass

    def setMouseTracking(self, enable): # real signature unknown; restored from __doc__
        """ setMouseTracking(self, enable: bool) """
        pass

    def setPalette(self, a0): # real signature unknown; restored from __doc__
        """ setPalette(self, a0: QPalette) """
        pass

    def setParent(self, parent, QWidget=None, *args=None, **kwargs=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setParent(self, parent: Optional[QWidget])
        setParent(self, parent: Optional[QWidget], f: Union[Qt.WindowFlags, Qt.WindowType])
        """
        pass

    def setShortcutAutoRepeat(self, id, enabled=True): # real signature unknown; restored from __doc__
        """ setShortcutAutoRepeat(self, id: int, enabled: bool = True) """
        pass

    def setShortcutEnabled(self, id, enabled=True): # real signature unknown; restored from __doc__
        """ setShortcutEnabled(self, id: int, enabled: bool = True) """
        pass

    def setSizeIncrement(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setSizeIncrement(self, w: int, h: int)
        setSizeIncrement(self, s: QSize)
        """
        pass

    def setSizePolicy(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setSizePolicy(self, a0: QSizePolicy)
        setSizePolicy(self, hor: QSizePolicy.Policy, ver: QSizePolicy.Policy)
        """
        pass

    def setStatusTip(self, a0, p_str=None): # real signature unknown; restored from __doc__
        """ setStatusTip(self, a0: Optional[str]) """
        pass

    def setStyle(self, a0, QStyle=None): # real signature unknown; restored from __doc__
        """ setStyle(self, a0: Optional[QStyle]) """
        pass

    def setStyleSheet(self, styleSheet, p_str=None): # real signature unknown; restored from __doc__
        """ setStyleSheet(self, styleSheet: Optional[str]) """
        pass

    def setTabletTracking(self, enable): # real signature unknown; restored from __doc__
        """ setTabletTracking(self, enable: bool) """
        pass

    def setTabOrder(self, a0, QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setTabOrder(a0: Optional[QWidget], a1: Optional[QWidget]) """
        pass

    def setToolTip(self, a0, p_str=None): # real signature unknown; restored from __doc__
        """ setToolTip(self, a0: Optional[str]) """
        pass

    def setToolTipDuration(self, msec): # real signature unknown; restored from __doc__
        """ setToolTipDuration(self, msec: int) """
        pass

    def setUpdatesEnabled(self, enable): # real signature unknown; restored from __doc__
        """ setUpdatesEnabled(self, enable: bool) """
        pass

    def setVisible(self, visible): # real signature unknown; restored from __doc__
        """ setVisible(self, visible: bool) """
        pass

    def setWhatsThis(self, a0, p_str=None): # real signature unknown; restored from __doc__
        """ setWhatsThis(self, a0: Optional[str]) """
        pass

    def setWindowFilePath(self, filePath, p_str=None): # real signature unknown; restored from __doc__
        """ setWindowFilePath(self, filePath: Optional[str]) """
        pass

    def setWindowFlag(self, a0, on=True): # real signature unknown; restored from __doc__
        """ setWindowFlag(self, a0: Qt.WindowType, on: bool = True) """
        pass

    def setWindowFlags(self, type, Qt_WindowFlags=None, Qt_WindowType=None): # real signature unknown; restored from __doc__
        """ setWindowFlags(self, type: Union[Qt.WindowFlags, Qt.WindowType]) """
        pass

    def setWindowIcon(self, icon): # real signature unknown; restored from __doc__
        """ setWindowIcon(self, icon: QIcon) """
        pass

    def setWindowIconText(self, a0, p_str=None): # real signature unknown; restored from __doc__
        """ setWindowIconText(self, a0: Optional[str]) """
        pass

    def setWindowModality(self, windowModality): # real signature unknown; restored from __doc__
        """ setWindowModality(self, windowModality: Qt.WindowModality) """
        pass

    def setWindowModified(self, a0): # real signature unknown; restored from __doc__
        """ setWindowModified(self, a0: bool) """
        pass

    def setWindowOpacity(self, level): # real signature unknown; restored from __doc__
        """ setWindowOpacity(self, level: float) """
        pass

    def setWindowRole(self, a0, p_str=None): # real signature unknown; restored from __doc__
        """ setWindowRole(self, a0: Optional[str]) """
        pass

    def setWindowState(self, state, Qt_WindowStates=None, Qt_WindowState=None): # real signature unknown; restored from __doc__
        """ setWindowState(self, state: Union[Qt.WindowStates, Qt.WindowState]) """
        pass

    def setWindowTitle(self, a0, p_str=None): # real signature unknown; restored from __doc__
        """ setWindowTitle(self, a0: Optional[str]) """
        pass

    def sharedPainter(self): # real signature unknown; restored from __doc__
        """ sharedPainter(self) -> Optional[QPainter] """
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

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> QSize """
        pass

    def sizeIncrement(self): # real signature unknown; restored from __doc__
        """ sizeIncrement(self) -> QSize """
        pass

    def sizePolicy(self): # real signature unknown; restored from __doc__
        """ sizePolicy(self) -> QSizePolicy """
        return QSizePolicy

    def stackUnder(self, a0, QWidget=None): # real signature unknown; restored from __doc__
        """ stackUnder(self, a0: Optional[QWidget]) """
        pass

    def statusTip(self): # real signature unknown; restored from __doc__
        """ statusTip(self) -> str """
        return ""

    def style(self): # real signature unknown; restored from __doc__
        """ style(self) -> Optional[QStyle] """
        pass

    def styleSheet(self): # real signature unknown; restored from __doc__
        """ styleSheet(self) -> str """
        return ""

    def tabletEvent(self, a0, QTabletEvent=None): # real signature unknown; restored from __doc__
        """ tabletEvent(self, a0: Optional[QTabletEvent]) """
        pass

    def testAttribute(self, attribute): # real signature unknown; restored from __doc__
        """ testAttribute(self, attribute: Qt.WidgetAttribute) -> bool """
        return False

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def toolTip(self): # real signature unknown; restored from __doc__
        """ toolTip(self) -> str """
        return ""

    def toolTipDuration(self): # real signature unknown; restored from __doc__
        """ toolTipDuration(self) -> int """
        return 0

    def underMouse(self): # real signature unknown; restored from __doc__
        """ underMouse(self) -> bool """
        return False

    def ungrabGesture(self, type): # real signature unknown; restored from __doc__
        """ ungrabGesture(self, type: Qt.GestureType) """
        pass

    def unsetCursor(self): # real signature unknown; restored from __doc__
        """ unsetCursor(self) """
        pass

    def unsetLayoutDirection(self): # real signature unknown; restored from __doc__
        """ unsetLayoutDirection(self) """
        pass

    def unsetLocale(self): # real signature unknown; restored from __doc__
        """ unsetLocale(self) """
        pass

    def update(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        update(self)
        update(self, a0: QRect)
        update(self, a0: QRegion)
        update(self, ax: int, ay: int, aw: int, ah: int)
        """
        pass

    def updateGeometry(self): # real signature unknown; restored from __doc__
        """ updateGeometry(self) """
        pass

    def updateMicroFocus(self): # real signature unknown; restored from __doc__
        """ updateMicroFocus(self) """
        pass

    def updatesEnabled(self): # real signature unknown; restored from __doc__
        """ updatesEnabled(self) -> bool """
        return False

    def visibleRegion(self): # real signature unknown; restored from __doc__
        """ visibleRegion(self) -> QRegion """
        pass

    def whatsThis(self): # real signature unknown; restored from __doc__
        """ whatsThis(self) -> str """
        return ""

    def wheelEvent(self, a0, QWheelEvent=None): # real signature unknown; restored from __doc__
        """ wheelEvent(self, a0: Optional[QWheelEvent]) """
        pass

    def width(self): # real signature unknown; restored from __doc__
        """ width(self) -> int """
        return 0

    def window(self): # real signature unknown; restored from __doc__
        """ window(self) -> Optional[QWidget] """
        pass

    def windowFilePath(self): # real signature unknown; restored from __doc__
        """ windowFilePath(self) -> str """
        return ""

    def windowFlags(self): # real signature unknown; restored from __doc__
        """ windowFlags(self) -> Qt.WindowFlags """
        pass

    def windowHandle(self): # real signature unknown; restored from __doc__
        """ windowHandle(self) -> Optional[QWindow] """
        pass

    def windowIcon(self): # real signature unknown; restored from __doc__
        """ windowIcon(self) -> QIcon """
        pass

    def windowIconChanged(self, *args, **kwargs): # real signature unknown
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

    def windowIconText(self): # real signature unknown; restored from __doc__
        """ windowIconText(self) -> str """
        return ""

    def windowIconTextChanged(self, *args, **kwargs): # real signature unknown
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

    def windowModality(self): # real signature unknown; restored from __doc__
        """ windowModality(self) -> Qt.WindowModality """
        pass

    def windowOpacity(self): # real signature unknown; restored from __doc__
        """ windowOpacity(self) -> float """
        return 0.0

    def windowRole(self): # real signature unknown; restored from __doc__
        """ windowRole(self) -> str """
        return ""

    def windowState(self): # real signature unknown; restored from __doc__
        """ windowState(self) -> Qt.WindowStates """
        pass

    def windowTitle(self): # real signature unknown; restored from __doc__
        """ windowTitle(self) -> str """
        return ""

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

    def windowType(self): # real signature unknown; restored from __doc__
        """ windowType(self) -> Qt.WindowType """
        pass

    def winId(self): # real signature unknown; restored from __doc__
        """ winId(self) -> PyQt5.sip.voidptr """
        pass

    def x(self): # real signature unknown; restored from __doc__
        """ x(self) -> int """
        return 0

    def y(self): # real signature unknown; restored from __doc__
        """ y(self) -> int """
        return 0

    def __init__(self, parent, QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    DrawChildren = 2
    DrawWindowBackground = 1
    IgnoreMask = 4


