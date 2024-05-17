# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


# functions

def qAlpha(rgb): # real signature unknown; restored from __doc__
    """
    qAlpha(rgb: QRgba64) -> int
    qAlpha(rgb: int) -> int
    """
    return 0

def qBlue(rgb): # real signature unknown; restored from __doc__
    """
    qBlue(rgb: QRgba64) -> int
    qBlue(rgb: int) -> int
    """
    return 0

def qFuzzyCompare(m1, m2): # real signature unknown; restored from __doc__
    """
    qFuzzyCompare(m1: QMatrix4x4, m2: QMatrix4x4) -> bool
    qFuzzyCompare(q1: QQuaternion, q2: QQuaternion) -> bool
    qFuzzyCompare(t1: QTransform, t2: QTransform) -> bool
    qFuzzyCompare(v1: QVector2D, v2: QVector2D) -> bool
    qFuzzyCompare(v1: QVector3D, v2: QVector3D) -> bool
    qFuzzyCompare(v1: QVector4D, v2: QVector4D) -> bool
    """
    return False

def qGray(r, g, b): # real signature unknown; restored from __doc__
    """
    qGray(r: int, g: int, b: int) -> int
    qGray(rgb: int) -> int
    """
    return 0

def qGreen(rgb): # real signature unknown; restored from __doc__
    """
    qGreen(rgb: QRgba64) -> int
    qGreen(rgb: int) -> int
    """
    return 0

def qIsGray(rgb): # real signature unknown; restored from __doc__
    """ qIsGray(rgb: int) -> bool """
    return False

def qPixelFormatAlpha(channelSize, typeInterpretation=None): # real signature unknown; restored from __doc__
    """ qPixelFormatAlpha(channelSize: int, typeInterpretation: QPixelFormat.TypeInterpretation = QPixelFormat.UnsignedInteger) -> QPixelFormat """
    return QPixelFormat

def qPixelFormatCmyk(channelSize, alphaSize=0, alphaUsage=None, alphaPosition=None, typeInterpretation=None): # real signature unknown; restored from __doc__
    """ qPixelFormatCmyk(channelSize: int, alphaSize: int = 0, alphaUsage: QPixelFormat.AlphaUsage = QPixelFormat.IgnoresAlpha, alphaPosition: QPixelFormat.AlphaPosition = QPixelFormat.AtBeginning, typeInterpretation: QPixelFormat.TypeInterpretation = QPixelFormat.UnsignedInteger) -> QPixelFormat """
    return QPixelFormat

def qPixelFormatGrayscale(channelSize, typeInterpretation=None): # real signature unknown; restored from __doc__
    """ qPixelFormatGrayscale(channelSize: int, typeInterpretation: QPixelFormat.TypeInterpretation = QPixelFormat.UnsignedInteger) -> QPixelFormat """
    return QPixelFormat

def qPixelFormatHsl(channelSize, alphaSize=0, alphaUsage=None, alphaPosition=None, typeInterpretation=None): # real signature unknown; restored from __doc__
    """ qPixelFormatHsl(channelSize: int, alphaSize: int = 0, alphaUsage: QPixelFormat.AlphaUsage = QPixelFormat.IgnoresAlpha, alphaPosition: QPixelFormat.AlphaPosition = QPixelFormat.AtBeginning, typeInterpretation: QPixelFormat.TypeInterpretation = QPixelFormat.FloatingPoint) -> QPixelFormat """
    return QPixelFormat

def qPixelFormatHsv(channelSize, alphaSize=0, alphaUsage=None, alphaPosition=None, typeInterpretation=None): # real signature unknown; restored from __doc__
    """ qPixelFormatHsv(channelSize: int, alphaSize: int = 0, alphaUsage: QPixelFormat.AlphaUsage = QPixelFormat.IgnoresAlpha, alphaPosition: QPixelFormat.AlphaPosition = QPixelFormat.AtBeginning, typeInterpretation: QPixelFormat.TypeInterpretation = QPixelFormat.FloatingPoint) -> QPixelFormat """
    return QPixelFormat

def qPixelFormatRgba(red, green, blue, alfa, usage, position, premultiplied=None, typeInterpretation=None): # real signature unknown; restored from __doc__
    """ qPixelFormatRgba(red: int, green: int, blue: int, alfa: int, usage: QPixelFormat.AlphaUsage, position: QPixelFormat.AlphaPosition, premultiplied: QPixelFormat.AlphaPremultiplied = QPixelFormat.NotPremultiplied, typeInterpretation: QPixelFormat.TypeInterpretation = QPixelFormat.UnsignedInteger) -> QPixelFormat """
    return QPixelFormat

