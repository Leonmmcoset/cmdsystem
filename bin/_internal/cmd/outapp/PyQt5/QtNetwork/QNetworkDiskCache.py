# encoding: utf-8
# module PyQt5.QtNetwork
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtNetwork.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


from .QAbstractNetworkCache import QAbstractNetworkCache

class QNetworkDiskCache(QAbstractNetworkCache):
    """ QNetworkDiskCache(parent: Optional[QObject] = None) """
    def cacheDirectory(self): # real signature unknown; restored from __doc__
        """ cacheDirectory(self) -> str """
        return ""

    def cacheSize(self): # real signature unknown; restored from __doc__
        """ cacheSize(self) -> int """
        return 0

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def data(self, url): # real signature unknown; restored from __doc__
        """ data(self, url: QUrl) -> Optional[QIODevice] """
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def expire(self): # real signature unknown; restored from __doc__
        """ expire(self) -> int """
        return 0

    def fileMetaData(self, fileName, p_str=None): # real signature unknown; restored from __doc__
        """ fileMetaData(self, fileName: Optional[str]) -> QNetworkCacheMetaData """
        return QNetworkCacheMetaData

    def insert(self, device, QIODevice=None): # real signature unknown; restored from __doc__
        """ insert(self, device: Optional[QIODevice]) """
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def maximumCacheSize(self): # real signature unknown; restored from __doc__
        """ maximumCacheSize(self) -> int """
        return 0

    def metaData(self, url): # real signature unknown; restored from __doc__
        """ metaData(self, url: QUrl) -> QNetworkCacheMetaData """
        return QNetworkCacheMetaData

    def prepare(self, metaData): # real signature unknown; restored from __doc__
        """ prepare(self, metaData: QNetworkCacheMetaData) -> Optional[QIODevice] """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def remove(self, url): # real signature unknown; restored from __doc__
        """ remove(self, url: QUrl) -> bool """
        return False

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setCacheDirectory(self, cacheDir, p_str=None): # real signature unknown; restored from __doc__
        """ setCacheDirectory(self, cacheDir: Optional[str]) """
        pass

    def setMaximumCacheSize(self, size): # real signature unknown; restored from __doc__
        """ setMaximumCacheSize(self, size: int) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def updateMetaData(self, metaData): # real signature unknown; restored from __doc__
        """ updateMetaData(self, metaData: QNetworkCacheMetaData) """
        pass

    def __init__(self, parent, QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass


