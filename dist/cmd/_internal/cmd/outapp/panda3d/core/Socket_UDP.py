# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .Socket_UDP_Incoming import Socket_UDP_Incoming

class Socket_UDP(Socket_UDP_Incoming):
    """
    /**
     * Base functionality for a combination UDP Reader and Writer.  This
     * duplicates code from Socket_UDP_Outgoing, to avoid the problems of multiple
     * inheritance.
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

    def InitToAddress(self, const_Socket_UDP_self, const_Socket_Address_address): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        InitToAddress(const Socket_UDP self, const Socket_Address address)
        
        // use this interface for a tagreted UDP connection
        
        /**
         * Connects the socket to a Specified address
         */
        """
        pass

    def Send(self, const_Socket_UDP_self, str_data): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        Send(const Socket_UDP self, str data)
        
        /**
         * Send data to connected address
         */
        
        /**
         * Send data to connected address
         */
        """
        pass

    def SendTo(self, const_Socket_UDP_self, str_data, const_Socket_Address_address): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        SendTo(const Socket_UDP self, str data, const Socket_Address address)
        
        /**
         * Send data to specified address
         */
        
        /**
         * Send data to specified address
         */
        """
        pass

    def SetToBroadCast(self, const_Socket_UDP_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        SetToBroadCast(const Socket_UDP self)
        
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
        'InitToAddress': None, # (!) real value is "<method 'InitToAddress' of 'panda3d.core.Socket_UDP' objects>"
        'Send': None, # (!) real value is "<method 'Send' of 'panda3d.core.Socket_UDP' objects>"
        'SendTo': None, # (!) real value is "<method 'SendTo' of 'panda3d.core.Socket_UDP' objects>"
        'SetToBroadCast': None, # (!) real value is "<method 'SetToBroadCast' of 'panda3d.core.Socket_UDP' objects>"
        '__doc__': '/**\n * Base functionality for a combination UDP Reader and Writer.  This\n * duplicates code from Socket_UDP_Outgoing, to avoid the problems of multiple\n * inheritance.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.Socket_UDP' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE38F140>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE38F140>)>'
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE38F140>)>'
    }


