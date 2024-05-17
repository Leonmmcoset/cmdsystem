# encoding: utf-8
# module PyQt5.QtXml
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtXml.pyd
# by generator 1.147
# no doc

# imports
import sip as __sip


class QDomNode(__sip.simplewrapper):
    """
    QDomNode()
    QDomNode(a0: QDomNode)
    """
    def appendChild(self, newChild): # real signature unknown; restored from __doc__
        """ appendChild(self, newChild: QDomNode) -> QDomNode """
        return QDomNode

    def attributes(self): # real signature unknown; restored from __doc__
        """ attributes(self) -> QDomNamedNodeMap """
        return QDomNamedNodeMap

    def childNodes(self): # real signature unknown; restored from __doc__
        """ childNodes(self) -> QDomNodeList """
        return QDomNodeList

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def cloneNode(self, deep=True): # real signature unknown; restored from __doc__
        """ cloneNode(self, deep: bool = True) -> QDomNode """
        return QDomNode

    def columnNumber(self): # real signature unknown; restored from __doc__
        """ columnNumber(self) -> int """
        return 0

    def firstChild(self): # real signature unknown; restored from __doc__
        """ firstChild(self) -> QDomNode """
        return QDomNode

    def firstChildElement(self, tagName, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ firstChildElement(self, tagName: Optional[str] = '') -> QDomElement """
        pass

    def hasAttributes(self): # real signature unknown; restored from __doc__
        """ hasAttributes(self) -> bool """
        return False

    def hasChildNodes(self): # real signature unknown; restored from __doc__
        """ hasChildNodes(self) -> bool """
        return False

    def insertAfter(self, newChild, refChild): # real signature unknown; restored from __doc__
        """ insertAfter(self, newChild: QDomNode, refChild: QDomNode) -> QDomNode """
        return QDomNode

    def insertBefore(self, newChild, refChild): # real signature unknown; restored from __doc__
        """ insertBefore(self, newChild: QDomNode, refChild: QDomNode) -> QDomNode """
        return QDomNode

    def isAttr(self): # real signature unknown; restored from __doc__
        """ isAttr(self) -> bool """
        return False

    def isCDATASection(self): # real signature unknown; restored from __doc__
        """ isCDATASection(self) -> bool """
        return False

    def isCharacterData(self): # real signature unknown; restored from __doc__
        """ isCharacterData(self) -> bool """
        return False

    def isComment(self): # real signature unknown; restored from __doc__
        """ isComment(self) -> bool """
        return False

    def isDocument(self): # real signature unknown; restored from __doc__
        """ isDocument(self) -> bool """
        return False

    def isDocumentFragment(self): # real signature unknown; restored from __doc__
        """ isDocumentFragment(self) -> bool """
        return False

    def isDocumentType(self): # real signature unknown; restored from __doc__
        """ isDocumentType(self) -> bool """
        return False

    def isElement(self): # real signature unknown; restored from __doc__
        """ isElement(self) -> bool """
        return False

    def isEntity(self): # real signature unknown; restored from __doc__
        """ isEntity(self) -> bool """
        return False

    def isEntityReference(self): # real signature unknown; restored from __doc__
        """ isEntityReference(self) -> bool """
        return False

    def isNotation(self): # real signature unknown; restored from __doc__
        """ isNotation(self) -> bool """
        return False

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def isProcessingInstruction(self): # real signature unknown; restored from __doc__
        """ isProcessingInstruction(self) -> bool """
        return False

    def isSupported(self, feature, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ isSupported(self, feature: Optional[str], version: Optional[str]) -> bool """
        pass

    def isText(self): # real signature unknown; restored from __doc__
        """ isText(self) -> bool """
        return False

    def lastChild(self): # real signature unknown; restored from __doc__
        """ lastChild(self) -> QDomNode """
        return QDomNode

    def lastChildElement(self, tagName, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ lastChildElement(self, tagName: Optional[str] = '') -> QDomElement """
        pass

    def lineNumber(self): # real signature unknown; restored from __doc__
        """ lineNumber(self) -> int """
        return 0

    def localName(self): # real signature unknown; restored from __doc__
        """ localName(self) -> str """
        return ""

    def namedItem(self, name, p_str=None): # real signature unknown; restored from __doc__
        """ namedItem(self, name: Optional[str]) -> QDomNode """
        return QDomNode

    def namespaceURI(self): # real signature unknown; restored from __doc__
        """ namespaceURI(self) -> str """
        return ""

    def nextSibling(self): # real signature unknown; restored from __doc__
        """ nextSibling(self) -> QDomNode """
        return QDomNode

    def nextSiblingElement(self, taName, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ nextSiblingElement(self, taName: Optional[str] = '') -> QDomElement """
        pass

    def nodeName(self): # real signature unknown; restored from __doc__
        """ nodeName(self) -> str """
        return ""

    def nodeType(self): # real signature unknown; restored from __doc__
        """ nodeType(self) -> QDomNode.NodeType """
        pass

    def nodeValue(self): # real signature unknown; restored from __doc__
        """ nodeValue(self) -> str """
        return ""

    def normalize(self): # real signature unknown; restored from __doc__
        """ normalize(self) """
        pass

    def ownerDocument(self): # real signature unknown; restored from __doc__
        """ ownerDocument(self) -> QDomDocument """
        return QDomDocument

    def parentNode(self): # real signature unknown; restored from __doc__
        """ parentNode(self) -> QDomNode """
        return QDomNode

    def prefix(self): # real signature unknown; restored from __doc__
        """ prefix(self) -> str """
        return ""

    def previousSibling(self): # real signature unknown; restored from __doc__
        """ previousSibling(self) -> QDomNode """
        return QDomNode

    def previousSiblingElement(self, tagName, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ previousSiblingElement(self, tagName: Optional[str] = '') -> QDomElement """
        pass

    def removeChild(self, oldChild): # real signature unknown; restored from __doc__
        """ removeChild(self, oldChild: QDomNode) -> QDomNode """
        return QDomNode

    def replaceChild(self, newChild, oldChild): # real signature unknown; restored from __doc__
        """ replaceChild(self, newChild: QDomNode, oldChild: QDomNode) -> QDomNode """
        return QDomNode

    def save(self, a0, a1, a2=None): # real signature unknown; restored from __doc__
        """ save(self, a0: QTextStream, a1: int, a2: QDomNode.EncodingPolicy = QDomNode.EncodingFromDocument) """
        pass

    def setNodeValue(self, a0, p_str=None): # real signature unknown; restored from __doc__
        """ setNodeValue(self, a0: Optional[str]) """
        pass

    def setPrefix(self, pre, p_str=None): # real signature unknown; restored from __doc__
        """ setPrefix(self, pre: Optional[str]) """
        pass

    def toAttr(self): # real signature unknown; restored from __doc__
        """ toAttr(self) -> QDomAttr """
        return QDomAttr

    def toCDATASection(self): # real signature unknown; restored from __doc__
        """ toCDATASection(self) -> QDomCDATASection """
        return QDomCDATASection

    def toCharacterData(self): # real signature unknown; restored from __doc__
        """ toCharacterData(self) -> QDomCharacterData """
        return QDomCharacterData

    def toComment(self): # real signature unknown; restored from __doc__
        """ toComment(self) -> QDomComment """
        return QDomComment

    def toDocument(self): # real signature unknown; restored from __doc__
        """ toDocument(self) -> QDomDocument """
        return QDomDocument

    def toDocumentFragment(self): # real signature unknown; restored from __doc__
        """ toDocumentFragment(self) -> QDomDocumentFragment """
        return QDomDocumentFragment

    def toDocumentType(self): # real signature unknown; restored from __doc__
        """ toDocumentType(self) -> QDomDocumentType """
        return QDomDocumentType

    def toElement(self): # real signature unknown; restored from __doc__
        """ toElement(self) -> QDomElement """
        return QDomElement

    def toEntity(self): # real signature unknown; restored from __doc__
        """ toEntity(self) -> QDomEntity """
        return QDomEntity

    def toEntityReference(self): # real signature unknown; restored from __doc__
        """ toEntityReference(self) -> QDomEntityReference """
        return QDomEntityReference

    def toNotation(self): # real signature unknown; restored from __doc__
        """ toNotation(self) -> QDomNotation """
        return QDomNotation

    def toProcessingInstruction(self): # real signature unknown; restored from __doc__
        """ toProcessingInstruction(self) -> QDomProcessingInstruction """
        return QDomProcessingInstruction

    def toText(self): # real signature unknown; restored from __doc__
        """ toText(self) -> QDomText """
        return QDomText

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, a0=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    AttributeNode = 2
    BaseNode = 21
    CDATASectionNode = 4
    CharacterDataNode = 22
    CommentNode = 8
    DocumentFragmentNode = 11
    DocumentNode = 9
    DocumentTypeNode = 10
    ElementNode = 1
    EncodingFromDocument = 1
    EncodingFromTextStream = 2
    EntityNode = 6
    EntityReferenceNode = 5
    NotationNode = 12
    ProcessingInstructionNode = 7
    TextNode = 3
    __hash__ = None


