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


from .QQuickItem import QQuickItem

class QQuickPaintedItem(QQuickItem):
    """ QQuickPaintedItem(parent: Optional[QQuickItem] = None) """
    def antialiasing(self): # real signature unknown; restored from __doc__
        """ antialiasing(self) -> bool """
        return False

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def childMouseEventFilter(self, *args, **kwargs): # real signature unknown
        pass

    def classBegin(self, *args, **kwargs): # real signature unknown
        pass

    def componentComplete(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def contentsBoundingRect(self): # real signature unknown; restored from __doc__
        """ contentsBoundingRect(self) -> QRectF """
        pass

    def contentsScale(self): # real signature unknown; restored from __doc__
        """ contentsScale(self) -> float """
        return 0.0

    def contentsScaleChanged(self, *args, **kwargs): # real signature unknown
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

    def contentsSize(self): # real signature unknown; restored from __doc__
        """ contentsSize(self) -> QSize """
        pass

    def contentsSizeChanged(self, *args, **kwargs): # real signature unknown
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

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def dragEnterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dragLeaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dragMoveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dropEvent(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, *args, **kwargs): # real signature unknown
        pass

    def fillColor(self): # real signature unknown; restored from __doc__
        """ fillColor(self) -> QColor """
        pass

    def fillColorChanged(self, *args, **kwargs): # real signature unknown
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

    def focusInEvent(self, *args, **kwargs): # real signature unknown
        pass

    def focusOutEvent(self, *args, **kwargs): # real signature unknown
        pass

    def geometryChanged(self, *args, **kwargs): # real signature unknown
        pass

    def heightValid(self, *args, **kwargs): # real signature unknown
        pass

    def hoverEnterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def hoverLeaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def hoverMoveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def inputMethodEvent(self, *args, **kwargs): # real signature unknown
        pass

    def isComponentComplete(self, *args, **kwargs): # real signature unknown
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def isTextureProvider(self): # real signature unknown; restored from __doc__
        """ isTextureProvider(self) -> bool """
        return False

    def itemChange(self, a0, a1): # real signature unknown; restored from __doc__
        """ itemChange(self, a0: QQuickItem.ItemChange, a1: QQuickItem.ItemChangeData) """
        pass

    def keyPressEvent(self, *args, **kwargs): # real signature unknown
        pass

    def keyReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mipmap(self): # real signature unknown; restored from __doc__
        """ mipmap(self) -> bool """
        return False

    def mouseDoubleClickEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mouseMoveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mousePressEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mouseReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mouseUngrabEvent(self, *args, **kwargs): # real signature unknown
        pass

    def opaquePainting(self): # real signature unknown; restored from __doc__
        """ opaquePainting(self) -> bool """
        return False

    def paint(self, painter, QPainter=None): # real signature unknown; restored from __doc__
        """ paint(self, painter: Optional[QPainter]) """
        pass

    def performanceHints(self): # real signature unknown; restored from __doc__
        """ performanceHints(self) -> QQuickPaintedItem.PerformanceHints """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def releaseResources(self): # real signature unknown; restored from __doc__
        """ releaseResources(self) """
        pass

    def renderTarget(self): # real signature unknown; restored from __doc__
        """ renderTarget(self) -> QQuickPaintedItem.RenderTarget """
        pass

    def renderTargetChanged(self, *args, **kwargs): # real signature unknown
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

    def resetContentsSize(self): # real signature unknown; restored from __doc__
        """ resetContentsSize(self) """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setAntialiasing(self, enable): # real signature unknown; restored from __doc__
        """ setAntialiasing(self, enable: bool) """
        pass

    def setContentsScale(self, a0): # real signature unknown; restored from __doc__
        """ setContentsScale(self, a0: float) """
        pass

    def setContentsSize(self, a0): # real signature unknown; restored from __doc__
        """ setContentsSize(self, a0: QSize) """
        pass

    def setFillColor(self, a0, QColor=None, Qt_GlobalColor=None): # real signature unknown; restored from __doc__
        """ setFillColor(self, a0: Union[QColor, Qt.GlobalColor]) """
        pass

    def setMipmap(self, enable): # real signature unknown; restored from __doc__
        """ setMipmap(self, enable: bool) """
        pass

    def setOpaquePainting(self, opaque): # real signature unknown; restored from __doc__
        """ setOpaquePainting(self, opaque: bool) """
        pass

    def setPerformanceHint(self, hint, enabled=True): # real signature unknown; restored from __doc__
        """ setPerformanceHint(self, hint: QQuickPaintedItem.PerformanceHint, enabled: bool = True) """
        pass

    def setPerformanceHints(self, hints, QQuickPaintedItem_PerformanceHints=None, QQuickPaintedItem_PerformanceHint=None): # real signature unknown; restored from __doc__
        """ setPerformanceHints(self, hints: Union[QQuickPaintedItem.PerformanceHints, QQuickPaintedItem.PerformanceHint]) """
        pass

    def setRenderTarget(self, target): # real signature unknown; restored from __doc__
        """ setRenderTarget(self, target: QQuickPaintedItem.RenderTarget) """
        pass

    def setTextureSize(self, size): # real signature unknown; restored from __doc__
        """ setTextureSize(self, size: QSize) """
        pass

    def textureProvider(self): # real signature unknown; restored from __doc__
        """ textureProvider(self) -> Optional[QSGTextureProvider] """
        pass

    def textureSize(self): # real signature unknown; restored from __doc__
        """ textureSize(self) -> QSize """
        pass

    def textureSizeChanged(self, *args, **kwargs): # real signature unknown
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

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def touchEvent(self, *args, **kwargs): # real signature unknown
        pass

    def touchUngrabEvent(self, *args, **kwargs): # real signature unknown
        pass

    def update(self, rect=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ update(self, rect: QRect = QRect()) """
        pass

    def updateInputMethod(self, *args, **kwargs): # real signature unknown
        pass

    def updatePaintNode(self, a0, QSGNode=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ updatePaintNode(self, a0: Optional[QSGNode], a1: Optional[QQuickItem.UpdatePaintNodeData]) -> Optional[QSGNode] """
        pass

    def updatePolish(self, *args, **kwargs): # real signature unknown
        pass

    def wheelEvent(self, *args, **kwargs): # real signature unknown
        pass

    def widthValid(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent, QQuickItem=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    FastFBOResizing = 1
    FramebufferObject = 1
    Image = 0
    InvertedYFramebufferObject = 2


