# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .TypedObject import TypedObject

class Socket_IP(TypedObject):
    """
    /**
     * Base functionality for a INET domain Socket This call should be the
     * starting point for all other unix domain sockets.
     *
     * SocketIP |
     * ------------------------------------------------------------------- |
     * |                       |                           | SocketTCP
     * SocketTCP_Listen    SocketUDP_Incoming   SocketUDP_OutBound
     *
     */
    """
    def Active(self, const_Socket_IP_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        Active(const Socket_IP self)
        
        /**
         * Ask if the socket is open (allocated)
         */
        """
        pass

    def Close(self, const_Socket_IP_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        Close(const Socket_IP self)
        
        /**
         * Closes a socket if it is open (allocated).
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def GetLastError(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        GetLastError()
        
        /**
         * Gets the last errcode from a socket operation.
         */
        """
        pass

    def GetPeerName(self, Socket_IP_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        GetPeerName(Socket_IP self)
        
        /**
         * Wrapper on berkly getpeername...
         */
        """
        pass

    def GetSocket(self, const_Socket_IP_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        GetSocket(const Socket_IP self)
        GetSocket(Socket_IP self)
        
        /**
         * Gets the base socket type
         */
        
        /**
         * Get The RAW file id of the socket
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def InitNetworkDriver(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        InitNetworkDriver()
        """
        pass

    def SetBlocking(self, const_Socket_IP_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        SetBlocking(const Socket_IP self)
        
        /**
         * Set the socket to block on subsequent calls to socket functions that
         * address this socket
         */
        """
        pass

    def SetNonBlocking(self, const_Socket_IP_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        SetNonBlocking(const Socket_IP self)
        
        /**
         * this function will throw a socket into non-blocking mode
         */
        """
        pass

    def SetRecvBufferSize(self, const_Socket_IP_self, int_size): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        SetRecvBufferSize(const Socket_IP self, int size)
        
        /**
         * Ok it sets the recv buffer size for both tcp and UDP
         */
        """
        pass

    def SetReuseAddress(self, const_Socket_IP_self, bool_flag): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        SetReuseAddress(const Socket_IP self, bool flag)
        
        /**
         * Informs a socket to reuse IP address as needed
         */
        """
        pass

    def SetSocket(self, const_Socket_IP_self, int_ins): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        SetSocket(const Socket_IP self, int ins)
        
        /**
         * Assigns an existing socket to this class
         */
        """
        pass

    def SetV6Only(self, const_Socket_IP_self, bool_flag): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        SetV6Only(const Socket_IP self, bool flag)
        
        /**
         * Sets a flag indicating whether this IPv6 socket should operate in
         * dual-stack mode or not.
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    DtoolClassDict = {
        'Active': None, # (!) real value is "<method 'Active' of 'panda3d.core.Socket_IP' objects>"
        'Close': None, # (!) real value is "<method 'Close' of 'panda3d.core.Socket_IP' objects>"
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        'GetLastError': None, # (!) real value is '<staticmethod(<built-in method GetLastError of type object at 0x00007FFCFE38E490>)>'
        'GetPeerName': None, # (!) real value is "<method 'GetPeerName' of 'panda3d.core.Socket_IP' objects>"
        'GetSocket': None, # (!) real value is "<method 'GetSocket' of 'panda3d.core.Socket_IP' objects>"
        'InitNetworkDriver': None, # (!) real value is '<staticmethod(<built-in method InitNetworkDriver of type object at 0x00007FFCFE38E490>)>'
        'SetBlocking': None, # (!) real value is "<method 'SetBlocking' of 'panda3d.core.Socket_IP' objects>"
        'SetNonBlocking': None, # (!) real value is "<method 'SetNonBlocking' of 'panda3d.core.Socket_IP' objects>"
        'SetRecvBufferSize': None, # (!) real value is "<method 'SetRecvBufferSize' of 'panda3d.core.Socket_IP' objects>"
        'SetReuseAddress': None, # (!) real value is "<method 'SetReuseAddress' of 'panda3d.core.Socket_IP' objects>"
        'SetSocket': None, # (!) real value is "<method 'SetSocket' of 'panda3d.core.Socket_IP' objects>"
        'SetV6Only': None, # (!) real value is "<method 'SetV6Only' of 'panda3d.core.Socket_IP' objects>"
        '__doc__': '/**\n * Base functionality for a INET domain Socket This call should be the\n * starting point for all other unix domain sockets.\n *\n * SocketIP |\n * ------------------------------------------------------------------- |\n * |                       |                           | SocketTCP\n * SocketTCP_Listen    SocketUDP_Incoming   SocketUDP_OutBound\n *\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.Socket_IP' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE38E490>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE38E490>)>'
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE38E490>)>'
    }


