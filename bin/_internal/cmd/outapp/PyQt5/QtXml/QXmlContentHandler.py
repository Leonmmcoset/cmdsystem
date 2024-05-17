# encoding: utf-8
# module PyQt5.QtXml
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtXml.pyd
# by generator 1.147
# no doc

# imports
import sip as __sip


class QXmlContentHandler(__sip.simplewrapper):
    """
    QXmlContentHandler()
    QXmlContentHandler(a0: QXmlContentHandler)
    """
    def characters(self, ch, p_str=None): # real signature unknown; restored from __doc__
        """ characters(self, ch: Optional[str]) -> bool """
        return False

    def endDocument(self): # real signature unknown; restored from __doc__
        """ endDocument(self) -> bool """
        return False

    def endElement(self, namespaceURI, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ endElement(self, namespaceURI: Optional[str], localName: Optional[str], qName: Optional[str]) -> bool """
        pass

    def endPrefixMapping(self, prefix, p_str=None): # real signature unknown; restored from __doc__
        """ endPrefixMapping(self, prefix: Optional[str]) -> bool """
        return False

    def errorString(self): # real signature unknown; restored from __doc__
        """ errorString(self) -> str """
        return ""

    def ignorableWhitespace(self, ch, p_str=None): # real signature unknown; restored from __doc__
        """ ignorableWhitespace(self, ch: Optional[str]) -> bool """
        return False

    def processingInstruction(self, target, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ processingInstruction(self, target: Optional[str], data: Optional[str]) -> bool """
        pass

    def setDocumentLocator(self, locator, QXmlLocator=None): # real signature unknown; restored from __doc__
        """ setDocumentLocator(self, locator: Optional[QXmlLocator]) """
        pass

    def skippedEntity(self, name, p_str=None): # real signature unknown; restored from __doc__
        """ skippedEntity(self, name: Optional[str]) -> bool """
        return False

    def startDocument(self): # real signature unknown; restored from __doc__
        """ startDocument(self) -> bool """
        return False

    def startElement(self, namespaceURI, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ startElement(self, namespaceURI: Optional[str], localName: Optional[str], qName: Optional[str], atts: QXmlAttributes) -> bool """
        pass

    def startPrefixMapping(self, prefix, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ startPrefixMapping(self, prefix: Optional[str], uri: Optional[str]) -> bool """
        pass

    def __init__(self, a0=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



