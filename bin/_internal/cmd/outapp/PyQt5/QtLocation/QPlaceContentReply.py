# encoding: utf-8
# module PyQt5.QtLocation
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtLocation.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


from .QPlaceReply import QPlaceReply

class QPlaceContentReply(QPlaceReply):
    """ QPlaceContentReply(parent: Optional[QObject] = None) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def content(self): # real signature unknown; restored from __doc__
        """ content(self) -> Dict[int, QPlaceContent] """
        return {}

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def nextPageRequest(self): # real signature unknown; restored from __doc__
        """ nextPageRequest(self) -> QPlaceContentRequest """
        return QPlaceContentRequest

    def previousPageRequest(self): # real signature unknown; restored from __doc__
        """ previousPageRequest(self) -> QPlaceContentRequest """
        return QPlaceContentRequest

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def request(self): # real signature unknown; restored from __doc__
        """ request(self) -> QPlaceContentRequest """
        return QPlaceContentRequest

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setContent(self, content, p_int=None, QPlaceContent=None): # real signature unknown; restored from __doc__
        """ setContent(self, content: Dict[int, QPlaceContent]) """
        pass

    def setError(self, *args, **kwargs): # real signature unknown
        pass

    def setFinished(self, *args, **kwargs): # real signature unknown
        pass

    def setNextPageRequest(self, next): # real signature unknown; restored from __doc__
        """ setNextPageRequest(self, next: QPlaceContentRequest) """
        pass

    def setPreviousPageRequest(self, previous): # real signature unknown; restored from __doc__
        """ setPreviousPageRequest(self, previous: QPlaceContentRequest) """
        pass

    def setRequest(self, request): # real signature unknown; restored from __doc__
        """ setRequest(self, request: QPlaceContentRequest) """
        pass

    def setTotalCount(self, total): # real signature unknown; restored from __doc__
        """ setTotalCount(self, total: int) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def totalCount(self): # real signature unknown; restored from __doc__
        """ totalCount(self) -> int """
        return 0

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> QPlaceReply.Type """
        pass

    def __init__(self, parent, QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass


