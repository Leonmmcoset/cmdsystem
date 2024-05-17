# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .TiXmlNode import TiXmlNode

class TiXmlDocument(TiXmlNode):
    """
    /** Always the top level node. A document binds together all the
        XML pieces. It can be saved, loaded, and printed to the screen.
        The 'value' of a document node is the xml file name.
    */
    """
    def assign(self, const_TiXmlDocument_self, const_TiXmlDocument_copy): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        assign(const TiXmlDocument self, const TiXmlDocument copy)
        """
        pass

    def ClearError(self, const_TiXmlDocument_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        ClearError(const TiXmlDocument self)
        
        /** If you have handled the error, it can be reset with this call. The error
                state is automatically cleared if you Parse a new XML block.
            */
        """
        pass

    def Error(self, TiXmlDocument_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        Error(TiXmlDocument self)
        
        /** If an error occurs, Error will be set to true. Also,
                - The ErrorId() will contain the integer identifier of the error (not generally useful)
                - The ErrorDesc() method will return the name of the error. (very useful)
                - The ErrorRow() and ErrorCol() will return the location of the error (if known)
            */
        """
        pass

    def ErrorCol(self, TiXmlDocument_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        ErrorCol(TiXmlDocument self)
        
        ///< The column where the error occured. See ErrorRow()
        """
        pass

    def ErrorDesc(self, TiXmlDocument_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        ErrorDesc(TiXmlDocument self)
        
        /// Contains a textual (english) description of the error if one occurs.
        """
        pass

    def ErrorId(self, TiXmlDocument_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        ErrorId(TiXmlDocument self)
        
        /** Generally, you probably want the error string ( ErrorDesc() ). But if you
                prefer the ErrorId, this function will fetch it.
            */
        """
        pass

    def ErrorRow(self, TiXmlDocument_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        ErrorRow(TiXmlDocument self)
        
        /** Returns the location (if known) of the error. The first column is column 1,
                and the first row is row 1. A value of 0 means the row and column wasn't applicable
                (memory errors, for example, have no row/column) or the parser lost the error. (An
                error in the error reporting, in that case.)
        
                @sa SetTabSize, Row, Column
            */
        """
        pass

    def LoadFile(self, const_TiXmlDocument_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        LoadFile(const TiXmlDocument self)
        LoadFile(const TiXmlDocument self, str filename, int encoding)
        LoadFile(const TiXmlDocument self, str filename, int encoding)
        LoadFile(const TiXmlDocument self, int encoding)
        
        /** Load a file using the current document value.
                Returns true if successful. Will delete any existing
                document data before loading.
            */
        
        /// Load a file using the given filename. Returns true if successful.
        
        /** Load a file using the given FILE*. Returns true if successful. Note that this method
                doesn't stream - the entire object pointed at by the FILE*
                will be interpreted as an XML file. TinyXML doesn't stream in XML from the current
                file location. Streaming may be added in the future.
            */
        
        ///< STL std::string version.
        """
        pass

    def Print(self, TiXmlDocument_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        Print(TiXmlDocument self)
        
        /** Write the document to standard out using formatted printing ("pretty print"). */
        """
        pass

    def RootElement(self, const_TiXmlDocument_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        RootElement(const TiXmlDocument self)
        RootElement(TiXmlDocument self)
        
        /** Get the root element -- the only top level element -- of the document.
                In well formed XML, there should only be one. TinyXml is tolerant of
                multiple elements at the document level.
            */
        """
        pass

    def SaveFile(self, TiXmlDocument_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        SaveFile(TiXmlDocument self)
        SaveFile(TiXmlDocument self, str filename)
        SaveFile(TiXmlDocument self, str filename)
        
        /// Save a file using the current document value. Returns true if successful.
        
        /// Save a file using the given filename. Returns true if successful.
        
        /// Save a file using the given FILE*. Returns true if successful.
        
        ///< STL std::string version.
        """
        pass

    def SetTabSize(self, const_TiXmlDocument_self, int__tabsize): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        SetTabSize(const TiXmlDocument self, int _tabsize)
        
        /** SetTabSize() allows the error reporting functions (ErrorRow() and ErrorCol())
                to report the correct values for row and column. It does not change the output
                or input in any way.
        
                By calling this method, with a tab size
                greater than 0, the row and column of each node and attribute is stored
                when the file is loaded. Very useful for tracking the DOM back in to
                the source file.
        
                The tab size is required for calculating the location of nodes. If not
                set, the default of 4 is used. The tabsize is set per document. Setting
                the tabsize to 0 disables row/column tracking.
        
                Note that row and column tracking is not supported when using operator>>.
        
                The tab size needs to be enabled before the parse or load. Correct usage:
                @verbatim
                TiXmlDocument doc;
                doc.SetTabSize( 8 );
                doc.Load( "myfile.xml" );
                @endverbatim
        
                @sa Row, Column
            */
        """
        pass

    def TabSize(self, TiXmlDocument_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        TabSize(TiXmlDocument self)
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
        'ClearError': None, # (!) real value is "<method 'ClearError' of 'panda3d.core.TiXmlDocument' objects>"
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        'Error': None, # (!) real value is "<method 'Error' of 'panda3d.core.TiXmlDocument' objects>"
        'ErrorCol': None, # (!) real value is "<method 'ErrorCol' of 'panda3d.core.TiXmlDocument' objects>"
        'ErrorDesc': None, # (!) real value is "<method 'ErrorDesc' of 'panda3d.core.TiXmlDocument' objects>"
        'ErrorId': None, # (!) real value is "<method 'ErrorId' of 'panda3d.core.TiXmlDocument' objects>"
        'ErrorRow': None, # (!) real value is "<method 'ErrorRow' of 'panda3d.core.TiXmlDocument' objects>"
        'LoadFile': None, # (!) real value is "<method 'LoadFile' of 'panda3d.core.TiXmlDocument' objects>"
        'Print': None, # (!) real value is "<method 'Print' of 'panda3d.core.TiXmlDocument' objects>"
        'RootElement': None, # (!) real value is "<method 'RootElement' of 'panda3d.core.TiXmlDocument' objects>"
        'SaveFile': None, # (!) real value is "<method 'SaveFile' of 'panda3d.core.TiXmlDocument' objects>"
        'SetTabSize': None, # (!) real value is "<method 'SetTabSize' of 'panda3d.core.TiXmlDocument' objects>"
        'TabSize': None, # (!) real value is "<method 'TabSize' of 'panda3d.core.TiXmlDocument' objects>"
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.TiXmlDocument' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.TiXmlDocument' objects>"
        '__doc__': "/** Always the top level node. A document binds together all the\n    XML pieces. It can be saved, loaded, and printed to the screen.\n    The 'value' of a document node is the xml file name.\n*/",
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.TiXmlDocument' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE390C60>'
        'assign': None, # (!) real value is "<method 'assign' of 'panda3d.core.TiXmlDocument' objects>"
    }


