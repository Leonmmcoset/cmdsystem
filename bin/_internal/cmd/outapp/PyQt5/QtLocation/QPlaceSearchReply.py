# encoding: utf-8
# module PyQt5.QtLocation
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtLocation.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


from .QPlaceReply import QPlaceReply

class QPlaceSearchReply(QPlaceReply):
    """ QPlaceSearchReply(parent: Optional[QObject] = None) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def nextPageRequest(self): # real signature unknown; restored from __doc__
        """ nextPageRequest(self) -> QPlaceSearchRequest """
        return QPlaceSearchRequest

    def previousPageRequest(self): # real signature unknown; restored from __doc__
        """ previousPageRequest(self) -> QPlaceSearchRequest """
        return QPlaceSearchRequest

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def request(self): # real signature unknown; restored from __doc__
        """ request(self) -> QPlaceSearchRequest """
        return QPlaceSearchRequest

    def results(self): # real signature unknown; restored from __doc__
        """ results(self) -> List[QPlaceSearchResult] """
        return []

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setError(self, *args, **kwargs): # real signature unknown
        pass

    def setFinished(self, *args, **kwargs): # real signature unknown
        pass

    def setNextPageRequest(self, next): # real signature unknown; restored from __doc__
        """ setNextPageRequest(self, next: QPlaceSearchRequest) """
        pass

    def setPreviousPageRequest(self, previous): # real signature unknown; restored from __doc__
        """ setPreviousPageRequest(self, previous: QPlaceSearchRequest) """
        pass

    def setRequest(self, request): # real signature unknown; restored from __doc__
        """ setRequest(self, request: QPlaceSearchRequest) """
        pass

    def setResults(self, results, QPlaceSearchResult=None): # real signature unknown; restored from __doc__
        """ setResults(self, results: Iterable[QPlaceSearchResult]) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> QPlaceReply.Type """
        pass

    def __init__(self, parent, QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass


