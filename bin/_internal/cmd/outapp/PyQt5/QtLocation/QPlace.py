# encoding: utf-8
# module PyQt5.QtLocation
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtLocation.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QPlace(__sip.simplewrapper):
    """
    QPlace()
    QPlace(other: QPlace)
    """
    def appendContactDetail(self, contactType, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ appendContactDetail(self, contactType: Optional[str], detail: QPlaceContactDetail) """
        pass

    def attribution(self): # real signature unknown; restored from __doc__
        """ attribution(self) -> str """
        return ""

    def categories(self): # real signature unknown; restored from __doc__
        """ categories(self) -> List[QPlaceCategory] """
        return []

    def contactDetails(self, contactType, p_str=None): # real signature unknown; restored from __doc__
        """ contactDetails(self, contactType: Optional[str]) -> List[QPlaceContactDetail] """
        return []

    def contactTypes(self): # real signature unknown; restored from __doc__
        """ contactTypes(self) -> List[str] """
        return []

    def content(self, type): # real signature unknown; restored from __doc__
        """ content(self, type: QPlaceContent.Type) -> Dict[int, QPlaceContent] """
        return {}

    def detailsFetched(self): # real signature unknown; restored from __doc__
        """ detailsFetched(self) -> bool """
        return False

    def extendedAttribute(self, attributeType, p_str=None): # real signature unknown; restored from __doc__
        """ extendedAttribute(self, attributeType: Optional[str]) -> QPlaceAttribute """
        return QPlaceAttribute

    def extendedAttributeTypes(self): # real signature unknown; restored from __doc__
        """ extendedAttributeTypes(self) -> List[str] """
        return []

    def icon(self): # real signature unknown; restored from __doc__
        """ icon(self) -> QPlaceIcon """
        return QPlaceIcon

    def insertContent(self, type, content, p_int=None, QPlaceContent=None): # real signature unknown; restored from __doc__
        """ insertContent(self, type: QPlaceContent.Type, content: Dict[int, QPlaceContent]) """
        pass

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ isEmpty(self) -> bool """
        return False

    def location(self): # real signature unknown; restored from __doc__
        """ location(self) -> QGeoLocation """
        pass

    def name(self): # real signature unknown; restored from __doc__
        """ name(self) -> str """
        return ""

    def placeId(self): # real signature unknown; restored from __doc__
        """ placeId(self) -> str """
        return ""

    def primaryEmail(self): # real signature unknown; restored from __doc__
        """ primaryEmail(self) -> str """
        return ""

    def primaryFax(self): # real signature unknown; restored from __doc__
        """ primaryFax(self) -> str """
        return ""

    def primaryPhone(self): # real signature unknown; restored from __doc__
        """ primaryPhone(self) -> str """
        return ""

    def primaryWebsite(self): # real signature unknown; restored from __doc__
        """ primaryWebsite(self) -> QUrl """
        pass

    def ratings(self): # real signature unknown; restored from __doc__
        """ ratings(self) -> QPlaceRatings """
        return QPlaceRatings

    def removeContactDetails(self, contactType, p_str=None): # real signature unknown; restored from __doc__
        """ removeContactDetails(self, contactType: Optional[str]) """
        pass

    def removeExtendedAttribute(self, attributeType, p_str=None): # real signature unknown; restored from __doc__
        """ removeExtendedAttribute(self, attributeType: Optional[str]) """
        pass

    def setAttribution(self, attribution, p_str=None): # real signature unknown; restored from __doc__
        """ setAttribution(self, attribution: Optional[str]) """
        pass

    def setCategories(self, categories, QPlaceCategory=None): # real signature unknown; restored from __doc__
        """ setCategories(self, categories: Iterable[QPlaceCategory]) """
        pass

    def setCategory(self, category): # real signature unknown; restored from __doc__
        """ setCategory(self, category: QPlaceCategory) """
        pass

    def setContactDetails(self, contactType, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setContactDetails(self, contactType: Optional[str], details: Iterable[QPlaceContactDetail]) """
        pass

    def setContent(self, type, content, p_int=None, QPlaceContent=None): # real signature unknown; restored from __doc__
        """ setContent(self, type: QPlaceContent.Type, content: Dict[int, QPlaceContent]) """
        pass

    def setDetailsFetched(self, fetched): # real signature unknown; restored from __doc__
        """ setDetailsFetched(self, fetched: bool) """
        pass

    def setExtendedAttribute(self, attributeType, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setExtendedAttribute(self, attributeType: Optional[str], attribute: QPlaceAttribute) """
        pass

    def setIcon(self, icon): # real signature unknown; restored from __doc__
        """ setIcon(self, icon: QPlaceIcon) """
        pass

    def setLocation(self, location): # real signature unknown; restored from __doc__
        """ setLocation(self, location: QGeoLocation) """
        pass

    def setName(self, name, p_str=None): # real signature unknown; restored from __doc__
        """ setName(self, name: Optional[str]) """
        pass

    def setPlaceId(self, identifier, p_str=None): # real signature unknown; restored from __doc__
        """ setPlaceId(self, identifier: Optional[str]) """
        pass

    def setRatings(self, ratings): # real signature unknown; restored from __doc__
        """ setRatings(self, ratings: QPlaceRatings) """
        pass

    def setSupplier(self, supplier): # real signature unknown; restored from __doc__
        """ setSupplier(self, supplier: QPlaceSupplier) """
        pass

    def setTotalContentCount(self, type, total): # real signature unknown; restored from __doc__
        """ setTotalContentCount(self, type: QPlaceContent.Type, total: int) """
        pass

    def setVisibility(self, visibility): # real signature unknown; restored from __doc__
        """ setVisibility(self, visibility: QLocation.Visibility) """
        pass

    def supplier(self): # real signature unknown; restored from __doc__
        """ supplier(self) -> QPlaceSupplier """
        return QPlaceSupplier

    def totalContentCount(self, type): # real signature unknown; restored from __doc__
        """ totalContentCount(self, type: QPlaceContent.Type) -> int """
        return 0

    def visibility(self): # real signature unknown; restored from __doc__
        """ visibility(self) -> QLocation.Visibility """
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


