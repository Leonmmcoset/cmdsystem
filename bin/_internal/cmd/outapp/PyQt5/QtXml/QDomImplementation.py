# encoding: utf-8
# module PyQt5.QtXml
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtXml.pyd
# by generator 1.147
# no doc

# imports
import sip as __sip


class QDomImplementation(__sip.simplewrapper):
    """
    QDomImplementation()
    QDomImplementation(a0: QDomImplementation)
    """
    def createDocument(self, nsURI, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ createDocument(self, nsURI: Optional[str], qName: Optional[str], doctype: QDomDocumentType) -> QDomDocument """
        pass

    def createDocumentType(self, qName, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ createDocumentType(self, qName: Optional[str], publicId: Optional[str], systemId: Optional[str]) -> QDomDocumentType """
        pass

    def hasFeature(self, feature, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ hasFeature(self, feature: Optional[str], version: Optional[str]) -> bool """
        pass

    def invalidDataPolicy(self): # real signature unknown; restored from __doc__
        """ invalidDataPolicy() -> QDomImplementation.InvalidDataPolicy """
        pass

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def setInvalidDataPolicy(self, policy): # real signature unknown; restored from __doc__
        """ setInvalidDataPolicy(policy: QDomImplementation.InvalidDataPolicy) """
        pass

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


    AcceptInvalidChars = 0
    DropInvalidChars = 1
    ReturnNullNode = 2
    __hash__ = None


