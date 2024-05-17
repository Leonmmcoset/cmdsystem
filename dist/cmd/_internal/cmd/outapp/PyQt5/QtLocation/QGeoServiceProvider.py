# encoding: utf-8
# module PyQt5.QtLocation
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtLocation.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QGeoServiceProvider(__PyQt5_QtCore.QObject):
    """ QGeoServiceProvider(providerName: Optional[str], parameters: Dict[str, Any] = {}, allowExperimental: bool = False) """
    def availableServiceProviders(self): # real signature unknown; restored from __doc__
        """ availableServiceProviders() -> List[str] """
        return []

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def error(self): # real signature unknown; restored from __doc__
        """ error(self) -> QGeoServiceProvider.Error """
        pass

    def errorString(self): # real signature unknown; restored from __doc__
        """ errorString(self) -> str """
        return ""

    def geocodingError(self): # real signature unknown; restored from __doc__
        """ geocodingError(self) -> QGeoServiceProvider.Error """
        pass

    def geocodingErrorString(self): # real signature unknown; restored from __doc__
        """ geocodingErrorString(self) -> str """
        return ""

    def geocodingFeatures(self): # real signature unknown; restored from __doc__
        """ geocodingFeatures(self) -> QGeoServiceProvider.GeocodingFeatures """
        pass

    def geocodingManager(self): # real signature unknown; restored from __doc__
        """ geocodingManager(self) -> Optional[QGeoCodingManager] """
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def mappingError(self): # real signature unknown; restored from __doc__
        """ mappingError(self) -> QGeoServiceProvider.Error """
        pass

    def mappingErrorString(self): # real signature unknown; restored from __doc__
        """ mappingErrorString(self) -> str """
        return ""

    def mappingFeatures(self): # real signature unknown; restored from __doc__
        """ mappingFeatures(self) -> QGeoServiceProvider.MappingFeatures """
        pass

    def navigationError(self): # real signature unknown; restored from __doc__
        """ navigationError(self) -> QGeoServiceProvider.Error """
        pass

    def navigationErrorString(self): # real signature unknown; restored from __doc__
        """ navigationErrorString(self) -> str """
        return ""

    def navigationFeatures(self): # real signature unknown; restored from __doc__
        """ navigationFeatures(self) -> QGeoServiceProvider.NavigationFeatures """
        pass

    def navigationManager(self): # real signature unknown; restored from __doc__
        """ navigationManager(self) -> Optional[QNavigationManager] """
        pass

    def placeManager(self): # real signature unknown; restored from __doc__
        """ placeManager(self) -> Optional[QPlaceManager] """
        pass

    def placesError(self): # real signature unknown; restored from __doc__
        """ placesError(self) -> QGeoServiceProvider.Error """
        pass

    def placesErrorString(self): # real signature unknown; restored from __doc__
        """ placesErrorString(self) -> str """
        return ""

    def placesFeatures(self): # real signature unknown; restored from __doc__
        """ placesFeatures(self) -> QGeoServiceProvider.PlacesFeatures """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def routingError(self): # real signature unknown; restored from __doc__
        """ routingError(self) -> QGeoServiceProvider.Error """
        pass

    def routingErrorString(self): # real signature unknown; restored from __doc__
        """ routingErrorString(self) -> str """
        return ""

    def routingFeatures(self): # real signature unknown; restored from __doc__
        """ routingFeatures(self) -> QGeoServiceProvider.RoutingFeatures """
        pass

    def routingManager(self): # real signature unknown; restored from __doc__
        """ routingManager(self) -> Optional[QGeoRoutingManager] """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setAllowExperimental(self, allow): # real signature unknown; restored from __doc__
        """ setAllowExperimental(self, allow: bool) """
        pass

    def setLocale(self, locale): # real signature unknown; restored from __doc__
        """ setLocale(self, locale: QLocale) """
        pass

    def setParameters(self, parameters, p_str=None, Any=None): # real signature unknown; restored from __doc__
        """ setParameters(self, parameters: Dict[str, Any]) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, providerName, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    AlternativeRoutesFeature = 16
    AnyGeocodingFeatures = -1
    AnyMappingFeatures = -1
    AnyNavigationFeatures = -1
    AnyPlacesFeatures = -1
    AnyRoutingFeatures = -1
    ConnectionError = 4
    ExcludeAreasRoutingFeature = 32
    LoaderError = 5
    LocalizedGeocodingFeature = 8
    LocalizedMappingFeature = 4
    LocalizedPlacesFeature = 256
    LocalizedRoutingFeature = 4
    MissingRequiredParameterError = 3
    NoError = 0
    NoGeocodingFeatures = 0
    NoMappingFeatures = 0
    NoNavigationFeatures = 0
    NoPlacesFeatures = 0
    NoRoutingFeatures = 0
    NotificationsFeature = 512
    NotSupportedError = 1
    OfflineGeocodingFeature = 2
    OfflineMappingFeature = 2
    OfflineNavigationFeature = 2
    OfflinePlacesFeature = 2
    OfflineRoutingFeature = 2
    OnlineGeocodingFeature = 1
    OnlineMappingFeature = 1
    OnlineNavigationFeature = 1
    OnlinePlacesFeature = 1
    OnlineRoutingFeature = 1
    PlaceMatchingFeature = 1024
    PlaceRecommendationsFeature = 64
    RemoveCategoryFeature = 32
    RemovePlaceFeature = 8
    ReverseGeocodingFeature = 4
    RouteUpdatesFeature = 8
    SaveCategoryFeature = 16
    SavePlaceFeature = 4
    SearchSuggestionsFeature = 128
    UnknownParameterError = 2


