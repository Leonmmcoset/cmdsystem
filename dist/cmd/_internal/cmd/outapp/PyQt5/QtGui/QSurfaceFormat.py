# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QSurfaceFormat(__sip.simplewrapper):
    """
    QSurfaceFormat()
    QSurfaceFormat(options: Union[QSurfaceFormat.FormatOptions, QSurfaceFormat.FormatOption])
    QSurfaceFormat(other: QSurfaceFormat)
    """
    def alphaBufferSize(self): # real signature unknown; restored from __doc__
        """ alphaBufferSize(self) -> int """
        return 0

    def blueBufferSize(self): # real signature unknown; restored from __doc__
        """ blueBufferSize(self) -> int """
        return 0

    def colorSpace(self): # real signature unknown; restored from __doc__
        """ colorSpace(self) -> QSurfaceFormat.ColorSpace """
        pass

    def defaultFormat(self): # real signature unknown; restored from __doc__
        """ defaultFormat() -> QSurfaceFormat """
        return QSurfaceFormat

    def depthBufferSize(self): # real signature unknown; restored from __doc__
        """ depthBufferSize(self) -> int """
        return 0

    def greenBufferSize(self): # real signature unknown; restored from __doc__
        """ greenBufferSize(self) -> int """
        return 0

    def hasAlpha(self): # real signature unknown; restored from __doc__
        """ hasAlpha(self) -> bool """
        return False

    def majorVersion(self): # real signature unknown; restored from __doc__
        """ majorVersion(self) -> int """
        return 0

    def minorVersion(self): # real signature unknown; restored from __doc__
        """ minorVersion(self) -> int """
        return 0

    def options(self): # real signature unknown; restored from __doc__
        """ options(self) -> QSurfaceFormat.FormatOptions """
        pass

    def profile(self): # real signature unknown; restored from __doc__
        """ profile(self) -> QSurfaceFormat.OpenGLContextProfile """
        pass

    def redBufferSize(self): # real signature unknown; restored from __doc__
        """ redBufferSize(self) -> int """
        return 0

    def renderableType(self): # real signature unknown; restored from __doc__
        """ renderableType(self) -> QSurfaceFormat.RenderableType """
        pass

    def samples(self): # real signature unknown; restored from __doc__
        """ samples(self) -> int """
        return 0

    def setAlphaBufferSize(self, size): # real signature unknown; restored from __doc__
        """ setAlphaBufferSize(self, size: int) """
        pass

    def setBlueBufferSize(self, size): # real signature unknown; restored from __doc__
        """ setBlueBufferSize(self, size: int) """
        pass

    def setColorSpace(self, colorSpace): # real signature unknown; restored from __doc__
        """ setColorSpace(self, colorSpace: QSurfaceFormat.ColorSpace) """
        pass

    def setDefaultFormat(self, format): # real signature unknown; restored from __doc__
        """ setDefaultFormat(format: QSurfaceFormat) """
        pass

    def setDepthBufferSize(self, size): # real signature unknown; restored from __doc__
        """ setDepthBufferSize(self, size: int) """
        pass

    def setGreenBufferSize(self, size): # real signature unknown; restored from __doc__
        """ setGreenBufferSize(self, size: int) """
        pass

    def setMajorVersion(self, majorVersion): # real signature unknown; restored from __doc__
        """ setMajorVersion(self, majorVersion: int) """
        pass

    def setMinorVersion(self, minorVersion): # real signature unknown; restored from __doc__
        """ setMinorVersion(self, minorVersion: int) """
        pass

    def setOption(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setOption(self, opt: Union[QSurfaceFormat.FormatOptions, QSurfaceFormat.FormatOption])
        setOption(self, option: QSurfaceFormat.FormatOption, on: bool = True)
        """
        pass

    def setOptions(self, options, QSurfaceFormat_FormatOptions=None, QSurfaceFormat_FormatOption=None): # real signature unknown; restored from __doc__
        """ setOptions(self, options: Union[QSurfaceFormat.FormatOptions, QSurfaceFormat.FormatOption]) """
        pass

    def setProfile(self, profile): # real signature unknown; restored from __doc__
        """ setProfile(self, profile: QSurfaceFormat.OpenGLContextProfile) """
        pass

    def setRedBufferSize(self, size): # real signature unknown; restored from __doc__
        """ setRedBufferSize(self, size: int) """
        pass

    def setRenderableType(self, type): # real signature unknown; restored from __doc__
        """ setRenderableType(self, type: QSurfaceFormat.RenderableType) """
        pass

    def setSamples(self, numSamples): # real signature unknown; restored from __doc__
        """ setSamples(self, numSamples: int) """
        pass

    def setStencilBufferSize(self, size): # real signature unknown; restored from __doc__
        """ setStencilBufferSize(self, size: int) """
        pass

    def setStereo(self, enable): # real signature unknown; restored from __doc__
        """ setStereo(self, enable: bool) """
        pass

    def setSwapBehavior(self, behavior): # real signature unknown; restored from __doc__
        """ setSwapBehavior(self, behavior: QSurfaceFormat.SwapBehavior) """
        pass

    def setSwapInterval(self, interval): # real signature unknown; restored from __doc__
        """ setSwapInterval(self, interval: int) """
        pass

    def setVersion(self, major, minor): # real signature unknown; restored from __doc__
        """ setVersion(self, major: int, minor: int) """
        pass

    def stencilBufferSize(self): # real signature unknown; restored from __doc__
        """ stencilBufferSize(self) -> int """
        return 0

    def stereo(self): # real signature unknown; restored from __doc__
        """ stereo(self) -> bool """
        return False

    def swapBehavior(self): # real signature unknown; restored from __doc__
        """ swapBehavior(self) -> QSurfaceFormat.SwapBehavior """
        pass

    def swapInterval(self): # real signature unknown; restored from __doc__
        """ swapInterval(self) -> int """
        return 0

    def testOption(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        testOption(self, opt: Union[QSurfaceFormat.FormatOptions, QSurfaceFormat.FormatOption]) -> bool
        testOption(self, option: QSurfaceFormat.FormatOption) -> bool
        """
        return False

    def version(self): # real signature unknown; restored from __doc__
        """ version(self) -> Tuple[int, int] """
        pass

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
    DebugContext = 2
    DefaultColorSpace = 0
    DefaultRenderableType = 0
    DefaultSwapBehavior = 0
    DeprecatedFunctions = 4
    DoubleBuffer = 2
    NoProfile = 0
    OpenGL = 1
    OpenGLES = 2
    OpenVG = 4
    ResetNotification = 8
    SingleBuffer = 1
    sRGBColorSpace = 1
    StereoBuffers = 1
    TripleBuffer = 3
    __hash__ = None


