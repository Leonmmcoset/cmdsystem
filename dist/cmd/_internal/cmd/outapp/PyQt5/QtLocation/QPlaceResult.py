# encoding: utf-8
# module PyQt5.QtLocation
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtLocation.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


from .QPlaceSearchResult import QPlaceSearchResult

class QPlaceResult(QPlaceSearchResult):
    """
    QPlaceResult()
    QPlaceResult(other: QPlaceSearchResult)
    QPlaceResult(a0: QPlaceResult)
    """
    def distance(self): # real signature unknown; restored from __doc__
        """ distance(self) -> float """
        return 0.0

    def isSponsored(self): # real signature unknown; restored from __doc__
        """ isSponsored(self) -> bool """
        return False

    def place(self): # real signature unknown; restored from __doc__
        """ place(self) -> QPlace """
        return QPlace

    def setDistance(self, distance): # real signature unknown; restored from __doc__
        """ setDistance(self, distance: float) """
        pass

    def setPlace(self, place): # real signature unknown; restored from __doc__
        """ setPlace(self, place: QPlace) """
        pass

    def setSponsored(self, sponsored): # real signature unknown; restored from __doc__
        """ setSponsored(self, sponsored: bool) """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


