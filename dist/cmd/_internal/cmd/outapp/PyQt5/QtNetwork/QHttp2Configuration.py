# encoding: utf-8
# module PyQt5.QtNetwork
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtNetwork.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QHttp2Configuration(__sip.simplewrapper):
    """
    QHttp2Configuration()
    QHttp2Configuration(other: QHttp2Configuration)
    """
    def huffmanCompressionEnabled(self): # real signature unknown; restored from __doc__
        """ huffmanCompressionEnabled(self) -> bool """
        return False

    def maxFrameSize(self): # real signature unknown; restored from __doc__
        """ maxFrameSize(self) -> int """
        return 0

    def serverPushEnabled(self): # real signature unknown; restored from __doc__
        """ serverPushEnabled(self) -> bool """
        return False

    def sessionReceiveWindowSize(self): # real signature unknown; restored from __doc__
        """ sessionReceiveWindowSize(self) -> int """
        return 0

    def setHuffmanCompressionEnabled(self, enable): # real signature unknown; restored from __doc__
        """ setHuffmanCompressionEnabled(self, enable: bool) """
        pass

    def setMaxFrameSize(self, size): # real signature unknown; restored from __doc__
        """ setMaxFrameSize(self, size: int) -> bool """
        return False

    def setServerPushEnabled(self, enable): # real signature unknown; restored from __doc__
        """ setServerPushEnabled(self, enable: bool) """
        pass

    def setSessionReceiveWindowSize(self, size): # real signature unknown; restored from __doc__
        """ setSessionReceiveWindowSize(self, size: int) -> bool """
        return False

    def setStreamReceiveWindowSize(self, size): # real signature unknown; restored from __doc__
        """ setStreamReceiveWindowSize(self, size: int) -> bool """
        return False

    def streamReceiveWindowSize(self): # real signature unknown; restored from __doc__
        """ streamReceiveWindowSize(self) -> int """
        return 0

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: QHttp2Configuration) """
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


