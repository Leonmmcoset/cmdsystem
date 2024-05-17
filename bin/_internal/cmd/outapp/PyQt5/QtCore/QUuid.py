# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


class QUuid(__sip.simplewrapper):
    """
    QUuid()
    QUuid(l: int, w1: int, w2: int, b1: int, b2: int, b3: int, b4: int, b5: int, b6: int, b7: int, b8: int)
    QUuid(a0: Optional[str])
    QUuid(a0: Union[QByteArray, bytes, bytearray])
    QUuid(a0: QUuid)
    """
    def createUuid(self): # real signature unknown; restored from __doc__
        """ createUuid() -> QUuid """
        return QUuid

    def createUuidV3(self, ns, baseData, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        createUuidV3(ns: QUuid, baseData: Union[QByteArray, bytes, bytearray]) -> QUuid
        createUuidV3(ns: QUuid, baseData: Optional[str]) -> QUuid
        """
        return QUuid

    def createUuidV5(self, ns, baseData, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        createUuidV5(ns: QUuid, baseData: Union[QByteArray, bytes, bytearray]) -> QUuid
        createUuidV5(ns: QUuid, baseData: Optional[str]) -> QUuid
        """
        return QUuid

    def fromRfc4122(self, a0, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ fromRfc4122(a0: Union[QByteArray, bytes, bytearray]) -> QUuid """
        return QUuid

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def toByteArray(self, mode=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        toByteArray(self) -> QByteArray
        toByteArray(self, mode: QUuid.StringFormat) -> QByteArray
        """
        return QByteArray

    def toRfc4122(self): # real signature unknown; restored from __doc__
        """ toRfc4122(self) -> QByteArray """
        return QByteArray

    def toString(self, mode=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        toString(self) -> str
        toString(self, mode: QUuid.StringFormat) -> str
        """
        return ""

    def variant(self): # real signature unknown; restored from __doc__
        """ variant(self) -> QUuid.Variant """
        pass

    def version(self): # real signature unknown; restored from __doc__
        """ version(self) -> QUuid.Version """
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

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    DCE = 2
    EmbeddedPOSIX = 2
    Id128 = 3
    Md5 = 3
    Microsoft = 6
    Name = 3
    NCS = 0
    Random = 4
    Reserved = 7
    Sha1 = 5
    Time = 1
    VarUnknown = -1
    VerUnknown = -1
    WithBraces = 0
    WithoutBraces = 1


