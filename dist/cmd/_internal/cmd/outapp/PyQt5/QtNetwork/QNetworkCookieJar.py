# encoding: utf-8
# module PyQt5.QtNetwork
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtNetwork.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QNetworkCookieJar(__PyQt5_QtCore.QObject):
    """ QNetworkCookieJar(parent: Optional[QObject] = None) """
    def allCookies(self): # real signature unknown; restored from __doc__
        """ allCookies(self) -> List[QNetworkCookie] """
        return []

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def cookiesForUrl(self, url): # real signature unknown; restored from __doc__
        """ cookiesForUrl(self, url: QUrl) -> List[QNetworkCookie] """
        return []

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def deleteCookie(self, cookie): # real signature unknown; restored from __doc__
        """ deleteCookie(self, cookie: QNetworkCookie) -> bool """
        return False

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def insertCookie(self, cookie): # real signature unknown; restored from __doc__
        """ insertCookie(self, cookie: QNetworkCookie) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setAllCookies(self, cookieList, QNetworkCookie=None): # real signature unknown; restored from __doc__
        """ setAllCookies(self, cookieList: Iterable[QNetworkCookie]) """
        pass

    def setCookiesFromUrl(self, cookieList, QNetworkCookie=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setCookiesFromUrl(self, cookieList: Iterable[QNetworkCookie], url: QUrl) -> bool """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def updateCookie(self, cookie): # real signature unknown; restored from __doc__
        """ updateCookie(self, cookie: QNetworkCookie) -> bool """
        return False

    def validateCookie(self, cookie, url): # real signature unknown; restored from __doc__
        """ validateCookie(self, cookie: QNetworkCookie, url: QUrl) -> bool """
        return False

    def __init__(self, parent, QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass


