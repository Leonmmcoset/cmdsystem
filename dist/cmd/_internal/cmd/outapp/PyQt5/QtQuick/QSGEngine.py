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


class QSGEngine(__PyQt5_QtCore.QObject):
    """ QSGEngine(parent: Optional[QObject] = None) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def createImageNode(self): # real signature unknown; restored from __doc__
        """ createImageNode(self) -> Optional[QSGImageNode] """
        pass

    def createRectangleNode(self): # real signature unknown; restored from __doc__
        """ createRectangleNode(self) -> Optional[QSGRectangleNode] """
        pass

    def createRenderer(self): # real signature unknown; restored from __doc__
        """ createRenderer(self) -> Optional[QSGAbstractRenderer] """
        pass

    def createTextureFromId(self, id, size, options, QSGEngine_CreateTextureOptions=None, QSGEngine_CreateTextureOption=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ createTextureFromId(self, id: int, size: QSize, options: Union[QSGEngine.CreateTextureOptions, QSGEngine.CreateTextureOption] = QSGEngine.CreateTextureOption()) -> Optional[QSGTexture] """
        pass

    def createTextureFromImage(self, image, options, QSGEngine_CreateTextureOptions=None, QSGEngine_CreateTextureOption=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ createTextureFromImage(self, image: QImage, options: Union[QSGEngine.CreateTextureOptions, QSGEngine.CreateTextureOption] = QSGEngine.CreateTextureOption()) -> Optional[QSGTexture] """
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def initialize(self, context, QOpenGLContext=None): # real signature unknown; restored from __doc__
        """ initialize(self, context: Optional[QOpenGLContext]) """
        pass

    def invalidate(self): # real signature unknown; restored from __doc__
        """ invalidate(self) """
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def rendererInterface(self): # real signature unknown; restored from __doc__
        """ rendererInterface(self) -> Optional[QSGRendererInterface] """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent, QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    TextureCanUseAtlas = 8
    TextureHasAlphaChannel = 1
    TextureIsOpaque = 16
    TextureOwnsGLTexture = 4


