# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class ConnectionReader(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * This is an abstract base class for a family of classes that listen for
     * activity on a socket and respond to it, for instance by reading a datagram
     * and serving it (or queueing it up for later service).
     *
     * A ConnectionReader may define an arbitrary number of threads (at least one)
     * to process datagrams coming in from an arbitrary number of sockets that it
     * is monitoring.  The number of threads is specified at construction time and
     * cannot be changed, but the set of sockets that is to be monitored may be
     * constantly modified at will.
     *
     * This is an abstract class because it doesn't define how to process each
     * received datagram.  See QueuedConnectionReader.  Also note that
     * ConnectionListener derives from this class, extending it to accept
     * connections on a rendezvous socket rather than read datagrams.
     */
    """
    def addConnection(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_connection(const ConnectionReader self, Connection connection)
        
        /**
         * Adds a new socket to the list of sockets the ConnectionReader will monitor.
         * A datagram that comes in on any of the monitored sockets will be reported.
         * In the case of a ConnectionListener, this adds a new rendezvous socket; any
         * activity on any of the monitored sockets will cause a connection to be
         * accepted.
         *
         * The return value is true if the connection was added, false if it was
         * already there.
         *
         * add_connection() is thread-safe, and may be called at will by any thread.
         */
        """
        pass

    def add_connection(self, const_ConnectionReader_self, Connection_connection): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_connection(const ConnectionReader self, Connection connection)
        
        /**
         * Adds a new socket to the list of sockets the ConnectionReader will monitor.
         * A datagram that comes in on any of the monitored sockets will be reported.
         * In the case of a ConnectionListener, this adds a new rendezvous socket; any
         * activity on any of the monitored sockets will cause a connection to be
         * accepted.
         *
         * The return value is true if the connection was added, false if it was
         * already there.
         *
         * add_connection() is thread-safe, and may be called at will by any thread.
         */
        """
        pass

    def getManager(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_manager(ConnectionReader self)
        
        /**
         * Returns a pointer to the ConnectionManager object that serves this
         * ConnectionReader.
         */
        """
        pass

    def getNumThreads(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_threads(ConnectionReader self)
        
        /**
         * Returns the number of threads the ConnectionReader has been created with.
         */
        """
        pass

    def getRawMode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_raw_mode(ConnectionReader self)
        
        /**
         * Returns the current setting of the raw mode flag.  See set_raw_mode().
         */
        """
        pass

    def getTcpHeaderSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_tcp_header_size(ConnectionReader self)
        
        /**
         * Returns the current setting of TCP header size.  See set_tcp_header_size().
         */
        """
        pass

    def get_manager(self, ConnectionReader_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_manager(ConnectionReader self)
        
        /**
         * Returns a pointer to the ConnectionManager object that serves this
         * ConnectionReader.
         */
        """
        pass

    def get_num_threads(self, ConnectionReader_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_threads(ConnectionReader self)
        
        /**
         * Returns the number of threads the ConnectionReader has been created with.
         */
        """
        pass

    def get_raw_mode(self, ConnectionReader_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_raw_mode(ConnectionReader self)
        
        /**
         * Returns the current setting of the raw mode flag.  See set_raw_mode().
         */
        """
        pass

    def get_tcp_header_size(self, ConnectionReader_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_tcp_header_size(ConnectionReader self)
        
        /**
         * Returns the current setting of TCP header size.  See set_tcp_header_size().
         */
        """
        pass

    def isConnectionOk(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_connection_ok(const ConnectionReader self, Connection connection)
        
        /**
         * Returns true if the indicated connection has been added to the
         * ConnectionReader and is being monitored properly, false if it is not known,
         * or if there was some error condition detected on the connection.  (If there
         * was an error condition, normally the ConnectionManager would have been
         * informed and closed the connection.)
         */
        """
        pass

    def isPolling(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_polling(ConnectionReader self)
        
        /**
         * Returns true if the reader is a polling reader, i.e.  it has no threads.
         */
        """
        pass

    def is_connection_ok(self, const_ConnectionReader_self, Connection_connection): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_connection_ok(const ConnectionReader self, Connection connection)
        
        /**
         * Returns true if the indicated connection has been added to the
         * ConnectionReader and is being monitored properly, false if it is not known,
         * or if there was some error condition detected on the connection.  (If there
         * was an error condition, normally the ConnectionManager would have been
         * informed and closed the connection.)
         */
        """
        pass

    def is_polling(self, ConnectionReader_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_polling(ConnectionReader self)
        
        /**
         * Returns true if the reader is a polling reader, i.e.  it has no threads.
         */
        """
        pass

    def poll(self, const_ConnectionReader_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        poll(const ConnectionReader self)
        
        /**
         * Explicitly polls the available sockets to see if any of them have any
         * noise.  This function does nothing unless this is a polling-type
         * ConnectionReader, i.e.  it was created with zero threads (and is_polling()
         * will return true).
         *
         * It is not necessary to call this explicitly for a QueuedConnectionReader.
         */
        """
        pass

    def removeConnection(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_connection(const ConnectionReader self, Connection connection)
        
        /**
         * Removes a socket from the list of sockets being monitored.  Returns true if
         * the socket was correctly removed, false if it was not on the list in the
         * first place.
         *
         * remove_connection() is thread-safe, and may be called at will by any
         * thread.
         */
        """
        pass

    def remove_connection(self, const_ConnectionReader_self, Connection_connection): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_connection(const ConnectionReader self, Connection connection)
        
        /**
         * Removes a socket from the list of sockets being monitored.  Returns true if
         * the socket was correctly removed, false if it was not on the list in the
         * first place.
         *
         * remove_connection() is thread-safe, and may be called at will by any
         * thread.
         */
        """
        pass

    def setRawMode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_raw_mode(const ConnectionReader self, bool mode)
        
        /**
         * Sets the ConnectionReader into raw mode (or turns off raw mode).  In raw
         * mode, datagram headers are not expected; instead, all the data available on
         * the pipe is treated as a single datagram.
         *
         * This is similar to set_tcp_header_size(0), except that it also turns off
         * headers for UDP packets.
         */
        """
        pass

    def setTcpHeaderSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_tcp_header_size(const ConnectionReader self, int tcp_header_size)
        
        /**
         * Sets the header size of TCP packets.  At the present, legal values for this
         * are 0, 2, or 4; this specifies the number of bytes to use encode the
         * datagram length at the start of each TCP datagram.  Sender and receiver
         * must independently agree on this.
         */
        """
        pass

    def set_raw_mode(self, const_ConnectionReader_self, bool_mode): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_raw_mode(const ConnectionReader self, bool mode)
        
        /**
         * Sets the ConnectionReader into raw mode (or turns off raw mode).  In raw
         * mode, datagram headers are not expected; instead, all the data available on
         * the pipe is treated as a single datagram.
         *
         * This is similar to set_tcp_header_size(0), except that it also turns off
         * headers for UDP packets.
         */
        """
        pass

    def set_tcp_header_size(self, const_ConnectionReader_self, int_tcp_header_size): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_tcp_header_size(const ConnectionReader self, int tcp_header_size)
        
        /**
         * Sets the header size of TCP packets.  At the present, legal values for this
         * are 0, 2, or 4; this specifies the number of bytes to use encode the
         * datagram length at the start of each TCP datagram.  Sender and receiver
         * must independently agree on this.
         */
        """
        pass

    def shutdown(self, const_ConnectionReader_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        shutdown(const ConnectionReader self)
        
        /**
         * Terminates all threads cleanly.  Normally this is only called by the
         * destructor, but it may be called explicitly before destruction.
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
        '__doc__': "/**\n * This is an abstract base class for a family of classes that listen for\n * activity on a socket and respond to it, for instance by reading a datagram\n * and serving it (or queueing it up for later service).\n *\n * A ConnectionReader may define an arbitrary number of threads (at least one)\n * to process datagrams coming in from an arbitrary number of sockets that it\n * is monitoring.  The number of threads is specified at construction time and\n * cannot be changed, but the set of sockets that is to be monitored may be\n * constantly modified at will.\n *\n * This is an abstract class because it doesn't define how to process each\n * received datagram.  See QueuedConnectionReader.  Also note that\n * ConnectionListener derives from this class, extending it to accept\n * connections on a rendezvous socket rather than read datagrams.\n */",
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.ConnectionReader' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE389AC0>'
        'addConnection': None, # (!) real value is "<method 'addConnection' of 'panda3d.core.ConnectionReader' objects>"
        'add_connection': None, # (!) real value is "<method 'add_connection' of 'panda3d.core.ConnectionReader' objects>"
        'getManager': None, # (!) real value is "<method 'getManager' of 'panda3d.core.ConnectionReader' objects>"
        'getNumThreads': None, # (!) real value is "<method 'getNumThreads' of 'panda3d.core.ConnectionReader' objects>"
        'getRawMode': None, # (!) real value is "<method 'getRawMode' of 'panda3d.core.ConnectionReader' objects>"
        'getTcpHeaderSize': None, # (!) real value is "<method 'getTcpHeaderSize' of 'panda3d.core.ConnectionReader' objects>"
        'get_manager': None, # (!) real value is "<method 'get_manager' of 'panda3d.core.ConnectionReader' objects>"
        'get_num_threads': None, # (!) real value is "<method 'get_num_threads' of 'panda3d.core.ConnectionReader' objects>"
        'get_raw_mode': None, # (!) real value is "<method 'get_raw_mode' of 'panda3d.core.ConnectionReader' objects>"
        'get_tcp_header_size': None, # (!) real value is "<method 'get_tcp_header_size' of 'panda3d.core.ConnectionReader' objects>"
        'isConnectionOk': None, # (!) real value is "<method 'isConnectionOk' of 'panda3d.core.ConnectionReader' objects>"
        'isPolling': None, # (!) real value is "<method 'isPolling' of 'panda3d.core.ConnectionReader' objects>"
        'is_connection_ok': None, # (!) real value is "<method 'is_connection_ok' of 'panda3d.core.ConnectionReader' objects>"
        'is_polling': None, # (!) real value is "<method 'is_polling' of 'panda3d.core.ConnectionReader' objects>"
        'poll': None, # (!) real value is "<method 'poll' of 'panda3d.core.ConnectionReader' objects>"
        'removeConnection': None, # (!) real value is "<method 'removeConnection' of 'panda3d.core.ConnectionReader' objects>"
        'remove_connection': None, # (!) real value is "<method 'remove_connection' of 'panda3d.core.ConnectionReader' objects>"
        'setRawMode': None, # (!) real value is "<method 'setRawMode' of 'panda3d.core.ConnectionReader' objects>"
        'setTcpHeaderSize': None, # (!) real value is "<method 'setTcpHeaderSize' of 'panda3d.core.ConnectionReader' objects>"
        'set_raw_mode': None, # (!) real value is "<method 'set_raw_mode' of 'panda3d.core.ConnectionReader' objects>"
        'set_tcp_header_size': None, # (!) real value is "<method 'set_tcp_header_size' of 'panda3d.core.ConnectionReader' objects>"
        'shutdown': None, # (!) real value is "<method 'shutdown' of 'panda3d.core.ConnectionReader' objects>"
    }


