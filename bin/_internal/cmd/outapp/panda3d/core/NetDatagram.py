# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .Datagram import Datagram

class NetDatagram(Datagram):
    """
    /**
     * A specific kind of Datagram, especially for sending across or receiving
     * from a network.  It's different only in that it knows which Connection
     * and/or NetAddress it is to be sent to or was received from.
     */
    """
    def assign(self, const_NetDatagram_self, const_NetDatagram_copy): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        assign(const NetDatagram self, const NetDatagram copy)
        assign(const NetDatagram self, const Datagram copy)
        """
        pass

    def getAddress(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_address(NetDatagram self)
        
        /**
         * Retrieves the host from which the datagram was read, or to which it is
         * scheduled to be sent.
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getConnection(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_connection(NetDatagram self)
        
        /**
         * Retrieves the socket from which the datagram was read, or to which it is
         * scheduled to be written.
         */
        """
        pass

    def get_address(self, NetDatagram_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_address(NetDatagram self)
        
        /**
         * Retrieves the host from which the datagram was read, or to which it is
         * scheduled to be sent.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_connection(self, NetDatagram_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_connection(NetDatagram self)
        
        /**
         * Retrieves the socket from which the datagram was read, or to which it is
         * scheduled to be written.
         */
        """
        pass

    def setAddress(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_address(const NetDatagram self, const NetAddress address)
        
        /**
         * Specifies the host to which the datagram should be sent.
         */
        """
        pass

    def setConnection(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_connection(const NetDatagram self, const Connection connection)
        
        /**
         * Specifies the socket to which the datagram should be written.
         */
        """
        pass

    def set_address(self, const_NetDatagram_self, const_NetAddress_address): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_address(const NetDatagram self, const NetAddress address)
        
        /**
         * Specifies the host to which the datagram should be sent.
         */
        """
        pass

    def set_connection(self, const_NetDatagram_self, const_Connection_connection): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_connection(const NetDatagram self, const Connection connection)
        
        /**
         * Specifies the socket to which the datagram should be written.
         */
        """
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __deepcopy__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.NetDatagram' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.NetDatagram' objects>"
        '__doc__': "/**\n * A specific kind of Datagram, especially for sending across or receiving\n * from a network.  It's different only in that it knows which Connection\n * and/or NetAddress it is to be sent to or was received from.\n */",
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.NetDatagram' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE389E60>'
        'assign': None, # (!) real value is "<method 'assign' of 'panda3d.core.NetDatagram' objects>"
        'getAddress': None, # (!) real value is "<method 'getAddress' of 'panda3d.core.NetDatagram' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE389E60>)>'
        'getConnection': None, # (!) real value is "<method 'getConnection' of 'panda3d.core.NetDatagram' objects>"
        'get_address': None, # (!) real value is "<method 'get_address' of 'panda3d.core.NetDatagram' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE389E60>)>'
        'get_connection': None, # (!) real value is "<method 'get_connection' of 'panda3d.core.NetDatagram' objects>"
        'setAddress': None, # (!) real value is "<method 'setAddress' of 'panda3d.core.NetDatagram' objects>"
        'setConnection': None, # (!) real value is "<method 'setConnection' of 'panda3d.core.NetDatagram' objects>"
        'set_address': None, # (!) real value is "<method 'set_address' of 'panda3d.core.NetDatagram' objects>"
        'set_connection': None, # (!) real value is "<method 'set_connection' of 'panda3d.core.NetDatagram' objects>"
    }


