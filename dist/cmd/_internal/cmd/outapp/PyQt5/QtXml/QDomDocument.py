# encoding: utf-8
# module PyQt5.QtXml
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtXml.pyd
# by generator 1.147
# no doc

# imports
import sip as __sip


from .QDomNode import QDomNode

class QDomDocument(QDomNode):
    """
    QDomDocument()
    QDomDocument(name: Optional[str])
    QDomDocument(doctype: QDomDocumentType)
    QDomDocument(x: QDomDocument)
    """
    def createAttribute(self, name, p_str=None): # real signature unknown; restored from __doc__
        """ createAttribute(self, name: Optional[str]) -> QDomAttr """
        return QDomAttr

    def createAttributeNS(self, nsURI, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ createAttributeNS(self, nsURI: Optional[str], qName: Optional[str]) -> QDomAttr """
        pass

    def createCDATASection(self, data, p_str=None): # real signature unknown; restored from __doc__
        """ createCDATASection(self, data: Optional[str]) -> QDomCDATASection """
        return QDomCDATASection

    def createComment(self, data, p_str=None): # real signature unknown; restored from __doc__
        """ createComment(self, data: Optional[str]) -> QDomComment """
        return QDomComment

    def createDocumentFragment(self): # real signature unknown; restored from __doc__
        """ createDocumentFragment(self) -> QDomDocumentFragment """
        return QDomDocumentFragment

    def createElement(self, tagName, p_str=None): # real signature unknown; restored from __doc__
        """ createElement(self, tagName: Optional[str]) -> QDomElement """
        return QDomElement

    def createElementNS(self, nsURI, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ createElementNS(self, nsURI: Optional[str], qName: Optional[str]) -> QDomElement """
        pass

    def createEntityReference(self, name, p_str=None): # real signature unknown; restored from __doc__
        """ createEntityReference(self, name: Optional[str]) -> QDomEntityReference """
        return QDomEntityReference

    def createProcessingInstruction(self, target, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ createProcessingInstruction(self, target: Optional[str], data: Optional[str]) -> QDomProcessingInstruction """
        pass

    def createTextNode(self, data, p_str=None): # real signature unknown; restored from __doc__
        """ createTextNode(self, data: Optional[str]) -> QDomText """
        return QDomText

    def doctype(self): # real signature unknown; restored from __doc__
        """ doctype(self) -> QDomDocumentType """
        return QDomDocumentType

    def documentElement(self): # real signature unknown; restored from __doc__
        """ documentElement(self) -> QDomElement """
        return QDomElement

    def elementById(self, elementId, p_str=None): # real signature unknown; restored from __doc__
        """ elementById(self, elementId: Optional[str]) -> QDomElement """
        return QDomElement

    def elementsByTagName(self, tagname, p_str=None): # real signature unknown; restored from __doc__
        """ elementsByTagName(self, tagname: Optional[str]) -> QDomNodeList """
        return QDomNodeList

    def elementsByTagNameNS(self, nsURI, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ elementsByTagNameNS(self, nsURI: Optional[str], localName: Optional[str]) -> QDomNodeList """
        pass

    def implementation(self): # real signature unknown; restored from __doc__
        """ implementation(self) -> QDomImplementation """
        return QDomImplementation

    def importNode(self, importedNode, deep): # real signature unknown; restored from __doc__
        """ importNode(self, importedNode: QDomNode, deep: bool) -> QDomNode """
        return QDomNode

    def nodeType(self): # real signature unknown; restored from __doc__
        """ nodeType(self) -> QDomNode.NodeType """
        pass

    def setContent(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setContent(self, text: Union[QByteArray, bytes, bytearray], namespaceProcessing: bool) -> (bool, Optional[str], Optional[int], Optional[int])
        setContent(self, text: Optional[str], namespaceProcessing: bool) -> (bool, Optional[str], Optional[int], Optional[int])
        setContent(self, dev: Optional[QIODevice], namespaceProcessing: bool) -> (bool, Optional[str], Optional[int], Optional[int])
        setContent(self, source: Optional[QXmlInputSource], namespaceProcessing: bool) -> (bool, Optional[str], Optional[int], Optional[int])
        setContent(self, text: Union[QByteArray, bytes, bytearray]) -> (bool, Optional[str], Optional[int], Optional[int])
        setContent(self, text: Optional[str]) -> (bool, Optional[str], Optional[int], Optional[int])
        setContent(self, dev: Optional[QIODevice]) -> (bool, Optional[str], Optional[int], Optional[int])
        setContent(self, source: Optional[QXmlInputSource], reader: Optional[QXmlReader]) -> (bool, Optional[str], Optional[int], Optional[int])
        setContent(self, reader: Optional[QXmlStreamReader], namespaceProcessing: bool) -> (bool, Optional[str], Optional[int], Optional[int])
        """
        pass

    def toByteArray(self, indent=1): # real signature unknown; restored from __doc__
        """ toByteArray(self, indent: int = 1) -> QByteArray """
        pass

    def toString(self, indent=1): # real signature unknown; restored from __doc__
        """ toString(self, indent: int = 1) -> str """
        return ""

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


