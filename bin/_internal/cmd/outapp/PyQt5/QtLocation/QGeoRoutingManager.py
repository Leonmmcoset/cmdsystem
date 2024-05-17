# encoding: utf-8
# module PyQt5.QtLocation
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtLocation.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QGeoRoutingManager(__PyQt5_QtCore.QObject):
    # no doc
    def calculateRoute(self, request): # real signature unknown; restored from __doc__
        """ calculateRoute(self, request: QGeoRouteRequest) -> Optional[QGeoRouteReply] """
        pass

    def error(self, *args, **kwargs): # real signature unknown
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
        pass

    def finished(self, *args, **kwargs): # real signature unknown
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
        pass

    def locale(self): # real signature unknown; restored from __doc__
        """ locale(self) -> QLocale """
        pass

    def managerName(self): # real signature unknown; restored from __doc__
        """ managerName(self) -> str """
        return ""

    def managerVersion(self): # real signature unknown; restored from __doc__
        """ managerVersion(self) -> int """
        return 0

    def measurementSystem(self): # real signature unknown; restored from __doc__
        """ measurementSystem(self) -> QLocale.MeasurementSystem """
        pass

    def setLocale(self, locale): # real signature unknown; restored from __doc__
        """ setLocale(self, locale: QLocale) """
        pass

    def setMeasurementSystem(self, system): # real signature unknown; restored from __doc__
        """ setMeasurementSystem(self, system: QLocale.MeasurementSystem) """
        pass

    def supportedFeatureTypes(self): # real signature unknown; restored from __doc__
        """ supportedFeatureTypes(self) -> QGeoRouteRequest.FeatureTypes """
        pass

    def supportedFeatureWeights(self): # real signature unknown; restored from __doc__
        """ supportedFeatureWeights(self) -> QGeoRouteRequest.FeatureWeights """
        pass

    def supportedManeuverDetails(self): # real signature unknown; restored from __doc__
        """ supportedManeuverDetails(self) -> QGeoRouteRequest.ManeuverDetails """
        pass

    def supportedRouteOptimizations(self): # real signature unknown; restored from __doc__
        """ supportedRouteOptimizations(self) -> QGeoRouteRequest.RouteOptimizations """
        pass

    def supportedSegmentDetails(self): # real signature unknown; restored from __doc__
        """ supportedSegmentDetails(self) -> QGeoRouteRequest.SegmentDetails """
        pass

    def supportedTravelModes(self): # real signature unknown; restored from __doc__
        """ supportedTravelModes(self) -> QGeoRouteRequest.TravelModes """
        pass

    def updateRoute(self, route, position): # real signature unknown; restored from __doc__
        """ updateRoute(self, route: QGeoRoute, position: QGeoCoordinate) -> Optional[QGeoRouteReply] """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass


