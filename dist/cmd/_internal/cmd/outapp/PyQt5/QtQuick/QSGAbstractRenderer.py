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


class QSGAbstractRenderer(__PyQt5_QtCore.QObject):
    # no doc
    def clearColor(self): # real signature unknown; restored from __doc__
        """ clearColor(self) -> QColor """
        pass

    def clearMode(self): # real signature unknown; restored from __doc__
        """ clearMode(self) -> QSGAbstractRenderer.ClearMode """
        pass

    def deviceRect(self): # real signature unknown; restored from __doc__
        """ deviceRect(self) -> QRect """
        pass

    def projectionMatrix(self): # real signature unknown; restored from __doc__
        """ projectionMatrix(self) -> QMatrix4x4 """
        pass

    def renderScene(self, fboId=0): # real signature unknown; restored from __doc__
        """ renderScene(self, fboId: int = 0) """
        pass

    def sceneGraphChanged(self, *args, **kwargs): # real signature unknown
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

    def setClearColor(self, color, QColor=None, Qt_GlobalColor=None): # real signature unknown; restored from __doc__
        """ setClearColor(self, color: Union[QColor, Qt.GlobalColor]) """
        pass

    def setClearMode(self, mode, QSGAbstractRenderer_ClearMode=None, QSGAbstractRenderer_ClearModeBit=None): # real signature unknown; restored from __doc__
        """ setClearMode(self, mode: Union[QSGAbstractRenderer.ClearMode, QSGAbstractRenderer.ClearModeBit]) """
        pass

    def setDeviceRect(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setDeviceRect(self, rect: QRect)
        setDeviceRect(self, size: QSize)
        """
        pass

    def setProjectionMatrix(self, matrix): # real signature unknown; restored from __doc__
        """ setProjectionMatrix(self, matrix: QMatrix4x4) """
        pass

    def setProjectionMatrixToRect(self, rect, flags=None, QSGAbstractRenderer_MatrixTransformFlags=None, QSGAbstractRenderer_MatrixTransformFlag=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setProjectionMatrixToRect(self, rect: QRectF)
        setProjectionMatrixToRect(self, rect: QRectF, flags: Union[QSGAbstractRenderer.MatrixTransformFlags, QSGAbstractRenderer.MatrixTransformFlag])
        """
        pass

    def setViewportRect(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setViewportRect(self, rect: QRect)
        setViewportRect(self, size: QSize)
        """
        pass

    def viewportRect(self): # real signature unknown; restored from __doc__
        """ viewportRect(self) -> QRect """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    ClearColorBuffer = 1
    ClearDepthBuffer = 2
    ClearStencilBuffer = 4
    MatrixTransformFlipY = 1


