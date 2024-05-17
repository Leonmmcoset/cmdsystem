# encoding: utf-8
# module PyQt5.QtNetwork
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtNetwork.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QHstsPolicy(__sip.simplewrapper):
    """
    QHstsPolicy()
    QHstsPolicy(expiry: Union[QDateTime, datetime.datetime], flags: Union[QHstsPolicy.PolicyFlags, QHstsPolicy.PolicyFlag], host: Optional[str], mode: QUrl.ParsingMode = QUrl.DecodedMode)
    QHstsPolicy(rhs: QHstsPolicy)
    """
    def expiry(self): # real signature unknown; restored from __doc__
        """ expiry(self) -> QDateTime """
        pass

    def host(self, options, QUrl_ComponentFormattingOptions=None, QUrl_ComponentFormattingOption=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ host(self, options: Union[QUrl.ComponentFormattingOptions, QUrl.ComponentFormattingOption] = QUrl.ComponentFormattingOption.FullyDecoded) -> str """
        pass

    def includesSubDomains(self): # real signature unknown; restored from __doc__
        """ includesSubDomains(self) -> bool """
        return False

    def isExpired(self): # real signature unknown; restored from __doc__
        """ isExpired(self) -> bool """
        return False

    def setExpiry(self, expiry, QDateTime=None, datetime_datetime=None): # real signature unknown; restored from __doc__
        """ setExpiry(self, expiry: Union[QDateTime, datetime.datetime]) """
        pass

    def setHost(self, host, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setHost(self, host: Optional[str], mode: QUrl.ParsingMode = QUrl.DecodedMode) """
        pass

    def setIncludesSubDomains(self, include): # real signature unknown; restored from __doc__
        """ setIncludesSubDomains(self, include: bool) """
        pass

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: QHstsPolicy) """
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


    IncludeSubDomains = 1
    __hash__ = None


