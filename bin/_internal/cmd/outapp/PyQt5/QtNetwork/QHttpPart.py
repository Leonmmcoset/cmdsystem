# encoding: utf-8
# module PyQt5.QtNetwork
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtNetwork.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QHttpPart(__sip.simplewrapper):
    """
    QHttpPart()
    QHttpPart(other: QHttpPart)
    """
    def setBody(self, body, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ setBody(self, body: Union[QByteArray, bytes, bytearray]) """
        pass

    def setBodyDevice(self, device, QIODevice=None): # real signature unknown; restored from __doc__
        """ setBodyDevice(self, device: Optional[QIODevice]) """
        pass

    def setHeader(self, header, value): # real signature unknown; restored from __doc__
        """ setHeader(self, header: QNetworkRequest.KnownHeaders, value: Any) """
        pass

    def setRawHeader(self, headerName, QByteArray=None, bytes=None, bytearray=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setRawHeader(self, headerName: Union[QByteArray, bytes, bytearray], headerValue: Union[QByteArray, bytes, bytearray]) """
        pass

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: QHttpPart) """
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


