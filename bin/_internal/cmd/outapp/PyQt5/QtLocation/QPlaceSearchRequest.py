# encoding: utf-8
# module PyQt5.QtLocation
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtLocation.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QPlaceSearchRequest(__sip.simplewrapper):
    """
    QPlaceSearchRequest()
    QPlaceSearchRequest(other: QPlaceSearchRequest)
    """
    def categories(self): # real signature unknown; restored from __doc__
        """ categories(self) -> List[QPlaceCategory] """
        return []

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def limit(self): # real signature unknown; restored from __doc__
        """ limit(self) -> int """
        return 0

    def recommendationId(self): # real signature unknown; restored from __doc__
        """ recommendationId(self) -> str """
        return ""

    def relevanceHint(self): # real signature unknown; restored from __doc__
        """ relevanceHint(self) -> QPlaceSearchRequest.RelevanceHint """
        pass

    def searchArea(self): # real signature unknown; restored from __doc__
        """ searchArea(self) -> QGeoShape """
        pass

    def searchContext(self): # real signature unknown; restored from __doc__
        """ searchContext(self) -> Any """
        pass

    def searchTerm(self): # real signature unknown; restored from __doc__
        """ searchTerm(self) -> str """
        return ""

    def setCategories(self, categories, QPlaceCategory=None): # real signature unknown; restored from __doc__
        """ setCategories(self, categories: Iterable[QPlaceCategory]) """
        pass

    def setCategory(self, category): # real signature unknown; restored from __doc__
        """ setCategory(self, category: QPlaceCategory) """
        pass

    def setLimit(self, limit): # real signature unknown; restored from __doc__
        """ setLimit(self, limit: int) """
        pass

    def setRecommendationId(self, recommendationId, p_str=None): # real signature unknown; restored from __doc__
        """ setRecommendationId(self, recommendationId: Optional[str]) """
        pass

    def setRelevanceHint(self, hint): # real signature unknown; restored from __doc__
        """ setRelevanceHint(self, hint: QPlaceSearchRequest.RelevanceHint) """
        pass

    def setSearchArea(self, area): # real signature unknown; restored from __doc__
        """ setSearchArea(self, area: QGeoShape) """
        pass

    def setSearchContext(self, context): # real signature unknown; restored from __doc__
        """ setSearchContext(self, context: Any) """
        pass

    def setSearchTerm(self, term, p_str=None): # real signature unknown; restored from __doc__
        """ setSearchTerm(self, term: Optional[str]) """
        pass

    def setVisibilityScope(self, visibilityScopes, QLocation_VisibilityScope=None, QLocation_Visibility=None): # real signature unknown; restored from __doc__
        """ setVisibilityScope(self, visibilityScopes: Union[QLocation.VisibilityScope, QLocation.Visibility]) """
        pass

    def visibilityScope(self): # real signature unknown; restored from __doc__
        """ visibilityScope(self) -> QLocation.VisibilityScope """
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


    DistanceHint = 1
    LexicalPlaceNameHint = 2
    UnspecifiedHint = 0
    __hash__ = None


