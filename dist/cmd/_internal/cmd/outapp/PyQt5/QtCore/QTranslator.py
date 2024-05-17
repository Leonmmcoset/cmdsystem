# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


from .QObject import QObject

class QTranslator(QObject):
    """ QTranslator(parent: Optional[QObject] = None) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def filePath(self): # real signature unknown; restored from __doc__
        """ filePath(self) -> str """
        return ""

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ isEmpty(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def language(self): # real signature unknown; restored from __doc__
        """ language(self) -> str """
        return ""

    def load(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        load(self, fileName: Optional[str], directory: Optional[str] = '', searchDelimiters: Optional[str] = '', suffix: Optional[str] = '') -> bool
        load(self, locale: QLocale, fileName: Optional[str], prefix: Optional[str] = '', directory: Optional[str] = '', suffix: Optional[str] = '') -> bool
        """
        pass

    def loadFromData(self, data, PyQt5_sip_array=None, bytes=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ loadFromData(self, data: Optional[PyQt5.sip.array[bytes]], directory: Optional[str] = '') -> bool """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def translate(self, context, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ translate(self, context: Optional[str], sourceText: Optional[str], disambiguation: Optional[str] = None, n: int = -1) -> str """
        pass

    def __init__(self, parent, QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass


