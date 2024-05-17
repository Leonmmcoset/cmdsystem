# encoding: utf-8
# module PyQt5.QtPositioning
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtPositioning.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


# no functions
# classes

class QGeoAddress(__sip.wrapper):
    """
    QGeoAddress()
    QGeoAddress(other: QGeoAddress)
    """
    def city(self): # real signature unknown; restored from __doc__
        """ city(self) -> str """
        return ""

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def country(self): # real signature unknown; restored from __doc__
        """ country(self) -> str """
        return ""

    def countryCode(self): # real signature unknown; restored from __doc__
        """ countryCode(self) -> str """
        return ""

    def county(self): # real signature unknown; restored from __doc__
        """ county(self) -> str """
        return ""

    def district(self): # real signature unknown; restored from __doc__
        """ district(self) -> str """
        return ""

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ isEmpty(self) -> bool """
        return False

    def isTextGenerated(self): # real signature unknown; restored from __doc__
        """ isTextGenerated(self) -> bool """
        return False

    def postalCode(self): # real signature unknown; restored from __doc__
        """ postalCode(self) -> str """
        return ""

    def setCity(self, city, p_str=None): # real signature unknown; restored from __doc__
        """ setCity(self, city: Optional[str]) """
        pass

    def setCountry(self, country, p_str=None): # real signature unknown; restored from __doc__
        """ setCountry(self, country: Optional[str]) """
        pass

    def setCountryCode(self, countryCode, p_str=None): # real signature unknown; restored from __doc__
        """ setCountryCode(self, countryCode: Optional[str]) """
        pass

    def setCounty(self, county, p_str=None): # real signature unknown; restored from __doc__
        """ setCounty(self, county: Optional[str]) """
        pass

    def setDistrict(self, district, p_str=None): # real signature unknown; restored from __doc__
        """ setDistrict(self, district: Optional[str]) """
        pass

    def setPostalCode(self, postalCode, p_str=None): # real signature unknown; restored from __doc__
        """ setPostalCode(self, postalCode: Optional[str]) """
        pass

    def setState(self, state, p_str=None): # real signature unknown; restored from __doc__
        """ setState(self, state: Optional[str]) """
        pass

    def setStreet(self, street, p_str=None): # real signature unknown; restored from __doc__
        """ setStreet(self, street: Optional[str]) """
        pass

    def setText(self, text, p_str=None): # real signature unknown; restored from __doc__
        """ setText(self, text: Optional[str]) """
        pass

    def state(self): # real signature unknown; restored from __doc__
        """ state(self) -> str """
        return ""

    def street(self): # real signature unknown; restored from __doc__
        """ street(self) -> str """
        return ""

    def text(self): # real signature unknown; restored from __doc__
        """ text(self) -> str """
        return ""

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


class QGeoAreaMonitorInfo(__sip.wrapper):
    """
    QGeoAreaMonitorInfo(name: Optional[str] = '')
    QGeoAreaMonitorInfo(other: QGeoAreaMonitorInfo)
    """
    def area(self): # real signature unknown; restored from __doc__
        """ area(self) -> QGeoShape """
        return QGeoShape

    def expiration(self): # real signature unknown; restored from __doc__
        """ expiration(self) -> QDateTime """
        pass

    def identifier(self): # real signature unknown; restored from __doc__
        """ identifier(self) -> str """
        return ""

    def isPersistent(self): # real signature unknown; restored from __doc__
        """ isPersistent(self) -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def name(self): # real signature unknown; restored from __doc__
        """ name(self) -> str """
        return ""

    def notificationParameters(self): # real signature unknown; restored from __doc__
        """ notificationParameters(self) -> Dict[str, Any] """
        return {}

    def setArea(self, newShape): # real signature unknown; restored from __doc__
        """ setArea(self, newShape: QGeoShape) """
        pass

    def setExpiration(self, expiry, QDateTime=None, datetime_datetime=None): # real signature unknown; restored from __doc__
        """ setExpiration(self, expiry: Union[QDateTime, datetime.datetime]) """
        pass

    def setName(self, name, p_str=None): # real signature unknown; restored from __doc__
        """ setName(self, name: Optional[str]) """
        pass

    def setNotificationParameters(self, parameters, p_str=None, Any=None): # real signature unknown; restored from __doc__
        """ setNotificationParameters(self, parameters: Dict[str, Any]) """
        pass

    def setPersistent(self, isPersistent): # real signature unknown; restored from __doc__
        """ setPersistent(self, isPersistent: bool) """
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


    __hash__ = None


