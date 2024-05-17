# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


class QUrlQuery(__sip.simplewrapper):
    """
    QUrlQuery()
    QUrlQuery(url: QUrl)
    QUrlQuery(queryString: Optional[str])
    QUrlQuery(other: QUrlQuery)
    """
    def addQueryItem(self, key, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ addQueryItem(self, key: Optional[str], value: Optional[str]) """
        pass

    def allQueryItemValues(self, key, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ allQueryItemValues(self, key: Optional[str], options: Union[QUrl.ComponentFormattingOptions, QUrl.ComponentFormattingOption] = QUrl.PrettyDecoded) -> List[str] """
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def defaultQueryPairDelimiter(self): # real signature unknown; restored from __doc__
        """ defaultQueryPairDelimiter() -> str """
        return ""

    def defaultQueryValueDelimiter(self): # real signature unknown; restored from __doc__
        """ defaultQueryValueDelimiter() -> str """
        return ""

    def hasQueryItem(self, key, p_str=None): # real signature unknown; restored from __doc__
        """ hasQueryItem(self, key: Optional[str]) -> bool """
        return False

    def isDetached(self): # real signature unknown; restored from __doc__
        """ isDetached(self) -> bool """
        return False

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ isEmpty(self) -> bool """
        return False

    def query(self, options, QUrl_ComponentFormattingOptions=None, QUrl_ComponentFormattingOption=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ query(self, options: Union[QUrl.ComponentFormattingOptions, QUrl.ComponentFormattingOption] = QUrl.PrettyDecoded) -> str """
        pass

    def queryItems(self, options, QUrl_ComponentFormattingOptions=None, QUrl_ComponentFormattingOption=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ queryItems(self, options: Union[QUrl.ComponentFormattingOptions, QUrl.ComponentFormattingOption] = QUrl.PrettyDecoded) -> List[Tuple[str, str]] """
        pass

    def queryItemValue(self, key, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ queryItemValue(self, key: Optional[str], options: Union[QUrl.ComponentFormattingOptions, QUrl.ComponentFormattingOption] = QUrl.PrettyDecoded) -> str """
        pass

    def queryPairDelimiter(self): # real signature unknown; restored from __doc__
        """ queryPairDelimiter(self) -> str """
        return ""

    def queryValueDelimiter(self): # real signature unknown; restored from __doc__
        """ queryValueDelimiter(self) -> str """
        return ""

    def removeAllQueryItems(self, key, p_str=None): # real signature unknown; restored from __doc__
        """ removeAllQueryItems(self, key: Optional[str]) """
        pass

    def removeQueryItem(self, key, p_str=None): # real signature unknown; restored from __doc__
        """ removeQueryItem(self, key: Optional[str]) """
        pass

    def setQuery(self, queryString, p_str=None): # real signature unknown; restored from __doc__
        """ setQuery(self, queryString: Optional[str]) """
        pass

    def setQueryDelimiters(self, valueDelimiter, pairDelimiter): # real signature unknown; restored from __doc__
        """ setQueryDelimiters(self, valueDelimiter: str, pairDelimiter: str) """
        pass

    def setQueryItems(self, query, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setQueryItems(self, query: Iterable[Tuple[Optional[str], Optional[str]]]) """
        pass

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: QUrlQuery) """
        pass

    def toString(self, options, QUrl_ComponentFormattingOptions=None, QUrl_ComponentFormattingOption=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ toString(self, options: Union[QUrl.ComponentFormattingOptions, QUrl.ComponentFormattingOption] = QUrl.PrettyDecoded) -> str """
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

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



