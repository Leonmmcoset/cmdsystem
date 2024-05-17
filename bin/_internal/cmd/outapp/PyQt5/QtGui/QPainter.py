# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QPainter(__sip.simplewrapper):
    """
    QPainter()
    QPainter(a0: Optional[QPaintDevice])
    """
    def background(self): # real signature unknown; restored from __doc__
        """ background(self) -> QBrush """
        return QBrush

    def backgroundMode(self): # real signature unknown; restored from __doc__
        """ backgroundMode(self) -> Qt.BGMode """
        pass

    def begin(self, a0, QPaintDevice=None): # real signature unknown; restored from __doc__
        """ begin(self, a0: Optional[QPaintDevice]) -> bool """
        return False

    def beginNativePainting(self): # real signature unknown; restored from __doc__
        """ beginNativePainting(self) """
        pass

    def boundingRect(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        boundingRect(self, rect: QRectF, flags: int, text: Optional[str]) -> QRectF
        boundingRect(self, rect: QRect, flags: int, text: Optional[str]) -> QRect
        boundingRect(self, rectangle: QRectF, text: Optional[str], option: QTextOption = QTextOption()) -> QRectF
        boundingRect(self, x: int, y: int, w: int, h: int, flags: int, text: Optional[str]) -> QRect
        """
        pass

    def brush(self): # real signature unknown; restored from __doc__
        """ brush(self) -> QBrush """
        return QBrush

    def brushOrigin(self): # real signature unknown; restored from __doc__
        """ brushOrigin(self) -> QPoint """
        pass

    def clipBoundingRect(self): # real signature unknown; restored from __doc__
        """ clipBoundingRect(self) -> QRectF """
        pass

    def clipPath(self): # real signature unknown; restored from __doc__
        """ clipPath(self) -> QPainterPath """
        return QPainterPath

    def clipRegion(self): # real signature unknown; restored from __doc__
        """ clipRegion(self) -> QRegion """
        return QRegion

    def combinedTransform(self): # real signature unknown; restored from __doc__
        """ combinedTransform(self) -> QTransform """
        return QTransform

    def compositionMode(self): # real signature unknown; restored from __doc__
        """ compositionMode(self) -> QPainter.CompositionMode """
        pass

    def device(self): # real signature unknown; restored from __doc__
        """ device(self) -> Optional[QPaintDevice] """
        pass

    def deviceTransform(self): # real signature unknown; restored from __doc__
        """ deviceTransform(self) -> QTransform """
        return QTransform

    def drawArc(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        drawArc(self, rect: QRectF, a: int, alen: int)
        drawArc(self, r: QRect, a: int, alen: int)
        drawArc(self, x: int, y: int, w: int, h: int, a: int, alen: int)
        """
        pass

    def drawChord(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        drawChord(self, rect: QRectF, a: int, alen: int)
        drawChord(self, rect: QRect, a: int, alen: int)
        drawChord(self, x: int, y: int, w: int, h: int, a: int, alen: int)
        """
        pass

    def drawConvexPolygon(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        drawConvexPolygon(self, poly: QPolygonF)
        drawConvexPolygon(self, poly: QPolygon)
        drawConvexPolygon(self, points: Optional[PyQt5.sip.array[Union[QPointF, QPoint]]])
        drawConvexPolygon(self, point: Optional[Union[QPointF, QPoint]], *args: Union[QPointF, QPoint])
        drawConvexPolygon(self, points: Optional[PyQt5.sip.array[QPoint]])
        drawConvexPolygon(self, point: Optional[QPoint], *args: QPoint)
        """
        pass

    def drawEllipse(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        drawEllipse(self, r: QRectF)
        drawEllipse(self, r: QRect)
        drawEllipse(self, x: int, y: int, w: int, h: int)
        drawEllipse(self, center: Union[QPointF, QPoint], rx: float, ry: float)
        drawEllipse(self, center: QPoint, rx: int, ry: int)
        """
        pass

    def drawGlyphRun(self, position, QPointF=None, QPoint=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ drawGlyphRun(self, position: Union[QPointF, QPoint], glyphRun: QGlyphRun) """
        pass

    def drawImage(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        drawImage(self, r: QRectF, image: QImage)
        drawImage(self, r: QRect, image: QImage)
        drawImage(self, p: Union[QPointF, QPoint], image: QImage)
        drawImage(self, p: QPoint, image: QImage)
        drawImage(self, x: int, y: int, image: QImage, sx: int = 0, sy: int = 0, sw: int = -1, sh: int = -1, flags: Union[Qt.ImageConversionFlags, Qt.ImageConversionFlag] = Qt.ImageConversionFlag.AutoColor)
        drawImage(self, targetRect: QRectF, image: QImage, sourceRect: QRectF, flags: Union[Qt.ImageConversionFlags, Qt.ImageConversionFlag] = Qt.ImageConversionFlag.AutoColor)
        drawImage(self, targetRect: QRect, image: QImage, sourceRect: QRect, flags: Union[Qt.ImageConversionFlags, Qt.ImageConversionFlag] = Qt.ImageConversionFlag.AutoColor)
        drawImage(self, p: Union[QPointF, QPoint], image: QImage, sr: QRectF, flags: Union[Qt.ImageConversionFlags, Qt.ImageConversionFlag] = Qt.ImageConversionFlag.AutoColor)
        drawImage(self, p: QPoint, image: QImage, sr: QRect, flags: Union[Qt.ImageConversionFlags, Qt.ImageConversionFlag] = Qt.ImageConversionFlag.AutoColor)
        """
        pass

    def drawLine(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        drawLine(self, l: QLineF)
        drawLine(self, line: QLine)
        drawLine(self, x1: int, y1: int, x2: int, y2: int)
        drawLine(self, p1: QPoint, p2: QPoint)
        drawLine(self, p1: Union[QPointF, QPoint], p2: Union[QPointF, QPoint])
        """
        pass

    def drawLines(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        drawLines(self, lines: Optional[PyQt5.sip.array[QLineF]])
        drawLines(self, line: Optional[QLineF], *args: QLineF)
        drawLines(self, pointPairs: Optional[PyQt5.sip.array[Union[QPointF, QPoint]]])
        drawLines(self, pointPair: Optional[Union[QPointF, QPoint]], *args: Union[QPointF, QPoint])
        drawLines(self, lines: Optional[PyQt5.sip.array[QLine]])
        drawLines(self, line: Optional[QLine], *args: QLine)
        drawLines(self, pointPairs: Optional[PyQt5.sip.array[QPoint]])
        drawLines(self, pointPair: Optional[QPoint], *args: QPoint)
        """
        pass

    def drawPath(self, path): # real signature unknown; restored from __doc__
        """ drawPath(self, path: QPainterPath) """
        pass

    def drawPicture(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        drawPicture(self, p: Union[QPointF, QPoint], picture: QPicture)
        drawPicture(self, x: int, y: int, p: QPicture)
        drawPicture(self, pt: QPoint, p: QPicture)
        """
        pass

    def drawPie(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        drawPie(self, rect: QRectF, a: int, alen: int)
        drawPie(self, rect: QRect, a: int, alen: int)
        drawPie(self, x: int, y: int, w: int, h: int, a: int, alen: int)
        """
        pass

    def drawPixmap(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        drawPixmap(self, targetRect: QRectF, pixmap: QPixmap, sourceRect: QRectF)
        drawPixmap(self, targetRect: QRect, pixmap: QPixmap, sourceRect: QRect)
        drawPixmap(self, p: Union[QPointF, QPoint], pm: QPixmap)
        drawPixmap(self, p: QPoint, pm: QPixmap)
        drawPixmap(self, r: QRect, pm: QPixmap)
        drawPixmap(self, x: int, y: int, pm: QPixmap)
        drawPixmap(self, x: int, y: int, w: int, h: int, pm: QPixmap)
        drawPixmap(self, x: int, y: int, w: int, h: int, pm: QPixmap, sx: int, sy: int, sw: int, sh: int)
        drawPixmap(self, x: int, y: int, pm: QPixmap, sx: int, sy: int, sw: int, sh: int)
        drawPixmap(self, p: Union[QPointF, QPoint], pm: QPixmap, sr: QRectF)
        drawPixmap(self, p: QPoint, pm: QPixmap, sr: QRect)
        """
        pass

    def drawPixmapFragments(self, fragments, PyQt5_sip_array=None, QPainter_PixmapFragment=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ drawPixmapFragments(self, fragments: Optional[PyQt5.sip.array[QPainter.PixmapFragment]], pixmap: QPixmap, hints: QPainter.PixmapFragmentHints = 0) """
        pass

    def drawPoint(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        drawPoint(self, p: Union[QPointF, QPoint])
        drawPoint(self, x: int, y: int)
        drawPoint(self, p: QPoint)
        """
        pass

    def drawPoints(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        drawPoints(self, points: QPolygonF)
        drawPoints(self, points: QPolygon)
        drawPoints(self, points: Optional[PyQt5.sip.array[Union[QPointF, QPoint]]])
        drawPoints(self, point: Optional[Union[QPointF, QPoint]], *args: Union[QPointF, QPoint])
        drawPoints(self, points: Optional[PyQt5.sip.array[QPoint]])
        drawPoints(self, point: Optional[QPoint], *args: QPoint)
        """
        pass

    def drawPolygon(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        drawPolygon(self, points: QPolygonF, fillRule: Qt.FillRule = Qt.OddEvenFill)
        drawPolygon(self, points: QPolygon, fillRule: Qt.FillRule = Qt.OddEvenFill)
        drawPolygon(self, points: Optional[PyQt5.sip.array[Union[QPointF, QPoint]]], fillRule: Qt.FillRule = Qt.OddEvenFill)
        drawPolygon(self, point: Optional[Union[QPointF, QPoint]], *args: Union[QPointF, QPoint])
        drawPolygon(self, points: Optional[PyQt5.sip.array[QPoint]], fillRule: Qt.FillRule = Qt.OddEvenFill)
        drawPolygon(self, point: Optional[QPoint], *args: QPoint)
        """
        pass

    def drawPolyline(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        drawPolyline(self, polyline: QPolygonF)
        drawPolyline(self, polyline: QPolygon)
        drawPolyline(self, points: Optional[PyQt5.sip.array[Union[QPointF, QPoint]]])
        drawPolyline(self, point: Optional[Union[QPointF, QPoint]], *args: Union[QPointF, QPoint])
        drawPolyline(self, points: Optional[PyQt5.sip.array[QPoint]])
        drawPolyline(self, point: Optional[QPoint], *args: QPoint)
        """
        pass

    def drawRect(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        drawRect(self, rect: QRectF)
        drawRect(self, x: int, y: int, w: int, h: int)
        drawRect(self, r: QRect)
        """
        pass

    def drawRects(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        drawRects(self, rects: Optional[PyQt5.sip.array[QRectF]])
        drawRects(self, rect: Optional[QRectF], *args: QRectF)
        drawRects(self, rects: Optional[PyQt5.sip.array[QRect]])
        drawRects(self, rect: Optional[QRect], *args: QRect)
        """
        pass

    def drawRoundedRect(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        drawRoundedRect(self, rect: QRectF, xRadius: float, yRadius: float, mode: Qt.SizeMode = Qt.AbsoluteSize)
        drawRoundedRect(self, x: int, y: int, w: int, h: int, xRadius: float, yRadius: float, mode: Qt.SizeMode = Qt.AbsoluteSize)
        drawRoundedRect(self, rect: QRect, xRadius: float, yRadius: float, mode: Qt.SizeMode = Qt.AbsoluteSize)
        """
        pass

    def drawStaticText(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        drawStaticText(self, topLeftPosition: Union[QPointF, QPoint], staticText: QStaticText)
        drawStaticText(self, p: QPoint, staticText: QStaticText)
        drawStaticText(self, x: int, y: int, staticText: QStaticText)
        """
        pass

    def drawText(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        drawText(self, p: Union[QPointF, QPoint], s: Optional[str])
        drawText(self, rectangle: QRectF, flags: int, text: Optional[str]) -> Optional[QRectF]
        drawText(self, rectangle: QRect, flags: int, text: Optional[str]) -> Optional[QRect]
        drawText(self, rectangle: QRectF, text: Optional[str], option: QTextOption = QTextOption())
        drawText(self, p: QPoint, s: Optional[str])
        drawText(self, x: int, y: int, width: int, height: int, flags: int, text: Optional[str]) -> Optional[QRect]
        drawText(self, x: int, y: int, s: Optional[str])
        """
        pass

    def drawTiledPixmap(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        drawTiledPixmap(self, rectangle: QRectF, pixmap: QPixmap, pos: Union[QPointF, QPoint] = QPointF())
        drawTiledPixmap(self, rectangle: QRect, pixmap: QPixmap, pos: QPoint = QPoint())
        drawTiledPixmap(self, x: int, y: int, width: int, height: int, pixmap: QPixmap, sx: int = 0, sy: int = 0)
        """
        pass

    def end(self): # real signature unknown; restored from __doc__
        """ end(self) -> bool """
        return False

    def endNativePainting(self): # real signature unknown; restored from __doc__
        """ endNativePainting(self) """
        pass

    def eraseRect(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        eraseRect(self, a0: QRectF)
        eraseRect(self, rect: QRect)
        eraseRect(self, x: int, y: int, w: int, h: int)
        """
        pass

    def fillPath(self, path, brush, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ fillPath(self, path: QPainterPath, brush: Union[QBrush, Union[QColor, Qt.GlobalColor], QGradient]) """
        pass

    def fillRect(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        fillRect(self, a0: QRectF, a1: Union[QBrush, Union[QColor, Qt.GlobalColor], QGradient])
        fillRect(self, a0: QRect, a1: Union[QBrush, Union[QColor, Qt.GlobalColor], QGradient])
        fillRect(self, x: int, y: int, w: int, h: int, b: Union[QBrush, Union[QColor, Qt.GlobalColor], QGradient])
        fillRect(self, a0: QRectF, color: Union[QColor, Qt.GlobalColor])
        fillRect(self, a0: QRect, color: Union[QColor, Qt.GlobalColor])
        fillRect(self, x: int, y: int, w: int, h: int, b: Union[QColor, Qt.GlobalColor])
        fillRect(self, x: int, y: int, w: int, h: int, c: Qt.GlobalColor)
        fillRect(self, r: QRect, c: Qt.GlobalColor)
        fillRect(self, r: QRectF, c: Qt.GlobalColor)
        fillRect(self, x: int, y: int, w: int, h: int, style: Qt.BrushStyle)
        fillRect(self, r: QRect, style: Qt.BrushStyle)
        fillRect(self, r: QRectF, style: Qt.BrushStyle)
        fillRect(self, x: int, y: int, w: int, h: int, preset: QGradient.Preset)
        fillRect(self, r: QRect, preset: QGradient.Preset)
        fillRect(self, r: QRectF, preset: QGradient.Preset)
        """
        pass

    def font(self): # real signature unknown; restored from __doc__
        """ font(self) -> QFont """
        return QFont

    def fontInfo(self): # real signature unknown; restored from __doc__
        """ fontInfo(self) -> QFontInfo """
        return QFontInfo

    def fontMetrics(self): # real signature unknown; restored from __doc__
        """ fontMetrics(self) -> QFontMetrics """
        return QFontMetrics

    def hasClipping(self): # real signature unknown; restored from __doc__
        """ hasClipping(self) -> bool """
        return False

    def isActive(self): # real signature unknown; restored from __doc__
        """ isActive(self) -> bool """
        return False

    def layoutDirection(self): # real signature unknown; restored from __doc__
        """ layoutDirection(self) -> Qt.LayoutDirection """
        pass

    def opacity(self): # real signature unknown; restored from __doc__
        """ opacity(self) -> float """
        return 0.0

    def paintEngine(self): # real signature unknown; restored from __doc__
        """ paintEngine(self) -> Optional[QPaintEngine] """
        pass

    def pen(self): # real signature unknown; restored from __doc__
        """ pen(self) -> QPen """
        return QPen

    def renderHints(self): # real signature unknown; restored from __doc__
        """ renderHints(self) -> QPainter.RenderHints """
        pass

    def resetTransform(self): # real signature unknown; restored from __doc__
        """ resetTransform(self) """
        pass

    def restore(self): # real signature unknown; restored from __doc__
        """ restore(self) """
        pass

    def rotate(self, a): # real signature unknown; restored from __doc__
        """ rotate(self, a: float) """
        pass

    def save(self): # real signature unknown; restored from __doc__
        """ save(self) """
        pass

    def scale(self, sx, sy): # real signature unknown; restored from __doc__
        """ scale(self, sx: float, sy: float) """
        pass

    def setBackground(self, bg, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setBackground(self, bg: Union[QBrush, Union[QColor, Qt.GlobalColor], QGradient]) """
        pass

    def setBackgroundMode(self, mode): # real signature unknown; restored from __doc__
        """ setBackgroundMode(self, mode: Qt.BGMode) """
        pass

    def setBrush(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setBrush(self, brush: Union[QBrush, Union[QColor, Qt.GlobalColor], QGradient])
        setBrush(self, style: Qt.BrushStyle)
        """
        pass

    def setBrushOrigin(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setBrushOrigin(self, a0: Union[QPointF, QPoint])
        setBrushOrigin(self, x: int, y: int)
        setBrushOrigin(self, p: QPoint)
        """
        pass

    def setClipPath(self, path, operation=None): # real signature unknown; restored from __doc__
        """ setClipPath(self, path: QPainterPath, operation: Qt.ClipOperation = Qt.ReplaceClip) """
        pass

    def setClipping(self, enable): # real signature unknown; restored from __doc__
        """ setClipping(self, enable: bool) """
        pass

    def setClipRect(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setClipRect(self, rectangle: QRectF, operation: Qt.ClipOperation = Qt.ReplaceClip)
        setClipRect(self, x: int, y: int, width: int, height: int, operation: Qt.ClipOperation = Qt.ReplaceClip)
        setClipRect(self, rectangle: QRect, operation: Qt.ClipOperation = Qt.ReplaceClip)
        """
        pass

    def setClipRegion(self, region, operation=None): # real signature unknown; restored from __doc__
        """ setClipRegion(self, region: QRegion, operation: Qt.ClipOperation = Qt.ReplaceClip) """
        pass

    def setCompositionMode(self, mode): # real signature unknown; restored from __doc__
        """ setCompositionMode(self, mode: QPainter.CompositionMode) """
        pass

    def setFont(self, f): # real signature unknown; restored from __doc__
        """ setFont(self, f: QFont) """
        pass

    def setLayoutDirection(self, direction): # real signature unknown; restored from __doc__
        """ setLayoutDirection(self, direction: Qt.LayoutDirection) """
        pass

    def setOpacity(self, opacity): # real signature unknown; restored from __doc__
        """ setOpacity(self, opacity: float) """
        pass

    def setPen(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setPen(self, color: Union[QColor, Qt.GlobalColor])
        setPen(self, pen: Union[QPen, Union[QColor, Qt.GlobalColor]])
        setPen(self, style: Qt.PenStyle)
        """
        pass

    def setRenderHint(self, hint, on=True): # real signature unknown; restored from __doc__
        """ setRenderHint(self, hint: QPainter.RenderHint, on: bool = True) """
        pass

    def setRenderHints(self, hints, QPainter_RenderHints=None, QPainter_RenderHint=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setRenderHints(self, hints: Union[QPainter.RenderHints, QPainter.RenderHint], on: bool = True) """
        pass

    def setTransform(self, transform, combine=False): # real signature unknown; restored from __doc__
        """ setTransform(self, transform: QTransform, combine: bool = False) """
        pass

    def setViewport(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setViewport(self, viewport: QRect)
        setViewport(self, x: int, y: int, w: int, h: int)
        """
        pass

    def setViewTransformEnabled(self, enable): # real signature unknown; restored from __doc__
        """ setViewTransformEnabled(self, enable: bool) """
        pass

    def setWindow(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setWindow(self, window: QRect)
        setWindow(self, x: int, y: int, w: int, h: int)
        """
        pass

    def setWorldMatrixEnabled(self, enabled): # real signature unknown; restored from __doc__
        """ setWorldMatrixEnabled(self, enabled: bool) """
        pass

    def setWorldTransform(self, matrix, combine=False): # real signature unknown; restored from __doc__
        """ setWorldTransform(self, matrix: QTransform, combine: bool = False) """
        pass

    def shear(self, sh, sv): # real signature unknown; restored from __doc__
        """ shear(self, sh: float, sv: float) """
        pass

    def strokePath(self, path, pen, QPen=None, Union=None, QColor=None, Qt_GlobalColor=None): # real signature unknown; restored from __doc__
        """ strokePath(self, path: QPainterPath, pen: Union[QPen, Union[QColor, Qt.GlobalColor]]) """
        pass

    def testRenderHint(self, hint): # real signature unknown; restored from __doc__
        """ testRenderHint(self, hint: QPainter.RenderHint) -> bool """
        return False

    def transform(self): # real signature unknown; restored from __doc__
        """ transform(self) -> QTransform """
        return QTransform

    def translate(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        translate(self, offset: Union[QPointF, QPoint])
        translate(self, dx: float, dy: float)
        translate(self, offset: QPoint)
        """
        pass

    def viewport(self): # real signature unknown; restored from __doc__
        """ viewport(self) -> QRect """
        pass

    def viewTransformEnabled(self): # real signature unknown; restored from __doc__
        """ viewTransformEnabled(self) -> bool """
        return False

    def window(self): # real signature unknown; restored from __doc__
        """ window(self) -> QRect """
        pass

    def worldMatrixEnabled(self): # real signature unknown; restored from __doc__
        """ worldMatrixEnabled(self) -> bool """
        return False

    def worldTransform(self): # real signature unknown; restored from __doc__
        """ worldTransform(self) -> QTransform """
        return QTransform

    def __enter__(self): # real signature unknown; restored from __doc__
        """ __enter__(self) -> Any """
        pass

    def __exit__(self, type, value, traceback): # real signature unknown; restored from __doc__
        """ __exit__(self, type: Any, value: Any, traceback: Any) """
        pass

    def __init__(self, a0=None, QPaintDevice=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    Antialiasing = 1
    CompositionMode_Clear = 2
    CompositionMode_ColorBurn = 19
    CompositionMode_ColorDodge = 18
    CompositionMode_Darken = 16
    CompositionMode_Destination = 4
    CompositionMode_DestinationAtop = 10
    CompositionMode_DestinationIn = 6
    CompositionMode_DestinationOut = 8
    CompositionMode_DestinationOver = 1
    CompositionMode_Difference = 22
    CompositionMode_Exclusion = 23
    CompositionMode_HardLight = 20
    CompositionMode_Lighten = 17
    CompositionMode_Multiply = 13
    CompositionMode_Overlay = 15
    CompositionMode_Plus = 12
    CompositionMode_Screen = 14
    CompositionMode_SoftLight = 21
    CompositionMode_Source = 3
    CompositionMode_SourceAtop = 9
    CompositionMode_SourceIn = 5
    CompositionMode_SourceOut = 7
    CompositionMode_SourceOver = 0
    CompositionMode_Xor = 11
    HighQualityAntialiasing = 8
    LosslessImageRendering = 64
    NonCosmeticDefaultPen = 16
    OpaqueHint = 1
    Qt4CompatiblePainting = 32
    RasterOp_ClearDestination = 35
    RasterOp_NotDestination = 37
    RasterOp_NotSource = 30
    RasterOp_NotSourceAndDestination = 31
    RasterOp_NotSourceAndNotDestination = 27
    RasterOp_NotSourceOrDestination = 33
    RasterOp_NotSourceOrNotDestination = 28
    RasterOp_NotSourceXorDestination = 29
    RasterOp_SetDestination = 36
    RasterOp_SourceAndDestination = 25
    RasterOp_SourceAndNotDestination = 32
    RasterOp_SourceOrDestination = 24
    RasterOp_SourceOrNotDestination = 34
    RasterOp_SourceXorDestination = 26
    SmoothPixmapTransform = 4
    TextAntialiasing = 2


