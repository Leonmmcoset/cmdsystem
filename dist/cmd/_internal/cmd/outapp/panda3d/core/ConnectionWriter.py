# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class ConnectionWriter(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * This class handles threaded delivery of datagrams to various TCP or UDP
     * sockets.
     *
     * A ConnectionWriter may define an arbitrary number of threads (0 or more) to
     * write its datagrams to sockets.  The number of threads is specified at
     * construction time and cannot be changed.
     */
    """
    def getCurrentQueueSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_current_queue_size(ConnectionWriter self)
        
        /**
         * Returns the current number of things in the queue.
         */
        """
        pass

    def getManager(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_manager(ConnectionWriter self)
        
        /**
         * Returns a pointer to the ConnectionManager object that serves this
         * ConnectionWriter.
         */
        """
        pass

    def getMaxQueueSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_max_queue_size(ConnectionWriter self)
        
        /**
         * Returns the maximum size the queue is allowed to grow to.  See
         * set_max_queue_size().
         */
        """
        pass

    def getNumThreads(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_threads(ConnectionWriter self)
        
        /**
         * Returns the number of threads the ConnectionWriter has been created with.
         */
        """
        pass

    def getRawMode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_raw_mode(ConnectionWriter self)
        
        /**
         * Returns the current setting of the raw mode flag.  See set_raw_mode().
         */
        """
        pass

    def getTcpHeaderSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_tcp_header_size(ConnectionWriter self)
        
        /**
         * Returns the current setting of TCP header size.  See set_tcp_header_size().
         */
        """
        pass

    def get_current_queue_size(self, ConnectionWriter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_current_queue_size(ConnectionWriter self)
        
        /**
         * Returns the current number of things in the queue.
         */
        """
        pass

    def get_manager(self, ConnectionWriter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_manager(ConnectionWriter self)
        
        /**
         * Returns a pointer to the ConnectionManager object that serves this
         * ConnectionWriter.
         */
        """
        pass

    def get_max_queue_size(self, ConnectionWriter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_max_queue_size(ConnectionWriter self)
        
        /**
         * Returns the maximum size the queue is allowed to grow to.  See
         * set_max_queue_size().
         */
        """
        pass

    def get_num_threads(self, ConnectionWriter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_threads(ConnectionWriter self)
        
        /**
         * Returns the number of threads the ConnectionWriter has been created with.
         */
        """
        pass

    def get_raw_mode(self, ConnectionWriter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_raw_mode(ConnectionWriter self)
        
        /**
         * Returns the current setting of the raw mode flag.  See set_raw_mode().
         */
        """
        pass

    def get_tcp_header_size(self, ConnectionWriter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_tcp_header_size(ConnectionWriter self)
        
        /**
         * Returns the current setting of TCP header size.  See set_tcp_header_size().
         */
        """
        pass

    def isImmediate(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_immediate(ConnectionWriter self)
        
        /**
         * Returns true if the writer is an immediate writer, i.e.  it has no threads.
         */
        """
        pass

    def isValidForUdp(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_valid_for_udp(ConnectionWriter self, const Datagram datagram)
        
        /**
         * Returns true if the datagram is small enough to be sent over a UDP packet,
         * false otherwise.
         */
        """
        pass

    def is_immediate(self, ConnectionWriter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_immediate(ConnectionWriter self)
        
        /**
         * Returns true if the writer is an immediate writer, i.e.  it has no threads.
         */
        """
        pass

    def is_valid_for_udp(self, ConnectionWriter_self, const_Datagram_datagram): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_valid_for_udp(ConnectionWriter self, const Datagram datagram)
        
        /**
         * Returns true if the datagram is small enough to be sent over a UDP packet,
         * false otherwise.
         */
        """
        pass

    def send(self, const_ConnectionWriter_self, const_Datagram_datagram, const_Connection_connection): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        send(const ConnectionWriter self, const Datagram datagram, const Connection connection)
        send(const ConnectionWriter self, const Datagram datagram, const Connection connection, const NetAddress address, bool block)
        send(const ConnectionWriter self, const Datagram datagram, const Connection connection, bool block)
        
        /**
         * Enqueues a datagram for transmittal on the indicated socket.  Since the
         * host address is not specified with this form, this function should only be
         * used for sending TCP packets.  Use the other send() method for sending UDP
         * packets.
         *
         * Returns true if successful, false if there was an error.  In the normal,
         * threaded case, this function only returns false if the send queue is
         * filled; it's impossible to detect a transmission error at this point.
         *
         * If block is true, this will not return false if the send queue is filled;
         * instead, it will wait until there is space available.
         */
        
        /**
         * Enqueues a datagram for transmittal on the indicated socket.  This form of
         * the function allows the specification of a destination host address, and so
         * is appropriate for UDP packets.  Use the other send() method for sending
         * TCP packets.
         *
         * Returns true if successful, false if there was an error.  In the normal,
         * threaded case, this function only returns false if the send queue is
         * filled; it's impossible to detect a transmission error at this point.
         *
         * If block is true, this will not return false if the send queue is filled;
         * instead, it will wait until there is space available.
         */
        """
        pass

    def setMaxQueueSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_max_queue_size(const ConnectionWriter self, int max_size)
        
        /**
         * Limits the number of packets that may be pending on the outbound queue.
         * This only has an effect when using threads; if num_threads is 0, then all
         * packets are sent immediately.
         */
        """
        pass

    def setRawMode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_raw_mode(const ConnectionWriter self, bool mode)
        
        /**
         * Sets the ConnectionWriter into raw mode (or turns off raw mode).  In raw
         * mode, datagrams are not sent along with their headers; the bytes in the
         * datagram are simply sent down the pipe.
         *
         * Setting the ConnectionWriter to raw mode must be done with care.  This can
         * only be done when the matching ConnectionReader is also set to raw mode, or
         * when the ConnectionWriter is communicating to a process that does not
         * expect datagrams.
         */
        """
        pass

    def setTcpHeaderSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_tcp_header_size(const ConnectionWriter self, int tcp_header_size)
        
        /**
         * Sets the header size of TCP packets.  At the present, legal values for this
         * are 0, 2, or 4; this specifies the number of bytes to use encode the
         * datagram length at the start of each TCP datagram.  Sender and receiver
         * must independently agree on this.
         */
        """
        pass

    def set_max_queue_size(self, const_ConnectionWriter_self, int_max_size): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_max_queue_size(const ConnectionWriter self, int max_size)
        
        /**
         * Limits the number of packets that may be pending on the outbound queue.
         * This only has an effect when using threads; if num_threads is 0, then all
         * packets are sent immediately.
         */
        """
        pass

    def set_raw_mode(self, const_ConnectionWriter_self, bool_mode): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_raw_mode(const ConnectionWriter self, bool mode)
        
        /**
         * Sets the ConnectionWriter into raw mode (or turns off raw mode).  In raw
         * mode, datagrams are not sent along with their headers; the bytes in the
         * datagram are simply sent down the pipe.
         *
         * Setting the ConnectionWriter to raw mode must be done with care.  This can
         * only be done when the matching ConnectionReader is also set to raw mode, or
         * when the ConnectionWriter is communicating to a process that does not
         * expect datagrams.
         */
        """
        pass

    def set_tcp_header_size(self, const_ConnectionWriter_self, int_tcp_header_size): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_tcp_header_size(const ConnectionWriter self, int tcp_header_size)
        
        /**
         * Sets the header size of TCP packets.  At the present, legal values for this
         * are 0, 2, or 4; this specifies the number of bytes to use encode the
         * datagram length at the start of each TCP datagram.  Sender and receiver
         * must independently agree on this.
         */
        """
        pass

    def shutdown(self, const_ConnectionWriter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        shutdown(const ConnectionWriter self)
        
        /**
         * Stops all the threads and cleans them up.  This is called automatically by
         * the destructor, but it may be called explicitly before destruction.
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
        '__doc__': '/**\n * This class handles threaded delivery of datagrams to various TCP or UDP\n * sockets.\n *\n * A ConnectionWriter may define an arbitrary number of threads (0 or more) to\n * write its datagrams to sockets.  The number of threads is specified at\n * construction time and cannot be changed.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.ConnectionWriter' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE38A3D0>'
        'getCurrentQueueSize': None, # (!) real value is "<method 'getCurrentQueueSize' of 'panda3d.core.ConnectionWriter' objects>"
        'getManager': None, # (!) real value is "<method 'getManager' of 'panda3d.core.ConnectionWriter' objects>"
        'getMaxQueueSize': None, # (!) real value is "<method 'getMaxQueueSize' of 'panda3d.core.ConnectionWriter' objects>"
        'getNumThreads': None, # (!) real value is "<method 'getNumThreads' of 'panda3d.core.ConnectionWriter' objects>"
        'getRawMode': None, # (!) real value is "<method 'getRawMode' of 'panda3d.core.ConnectionWriter' objects>"
        'getTcpHeaderSize': None, # (!) real value is "<method 'getTcpHeaderSize' of 'panda3d.core.ConnectionWriter' objects>"
        'get_current_queue_size': None, # (!) real value is "<method 'get_current_queue_size' of 'panda3d.core.ConnectionWriter' objects>"
        'get_manager': None, # (!) real value is "<method 'get_manager' of 'panda3d.core.ConnectionWriter' objects>"
        'get_max_queue_size': None, # (!) real value is "<method 'get_max_queue_size' of 'panda3d.core.ConnectionWriter' objects>"
        'get_num_threads': None, # (!) real value is "<method 'get_num_threads' of 'panda3d.core.ConnectionWriter' objects>"
        'get_raw_mode': None, # (!) real value is "<method 'get_raw_mode' of 'panda3d.core.ConnectionWriter' objects>"
        'get_tcp_header_size': None, # (!) real value is "<method 'get_tcp_header_size' of 'panda3d.core.ConnectionWriter' objects>"
        'isImmediate': None, # (!) real value is "<method 'isImmediate' of 'panda3d.core.ConnectionWriter' objects>"
        'isValidForUdp': None, # (!) real value is "<method 'isValidForUdp' of 'panda3d.core.ConnectionWriter' objects>"
        'is_immediate': None, # (!) real value is "<method 'is_immediate' of 'panda3d.core.ConnectionWriter' objects>"
        'is_valid_for_udp': None, # (!) real value is "<method 'is_valid_for_udp' of 'panda3d.core.ConnectionWriter' objects>"
        'send': None, # (!) real value is "<method 'send' of 'panda3d.core.ConnectionWriter' objects>"
        'setMaxQueueSize': None, # (!) real value is "<method 'setMaxQueueSize' of 'panda3d.core.ConnectionWriter' objects>"
        'setRawMode': None, # (!) real value is "<method 'setRawMode' of 'panda3d.core.ConnectionWriter' objects>"
        'setTcpHeaderSize': None, # (!) real value is "<method 'setTcpHeaderSize' of 'panda3d.core.ConnectionWriter' objects>"
        'set_max_queue_size': None, # (!) real value is "<method 'set_max_queue_size' of 'panda3d.core.ConnectionWriter' objects>"
        'set_raw_mode': None, # (!) real value is "<method 'set_raw_mode' of 'panda3d.core.ConnectionWriter' objects>"
        'set_tcp_header_size': None, # (!) real value is "<method 'set_tcp_header_size' of 'panda3d.core.ConnectionWriter' objects>"
        'shutdown': None, # (!) real value is "<method 'shutdown' of 'panda3d.core.ConnectionWriter' objects>"
    }


