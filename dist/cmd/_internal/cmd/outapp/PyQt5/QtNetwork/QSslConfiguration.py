# encoding: utf-8
# module PyQt5.QtNetwork
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtNetwork.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QSslConfiguration(__sip.simplewrapper):
    """
    QSslConfiguration()
    QSslConfiguration(other: QSslConfiguration)
    """
    def addCaCertificate(self, certificate): # real signature unknown; restored from __doc__
        """ addCaCertificate(self, certificate: QSslCertificate) """
        pass

    def addCaCertificates(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        addCaCertificates(self, path: Optional[str], format: QSsl.EncodingFormat = QSsl.Pem, syntax: QSslCertificate.PatternSyntax = QSslCertificate.PatternSyntax.FixedString) -> bool
        addCaCertificates(self, certificates: Iterable[QSslCertificate])
        """
        pass

    def allowedNextProtocols(self): # real signature unknown; restored from __doc__
        """ allowedNextProtocols(self) -> List[QByteArray] """
        return []

    def backendConfiguration(self): # real signature unknown; restored from __doc__
        """ backendConfiguration(self) -> Dict[QByteArray, Any] """
        return {}

    def caCertificates(self): # real signature unknown; restored from __doc__
        """ caCertificates(self) -> List[QSslCertificate] """
        return []

    def ciphers(self): # real signature unknown; restored from __doc__
        """ ciphers(self) -> List[QSslCipher] """
        return []

    def defaultConfiguration(self): # real signature unknown; restored from __doc__
        """ defaultConfiguration() -> QSslConfiguration """
        return QSslConfiguration

    def diffieHellmanParameters(self): # real signature unknown; restored from __doc__
        """ diffieHellmanParameters(self) -> QSslDiffieHellmanParameters """
        return QSslDiffieHellmanParameters

    def ellipticCurves(self): # real signature unknown; restored from __doc__
        """ ellipticCurves(self) -> List[QSslEllipticCurve] """
        return []

    def ephemeralServerKey(self): # real signature unknown; restored from __doc__
        """ ephemeralServerKey(self) -> QSslKey """
        return QSslKey

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def localCertificate(self): # real signature unknown; restored from __doc__
        """ localCertificate(self) -> QSslCertificate """
        return QSslCertificate

    def localCertificateChain(self): # real signature unknown; restored from __doc__
        """ localCertificateChain(self) -> List[QSslCertificate] """
        return []

    def nextNegotiatedProtocol(self): # real signature unknown; restored from __doc__
        """ nextNegotiatedProtocol(self) -> QByteArray """
        pass

    def nextProtocolNegotiationStatus(self): # real signature unknown; restored from __doc__
        """ nextProtocolNegotiationStatus(self) -> QSslConfiguration.NextProtocolNegotiationStatus """
        pass

    def ocspStaplingEnabled(self): # real signature unknown; restored from __doc__
        """ ocspStaplingEnabled(self) -> bool """
        return False

    def peerCertificate(self): # real signature unknown; restored from __doc__
        """ peerCertificate(self) -> QSslCertificate """
        return QSslCertificate

    def peerCertificateChain(self): # real signature unknown; restored from __doc__
        """ peerCertificateChain(self) -> List[QSslCertificate] """
        return []

    def peerVerifyDepth(self): # real signature unknown; restored from __doc__
        """ peerVerifyDepth(self) -> int """
        return 0

    def peerVerifyMode(self): # real signature unknown; restored from __doc__
        """ peerVerifyMode(self) -> QSslSocket.PeerVerifyMode """
        pass

    def preSharedKeyIdentityHint(self): # real signature unknown; restored from __doc__
        """ preSharedKeyIdentityHint(self) -> QByteArray """
        pass

    def privateKey(self): # real signature unknown; restored from __doc__
        """ privateKey(self) -> QSslKey """
        return QSslKey

    def protocol(self): # real signature unknown; restored from __doc__
        """ protocol(self) -> QSsl.SslProtocol """
        pass

    def sessionCipher(self): # real signature unknown; restored from __doc__
        """ sessionCipher(self) -> QSslCipher """
        return QSslCipher

    def sessionProtocol(self): # real signature unknown; restored from __doc__
        """ sessionProtocol(self) -> QSsl.SslProtocol """
        pass

    def sessionTicket(self): # real signature unknown; restored from __doc__
        """ sessionTicket(self) -> QByteArray """
        pass

    def sessionTicketLifeTimeHint(self): # real signature unknown; restored from __doc__
        """ sessionTicketLifeTimeHint(self) -> int """
        return 0

    def setAllowedNextProtocols(self, protocols, Union=None, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ setAllowedNextProtocols(self, protocols: Iterable[Union[QByteArray, bytes, bytearray]]) """
        pass

    def setBackendConfiguration(self, backendConfiguration, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setBackendConfiguration(self, backendConfiguration: Dict[Union[QByteArray, bytes, bytearray], Any] = {}) """
        pass

    def setBackendConfigurationOption(self, name, QByteArray=None, bytes=None, bytearray=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setBackendConfigurationOption(self, name: Union[QByteArray, bytes, bytearray], value: Any) """
        pass

    def setCaCertificates(self, certificates, QSslCertificate=None): # real signature unknown; restored from __doc__
        """ setCaCertificates(self, certificates: Iterable[QSslCertificate]) """
        pass

    def setCiphers(self, ciphers, QSslCipher=None): # real signature unknown; restored from __doc__
        """ setCiphers(self, ciphers: Iterable[QSslCipher]) """
        pass

    def setDefaultConfiguration(self, configuration): # real signature unknown; restored from __doc__
        """ setDefaultConfiguration(configuration: QSslConfiguration) """
        pass

    def setDiffieHellmanParameters(self, dhparams): # real signature unknown; restored from __doc__
        """ setDiffieHellmanParameters(self, dhparams: QSslDiffieHellmanParameters) """
        pass

    def setEllipticCurves(self, curves, QSslEllipticCurve=None): # real signature unknown; restored from __doc__
        """ setEllipticCurves(self, curves: Iterable[QSslEllipticCurve]) """
        pass

    def setLocalCertificate(self, certificate): # real signature unknown; restored from __doc__
        """ setLocalCertificate(self, certificate: QSslCertificate) """
        pass

    def setLocalCertificateChain(self, localChain, QSslCertificate=None): # real signature unknown; restored from __doc__
        """ setLocalCertificateChain(self, localChain: Iterable[QSslCertificate]) """
        pass

    def setOcspStaplingEnabled(self, enable): # real signature unknown; restored from __doc__
        """ setOcspStaplingEnabled(self, enable: bool) """
        pass

    def setPeerVerifyDepth(self, depth): # real signature unknown; restored from __doc__
        """ setPeerVerifyDepth(self, depth: int) """
        pass

    def setPeerVerifyMode(self, mode): # real signature unknown; restored from __doc__
        """ setPeerVerifyMode(self, mode: QSslSocket.PeerVerifyMode) """
        pass

    def setPreSharedKeyIdentityHint(self, hint, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ setPreSharedKeyIdentityHint(self, hint: Union[QByteArray, bytes, bytearray]) """
        pass

    def setPrivateKey(self, key): # real signature unknown; restored from __doc__
        """ setPrivateKey(self, key: QSslKey) """
        pass

    def setProtocol(self, protocol): # real signature unknown; restored from __doc__
        """ setProtocol(self, protocol: QSsl.SslProtocol) """
        pass

    def setSessionTicket(self, sessionTicket, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ setSessionTicket(self, sessionTicket: Union[QByteArray, bytes, bytearray]) """
        pass

    def setSslOption(self, option, on): # real signature unknown; restored from __doc__
        """ setSslOption(self, option: QSsl.SslOption, on: bool) """
        pass

    def supportedCiphers(self): # real signature unknown; restored from __doc__
        """ supportedCiphers() -> List[QSslCipher] """
        return []

    def supportedEllipticCurves(self): # real signature unknown; restored from __doc__
        """ supportedEllipticCurves() -> List[QSslEllipticCurve] """
        return []

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: QSslConfiguration) """
        pass

    def systemCaCertificates(self): # real signature unknown; restored from __doc__
        """ systemCaCertificates() -> List[QSslCertificate] """
        return []

    def testSslOption(self, option): # real signature unknown; restored from __doc__
        """ testSslOption(self, option: QSsl.SslOption) -> bool """
        return False

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


    NextProtocolHttp1_1 = b'http/1.1'
    NextProtocolNegotiationNegotiated = 1
    NextProtocolNegotiationNone = 0
    NextProtocolNegotiationUnsupported = 2
    NextProtocolSpdy3_0 = b'spdy/3'
    __hash__ = None


