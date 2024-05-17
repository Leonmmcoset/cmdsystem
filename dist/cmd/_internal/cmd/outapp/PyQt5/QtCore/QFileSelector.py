# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


from .QObject import QObject

class QFileSelector(QObject):
    """ QFileSelector(parent: Optional[QObject] = None) """
    def allSelectors(self): # real signature unknown; restored from __doc__
        """ allSelectors(self) -> List[str] """
        return []

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def extraSelectors(self): # real signature unknown; restored from __doc__
        """ extraSelectors(self) -> List[str] """
        return []

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def select(self, filePath, p_str=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        select(self, filePath: Optional[str]) -> str
        select(self, filePath: QUrl) -> QUrl
        """
        return "" or QUrl

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setExtraSelectors(self, p_list, Optional=None, p_str=None): # real signature unknown; restored from __doc__
        """ setExtraSelectors(self, list: Iterable[Optional[str]]) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent, QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass


