# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QTextDocumentWriter(__sip.simplewrapper):
    """
    QTextDocumentWriter()
    QTextDocumentWriter(device: Optional[QIODevice], format: Union[QByteArray, bytes, bytearray])
    QTextDocumentWriter(fileName: Optional[str], format: Union[QByteArray, bytes, bytearray] = QByteArray())
    """
    def codec(self): # real signature unknown; restored from __doc__
        """ codec(self) -> Optional[QTextCodec] """
        pass

    def device(self): # real signature unknown; restored from __doc__
        """ device(self) -> Optional[QIODevice] """
        pass

    def fileName(self): # real signature unknown; restored from __doc__
        """ fileName(self) -> str """
        return ""

    def format(self): # real signature unknown; restored from __doc__
        """ format(self) -> QByteArray """
        pass

    def setCodec(self, codec, QTextCodec=None): # real signature unknown; restored from __doc__
        """ setCodec(self, codec: Optional[QTextCodec]) """
        pass

    def setDevice(self, device, QIODevice=None): # real signature unknown; restored from __doc__
        """ setDevice(self, device: Optional[QIODevice]) """
        pass

    def setFileName(self, fileName, p_str=None): # real signature unknown; restored from __doc__
        """ setFileName(self, fileName: Optional[str]) """
        pass

    def setFormat(self, format, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ setFormat(self, format: Union[QByteArray, bytes, bytearray]) """
        pass

    def supportedDocumentFormats(self): # real signature unknown; restored from __doc__
        """ supportedDocumentFormats() -> List[QByteArray] """
        return []

    def write(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        write(self, document: Optional[QTextDocument]) -> bool
        write(self, fragment: QTextDocumentFragment) -> bool
        """
        return False

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



