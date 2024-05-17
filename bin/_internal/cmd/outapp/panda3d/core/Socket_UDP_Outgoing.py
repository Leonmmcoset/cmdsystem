# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .Socket_IP import Socket_IP

class Socket_UDP_Outgoing(Socket_IP):
    """
    /**
     * Base functionality for a UDP sending socket
     */
    """
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

    def InitNoAddress(self, const_Socket_UDP_Outgoing_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        InitNoAddress(const Socket_UDP_Outgoing self)
        
        // use this interface for a none tagreted UDP connection
        
        /**
         * This will set a udp up for targeted sends.
         */
        """
        pass

    def InitToAddress(self, const_Socket_UDP_Outgoing_self, const_Socket_Address_address): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        InitToAddress(const Socket_UDP_Outgoing self, const Socket_Address address)
        
        // use this interface for a tagreted UDP connection
        
        /**
         * Connects the Socket to a specified address
         */
        """
        pass

    def Send(self, const_Socket_UDP_Outgoing_self, str_data): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        Send(const Socket_UDP_Outgoing self, str data)
        
        /**
         * Send data to connected address
         */
        
        /**
         * Send data to connected address
         */
        """
        pass

    def SendTo(self, const_Socket_UDP_Outgoing_self, str_data, const_Socket_Address_address): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        SendTo(const Socket_UDP_Outgoing self, str data, const Socket_Address address)
        
        /**
         * Send data to specified address
         */
        
        /**
         * Send data to specified address
         */
        """
        pass

    def SetToBroadCast(self, const_Socket_UDP_Outgoing_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        SetToBroadCast(const Socket_UDP_Outgoing self)
        
        /**
         * Ask the OS to let us receive broadcast packets on this port.
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
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        'InitNoAddress': None, # (!) real value is "<method 'InitNoAddress' of 'panda3d.core.Socket_UDP_Outgoing' objects>"
        'InitToAddress': None, # (!) real value is "<method 'InitToAddress' of 'panda3d.core.Socket_UDP_Outgoing' objects>"
        'Send': None, # (!) real value is "<method 'Send' of 'panda3d.core.Socket_UDP_Outgoing' objects>"
        'SendTo': None, # (!) real value is "<method 'SendTo' of 'panda3d.core.Socket_UDP_Outgoing' objects>"
        'SetToBroadCast': None, # (!) real value is "<method 'SetToBroadCast' of 'panda3d.core.Socket_UDP_Outgoing' objects>"
        '__doc__': '/**\n * Base functionality for a UDP sending socket\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.Socket_UDP_Outgoing' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE38EBD0>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE38EBD0>)>'
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE38EBD0>)>'
    }


