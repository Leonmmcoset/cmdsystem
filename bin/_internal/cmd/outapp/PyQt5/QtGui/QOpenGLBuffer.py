# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QOpenGLBuffer(__sip.simplewrapper):
    """
    QOpenGLBuffer()
    QOpenGLBuffer(type: QOpenGLBuffer.Type)
    QOpenGLBuffer(other: QOpenGLBuffer)
    """
    def allocate(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        allocate(self, data: Optional[PyQt5.sip.voidptr], count: int)
        allocate(self, count: int)
        """
        pass

    def bind(self): # real signature unknown; restored from __doc__
        """ bind(self) -> bool """
        return False

    def bufferId(self): # real signature unknown; restored from __doc__
        """ bufferId(self) -> int """
        return 0

    def create(self): # real signature unknown; restored from __doc__
        """ create(self) -> bool """
        return False

    def destroy(self): # real signature unknown; restored from __doc__
        """ destroy(self) """
        pass

    def isCreated(self): # real signature unknown; restored from __doc__
        """ isCreated(self) -> bool """
        return False

    def map(self, access): # real signature unknown; restored from __doc__
        """ map(self, access: QOpenGLBuffer.Access) -> Optional[PyQt5.sip.voidptr] """
        pass

    def mapRange(self, offset, count, access, QOpenGLBuffer_RangeAccessFlags=None, QOpenGLBuffer_RangeAccessFlag=None): # real signature unknown; restored from __doc__
        """ mapRange(self, offset: int, count: int, access: Union[QOpenGLBuffer.RangeAccessFlags, QOpenGLBuffer.RangeAccessFlag]) -> Optional[PyQt5.sip.voidptr] """
        pass

    def read(self, offset, data, PyQt5_sip_voidptr=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ read(self, offset: int, data: Optional[PyQt5.sip.voidptr], count: int) -> bool """
        pass

    def release(self, type=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        release(self)
        release(type: QOpenGLBuffer.Type)
        """
        pass

    def setUsagePattern(self, value): # real signature unknown; restored from __doc__
        """ setUsagePattern(self, value: QOpenGLBuffer.UsagePattern) """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ size(self) -> int """
        return 0

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> QOpenGLBuffer.Type """
        pass

    def unmap(self): # real signature unknown; restored from __doc__
        """ unmap(self) -> bool """
        return False

    def usagePattern(self): # real signature unknown; restored from __doc__
        """ usagePattern(self) -> QOpenGLBuffer.UsagePattern """
        pass

    def write(self, offset, data, PyQt5_sip_voidptr=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ write(self, offset: int, data: Optional[PyQt5.sip.voidptr], count: int) """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    DynamicCopy = 35050
    DynamicDraw = 35048
    DynamicRead = 35049
    IndexBuffer = 34963
    PixelPackBuffer = 35051
    PixelUnpackBuffer = 35052
    RangeFlushExplicit = 16
    RangeInvalidate = 4
    RangeInvalidateBuffer = 8
    RangeRead = 1
    RangeUnsynchronized = 32
    RangeWrite = 2
    ReadOnly = 35000
    ReadWrite = 35002
    StaticCopy = 35046
    StaticDraw = 35044
    StaticRead = 35045
    StreamCopy = 35042
    StreamDraw = 35040
    StreamRead = 35041
    VertexBuffer = 34962
    WriteOnly = 35001


