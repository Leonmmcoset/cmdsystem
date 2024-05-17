# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


class QXmlStreamWriter(__sip.simplewrapper):
    """
    QXmlStreamWriter()
    QXmlStreamWriter(device: Optional[QIODevice])
    QXmlStreamWriter(array: Optional[Union[QByteArray, bytes, bytearray]])
    """
    def autoFormatting(self): # real signature unknown; restored from __doc__
        """ autoFormatting(self) -> bool """
        return False

    def autoFormattingIndent(self): # real signature unknown; restored from __doc__
        """ autoFormattingIndent(self) -> int """
        return 0

    def codec(self): # real signature unknown; restored from __doc__
        """ codec(self) -> Optional[QTextCodec] """
        pass

    def device(self): # real signature unknown; restored from __doc__
        """ device(self) -> Optional[QIODevice] """
        pass

    def hasError(self): # real signature unknown; restored from __doc__
        """ hasError(self) -> bool """
        return False

    def setAutoFormatting(self, a0): # real signature unknown; restored from __doc__
        """ setAutoFormatting(self, a0: bool) """
        pass

    def setAutoFormattingIndent(self, spaces): # real signature unknown; restored from __doc__
        """ setAutoFormattingIndent(self, spaces: int) """
        pass

    def setCodec(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setCodec(self, codec: Optional[QTextCodec])
        setCodec(self, codecName: Optional[str])
        """
        pass

    def setDevice(self, device, QIODevice=None): # real signature unknown; restored from __doc__
        """ setDevice(self, device: Optional[QIODevice]) """
        pass

    def writeAttribute(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        writeAttribute(self, qualifiedName: Optional[str], value: Optional[str])
        writeAttribute(self, namespaceUri: Optional[str], name: Optional[str], value: Optional[str])
        writeAttribute(self, attribute: QXmlStreamAttribute)
        """
        pass

    def writeAttributes(self, attributes): # real signature unknown; restored from __doc__
        """ writeAttributes(self, attributes: QXmlStreamAttributes) """
        pass

    def writeCDATA(self, text, p_str=None): # real signature unknown; restored from __doc__
        """ writeCDATA(self, text: Optional[str]) """
        pass

    def writeCharacters(self, text, p_str=None): # real signature unknown; restored from __doc__
        """ writeCharacters(self, text: Optional[str]) """
        pass

    def writeComment(self, text, p_str=None): # real signature unknown; restored from __doc__
        """ writeComment(self, text: Optional[str]) """
        pass

    def writeCurrentToken(self, reader): # real signature unknown; restored from __doc__
        """ writeCurrentToken(self, reader: QXmlStreamReader) """
        pass

    def writeDefaultNamespace(self, namespaceUri, p_str=None): # real signature unknown; restored from __doc__
        """ writeDefaultNamespace(self, namespaceUri: Optional[str]) """
        pass

    def writeDTD(self, dtd, p_str=None): # real signature unknown; restored from __doc__
        """ writeDTD(self, dtd: Optional[str]) """
        pass

    def writeEmptyElement(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        writeEmptyElement(self, qualifiedName: Optional[str])
        writeEmptyElement(self, namespaceUri: Optional[str], name: Optional[str])
        """
        pass

    def writeEndDocument(self): # real signature unknown; restored from __doc__
        """ writeEndDocument(self) """
        pass

    def writeEndElement(self): # real signature unknown; restored from __doc__
        """ writeEndElement(self) """
        pass

    def writeEntityReference(self, name, p_str=None): # real signature unknown; restored from __doc__
        """ writeEntityReference(self, name: Optional[str]) """
        pass

    def writeNamespace(self, namespaceUri, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ writeNamespace(self, namespaceUri: Optional[str], prefix: Optional[str] = '') """
        pass

    def writeProcessingInstruction(self, target, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ writeProcessingInstruction(self, target: Optional[str], data: Optional[str] = '') """
        pass

    def writeStartDocument(self, version=None, p_str=None, *args=None, **kwargs=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        writeStartDocument(self)
        writeStartDocument(self, version: Optional[str])
        writeStartDocument(self, version: Optional[str], standalone: bool)
        """
        pass

    def writeStartElement(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        writeStartElement(self, qualifiedName: Optional[str])
        writeStartElement(self, namespaceUri: Optional[str], name: Optional[str])
        """
        pass

    def writeTextElement(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        writeTextElement(self, qualifiedName: Optional[str], text: Optional[str])
        writeTextElement(self, namespaceUri: Optional[str], name: Optional[str], text: Optional[str])
        """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



