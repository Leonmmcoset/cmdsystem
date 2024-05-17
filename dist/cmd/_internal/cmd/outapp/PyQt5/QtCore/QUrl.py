# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


class QUrl(__sip.simplewrapper):
    """
    QUrl()
    QUrl(url: Optional[str], mode: QUrl.ParsingMode = QUrl.TolerantMode)
    QUrl(copy: QUrl)
    """
    def adjusted(self, options, QUrl_FormattingOptions=None, QUrl_UrlFormattingOption=None, QUrl_ComponentFormattingOption=None): # real signature unknown; restored from __doc__
        """ adjusted(self, options: Union[QUrl.FormattingOptions, QUrl.UrlFormattingOption, QUrl.ComponentFormattingOption]) -> QUrl """
        return QUrl

    def authority(self, options, QUrl_ComponentFormattingOptions=None, QUrl_ComponentFormattingOption=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ authority(self, options: Union[QUrl.ComponentFormattingOptions, QUrl.ComponentFormattingOption] = QUrl.PrettyDecoded) -> str """
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def detach(self): # real signature unknown; restored from __doc__
        """ detach(self) """
        pass

    def errorString(self): # real signature unknown; restored from __doc__
        """ errorString(self) -> str """
        return ""

    def fileName(self, options, QUrl_ComponentFormattingOptions=None, QUrl_ComponentFormattingOption=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ fileName(self, options: Union[QUrl.ComponentFormattingOptions, QUrl.ComponentFormattingOption] = QUrl.FullyDecoded) -> str """
        pass

    def fragment(self, options, QUrl_ComponentFormattingOptions=None, QUrl_ComponentFormattingOption=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ fragment(self, options: Union[QUrl.ComponentFormattingOptions, QUrl.ComponentFormattingOption] = QUrl.PrettyDecoded) -> str """
        pass

    def fromAce(self, a0, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ fromAce(a0: Union[QByteArray, bytes, bytearray]) -> str """
        return ""

    def fromEncoded(self, u, QByteArray=None, bytes=None, bytearray=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ fromEncoded(u: Union[QByteArray, bytes, bytearray], mode: QUrl.ParsingMode = QUrl.TolerantMode) -> QUrl """
        pass

    def fromLocalFile(self, localfile, p_str=None): # real signature unknown; restored from __doc__
        """ fromLocalFile(localfile: Optional[str]) -> QUrl """
        return QUrl

    def fromPercentEncoding(self, a0, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ fromPercentEncoding(a0: Union[QByteArray, bytes, bytearray]) -> str """
        return ""

    def fromStringList(self, uris, Optional=None, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ fromStringList(uris: Iterable[Optional[str]], mode: QUrl.ParsingMode = QUrl.TolerantMode) -> List[QUrl] """
        pass

    def fromUserInput(self, userInput, p_str=None, *args=None, **kwargs=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        fromUserInput(userInput: Optional[str]) -> QUrl
        fromUserInput(userInput: Optional[str], workingDirectory: Optional[str], options: Union[QUrl.UserInputResolutionOptions, QUrl.UserInputResolutionOption] = QUrl.DefaultResolution) -> QUrl
        """
        return QUrl

    def hasFragment(self): # real signature unknown; restored from __doc__
        """ hasFragment(self) -> bool """
        return False

    def hasQuery(self): # real signature unknown; restored from __doc__
        """ hasQuery(self) -> bool """
        return False

    def host(self, a0, QUrl_ComponentFormattingOptions=None, QUrl_ComponentFormattingOption=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ host(self, a0: Union[QUrl.ComponentFormattingOptions, QUrl.ComponentFormattingOption] = QUrl.FullyDecoded) -> str """
        pass

    def idnWhitelist(self): # real signature unknown; restored from __doc__
        """ idnWhitelist() -> List[str] """
        return []

    def isDetached(self): # real signature unknown; restored from __doc__
        """ isDetached(self) -> bool """
        return False

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ isEmpty(self) -> bool """
        return False

    def isLocalFile(self): # real signature unknown; restored from __doc__
        """ isLocalFile(self) -> bool """
        return False

    def isParentOf(self, url): # real signature unknown; restored from __doc__
        """ isParentOf(self, url: QUrl) -> bool """
        return False

    def isRelative(self): # real signature unknown; restored from __doc__
        """ isRelative(self) -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def matches(self, url, options, QUrl_FormattingOptions=None, QUrl_UrlFormattingOption=None, QUrl_ComponentFormattingOption=None): # real signature unknown; restored from __doc__
        """ matches(self, url: QUrl, options: Union[QUrl.FormattingOptions, QUrl.UrlFormattingOption, QUrl.ComponentFormattingOption]) -> bool """
        return False

    def password(self, options, QUrl_ComponentFormattingOptions=None, QUrl_ComponentFormattingOption=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ password(self, options: Union[QUrl.ComponentFormattingOptions, QUrl.ComponentFormattingOption] = QUrl.FullyDecoded) -> str """
        pass

    def path(self, options, QUrl_ComponentFormattingOptions=None, QUrl_ComponentFormattingOption=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ path(self, options: Union[QUrl.ComponentFormattingOptions, QUrl.ComponentFormattingOption] = QUrl.FullyDecoded) -> str """
        pass

    def port(self, defaultPort=-1): # real signature unknown; restored from __doc__
        """ port(self, defaultPort: int = -1) -> int """
        return 0

    def query(self, options, QUrl_ComponentFormattingOptions=None, QUrl_ComponentFormattingOption=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ query(self, options: Union[QUrl.ComponentFormattingOptions, QUrl.ComponentFormattingOption] = QUrl.PrettyDecoded) -> str """
        pass

    def resolved(self, relative): # real signature unknown; restored from __doc__
        """ resolved(self, relative: QUrl) -> QUrl """
        return QUrl

    def scheme(self): # real signature unknown; restored from __doc__
        """ scheme(self) -> str """
        return ""

    def setAuthority(self, authority, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setAuthority(self, authority: Optional[str], mode: QUrl.ParsingMode = QUrl.TolerantMode) """
        pass

    def setFragment(self, fragment, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setFragment(self, fragment: Optional[str], mode: QUrl.ParsingMode = QUrl.TolerantMode) """
        pass

    def setHost(self, host, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setHost(self, host: Optional[str], mode: QUrl.ParsingMode = QUrl.DecodedMode) """
        pass

    def setIdnWhitelist(self, a0, Optional=None, p_str=None): # real signature unknown; restored from __doc__
        """ setIdnWhitelist(a0: Iterable[Optional[str]]) """
        pass

    def setPassword(self, password, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setPassword(self, password: Optional[str], mode: QUrl.ParsingMode = QUrl.DecodedMode) """
        pass

    def setPath(self, path, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setPath(self, path: Optional[str], mode: QUrl.ParsingMode = QUrl.DecodedMode) """
        pass

    def setPort(self, port): # real signature unknown; restored from __doc__
        """ setPort(self, port: int) """
        pass

    def setQuery(self, query, p_str=None, *args=None, **kwargs=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setQuery(self, query: Optional[str], mode: QUrl.ParsingMode = QUrl.TolerantMode)
        setQuery(self, query: QUrlQuery)
        """
        pass

    def setScheme(self, scheme, p_str=None): # real signature unknown; restored from __doc__
        """ setScheme(self, scheme: Optional[str]) """
        pass

    def setUrl(self, url, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setUrl(self, url: Optional[str], mode: QUrl.ParsingMode = QUrl.TolerantMode) """
        pass

    def setUserInfo(self, userInfo, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setUserInfo(self, userInfo: Optional[str], mode: QUrl.ParsingMode = QUrl.TolerantMode) """
        pass

    def setUserName(self, userName, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setUserName(self, userName: Optional[str], mode: QUrl.ParsingMode = QUrl.DecodedMode) """
        pass

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: QUrl) """
        pass

    def toAce(self, a0, p_str=None): # real signature unknown; restored from __doc__
        """ toAce(a0: Optional[str]) -> QByteArray """
        return QByteArray

    def toDisplayString(self, options=None): # real signature unknown; restored from __doc__
        """ toDisplayString(self, options: QUrl.FormattingOptions = QUrl.PrettyDecoded) -> str """
        return ""

    def toEncoded(self, options=None): # real signature unknown; restored from __doc__
        """ toEncoded(self, options: QUrl.FormattingOptions = QUrl.FullyEncoded) -> QByteArray """
        return QByteArray

    def toLocalFile(self): # real signature unknown; restored from __doc__
        """ toLocalFile(self) -> str """
        return ""

    def toPercentEncoding(self, input, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ toPercentEncoding(input: Optional[str], exclude: Union[QByteArray, bytes, bytearray] = QByteArray(), include: Union[QByteArray, bytes, bytearray] = QByteArray()) -> QByteArray """
        pass

    def topLevelDomain(self, options, QUrl_ComponentFormattingOptions=None, QUrl_ComponentFormattingOption=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ topLevelDomain(self, options: Union[QUrl.ComponentFormattingOptions, QUrl.ComponentFormattingOption] = QUrl.FullyDecoded) -> str """
        pass

    def toString(self, options=None): # real signature unknown; restored from __doc__
        """ toString(self, options: QUrl.FormattingOptions = QUrl.PrettyDecoded) -> str """
        return ""

    def toStringList(self, uris, QUrl=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ toStringList(uris: Iterable[QUrl], options: QUrl.FormattingOptions = QUrl.PrettyDecoded) -> List[str] """
        pass

    def url(self, options=None): # real signature unknown; restored from __doc__
        """ url(self, options: QUrl.FormattingOptions = QUrl.PrettyDecoded) -> str """
        return ""

    def userInfo(self, options, QUrl_ComponentFormattingOptions=None, QUrl_ComponentFormattingOption=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ userInfo(self, options: Union[QUrl.ComponentFormattingOptions, QUrl.ComponentFormattingOption] = QUrl.PrettyDecoded) -> str """
        pass

    def userName(self, options, QUrl_ComponentFormattingOptions=None, QUrl_ComponentFormattingOption=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ userName(self, options: Union[QUrl.ComponentFormattingOptions, QUrl.ComponentFormattingOption] = QUrl.FullyDecoded) -> str """
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

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
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

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    AssumeLocalFile = 1
    DecodedMode = 2
    DecodeReserved = 33554432
    DefaultResolution = 0
    EncodeDelimiters = 12582912
    EncodeReserved = 16777216
    EncodeSpaces = 1048576
    EncodeUnicode = 2097152
    FullyDecoded = 133169152
    FullyEncoded = 32505856
    None_ = 0
    NormalizePathSegments = 4096
    PreferLocalFile = 512
    PrettyDecoded = 0
    RemoveAuthority = 30
    RemoveFilename = 2048
    RemoveFragment = 128
    RemovePassword = 2
    RemovePath = 32
    RemovePort = 8
    RemoveQuery = 64
    RemoveScheme = 1
    RemoveUserInfo = 6
    StrictMode = 1
    StripTrailingSlash = 1024
    TolerantMode = 0


