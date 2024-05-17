# encoding: utf-8
# module PyQt5.QtQuick3D
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtQuick3D.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtQml as __PyQt5_QtQml
import sip as __sip


# no functions
# classes

class QQuick3D(__sip.simplewrapper):
    """
    QQuick3D()
    QQuick3D(a0: QQuick3D)
    """
    def idealSurfaceFormat(self, samples=-1): # real signature unknown; restored from __doc__
        """ idealSurfaceFormat(samples: int = -1) -> QSurfaceFormat """
        pass

    def __init__(self, a0=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QQuick3DObject(__PyQt5_QtCore.QObject, __PyQt5_QtQml.QQmlParserStatus):
    # no doc
    def parentItem(self): # real signature unknown; restored from __doc__
        """ parentItem(self) -> Optional[QQuick3DObject] """
        pass

    def setParentItem(self, parentItem, QQuick3DObject=None): # real signature unknown; restored from __doc__
        """ setParentItem(self, parentItem: Optional[QQuick3DObject]) """
        pass

    def setState(self, state, p_str=None): # real signature unknown; restored from __doc__
        """ setState(self, state: Optional[str]) """
        pass

    def state(self): # real signature unknown; restored from __doc__
        """ state(self) -> str """
        return ""

    def stateChanged(self, *args, **kwargs): # real signature unknown
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

    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class QQuick3DGeometry(QQuick3DObject):
    """ QQuick3DGeometry(parent: Optional[QQuick3DObject] = None) """
    def addAttribute(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        addAttribute(self, semantic: QQuick3DGeometry.Attribute.Semantic, offset: int, componentType: QQuick3DGeometry.Attribute.ComponentType)
        addAttribute(self, att: QQuick3DGeometry.Attribute)
        """
        pass

    def attribute(self, index): # real signature unknown; restored from __doc__
        """ attribute(self, index: int) -> QQuick3DGeometry.Attribute """
        pass

    def attributeCount(self): # real signature unknown; restored from __doc__
        """ attributeCount(self) -> int """
        return 0

    def boundsMax(self): # real signature unknown; restored from __doc__
        """ boundsMax(self) -> QVector3D """
        pass

    def boundsMin(self): # real signature unknown; restored from __doc__
        """ boundsMin(self) -> QVector3D """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def classBegin(self, *args, **kwargs): # real signature unknown
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def componentComplete(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def indexBuffer(self): # real signature unknown; restored from __doc__
        """ indexBuffer(self) -> QByteArray """
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def name(self): # real signature unknown; restored from __doc__
        """ name(self) -> str """
        return ""

    def nameChanged(self, *args, **kwargs): # real signature unknown
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

    def primitiveType(self): # real signature unknown; restored from __doc__
        """ primitiveType(self) -> QQuick3DGeometry.PrimitiveType """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setBounds(self, min, max): # real signature unknown; restored from __doc__
        """ setBounds(self, min: QVector3D, max: QVector3D) """
        pass

    def setIndexData(self, data, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ setIndexData(self, data: Union[QByteArray, bytes, bytearray]) """
        pass

    def setName(self, name, p_str=None): # real signature unknown; restored from __doc__
        """ setName(self, name: Optional[str]) """
        pass

    def setPrimitiveType(self, type): # real signature unknown; restored from __doc__
        """ setPrimitiveType(self, type: QQuick3DGeometry.PrimitiveType) """
        pass

    def setStride(self, stride): # real signature unknown; restored from __doc__
        """ setStride(self, stride: int) """
        pass

    def setVertexData(self, data, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ setVertexData(self, data: Union[QByteArray, bytes, bytearray]) """
        pass

    def stride(self): # real signature unknown; restored from __doc__
        """ stride(self) -> int """
        return 0

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def vertexBuffer(self): # real signature unknown; restored from __doc__
        """ vertexBuffer(self) -> QByteArray """
        pass

    def __init__(self, parent, QQuick3DObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass



# variables with complex values



