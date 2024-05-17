# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


class QCborStreamWriter(__sip.simplewrapper):
    """
    QCborStreamWriter(device: Optional[QIODevice])
    QCborStreamWriter(data: Optional[Union[QByteArray, bytes, bytearray]])
    """
    def append(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        append(self, st: QCborSimpleType)
        append(self, tag: QCborKnownTags)
        append(self, str: Optional[str])
        append(self, ba: Union[QByteArray, bytes, bytearray])
        append(self, b: bool)
        append(self, d: float)
        append(self, a0: int)
        """
        pass

    def appendNull(self): # real signature unknown; restored from __doc__
        """ appendNull(self) """
        pass

    def appendUndefined(self): # real signature unknown; restored from __doc__
        """ appendUndefined(self) """
        pass

    def device(self): # real signature unknown; restored from __doc__
        """ device(self) -> Optional[QIODevice] """
        pass

    def endArray(self): # real signature unknown; restored from __doc__
        """ endArray(self) -> bool """
        return False

    def endMap(self): # real signature unknown; restored from __doc__
        """ endMap(self) -> bool """
        return False

    def setDevice(self, device, QIODevice=None): # real signature unknown; restored from __doc__
        """ setDevice(self, device: Optional[QIODevice]) """
        pass

    def startArray(self, count=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        startArray(self)
        startArray(self, count: int)
        """
        pass

    def startMap(self, count=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        startMap(self)
        startMap(self, count: int)
        """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



