# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QTextDocumentFragment(__sip.simplewrapper):
    """
    QTextDocumentFragment()
    QTextDocumentFragment(document: Optional[QTextDocument])
    QTextDocumentFragment(range: QTextCursor)
    QTextDocumentFragment(rhs: QTextDocumentFragment)
    """
    def fromHtml(self, html, p_str=None, *args=None, **kwargs=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        fromHtml(html: Optional[str]) -> QTextDocumentFragment
        fromHtml(html: Optional[str], resourceProvider: Optional[QTextDocument]) -> QTextDocumentFragment
        """
        return QTextDocumentFragment

    def fromPlainText(self, plainText, p_str=None): # real signature unknown; restored from __doc__
        """ fromPlainText(plainText: Optional[str]) -> QTextDocumentFragment """
        return QTextDocumentFragment

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ isEmpty(self) -> bool """
        return False

    def toHtml(self, encoding, QByteArray=None, bytes=None, bytearray=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ toHtml(self, encoding: Union[QByteArray, bytes, bytearray] = QByteArray()) -> str """
        pass

    def toPlainText(self): # real signature unknown; restored from __doc__
        """ toPlainText(self) -> str """
        return ""

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



