# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QPaintEngine(__sip.simplewrapper):
    """ QPaintEngine(features: Union[QPaintEngine.PaintEngineFeatures, QPaintEngine.PaintEngineFeature] = QPaintEngine.PaintEngineFeatures()) """
    def begin(self, pdev, QPaintDevice=None): # real signature unknown; restored from __doc__
        """ begin(self, pdev: Optional[QPaintDevice]) -> bool """
        return False

    def drawEllipse(self, r): # real signature unknown; restored from __doc__ with multiple overloads
        """
        drawEllipse(self, r: QRectF)
        drawEllipse(self, r: QRect)
        """
        pass

    def drawImage(self, r, pm, sr, flags, Qt_ImageConversionFlags=None, Qt_ImageConversionFlag=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ drawImage(self, r: QRectF, pm: QImage, sr: QRectF, flags: Union[Qt.ImageConversionFlags, Qt.ImageConversionFlag] = Qt.AutoColor) """
        pass

    def drawLines(self, lines, PyQt5_sip_array=None, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        drawLines(self, lines: Optional[PyQt5.sip.array[QLine]])
        drawLines(self, lines: Optional[PyQt5.sip.array[QLineF]])
        """
        pass

    def drawPath(self, path): # real signature unknown; restored from __doc__
        """ drawPath(self, path: QPainterPath) """
        pass

    def drawPixmap(self, r, pm, sr): # real signature unknown; restored from __doc__
        """ drawPixmap(self, r: QRectF, pm: QPixmap, sr: QRectF) """
        pass

    def drawPoints(self, points, PyQt5_sip_array=None, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        drawPoints(self, points: Optional[PyQt5.sip.array[Union[QPointF, QPoint]]])
        drawPoints(self, points: Optional[PyQt5.sip.array[QPoint]])
        """
        pass

    def drawPolygon(self, points, PyQt5_sip_array=None, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        drawPolygon(self, points: Optional[PyQt5.sip.array[Union[QPointF, QPoint]]], mode: QPaintEngine.PolygonDrawMode)
        drawPolygon(self, points: Optional[PyQt5.sip.array[QPoint]], mode: QPaintEngine.PolygonDrawMode)
        """
        pass

    def drawRects(self, rects, PyQt5_sip_array=None, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        drawRects(self, rects: Optional[PyQt5.sip.array[QRect]])
        drawRects(self, rects: Optional[PyQt5.sip.array[QRectF]])
        """
        pass

    def drawTextItem(self, p, QPointF=None, QPoint=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ drawTextItem(self, p: Union[QPointF, QPoint], textItem: QTextItem) """
        pass

    def drawTiledPixmap(self, r, pixmap, s, QPointF=None, QPoint=None): # real signature unknown; restored from __doc__
        """ drawTiledPixmap(self, r: QRectF, pixmap: QPixmap, s: Union[QPointF, QPoint]) """
        pass

    def end(self): # real signature unknown; restored from __doc__
        """ end(self) -> bool """
        return False

    def hasFeature(self, feature, QPaintEngine_PaintEngineFeatures=None, QPaintEngine_PaintEngineFeature=None): # real signature unknown; restored from __doc__
        """ hasFeature(self, feature: Union[QPaintEngine.PaintEngineFeatures, QPaintEngine.PaintEngineFeature]) -> bool """
        return False

    def isActive(self): # real signature unknown; restored from __doc__
        """ isActive(self) -> bool """
        return False

    def paintDevice(self): # real signature unknown; restored from __doc__
        """ paintDevice(self) -> Optional[QPaintDevice] """
        pass

    def painter(self): # real signature unknown; restored from __doc__
        """ painter(self) -> Optional[QPainter] """
        pass

    def setActive(self, newState): # real signature unknown; restored from __doc__
        """ setActive(self, newState: bool) """
        pass

    def setPaintDevice(self, device, QPaintDevice=None): # real signature unknown; restored from __doc__
        """ setPaintDevice(self, device: Optional[QPaintDevice]) """
        pass

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> QPaintEngine.Type """
        pass

    def updateState(self, state): # real signature unknown; restored from __doc__
        """ updateState(self, state: QPaintEngineState) """
        pass

    def __init__(self, features, QPaintEngine_PaintEngineFeatures=None, QPaintEngine_PaintEngineFeature=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    AllDirty = 65535
    AllFeatures = -1
    AlphaBlend = 128
    Antialiasing = 1024
    BlendModes = 32768
    Blitter = 16
    BrushStroke = 2048
    ConicalGradientFill = 64
    ConstantOpacity = 4096
    ConvexMode = 2
    CoreGraphics = 3
    Direct2D = 17
    Direct3D = 11
    DirtyBackground = 16
    DirtyBackgroundMode = 32
    DirtyBrush = 2
    DirtyBrushOrigin = 4
    DirtyClipEnabled = 2048
    DirtyClipPath = 256
    DirtyClipRegion = 128
    DirtyCompositionMode = 1024
    DirtyFont = 8
    DirtyHints = 512
    DirtyOpacity = 4096
    DirtyPen = 1
    DirtyTransform = 64
    LinearGradientFill = 16
    MacPrinter = 4
    MaskedBrush = 8192
    MaxUser = 100
    ObjectBoundingModeGradients = 65536
    OddEvenMode = 0
    OpenGL = 7
    OpenGL2 = 14
    OpenVG = 13
    PaintBuffer = 15
    PainterPaths = 512
    PaintOutsidePaintEvent = 536870912
    PatternBrush = 8
    PatternTransform = 2
    Pdf = 12
    PerspectiveTransform = 16384
    Picture = 8
    PixmapTransform = 4
    PolylineMode = 3
    PorterDuff = 256
    PostScript = 6
    PrimitiveTransform = 1
    QuickDraw = 2
    QWindowSystem = 5
    RadialGradientFill = 32
    Raster = 10
    RasterOpModes = 131072
    SVG = 9
    User = 50
    WindingMode = 1
    Windows = 1
    X11 = 0


