# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .Socket_IP import Socket_IP

class Socket_TCP_Listen(Socket_IP):
    """
    /**
     * Base functionality for a TCP rendezvous socket
     */
    """
    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def GetIncomingConnection(self, const_Socket_TCP_Listen_self, Socket_TCP_newsession, Socket_Address_address): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        GetIncomingConnection(const Socket_TCP_Listen self, Socket_TCP newsession, Socket_Address address)
        
        /**
         * This function is used to accept new connections
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def OpenForListen(self, const_Socket_TCP_Listen_self, const_Socket_Address_address, int_backlog_size): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        OpenForListen(const Socket_TCP_Listen self, const Socket_Address address, int backlog_size)
        OpenForListen(const Socket_TCP_Listen self, int port, int backlog_size)
        
        /**
         * This function will initialize a listening Socket
         */
        
        /**
         * This function will initialize a listening Socket
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
        'GetIncomingConnection': None, # (!) real value is "<method 'GetIncomingConnection' of 'panda3d.core.Socket_TCP_Listen' objects>"
        'OpenForListen': None, # (!) real value is "<method 'OpenForListen' of 'panda3d.core.Socket_TCP_Listen' objects>"
        '__doc__': '/**\n * Base functionality for a TCP rendezvous socket\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.Socket_TCP_Listen' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE38E830>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE38E830>)>'
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE38E830>)>'
    }


