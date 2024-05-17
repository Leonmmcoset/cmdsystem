# encoding: utf-8
# module PyQt5.QtXml
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtXml.pyd
# by generator 1.147
# no doc

# imports
import sip as __sip


class QXmlErrorHandler(__sip.simplewrapper):
    """
    QXmlErrorHandler()
    QXmlErrorHandler(a0: QXmlErrorHandler)
    """
    def error(self, exception): # real signature unknown; restored from __doc__
        """ error(self, exception: QXmlParseException) -> bool """
        return False

    def errorString(self): # real signature unknown; restored from __doc__
        """ errorString(self) -> str """
        return ""

    def fatalError(self, exception): # real signature unknown; restored from __doc__
        """ fatalError(self, exception: QXmlParseException) -> bool """
        return False

    def warning(self, exception): # real signature unknown; restored from __doc__
        """ warning(self, exception: QXmlParseException) -> bool """
        return False

    def __init__(self, a0=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



