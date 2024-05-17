# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class TiXmlHandle(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
        A TiXmlHandle is a class that wraps a node pointer with null checks; this is
        an incredibly useful thing. Note that TiXmlHandle is not part of the TinyXml
        DOM structure. It is a separate utility class.
    
        Take an example:
        @verbatim
        <Document>
            <Element attributeA = "valueA">
                <Child attributeB = "value1" />
                <Child attributeB = "value2" />
            </Element>
        <Document>
        @endverbatim
    
        Assuming you want the value of "attributeB" in the 2nd "Child" element, it's very
        easy to write a *lot* of code that looks like:
    
        @verbatim
        TiXmlElement* root = document.FirstChildElement( "Document" );
        if ( root )
        {
            TiXmlElement* element = root->FirstChildElement( "Element" );
            if ( element )
            {
                TiXmlElement* child = element->FirstChildElement( "Child" );
                if ( child )
                {
                    TiXmlElement* child2 = child->NextSiblingElement( "Child" );
                    if ( child2 )
                    {
                        // Finally do something useful.
        @endverbatim
    
        And that doesn't even cover "else" cases. TiXmlHandle addresses the verbosity
        of such code. A TiXmlHandle checks for null pointers so it is perfectly safe
        and correct to use:
    
        @verbatim
        TiXmlHandle docHandle( &document );
        TiXmlElement* child2 = docHandle.FirstChild( "Document" ).FirstChild( "Element" ).Child( "Child", 1 ).ToElement();
        if ( child2 )
        {
            // do something useful
        @endverbatim
    
        Which is MUCH more concise and useful.
    
        It is also safe to copy handles - internally they are nothing more than node pointers.
        @verbatim
        TiXmlHandle handleCopy = handle;
        @endverbatim
    
        What they should not be used for is iteration:
    
        @verbatim
        int i=0;
        while ( true )
        {
            TiXmlElement* child = docHandle.FirstChild( "Document" ).FirstChild( "Element" ).Child( "Child", i ).ToElement();
            if ( !child )
                break;
            // do something
            ++i;
        }
        @endverbatim
    
        It seems reasonable, but it is in fact two embedded while loops. The Child method is
        a linear walk to find the element, so this code would iterate much more than it needs
        to. Instead, prefer:
    
        @verbatim
        TiXmlElement* child = docHandle.FirstChild( "Document" ).FirstChild( "Element" ).FirstChild( "Child" ).ToElement();
    
        for( child; child; child=child->NextSiblingElement() )
        {
            // do something
        }
        @endverbatim
    */
    """
    def assign(self, const_TiXmlHandle_self, const_TiXmlHandle_ref): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        assign(const TiXmlHandle self, const TiXmlHandle ref)
        """
        pass

    def Child(self, TiXmlHandle_self, int_index): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        Child(TiXmlHandle self, int index)
        Child(TiXmlHandle self, str _value, int index)
        Child(TiXmlHandle self, str value, int index)
        
        /** Return a handle to the "index" child with the given name.
                The first child is 0, the second 1, etc.
            */
        
        /** Return a handle to the "index" child.
                The first child is 0, the second 1, etc.
            */
        """
        pass

    def ChildElement(self, TiXmlHandle_self, int_index): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        ChildElement(TiXmlHandle self, int index)
        ChildElement(TiXmlHandle self, str _value, int index)
        ChildElement(TiXmlHandle self, str value, int index)
        
        /** Return a handle to the "index" child element with the given name.
                The first child element is 0, the second 1, etc. Note that only TiXmlElements
                are indexed: other types are not counted.
            */
        
        /** Return a handle to the "index" child element.
                The first child element is 0, the second 1, etc. Note that only TiXmlElements
                are indexed: other types are not counted.
            */
        """
        pass

    def Element(self, TiXmlHandle_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        Element(TiXmlHandle self)
        
        /** @deprecated use ToElement.
                Return the handle as a TiXmlElement. This may return null.
            */
        """
        pass

    def FirstChild(self, TiXmlHandle_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        FirstChild(TiXmlHandle self)
        FirstChild(TiXmlHandle self, str _value)
        FirstChild(TiXmlHandle self, str value)
        
        /// Return a handle to the first child node.
        
        /// Return a handle to the first child node with the given name.
        """
        pass

    def FirstChildElement(self, TiXmlHandle_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        FirstChildElement(TiXmlHandle self)
        FirstChildElement(TiXmlHandle self, str _value)
        FirstChildElement(TiXmlHandle self, str value)
        
        /// Return a handle to the first child element.
        
        /// Return a handle to the first child element with the given name.
        """
        pass

    def Node(self, TiXmlHandle_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        Node(TiXmlHandle self)
        
        /** @deprecated use ToNode.
                Return the handle as a TiXmlNode. This may return null.
            */
        """
        pass

    def Text(self, TiXmlHandle_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        Text(TiXmlHandle self)
        
        /** @deprecated use ToText()
                Return the handle as a TiXmlText. This may return null.
            */
        """
        pass

    def ToElement(self, TiXmlHandle_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        ToElement(TiXmlHandle self)
        
        /** Return the handle as a TiXmlElement. This may return null.
            */
        """
        pass

    def ToNode(self, TiXmlHandle_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        ToNode(TiXmlHandle self)
        
        /** Return the handle as a TiXmlNode. This may return null.
            */
        """
        pass

    def ToText(self, TiXmlHandle_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        ToText(TiXmlHandle self)
        
        /** Return the handle as a TiXmlText. This may return null.
            */
        """
        pass

    def ToUnknown(self, TiXmlHandle_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        ToUnknown(TiXmlHandle self)
        
        /** Return the handle as a TiXmlUnknown. This may return null.
            */
        """
        pass

    def Unknown(self, TiXmlHandle_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        Unknown(TiXmlHandle self)
        
        /** @deprecated use ToUnknown()
                Return the handle as a TiXmlUnknown. This may return null.
            */
        """
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __deepcopy__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    DtoolClassDict = {
        'Child': None, # (!) real value is "<method 'Child' of 'panda3d.core.TiXmlHandle' objects>"
        'ChildElement': None, # (!) real value is "<method 'ChildElement' of 'panda3d.core.TiXmlHandle' objects>"
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        'Element': None, # (!) real value is "<method 'Element' of 'panda3d.core.TiXmlHandle' objects>"
        'FirstChild': None, # (!) real value is "<method 'FirstChild' of 'panda3d.core.TiXmlHandle' objects>"
        'FirstChildElement': None, # (!) real value is "<method 'FirstChildElement' of 'panda3d.core.TiXmlHandle' objects>"
        'Node': None, # (!) real value is "<method 'Node' of 'panda3d.core.TiXmlHandle' objects>"
        'Text': None, # (!) real value is "<method 'Text' of 'panda3d.core.TiXmlHandle' objects>"
        'ToElement': None, # (!) real value is "<method 'ToElement' of 'panda3d.core.TiXmlHandle' objects>"
        'ToNode': None, # (!) real value is "<method 'ToNode' of 'panda3d.core.TiXmlHandle' objects>"
        'ToText': None, # (!) real value is "<method 'ToText' of 'panda3d.core.TiXmlHandle' objects>"
        'ToUnknown': None, # (!) real value is "<method 'ToUnknown' of 'panda3d.core.TiXmlHandle' objects>"
        'Unknown': None, # (!) real value is "<method 'Unknown' of 'panda3d.core.TiXmlHandle' objects>"
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.TiXmlHandle' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.TiXmlHandle' objects>"
        '__doc__': '/**\n    A TiXmlHandle is a class that wraps a node pointer with null checks; this is\n    an incredibly useful thing. Note that TiXmlHandle is not part of the TinyXml\n    DOM structure. It is a separate utility class.\n\n    Take an example:\n    @verbatim\n    <Document>\n        <Element attributeA = "valueA">\n            <Child attributeB = "value1" />\n            <Child attributeB = "value2" />\n        </Element>\n    <Document>\n    @endverbatim\n\n    Assuming you want the value of "attributeB" in the 2nd "Child" element, it\'s very\n    easy to write a *lot* of code that looks like:\n\n    @verbatim\n    TiXmlElement* root = document.FirstChildElement( "Document" );\n    if ( root )\n    {\n        TiXmlElement* element = root->FirstChildElement( "Element" );\n        if ( element )\n        {\n            TiXmlElement* child = element->FirstChildElement( "Child" );\n            if ( child )\n            {\n                TiXmlElement* child2 = child->NextSiblingElement( "Child" );\n                if ( child2 )\n                {\n                    // Finally do something useful.\n    @endverbatim\n\n    And that doesn\'t even cover "else" cases. TiXmlHandle addresses the verbosity\n    of such code. A TiXmlHandle checks for null pointers so it is perfectly safe\n    and correct to use:\n\n    @verbatim\n    TiXmlHandle docHandle( &document );\n    TiXmlElement* child2 = docHandle.FirstChild( "Document" ).FirstChild( "Element" ).Child( "Child", 1 ).ToElement();\n    if ( child2 )\n    {\n        // do something useful\n    @endverbatim\n\n    Which is MUCH more concise and useful.\n\n    It is also safe to copy handles - internally they are nothing more than node pointers.\n    @verbatim\n    TiXmlHandle handleCopy = handle;\n    @endverbatim\n\n    What they should not be used for is iteration:\n\n    @verbatim\n    int i=0;\n    while ( true )\n    {\n        TiXmlElement* child = docHandle.FirstChild( "Document" ).FirstChild( "Element" ).Child( "Child", i ).ToElement();\n        if ( !child )\n            break;\n        // do something\n        ++i;\n    }\n    @endverbatim\n\n    It seems reasonable, but it is in fact two embedded while loops. The Child method is\n    a linear walk to find the element, so this code would iterate much more than it needs\n    to. Instead, prefer:\n\n    @verbatim\n    TiXmlElement* child = docHandle.FirstChild( "Document" ).FirstChild( "Element" ).FirstChild( "Child" ).ToElement();\n\n    for( child; child; child=child->NextSiblingElement() )\n    {\n        // do something\n    }\n    @endverbatim\n*/',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.TiXmlHandle' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE391CB0>'
        'assign': None, # (!) real value is "<method 'assign' of 'panda3d.core.TiXmlHandle' objects>"
    }


