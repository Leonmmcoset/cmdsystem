# encoding: utf-8
# module PyQt5.QtQuick
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtQuick.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import PyQt5.QtQml as __PyQt5_QtQml
import sip as __sip


class QSGRendererInterface(__sip.simplewrapper):
    # no doc
    def getResource(self, window, QQuickWindow=None, *args, **kwargs): # real signature unknown; restored from __doc__ with multiple overloads
        """
        getResource(self, window: Optional[QQuickWindow], resource: QSGRendererInterface.Resource) -> Optional[PyQt5.sip.voidptr]
        getResource(self, window: Optional[QQuickWindow], resource: Optional[str]) -> Optional[PyQt5.sip.voidptr]
        """
        pass

    def graphicsApi(self): # real signature unknown; restored from __doc__
        """ graphicsApi(self) -> QSGRendererInterface.GraphicsApi """
        pass

    def isApiRhiBased(self, api): # real signature unknown; restored from __doc__
        """ isApiRhiBased(api: QSGRendererInterface.GraphicsApi) -> bool """
        return False

    def shaderCompilationType(self): # real signature unknown; restored from __doc__
        """ shaderCompilationType(self) -> QSGRendererInterface.ShaderCompilationTypes """
        pass

    def shaderSourceType(self): # real signature unknown; restored from __doc__
        """ shaderSourceType(self) -> QSGRendererInterface.ShaderSourceTypes """
        pass

    def shaderType(self): # real signature unknown; restored from __doc__
        """ shaderType(self) -> QSGRendererInterface.ShaderType """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    CommandEncoderResource = 8
    CommandListResource = 2
    CommandQueueResource = 1
    DeviceContextResource = 7
    DeviceResource = 0
    Direct3D11Rhi = 6
    Direct3D12 = 3
    GLSL = 1
    HLSL = 2
    MetalRhi = 8
    NullRhi = 9
    OfflineCompilation = 2
    OpenGL = 2
    OpenGLContextResource = 6
    OpenGLRhi = 5
    OpenVG = 4
    PainterResource = 3
    PhysicalDeviceResource = 5
    RenderPassResource = 10
    RhiResource = 4
    RhiShader = 3
    RuntimeCompilation = 1
    ShaderByteCode = 4
    ShaderSourceFile = 2
    ShaderSourceString = 1
    Software = 1
    Unknown = 0
    UnknownShadingLanguage = 0
    VulkanInstanceResource = 9
    VulkanRhi = 7


