# encoding: utf-8
# module PyQt5.QtLocation
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtLocation.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QGeoRoutingManagerEngine(__PyQt5_QtCore.QObject):
    """ QGeoRoutingManagerEngine(parameters: Dict[str, Any], parent: Optional[QObject] = None) """
    def calculateRoute(self, request): # real signature unknown; restored from __doc__
        """ calculateRoute(self, request: QGeoRouteRequest) -> Optional[QGeoRouteReply] """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
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

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
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

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setLocale(self, locale): # real signature unknown; restored from __doc__
        """ setLocale(self, locale: QLocale) """
        pass

    def setMeasurementSystem(self, system): # real signature unknown; restored from __doc__
        """ setMeasurementSystem(self, system: QLocale.MeasurementSystem) """
        pass

    def setSupportedFeatureTypes(self, featureTypes, QGeoRouteRequest_FeatureTypes=None, QGeoRouteRequest_FeatureType=None): # real signature unknown; restored from __doc__
        """ setSupportedFeatureTypes(self, featureTypes: Union[QGeoRouteRequest.FeatureTypes, QGeoRouteRequest.FeatureType]) """
        pass

    def setSupportedFeatureWeights(self, featureWeights, QGeoRouteRequest_FeatureWeights=None, QGeoRouteRequest_FeatureWeight=None): # real signature unknown; restored from __doc__
        """ setSupportedFeatureWeights(self, featureWeights: Union[QGeoRouteRequest.FeatureWeights, QGeoRouteRequest.FeatureWeight]) """
        pass

    def setSupportedManeuverDetails(self, maneuverDetails, QGeoRouteRequest_ManeuverDetails=None, QGeoRouteRequest_ManeuverDetail=None): # real signature unknown; restored from __doc__
        """ setSupportedManeuverDetails(self, maneuverDetails: Union[QGeoRouteRequest.ManeuverDetails, QGeoRouteRequest.ManeuverDetail]) """
        pass

    def setSupportedRouteOptimizations(self, optimizations, QGeoRouteRequest_RouteOptimizations=None, QGeoRouteRequest_RouteOptimization=None): # real signature unknown; restored from __doc__
        """ setSupportedRouteOptimizations(self, optimizations: Union[QGeoRouteRequest.RouteOptimizations, QGeoRouteRequest.RouteOptimization]) """
        pass

    def setSupportedSegmentDetails(self, segmentDetails, QGeoRouteRequest_SegmentDetails=None, QGeoRouteRequest_SegmentDetail=None): # real signature unknown; restored from __doc__
        """ setSupportedSegmentDetails(self, segmentDetails: Union[QGeoRouteRequest.SegmentDetails, QGeoRouteRequest.SegmentDetail]) """
        pass

    def setSupportedTravelModes(self, travelModes, QGeoRouteRequest_TravelModes=None, QGeoRouteRequest_TravelMode=None): # real signature unknown; restored from __doc__
        """ setSupportedTravelModes(self, travelModes: Union[QGeoRouteRequest.TravelModes, QGeoRouteRequest.TravelMode]) """
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

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def updateRoute(self, route, position): # real signature unknown; restored from __doc__
        """ updateRoute(self, route: QGeoRoute, position: QGeoCoordinate) -> Optional[QGeoRouteReply] """
        pass

    def __init__(self, parameters, p_str=None, Any=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass


