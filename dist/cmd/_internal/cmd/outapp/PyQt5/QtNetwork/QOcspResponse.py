# encoding: utf-8
# module PyQt5.QtNetwork
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtNetwork.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QOcspResponse(__sip.simplewrapper):
    """
    QOcspResponse()
    QOcspResponse(other: QOcspResponse)
    """
    def certificateStatus(self): # real signature unknown; restored from __doc__
        """ certificateStatus(self) -> QOcspCertificateStatus """
        return QOcspCertificateStatus

    def responder(self): # real signature unknown; restored from __doc__
        """ responder(self) -> QSslCertificate """
        return QSslCertificate

    def revocationReason(self): # real signature unknown; restored from __doc__
        """ revocationReason(self) -> QOcspRevocationReason """
        return QOcspRevocationReason

    def subject(self): # real signature unknown; restored from __doc__
        """ subject(self) -> QSslCertificate """
        return QSslCertificate

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: QOcspResponse) """
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