def qPixelFormatYuv(layout, alphaSize=0, alphaUsage=None, alphaPosition=None, premultiplied=None, typeInterpretation=None, byteOrder=None): # real signature unknown; restored from __doc__
    """ qPixelFormatYuv(layout: QPixelFormat.YUVLayout, alphaSize: int = 0, alphaUsage: QPixelFormat.AlphaUsage = QPixelFormat.IgnoresAlpha, alphaPosition: QPixelFormat.AlphaPosition = QPixelFormat.AtBeginning, premultiplied: QPixelFormat.AlphaPremultiplied = QPixelFormat.NotPremultiplied, typeInterpretation: QPixelFormat.TypeInterpretation = QPixelFormat.UnsignedByte, byteOrder: QPixelFormat.ByteOrder = QPixelFormat.LittleEndian) -> QPixelFormat """
    return QPixelFormat

def qPremultiply(c): # real signature unknown; restored from __doc__
    """
    qPremultiply(c: QRgba64) -> QRgba64
    qPremultiply(x: int) -> int
    """
    return QRgba64

def qRed(rgb): # real signature unknown; restored from __doc__
    """
    qRed(rgb: QRgba64) -> int
    qRed(rgb: int) -> int
    """
    return 0

def qRgb(r, g, b): # real signature unknown; restored from __doc__
    """ qRgb(r: int, g: int, b: int) -> int """
    return 0

def qRgba(r, g, b, a): # real signature unknown; restored from __doc__
    """ qRgba(r: int, g: int, b: int, a: int) -> int """
    return 0

def qRgba64(r, g, b, a): # real signature unknown; restored from __doc__
    """
    qRgba64(r: int, g: int, b: int, a: int) -> QRgba64
    qRgba64(c: int) -> QRgba64
    """
    return QRgba64

def qt_set_sequence_auto_mnemonic(b): # real signature unknown; restored from __doc__
    """ qt_set_sequence_auto_mnemonic(b: bool) """
    pass

def qUnpremultiply(c): # real signature unknown; restored from __doc__
    """
    qUnpremultiply(c: QRgba64) -> QRgba64
    qUnpremultiply(p: int) -> int
    """
    return QRgba64

# classes

