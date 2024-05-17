# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QOpenGLShader(__PyQt5_QtCore.QObject):
    """ QOpenGLShader(type: Union[QOpenGLShader.ShaderType, QOpenGLShader.ShaderTypeBit], parent: Optional[QObject] = None) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def compileSourceCode(self, source, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        compileSourceCode(self, source: Union[QByteArray, bytes, bytearray]) -> bool
        compileSourceCode(self, source: Optional[str]) -> bool
        """
        return False

    def compileSourceFile(self, fileName, p_str=None): # real signature unknown; restored from __doc__
        """ compileSourceFile(self, fileName: Optional[str]) -> bool """
        return False

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def hasOpenGLShaders(self, type, QOpenGLShader_ShaderType=None, QOpenGLShader_ShaderTypeBit=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ hasOpenGLShaders(type: Union[QOpenGLShader.ShaderType, QOpenGLShader.ShaderTypeBit], context: Optional[QOpenGLContext] = None) -> bool """
        pass

    def isCompiled(self): # real signature unknown; restored from __doc__
        """ isCompiled(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def log(self): # real signature unknown; restored from __doc__
        """ log(self) -> str """
        return ""

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def shaderId(self): # real signature unknown; restored from __doc__
        """ shaderId(self) -> int """
        return 0

    def shaderType(self): # real signature unknown; restored from __doc__
        """ shaderType(self) -> QOpenGLShader.ShaderType """
        pass

    def sourceCode(self): # real signature unknown; restored from __doc__
        """ sourceCode(self) -> QByteArray """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, type, QOpenGLShader_ShaderType=None, QOpenGLShader_ShaderTypeBit=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    Compute = 32
    Fragment = 2
    Geometry = 4
    TessellationControl = 8
    TessellationEvaluation = 16
    Vertex = 1


