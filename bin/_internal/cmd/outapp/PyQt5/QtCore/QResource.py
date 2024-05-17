# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


class QResource(__sip.simplewrapper):
    """ QResource(fileName: Optional[str] = '', locale: QLocale = QLocale()) """
    def absoluteFilePath(self): # real signature unknown; restored from __doc__
        """ absoluteFilePath(self) -> str """
        return ""

    def children(self): # real signature unknown; restored from __doc__
        """ children(self) -> List[str] """
        return []

    def compressionAlgorithm(self): # real signature unknown; restored from __doc__
        """ compressionAlgorithm(self) -> QResource.Compression """
        pass

    def data(self): # real signature unknown; restored from __doc__
        """ data(self) -> bytes """
        return b""

    def fileName(self): # real signature unknown; restored from __doc__
        """ fileName(self) -> str """
        return ""

    def isCompressed(self): # real signature unknown; restored from __doc__
        """ isCompressed(self) -> bool """
        return False

    def isDir(self): # real signature unknown; restored from __doc__
        """ isDir(self) -> bool """
        return False

    def isFile(self): # real signature unknown; restored from __doc__
        """ isFile(self) -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def lastModified(self): # real signature unknown; restored from __doc__
        """ lastModified(self) -> QDateTime """
        return QDateTime

    def locale(self): # real signature unknown; restored from __doc__
        """ locale(self) -> QLocale """
        return QLocale

    def registerResource(self, rccFileName, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ registerResource(rccFileName: Optional[str], mapRoot: Optional[str] = '') -> bool """
        pass

    def registerResourceData(self, rccData, bytes=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ registerResourceData(rccData: Optional[bytes], mapRoot: Optional[str] = '') -> bool """
        pass

    def setFileName(self, file, p_str=None): # real signature unknown; restored from __doc__
        """ setFileName(self, file: Optional[str]) """
        pass

    def setLocale(self, locale): # real signature unknown; restored from __doc__
        """ setLocale(self, locale: QLocale) """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ size(self) -> int """
        return 0

    def uncompressedData(self): # real signature unknown; restored from __doc__
        """ uncompressedData(self) -> QByteArray """
        return QByteArray

    def uncompressedSize(self): # real signature unknown; restored from __doc__
        """ uncompressedSize(self) -> int """
        return 0

    def unregisterResource(self, rccFileName, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ unregisterResource(rccFileName: Optional[str], mapRoot: Optional[str] = '') -> bool """
        pass

    def unregisterResourceData(self, rccData, bytes=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ unregisterResourceData(rccData: Optional[bytes], mapRoot: Optional[str] = '') -> bool """
        pass

    def __init__(self, fileName, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    NoCompression = 0
    ZlibCompression = 1
    ZstdCompression = 2