from .QAbstractOpenGLFunctions import QAbstractOpenGLFunctions
from .QAbstractTextDocumentLayout import QAbstractTextDocumentLayout
from .QActionEvent import QActionEvent
from .QBackingStore import QBackingStore
from .QPaintDevice import QPaintDevice
from .QPixmap import QPixmap
from .QBitmap import QBitmap
from .QBrush import QBrush
from .QClipboard import QClipboard
from .QCloseEvent import QCloseEvent
from .QColor import QColor
from .QColorConstants import QColorConstants
from .QColorSpace import QColorSpace
from .QColorTransform import QColorTransform
from .QGradient import QGradient
from .QConicalGradient import QConicalGradient
from .QInputEvent import QInputEvent
from .QContextMenuEvent import QContextMenuEvent
from .QCursor import QCursor
from .QDesktopServices import QDesktopServices
from .QValidator import QValidator
from .QDoubleValidator import QDoubleValidator
from .QDrag import QDrag
from .QDropEvent import QDropEvent
from .QDragMoveEvent import QDragMoveEvent
from .QDragEnterEvent import QDragEnterEvent
from .QDragLeaveEvent import QDragLeaveEvent
from .QEnterEvent import QEnterEvent
from .QExposeEvent import QExposeEvent
from .QFileOpenEvent import QFileOpenEvent
from .QFocusEvent import QFocusEvent
from .QFont import QFont
from .QFontDatabase import QFontDatabase
from .QFontInfo import QFontInfo
from .QFontMetrics import QFontMetrics
from .QFontMetricsF import QFontMetricsF
from .QGlyphRun import QGlyphRun
from .QGuiApplication import QGuiApplication
from .QHelpEvent import QHelpEvent
from .QHideEvent import QHideEvent
from .QHoverEvent import QHoverEvent
from .QIcon import QIcon
from .QIconDragEvent import QIconDragEvent
from .QIconEngine import QIconEngine
from .QImage import QImage
from .QImageIOHandler import QImageIOHandler
from .QImageReader import QImageReader
from .QImageWriter import QImageWriter
from .QInputMethod import QInputMethod
from .QInputMethodEvent import QInputMethodEvent
from .QInputMethodQueryEvent import QInputMethodQueryEvent
from .QIntValidator import QIntValidator
from .QKeyEvent import QKeyEvent
from .QKeySequence import QKeySequence
from .QLinearGradient import QLinearGradient
from .QMatrix2x2 import QMatrix2x2
from .QMatrix2x3 import QMatrix2x3
from .QMatrix2x4 import QMatrix2x4
from .QMatrix3x2 import QMatrix3x2
from .QMatrix3x3 import QMatrix3x3
from .QMatrix3x4 import QMatrix3x4
from .QMatrix4x2 import QMatrix4x2
from .QMatrix4x3 import QMatrix4x3
from .QMatrix4x4 import QMatrix4x4
from .QMouseEvent import QMouseEvent
from .QMoveEvent import QMoveEvent
from .QMovie import QMovie
from .QNativeGestureEvent import QNativeGestureEvent
from .QSurface import QSurface
from .QOffscreenSurface import QOffscreenSurface
from .QOpenGLBuffer import QOpenGLBuffer
from .QOpenGLContext import QOpenGLContext
from .QOpenGLContextGroup import QOpenGLContextGroup
from .QOpenGLDebugLogger import QOpenGLDebugLogger
from .QOpenGLDebugMessage import QOpenGLDebugMessage
from .QOpenGLFramebufferObject import QOpenGLFramebufferObject
from .QOpenGLFramebufferObjectFormat import QOpenGLFramebufferObjectFormat
from .QOpenGLPaintDevice import QOpenGLPaintDevice
from .QOpenGLPixelTransferOptions import QOpenGLPixelTransferOptions
from .QOpenGLShader import QOpenGLShader
from .QOpenGLShaderProgram import QOpenGLShaderProgram
from .QOpenGLTexture import QOpenGLTexture
from .QOpenGLTextureBlitter import QOpenGLTextureBlitter
from .QOpenGLTimeMonitor import QOpenGLTimeMonitor
from .QOpenGLTimerQuery import QOpenGLTimerQuery
from .QOpenGLVersionProfile import QOpenGLVersionProfile
from .QOpenGLVertexArrayObject import QOpenGLVertexArrayObject
from .QWindow import QWindow
from .QPaintDeviceWindow import QPaintDeviceWindow
from .QOpenGLWindow import QOpenGLWindow
from .QPagedPaintDevice import QPagedPaintDevice
from .QPageLayout import QPageLayout
from .QPageSize import QPageSize
from .QPaintEngine import QPaintEngine
from .QPaintEngineState import QPaintEngineState
from .QPainter import QPainter
from .QPainterPath import QPainterPath
from .QPainterPathStroker import QPainterPathStroker
from .QPaintEvent import QPaintEvent
from .QPalette import QPalette
from .QPdfWriter import QPdfWriter
from .QPen import QPen
from .QPicture import QPicture
from .QPictureIO import QPictureIO
from .QPixelFormat import QPixelFormat
from .QPixmapCache import QPixmapCache
from .QPlatformSurfaceEvent import QPlatformSurfaceEvent
from .QPointingDeviceUniqueId import QPointingDeviceUniqueId
from .QPolygon import QPolygon
from .QPolygonF import QPolygonF
from .QQuaternion import QQuaternion
from .QRadialGradient import QRadialGradient
from .QRasterWindow import QRasterWindow
from .QRawFont import QRawFont
from .QRegExpValidator import QRegExpValidator
from .QRegion import QRegion
from .QRegularExpressionValidator import QRegularExpressionValidator
from .QResizeEvent import QResizeEvent
from .QRgba64 import QRgba64
from .QScreen import QScreen
from .QScrollEvent import QScrollEvent
from .QScrollPrepareEvent import QScrollPrepareEvent
from .QSessionManager import QSessionManager
from .QShortcutEvent import QShortcutEvent
from .QShowEvent import QShowEvent
from .QStandardItem import QStandardItem
from .QStandardItemModel import QStandardItemModel
from .QStaticText import QStaticText
from .QStatusTipEvent import QStatusTipEvent
from .QStyleHints import QStyleHints
from .QSurfaceFormat import QSurfaceFormat
from .QSyntaxHighlighter import QSyntaxHighlighter
from .QTabletEvent import QTabletEvent
from .QTextBlock import QTextBlock
from .QTextFormat import QTextFormat
from .QTextBlockFormat import QTextBlockFormat
from .QTextObject import QTextObject
from .QTextBlockGroup import QTextBlockGroup
from .QTextBlockUserData import QTextBlockUserData
from .QTextCharFormat import QTextCharFormat
from .QTextCursor import QTextCursor
from .QTextDocument import QTextDocument
from .QTextDocumentFragment import QTextDocumentFragment
from .QTextDocumentWriter import QTextDocumentWriter
from .QTextFragment import QTextFragment
from .QTextFrame import QTextFrame
from .QTextFrameFormat import QTextFrameFormat
from .QTextImageFormat import QTextImageFormat
from .QTextInlineObject import QTextInlineObject
from .QTextItem import QTextItem
from .QTextLayout import QTextLayout
from .QTextLength import QTextLength
from .QTextLine import QTextLine
from .QTextList import QTextList
from .QTextListFormat import QTextListFormat
from .QTextObjectInterface import QTextObjectInterface
from .QTextOption import QTextOption
from .QTextTable import QTextTable
from .QTextTableCell import QTextTableCell
from .QTextTableCellFormat import QTextTableCellFormat
from .QTextTableFormat import QTextTableFormat
from .QTouchDevice import QTouchDevice
from .QTouchEvent import QTouchEvent
from .QTransform import QTransform
from .QVector2D import QVector2D
from .QVector3D import QVector3D
from .QVector4D import QVector4D
from .QWhatsThisClickedEvent import QWhatsThisClickedEvent
from .QWheelEvent import QWheelEvent
from .QWindowStateChangeEvent import QWindowStateChangeEvent
# variables with complex values



