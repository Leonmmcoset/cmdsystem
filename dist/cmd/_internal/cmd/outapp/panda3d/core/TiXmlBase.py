# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class TiXmlBase(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /** TiXmlBase is a base class for every class in TinyXml.
        It does little except to establish that TinyXml classes
        can be printed and provide some utility functions.
    
        In XML, the document and elements can contain
        other elements and other types of nodes.
    
        @verbatim
        A Document can contain: Element (container or leaf)
                                Comment (leaf)
                                Unknown (leaf)
                                Declaration( leaf )
    
        An Element can contain: Element (container or leaf)
                                Text    (leaf)
                                Attributes (not on tree)
                                Comment (leaf)
                                Unknown (leaf)
    
        A Decleration contains: Attributes (not on tree)
        @endverbatim
    */
    """
    def Column(self, TiXmlBase_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        Column(TiXmlBase self)
        
        ///< See Row()
        """
        pass

    def IsWhiteSpaceCondensed(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        IsWhiteSpaceCondensed()
        
        /// Return the current white space setting.
        """
        pass

    def Row(self, TiXmlBase_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        Row(TiXmlBase self)
        
        /** Return the position, in the original source file, of this node or attribute.
                The row and column are 1-based. (That is the first row and first column is
                1,1). If the returns values are 0 or less, then the parser does not have
                a row and column value.
        
                Generally, the row and column value will be set when the TiXmlDocument::Load(),
                TiXmlDocument::LoadFile(), or any TiXmlNode::Parse() is called. It will NOT be set
                when the DOM was created from operator>>.
        
                The values reflect the initial load. Once the DOM is modified programmatically
                (by adding or changing nodes and attributes) the new values will NOT update to
                reflect changes in the document.
        
                There is a minor performance cost to computing the row and column. Computation
                can be disabled if TiXmlDocument::SetTabSize() is called with 0 as the value.
        
                @sa TiXmlDocument::SetTabSize()
            */
        """
        pass

    def SetCondenseWhiteSpace(self, bool_condense): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        SetCondenseWhiteSpace(bool condense)
        
        /** The world does not agree on whether white space should be kept or
                not. In order to make everyone happy, these global, static functions
                are provided to set whether or not TinyXml will condense all white space
                into a single space or not. The default is to condense. Note changing this
                value is not thread safe.
            */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    DtoolClassDict = {
        'Column': None, # (!) real value is "<method 'Column' of 'panda3d.core.TiXmlBase' objects>"
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        'IsWhiteSpaceCondensed': None, # (!) real value is '<staticmethod(<built-in method IsWhiteSpaceCondensed of type object at 0x00007FFCFE3906E0>)>'
        'Row': None, # (!) real value is "<method 'Row' of 'panda3d.core.TiXmlBase' objects>"
        'SetCondenseWhiteSpace': None, # (!) real value is '<staticmethod(<built-in method SetCondenseWhiteSpace of type object at 0x00007FFCFE3906E0>)>'
        'TIXML_ERROR': 1,
        'TIXML_ERROR_DOCUMENT_EMPTY': 12,
        'TIXML_ERROR_DOCUMENT_TOP_ONLY': 15,
        'TIXML_ERROR_EMBEDDED_NULL': 13,
        'TIXML_ERROR_FAILED_TO_READ_ELEMENT_NAME': 4,
        'TIXML_ERROR_OPENING_FILE': 2,
        'TIXML_ERROR_PARSING_CDATA': 14,
        'TIXML_ERROR_PARSING_COMMENT': 10,
        'TIXML_ERROR_PARSING_DECLARATION': 11,
        'TIXML_ERROR_PARSING_ELEMENT': 3,
        'TIXML_ERROR_PARSING_EMPTY': 7,
        'TIXML_ERROR_PARSING_UNKNOWN': 9,
        'TIXML_ERROR_READING_ATTRIBUTES': 6,
        'TIXML_ERROR_READING_ELEMENT_VALUE': 5,
        'TIXML_ERROR_READING_END_TAG': 8,
        'TIXML_ERROR_STRING_COUNT': 16,
        'TIXML_NO_ERROR': 0,
        '__doc__': '/** TiXmlBase is a base class for every class in TinyXml.\n    It does little except to establish that TinyXml classes\n    can be printed and provide some utility functions.\n\n    In XML, the document and elements can contain\n    other elements and other types of nodes.\n\n    @verbatim\n    A Document can contain: Element (container or leaf)\n                            Comment (leaf)\n                            Unknown (leaf)\n                            Declaration( leaf )\n\n    An Element can contain: Element (container or leaf)\n                            Text    (leaf)\n                            Attributes (not on tree)\n                            Comment (leaf)\n                            Unknown (leaf)\n\n    A Decleration contains: Attributes (not on tree)\n    @endverbatim\n*/',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.TiXmlBase' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE3906E0>'
    }
    TIXML_ERROR = 1
    TIXML_ERROR_DOCUMENT_EMPTY = 12
    TIXML_ERROR_DOCUMENT_TOP_ONLY = 15
    TIXML_ERROR_EMBEDDED_NULL = 13
    TIXML_ERROR_FAILED_TO_READ_ELEMENT_NAME = 4
    TIXML_ERROR_OPENING_FILE = 2
    TIXML_ERROR_PARSING_CDATA = 14
    TIXML_ERROR_PARSING_COMMENT = 10
    TIXML_ERROR_PARSING_DECLARATION = 11
    TIXML_ERROR_PARSING_ELEMENT = 3
    TIXML_ERROR_PARSING_EMPTY = 7
    TIXML_ERROR_PARSING_UNKNOWN = 9
    TIXML_ERROR_READING_ATTRIBUTES = 6
    TIXML_ERROR_READING_ELEMENT_VALUE = 5
    TIXML_ERROR_READING_END_TAG = 8
    TIXML_ERROR_STRING_COUNT = 16
    TIXML_NO_ERROR = 0


