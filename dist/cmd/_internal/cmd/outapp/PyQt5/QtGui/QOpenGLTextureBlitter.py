# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QOpenGLTextureBlitter(__sip.simplewrapper):
    """ QOpenGLTextureBlitter() """
    def bind(self, target=None): # real signature unknown; restored from __doc__
        """ bind(self, target: int = GL_TEXTURE_2D) """
        pass

    def blit(self, texture, targetTransform, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        blit(self, texture: int, targetTransform: QMatrix4x4, sourceOrigin: QOpenGLTextureBlitter.Origin)
        blit(self, texture: int, targetTransform: QMatrix4x4, sourceTransform: QMatrix3x3)
        """
        pass

    def create(self): # real signature unknown; restored from __doc__
        """ create(self) -> bool """
        return False

    def destroy(self): # real signature unknown; restored from __doc__
        """ destroy(self) """
        pass

    def isCreated(self): # real signature unknown; restored from __doc__
        """ isCreated(self) -> bool """
        return False

    def release(self): # real signature unknown; restored from __doc__
        """ release(self) """
        pass

    def setOpacity(self, opacity): # real signature unknown; restored from __doc__
        """ setOpacity(self, opacity: float) """
        pass

    def setRedBlueSwizzle(self, swizzle): # real signature unknown; restored from __doc__
        """ setRedBlueSwizzle(self, swizzle: bool) """
        pass

    def sourceTransform(self, subTexture, textureSize, origin): # real signature unknown; restored from __doc__
        """ sourceTransform(subTexture: QRectF, textureSize: QSize, origin: QOpenGLTextureBlitter.Origin) -> QMatrix3x3 """
        return QMatrix3x3

    def supportsExternalOESTarget(self): # real signature unknown; restored from __doc__
        """ supportsExternalOESTarget(self) -> bool """
        return False

    def targetTransform(self, target, viewport): # real signature unknown; restored from __doc__
        """ targetTransform(target: QRectF, viewport: QRect) -> QMatrix4x4 """
        return QMatrix4x4

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    OriginBottomLeft = 0
    OriginTopLeft = 1


