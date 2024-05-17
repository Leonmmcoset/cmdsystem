# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .TiXmlVisitor import TiXmlVisitor

class TiXmlPrinter(TiXmlVisitor):
    """
    /** Print to memory functionality. The TiXmlPrinter is useful when you need to:
    
        -# Print to memory (especially in non-STL mode)
        -# Control formatting (line endings, etc.)
    
        When constructed, the TiXmlPrinter is in its default "pretty printing" mode.
        Before calling Accept() you can call methods to control the printing
        of the XML document. After TiXmlNode::Accept() is called, the printed document can
        be accessed via the CStr(), Str(), and Size() methods.
    
        TiXmlPrinter uses the Visitor API.
        @verbatim
        TiXmlPrinter printer;
        printer.SetIndent( "\t" );
    
        doc.Accept( &printer );
        fprintf( stdout, "%s", printer.CStr() );
        @endverbatim
    */
    """
    def CStr(self, const_TiXmlPrinter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        CStr(const TiXmlPrinter self)
        
        /// Return the result.
        """
        pass

    def Indent(self, const_TiXmlPrinter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        Indent(const TiXmlPrinter self)
        
        /// Query the indention string.
        """
        pass

    def LineBreak(self, const_TiXmlPrinter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        LineBreak(const TiXmlPrinter self)
        
        /// Query the current line breaking string.
        """
        pass

    def SetIndent(self, const_TiXmlPrinter_self, str__indent): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        SetIndent(const TiXmlPrinter self, str _indent)
        
        /** Set the indent characters for printing. By default 4 spaces
                but tab (\t) is also useful, or null/empty string for no indentation.
            */
        """
        pass

    def SetLineBreak(self, const_TiXmlPrinter_self, str__lineBreak): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        SetLineBreak(const TiXmlPrinter self, str _lineBreak)
        
        /** Set the line breaking string. By default set to newline (\n).
                Some operating systems prefer other characters, or can be
                set to the null/empty string for no indenation.
            */
        """
        pass

    def SetStreamPrinting(self, const_TiXmlPrinter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        SetStreamPrinting(const TiXmlPrinter self)
        
        /** Switch over to "stream printing" which is the most dense formatting without
                linebreaks. Common when the XML is needed for network transmission.
            */
        """
        pass

    def Size(self, const_TiXmlPrinter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        Size(const TiXmlPrinter self)
        
        /// Return the length of the result string.
        """
        pass

    def Str(self, const_TiXmlPrinter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        Str(const TiXmlPrinter self)
        
        /// Return the result.
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
        'CStr': None, # (!) real value is "<method 'CStr' of 'panda3d.core.TiXmlPrinter' objects>"
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        'Indent': None, # (!) real value is "<method 'Indent' of 'panda3d.core.TiXmlPrinter' objects>"
        'LineBreak': None, # (!) real value is "<method 'LineBreak' of 'panda3d.core.TiXmlPrinter' objects>"
        'SetIndent': None, # (!) real value is "<method 'SetIndent' of 'panda3d.core.TiXmlPrinter' objects>"
        'SetLineBreak': None, # (!) real value is "<method 'SetLineBreak' of 'panda3d.core.TiXmlPrinter' objects>"
        'SetStreamPrinting': None, # (!) real value is "<method 'SetStreamPrinting' of 'panda3d.core.TiXmlPrinter' objects>"
        'Size': None, # (!) real value is "<method 'Size' of 'panda3d.core.TiXmlPrinter' objects>"
        'Str': None, # (!) real value is "<method 'Str' of 'panda3d.core.TiXmlPrinter' objects>"
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.TiXmlPrinter' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.TiXmlPrinter' objects>"
        '__doc__': '/** Print to memory functionality. The TiXmlPrinter is useful when you need to:\n\n    -# Print to memory (especially in non-STL mode)\n    -# Control formatting (line endings, etc.)\n\n    When constructed, the TiXmlPrinter is in its default "pretty printing" mode.\n    Before calling Accept() you can call methods to control the printing\n    of the XML document. After TiXmlNode::Accept() is called, the printed document can\n    be accessed via the CStr(), Str(), and Size() methods.\n\n    TiXmlPrinter uses the Visitor API.\n    @verbatim\n    TiXmlPrinter printer;\n    printer.SetIndent( "\\t" );\n\n    doc.Accept( &printer );\n    fprintf( stdout, "%s", printer.CStr() );\n    @endverbatim\n*/',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.TiXmlPrinter' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE391E80>'
    }


