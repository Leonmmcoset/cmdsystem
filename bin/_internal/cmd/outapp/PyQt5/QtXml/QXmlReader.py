# encoding: utf-8
# module PyQt5.QtXml
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtXml.pyd
# by generator 1.147
# no doc

# imports
import sip as __sip


class QXmlReader(__sip.simplewrapper):
    """
    QXmlReader()
    QXmlReader(a0: QXmlReader)
    """
    def contentHandler(self): # real signature unknown; restored from __doc__
        """ contentHandler(self) -> Optional[QXmlContentHandler] """
        pass

    def declHandler(self): # real signature unknown; restored from __doc__
        """ declHandler(self) -> Optional[QXmlDeclHandler] """
        pass

    def DTDHandler(self): # real signature unknown; restored from __doc__
        """ DTDHandler(self) -> Optional[QXmlDTDHandler] """
        pass

    def entityResolver(self): # real signature unknown; restored from __doc__
        """ entityResolver(self) -> Optional[QXmlEntityResolver] """
        pass

    def errorHandler(self): # real signature unknown; restored from __doc__
        """ errorHandler(self) -> Optional[QXmlErrorHandler] """
        pass

    def feature(self, name, p_str=None): # real signature unknown; restored from __doc__
        """ feature(self, name: Optional[str]) -> (bool, Optional[bool]) """
        pass

    def hasFeature(self, name, p_str=None): # real signature unknown; restored from __doc__
        """ hasFeature(self, name: Optional[str]) -> bool """
        return False

    def hasProperty(self, name, p_str=None): # real signature unknown; restored from __doc__
        """ hasProperty(self, name: Optional[str]) -> bool """
        return False

    def lexicalHandler(self): # real signature unknown; restored from __doc__
        """ lexicalHandler(self) -> Optional[QXmlLexicalHandler] """
        pass

    def parse(self, input, QXmlInputSource=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        parse(self, input: QXmlInputSource) -> bool
        parse(self, input: Optional[QXmlInputSource]) -> bool
        """
        return False

    def property(self, name, p_str=None): # real signature unknown; restored from __doc__
        """ property(self, name: Optional[str]) -> (Optional[PyQt5.sip.voidptr], Optional[bool]) """
        pass

    def setContentHandler(self, handler, QXmlContentHandler=None): # real signature unknown; restored from __doc__
        """ setContentHandler(self, handler: Optional[QXmlContentHandler]) """
        pass

    def setDeclHandler(self, handler, QXmlDeclHandler=None): # real signature unknown; restored from __doc__
        """ setDeclHandler(self, handler: Optional[QXmlDeclHandler]) """
        pass

    def setDTDHandler(self, handler, QXmlDTDHandler=None): # real signature unknown; restored from __doc__
        """ setDTDHandler(self, handler: Optional[QXmlDTDHandler]) """
        pass

    def setEntityResolver(self, handler, QXmlEntityResolver=None): # real signature unknown; restored from __doc__
        """ setEntityResolver(self, handler: Optional[QXmlEntityResolver]) """
        pass

    def setErrorHandler(self, handler, QXmlErrorHandler=None): # real signature unknown; restored from __doc__
        """ setErrorHandler(self, handler: Optional[QXmlErrorHandler]) """
        pass

    def setFeature(self, name, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setFeature(self, name: Optional[str], value: bool) """
        pass

    def setLexicalHandler(self, handler, QXmlLexicalHandler=None): # real signature unknown; restored from __doc__
        """ setLexicalHandler(self, handler: Optional[QXmlLexicalHandler]) """
        pass

    def setProperty(self, name, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setProperty(self, name: Optional[str], value: Optional[PyQt5.sip.voidptr]) """
        pass

    def __init__(self, a0=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



