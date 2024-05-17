# encoding: utf-8
# module PyQt5.QtNetwork
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtNetwork.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QSslDiffieHellmanParameters(__sip.simplewrapper):
    """
    QSslDiffieHellmanParameters()
    QSslDiffieHellmanParameters(other: QSslDiffieHellmanParameters)
    """
    def defaultParameters(self): # real signature unknown; restored from __doc__
        """ defaultParameters() -> QSslDiffieHellmanParameters """
        return QSslDiffieHellmanParameters

    def error(self): # real signature unknown; restored from __doc__
        """ error(self) -> QSslDiffieHellmanParameters.Error """
        pass

    def errorString(self): # real signature unknown; restored from __doc__
        """ errorString(self) -> str """
        return ""

    def fromEncoded(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        fromEncoded(encoded: Union[QByteArray, bytes, bytearray], encoding: QSsl.EncodingFormat = QSsl.EncodingFormat.Pem) -> QSslDiffieHellmanParameters
        fromEncoded(device: Optional[QIODevice], encoding: QSsl.EncodingFormat = QSsl.EncodingFormat.Pem) -> QSslDiffieHellmanParameters
        """
        pass

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ isEmpty(self) -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: QSslDiffieHellmanParameters) """
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


    InvalidInputDataError = 1
    NoError = 0
    UnsafeParametersError = 2


