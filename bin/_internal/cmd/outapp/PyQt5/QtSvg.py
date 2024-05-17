# encoding: utf-8
# module PyQt5.QtSvg
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtSvg.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import PyQt5.QtWidgets as __PyQt5_QtWidgets


# no functions
# classes

class QGraphicsSvgItem(__PyQt5_QtWidgets.QGraphicsObject):
    """
    QGraphicsSvgItem(parent: Optional[QGraphicsItem] = None)
    QGraphicsSvgItem(fileName: Optional[str], parent: Optional[QGraphicsItem] = None)
    """
    def boundingRect(self): # real signature unknown; restored from __doc__
        """ boundingRect(self) -> QRectF """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def contextMenuEvent(self, *args, **kwargs): # real signature unknown
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

    def elementId(self): # real signature unknown; restored from __doc__
        """ elementId(self) -> str """
        return ""

    def event(self, *args, **kwargs): # real signature unknown
        pass

    def focusInEvent(self, *args, **kwargs): # real signature unknown
        pass

    def focusOutEvent(self, *args, **kwargs): # real signature unknown
        pass

    def hoverEnterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def hoverLeaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def hoverMoveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def inputMethodEvent(self, *args, **kwargs): # real signature unknown
        pass

    def inputMethodQuery(self, *args, **kwargs): # real signature unknown
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def itemChange(self, *args, **kwargs): # real signature unknown
        pass

    def keyPressEvent(self, *args, **kwargs): # real signature unknown
        pass

    def keyReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def maximumCacheSize(self): # real signature unknown; restored from __doc__
        """ maximumCacheSize(self) -> QSize """
        pass

    def mouseDoubleClickEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mouseMoveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mousePressEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mouseReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def paint(self, painter, QPainter=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ paint(self, painter: Optional[QPainter], option: Optional[QStyleOptionGraphicsItem], widget: Optional[QWidget] = None) """
        pass

    def prepareGeometryChange(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def renderer(self): # real signature unknown; restored from __doc__
        """ renderer(self) -> Optional[QSvgRenderer] """
        pass

    def sceneEvent(self, *args, **kwargs): # real signature unknown
        pass

    def sceneEventFilter(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setElementId(self, id, p_str=None): # real signature unknown; restored from __doc__
        """ setElementId(self, id: Optional[str]) """
        pass

    def setMaximumCacheSize(self, size): # real signature unknown; restored from __doc__
        """ setMaximumCacheSize(self, size: QSize) """
        pass

    def setSharedRenderer(self, renderer, QSvgRenderer=None): # real signature unknown; restored from __doc__
        """ setSharedRenderer(self, renderer: Optional[QSvgRenderer]) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> int """
        return 0

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

    def wheelEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


class QSvgGenerator(__PyQt5_QtGui.QPaintDevice):
    """ QSvgGenerator() """
    def description(self): # real signature unknown; restored from __doc__
        """ description(self) -> str """
        return ""

    def fileName(self): # real signature unknown; restored from __doc__
        """ fileName(self) -> str """
        return ""

    def metric(self, metric): # real signature unknown; restored from __doc__
        """ metric(self, metric: QPaintDevice.PaintDeviceMetric) -> int """
        return 0

    def outputDevice(self): # real signature unknown; restored from __doc__
        """ outputDevice(self) -> Optional[QIODevice] """
        pass

    def paintEngine(self): # real signature unknown; restored from __doc__
        """ paintEngine(self) -> Optional[QPaintEngine] """
        pass

    def resolution(self): # real signature unknown; restored from __doc__
        """ resolution(self) -> int """
        return 0

    def setDescription(self, description, p_str=None): # real signature unknown; restored from __doc__
        """ setDescription(self, description: Optional[str]) """
        pass

    def setFileName(self, fileName, p_str=None): # real signature unknown; restored from __doc__
        """ setFileName(self, fileName: Optional[str]) """
        pass

    def setOutputDevice(self, outputDevice, QIODevice=None): # real signature unknown; restored from __doc__
        """ setOutputDevice(self, outputDevice: Optional[QIODevice]) """
        pass

    def setResolution(self, resolution): # real signature unknown; restored from __doc__
        """ setResolution(self, resolution: int) """
        pass

    def setSize(self, size): # real signature unknown; restored from __doc__
        """ setSize(self, size: QSize) """
        pass

    def setTitle(self, title, p_str=None): # real signature unknown; restored from __doc__
        """ setTitle(self, title: Optional[str]) """
        pass

    def setViewBox(self, viewBox): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setViewBox(self, viewBox: QRect)
        setViewBox(self, viewBox: QRectF)
        """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ size(self) -> QSize """
        pass

    def title(self): # real signature unknown; restored from __doc__
        """ title(self) -> str """
        return ""

    def viewBox(self): # real signature unknown; restored from __doc__
        """ viewBox(self) -> QRect """
        pass

    def viewBoxF(self): # real signature unknown; restored from __doc__
        """ viewBoxF(self) -> QRectF """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass


class QSvgRenderer(__PyQt5_QtCore.QObject):
    """
    QSvgRenderer(parent: Optional[QObject] = None)
    QSvgRenderer(filename: Optional[str], parent: Optional[QObject] = None)
    QSvgRenderer(contents: Union[QByteArray, bytes, bytearray], parent: Optional[QObject] = None)
    QSvgRenderer(contents: Optional[QXmlStreamReader], parent: Optional[QObject] = None)
    """
    def animated(self): # real signature unknown; restored from __doc__
        """ animated(self) -> bool """
        return False

    def animationDuration(self): # real signature unknown; restored from __doc__
        """ animationDuration(self) -> int """
        return 0

    def aspectRatioMode(self): # real signature unknown; restored from __doc__
        """ aspectRatioMode(self) -> Qt.AspectRatioMode """
        pass

    def boundsOnElement(self, id, p_str=None): # real signature unknown; restored from __doc__
        """ boundsOnElement(self, id: Optional[str]) -> QRectF """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def currentFrame(self): # real signature unknown; restored from __doc__
        """ currentFrame(self) -> int """
        return 0

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def defaultSize(self): # real signature unknown; restored from __doc__
        """ defaultSize(self) -> QSize """
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def elementExists(self, id, p_str=None): # real signature unknown; restored from __doc__
        """ elementExists(self, id: Optional[str]) -> bool """
        return False

    def framesPerSecond(self): # real signature unknown; restored from __doc__
        """ framesPerSecond(self) -> int """
        return 0

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def load(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        load(self, filename: Optional[str]) -> bool
        load(self, contents: Union[QByteArray, bytes, bytearray]) -> bool
        load(self, contents: Optional[QXmlStreamReader]) -> bool
        """
        return False

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def render(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        render(self, p: Optional[QPainter])
        render(self, p: Optional[QPainter], bounds: QRectF)
        render(self, painter: Optional[QPainter], elementId: Optional[str], bounds: QRectF = QRectF())
        """
        pass

    def repaintNeeded(self, *args, **kwargs): # real signature unknown
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

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setAspectRatioMode(self, mode): # real signature unknown; restored from __doc__
        """ setAspectRatioMode(self, mode: Qt.AspectRatioMode) """
        pass

    def setCurrentFrame(self, a0): # real signature unknown; restored from __doc__
        """ setCurrentFrame(self, a0: int) """
        pass

    def setFramesPerSecond(self, num): # real signature unknown; restored from __doc__
        """ setFramesPerSecond(self, num: int) """
        pass

    def setViewBox(self, viewbox): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setViewBox(self, viewbox: QRect)
        setViewBox(self, viewbox: QRectF)
        """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def transformForElement(self, id, p_str=None): # real signature unknown; restored from __doc__
        """ transformForElement(self, id: Optional[str]) -> QTransform """
        pass

    def viewBox(self): # real signature unknown; restored from __doc__
        """ viewBox(self) -> QRect """
        pass

    def viewBoxF(self): # real signature unknown; restored from __doc__
        """ viewBoxF(self) -> QRectF """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


class QSvgWidget(__PyQt5_QtWidgets.QWidget):
    """
    QSvgWidget(parent: Optional[QWidget] = None)
    QSvgWidget(file: Optional[str], parent: Optional[QWidget] = None)
    """
    def actionEvent(self, *args, **kwargs): # real signature unknown
        pass

    def changeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def closeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def contextMenuEvent(self, *args, **kwargs): # real signature unknown
        pass

    def create(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def destroy(self, *args, **kwargs): # real signature unknown
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

    def enterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, *args, **kwargs): # real signature unknown
        pass

    def focusInEvent(self, *args, **kwargs): # real signature unknown
        pass

    def focusNextChild(self, *args, **kwargs): # real signature unknown
        pass

    def focusNextPrevChild(self, *args, **kwargs): # real signature unknown
        pass

    def focusOutEvent(self, *args, **kwargs): # real signature unknown
        pass

    def focusPreviousChild(self, *args, **kwargs): # real signature unknown
        pass

    def hideEvent(self, *args, **kwargs): # real signature unknown
        pass

    def initPainter(self, *args, **kwargs): # real signature unknown
        pass

    def inputMethodEvent(self, *args, **kwargs): # real signature unknown
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def keyPressEvent(self, *args, **kwargs): # real signature unknown
        pass

    def keyReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def leaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def load(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        load(self, file: Optional[str])
        load(self, contents: Union[QByteArray, bytes, bytearray])
        """
        pass

    def metric(self, *args, **kwargs): # real signature unknown
        pass

    def mouseDoubleClickEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mouseMoveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mousePressEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mouseReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def moveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def nativeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def paintEvent(self, event, QPaintEvent=None): # real signature unknown; restored from __doc__
        """ paintEvent(self, event: Optional[QPaintEvent]) """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def renderer(self): # real signature unknown; restored from __doc__
        """ renderer(self) -> Optional[QSvgRenderer] """
        pass

    def resizeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def sharedPainter(self, *args, **kwargs): # real signature unknown
        pass

    def showEvent(self, *args, **kwargs): # real signature unknown
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> QSize """
        pass

    def tabletEvent(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

    def wheelEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


# variables with complex values



