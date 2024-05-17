# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .ConnectionListener import ConnectionListener

from .QueuedReturn_ConnectionListenerData import QueuedReturn_ConnectionListenerData

class QueuedConnectionListener(ConnectionListener, QueuedReturn_ConnectionListenerData):
    """
    /**
     * This flavor of ConnectionListener will queue up all of the TCP connections
     * it established for later detection by the client code.
     */
    """
    def getNewConnection(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_new_connection(const QueuedConnectionListener self, PointerTo new_connection)
        get_new_connection(const QueuedConnectionListener self, PointerTo rendezvous, NetAddress address, PointerTo new_connection)
        
        /**
         * If a previous call to new_connection_available() returned true, this
         * function will return information about the newly established connection.
         *
         * The rendezvous parameter is the particular rendezvous socket this new
         * connection originally communicated with; it is provided in case the
         * ConnectionListener was monitorind more than one and you care which one it
         * was.  The address parameter is the net address of the new client, and
         * new_connection is the socket of the newly established connection.
         *
         * The return value is true if a connection was successfully returned, or
         * false if there was, in fact, no new connection.  (This may happen if there
         * are multiple threads accessing the QueuedConnectionListener).
         */
        
        /**
         * This flavor of get_new_connection() simply returns a new connection,
         * assuming the user doesn't care about the rendezvous socket that originated
         * it or the address it came from.
         */
        """
        pass

    def get_new_connection(self, const_QueuedConnectionListener_self, PointerTo_new_connection): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_new_connection(const QueuedConnectionListener self, PointerTo new_connection)
        get_new_connection(const QueuedConnectionListener self, PointerTo rendezvous, NetAddress address, PointerTo new_connection)
        
        /**
         * If a previous call to new_connection_available() returned true, this
         * function will return information about the newly established connection.
         *
         * The rendezvous parameter is the particular rendezvous socket this new
         * connection originally communicated with; it is provided in case the
         * ConnectionListener was monitorind more than one and you care which one it
         * was.  The address parameter is the net address of the new client, and
         * new_connection is the socket of the newly established connection.
         *
         * The return value is true if a connection was successfully returned, or
         * false if there was, in fact, no new connection.  (This may happen if there
         * are multiple threads accessing the QueuedConnectionListener).
         */
        
        /**
         * This flavor of get_new_connection() simply returns a new connection,
         * assuming the user doesn't care about the rendezvous socket that originated
         * it or the address it came from.
         */
        """
        pass

    def newConnectionAvailable(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        new_connection_available(const QueuedConnectionListener self)
        
        /**
         * Returns true if a new connection was recently established; the connection
         * information may then be retrieved via get_new_connection().
         */
        """
        pass

    def new_connection_available(self, const_QueuedConnectionListener_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        new_connection_available(const QueuedConnectionListener self)
        
        /**
         * Returns true if a new connection was recently established; the connection
         * information may then be retrieved via get_new_connection().
         */
        """
        pass

    def upcastToConnectionListener(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_ConnectionListener(const QueuedConnectionListener self)
        
        upcast from QueuedConnectionListener to ConnectionListener
        """
        pass

    def upcastToQueuedReturnConnectionListenerData(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_QueuedReturn_ConnectionListenerData(const QueuedConnectionListener self)
        
        upcast from QueuedConnectionListener to QueuedReturn< ConnectionListenerData >
        """
        pass

    def upcast_to_ConnectionListener(self, const_QueuedConnectionListener_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_ConnectionListener(const QueuedConnectionListener self)
        
        upcast from QueuedConnectionListener to ConnectionListener
        """
        pass

    def upcast_to_QueuedReturn_ConnectionListenerData(self, const_QueuedConnectionListener_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_QueuedReturn_ConnectionListenerData(const QueuedConnectionListener self)
        
        upcast from QueuedConnectionListener to QueuedReturn< ConnectionListenerData >
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
        '__doc__': '/**\n * This flavor of ConnectionListener will queue up all of the TCP connections\n * it established for later detection by the client code.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.QueuedConnectionListener' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE38AB10>'
        'getNewConnection': None, # (!) real value is "<method 'getNewConnection' of 'panda3d.core.QueuedConnectionListener' objects>"
        'get_new_connection': None, # (!) real value is "<method 'get_new_connection' of 'panda3d.core.QueuedConnectionListener' objects>"
        'newConnectionAvailable': None, # (!) real value is "<method 'newConnectionAvailable' of 'panda3d.core.QueuedConnectionListener' objects>"
        'new_connection_available': None, # (!) real value is "<method 'new_connection_available' of 'panda3d.core.QueuedConnectionListener' objects>"
        'upcastToConnectionListener': None, # (!) real value is "<method 'upcastToConnectionListener' of 'panda3d.core.QueuedConnectionListener' objects>"
        'upcastToQueuedReturnConnectionListenerData': None, # (!) real value is "<method 'upcastToQueuedReturnConnectionListenerData' of 'panda3d.core.QueuedConnectionListener' objects>"
        'upcast_to_ConnectionListener': None, # (!) real value is "<method 'upcast_to_ConnectionListener' of 'panda3d.core.QueuedConnectionListener' objects>"
        'upcast_to_QueuedReturn_ConnectionListenerData': None, # (!) real value is "<method 'upcast_to_QueuedReturn_ConnectionListenerData' of 'panda3d.core.QueuedConnectionListener' objects>"
    }