class QGeoAreaMonitorSource(__PyQt5_QtCore.QObject):
    """ QGeoAreaMonitorSource(parent: Optional[QObject]) """
    def activeMonitors(self, lookupArea=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        activeMonitors(self) -> List[QGeoAreaMonitorInfo]
        activeMonitors(self, lookupArea: QGeoShape) -> List[QGeoAreaMonitorInfo]
        """
        return []

    def areaEntered(self, *args, **kwargs): # real signature unknown
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

    def areaExited(self, *args, **kwargs): # real signature unknown
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

    def availableSources(self): # real signature unknown; restored from __doc__
        """ availableSources() -> List[str] """
        return []

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def createDefaultSource(self, parent, QObject=None): # real signature unknown; restored from __doc__
        """ createDefaultSource(parent: Optional[QObject]) -> Optional[QGeoAreaMonitorSource] """
        pass

    def createSource(self, sourceName, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ createSource(sourceName: Optional[str], parent: Optional[QObject]) -> Optional[QGeoAreaMonitorSource] """
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

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def monitorExpired(self, *args, **kwargs): # real signature unknown
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

    def positionInfoSource(self): # real signature unknown; restored from __doc__
        """ positionInfoSource(self) -> Optional[QGeoPositionInfoSource] """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def requestUpdate(self, monitor, signal, p_str=None): # real signature unknown; restored from __doc__
        """ requestUpdate(self, monitor: QGeoAreaMonitorInfo, signal: Optional[str]) -> bool """
        return False

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setPositionInfoSource(self, source, QGeoPositionInfoSource=None): # real signature unknown; restored from __doc__
        """ setPositionInfoSource(self, source: Optional[QGeoPositionInfoSource]) """
        pass

    def sourceName(self): # real signature unknown; restored from __doc__
        """ sourceName(self) -> str """
        return ""

    def startMonitoring(self, monitor): # real signature unknown; restored from __doc__
        """ startMonitoring(self, monitor: QGeoAreaMonitorInfo) -> bool """
        return False

    def stopMonitoring(self, monitor): # real signature unknown; restored from __doc__
        """ stopMonitoring(self, monitor: QGeoAreaMonitorInfo) -> bool """
        return False

    def supportedAreaMonitorFeatures(self): # real signature unknown; restored from __doc__
        """ supportedAreaMonitorFeatures(self) -> QGeoAreaMonitorSource.AreaMonitorFeatures """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent, QObject=None): # real signature unknown; restored from __doc__
        pass

    AccessError = 0
    AnyAreaMonitorFeature = -1
    InsufficientPositionInfo = 1
    NoError = 3
    PersistentAreaMonitorFeature = 1
    UnknownSourceError = 2


class QGeoShape(__sip.wrapper):
    """
    QGeoShape()
    QGeoShape(other: QGeoShape)
    """
    def boundingGeoRectangle(self): # real signature unknown; restored from __doc__
        """ boundingGeoRectangle(self) -> QGeoRectangle """
        return QGeoRectangle

    def center(self): # real signature unknown; restored from __doc__
        """ center(self) -> QGeoCoordinate """
        return QGeoCoordinate

    def contains(self, coordinate): # real signature unknown; restored from __doc__
        """ contains(self, coordinate: QGeoCoordinate) -> bool """
        return False

    def extendShape(self, coordinate): # real signature unknown; restored from __doc__
        """ extendShape(self, coordinate: QGeoCoordinate) """
        pass

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ isEmpty(self) -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def toString(self): # real signature unknown; restored from __doc__
        """ toString(self) -> str """
        return ""

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> QGeoShape.ShapeType """
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


    CircleType = 2
    PathType = 3
    PolygonType = 4
    RectangleType = 1
    UnknownType = 0
    __hash__ = None


class QGeoCircle(QGeoShape):
    """
    QGeoCircle()
    QGeoCircle(center: QGeoCoordinate, radius: float = -1)
    QGeoCircle(other: QGeoCircle)
    QGeoCircle(other: QGeoShape)
    """
    def center(self): # real signature unknown; restored from __doc__
        """ center(self) -> QGeoCoordinate """
        return QGeoCoordinate

    def extendCircle(self, coordinate): # real signature unknown; restored from __doc__
        """ extendCircle(self, coordinate: QGeoCoordinate) """
        pass

    def radius(self): # real signature unknown; restored from __doc__
        """ radius(self) -> float """
        return 0.0

    def setCenter(self, center): # real signature unknown; restored from __doc__
        """ setCenter(self, center: QGeoCoordinate) """
        pass

    def setRadius(self, radius): # real signature unknown; restored from __doc__
        """ setRadius(self, radius: float) """
        pass

    def toString(self): # real signature unknown; restored from __doc__
        """ toString(self) -> str """
        return ""

    def translate(self, degreesLatitude, degreesLongitude): # real signature unknown; restored from __doc__
        """ translate(self, degreesLatitude: float, degreesLongitude: float) """
        pass

    def translated(self, degreesLatitude, degreesLongitude): # real signature unknown; restored from __doc__
        """ translated(self, degreesLatitude: float, degreesLongitude: float) -> QGeoCircle """
        return QGeoCircle

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

    __hash__ = None


class QGeoCoordinate(__sip.wrapper):
    """
    QGeoCoordinate()
    QGeoCoordinate(latitude: float, longitude: float)
    QGeoCoordinate(latitude: float, longitude: float, altitude: float)
    QGeoCoordinate(other: QGeoCoordinate)
    """
    def altitude(self): # real signature unknown; restored from __doc__
        """ altitude(self) -> float """
        return 0.0

    def atDistanceAndAzimuth(self, distance, azimuth, distanceUp=0): # real signature unknown; restored from __doc__
        """ atDistanceAndAzimuth(self, distance: float, azimuth: float, distanceUp: float = 0) -> QGeoCoordinate """
        return QGeoCoordinate

    def azimuthTo(self, other): # real signature unknown; restored from __doc__
        """ azimuthTo(self, other: QGeoCoordinate) -> float """
        return 0.0

    def distanceTo(self, other): # real signature unknown; restored from __doc__
        """ distanceTo(self, other: QGeoCoordinate) -> float """
        return 0.0

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def latitude(self): # real signature unknown; restored from __doc__
        """ latitude(self) -> float """
        return 0.0

    def longitude(self): # real signature unknown; restored from __doc__
        """ longitude(self) -> float """
        return 0.0

    def setAltitude(self, altitude): # real signature unknown; restored from __doc__
        """ setAltitude(self, altitude: float) """
        pass

    def setLatitude(self, latitude): # real signature unknown; restored from __doc__
        """ setLatitude(self, latitude: float) """
        pass

    def setLongitude(self, longitude): # real signature unknown; restored from __doc__
        """ setLongitude(self, longitude: float) """
        pass

    def toString(self, format=None): # real signature unknown; restored from __doc__
        """ toString(self, format: QGeoCoordinate.CoordinateFormat = QGeoCoordinate.DegreesMinutesSecondsWithHemisphere) -> str """
        return ""

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> QGeoCoordinate.CoordinateType """
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

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
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


    Coordinate2D = 1
    Coordinate3D = 2
    Degrees = 0
    DegreesMinutes = 2
    DegreesMinutesSeconds = 4
    DegreesMinutesSecondsWithHemisphere = 5
    DegreesMinutesWithHemisphere = 3
    DegreesWithHemisphere = 1
    InvalidCoordinate = 0


class QGeoLocation(__sip.wrapper):
    """
    QGeoLocation()
    QGeoLocation(other: QGeoLocation)
    """
    def address(self): # real signature unknown; restored from __doc__
        """ address(self) -> QGeoAddress """
        return QGeoAddress

    def boundingBox(self): # real signature unknown; restored from __doc__
        """ boundingBox(self) -> QGeoRectangle """
        return QGeoRectangle

    def coordinate(self): # real signature unknown; restored from __doc__
        """ coordinate(self) -> QGeoCoordinate """
        return QGeoCoordinate

    def extendedAttributes(self): # real signature unknown; restored from __doc__
        """ extendedAttributes(self) -> Dict[str, Any] """
        return {}

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ isEmpty(self) -> bool """
        return False

    def setAddress(self, address): # real signature unknown; restored from __doc__
        """ setAddress(self, address: QGeoAddress) """
        pass

    def setBoundingBox(self, box): # real signature unknown; restored from __doc__
        """ setBoundingBox(self, box: QGeoRectangle) """
        pass

    def setCoordinate(self, position): # real signature unknown; restored from __doc__
        """ setCoordinate(self, position: QGeoCoordinate) """
        pass

    def setExtendedAttributes(self, data, p_str=None, Any=None): # real signature unknown; restored from __doc__
        """ setExtendedAttributes(self, data: Dict[str, Any]) """
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


class QGeoPath(QGeoShape):
    """
    QGeoPath()
    QGeoPath(path: Iterable[QGeoCoordinate], width: float = 0)
    QGeoPath(other: QGeoPath)
    QGeoPath(other: QGeoShape)
    """
    def addCoordinate(self, coordinate): # real signature unknown; restored from __doc__
        """ addCoordinate(self, coordinate: QGeoCoordinate) """
        pass

    def clearPath(self): # real signature unknown; restored from __doc__
        """ clearPath(self) """
        pass

    def containsCoordinate(self, coordinate): # real signature unknown; restored from __doc__
        """ containsCoordinate(self, coordinate: QGeoCoordinate) -> bool """
        return False

    def coordinateAt(self, index): # real signature unknown; restored from __doc__
        """ coordinateAt(self, index: int) -> QGeoCoordinate """
        return QGeoCoordinate

    def insertCoordinate(self, index, coordinate): # real signature unknown; restored from __doc__
        """ insertCoordinate(self, index: int, coordinate: QGeoCoordinate) """
        pass

    def length(self, indexFrom=0, indexTo=-1): # real signature unknown; restored from __doc__
        """ length(self, indexFrom: int = 0, indexTo: int = -1) -> float """
        return 0.0

    def path(self): # real signature unknown; restored from __doc__
        """ path(self) -> List[QGeoCoordinate] """
        return []

    def removeCoordinate(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        removeCoordinate(self, coordinate: QGeoCoordinate)
        removeCoordinate(self, index: int)
        """
        pass

    def replaceCoordinate(self, index, coordinate): # real signature unknown; restored from __doc__
        """ replaceCoordinate(self, index: int, coordinate: QGeoCoordinate) """
        pass

    def setPath(self, path, QGeoCoordinate=None): # real signature unknown; restored from __doc__
        """ setPath(self, path: Iterable[QGeoCoordinate]) """
        pass

    def setWidth(self, width): # real signature unknown; restored from __doc__
        """ setWidth(self, width: float) """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ size(self) -> int """
        return 0

    def toString(self): # real signature unknown; restored from __doc__
        """ toString(self) -> str """
        return ""

    def translate(self, degreesLatitude, degreesLongitude): # real signature unknown; restored from __doc__
        """ translate(self, degreesLatitude: float, degreesLongitude: float) """
        pass

    def translated(self, degreesLatitude, degreesLongitude): # real signature unknown; restored from __doc__
        """ translated(self, degreesLatitude: float, degreesLongitude: float) -> QGeoPath """
        return QGeoPath

    def width(self): # real signature unknown; restored from __doc__
        """ width(self) -> float """
        return 0.0

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

    __hash__ = None


class QGeoPolygon(QGeoShape):
    """
    QGeoPolygon()
    QGeoPolygon(path: Iterable[QGeoCoordinate])
    QGeoPolygon(other: QGeoPolygon)
    QGeoPolygon(other: QGeoShape)
    """
    def addCoordinate(self, coordinate): # real signature unknown; restored from __doc__
        """ addCoordinate(self, coordinate: QGeoCoordinate) """
        pass

    def addHole(self, holePath, QGeoCoordinate=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        addHole(self, holePath: Iterable[QGeoCoordinate])
        addHole(self, holePath: Any)
        """
        pass

    def containsCoordinate(self, coordinate): # real signature unknown; restored from __doc__
        """ containsCoordinate(self, coordinate: QGeoCoordinate) -> bool """
        return False

    def coordinateAt(self, index): # real signature unknown; restored from __doc__
        """ coordinateAt(self, index: int) -> QGeoCoordinate """
        return QGeoCoordinate

    def hole(self, index): # real signature unknown; restored from __doc__
        """ hole(self, index: int) -> List[Any] """
        return []

    def holePath(self, index): # real signature unknown; restored from __doc__
        """ holePath(self, index: int) -> List[QGeoCoordinate] """
        return []

    def holesCount(self): # real signature unknown; restored from __doc__
        """ holesCount(self) -> int """
        return 0

    def insertCoordinate(self, index, coordinate): # real signature unknown; restored from __doc__
        """ insertCoordinate(self, index: int, coordinate: QGeoCoordinate) """
        pass

    def length(self, indexFrom=0, indexTo=-1): # real signature unknown; restored from __doc__
        """ length(self, indexFrom: int = 0, indexTo: int = -1) -> float """
        return 0.0

    def path(self): # real signature unknown; restored from __doc__
        """ path(self) -> List[QGeoCoordinate] """
        return []

    def perimeter(self): # real signature unknown; restored from __doc__
        """ perimeter(self) -> List[Any] """
        return []

    def removeCoordinate(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        removeCoordinate(self, coordinate: QGeoCoordinate)
        removeCoordinate(self, index: int)
        """
        pass

    def removeHole(self, index): # real signature unknown; restored from __doc__
        """ removeHole(self, index: int) """
        pass

    def replaceCoordinate(self, index, coordinate): # real signature unknown; restored from __doc__
        """ replaceCoordinate(self, index: int, coordinate: QGeoCoordinate) """
        pass

    def setPath(self, path, QGeoCoordinate=None): # real signature unknown; restored from __doc__
        """ setPath(self, path: Iterable[QGeoCoordinate]) """
        pass

    def setPerimeter(self, path, Any=None): # real signature unknown; restored from __doc__
        """ setPerimeter(self, path: Iterable[Any]) """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ size(self) -> int """
        return 0

    def toString(self): # real signature unknown; restored from __doc__
        """ toString(self) -> str """
        return ""

    def translate(self, degreesLatitude, degreesLongitude): # real signature unknown; restored from __doc__
        """ translate(self, degreesLatitude: float, degreesLongitude: float) """
        pass

    def translated(self, degreesLatitude, degreesLongitude): # real signature unknown; restored from __doc__
        """ translated(self, degreesLatitude: float, degreesLongitude: float) -> QGeoPolygon """
        return QGeoPolygon

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

    __hash__ = None


class QGeoPositionInfo(__sip.wrapper):
    """
    QGeoPositionInfo()
    QGeoPositionInfo(coordinate: QGeoCoordinate, updateTime: Union[QDateTime, datetime.datetime])
    QGeoPositionInfo(other: QGeoPositionInfo)
    """
    def attribute(self, attribute): # real signature unknown; restored from __doc__
        """ attribute(self, attribute: QGeoPositionInfo.Attribute) -> float """
        return 0.0

    def coordinate(self): # real signature unknown; restored from __doc__
        """ coordinate(self) -> QGeoCoordinate """
        return QGeoCoordinate

    def hasAttribute(self, attribute): # real signature unknown; restored from __doc__
        """ hasAttribute(self, attribute: QGeoPositionInfo.Attribute) -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def removeAttribute(self, attribute): # real signature unknown; restored from __doc__
        """ removeAttribute(self, attribute: QGeoPositionInfo.Attribute) """
        pass

    def setAttribute(self, attribute, value): # real signature unknown; restored from __doc__
        """ setAttribute(self, attribute: QGeoPositionInfo.Attribute, value: float) """
        pass

    def setCoordinate(self, coordinate): # real signature unknown; restored from __doc__
        """ setCoordinate(self, coordinate: QGeoCoordinate) """
        pass

    def setTimestamp(self, timestamp, QDateTime=None, datetime_datetime=None): # real signature unknown; restored from __doc__
        """ setTimestamp(self, timestamp: Union[QDateTime, datetime.datetime]) """
        pass

    def timestamp(self): # real signature unknown; restored from __doc__
        """ timestamp(self) -> QDateTime """
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


    Direction = 0
    GroundSpeed = 1
    HorizontalAccuracy = 4
    MagneticVariation = 3
    VerticalAccuracy = 5
    VerticalSpeed = 2
    __hash__ = None


class QGeoPositionInfoSource(__PyQt5_QtCore.QObject):
    """ QGeoPositionInfoSource(parent: Optional[QObject]) """
    def availableSources(self): # real signature unknown; restored from __doc__
        """ availableSources() -> List[str] """
        return []

    def backendProperty(self, name, p_str=None): # real signature unknown; restored from __doc__
        """ backendProperty(self, name: Optional[str]) -> Any """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def createDefaultSource(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        createDefaultSource(parent: Optional[QObject]) -> Optional[QGeoPositionInfoSource]
        createDefaultSource(parameters: Dict[str, Any], parent: Optional[QObject]) -> Optional[QGeoPositionInfoSource]
        """
        pass

    def createSource(self, sourceName, p_str=None, *args, **kwargs): # real signature unknown; restored from __doc__ with multiple overloads
        """
        createSource(sourceName: Optional[str], parent: Optional[QObject]) -> Optional[QGeoPositionInfoSource]
        createSource(sourceName: Optional[str], parameters: Dict[str, Any], parent: Optional[QObject]) -> Optional[QGeoPositionInfoSource]
        """
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

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def lastKnownPosition(self, fromSatellitePositioningMethodsOnly=False): # real signature unknown; restored from __doc__
        """ lastKnownPosition(self, fromSatellitePositioningMethodsOnly: bool = False) -> QGeoPositionInfo """
        return QGeoPositionInfo

    def minimumUpdateInterval(self): # real signature unknown; restored from __doc__
        """ minimumUpdateInterval(self) -> int """
        return 0

    def positionUpdated(self, *args, **kwargs): # real signature unknown
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

    def preferredPositioningMethods(self): # real signature unknown; restored from __doc__
        """ preferredPositioningMethods(self) -> QGeoPositionInfoSource.PositioningMethods """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def requestUpdate(self, timeout=0): # real signature unknown; restored from __doc__
        """ requestUpdate(self, timeout: int = 0) """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setBackendProperty(self, name, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setBackendProperty(self, name: Optional[str], value: Any) -> bool """
        pass

    def setPreferredPositioningMethods(self, methods, QGeoPositionInfoSource_PositioningMethods=None, QGeoPositionInfoSource_PositioningMethod=None): # real signature unknown; restored from __doc__
        """ setPreferredPositioningMethods(self, methods: Union[QGeoPositionInfoSource.PositioningMethods, QGeoPositionInfoSource.PositioningMethod]) """
        pass

    def setUpdateInterval(self, msec): # real signature unknown; restored from __doc__
        """ setUpdateInterval(self, msec: int) """
        pass

    def sourceName(self): # real signature unknown; restored from __doc__
        """ sourceName(self) -> str """
        return ""

    def startUpdates(self): # real signature unknown; restored from __doc__
        """ startUpdates(self) """
        pass

    def stopUpdates(self): # real signature unknown; restored from __doc__
        """ stopUpdates(self) """
        pass

    def supportedPositioningMethods(self): # real signature unknown; restored from __doc__
        """ supportedPositioningMethods(self) -> QGeoPositionInfoSource.PositioningMethods """
        pass

    def supportedPositioningMethodsChanged(self, *args, **kwargs): # real signature unknown
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

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def updateInterval(self): # real signature unknown; restored from __doc__
        """ updateInterval(self) -> int """
        return 0

    def updateTimeout(self, *args, **kwargs): # real signature unknown
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

    def __init__(self, parent, QObject=None): # real signature unknown; restored from __doc__
        pass

    AccessError = 0
    AllPositioningMethods = -1
    ClosedError = 1
    NoError = 3
    NonSatellitePositioningMethods = -256
    NoPositioningMethods = 0
    SatellitePositioningMethods = 255
    UnknownSourceError = 2


class QGeoRectangle(QGeoShape):
    """
    QGeoRectangle()
    QGeoRectangle(center: QGeoCoordinate, degreesWidth: float, degreesHeight: float)
    QGeoRectangle(topLeft: QGeoCoordinate, bottomRight: QGeoCoordinate)
    QGeoRectangle(coordinates: Iterable[QGeoCoordinate])
    QGeoRectangle(other: QGeoRectangle)
    QGeoRectangle(other: QGeoShape)
    """
    def bottomLeft(self): # real signature unknown; restored from __doc__
        """ bottomLeft(self) -> QGeoCoordinate """
        return QGeoCoordinate

    def bottomRight(self): # real signature unknown; restored from __doc__
        """ bottomRight(self) -> QGeoCoordinate """
        return QGeoCoordinate

    def center(self): # real signature unknown; restored from __doc__
        """ center(self) -> QGeoCoordinate """
        return QGeoCoordinate

    def contains(self, rectangle): # real signature unknown; restored from __doc__
        """ contains(self, rectangle: QGeoRectangle) -> bool """
        return False

    def extendRectangle(self, coordinate): # real signature unknown; restored from __doc__
        """ extendRectangle(self, coordinate: QGeoCoordinate) """
        pass

    def height(self): # real signature unknown; restored from __doc__
        """ height(self) -> float """
        return 0.0

    def intersects(self, rectangle): # real signature unknown; restored from __doc__
        """ intersects(self, rectangle: QGeoRectangle) -> bool """
        return False

    def setBottomLeft(self, bottomLeft): # real signature unknown; restored from __doc__
        """ setBottomLeft(self, bottomLeft: QGeoCoordinate) """
        pass

    def setBottomRight(self, bottomRight): # real signature unknown; restored from __doc__
        """ setBottomRight(self, bottomRight: QGeoCoordinate) """
        pass

    def setCenter(self, center): # real signature unknown; restored from __doc__
        """ setCenter(self, center: QGeoCoordinate) """
        pass

    def setHeight(self, degreesHeight): # real signature unknown; restored from __doc__
        """ setHeight(self, degreesHeight: float) """
        pass

    def setTopLeft(self, topLeft): # real signature unknown; restored from __doc__
        """ setTopLeft(self, topLeft: QGeoCoordinate) """
        pass

    def setTopRight(self, topRight): # real signature unknown; restored from __doc__
        """ setTopRight(self, topRight: QGeoCoordinate) """
        pass

    def setWidth(self, degreesWidth): # real signature unknown; restored from __doc__
        """ setWidth(self, degreesWidth: float) """
        pass

    def topLeft(self): # real signature unknown; restored from __doc__
        """ topLeft(self) -> QGeoCoordinate """
        return QGeoCoordinate

    def topRight(self): # real signature unknown; restored from __doc__
        """ topRight(self) -> QGeoCoordinate """
        return QGeoCoordinate

    def toString(self): # real signature unknown; restored from __doc__
        """ toString(self) -> str """
        return ""

    def translate(self, degreesLatitude, degreesLongitude): # real signature unknown; restored from __doc__
        """ translate(self, degreesLatitude: float, degreesLongitude: float) """
        pass

    def translated(self, degreesLatitude, degreesLongitude): # real signature unknown; restored from __doc__
        """ translated(self, degreesLatitude: float, degreesLongitude: float) -> QGeoRectangle """
        return QGeoRectangle

    def united(self, rectangle): # real signature unknown; restored from __doc__
        """ united(self, rectangle: QGeoRectangle) -> QGeoRectangle """
        return QGeoRectangle

    def width(self): # real signature unknown; restored from __doc__
        """ width(self) -> float """
        return 0.0

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

    def __ior__(self, *args, **kwargs): # real signature unknown
        """ Return self|=value. """
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

    def __or__(self, *args, **kwargs): # real signature unknown
        """ Return self|value. """
        pass

    def __ror__(self, *args, **kwargs): # real signature unknown
        """ Return value|self. """
        pass

    __hash__ = None


class QGeoSatelliteInfo(__sip.wrapper):
    """
    QGeoSatelliteInfo()
    QGeoSatelliteInfo(other: QGeoSatelliteInfo)
    """
    def attribute(self, attribute): # real signature unknown; restored from __doc__
        """ attribute(self, attribute: QGeoSatelliteInfo.Attribute) -> float """
        return 0.0

    def hasAttribute(self, attribute): # real signature unknown; restored from __doc__
        """ hasAttribute(self, attribute: QGeoSatelliteInfo.Attribute) -> bool """
        return False

    def removeAttribute(self, attribute): # real signature unknown; restored from __doc__
        """ removeAttribute(self, attribute: QGeoSatelliteInfo.Attribute) """
        pass

    def satelliteIdentifier(self): # real signature unknown; restored from __doc__
        """ satelliteIdentifier(self) -> int """
        return 0

    def satelliteSystem(self): # real signature unknown; restored from __doc__
        """ satelliteSystem(self) -> QGeoSatelliteInfo.SatelliteSystem """
        pass

    def setAttribute(self, attribute, value): # real signature unknown; restored from __doc__
        """ setAttribute(self, attribute: QGeoSatelliteInfo.Attribute, value: float) """
        pass

    def setSatelliteIdentifier(self, satId): # real signature unknown; restored from __doc__
        """ setSatelliteIdentifier(self, satId: int) """
        pass

    def setSatelliteSystem(self, system): # real signature unknown; restored from __doc__
        """ setSatelliteSystem(self, system: QGeoSatelliteInfo.SatelliteSystem) """
        pass

    def setSignalStrength(self, signalStrength): # real signature unknown; restored from __doc__
        """ setSignalStrength(self, signalStrength: int) """
        pass

    def signalStrength(self): # real signature unknown; restored from __doc__
        """ signalStrength(self) -> int """
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


    Azimuth = 1
    Elevation = 0
    GLONASS = 2
    GPS = 1
    Undefined = 0
    __hash__ = None


class QGeoSatelliteInfoSource(__PyQt5_QtCore.QObject):
    """ QGeoSatelliteInfoSource(parent: Optional[QObject]) """
    def availableSources(self): # real signature unknown; restored from __doc__
        """ availableSources() -> List[str] """
        return []

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def createDefaultSource(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        createDefaultSource(parent: Optional[QObject]) -> Optional[QGeoSatelliteInfoSource]
        createDefaultSource(parameters: Dict[str, Any], parent: Optional[QObject]) -> Optional[QGeoSatelliteInfoSource]
        """
        pass

    def createSource(self, sourceName, p_str=None, *args, **kwargs): # real signature unknown; restored from __doc__ with multiple overloads
        """
        createSource(sourceName: Optional[str], parent: Optional[QObject]) -> Optional[QGeoSatelliteInfoSource]
        createSource(sourceName: Optional[str], parameters: Dict[str, Any], parent: Optional[QObject]) -> Optional[QGeoSatelliteInfoSource]
        """
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

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def minimumUpdateInterval(self): # real signature unknown; restored from __doc__
        """ minimumUpdateInterval(self) -> int """
        return 0

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def requestTimeout(self, *args, **kwargs): # real signature unknown
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

    def requestUpdate(self, timeout=0): # real signature unknown; restored from __doc__
        """ requestUpdate(self, timeout: int = 0) """
        pass

    def satellitesInUseUpdated(self, *args, **kwargs): # real signature unknown
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

    def satellitesInViewUpdated(self, *args, **kwargs): # real signature unknown
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

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setUpdateInterval(self, msec): # real signature unknown; restored from __doc__
        """ setUpdateInterval(self, msec: int) """
        pass

    def sourceName(self): # real signature unknown; restored from __doc__
        """ sourceName(self) -> str """
        return ""

    def startUpdates(self): # real signature unknown; restored from __doc__
        """ startUpdates(self) """
        pass

    def stopUpdates(self): # real signature unknown; restored from __doc__
        """ stopUpdates(self) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def updateInterval(self): # real signature unknown; restored from __doc__
        """ updateInterval(self) -> int """
        return 0

    def __init__(self, parent, QObject=None): # real signature unknown; restored from __doc__
        pass

    AccessError = 0
    ClosedError = 1
    NoError = 2
    UnknownSourceError = -1


class QNmeaPositionInfoSource(QGeoPositionInfoSource):
    """ QNmeaPositionInfoSource(updateMode: QNmeaPositionInfoSource.UpdateMode, parent: Optional[QObject] = None) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def device(self): # real signature unknown; restored from __doc__
        """ device(self) -> Optional[QIODevice] """
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def error(self): # real signature unknown; restored from __doc__
        """ error(self) -> QGeoPositionInfoSource.Error """
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def lastKnownPosition(self, fromSatellitePositioningMethodsOnly=False): # real signature unknown; restored from __doc__
        """ lastKnownPosition(self, fromSatellitePositioningMethodsOnly: bool = False) -> QGeoPositionInfo """
        return QGeoPositionInfo

    def minimumUpdateInterval(self): # real signature unknown; restored from __doc__
        """ minimumUpdateInterval(self) -> int """
        return 0

    def parsePosInfoFromNmeaData(self, data, bytes=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ parsePosInfoFromNmeaData(self, data: Optional[bytes], size: int, posInfo: Optional[QGeoPositionInfo]) -> (bool, Optional[bool]) """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def requestUpdate(self, timeout=0): # real signature unknown; restored from __doc__
        """ requestUpdate(self, timeout: int = 0) """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setDevice(self, source, QIODevice=None): # real signature unknown; restored from __doc__
        """ setDevice(self, source: Optional[QIODevice]) """
        pass

    def setUpdateInterval(self, msec): # real signature unknown; restored from __doc__
        """ setUpdateInterval(self, msec: int) """
        pass

    def setUserEquivalentRangeError(self, uere): # real signature unknown; restored from __doc__
        """ setUserEquivalentRangeError(self, uere: float) """
        pass

    def startUpdates(self): # real signature unknown; restored from __doc__
        """ startUpdates(self) """
        pass

    def stopUpdates(self): # real signature unknown; restored from __doc__
        """ stopUpdates(self) """
        pass

    def supportedPositioningMethods(self): # real signature unknown; restored from __doc__
        """ supportedPositioningMethods(self) -> QGeoPositionInfoSource.PositioningMethods """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def updateMode(self): # real signature unknown; restored from __doc__
        """ updateMode(self) -> QNmeaPositionInfoSource.UpdateMode """
        pass

    def userEquivalentRangeError(self): # real signature unknown; restored from __doc__
        """ userEquivalentRangeError(self) -> float """
        return 0.0

    def __init__(self, updateMode, parent, QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    RealTimeMode = 1
    SimulationMode = 2


# variables with complex values



