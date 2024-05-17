# encoding: utf-8
# module PyQt5.QtXml
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtXml.pyd
# by generator 1.147
# no doc

# imports
import sip as __sip


class QXmlLexicalHandler(__sip.simplewrapper):
    """
    QXmlLexicalHandler()
    QXmlLexicalHandler(a0: QXmlLexicalHandler)
    """
    def comment(self, ch, p_str=None): # real signature unknown; restored from __doc__
        """ comment(self, ch: Optional[str]) -> bool """
        return False

    def endCDATA(self): # real signature unknown; restored from __doc__
        """ endCDATA(self) -> bool """
        return False

    def endDTD(self): # real signature unknown; restored from __doc__
        """ endDTD(self) -> bool """
        return False

    def endEntity(self, name, p_str=None): # real signature unknown; restored from __doc__
        """ endEntity(self, name: Optional[str]) -> bool """
        return False

    def errorString(self): # real signature unknown; restored from __doc__
        """ errorString(self) -> str """
        return ""

    def startCDATA(self): # real signature unknown; restored from __doc__
        """ startCDATA(self) -> bool """
        return False

    def startDTD(self, name, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ startDTD(self, name: Optional[str], publicId: Optional[str], systemId: Optional[str]) -> bool """
        pass

    def startEntity(self, name, p_str=None): # real signature unknown; restored from __doc__
        """ startEntity(self, name: Optional[str]) -> bool """
        return False

    def __init__(self, a0=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



