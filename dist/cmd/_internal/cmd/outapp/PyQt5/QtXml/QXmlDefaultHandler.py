# encoding: utf-8
# module PyQt5.QtXml
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtXml.pyd
# by generator 1.147
# no doc

# imports
import sip as __sip


from .QXmlContentHandler import QXmlContentHandler

from .QXmlErrorHandler import QXmlErrorHandler

from .QXmlDTDHandler import QXmlDTDHandler

from .QXmlEntityResolver import QXmlEntityResolver

from .QXmlLexicalHandler import QXmlLexicalHandler

from .QXmlDeclHandler import QXmlDeclHandler

class QXmlDefaultHandler(QXmlContentHandler, QXmlErrorHandler, QXmlDTDHandler, QXmlEntityResolver, QXmlLexicalHandler, QXmlDeclHandler):
    """ QXmlDefaultHandler() """
    def attributeDecl(self, eName, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ attributeDecl(self, eName: Optional[str], aName: Optional[str], type: Optional[str], valueDefault: Optional[str], value: Optional[str]) -> bool """
        pass

    def characters(self, ch, p_str=None): # real signature unknown; restored from __doc__
        """ characters(self, ch: Optional[str]) -> bool """
        return False

    def comment(self, ch, p_str=None): # real signature unknown; restored from __doc__
        """ comment(self, ch: Optional[str]) -> bool """
        return False

    def endCDATA(self): # real signature unknown; restored from __doc__
        """ endCDATA(self) -> bool """
        return False

    def endDocument(self): # real signature unknown; restored from __doc__
        """ endDocument(self) -> bool """
        return False

    def endDTD(self): # real signature unknown; restored from __doc__
        """ endDTD(self) -> bool """
        return False

    def endElement(self, namespaceURI, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ endElement(self, namespaceURI: Optional[str], localName: Optional[str], qName: Optional[str]) -> bool """
        pass

    def endEntity(self, name, p_str=None): # real signature unknown; restored from __doc__
        """ endEntity(self, name: Optional[str]) -> bool """
        return False

    def endPrefixMapping(self, prefix, p_str=None): # real signature unknown; restored from __doc__
        """ endPrefixMapping(self, prefix: Optional[str]) -> bool """
        return False

    def error(self, exception): # real signature unknown; restored from __doc__
        """ error(self, exception: QXmlParseException) -> bool """
        return False

    def errorString(self): # real signature unknown; restored from __doc__
        """ errorString(self) -> str """
        return ""

    def externalEntityDecl(self, name, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ externalEntityDecl(self, name: Optional[str], publicId: Optional[str], systemId: Optional[str]) -> bool """
        pass

    def fatalError(self, exception): # real signature unknown; restored from __doc__
        """ fatalError(self, exception: QXmlParseException) -> bool """
        return False

    def ignorableWhitespace(self, ch, p_str=None): # real signature unknown; restored from __doc__
        """ ignorableWhitespace(self, ch: Optional[str]) -> bool """
        return False

    def internalEntityDecl(self, name, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ internalEntityDecl(self, name: Optional[str], value: Optional[str]) -> bool """
        pass

    def notationDecl(self, name, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ notationDecl(self, name: Optional[str], publicId: Optional[str], systemId: Optional[str]) -> bool """
        pass

    def processingInstruction(self, target, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ processingInstruction(self, target: Optional[str], data: Optional[str]) -> bool """
        pass

    def resolveEntity(self, publicId, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ resolveEntity(self, publicId: Optional[str], systemId: Optional[str]) -> (bool, Optional[QXmlInputSource]) """
        pass

    def setDocumentLocator(self, locator, QXmlLocator=None): # real signature unknown; restored from __doc__
        """ setDocumentLocator(self, locator: Optional[QXmlLocator]) """
        pass

    def skippedEntity(self, name, p_str=None): # real signature unknown; restored from __doc__
        """ skippedEntity(self, name: Optional[str]) -> bool """
        return False

    def startCDATA(self): # real signature unknown; restored from __doc__
        """ startCDATA(self) -> bool """
        return False

    def startDocument(self): # real signature unknown; restored from __doc__
        """ startDocument(self) -> bool """
        return False

    def startDTD(self, name, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ startDTD(self, name: Optional[str], publicId: Optional[str], systemId: Optional[str]) -> bool """
        pass

    def startElement(self, namespaceURI, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ startElement(self, namespaceURI: Optional[str], localName: Optional[str], qName: Optional[str], atts: QXmlAttributes) -> bool """
        pass

    def startEntity(self, name, p_str=None): # real signature unknown; restored from __doc__
        """ startEntity(self, name: Optional[str]) -> bool """
        return False

    def startPrefixMapping(self, prefix, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ startPrefixMapping(self, prefix: Optional[str], uri: Optional[str]) -> bool """
        pass

    def unparsedEntityDecl(self, name, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ unparsedEntityDecl(self, name: Optional[str], publicId: Optional[str], systemId: Optional[str], notationName: Optional[str]) -> bool """
        pass

    def warning(self, exception): # real signature unknown; restored from __doc__
        """ warning(self, exception: QXmlParseException) -> bool """
        return False

    def __init__(self): # real signature unknown; restored from __doc__
        pass


