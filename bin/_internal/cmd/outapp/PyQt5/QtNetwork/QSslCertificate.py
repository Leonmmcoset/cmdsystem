# encoding: utf-8
# module PyQt5.QtNetwork
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtNetwork.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QSslCertificate(__sip.simplewrapper):
    """
    QSslCertificate(device: Optional[QIODevice], format: QSsl.EncodingFormat = QSsl.Pem)
    QSslCertificate(data: Union[QByteArray, bytes, bytearray] = QByteArray(), format: QSsl.EncodingFormat = QSsl.Pem)
    QSslCertificate(other: QSslCertificate)
    """
    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def digest(self, algorithm=None): # real signature unknown; restored from __doc__
        """ digest(self, algorithm: QCryptographicHash.Algorithm = QCryptographicHash.Md5) -> QByteArray """
        pass

    def effectiveDate(self): # real signature unknown; restored from __doc__
        """ effectiveDate(self) -> QDateTime """
        pass

    def expiryDate(self): # real signature unknown; restored from __doc__
        """ expiryDate(self) -> QDateTime """
        pass

    def extensions(self): # real signature unknown; restored from __doc__
        """ extensions(self) -> List[QSslCertificateExtension] """
        return []

    def fromData(self, data, QByteArray=None, bytes=None, bytearray=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ fromData(data: Union[QByteArray, bytes, bytearray], format: QSsl.EncodingFormat = QSsl.Pem) -> List[QSslCertificate] """
        pass

    def fromDevice(self, device, QIODevice=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ fromDevice(device: Optional[QIODevice], format: QSsl.EncodingFormat = QSsl.Pem) -> List[QSslCertificate] """
        pass

    def fromPath(self, path, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ fromPath(path: Optional[str], format: QSsl.EncodingFormat = QSsl.Pem, syntax: QRegExp.PatternSyntax = QRegExp.FixedString) -> List[QSslCertificate] """
        pass

    def handle(self): # real signature unknown; restored from __doc__
        """ handle(self) -> Optional[PyQt5.sip.voidptr] """
        pass

    def importPkcs12(self, device, QIODevice=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ importPkcs12(device: Optional[QIODevice], key: Optional[QSslKey], certificate: Optional[QSslCertificate], caCertificates: Optional[Iterable[QSslCertificate]] = [], passPhrase: Union[QByteArray, bytes, bytearray] = QByteArray()) -> bool """
        pass

    def isBlacklisted(self): # real signature unknown; restored from __doc__
        """ isBlacklisted(self) -> bool """
        return False

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def isSelfSigned(self): # real signature unknown; restored from __doc__
        """ isSelfSigned(self) -> bool """
        return False

    def issuerDisplayName(self): # real signature unknown; restored from __doc__
        """ issuerDisplayName(self) -> str """
        return ""

    def issuerInfo(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        issuerInfo(self, info: QSslCertificate.SubjectInfo) -> List[str]
        issuerInfo(self, attribute: Union[QByteArray, bytes, bytearray]) -> List[str]
        """
        return []

    def issuerInfoAttributes(self): # real signature unknown; restored from __doc__
        """ issuerInfoAttributes(self) -> List[QByteArray] """
        return []

    def publicKey(self): # real signature unknown; restored from __doc__
        """ publicKey(self) -> QSslKey """
        return QSslKey

    def serialNumber(self): # real signature unknown; restored from __doc__
        """ serialNumber(self) -> QByteArray """
        pass

    def subjectAlternativeNames(self): # real signature unknown; restored from __doc__
        """ subjectAlternativeNames(self) -> Dict[QSsl.AlternativeNameEntryType, List[str]] """
        return {}

    def subjectDisplayName(self): # real signature unknown; restored from __doc__
        """ subjectDisplayName(self) -> str """
        return ""

    def subjectInfo(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        subjectInfo(self, info: QSslCertificate.SubjectInfo) -> List[str]
        subjectInfo(self, attribute: Union[QByteArray, bytes, bytearray]) -> List[str]
        """
        return []

    def subjectInfoAttributes(self): # real signature unknown; restored from __doc__
        """ subjectInfoAttributes(self) -> List[QByteArray] """
        return []

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: QSslCertificate) """
        pass

    def toDer(self): # real signature unknown; restored from __doc__
        """ toDer(self) -> QByteArray """
        pass

    def toPem(self): # real signature unknown; restored from __doc__
        """ toPem(self) -> QByteArray """
        pass

    def toText(self): # real signature unknown; restored from __doc__
        """ toText(self) -> str """
        return ""

    def verify(self, certificateChain, QSslCertificate=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ verify(certificateChain: Iterable[QSslCertificate], hostName: Optional[str] = '') -> List[QSslError] """
        pass

    def version(self): # real signature unknown; restored from __doc__
        """ version(self) -> QByteArray """
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


    CommonName = 1
    CountryName = 4
    DistinguishedNameQualifier = 6
    EmailAddress = 8
    LocalityName = 2
    Organization = 0
    OrganizationalUnitName = 3
    SerialNumber = 7
    StateOrProvinceName = 5


