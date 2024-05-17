# encoding: utf-8
# module PyQt5.QtLocation
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtLocation.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QPlaceContent(__sip.simplewrapper):
    """
    QPlaceContent()
    QPlaceContent(other: QPlaceContent)
    """
    def attribution(self): # real signature unknown; restored from __doc__
        """ attribution(self) -> str """
        return ""

    def setAttribution(self, attribution, p_str=None): # real signature unknown; restored from __doc__
        """ setAttribution(self, attribution: Optional[str]) """
        pass

    def setSupplier(self, supplier): # real signature unknown; restored from __doc__
        """ setSupplier(self, supplier: QPlaceSupplier) """
        pass

    def setUser(self, user): # real signature unknown; restored from __doc__
        """ setUser(self, user: QPlaceUser) """
        pass

    def supplier(self): # real signature unknown; restored from __doc__
        """ supplier(self) -> QPlaceSupplier """
        return QPlaceSupplier

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> QPlaceContent.Type """
        pass

    def user(self): # real signature unknown; restored from __doc__
        """ user(self) -> QPlaceUser """
        return QPlaceUser

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


    CustomType = 256
    EditorialType = 3
    ImageType = 1
    NoType = 0
    ReviewType = 2
    __hash__ = None


