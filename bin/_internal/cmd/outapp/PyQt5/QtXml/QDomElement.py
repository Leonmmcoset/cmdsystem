# encoding: utf-8
# module PyQt5.QtXml
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtXml.pyd
# by generator 1.147
# no doc

# imports
import sip as __sip


from .QDomNode import QDomNode

class QDomElement(QDomNode):
    """
    QDomElement()
    QDomElement(x: QDomElement)
    """
    def attribute(self, name, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ attribute(self, name: Optional[str], defaultValue: Optional[str] = '') -> str """
        pass

    def attributeNode(self, name, p_str=None): # real signature unknown; restored from __doc__
        """ attributeNode(self, name: Optional[str]) -> QDomAttr """
        return QDomAttr

    def attributeNodeNS(self, nsURI, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ attributeNodeNS(self, nsURI: Optional[str], localName: Optional[str]) -> QDomAttr """
        pass

    def attributeNS(self, nsURI, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ attributeNS(self, nsURI: Optional[str], localName: Optional[str], defaultValue: Optional[str] = '') -> str """
        pass

    def attributes(self): # real signature unknown; restored from __doc__
        """ attributes(self) -> QDomNamedNodeMap """
        return QDomNamedNodeMap

    def elementsByTagName(self, tagname, p_str=None): # real signature unknown; restored from __doc__
        """ elementsByTagName(self, tagname: Optional[str]) -> QDomNodeList """
        return QDomNodeList

    def elementsByTagNameNS(self, nsURI, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ elementsByTagNameNS(self, nsURI: Optional[str], localName: Optional[str]) -> QDomNodeList """
        pass

    def hasAttribute(self, name, p_str=None): # real signature unknown; restored from __doc__
        """ hasAttribute(self, name: Optional[str]) -> bool """
        return False

    def hasAttributeNS(self, nsURI, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ hasAttributeNS(self, nsURI: Optional[str], localName: Optional[str]) -> bool """
        pass

    def nodeType(self): # real signature unknown; restored from __doc__
        """ nodeType(self) -> QDomNode.NodeType """
        pass

    def removeAttribute(self, name, p_str=None): # real signature unknown; restored from __doc__
        """ removeAttribute(self, name: Optional[str]) """
        pass

    def removeAttributeNode(self, oldAttr): # real signature unknown; restored from __doc__
        """ removeAttributeNode(self, oldAttr: QDomAttr) -> QDomAttr """
        return QDomAttr

    def removeAttributeNS(self, nsURI, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ removeAttributeNS(self, nsURI: Optional[str], localName: Optional[str]) """
        pass

    def setAttribute(self, name, p_str=None, *args, **kwargs): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setAttribute(self, name: Optional[str], value: Optional[str])
        setAttribute(self, name: Optional[str], value: int)
        setAttribute(self, name: Optional[str], value: int)
        setAttribute(self, name: Optional[str], value: float)
        setAttribute(self, name: Optional[str], value: int)
        """
        pass

    def setAttributeNode(self, newAttr): # real signature unknown; restored from __doc__
        """ setAttributeNode(self, newAttr: QDomAttr) -> QDomAttr """
        return QDomAttr

    def setAttributeNodeNS(self, newAttr): # real signature unknown; restored from __doc__
        """ setAttributeNodeNS(self, newAttr: QDomAttr) -> QDomAttr """
        return QDomAttr

    def setAttributeNS(self, nsURI, p_str=None, *args, **kwargs): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setAttributeNS(self, nsURI: Optional[str], qName: Optional[str], value: Optional[str])
        setAttributeNS(self, nsURI: Optional[str], qName: Optional[str], value: int)
        setAttributeNS(self, nsURI: Optional[str], qName: Optional[str], value: int)
        setAttributeNS(self, nsURI: Optional[str], qName: Optional[str], value: float)
        setAttributeNS(self, nsURI: Optional[str], qName: Optional[str], value: int)
        """
        pass

    def setTagName(self, name, p_str=None): # real signature unknown; restored from __doc__
        """ setTagName(self, name: Optional[str]) """
        pass

    def tagName(self): # real signature unknown; restored from __doc__
        """ tagName(self) -> str """
        return ""

    def text(self): # real signature unknown; restored from __doc__
        """ text(self) -> str """
        return ""

    def __init__(self, x=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass


