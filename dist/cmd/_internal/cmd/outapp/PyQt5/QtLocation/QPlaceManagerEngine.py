# encoding: utf-8
# module PyQt5.QtLocation
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtLocation.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QPlaceManagerEngine(__PyQt5_QtCore.QObject):
    """ QPlaceManagerEngine(parameters: Dict[str, Any], parent: Optional[QObject] = None) """
    def category(self, categoryId, p_str=None): # real signature unknown; restored from __doc__
        """ category(self, categoryId: Optional[str]) -> QPlaceCategory """
        return QPlaceCategory

    def categoryAdded(self, *args, **kwargs): # real signature unknown
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

    def categoryRemoved(self, *args, **kwargs): # real signature unknown
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

    def categoryUpdated(self, *args, **kwargs): # real signature unknown
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

    def childCategories(self, parentId, p_str=None): # real signature unknown; restored from __doc__
        """ childCategories(self, parentId: Optional[str]) -> List[QPlaceCategory] """
        return []

    def childCategoryIds(self, categoryId, p_str=None): # real signature unknown; restored from __doc__
        """ childCategoryIds(self, categoryId: Optional[str]) -> List[str] """
        return []

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def compatiblePlace(self, original): # real signature unknown; restored from __doc__
        """ compatiblePlace(self, original: QPlace) -> QPlace """
        return QPlace

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def constructIconUrl(self, icon, size): # real signature unknown; restored from __doc__
        """ constructIconUrl(self, icon: QPlaceIcon, size: QSize) -> QUrl """
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dataChanged(self, *args, **kwargs): # real signature unknown
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

    def getPlaceContent(self, request): # real signature unknown; restored from __doc__
        """ getPlaceContent(self, request: QPlaceContentRequest) -> Optional[QPlaceContentReply] """
        pass

    def getPlaceDetails(self, placeId, p_str=None): # real signature unknown; restored from __doc__
        """ getPlaceDetails(self, placeId: Optional[str]) -> Optional[QPlaceDetailsReply] """
        pass

    def initializeCategories(self): # real signature unknown; restored from __doc__
        """ initializeCategories(self) -> Optional[QPlaceReply] """
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def locales(self): # real signature unknown; restored from __doc__
        """ locales(self) -> List[QLocale] """
        return []

    def manager(self): # real signature unknown; restored from __doc__
        """ manager(self) -> Optional[QPlaceManager] """
        pass

    def managerName(self): # real signature unknown; restored from __doc__
        """ managerName(self) -> str """
        return ""

    def managerVersion(self): # real signature unknown; restored from __doc__
        """ managerVersion(self) -> int """
        return 0

    def matchingPlaces(self, request): # real signature unknown; restored from __doc__
        """ matchingPlaces(self, request: QPlaceMatchRequest) -> Optional[QPlaceMatchReply] """
        pass

    def parentCategoryId(self, categoryId, p_str=None): # real signature unknown; restored from __doc__
        """ parentCategoryId(self, categoryId: Optional[str]) -> str """
        return ""

    def placeAdded(self, *args, **kwargs): # real signature unknown
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

    def placeRemoved(self, *args, **kwargs): # real signature unknown
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

    def placeUpdated(self, *args, **kwargs): # real signature unknown
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

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def removeCategory(self, categoryId, p_str=None): # real signature unknown; restored from __doc__
        """ removeCategory(self, categoryId: Optional[str]) -> Optional[QPlaceIdReply] """
        pass

    def removePlace(self, placeId, p_str=None): # real signature unknown; restored from __doc__
        """ removePlace(self, placeId: Optional[str]) -> Optional[QPlaceIdReply] """
        pass

    def saveCategory(self, category, parentId, p_str=None): # real signature unknown; restored from __doc__
        """ saveCategory(self, category: QPlaceCategory, parentId: Optional[str]) -> Optional[QPlaceIdReply] """
        pass

    def savePlace(self, place): # real signature unknown; restored from __doc__
        """ savePlace(self, place: QPlace) -> Optional[QPlaceIdReply] """
        pass

    def search(self, request): # real signature unknown; restored from __doc__
        """ search(self, request: QPlaceSearchRequest) -> Optional[QPlaceSearchReply] """
        pass

    def searchSuggestions(self, request): # real signature unknown; restored from __doc__
        """ searchSuggestions(self, request: QPlaceSearchRequest) -> Optional[QPlaceSearchSuggestionReply] """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setLocales(self, locales, QLocale=None): # real signature unknown; restored from __doc__
        """ setLocales(self, locales: Iterable[QLocale]) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parameters, p_str=None, Any=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass


