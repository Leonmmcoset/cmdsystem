# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


from .QObject import QObject

class QMimeData(QObject):
    """ QMimeData() """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def colorData(self): # real signature unknown; restored from __doc__
        """ colorData(self) -> Any """
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def data(self, mimetype, p_str=None): # real signature unknown; restored from __doc__
        """ data(self, mimetype: Optional[str]) -> QByteArray """
        return QByteArray

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def formats(self): # real signature unknown; restored from __doc__
        """ formats(self) -> List[str] """
        return []

    def hasColor(self): # real signature unknown; restored from __doc__
        """ hasColor(self) -> bool """
        return False

    def hasFormat(self, mimetype, p_str=None): # real signature unknown; restored from __doc__
        """ hasFormat(self, mimetype: Optional[str]) -> bool """
        return False

    def hasHtml(self): # real signature unknown; restored from __doc__
        """ hasHtml(self) -> bool """
        return False

    def hasImage(self): # real signature unknown; restored from __doc__
        """ hasImage(self) -> bool """
        return False

    def hasText(self): # real signature unknown; restored from __doc__
        """ hasText(self) -> bool """
        return False

    def hasUrls(self): # real signature unknown; restored from __doc__
        """ hasUrls(self) -> bool """
        return False

    def html(self): # real signature unknown; restored from __doc__
        """ html(self) -> str """
        return ""

    def imageData(self): # real signature unknown; restored from __doc__
        """ imageData(self) -> Any """
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def removeFormat(self, mimetype, p_str=None): # real signature unknown; restored from __doc__
        """ removeFormat(self, mimetype: Optional[str]) """
        pass

    def retrieveData(self, mimetype, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ retrieveData(self, mimetype: Optional[str], preferredType: QVariant.Type) -> Any """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setColorData(self, color): # real signature unknown; restored from __doc__
        """ setColorData(self, color: Any) """
        pass

    def setData(self, mimetype, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setData(self, mimetype: Optional[str], data: Union[QByteArray, bytes, bytearray]) """
        pass

    def setHtml(self, html, p_str=None): # real signature unknown; restored from __doc__
        """ setHtml(self, html: Optional[str]) """
        pass

    def setImageData(self, image): # real signature unknown; restored from __doc__
        """ setImageData(self, image: Any) """
        pass

    def setText(self, text, p_str=None): # real signature unknown; restored from __doc__
        """ setText(self, text: Optional[str]) """
        pass

    def setUrls(self, urls, QUrl=None): # real signature unknown; restored from __doc__
        """ setUrls(self, urls: Iterable[QUrl]) """
        pass

    def text(self): # real signature unknown; restored from __doc__
        """ text(self) -> str """
        return ""

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def urls(self): # real signature unknown; restored from __doc__
        """ urls(self) -> List[QUrl] """
        return []

    def __init__(self): # real signature unknown; restored from __doc__
        pass


