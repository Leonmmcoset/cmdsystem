# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class ConnectionManager(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * The primary interface to the low-level networking layer in this package.  A
     * ConnectionManager is used to establish and destroy TCP and UDP connections.
     * Communication on these connections, once established, is handled via
     * ConnectionReader, ConnectionWriter, and ConnectionListener.
     *
     * You may use this class directly if you don't care about tracking which
     * connections have been unexpectedly closed; otherwise, you should use
     * QueuedConnectionManager to get reports about these events (or derive your
     * own class to handle these events properly).
     */
    """
    def closeConnection(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        close_connection(const ConnectionManager self, const Connection connection)
        
        /**
         * Terminates a UDP or TCP socket previously opened.  This also removes it
         * from any associated ConnectionReader or ConnectionListeners.
         *
         * The socket itself may not be immediately closed--it will not be closed
         * until all outstanding pointers to it are cleared, including any pointers
         * remaining in NetDatagrams recently received from the socket.
         *
         * The return value is true if the connection was marked to be closed, or
         * false if close_connection() had already been called (or the connection did
         * not belong to this ConnectionManager).  In neither case can you infer
         * anything about whether the connection has *actually* been closed yet based
         * on the return value.
         */
        """
        pass

    def close_connection(self, const_ConnectionManager_self, const_Connection_connection): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        close_connection(const ConnectionManager self, const Connection connection)
        
        /**
         * Terminates a UDP or TCP socket previously opened.  This also removes it
         * from any associated ConnectionReader or ConnectionListeners.
         *
         * The socket itself may not be immediately closed--it will not be closed
         * until all outstanding pointers to it are cleared, including any pointers
         * remaining in NetDatagrams recently received from the socket.
         *
         * The return value is true if the connection was marked to be closed, or
         * false if close_connection() had already been called (or the connection did
         * not belong to this ConnectionManager).  In neither case can you infer
         * anything about whether the connection has *actually* been closed yet based
         * on the return value.
         */
        """
        pass

    def getHostName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_host_name()
        
        /**
         * Returns the name of this particular machine on the network, if available,
         * or the empty string if the hostname cannot be determined.
         */
        """
        pass

    def getInterface(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_interface(const ConnectionManager self, int n)
        
        /**
         * Returns the nth usable network interface detected on this machine.
         * See scan_interfaces() to repopulate this list.
         */
        """
        pass

    def getInterfaces(self, *args, **kwargs): # real signature unknown
        pass

    def getNumInterfaces(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_interfaces(const ConnectionManager self)
        
        /**
         * This returns the number of usable network interfaces detected on this
         * machine.  See scan_interfaces() to repopulate this list.
         */
        """
        pass

    def get_host_name(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_host_name()
        
        /**
         * Returns the name of this particular machine on the network, if available,
         * or the empty string if the hostname cannot be determined.
         */
        """
        pass

    def get_interface(self, const_ConnectionManager_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_interface(const ConnectionManager self, int n)
        
        /**
         * Returns the nth usable network interface detected on this machine.
         * See scan_interfaces() to repopulate this list.
         */
        """
        pass

    def get_interfaces(self, *args, **kwargs): # real signature unknown
        pass

    def get_num_interfaces(self, const_ConnectionManager_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_interfaces(const ConnectionManager self)
        
        /**
         * This returns the number of usable network interfaces detected on this
         * machine.  See scan_interfaces() to repopulate this list.
         */
        """
        pass

    def openTCPClientConnection(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        open_TCP_client_connection(const ConnectionManager self, const NetAddress address, int timeout_ms)
        open_TCP_client_connection(const ConnectionManager self, str hostname, int port, int timeout_ms)
        
        /**
         * Attempts to establish a TCP client connection to a server at the indicated
         * address.  If the connection is not established within timeout_ms
         * milliseconds, a null connection is returned.
         */
        
        /**
         * This is a shorthand version of the function to directly establish
         * communications to a named host and port.
         */
        """
        pass

    def openTCPServerRendezvous(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        open_TCP_server_rendezvous(const ConnectionManager self, const NetAddress address, int backlog)
        open_TCP_server_rendezvous(const ConnectionManager self, int port, int backlog)
        open_TCP_server_rendezvous(const ConnectionManager self, str hostname, int port, int backlog)
        
        /**
         * Creates a socket to be used as a rendezvous socket for a server to listen
         * for TCP connections.  The socket returned by this call should only be added
         * to a ConnectionListener (not to a generic ConnectionReader).
         *
         * This variant of this method accepts a single port, and will listen to that
         * port on all available interfaces, both IPv4 and IPv6.
         *
         * backlog is the maximum length of the queue of pending connections.
         */
        
        /**
         * Creates a socket to be used as a rendezvous socket for a server to listen
         * for TCP connections.  The socket returned by this call should only be added
         * to a ConnectionListener (not to a generic ConnectionReader).
         *
         * This variant of this method accepts a "hostname", which is usually just an
         * IP address in dotted notation, and a port number.  It will listen on the
         * interface indicated by the IP address.  If the IP address is empty string,
         * it will listen on all interfaces.
         *
         * backlog is the maximum length of the queue of pending connections.
         */
        
        /**
         * Creates a socket to be used as a rendezvous socket for a server to listen
         * for TCP connections.  The socket returned by this call should only be added
         * to a ConnectionListener (not to a generic ConnectionReader).
         *
         * This variant of this method accepts a NetAddress, which allows you to
         * specify a specific interface to listen to.
         *
         * backlog is the maximum length of the queue of pending connections.
         */
        """
        pass

    def openUDPConnection(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        open_UDP_connection(const ConnectionManager self)
        open_UDP_connection(const ConnectionManager self, int port)
        open_UDP_connection(const ConnectionManager self, str hostname, int port, bool for_broadcast)
        
        /**
         * Opens a socket for sending and/or receiving UDP packets.  If the port
         * number is greater than zero, the UDP connection will be opened for
         * listening on the indicated port; otherwise, it will be useful only for
         * sending.
         *
         * Use a ConnectionReader and ConnectionWriter to handle the actual
         * communication.
         */
        
        /**
         * Opens a socket for sending and/or receiving UDP packets.  If the port
         * number is greater than zero, the UDP connection will be opened for
         * listening on the indicated port; otherwise, it will be useful only for
         * sending.
         *
         * This variant accepts both a hostname and port to listen on a particular
         * interface; if the hostname is empty, all interfaces will be available,
         * both IPv4 and IPv6.
         *
         * If for_broadcast is true, this UDP connection will be configured to send
         * and/or receive messages on the broadcast address (255.255.255.255);
         * otherwise, these messages may be automatically filtered by the OS.
         *
         * Use a ConnectionReader and ConnectionWriter to handle the actual
         * communication.
         */
        """
        pass

    def open_TCP_client_connection(self, const_ConnectionManager_self, const_NetAddress_address, int_timeout_ms): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        open_TCP_client_connection(const ConnectionManager self, const NetAddress address, int timeout_ms)
        open_TCP_client_connection(const ConnectionManager self, str hostname, int port, int timeout_ms)
        
        /**
         * Attempts to establish a TCP client connection to a server at the indicated
         * address.  If the connection is not established within timeout_ms
         * milliseconds, a null connection is returned.
         */
        
        /**
         * This is a shorthand version of the function to directly establish
         * communications to a named host and port.
         */
        """
        pass

    def open_TCP_server_rendezvous(self, const_ConnectionManager_self, const_NetAddress_address, int_backlog): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        open_TCP_server_rendezvous(const ConnectionManager self, const NetAddress address, int backlog)
        open_TCP_server_rendezvous(const ConnectionManager self, int port, int backlog)
        open_TCP_server_rendezvous(const ConnectionManager self, str hostname, int port, int backlog)
        
        /**
         * Creates a socket to be used as a rendezvous socket for a server to listen
         * for TCP connections.  The socket returned by this call should only be added
         * to a ConnectionListener (not to a generic ConnectionReader).
         *
         * This variant of this method accepts a single port, and will listen to that
         * port on all available interfaces, both IPv4 and IPv6.
         *
         * backlog is the maximum length of the queue of pending connections.
         */
        
        /**
         * Creates a socket to be used as a rendezvous socket for a server to listen
         * for TCP connections.  The socket returned by this call should only be added
         * to a ConnectionListener (not to a generic ConnectionReader).
         *
         * This variant of this method accepts a "hostname", which is usually just an
         * IP address in dotted notation, and a port number.  It will listen on the
         * interface indicated by the IP address.  If the IP address is empty string,
         * it will listen on all interfaces.
         *
         * backlog is the maximum length of the queue of pending connections.
         */
        
        /**
         * Creates a socket to be used as a rendezvous socket for a server to listen
         * for TCP connections.  The socket returned by this call should only be added
         * to a ConnectionListener (not to a generic ConnectionReader).
         *
         * This variant of this method accepts a NetAddress, which allows you to
         * specify a specific interface to listen to.
         *
         * backlog is the maximum length of the queue of pending connections.
         */
        """
        pass

    def open_UDP_connection(self, const_ConnectionManager_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        open_UDP_connection(const ConnectionManager self)
        open_UDP_connection(const ConnectionManager self, int port)
        open_UDP_connection(const ConnectionManager self, str hostname, int port, bool for_broadcast)
        
        /**
         * Opens a socket for sending and/or receiving UDP packets.  If the port
         * number is greater than zero, the UDP connection will be opened for
         * listening on the indicated port; otherwise, it will be useful only for
         * sending.
         *
         * Use a ConnectionReader and ConnectionWriter to handle the actual
         * communication.
         */
        
        /**
         * Opens a socket for sending and/or receiving UDP packets.  If the port
         * number is greater than zero, the UDP connection will be opened for
         * listening on the indicated port; otherwise, it will be useful only for
         * sending.
         *
         * This variant accepts both a hostname and port to listen on a particular
         * interface; if the hostname is empty, all interfaces will be available,
         * both IPv4 and IPv6.
         *
         * If for_broadcast is true, this UDP connection will be configured to send
         * and/or receive messages on the broadcast address (255.255.255.255);
         * otherwise, these messages may be automatically filtered by the OS.
         *
         * Use a ConnectionReader and ConnectionWriter to handle the actual
         * communication.
         */
        """
        pass

    def scanInterfaces(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        scan_interfaces(const ConnectionManager self)
        
        /**
         * Repopulates the list reported by get_num_interface()/get_interface().  It
         * is not necessary to call this explicitly, unless you want to re-determine
         * the connected interfaces (for instance, if you suspect the hardware has
         * recently changed).
         */
        """
        pass

    def scan_interfaces(self, const_ConnectionManager_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        scan_interfaces(const ConnectionManager self)
        
        /**
         * Repopulates the list reported by get_num_interface()/get_interface().  It
         * is not necessary to call this explicitly, unless you want to re-determine
         * the connected interfaces (for instance, if you suspect the hardware has
         * recently changed).
         */
        """
        pass

    def waitForReaders(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        wait_for_readers(const ConnectionManager self, double timeout)
        
        /**
         * Blocks the process for timeout number of seconds, or until any data is
         * available on any of the non-threaded ConnectionReaders or
         * ConnectionListeners, whichever comes first.  The return value is true if
         * there is data available (but you have to iterate through all readers to
         * find it), or false if the timeout occurred without any data.
         *
         * If the timeout value is negative, this will block forever or until data is
         * available.
         *
         * This only works if all ConnectionReaders and ConnectionListeners are non-
         * threaded.  If any threaded ConnectionReaders are part of the
         * ConnectionManager, the timeout value is implicitly treated as 0.
         */
        """
        pass

    def wait_for_readers(self, const_ConnectionManager_self, double_timeout): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        wait_for_readers(const ConnectionManager self, double timeout)
        
        /**
         * Blocks the process for timeout number of seconds, or until any data is
         * available on any of the non-threaded ConnectionReaders or
         * ConnectionListeners, whichever comes first.  The return value is true if
         * there is data available (but you have to iterate through all readers to
         * find it), or false if the timeout occurred without any data.
         *
         * If the timeout value is negative, this will block forever or until data is
         * available.
         *
         * This only works if all ConnectionReaders and ConnectionListeners are non-
         * threaded.  If any threaded ConnectionReaders are part of the
         * ConnectionManager, the timeout value is implicitly treated as 0.
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    interfaces = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        'Interface': None, # (!) real value is "<class 'panda3d.core.Interface'>"
        '__doc__': "/**\n * The primary interface to the low-level networking layer in this package.  A\n * ConnectionManager is used to establish and destroy TCP and UDP connections.\n * Communication on these connections, once established, is handled via\n * ConnectionReader, ConnectionWriter, and ConnectionListener.\n *\n * You may use this class directly if you don't care about tracking which\n * connections have been unexpectedly closed; otherwise, you should use\n * QueuedConnectionManager to get reports about these events (or derive your\n * own class to handle these events properly).\n */",
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.ConnectionManager' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE38A030>'
        'closeConnection': None, # (!) real value is "<method 'closeConnection' of 'panda3d.core.ConnectionManager' objects>"
        'close_connection': None, # (!) real value is "<method 'close_connection' of 'panda3d.core.ConnectionManager' objects>"
        'getHostName': None, # (!) real value is '<staticmethod(<built-in method getHostName of type object at 0x00007FFCFE38A030>)>'
        'getInterface': None, # (!) real value is "<method 'getInterface' of 'panda3d.core.ConnectionManager' objects>"
        'getInterfaces': None, # (!) real value is "<method 'getInterfaces' of 'panda3d.core.ConnectionManager' objects>"
        'getNumInterfaces': None, # (!) real value is "<method 'getNumInterfaces' of 'panda3d.core.ConnectionManager' objects>"
        'get_host_name': None, # (!) real value is '<staticmethod(<built-in method get_host_name of type object at 0x00007FFCFE38A030>)>'
        'get_interface': None, # (!) real value is "<method 'get_interface' of 'panda3d.core.ConnectionManager' objects>"
        'get_interfaces': None, # (!) real value is "<method 'get_interfaces' of 'panda3d.core.ConnectionManager' objects>"
        'get_num_interfaces': None, # (!) real value is "<method 'get_num_interfaces' of 'panda3d.core.ConnectionManager' objects>"
        'host_name': None, # (!) real value is "<attribute 'host_name' of 'panda3d.core.ConnectionManager'>"
        'interfaces': None, # (!) real value is "<attribute 'interfaces' of 'panda3d.core.ConnectionManager' objects>"
        'openTCPClientConnection': None, # (!) real value is "<method 'openTCPClientConnection' of 'panda3d.core.ConnectionManager' objects>"
        'openTCPServerRendezvous': None, # (!) real value is "<method 'openTCPServerRendezvous' of 'panda3d.core.ConnectionManager' objects>"
        'openUDPConnection': None, # (!) real value is "<method 'openUDPConnection' of 'panda3d.core.ConnectionManager' objects>"
        'open_TCP_client_connection': None, # (!) real value is "<method 'open_TCP_client_connection' of 'panda3d.core.ConnectionManager' objects>"
        'open_TCP_server_rendezvous': None, # (!) real value is "<method 'open_TCP_server_rendezvous' of 'panda3d.core.ConnectionManager' objects>"
        'open_UDP_connection': None, # (!) real value is "<method 'open_UDP_connection' of 'panda3d.core.ConnectionManager' objects>"
        'scanInterfaces': None, # (!) real value is "<method 'scanInterfaces' of 'panda3d.core.ConnectionManager' objects>"
        'scan_interfaces': None, # (!) real value is "<method 'scan_interfaces' of 'panda3d.core.ConnectionManager' objects>"
        'waitForReaders': None, # (!) real value is "<method 'waitForReaders' of 'panda3d.core.ConnectionManager' objects>"
        'wait_for_readers': None, # (!) real value is "<method 'wait_for_readers' of 'panda3d.core.ConnectionManager' objects>"
    }
    host_name = 'DESKTOP-G6NU34J'
    Interface = None # (!) real value is "<class 'panda3d.core.Interface'>"


