# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class TiXmlVisitor(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
        Implements the interface to the "Visitor pattern" (see the Accept() method.)
        If you call the Accept() method, it requires being passed a TiXmlVisitor
        class to handle callbacks. For nodes that contain other nodes (Document, Element)
        you will get called with a VisitEnter/VisitExit pair. Nodes that are always leaves
        are simply called with Visit().
    
        If you return 'true' from a Visit method, recursive parsing will continue. If you return
        false, <b>no children of this node or its sibilings</b> will be Visited.
    
        All flavors of Visit methods have a default implementation that returns 'true' (continue
        visiting). You need to only override methods that are interesting to you.
    
        Generally Accept() is called on the TiXmlDocument, although all nodes suppert Visiting.
    
        You should never change the document from a callback.
    
        @sa TiXmlNode::Accept()
    */
    """
    def Visit(self, const_TiXmlVisitor_self, const_TiXmlDeclaration_param0): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        Visit(const TiXmlVisitor self, const TiXmlDeclaration param0)
        Visit(const TiXmlVisitor self, const TiXmlUnknown param0)
        Visit(const TiXmlVisitor self, const TiXmlText param0)
        Visit(const TiXmlVisitor self, const TiXmlComment param0)
        
        /*declaration*/
        
        /*text*/
        
        /*comment*/
        
        /*unknown*/
        """
        pass

    def VisitEnter(self, const_TiXmlVisitor_self, const_TiXmlDocument_param0): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        VisitEnter(const TiXmlVisitor self, const TiXmlDocument param0)
        VisitEnter(const TiXmlVisitor self, const TiXmlElement param0, const TiXmlAttribute param1)
        
        /*doc*/
        
        /*firstAttribute*/
        """
        pass

    def VisitExit(self, const_TiXmlVisitor_self, const_TiXmlElement_param0): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        VisitExit(const TiXmlVisitor self, const TiXmlElement param0)
        
        /*doc*/
        
        /*element*/
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
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        'Visit': None, # (!) real value is "<method 'Visit' of 'panda3d.core.TiXmlVisitor' objects>"
        'VisitEnter': None, # (!) real value is "<method 'VisitEnter' of 'panda3d.core.TiXmlVisitor' objects>"
        'VisitExit': None, # (!) real value is "<method 'VisitExit' of 'panda3d.core.TiXmlVisitor' objects>"
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.TiXmlVisitor' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.TiXmlVisitor' objects>"
        '__doc__': '/**\n    Implements the interface to the "Visitor pattern" (see the Accept() method.)\n    If you call the Accept() method, it requires being passed a TiXmlVisitor\n    class to handle callbacks. For nodes that contain other nodes (Document, Element)\n    you will get called with a VisitEnter/VisitExit pair. Nodes that are always leaves\n    are simply called with Visit().\n\n    If you return \'true\' from a Visit method, recursive parsing will continue. If you return\n    false, <b>no children of this node or its sibilings</b> will be Visited.\n\n    All flavors of Visit methods have a default implementation that returns \'true\' (continue\n    visiting). You need to only override methods that are interesting to you.\n\n    Generally Accept() is called on the TiXmlDocument, although all nodes suppert Visiting.\n\n    You should never change the document from a callback.\n\n    @sa TiXmlNode::Accept()\n*/',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.TiXmlVisitor' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE3911D0>'
    }


