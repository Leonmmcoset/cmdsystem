# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .ConnectionManager import ConnectionManager

from .QueuedReturn_PointerTo_Connection import QueuedReturn_PointerTo_Connection

class QueuedConnectionManager(ConnectionManager, QueuedReturn_PointerTo_Connection):
    """
    /**
     * This flavor of ConnectionManager will queue up all of the reset-connection
     * messages from the ConnectionReaders and ConnectionWriters and report them
     * to the client on demand.
     *
     * When a reset connection has been discovered via
     * reset_connection_available()/get_reset_connection(), it is still the
     * responsibility of the client to call close_connection() on that connection
     * to free up its resources.
     */
    """
    def getResetConnection(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_reset_connection(const QueuedConnectionManager self, PointerTo connection)
        
        /**
         * If a previous call to reset_connection_available() returned true, this
         * function will return information about the newly reset connection.
         *
         * Only connections which were externally reset are certain to appear in this
         * list.  Those which were explicitly closed via a call to close_connection()
         * may or may not be reported.  Furthermore, it is the responsibility of the
         * caller to subsequently call close_connection() with any connection reported
         * reset by this call.  (There is no harm in calling close_connection() more
         * than once on a given socket.)
         *
         * The return value is true if a connection was successfully returned, or
         * false if there was, in fact, no reset connection.  (This may happen if
         * there are multiple threads accessing the QueuedConnectionManager).
         */
        """
        pass

    def get_reset_connection(self, const_QueuedConnectionManager_self, PointerTo_connection): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_reset_connection(const QueuedConnectionManager self, PointerTo connection)
        
        /**
         * If a previous call to reset_connection_available() returned true, this
         * function will return information about the newly reset connection.
         *
         * Only connections which were externally reset are certain to appear in this
         * list.  Those which were explicitly closed via a call to close_connection()
         * may or may not be reported.  Furthermore, it is the responsibility of the
         * caller to subsequently call close_connection() with any connection reported
         * reset by this call.  (There is no harm in calling close_connection() more
         * than once on a given socket.)
         *
         * The return value is true if a connection was successfully returned, or
         * false if there was, in fact, no reset connection.  (This may happen if
         * there are multiple threads accessing the QueuedConnectionManager).
         */
        """
        pass

    def resetConnectionAvailable(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        reset_connection_available(QueuedConnectionManager self)
        
        /**
         * Returns true if one of the readers/writers/listeners reported a connection
         * reset recently.  If so, the particular connection that has been reset can
         * be extracted via get_reset_connection().
         *
         * Only connections which were externally reset are certain to appear in this
         * list.  Those which were explicitly closed via a call to close_connection()
         * may or may not be reported.  Furthermore, it is the responsibility of the
         * caller to subsequently call close_connection() with any connection reported
         * reset by this call.  (There is no harm in calling close_connection() more
         * than once on a given socket.)
         */
        """
        pass

    def reset_connection_available(self, QueuedConnectionManager_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        reset_connection_available(QueuedConnectionManager self)
        
        /**
         * Returns true if one of the readers/writers/listeners reported a connection
         * reset recently.  If so, the particular connection that has been reset can
         * be extracted via get_reset_connection().
         *
         * Only connections which were externally reset are certain to appear in this
         * list.  Those which were explicitly closed via a call to close_connection()
         * may or may not be reported.  Furthermore, it is the responsibility of the
         * caller to subsequently call close_connection() with any connection reported
         * reset by this call.  (There is no harm in calling close_connection() more
         * than once on a given socket.)
         */
        """
        pass

    def upcastToConnectionManager(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_ConnectionManager(const QueuedConnectionManager self)
        
        upcast from QueuedConnectionManager to ConnectionManager
        """
        pass

    def upcastToQueuedReturnPointerToConnection(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_QueuedReturn_PointerTo_Connection(const QueuedConnectionManager self)
        
        upcast from QueuedConnectionManager to QueuedReturn< PointerTo< Connection > >
        """
        pass

    def upcast_to_ConnectionManager(self, const_QueuedConnectionManager_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_ConnectionManager(const QueuedConnectionManager self)
        
        upcast from QueuedConnectionManager to ConnectionManager
        """
        pass

    def upcast_to_QueuedReturn_PointerTo_Connection(self, const_QueuedConnectionManager_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_QueuedReturn_PointerTo_Connection(const QueuedConnectionManager self)
        
        upcast from QueuedConnectionManager to QueuedReturn< PointerTo< Connection > >
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
        '__doc__': '/**\n * This flavor of ConnectionManager will queue up all of the reset-connection\n * messages from the ConnectionReaders and ConnectionWriters and report them\n * to the client on demand.\n *\n * When a reset connection has been discovered via\n * reset_connection_available()/get_reset_connection(), it is still the\n * responsibility of the client to call close_connection() on that connection\n * to free up its resources.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.QueuedConnectionManager' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE38AEB0>'
        'getResetConnection': None, # (!) real value is "<method 'getResetConnection' of 'panda3d.core.QueuedConnectionManager' objects>"
        'get_reset_connection': None, # (!) real value is "<method 'get_reset_connection' of 'panda3d.core.QueuedConnectionManager' objects>"
        'resetConnectionAvailable': None, # (!) real value is "<method 'resetConnectionAvailable' of 'panda3d.core.QueuedConnectionManager' objects>"
        'reset_connection_available': None, # (!) real value is "<method 'reset_connection_available' of 'panda3d.core.QueuedConnectionManager' objects>"
        'upcastToConnectionManager': None, # (!) real value is "<method 'upcastToConnectionManager' of 'panda3d.core.QueuedConnectionManager' objects>"
        'upcastToQueuedReturnPointerToConnection': None, # (!) real value is "<method 'upcastToQueuedReturnPointerToConnection' of 'panda3d.core.QueuedConnectionManager' objects>"
        'upcast_to_ConnectionManager': None, # (!) real value is "<method 'upcast_to_ConnectionManager' of 'panda3d.core.QueuedConnectionManager' objects>"
        'upcast_to_QueuedReturn_PointerTo_Connection': None, # (!) real value is "<method 'upcast_to_QueuedReturn_PointerTo_Connection' of 'panda3d.core.QueuedConnectionManager' objects>"
    }


