# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .TiXmlBase import TiXmlBase

class TiXmlNode(TiXmlBase):
    """
    /** The parent class for everything in the Document Object Model.
        (Except for attributes).
        Nodes have siblings, a parent, and children. A node can be
        in a document, or stand on its own. The type of a TiXmlNode
        can be queried, and it can be cast to its more defined type.
    */
    """
    def Accept(self, TiXmlNode_self, TiXmlVisitor_visitor): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        Accept(TiXmlNode self, TiXmlVisitor visitor)
        
        /** Accept a hierchical visit the nodes in the TinyXML DOM. Every node in the
                XML tree will be conditionally visited and the host will be called back
                via the TiXmlVisitor interface.
        
                This is essentially a SAX interface for TinyXML. (Note however it doesn't re-parse
                the XML for the callbacks, so the performance of TinyXML is unchanged by using this
                interface versus any other.)
        
                The interface has been based on ideas from:
        
                - http://www.saxproject.org/
                - http://c2.com/cgi/wiki?HierarchicalVisitorPattern
        
                Which are both good references for "visiting".
        
                An example of using Accept():
                @verbatim
                TiXmlPrinter printer;
                tinyxmlDoc.Accept( &printer );
                const char* xmlcstr = printer.CStr();
                @endverbatim
            */
        """
        pass

    def Clear(self, const_TiXmlNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        Clear(const TiXmlNode self)
        
        /// Delete all the children of this node. Does not affect 'this'.
        """
        pass

    def Clone(self, TiXmlNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        Clone(TiXmlNode self)
        
        /** Create an exact duplicate of this node and return it. The memory must be deleted
                by the caller.
            */
        """
        pass

    def FirstChild(self, const_TiXmlNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        FirstChild(const TiXmlNode self)
        FirstChild(TiXmlNode self)
        FirstChild(const TiXmlNode self, str _value)
        FirstChild(const TiXmlNode self, str _value)
        FirstChild(TiXmlNode self, str _value)
        FirstChild(TiXmlNode self, str value)
        
        ///< The first child of this node. Will be null if there are no children.
        
        ///< The first child of this node. Will be null if there are no children.
        
        ///< The first child of this node with the matching 'value'. Will be null if none found.
        /// The first child of this node with the matching 'value'. Will be null if none found.
        
        ///< STL std::string form.
        
        ///< STL std::string form.
        """
        pass

    def FirstChildElement(self, const_TiXmlNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        FirstChildElement(const TiXmlNode self)
        FirstChildElement(TiXmlNode self)
        FirstChildElement(const TiXmlNode self, str _value)
        FirstChildElement(const TiXmlNode self, str _value)
        FirstChildElement(TiXmlNode self, str _value)
        FirstChildElement(TiXmlNode self, str _value)
        
        /// Convenience function to get through elements.
        
        /// Convenience function to get through elements.
        
        ///< STL std::string form.
        
        ///< STL std::string form.
        """
        pass

    def GetDocument(self, const_TiXmlNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        GetDocument(const TiXmlNode self)
        GetDocument(TiXmlNode self)
        
        /** Return a pointer to the Document this node lives in.
                Returns null if not in a document.
            */
        """
        pass

    def InsertAfterChild(self, const_TiXmlNode_self, TiXmlNode_afterThis, const_TiXmlNode_addThis): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        InsertAfterChild(const TiXmlNode self, TiXmlNode afterThis, const TiXmlNode addThis)
        
        /** Add a new node related to this. Adds a child after the specified child.
                Returns a pointer to the new object or NULL if an error occured.
            */
        """
        pass

    def InsertBeforeChild(self, const_TiXmlNode_self, TiXmlNode_beforeThis, const_TiXmlNode_addThis): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        InsertBeforeChild(const TiXmlNode self, TiXmlNode beforeThis, const TiXmlNode addThis)
        
        /** Add a new node related to this. Adds a child before the specified child.
                Returns a pointer to the new object or NULL if an error occured.
            */
        """
        pass

    def InsertEndChild(self, const_TiXmlNode_self, const_TiXmlNode_addThis): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        InsertEndChild(const TiXmlNode self, const TiXmlNode addThis)
        
        /** Add a new node related to this. Adds a child past the LastChild.
                Returns a pointer to the new object or NULL if an error occured.
            */
        """
        pass

    def IterateChildren(self, const_TiXmlNode_self, const_TiXmlNode_previous): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        IterateChildren(const TiXmlNode self, const TiXmlNode previous)
        IterateChildren(TiXmlNode self, const TiXmlNode previous)
        IterateChildren(const TiXmlNode self, str _value, const TiXmlNode previous)
        IterateChildren(const TiXmlNode self, str _value, const TiXmlNode previous)
        IterateChildren(TiXmlNode self, str _value, const TiXmlNode previous)
        IterateChildren(TiXmlNode self, str value, const TiXmlNode previous)
        
        /** An alternate way to walk the children of a node.
                One way to iterate over nodes is:
                @verbatim
                    for( child = parent->FirstChild(); child; child = child->NextSibling() )
                @endverbatim
        
                IterateChildren does the same thing with the syntax:
                @verbatim
                    child = 0;
                    while( child = parent->IterateChildren( child ) )
                @endverbatim
        
                IterateChildren takes the previous child as input and finds
                the next one. If the previous child is null, it returns the
                first. IterateChildren will return null when done.
            */
        
        /// This flavor of IterateChildren searches for children with a particular 'value'
        
        ///< STL std::string form.
        
        ///< STL std::string form.
        """
        pass

    def LastChild(self, const_TiXmlNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        LastChild(const TiXmlNode self)
        LastChild(TiXmlNode self)
        LastChild(const TiXmlNode self, str _value)
        LastChild(const TiXmlNode self, str _value)
        LastChild(TiXmlNode self, str _value)
        LastChild(TiXmlNode self, str value)
        
        /// The last child of this node. Will be null if there are no children.
        
        /// The last child of this node. Will be null if there are no children.
        
        /// The last child of this node matching 'value'. Will be null if there are no children.
        
        /// The last child of this node matching 'value'. Will be null if there are no children.
        
        ///< STL std::string form.
        
        ///< STL std::string form.
        """
        pass

    def NextSibling(self, const_TiXmlNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        NextSibling(const TiXmlNode self)
        NextSibling(TiXmlNode self)
        NextSibling(const TiXmlNode self, str _value)
        NextSibling(const TiXmlNode self, str _next)
        NextSibling(TiXmlNode self, str _value)
        NextSibling(TiXmlNode self, str param0)
        
        ///< STL std::string form.
        
        ///< STL std::string form.
        
        /// Navigate to a sibling node.
        
        /// Navigate to a sibling node with the given 'value'.
        """
        pass

    def NextSiblingElement(self, const_TiXmlNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        NextSiblingElement(const TiXmlNode self)
        NextSiblingElement(TiXmlNode self)
        NextSiblingElement(const TiXmlNode self, str _value)
        NextSiblingElement(const TiXmlNode self, str _next)
        NextSiblingElement(TiXmlNode self, str _value)
        NextSiblingElement(TiXmlNode self, str param0)
        
        /** Convenience function to get through elements.
                Calls NextSibling and ToElement. Will skip all non-Element
                nodes. Returns 0 if there is not another element.
            */
        
        /** Convenience function to get through elements.
                Calls NextSibling and ToElement. Will skip all non-Element
                nodes. Returns 0 if there is not another element.
            */
        
        ///< STL std::string form.
        
        ///< STL std::string form.
        """
        pass

    def NoChildren(self, TiXmlNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        NoChildren(TiXmlNode self)
        
        /// Returns true if this node has no children.
        """
        pass

    def Parent(self, const_TiXmlNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        Parent(const TiXmlNode self)
        Parent(TiXmlNode self)
        
        /// One step up the DOM.
        """
        pass

    def PreviousSibling(self, const_TiXmlNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        PreviousSibling(const TiXmlNode self)
        PreviousSibling(TiXmlNode self)
        PreviousSibling(const TiXmlNode self, str _value)
        PreviousSibling(const TiXmlNode self, str _prev)
        PreviousSibling(TiXmlNode self, str _value)
        PreviousSibling(TiXmlNode self, str param0)
        
        /// Navigate to a sibling node.
        
        /// Navigate to a sibling node.
        
        ///< STL std::string form.
        
        ///< STL std::string form.
        """
        pass

    def RemoveChild(self, const_TiXmlNode_self, TiXmlNode_removeThis): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        RemoveChild(const TiXmlNode self, TiXmlNode removeThis)
        
        /// Delete a child of this node.
        """
        pass

    def ReplaceChild(self, const_TiXmlNode_self, TiXmlNode_replaceThis, const_TiXmlNode_withThis): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        ReplaceChild(const TiXmlNode self, TiXmlNode replaceThis, const TiXmlNode withThis)
        
        /** Replace a child of this node.
                Returns a pointer to the new object or NULL if an error occured.
            */
        """
        pass

    def SetValue(self, const_TiXmlNode_self, str__value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        SetValue(const TiXmlNode self, str _value)
        SetValue(const TiXmlNode self, str _value)
        
        /** Changes the value of the node. Defined as:
                @verbatim
                Document:   filename of the xml file
                Element:    name of the element
                Comment:    the comment text
                Unknown:    the tag contents
                Text:       the text string
                @endverbatim
            */
        
        /// STL std::string form.
        """
        pass

    def ToComment(self, const_TiXmlNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        ToComment(const TiXmlNode self)
        ToComment(TiXmlNode self)
        
        ///< Cast to a more defined type. Will return null if not of the requested type.
        
        ///< Cast to a more defined type. Will return null if not of the requested type.
        """
        pass

    def ToDeclaration(self, const_TiXmlNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        ToDeclaration(const TiXmlNode self)
        ToDeclaration(TiXmlNode self)
        
        ///< Cast to a more defined type. Will return null if not of the requested type.
        
        ///< Cast to a more defined type. Will return null if not of the requested type.
        """
        pass

    def ToDocument(self, const_TiXmlNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        ToDocument(const TiXmlNode self)
        ToDocument(TiXmlNode self)
        
        ///< Cast to a more defined type. Will return null if not of the requested type.
        
        ///< Cast to a more defined type. Will return null if not of the requested type.
        """
        pass

    def ToElement(self, const_TiXmlNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        ToElement(const TiXmlNode self)
        ToElement(TiXmlNode self)
        
        ///< Cast to a more defined type. Will return null if not of the requested type.
        
        ///< Cast to a more defined type. Will return null if not of the requested type.
        """
        pass

    def ToText(self, const_TiXmlNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        ToText(const TiXmlNode self)
        ToText(TiXmlNode self)
        
        ///< Cast to a more defined type. Will return null if not of the requested type.
        
        ///< Cast to a more defined type. Will return null if not of the requested type.
        """
        pass

    def ToUnknown(self, const_TiXmlNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        ToUnknown(const TiXmlNode self)
        ToUnknown(TiXmlNode self)
        
        ///< Cast to a more defined type. Will return null if not of the requested type.
        
        ///< Cast to a more defined type. Will return null if not of the requested type.
        """
        pass

    def Type(self, TiXmlNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        Type(TiXmlNode self)
        
        /** Query the type (as an enumerated value, above) of this node.
                The possible types are: DOCUMENT, ELEMENT, COMMENT,
                                        UNKNOWN, TEXT, and DECLARATION.
            */
        """
        pass

    def Value(self, TiXmlNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        Value(TiXmlNode self)
        
        /** The meaning of 'value' changes for the specific type of
                TiXmlNode.
                @verbatim
                Document:   filename of the xml file
                Element:    name of the element
                Comment:    the comment text
                Unknown:    the tag contents
                Text:       the text string
                @endverbatim
        
                The subclasses will wrap this function.
            */
        """
        pass

    def ValueStr(self, TiXmlNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        ValueStr(TiXmlNode self)
        
        /** Return Value() as a std::string. If you only use STL,
                this is more efficient than calling Value().
                Only available in STL mode.
            */
        """
        pass

    def ValueTStr(self, TiXmlNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        ValueTStr(TiXmlNode self)
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    DtoolClassDict = {
        'Accept': None, # (!) real value is "<method 'Accept' of 'panda3d.core.TiXmlNode' objects>"
        'Clear': None, # (!) real value is "<method 'Clear' of 'panda3d.core.TiXmlNode' objects>"
        'Clone': None, # (!) real value is "<method 'Clone' of 'panda3d.core.TiXmlNode' objects>"
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        'FirstChild': None, # (!) real value is "<method 'FirstChild' of 'panda3d.core.TiXmlNode' objects>"
        'FirstChildElement': None, # (!) real value is "<method 'FirstChildElement' of 'panda3d.core.TiXmlNode' objects>"
        'GetDocument': None, # (!) real value is "<method 'GetDocument' of 'panda3d.core.TiXmlNode' objects>"
        'InsertAfterChild': None, # (!) real value is "<method 'InsertAfterChild' of 'panda3d.core.TiXmlNode' objects>"
        'InsertBeforeChild': None, # (!) real value is "<method 'InsertBeforeChild' of 'panda3d.core.TiXmlNode' objects>"
        'InsertEndChild': None, # (!) real value is "<method 'InsertEndChild' of 'panda3d.core.TiXmlNode' objects>"
        'IterateChildren': None, # (!) real value is "<method 'IterateChildren' of 'panda3d.core.TiXmlNode' objects>"
        'LastChild': None, # (!) real value is "<method 'LastChild' of 'panda3d.core.TiXmlNode' objects>"
        'NextSibling': None, # (!) real value is "<method 'NextSibling' of 'panda3d.core.TiXmlNode' objects>"
        'NextSiblingElement': None, # (!) real value is "<method 'NextSiblingElement' of 'panda3d.core.TiXmlNode' objects>"
        'NoChildren': None, # (!) real value is "<method 'NoChildren' of 'panda3d.core.TiXmlNode' objects>"
        'Parent': None, # (!) real value is "<method 'Parent' of 'panda3d.core.TiXmlNode' objects>"
        'PreviousSibling': None, # (!) real value is "<method 'PreviousSibling' of 'panda3d.core.TiXmlNode' objects>"
        'RemoveChild': None, # (!) real value is "<method 'RemoveChild' of 'panda3d.core.TiXmlNode' objects>"
        'ReplaceChild': None, # (!) real value is "<method 'ReplaceChild' of 'panda3d.core.TiXmlNode' objects>"
        'SetValue': None, # (!) real value is "<method 'SetValue' of 'panda3d.core.TiXmlNode' objects>"
        'TINYXMLCOMMENT': 2,
        'TINYXMLDECLARATION': 5,
        'TINYXMLDOCUMENT': 0,
        'TINYXMLELEMENT': 1,
        'TINYXMLTEXT': 4,
        'TINYXMLTYPECOUNT': 6,
        'TINYXMLUNKNOWN': 3,
        'TINYXML_COMMENT': 2,
        'TINYXML_DECLARATION': 5,
        'TINYXML_DOCUMENT': 0,
        'TINYXML_ELEMENT': 1,
        'TINYXML_TEXT': 4,
        'TINYXML_TYPECOUNT': 6,
        'TINYXML_UNKNOWN': 3,
        'ToComment': None, # (!) real value is "<method 'ToComment' of 'panda3d.core.TiXmlNode' objects>"
        'ToDeclaration': None, # (!) real value is "<method 'ToDeclaration' of 'panda3d.core.TiXmlNode' objects>"
        'ToDocument': None, # (!) real value is "<method 'ToDocument' of 'panda3d.core.TiXmlNode' objects>"
        'ToElement': None, # (!) real value is "<method 'ToElement' of 'panda3d.core.TiXmlNode' objects>"
        'ToText': None, # (!) real value is "<method 'ToText' of 'panda3d.core.TiXmlNode' objects>"
        'ToUnknown': None, # (!) real value is "<method 'ToUnknown' of 'panda3d.core.TiXmlNode' objects>"
        'Type': None, # (!) real value is "<method 'Type' of 'panda3d.core.TiXmlNode' objects>"
        'Value': None, # (!) real value is "<method 'Value' of 'panda3d.core.TiXmlNode' objects>"
        'ValueStr': None, # (!) real value is "<method 'ValueStr' of 'panda3d.core.TiXmlNode' objects>"
        'ValueTStr': None, # (!) real value is "<method 'ValueTStr' of 'panda3d.core.TiXmlNode' objects>"
        '__doc__': '/** The parent class for everything in the Document Object Model.\n    (Except for attributes).\n    Nodes have siblings, a parent, and children. A node can be\n    in a document, or stand on its own. The type of a TiXmlNode\n    can be queried, and it can be cast to its more defined type.\n*/',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.TiXmlNode' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE390A90>'
    }
    TINYXMLCOMMENT = 2
    TINYXMLDECLARATION = 5
    TINYXMLDOCUMENT = 0
    TINYXMLELEMENT = 1
    TINYXMLTEXT = 4
    TINYXMLTYPECOUNT = 6
    TINYXMLUNKNOWN = 3
    TINYXML_COMMENT = 2
    TINYXML_DECLARATION = 5
    TINYXML_DOCUMENT = 0
    TINYXML_ELEMENT = 1
    TINYXML_TEXT = 4
    TINYXML_TYPECOUNT = 6
    TINYXML_UNKNOWN = 3


