# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QOpenGLShaderProgram(__PyQt5_QtCore.QObject):
    """ QOpenGLShaderProgram(parent: Optional[QObject] = None) """
    def addCacheableShaderFromSourceCode(self, type, QOpenGLShader_ShaderType=None, QOpenGLShader_ShaderTypeBit=None, *args, **kwargs): # real signature unknown; restored from __doc__ with multiple overloads
        """
        addCacheableShaderFromSourceCode(self, type: Union[QOpenGLShader.ShaderType, QOpenGLShader.ShaderTypeBit], source: Union[QByteArray, bytes, bytearray]) -> bool
        addCacheableShaderFromSourceCode(self, type: Union[QOpenGLShader.ShaderType, QOpenGLShader.ShaderTypeBit], source: Optional[str]) -> bool
        """
        pass

    def addCacheableShaderFromSourceFile(self, type, QOpenGLShader_ShaderType=None, QOpenGLShader_ShaderTypeBit=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ addCacheableShaderFromSourceFile(self, type: Union[QOpenGLShader.ShaderType, QOpenGLShader.ShaderTypeBit], fileName: Optional[str]) -> bool """
        pass

    def addShader(self, shader, QOpenGLShader=None): # real signature unknown; restored from __doc__
        """ addShader(self, shader: Optional[QOpenGLShader]) -> bool """
        return False

    def addShaderFromSourceCode(self, type, QOpenGLShader_ShaderType=None, QOpenGLShader_ShaderTypeBit=None, *args, **kwargs): # real signature unknown; restored from __doc__ with multiple overloads
        """
        addShaderFromSourceCode(self, type: Union[QOpenGLShader.ShaderType, QOpenGLShader.ShaderTypeBit], source: Union[QByteArray, bytes, bytearray]) -> bool
        addShaderFromSourceCode(self, type: Union[QOpenGLShader.ShaderType, QOpenGLShader.ShaderTypeBit], source: Optional[str]) -> bool
        """
        pass

    def addShaderFromSourceFile(self, type, QOpenGLShader_ShaderType=None, QOpenGLShader_ShaderTypeBit=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ addShaderFromSourceFile(self, type: Union[QOpenGLShader.ShaderType, QOpenGLShader.ShaderTypeBit], fileName: Optional[str]) -> bool """
        pass

    def attributeLocation(self, name, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        attributeLocation(self, name: Union[QByteArray, bytes, bytearray]) -> int
        attributeLocation(self, name: Optional[str]) -> int
        """
        return 0

    def bind(self): # real signature unknown; restored from __doc__
        """ bind(self) -> bool """
        return False

    def bindAttributeLocation(self, name, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        bindAttributeLocation(self, name: Union[QByteArray, bytes, bytearray], location: int)
        bindAttributeLocation(self, name: Optional[str], location: int)
        """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def create(self): # real signature unknown; restored from __doc__
        """ create(self) -> bool """
        return False

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def defaultInnerTessellationLevels(self): # real signature unknown; restored from __doc__
        """ defaultInnerTessellationLevels(self) -> List[float] """
        return []

    def defaultOuterTessellationLevels(self): # real signature unknown; restored from __doc__
        """ defaultOuterTessellationLevels(self) -> List[float] """
        return []

    def disableAttributeArray(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        disableAttributeArray(self, location: int)
        disableAttributeArray(self, name: Optional[str])
        """
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def enableAttributeArray(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        enableAttributeArray(self, location: int)
        enableAttributeArray(self, name: Optional[str])
        """
        pass

    def hasOpenGLShaderPrograms(self, context, QOpenGLContext=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ hasOpenGLShaderPrograms(context: Optional[QOpenGLContext] = None) -> bool """
        pass

    def isLinked(self): # real signature unknown; restored from __doc__
        """ isLinked(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def link(self): # real signature unknown; restored from __doc__
        """ link(self) -> bool """
        return False

    def log(self): # real signature unknown; restored from __doc__
        """ log(self) -> str """
        return ""

    def maxGeometryOutputVertices(self): # real signature unknown; restored from __doc__
        """ maxGeometryOutputVertices(self) -> int """
        return 0

    def patchVertexCount(self): # real signature unknown; restored from __doc__
        """ patchVertexCount(self) -> int """
        return 0

    def programId(self): # real signature unknown; restored from __doc__
        """ programId(self) -> int """
        return 0

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def release(self): # real signature unknown; restored from __doc__
        """ release(self) """
        pass

    def removeAllShaders(self): # real signature unknown; restored from __doc__
        """ removeAllShaders(self) """
        pass

    def removeShader(self, shader, QOpenGLShader=None): # real signature unknown; restored from __doc__
        """ removeShader(self, shader: Optional[QOpenGLShader]) """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setAttributeArray(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setAttributeArray(self, location: int, values: PYQT_SHADER_ATTRIBUTE_ARRAY)
        setAttributeArray(self, name: Optional[str], values: PYQT_SHADER_ATTRIBUTE_ARRAY)
        """
        pass

    def setAttributeBuffer(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setAttributeBuffer(self, location: int, type: int, offset: int, tupleSize: int, stride: int = 0)
        setAttributeBuffer(self, name: Optional[str], type: int, offset: int, tupleSize: int, stride: int = 0)
        """
        pass

    def setAttributeValue(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setAttributeValue(self, location: int, value: float)
        setAttributeValue(self, location: int, x: float, y: float)
        setAttributeValue(self, location: int, x: float, y: float, z: float)
        setAttributeValue(self, location: int, x: float, y: float, z: float, w: float)
        setAttributeValue(self, location: int, value: QVector2D)
        setAttributeValue(self, location: int, value: QVector3D)
        setAttributeValue(self, location: int, value: QVector4D)
        setAttributeValue(self, location: int, value: Union[QColor, Qt.GlobalColor])
        setAttributeValue(self, name: Optional[str], value: float)
        setAttributeValue(self, name: Optional[str], x: float, y: float)
        setAttributeValue(self, name: Optional[str], x: float, y: float, z: float)
        setAttributeValue(self, name: Optional[str], x: float, y: float, z: float, w: float)
        setAttributeValue(self, name: Optional[str], value: QVector2D)
        setAttributeValue(self, name: Optional[str], value: QVector3D)
        setAttributeValue(self, name: Optional[str], value: QVector4D)
        setAttributeValue(self, name: Optional[str], value: Union[QColor, Qt.GlobalColor])
        """
        pass

    def setDefaultInnerTessellationLevels(self, levels, p_float=None): # real signature unknown; restored from __doc__
        """ setDefaultInnerTessellationLevels(self, levels: Iterable[float]) """
        pass

    def setDefaultOuterTessellationLevels(self, levels, p_float=None): # real signature unknown; restored from __doc__
        """ setDefaultOuterTessellationLevels(self, levels: Iterable[float]) """
        pass

    def setPatchVertexCount(self, count): # real signature unknown; restored from __doc__
        """ setPatchVertexCount(self, count: int) """
        pass

    def setUniformValue(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setUniformValue(self, location: int, value: int)
        setUniformValue(self, location: int, value: float)
        setUniformValue(self, location: int, x: float, y: float)
        setUniformValue(self, location: int, x: float, y: float, z: float)
        setUniformValue(self, location: int, x: float, y: float, z: float, w: float)
        setUniformValue(self, location: int, value: QVector2D)
        setUniformValue(self, location: int, value: QVector3D)
        setUniformValue(self, location: int, value: QVector4D)
        setUniformValue(self, location: int, color: Union[QColor, Qt.GlobalColor])
        setUniformValue(self, location: int, point: QPoint)
        setUniformValue(self, location: int, point: Union[QPointF, QPoint])
        setUniformValue(self, location: int, size: QSize)
        setUniformValue(self, location: int, size: QSizeF)
        setUniformValue(self, location: int, value: QMatrix2x2)
        setUniformValue(self, location: int, value: QMatrix2x3)
        setUniformValue(self, location: int, value: QMatrix2x4)
        setUniformValue(self, location: int, value: QMatrix3x2)
        setUniformValue(self, location: int, value: QMatrix3x3)
        setUniformValue(self, location: int, value: QMatrix3x4)
        setUniformValue(self, location: int, value: QMatrix4x2)
        setUniformValue(self, location: int, value: QMatrix4x3)
        setUniformValue(self, location: int, value: QMatrix4x4)
        setUniformValue(self, location: int, value: QTransform)
        setUniformValue(self, name: Optional[str], value: int)
        setUniformValue(self, name: Optional[str], value: float)
        setUniformValue(self, name: Optional[str], x: float, y: float)
        setUniformValue(self, name: Optional[str], x: float, y: float, z: float)
        setUniformValue(self, name: Optional[str], x: float, y: float, z: float, w: float)
        setUniformValue(self, name: Optional[str], value: QVector2D)
        setUniformValue(self, name: Optional[str], value: QVector3D)
        setUniformValue(self, name: Optional[str], value: QVector4D)
        setUniformValue(self, name: Optional[str], color: Union[QColor, Qt.GlobalColor])
        setUniformValue(self, name: Optional[str], point: QPoint)
        setUniformValue(self, name: Optional[str], point: Union[QPointF, QPoint])
        setUniformValue(self, name: Optional[str], size: QSize)
        setUniformValue(self, name: Optional[str], size: QSizeF)
        setUniformValue(self, name: Optional[str], value: QMatrix2x2)
        setUniformValue(self, name: Optional[str], value: QMatrix2x3)
        setUniformValue(self, name: Optional[str], value: QMatrix2x4)
        setUniformValue(self, name: Optional[str], value: QMatrix3x2)
        setUniformValue(self, name: Optional[str], value: QMatrix3x3)
        setUniformValue(self, name: Optional[str], value: QMatrix3x4)
        setUniformValue(self, name: Optional[str], value: QMatrix4x2)
        setUniformValue(self, name: Optional[str], value: QMatrix4x3)
        setUniformValue(self, name: Optional[str], value: QMatrix4x4)
        setUniformValue(self, name: Optional[str], value: QTransform)
        """
        pass

    def setUniformValueArray(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setUniformValueArray(self, location: int, values: PYQT_SHADER_UNIFORM_VALUE_ARRAY)
        setUniformValueArray(self, name: Optional[str], values: PYQT_SHADER_UNIFORM_VALUE_ARRAY)
        """
        pass

    def shaders(self): # real signature unknown; restored from __doc__
        """ shaders(self) -> List[QOpenGLShader] """
        return []

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def uniformLocation(self, name, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        uniformLocation(self, name: Union[QByteArray, bytes, bytearray]) -> int
        uniformLocation(self, name: Optional[str]) -> int
        """
        return 0

    def __init__(self, parent, QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass


