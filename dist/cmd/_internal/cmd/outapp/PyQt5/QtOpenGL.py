# encoding: utf-8
# module PyQt5.QtOpenGL
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtOpenGL.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtWidgets as __PyQt5_QtWidgets
import sip as __sip


# no functions
# classes

class QGL(__sip.simplewrapper):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    AccumBuffer = 16
    AlphaChannel = 8
    ColorIndex = 262144
    DeprecatedFunctions = 1024
    DepthBuffer = 2
    DirectRendering = 128
    DoubleBuffer = 1
    HasOverlay = 256
    IndirectRendering = 8388608
    NoAccumBuffer = 1048576
    NoAlphaChannel = 524288
    NoDeprecatedFunctions = 67108864
    NoDepthBuffer = 131072
    NoOverlay = 16777216
    NoSampleBuffers = 33554432
    NoStencilBuffer = 2097152
    NoStereoBuffers = 4194304
    Rgba = 4
    SampleBuffers = 512
    SingleBuffer = 65536
    StencilBuffer = 32
    StereoBuffers = 64


class QGLContext(__sip.wrapper):
    """ QGLContext(format: QGLFormat) """
    def areSharing(self, context1, QGLContext=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ areSharing(context1: Optional[QGLContext], context2: Optional[QGLContext]) -> bool """
        pass

    def bindTexture(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        bindTexture(self, image: QImage, target: int = GL_TEXTURE_2D, format: int = GL_RGBA) -> int
        bindTexture(self, pixmap: QPixmap, target: int = GL_TEXTURE_2D, format: int = GL_RGBA) -> int
        bindTexture(self, fileName: Optional[str]) -> int
        bindTexture(self, image: QImage, target: int, format: int, options: Union[QGLContext.BindOptions, QGLContext.BindOption]) -> int
        bindTexture(self, pixmap: QPixmap, target: int, format: int, options: Union[QGLContext.BindOptions, QGLContext.BindOption]) -> int
        """
        return 0

    def chooseContext(self, shareContext, QGLContext=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ chooseContext(self, shareContext: Optional[QGLContext] = None) -> bool """
        pass

    def create(self, shareContext, QGLContext=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ create(self, shareContext: Optional[QGLContext] = None) -> bool """
        pass

    def currentContext(self): # real signature unknown; restored from __doc__
        """ currentContext() -> Optional[QGLContext] """
        pass

    def deleteTexture(self, tx_id): # real signature unknown; restored from __doc__
        """ deleteTexture(self, tx_id: int) """
        pass

    def device(self): # real signature unknown; restored from __doc__
        """ device(self) -> Optional[QPaintDevice] """
        pass

    def deviceIsPixmap(self): # real signature unknown; restored from __doc__
        """ deviceIsPixmap(self) -> bool """
        return False

    def doneCurrent(self): # real signature unknown; restored from __doc__
        """ doneCurrent(self) """
        pass

    def drawTexture(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        drawTexture(self, target: QRectF, textureId: int, textureTarget: int = GL_TEXTURE_2D)
        drawTexture(self, point: Union[QPointF, QPoint], textureId: int, textureTarget: int = GL_TEXTURE_2D)
        """
        pass

    def format(self): # real signature unknown; restored from __doc__
        """ format(self) -> QGLFormat """
        return QGLFormat

    def getProcAddress(self, proc, p_str=None): # real signature unknown; restored from __doc__
        """ getProcAddress(self, proc: Optional[str]) -> Optional[PyQt5.sip.voidptr] """
        pass

    def initialized(self): # real signature unknown; restored from __doc__
        """ initialized(self) -> bool """
        return False

    def isSharing(self): # real signature unknown; restored from __doc__
        """ isSharing(self) -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def makeCurrent(self): # real signature unknown; restored from __doc__
        """ makeCurrent(self) """
        pass

    def moveToThread(self, thread, QThread=None): # real signature unknown; restored from __doc__
        """ moveToThread(self, thread: Optional[QThread]) """
        pass

    def overlayTransparentColor(self): # real signature unknown; restored from __doc__
        """ overlayTransparentColor(self) -> QColor """
        pass

    def requestedFormat(self): # real signature unknown; restored from __doc__
        """ requestedFormat(self) -> QGLFormat """
        return QGLFormat

    def reset(self): # real signature unknown; restored from __doc__
        """ reset(self) """
        pass

    def setFormat(self, format): # real signature unknown; restored from __doc__
        """ setFormat(self, format: QGLFormat) """
        pass

    def setInitialized(self, on): # real signature unknown; restored from __doc__
        """ setInitialized(self, on: bool) """
        pass

    def setTextureCacheLimit(self, size): # real signature unknown; restored from __doc__
        """ setTextureCacheLimit(size: int) """
        pass

    def setWindowCreated(self, on): # real signature unknown; restored from __doc__
        """ setWindowCreated(self, on: bool) """
        pass

    def swapBuffers(self): # real signature unknown; restored from __doc__
        """ swapBuffers(self) """
        pass

    def textureCacheLimit(self): # real signature unknown; restored from __doc__
        """ textureCacheLimit() -> int """
        return 0

    def windowCreated(self): # real signature unknown; restored from __doc__
        """ windowCreated(self) -> bool """
        return False

    def __init__(self, format): # real signature unknown; restored from __doc__
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    DefaultBindOption = 11
    InvertedYBindOption = 1
    LinearFilteringBindOption = 8
    MipmapBindOption = 2
    NoBindOption = 0
    PremultipliedAlphaBindOption = 4


class QGLFormat(__sip.simplewrapper):
    """
    QGLFormat()
    QGLFormat(options: Union[QGL.FormatOptions, QGL.FormatOption], plane: int = 0)
    QGLFormat(other: QGLFormat)
    """
    def accum(self): # real signature unknown; restored from __doc__
        """ accum(self) -> bool """
        return False

    def accumBufferSize(self): # real signature unknown; restored from __doc__
        """ accumBufferSize(self) -> int """
        return 0

    def alpha(self): # real signature unknown; restored from __doc__
        """ alpha(self) -> bool """
        return False

    def alphaBufferSize(self): # real signature unknown; restored from __doc__
        """ alphaBufferSize(self) -> int """
        return 0

    def blueBufferSize(self): # real signature unknown; restored from __doc__
        """ blueBufferSize(self) -> int """
        return 0

    def defaultFormat(self): # real signature unknown; restored from __doc__
        """ defaultFormat() -> QGLFormat """
        return QGLFormat

    def defaultOverlayFormat(self): # real signature unknown; restored from __doc__
        """ defaultOverlayFormat() -> QGLFormat """
        return QGLFormat

    def depth(self): # real signature unknown; restored from __doc__
        """ depth(self) -> bool """
        return False

    def depthBufferSize(self): # real signature unknown; restored from __doc__
        """ depthBufferSize(self) -> int """
        return 0

    def directRendering(self): # real signature unknown; restored from __doc__
        """ directRendering(self) -> bool """
        return False

    def doubleBuffer(self): # real signature unknown; restored from __doc__
        """ doubleBuffer(self) -> bool """
        return False

    def greenBufferSize(self): # real signature unknown; restored from __doc__
        """ greenBufferSize(self) -> int """
        return 0

    def hasOpenGL(self): # real signature unknown; restored from __doc__
        """ hasOpenGL() -> bool """
        return False

    def hasOpenGLOverlays(self): # real signature unknown; restored from __doc__
        """ hasOpenGLOverlays() -> bool """
        return False

    def hasOverlay(self): # real signature unknown; restored from __doc__
        """ hasOverlay(self) -> bool """
        return False

    def majorVersion(self): # real signature unknown; restored from __doc__
        """ majorVersion(self) -> int """
        return 0

    def minorVersion(self): # real signature unknown; restored from __doc__
        """ minorVersion(self) -> int """
        return 0

    def openGLVersionFlags(self): # real signature unknown; restored from __doc__
        """ openGLVersionFlags() -> QGLFormat.OpenGLVersionFlags """
        pass

    def plane(self): # real signature unknown; restored from __doc__
        """ plane(self) -> int """
        return 0

    def profile(self): # real signature unknown; restored from __doc__
        """ profile(self) -> QGLFormat.OpenGLContextProfile """
        pass

    def redBufferSize(self): # real signature unknown; restored from __doc__
        """ redBufferSize(self) -> int """
        return 0

    def rgba(self): # real signature unknown; restored from __doc__
        """ rgba(self) -> bool """
        return False

    def sampleBuffers(self): # real signature unknown; restored from __doc__
        """ sampleBuffers(self) -> bool """
        return False

    def samples(self): # real signature unknown; restored from __doc__
        """ samples(self) -> int """
        return 0

    def setAccum(self, enable): # real signature unknown; restored from __doc__
        """ setAccum(self, enable: bool) """
        pass

    def setAccumBufferSize(self, size): # real signature unknown; restored from __doc__
        """ setAccumBufferSize(self, size: int) """
        pass

    def setAlpha(self, enable): # real signature unknown; restored from __doc__
        """ setAlpha(self, enable: bool) """
        pass

    def setAlphaBufferSize(self, size): # real signature unknown; restored from __doc__
        """ setAlphaBufferSize(self, size: int) """
        pass

    def setBlueBufferSize(self, size): # real signature unknown; restored from __doc__
        """ setBlueBufferSize(self, size: int) """
        pass

    def setDefaultFormat(self, f): # real signature unknown; restored from __doc__
        """ setDefaultFormat(f: QGLFormat) """
        pass

    def setDefaultOverlayFormat(self, f): # real signature unknown; restored from __doc__
        """ setDefaultOverlayFormat(f: QGLFormat) """
        pass

    def setDepth(self, enable): # real signature unknown; restored from __doc__
        """ setDepth(self, enable: bool) """
        pass

    def setDepthBufferSize(self, size): # real signature unknown; restored from __doc__
        """ setDepthBufferSize(self, size: int) """
        pass

    def setDirectRendering(self, enable): # real signature unknown; restored from __doc__
        """ setDirectRendering(self, enable: bool) """
        pass

    def setDoubleBuffer(self, enable): # real signature unknown; restored from __doc__
        """ setDoubleBuffer(self, enable: bool) """
        pass

    def setGreenBufferSize(self, size): # real signature unknown; restored from __doc__
        """ setGreenBufferSize(self, size: int) """
        pass

    def setOption(self, opt, QGL_FormatOptions=None, QGL_FormatOption=None): # real signature unknown; restored from __doc__
        """ setOption(self, opt: Union[QGL.FormatOptions, QGL.FormatOption]) """
        pass

    def setOverlay(self, enable): # real signature unknown; restored from __doc__
        """ setOverlay(self, enable: bool) """
        pass

    def setPlane(self, plane): # real signature unknown; restored from __doc__
        """ setPlane(self, plane: int) """
        pass

    def setProfile(self, profile): # real signature unknown; restored from __doc__
        """ setProfile(self, profile: QGLFormat.OpenGLContextProfile) """
        pass

    def setRedBufferSize(self, size): # real signature unknown; restored from __doc__
        """ setRedBufferSize(self, size: int) """
        pass

    def setRgba(self, enable): # real signature unknown; restored from __doc__
        """ setRgba(self, enable: bool) """
        pass

    def setSampleBuffers(self, enable): # real signature unknown; restored from __doc__
        """ setSampleBuffers(self, enable: bool) """
        pass

    def setSamples(self, numSamples): # real signature unknown; restored from __doc__
        """ setSamples(self, numSamples: int) """
        pass

    def setStencil(self, enable): # real signature unknown; restored from __doc__
        """ setStencil(self, enable: bool) """
        pass

    def setStencilBufferSize(self, size): # real signature unknown; restored from __doc__
        """ setStencilBufferSize(self, size: int) """
        pass

    def setStereo(self, enable): # real signature unknown; restored from __doc__
        """ setStereo(self, enable: bool) """
        pass

    def setSwapInterval(self, interval): # real signature unknown; restored from __doc__
        """ setSwapInterval(self, interval: int) """
        pass

    def setVersion(self, major, minor): # real signature unknown; restored from __doc__
        """ setVersion(self, major: int, minor: int) """
        pass

    def stencil(self): # real signature unknown; restored from __doc__
        """ stencil(self) -> bool """
        return False

    def stencilBufferSize(self): # real signature unknown; restored from __doc__
        """ stencilBufferSize(self) -> int """
        return 0

    def stereo(self): # real signature unknown; restored from __doc__
        """ stereo(self) -> bool """
        return False

    def swapInterval(self): # real signature unknown; restored from __doc__
        """ swapInterval(self) -> int """
        return 0

    def testOption(self, opt, QGL_FormatOptions=None, QGL_FormatOption=None): # real signature unknown; restored from __doc__
        """ testOption(self, opt: Union[QGL.FormatOptions, QGL.FormatOption]) -> bool """
        return False

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    CompatibilityProfile = 2
    CoreProfile = 1
    NoProfile = 0
    OpenGL_ES_CommonLite_Version_1_0 = 256
    OpenGL_ES_CommonLite_Version_1_1 = 1024
    OpenGL_ES_Common_Version_1_0 = 128
    OpenGL_ES_Common_Version_1_1 = 512
    OpenGL_ES_Version_2_0 = 2048
    OpenGL_Version_1_1 = 1
    OpenGL_Version_1_2 = 2
    OpenGL_Version_1_3 = 4
    OpenGL_Version_1_4 = 8
    OpenGL_Version_1_5 = 16
    OpenGL_Version_2_0 = 32
    OpenGL_Version_2_1 = 64
    OpenGL_Version_3_0 = 4096
    OpenGL_Version_3_1 = 8192
    OpenGL_Version_3_2 = 16384
    OpenGL_Version_3_3 = 32768
    OpenGL_Version_4_0 = 65536
    OpenGL_Version_4_1 = 131072
    OpenGL_Version_4_2 = 262144
    OpenGL_Version_4_3 = 524288
    OpenGL_Version_None = 0
    __hash__ = None


class QGLWidget(__PyQt5_QtWidgets.QWidget):
    """
    QGLWidget(parent: Optional[QWidget] = None, shareWidget: Optional[QGLWidget] = None, flags: Union[Qt.WindowFlags, Qt.WindowType] = Qt.WindowFlags())
    QGLWidget(context: Optional[QGLContext], parent: Optional[QWidget] = None, shareWidget: Optional[QGLWidget] = None, flags: Union[Qt.WindowFlags, Qt.WindowType] = Qt.WindowFlags())
    QGLWidget(format: QGLFormat, parent: Optional[QWidget] = None, shareWidget: Optional[QGLWidget] = None, flags: Union[Qt.WindowFlags, Qt.WindowType] = Qt.WindowFlags())
    """
    def actionEvent(self, *args, **kwargs): # real signature unknown
        pass

    def autoBufferSwap(self): # real signature unknown; restored from __doc__
        """ autoBufferSwap(self) -> bool """
        return False

    def bindTexture(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        bindTexture(self, image: QImage, target: int = GL_TEXTURE_2D, format: int = GL_RGBA) -> int
        bindTexture(self, pixmap: QPixmap, target: int = GL_TEXTURE_2D, format: int = GL_RGBA) -> int
        bindTexture(self, fileName: Optional[str]) -> int
        bindTexture(self, image: QImage, target: int, format: int, options: Union[QGLContext.BindOptions, QGLContext.BindOption]) -> int
        bindTexture(self, pixmap: QPixmap, target: int, format: int, options: Union[QGLContext.BindOptions, QGLContext.BindOption]) -> int
        """
        return 0

    def changeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def closeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def context(self): # real signature unknown; restored from __doc__
        """ context(self) -> Optional[QGLContext] """
        pass

    def contextMenuEvent(self, *args, **kwargs): # real signature unknown
        pass

    def convertToGLFormat(self, img): # real signature unknown; restored from __doc__
        """ convertToGLFormat(img: QImage) -> QImage """
        pass

    def create(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def deleteTexture(self, tx_id): # real signature unknown; restored from __doc__
        """ deleteTexture(self, tx_id: int) """
        pass

    def destroy(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def doneCurrent(self): # real signature unknown; restored from __doc__
        """ doneCurrent(self) """
        pass

    def doubleBuffer(self): # real signature unknown; restored from __doc__
        """ doubleBuffer(self) -> bool """
        return False

    def dragEnterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dragLeaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dragMoveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def drawTexture(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        drawTexture(self, target: QRectF, textureId: int, textureTarget: int = GL_TEXTURE_2D)
        drawTexture(self, point: Union[QPointF, QPoint], textureId: int, textureTarget: int = GL_TEXTURE_2D)
        """
        pass

    def dropEvent(self, *args, **kwargs): # real signature unknown
        pass

    def enterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, a0, QEvent=None): # real signature unknown; restored from __doc__
        """ event(self, a0: Optional[QEvent]) -> bool """
        return False

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

    def format(self): # real signature unknown; restored from __doc__
        """ format(self) -> QGLFormat """
        return QGLFormat

    def glDraw(self): # real signature unknown; restored from __doc__
        """ glDraw(self) """
        pass

    def glInit(self): # real signature unknown; restored from __doc__
        """ glInit(self) """
        pass

    def grabFrameBuffer(self, withAlpha=False): # real signature unknown; restored from __doc__
        """ grabFrameBuffer(self, withAlpha: bool = False) -> QImage """
        pass

    def hideEvent(self, *args, **kwargs): # real signature unknown
        pass

    def initializeGL(self): # real signature unknown; restored from __doc__
        """ initializeGL(self) """
        pass

    def initializeOverlayGL(self): # real signature unknown; restored from __doc__
        """ initializeOverlayGL(self) """
        pass

    def initPainter(self, *args, **kwargs): # real signature unknown
        pass

    def inputMethodEvent(self, *args, **kwargs): # real signature unknown
        pass

    def isSharing(self): # real signature unknown; restored from __doc__
        """ isSharing(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def keyPressEvent(self, *args, **kwargs): # real signature unknown
        pass

    def keyReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def leaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def makeCurrent(self): # real signature unknown; restored from __doc__
        """ makeCurrent(self) """
        pass

    def makeOverlayCurrent(self): # real signature unknown; restored from __doc__
        """ makeOverlayCurrent(self) """
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

    def overlayContext(self): # real signature unknown; restored from __doc__
        """ overlayContext(self) -> Optional[QGLContext] """
        pass

    def paintEngine(self): # real signature unknown; restored from __doc__
        """ paintEngine(self) -> Optional[QPaintEngine] """
        pass

    def paintEvent(self, a0, QPaintEvent=None): # real signature unknown; restored from __doc__
        """ paintEvent(self, a0: Optional[QPaintEvent]) """
        pass

    def paintGL(self): # real signature unknown; restored from __doc__
        """ paintGL(self) """
        pass

    def paintOverlayGL(self): # real signature unknown; restored from __doc__
        """ paintOverlayGL(self) """
        pass

    def qglClearColor(self, c, QColor=None, Qt_GlobalColor=None): # real signature unknown; restored from __doc__
        """ qglClearColor(self, c: Union[QColor, Qt.GlobalColor]) """
        pass

    def qglColor(self, c, QColor=None, Qt_GlobalColor=None): # real signature unknown; restored from __doc__
        """ qglColor(self, c: Union[QColor, Qt.GlobalColor]) """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def renderPixmap(self, width=0, height=0, useContext=False): # real signature unknown; restored from __doc__
        """ renderPixmap(self, width: int = 0, height: int = 0, useContext: bool = False) -> QPixmap """
        pass

    def renderText(self, x, y, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        renderText(self, x: int, y: int, str: Optional[str], font: QFont = QFont())
        renderText(self, x: float, y: float, z: float, str: Optional[str], font: QFont = QFont())
        """
        pass

    def resizeEvent(self, a0, QResizeEvent=None): # real signature unknown; restored from __doc__
        """ resizeEvent(self, a0: Optional[QResizeEvent]) """
        pass

    def resizeGL(self, w, h): # real signature unknown; restored from __doc__
        """ resizeGL(self, w: int, h: int) """
        pass

    def resizeOverlayGL(self, w, h): # real signature unknown; restored from __doc__
        """ resizeOverlayGL(self, w: int, h: int) """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setAutoBufferSwap(self, on): # real signature unknown; restored from __doc__
        """ setAutoBufferSwap(self, on: bool) """
        pass

    def setContext(self, context, QGLContext=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setContext(self, context: Optional[QGLContext], shareContext: Optional[QGLContext] = None, deleteOldContext: bool = True) """
        pass

    def sharedPainter(self, *args, **kwargs): # real signature unknown
        pass

    def showEvent(self, *args, **kwargs): # real signature unknown
        pass

    def swapBuffers(self): # real signature unknown; restored from __doc__
        """ swapBuffers(self) """
        pass

    def tabletEvent(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def updateGL(self): # real signature unknown; restored from __doc__
        """ updateGL(self) """
        pass

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

    def updateOverlayGL(self): # real signature unknown; restored from __doc__
        """ updateOverlayGL(self) """
        pass

    def wheelEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


# variables with complex values



