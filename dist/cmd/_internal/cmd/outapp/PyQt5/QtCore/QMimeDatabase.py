# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


class QMimeDatabase(__sip.simplewrapper):
    """ QMimeDatabase() """
    def allMimeTypes(self): # real signature unknown; restored from __doc__
        """ allMimeTypes(self) -> List[QMimeType] """
        return []

    def mimeTypeForData(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        mimeTypeForData(self, data: Union[QByteArray, bytes, bytearray]) -> QMimeType
        mimeTypeForData(self, device: Optional[QIODevice]) -> QMimeType
        """
        return QMimeType

    def mimeTypeForFile(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        mimeTypeForFile(self, fileName: Optional[str], mode: QMimeDatabase.MatchMode = QMimeDatabase.MatchDefault) -> QMimeType
        mimeTypeForFile(self, fileInfo: QFileInfo, mode: QMimeDatabase.MatchMode = QMimeDatabase.MatchDefault) -> QMimeType
        """
        return QMimeType

    def mimeTypeForFileNameAndData(self, fileName, p_str=None, *args, **kwargs): # real signature unknown; restored from __doc__ with multiple overloads
        """
        mimeTypeForFileNameAndData(self, fileName: Optional[str], device: Optional[QIODevice]) -> QMimeType
        mimeTypeForFileNameAndData(self, fileName: Optional[str], data: Union[QByteArray, bytes, bytearray]) -> QMimeType
        """
        pass

    def mimeTypeForName(self, nameOrAlias, p_str=None): # real signature unknown; restored from __doc__
        """ mimeTypeForName(self, nameOrAlias: Optional[str]) -> QMimeType """
        return QMimeType

    def mimeTypeForUrl(self, url): # real signature unknown; restored from __doc__
        """ mimeTypeForUrl(self, url: QUrl) -> QMimeType """
        return QMimeType

    def mimeTypesForFileName(self, fileName, p_str=None): # real signature unknown; restored from __doc__
        """ mimeTypesForFileName(self, fileName: Optional[str]) -> List[QMimeType] """
        return []

    def suffixForFileName(self, fileName, p_str=None): # real signature unknown; restored from __doc__
        """ suffixForFileName(self, fileName: Optional[str]) -> str """
        return ""

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    MatchContent = 2
    MatchDefault = 0
    MatchExtension = 1


