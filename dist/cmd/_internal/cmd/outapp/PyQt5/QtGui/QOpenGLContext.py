# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QOpenGLContext(__PyQt5_QtCore.QObject):
    """ QOpenGLContext(parent: Optional[QObject] = None) """
    def aboutToBeDestroyed(self, *args, **kwargs): # real signature unknown
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

    def areSharing(self, first, QOpenGLContext=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ areSharing(first: Optional[QOpenGLContext], second: Optional[QOpenGLContext]) -> bool """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def create(self): # real signature unknown; restored from __doc__
        """ create(self) -> bool """
        return False

    def currentContext(self): # real signature unknown; restored from __doc__
        """ currentContext() -> Optional[QOpenGLContext] """
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def defaultFramebufferObject(self): # real signature unknown; restored from __doc__
        """ defaultFramebufferObject(self) -> int """
        return 0

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def doneCurrent(self): # real signature unknown; restored from __doc__
        """ doneCurrent(self) """
        pass

    def extensions(self): # real signature unknown; restored from __doc__
        """ extensions(self) -> Set[QByteArray] """
        pass

    def format(self): # real signature unknown; restored from __doc__
        """ format(self) -> QSurfaceFormat """
        return QSurfaceFormat

    def getProcAddress(self, procName, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ getProcAddress(self, procName: Union[QByteArray, bytes, bytearray]) -> Optional[PyQt5.sip.voidptr] """
        pass

    def globalShareContext(self): # real signature unknown; restored from __doc__
        """ globalShareContext() -> Optional[QOpenGLContext] """
        pass

    def hasExtension(self, extension, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ hasExtension(self, extension: Union[QByteArray, bytes, bytearray]) -> bool """
        return False

    def isOpenGLES(self): # real signature unknown; restored from __doc__
        """ isOpenGLES(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def makeCurrent(self, surface, QSurface=None): # real signature unknown; restored from __doc__
        """ makeCurrent(self, surface: Optional[QSurface]) -> bool """
        return False

    def nativeHandle(self): # real signature unknown; restored from __doc__
        """ nativeHandle(self) -> Any """
        pass

    def openGLModuleHandle(self): # real signature unknown; restored from __doc__
        """ openGLModuleHandle() -> Optional[PyQt5.sip.voidptr] """
        pass

    def openGLModuleType(self): # real signature unknown; restored from __doc__
        """ openGLModuleType() -> QOpenGLContext.OpenGLModuleType """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def screen(self): # real signature unknown; restored from __doc__
        """ screen(self) -> Optional[QScreen] """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setFormat(self, format): # real signature unknown; restored from __doc__
        """ setFormat(self, format: QSurfaceFormat) """
        pass

    def setNativeHandle(self, handle): # real signature unknown; restored from __doc__
        """ setNativeHandle(self, handle: Any) """
        pass

    def setScreen(self, screen, QScreen=None): # real signature unknown; restored from __doc__
        """ setScreen(self, screen: Optional[QScreen]) """
        pass

    def setShareContext(self, shareContext, QOpenGLContext=None): # real signature unknown; restored from __doc__
        """ setShareContext(self, shareContext: Optional[QOpenGLContext]) """
        pass

    def shareContext(self): # real signature unknown; restored from __doc__
        """ shareContext(self) -> Optional[QOpenGLContext] """
        pass

    def shareGroup(self): # real signature unknown; restored from __doc__
        """ shareGroup(self) -> Optional[QOpenGLContextGroup] """
        pass

    def supportsThreadedOpenGL(self): # real signature unknown; restored from __doc__
        """ supportsThreadedOpenGL() -> bool """
        return False

    def surface(self): # real signature unknown; restored from __doc__
        """ surface(self) -> Optional[QSurface] """
        pass

    def swapBuffers(self, surface, QSurface=None): # real signature unknown; restored from __doc__
        """ swapBuffers(self, surface: Optional[QSurface]) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def versionFunctions(self, versionProfile, QOpenGLVersionProfile=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ versionFunctions(self, versionProfile: Optional[QOpenGLVersionProfile] = None) -> Any """
        pass

    def __init__(self, parent, QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    LibGL = 0
    LibGLES = 1


