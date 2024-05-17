# encoding: utf-8
# module PyQt5.QtLocation
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtLocation.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QPlaceManager(__PyQt5_QtCore.QObject):
    # no doc
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

    def childCategories(self, parentId, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ childCategories(self, parentId: Optional[str] = '') -> List[QPlaceCategory] """
        pass

    def childCategoryIds(self, parentId, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ childCategoryIds(self, parentId: Optional[str] = '') -> List[str] """
        pass

    def compatiblePlace(self, place): # real signature unknown; restored from __doc__
        """ compatiblePlace(self, place: QPlace) -> QPlace """
        return QPlace

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

    def locales(self): # real signature unknown; restored from __doc__
        """ locales(self) -> List[QLocale] """
        return []

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

    def removeCategory(self, categoryId, p_str=None): # real signature unknown; restored from __doc__
        """ removeCategory(self, categoryId: Optional[str]) -> Optional[QPlaceIdReply] """
        pass

    def removePlace(self, placeId, p_str=None): # real signature unknown; restored from __doc__
        """ removePlace(self, placeId: Optional[str]) -> Optional[QPlaceIdReply] """
        pass

    def saveCategory(self, category, parentId, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ saveCategory(self, category: QPlaceCategory, parentId: Optional[str] = '') -> Optional[QPlaceIdReply] """
        pass

    def savePlace(self, place): # real signature unknown; restored from __doc__
        """ savePlace(self, place: QPlace) -> Optional[QPlaceIdReply] """
        pass

    def search(self, query): # real signature unknown; restored from __doc__
        """ search(self, query: QPlaceSearchRequest) -> Optional[QPlaceSearchReply] """
        pass

    def searchSuggestions(self, request): # real signature unknown; restored from __doc__
        """ searchSuggestions(self, request: QPlaceSearchRequest) -> Optional[QPlaceSearchSuggestionReply] """
        pass

    def setLocale(self, locale): # real signature unknown; restored from __doc__
        """ setLocale(self, locale: QLocale) """
        pass

    def setLocales(self, locale, QLocale=None): # real signature unknown; restored from __doc__
        """ setLocales(self, locale: Iterable[QLocale]) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass


