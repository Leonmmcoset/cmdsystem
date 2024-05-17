# encoding: utf-8
# module PyQt5.QtLocation
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtLocation.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QGeoRouteSegment(__sip.simplewrapper):
    """
    QGeoRouteSegment()
    QGeoRouteSegment(other: QGeoRouteSegment)
    """
    def distance(self): # real signature unknown; restored from __doc__
        """ distance(self) -> float """
        return 0.0

    def isLegLastSegment(self): # real signature unknown; restored from __doc__
        """ isLegLastSegment(self) -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def maneuver(self): # real signature unknown; restored from __doc__
        """ maneuver(self) -> QGeoManeuver """
        return QGeoManeuver

    def nextRouteSegment(self): # real signature unknown; restored from __doc__
        """ nextRouteSegment(self) -> QGeoRouteSegment """
        return QGeoRouteSegment

    def path(self): # real signature unknown; restored from __doc__
        """ path(self) -> List[QGeoCoordinate] """
        return []

    def setDistance(self, distance): # real signature unknown; restored from __doc__
        """ setDistance(self, distance: float) """
        pass

    def setManeuver(self, maneuver): # real signature unknown; restored from __doc__
        """ setManeuver(self, maneuver: QGeoManeuver) """
        pass

    def setNextRouteSegment(self, routeSegment): # real signature unknown; restored from __doc__
        """ setNextRouteSegment(self, routeSegment: QGeoRouteSegment) """
        pass

    def setPath(self, path, QGeoCoordinate=None): # real signature unknown; restored from __doc__
        """ setPath(self, path: Iterable[QGeoCoordinate]) """
        pass

    def setTravelTime(self, secs): # real signature unknown; restored from __doc__
        """ setTravelTime(self, secs: int) """
        pass

    def travelTime(self): # real signature unknown; restored from __doc__
        """ travelTime(self) -> int """
        return 0

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, other=None): # real signature unknown; restored from __doc__ with multiple overloads
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


    __hash__ = None


