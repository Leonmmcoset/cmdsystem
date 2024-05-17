# encoding: utf-8
# module PyQt5.QtLocation
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtLocation.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QGeoRoute(__sip.simplewrapper):
    """
    QGeoRoute()
    QGeoRoute(other: QGeoRoute)
    """
    def bounds(self): # real signature unknown; restored from __doc__
        """ bounds(self) -> QGeoRectangle """
        pass

    def distance(self): # real signature unknown; restored from __doc__
        """ distance(self) -> float """
        return 0.0

    def extendedAttributes(self): # real signature unknown; restored from __doc__
        """ extendedAttributes(self) -> Dict[str, Any] """
        return {}

    def firstRouteSegment(self): # real signature unknown; restored from __doc__
        """ firstRouteSegment(self) -> QGeoRouteSegment """
        return QGeoRouteSegment

    def path(self): # real signature unknown; restored from __doc__
        """ path(self) -> List[QGeoCoordinate] """
        return []

    def request(self): # real signature unknown; restored from __doc__
        """ request(self) -> QGeoRouteRequest """
        return QGeoRouteRequest

    def routeId(self): # real signature unknown; restored from __doc__
        """ routeId(self) -> str """
        return ""

    def routeLegs(self): # real signature unknown; restored from __doc__
        """ routeLegs(self) -> List[QGeoRouteLeg] """
        return []

    def setBounds(self, bounds): # real signature unknown; restored from __doc__
        """ setBounds(self, bounds: QGeoRectangle) """
        pass

    def setDistance(self, distance): # real signature unknown; restored from __doc__
        """ setDistance(self, distance: float) """
        pass

    def setExtendedAttributes(self, extendedAttributes, p_str=None, Any=None): # real signature unknown; restored from __doc__
        """ setExtendedAttributes(self, extendedAttributes: Dict[str, Any]) """
        pass

    def setFirstRouteSegment(self, routeSegment): # real signature unknown; restored from __doc__
        """ setFirstRouteSegment(self, routeSegment: QGeoRouteSegment) """
        pass

    def setPath(self, path, QGeoCoordinate=None): # real signature unknown; restored from __doc__
        """ setPath(self, path: Iterable[QGeoCoordinate]) """
        pass

    def setRequest(self, request): # real signature unknown; restored from __doc__
        """ setRequest(self, request: QGeoRouteRequest) """
        pass

    def setRouteId(self, id, p_str=None): # real signature unknown; restored from __doc__
        """ setRouteId(self, id: Optional[str]) """
        pass

    def setRouteLegs(self, legs, QGeoRouteLeg=None): # real signature unknown; restored from __doc__
        """ setRouteLegs(self, legs: Iterable[QGeoRouteLeg]) """
        pass

    def setTravelMode(self, mode): # real signature unknown; restored from __doc__
        """ setTravelMode(self, mode: QGeoRouteRequest.TravelMode) """
        pass

    def setTravelTime(self, secs): # real signature unknown; restored from __doc__
        """ setTravelTime(self, secs: int) """
        pass

    def travelMode(self): # real signature unknown; restored from __doc__
        """ travelMode(self) -> QGeoRouteRequest.TravelMode """
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


