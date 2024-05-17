# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


class QJsonDocument(__sip.simplewrapper):
    """
    QJsonDocument()
    QJsonDocument(object: Dict[Optional[str], Union[QJsonValue, QJsonValue.Type, Iterable[QJsonValue], Dict[Optional[str], QJsonValue], bool, int, float, None, Optional[str]]])
    QJsonDocument(array: Iterable[Union[QJsonValue, QJsonValue.Type, Iterable[QJsonValue], Dict[Optional[str], QJsonValue], bool, int, float, None, Optional[str]]])
    QJsonDocument(other: QJsonDocument)
    """
    def array(self): # real signature unknown; restored from __doc__
        """ array(self) -> List[QJsonValue] """
        return []

    def fromBinaryData(self, data, QByteArray=None, bytes=None, bytearray=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ fromBinaryData(data: Union[QByteArray, bytes, bytearray], validation: QJsonDocument.DataValidation = QJsonDocument.Validate) -> QJsonDocument """
        pass

    def fromJson(self, json, QByteArray=None, bytes=None, bytearray=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ fromJson(json: Union[QByteArray, bytes, bytearray], error: Optional[QJsonParseError] = None) -> QJsonDocument """
        pass

    def fromRawData(self, data, bytes=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ fromRawData(data: Optional[bytes], size: int, validation: QJsonDocument.DataValidation = QJsonDocument.Validate) -> QJsonDocument """
        pass

    def fromVariant(self, variant): # real signature unknown; restored from __doc__
        """ fromVariant(variant: Any) -> QJsonDocument """
        return QJsonDocument

    def isArray(self): # real signature unknown; restored from __doc__
        """ isArray(self) -> bool """
        return False

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ isEmpty(self) -> bool """
        return False

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def isObject(self): # real signature unknown; restored from __doc__
        """ isObject(self) -> bool """
        return False

    def object(self): # real signature unknown; restored from __doc__
        """ object(self) -> Dict[str, QJsonValue] """
        return {}

    def rawData(self): # real signature unknown; restored from __doc__
        """ rawData(self) -> (Optional[bytes], Optional[int]) """
        pass

    def setArray(self, array, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setArray(self, array: Iterable[Union[QJsonValue, QJsonValue.Type, Iterable[QJsonValue], Dict[Optional[str], QJsonValue], bool, int, float, None, Optional[str]]]) """
        pass

    def setObject(self, p_object, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setObject(self, object: Dict[Optional[str], Union[QJsonValue, QJsonValue.Type, Iterable[QJsonValue], Dict[Optional[str], QJsonValue], bool, int, float, None, Optional[str]]]) """
        pass

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: QJsonDocument) """
        pass

    def toBinaryData(self): # real signature unknown; restored from __doc__
        """ toBinaryData(self) -> QByteArray """
        return QByteArray

    def toJson(self, format=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        toJson(self) -> QByteArray
        toJson(self, format: QJsonDocument.JsonFormat) -> QByteArray
        """
        return QByteArray

    def toVariant(self): # real signature unknown; restored from __doc__
        """ toVariant(self) -> Any """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
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


    BypassValidation = 1
    Compact = 1
    Indented = 0
    Validate = 0
    __hash__ = None


