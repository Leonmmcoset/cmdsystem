# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QOpenGLFramebufferObject(__sip.simplewrapper):
    """
    QOpenGLFramebufferObject(size: QSize, target: int = GL_TEXTURE_2D)
    QOpenGLFramebufferObject(width: int, height: int, target: int = GL_TEXTURE_2D)
    QOpenGLFramebufferObject(size: QSize, attachment: QOpenGLFramebufferObject.Attachment, target: int = GL_TEXTURE_2D, internal_format: int = GL_RGBA8)
    QOpenGLFramebufferObject(width: int, height: int, attachment: QOpenGLFramebufferObject.Attachment, target: int = GL_TEXTURE_2D, internal_format: int = GL_RGBA8)
    QOpenGLFramebufferObject(size: QSize, format: QOpenGLFramebufferObjectFormat)
    QOpenGLFramebufferObject(width: int, height: int, format: QOpenGLFramebufferObjectFormat)
    """
    def addColorAttachment(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        addColorAttachment(self, size: QSize, internal_format: int = 0)
        addColorAttachment(self, width: int, height: int, internal_format: int = 0)
        """
        pass

    def attachment(self): # real signature unknown; restored from __doc__
        """ attachment(self) -> QOpenGLFramebufferObject.Attachment """
        pass

    def bind(self): # real signature unknown; restored from __doc__
        """ bind(self) -> bool """
        return False

    def bindDefault(self): # real signature unknown; restored from __doc__
        """ bindDefault() -> bool """
        return False

    def blitFramebuffer(self, target, QOpenGLFramebufferObject=None, *args, **kwargs): # real signature unknown; restored from __doc__ with multiple overloads
        """
        blitFramebuffer(target: Optional[QOpenGLFramebufferObject], targetRect: QRect, source: Optional[QOpenGLFramebufferObject], sourceRect: QRect, buffers: int = GL_COLOR_BUFFER_BIT, filter: int = GL_NEAREST)
        blitFramebuffer(target: Optional[QOpenGLFramebufferObject], source: Optional[QOpenGLFramebufferObject], buffers: int = GL_COLOR_BUFFER_BIT, filter: int = GL_NEAREST)
        blitFramebuffer(target: Optional[QOpenGLFramebufferObject], targetRect: QRect, source: Optional[QOpenGLFramebufferObject], sourceRect: QRect, buffers: int, filter: int, readColorAttachmentIndex: int, drawColorAttachmentIndex: int)
        blitFramebuffer(target: Optional[QOpenGLFramebufferObject], targetRect: QRect, source: Optional[QOpenGLFramebufferObject], sourceRect: QRect, buffers: int, filter: int, readColorAttachmentIndex: int, drawColorAttachmentIndex: int, restorePolicy: QOpenGLFramebufferObject.FramebufferRestorePolicy)
        """
        pass

    def format(self): # real signature unknown; restored from __doc__
        """ format(self) -> QOpenGLFramebufferObjectFormat """
        return QOpenGLFramebufferObjectFormat

    def handle(self): # real signature unknown; restored from __doc__
        """ handle(self) -> int """
        return 0

    def hasOpenGLFramebufferBlit(self): # real signature unknown; restored from __doc__
        """ hasOpenGLFramebufferBlit() -> bool """
        return False

    def hasOpenGLFramebufferObjects(self): # real signature unknown; restored from __doc__
        """ hasOpenGLFramebufferObjects() -> bool """
        return False

    def height(self): # real signature unknown; restored from __doc__
        """ height(self) -> int """
        return 0

    def isBound(self): # real signature unknown; restored from __doc__
        """ isBound(self) -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def release(self): # real signature unknown; restored from __doc__
        """ release(self) -> bool """
        return False

    def setAttachment(self, attachment): # real signature unknown; restored from __doc__
        """ setAttachment(self, attachment: QOpenGLFramebufferObject.Attachment) """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ size(self) -> QSize """
        pass

    def sizes(self): # real signature unknown; restored from __doc__
        """ sizes(self) -> List[QSize] """
        return []

    def takeTexture(self, colorAttachmentIndex=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        takeTexture(self) -> int
        takeTexture(self, colorAttachmentIndex: int) -> int
        """
        return 0

    def texture(self): # real signature unknown; restored from __doc__
        """ texture(self) -> int """
        return 0

    def textures(self): # real signature unknown; restored from __doc__
        """ textures(self) -> List[int] """
        return []

    def toImage(self, flipped=None, colorAttachmentIndex=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        toImage(self) -> QImage
        toImage(self, flipped: bool) -> QImage
        toImage(self, flipped: bool, colorAttachmentIndex: int) -> QImage
        """
        return QImage

    def width(self): # real signature unknown; restored from __doc__
        """ width(self) -> int """
        return 0

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    CombinedDepthStencil = 1
    Depth = 2
    DontRestoreFramebufferBinding = 0
    NoAttachment = 0
    RestoreFrameBufferBinding = 2
    RestoreFramebufferBindingToDefault = 1


