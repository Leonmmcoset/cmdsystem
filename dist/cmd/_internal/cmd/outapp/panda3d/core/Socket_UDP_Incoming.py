# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .Socket_IP import Socket_IP

class Socket_UDP_Incoming(Socket_IP):
    """
    /**
     * Base functionality for a UDP Reader
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

    def InitNoAddress(self, const_Socket_UDP_Incoming_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        InitNoAddress(const Socket_UDP_Incoming self)
        
        /**
         * Set this socket to work without a bound external address.
         */
        """
        pass

    def OpenForInput(self, const_Socket_UDP_Incoming_self, const_Socket_Address_address): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        OpenForInput(const Socket_UDP_Incoming self, const Socket_Address address)
        OpenForInput(const Socket_UDP_Incoming self, int port)
        
        /**
         * Starts a UDP socket listening on a port
         */
        
        /**
         * Starts a UDP socket listening on a port
         */
        """
        pass

    def OpenForInputMCast(self, const_Socket_UDP_Incoming_self, const_Socket_Address_address): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        OpenForInputMCast(const Socket_UDP_Incoming self, const Socket_Address address)
        
        /**
         * Starts a UDP socket listening on a port
         */
        """
        pass

    def SendTo(self, const_Socket_UDP_Incoming_self, str_data, int_len, const_Socket_Address_address): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        SendTo(const Socket_UDP_Incoming self, str data, int len, const Socket_Address address)
        
        /**
         * Send data to specified address
         */
        """
        pass

    def SetToBroadCast(self, const_Socket_UDP_Incoming_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        SetToBroadCast(const Socket_UDP_Incoming self)
        
        /**
         * Flips the OS bits that allow for brodcast packets to come in on this port.
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
        'InitNoAddress': None, # (!) real value is "<method 'InitNoAddress' of 'panda3d.core.Socket_UDP_Incoming' objects>"
        'OpenForInput': None, # (!) real value is "<method 'OpenForInput' of 'panda3d.core.Socket_UDP_Incoming' objects>"
        'OpenForInputMCast': None, # (!) real value is "<method 'OpenForInputMCast' of 'panda3d.core.Socket_UDP_Incoming' objects>"
        'SendTo': None, # (!) real value is "<method 'SendTo' of 'panda3d.core.Socket_UDP_Incoming' objects>"
        'SetToBroadCast': None, # (!) real value is "<method 'SetToBroadCast' of 'panda3d.core.Socket_UDP_Incoming' objects>"
        '__doc__': '/**\n * Base functionality for a UDP Reader\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.Socket_UDP_Incoming' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE38EA00>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE38EA00>)>'
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE38EA00>)>'
    }


