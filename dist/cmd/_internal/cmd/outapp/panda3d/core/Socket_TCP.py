# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .Socket_IP import Socket_IP

class Socket_TCP(Socket_IP):
    """
    /**
     * Base functionality for a TCP connected socket This class is pretty useless
     * by itself but it does hide some of the platform differences from machine to
     * machine
     */
    """
    def ActiveOpen(self, const_Socket_TCP_self, const_Socket_Address_theaddress, bool_setdelay): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        ActiveOpen(const Socket_TCP self, const Socket_Address theaddress, bool setdelay)
        
        // inline bool ActiveOpen(const Socket_Address &theaddress);
        
        /**
         * This function will try and set the socket up for active open to a specified
         * address and port provided by the input parameter
         */
        """
        pass

    def ActiveOpenNonBlocking(self, const_Socket_TCP_self, const_Socket_Address_theaddress): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        ActiveOpenNonBlocking(const Socket_TCP self, const Socket_Address theaddress)
        
        /**
         * This function will try and set the socket up for active open to a specified
         * address and port provided by the input parameter (non-blocking version)
         */
        """
        pass

    def DontLinger(self, const_Socket_TCP_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        DontLinger(const Socket_TCP self)
        
        /**
         * Turn off the linger flag.  The socket will quickly release buffered items
         * and free up OS resources.  You may lose a stream if you use this flag and
         * do not negotiate the close at the application layer.
         */
        """
        pass

    def ErrorIsWouldBlocking(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        ErrorIs_WouldBlocking(const Socket_TCP self, int err)
        """
        pass

    def ErrorIs_WouldBlocking(self, const_Socket_TCP_self, int_err): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        ErrorIs_WouldBlocking(const Socket_TCP self, int err)
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def RecvData(self, const_Socket_TCP_self, int_max_len): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        RecvData(const Socket_TCP self, int max_len)
        
        /**
         * Read the data from the connection - if error 0 if socket closed for read or
         * length is 0 + bytes read ( May be smaller than requested)
         */
        
        /**
         * Read the data from the connection - if error 0 if socket closed for read or
         * length is 0 + bytes read (May be smaller than requested)
         */
        """
        pass

    def SendData(self, const_Socket_TCP_self, str_str): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        SendData(const Socket_TCP self, str str)
        
        /**
         * Ok Lets Send the Data - if error 0 if socket closed for write or lengh is 0
         * + bytes writen ( May be smaller than requested)
         */
        """
        pass

    def SetLinger(self, const_Socket_TCP_self, int_interval_seconds): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        SetLinger(const Socket_TCP self, int interval_seconds)
        
        /**
         * will control the behavior of SO_LINGER for a TCP socket
         */
        """
        pass

    def SetNoDelay(self, const_Socket_TCP_self, bool_flag): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        SetNoDelay(const Socket_TCP self, bool flag)
        
        /**
         * Disable Nagle algorithm.  Don't delay send to coalesce packets
         */
        """
        pass

    def SetSendBufferSize(self, const_Socket_TCP_self, int_insize): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        SetSendBufferSize(const Socket_TCP self, int insize)
        
        /**
         * Just like it sounds.  Sets a buffered socket recv buffer size.  This
         * function does not refuse ranges outside hard-coded OS limits
         */
        """
        pass

    def ShutdownSend(self, const_Socket_TCP_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        ShutdownSend(const Socket_TCP self)
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    DtoolClassDict = {
        'ActiveOpen': None, # (!) real value is "<method 'ActiveOpen' of 'panda3d.core.Socket_TCP' objects>"
        'ActiveOpenNonBlocking': None, # (!) real value is "<method 'ActiveOpenNonBlocking' of 'panda3d.core.Socket_TCP' objects>"
        'DontLinger': None, # (!) real value is "<method 'DontLinger' of 'panda3d.core.Socket_TCP' objects>"
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        'ErrorIsWouldBlocking': None, # (!) real value is "<method 'ErrorIsWouldBlocking' of 'panda3d.core.Socket_TCP' objects>"
        'ErrorIs_WouldBlocking': None, # (!) real value is "<method 'ErrorIs_WouldBlocking' of 'panda3d.core.Socket_TCP' objects>"
        'RecvData': None, # (!) real value is "<method 'RecvData' of 'panda3d.core.Socket_TCP' objects>"
        'SendData': None, # (!) real value is "<method 'SendData' of 'panda3d.core.Socket_TCP' objects>"
        'SetLinger': None, # (!) real value is "<method 'SetLinger' of 'panda3d.core.Socket_TCP' objects>"
        'SetNoDelay': None, # (!) real value is "<method 'SetNoDelay' of 'panda3d.core.Socket_TCP' objects>"
        'SetSendBufferSize': None, # (!) real value is "<method 'SetSendBufferSize' of 'panda3d.core.Socket_TCP' objects>"
        'ShutdownSend': None, # (!) real value is "<method 'ShutdownSend' of 'panda3d.core.Socket_TCP' objects>"
        '__doc__': '/**\n * Base functionality for a TCP connected socket This class is pretty useless\n * by itself but it does hide some of the platform differences from machine to\n * machine\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.Socket_TCP' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE38E660>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE38E660>)>'
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE38E660>)>'
    }


