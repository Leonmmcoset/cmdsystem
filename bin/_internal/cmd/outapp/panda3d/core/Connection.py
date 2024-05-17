# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .ReferenceCount import ReferenceCount

class Connection(ReferenceCount):
    """
    /**
     * Represents a single TCP or UDP socket for input or output.
     */
    """
    def considerFlush(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        consider_flush(const Connection self)
        
        /**
         * Sends the most recently queued TCP datagram(s) if enough time has elapsed.
         * This only has meaning if set_collect_tcp() has been set to true.
         */
        """
        pass

    def consider_flush(self, const_Connection_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        consider_flush(const Connection self)
        
        /**
         * Sends the most recently queued TCP datagram(s) if enough time has elapsed.
         * This only has meaning if set_collect_tcp() has been set to true.
         */
        """
        pass

    def flush(self, const_Connection_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        flush(const Connection self)
        
        /**
         * Sends the most recently queued TCP datagram(s) now.  This only has meaning
         * if set_collect_tcp() has been set to true.
         */
        """
        pass

    def getAddress(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_address(Connection self)
        
        /**
         * Returns the address bound to this connection, if it is a TCP connection.
         */
        """
        pass

    def getCollectTcp(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_collect_tcp(Connection self)
        
        /**
         * Returns the current setting of "collect-tcp" mode.  See set_collect_tcp().
         */
        """
        pass

    def getCollectTcpInterval(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_collect_tcp_interval(Connection self)
        
        /**
         * Returns the interval in time, in seconds, for which to hold TCP packets
         * before sending all of the recently received packets at once.  This only has
         * meaning if "collect-tcp" mode is enabled; see set_collect_tcp().
         */
        """
        pass

    def getManager(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_manager(Connection self)
        
        /**
         * Returns a pointer to the ConnectionManager object that serves this
         * connection.
         */
        """
        pass

    def getSocket(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_socket(Connection self)
        
        /**
         * Returns the internal Socket_IP that defines the connection.
         */
        """
        pass

    def get_address(self, Connection_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_address(Connection self)
        
        /**
         * Returns the address bound to this connection, if it is a TCP connection.
         */
        """
        pass

    def get_collect_tcp(self, Connection_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_collect_tcp(Connection self)
        
        /**
         * Returns the current setting of "collect-tcp" mode.  See set_collect_tcp().
         */
        """
        pass

    def get_collect_tcp_interval(self, Connection_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_collect_tcp_interval(Connection self)
        
        /**
         * Returns the interval in time, in seconds, for which to hold TCP packets
         * before sending all of the recently received packets at once.  This only has
         * meaning if "collect-tcp" mode is enabled; see set_collect_tcp().
         */
        """
        pass

    def get_manager(self, Connection_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_manager(Connection self)
        
        /**
         * Returns a pointer to the ConnectionManager object that serves this
         * connection.
         */
        """
        pass

    def get_socket(self, Connection_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_socket(Connection self)
        
        /**
         * Returns the internal Socket_IP that defines the connection.
         */
        """
        pass

    def setCollectTcp(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_collect_tcp(const Connection self, bool collect_tcp)
        
        /**
         * Enables or disables "collect-tcp" mode.  In this mode, individual TCP
         * packets are not sent immediately, but rather they are collected together
         * and accumulated to be sent periodically as one larger TCP packet.  This
         * cuts down on overhead from the TCP/IP protocol, especially if many small
         * packets need to be sent on the same connection, but it introduces
         * additional latency (since packets must be held before they can be sent).
         *
         * See set_collect_tcp_interval() to specify the interval of time for which to
         * hold packets before sending them.
         *
         * If you enable this mode, you may also need to periodically call
         * consider_flush() to flush the queue if no packets have been sent recently.
         */
        """
        pass

    def setCollectTcpInterval(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_collect_tcp_interval(const Connection self, double interval)
        
        /**
         * Specifies the interval in time, in seconds, for which to hold TCP packets
         * before sending all of the recently received packets at once.  This only has
         * meaning if "collect-tcp" mode is enabled; see set_collect_tcp().
         */
        """
        pass

    def setIpTimeToLive(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_ip_time_to_live(const Connection self, int ttl)
        
        /**
         * Sets IP time-to-live.
         */
        """
        pass

    def setIpTypeOfService(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_ip_type_of_service(const Connection self, int tos)
        
        /**
         * Sets IP type-of-service and precedence.
         */
        """
        pass

    def setKeepAlive(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_keep_alive(const Connection self, bool flag)
        
        /**
         * Sets whether the connection is periodically tested to see if it is still
         * alive.
         */
        """
        pass

    def setLinger(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_linger(const Connection self, bool flag, double time)
        
        // Socket options.  void set_nonblock(bool flag);
        
        /**
         * Sets the time to linger on close if data is present.  If flag is false,
         * when you close a socket with data available the system attempts to deliver
         * the data to the peer (the default behavior).  If flag is false but time is
         * zero, the system discards any undelivered data when you close the socket.
         * If flag is false but time is nonzero, the system waits up to time seconds
         * to deliver the data.
         */
        """
        pass

    def setMaxSegment(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_max_segment(const Connection self, int size)
        
        /**
         * Sets the maximum segment size.
         */
        """
        pass

    def setNoDelay(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_no_delay(const Connection self, bool flag)
        
        /**
         * If flag is true, this disables the Nagle algorithm, and prevents delaying
         * of send to coalesce packets.
         */
        """
        pass

    def setRecvBufferSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_recv_buffer_size(const Connection self, int size)
        
        /**
         * Sets the size of the receive buffer, in bytes.
         */
        """
        pass

    def setReuseAddr(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_reuse_addr(const Connection self, bool flag)
        
        /**
         * Sets whether local address reuse is allowed.
         */
        """
        pass

    def setSendBufferSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_send_buffer_size(const Connection self, int size)
        
        /**
         * Sets the size of the send buffer, in bytes.
         */
        """
        pass

    def set_collect_tcp(self, const_Connection_self, bool_collect_tcp): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_collect_tcp(const Connection self, bool collect_tcp)
        
        /**
         * Enables or disables "collect-tcp" mode.  In this mode, individual TCP
         * packets are not sent immediately, but rather they are collected together
         * and accumulated to be sent periodically as one larger TCP packet.  This
         * cuts down on overhead from the TCP/IP protocol, especially if many small
         * packets need to be sent on the same connection, but it introduces
         * additional latency (since packets must be held before they can be sent).
         *
         * See set_collect_tcp_interval() to specify the interval of time for which to
         * hold packets before sending them.
         *
         * If you enable this mode, you may also need to periodically call
         * consider_flush() to flush the queue if no packets have been sent recently.
         */
        """
        pass

    def set_collect_tcp_interval(self, const_Connection_self, double_interval): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_collect_tcp_interval(const Connection self, double interval)
        
        /**
         * Specifies the interval in time, in seconds, for which to hold TCP packets
         * before sending all of the recently received packets at once.  This only has
         * meaning if "collect-tcp" mode is enabled; see set_collect_tcp().
         */
        """
        pass

    def set_ip_time_to_live(self, const_Connection_self, int_ttl): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_ip_time_to_live(const Connection self, int ttl)
        
        /**
         * Sets IP time-to-live.
         */
        """
        pass

    def set_ip_type_of_service(self, const_Connection_self, int_tos): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_ip_type_of_service(const Connection self, int tos)
        
        /**
         * Sets IP type-of-service and precedence.
         */
        """
        pass

    def set_keep_alive(self, const_Connection_self, bool_flag): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_keep_alive(const Connection self, bool flag)
        
        /**
         * Sets whether the connection is periodically tested to see if it is still
         * alive.
         */
        """
        pass

    def set_linger(self, const_Connection_self, bool_flag, double_time): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_linger(const Connection self, bool flag, double time)
        
        // Socket options.  void set_nonblock(bool flag);
        
        /**
         * Sets the time to linger on close if data is present.  If flag is false,
         * when you close a socket with data available the system attempts to deliver
         * the data to the peer (the default behavior).  If flag is false but time is
         * zero, the system discards any undelivered data when you close the socket.
         * If flag is false but time is nonzero, the system waits up to time seconds
         * to deliver the data.
         */
        """
        pass

    def set_max_segment(self, const_Connection_self, int_size): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_max_segment(const Connection self, int size)
        
        /**
         * Sets the maximum segment size.
         */
        """
        pass

    def set_no_delay(self, const_Connection_self, bool_flag): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_no_delay(const Connection self, bool flag)
        
        /**
         * If flag is true, this disables the Nagle algorithm, and prevents delaying
         * of send to coalesce packets.
         */
        """
        pass

    def set_recv_buffer_size(self, const_Connection_self, int_size): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_recv_buffer_size(const Connection self, int size)
        
        /**
         * Sets the size of the receive buffer, in bytes.
         */
        """
        pass

    def set_reuse_addr(self, const_Connection_self, bool_flag): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_reuse_addr(const Connection self, bool flag)
        
        /**
         * Sets whether local address reuse is allowed.
         */
        """
        pass

    def set_send_buffer_size(self, const_Connection_self, int_size): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_send_buffer_size(const Connection self, int size)
        
        /**
         * Sets the size of the send buffer, in bytes.
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
        '__doc__': '/**\n * Represents a single TCP or UDP socket for input or output.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.Connection' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE3898F0>'
        'considerFlush': None, # (!) real value is "<method 'considerFlush' of 'panda3d.core.Connection' objects>"
        'consider_flush': None, # (!) real value is "<method 'consider_flush' of 'panda3d.core.Connection' objects>"
        'flush': None, # (!) real value is "<method 'flush' of 'panda3d.core.Connection' objects>"
        'getAddress': None, # (!) real value is "<method 'getAddress' of 'panda3d.core.Connection' objects>"
        'getCollectTcp': None, # (!) real value is "<method 'getCollectTcp' of 'panda3d.core.Connection' objects>"
        'getCollectTcpInterval': None, # (!) real value is "<method 'getCollectTcpInterval' of 'panda3d.core.Connection' objects>"
        'getManager': None, # (!) real value is "<method 'getManager' of 'panda3d.core.Connection' objects>"
        'getSocket': None, # (!) real value is "<method 'getSocket' of 'panda3d.core.Connection' objects>"
        'get_address': None, # (!) real value is "<method 'get_address' of 'panda3d.core.Connection' objects>"
        'get_collect_tcp': None, # (!) real value is "<method 'get_collect_tcp' of 'panda3d.core.Connection' objects>"
        'get_collect_tcp_interval': None, # (!) real value is "<method 'get_collect_tcp_interval' of 'panda3d.core.Connection' objects>"
        'get_manager': None, # (!) real value is "<method 'get_manager' of 'panda3d.core.Connection' objects>"
        'get_socket': None, # (!) real value is "<method 'get_socket' of 'panda3d.core.Connection' objects>"
        'setCollectTcp': None, # (!) real value is "<method 'setCollectTcp' of 'panda3d.core.Connection' objects>"
        'setCollectTcpInterval': None, # (!) real value is "<method 'setCollectTcpInterval' of 'panda3d.core.Connection' objects>"
        'setIpTimeToLive': None, # (!) real value is "<method 'setIpTimeToLive' of 'panda3d.core.Connection' objects>"
        'setIpTypeOfService': None, # (!) real value is "<method 'setIpTypeOfService' of 'panda3d.core.Connection' objects>"
        'setKeepAlive': None, # (!) real value is "<method 'setKeepAlive' of 'panda3d.core.Connection' objects>"
        'setLinger': None, # (!) real value is "<method 'setLinger' of 'panda3d.core.Connection' objects>"
        'setMaxSegment': None, # (!) real value is "<method 'setMaxSegment' of 'panda3d.core.Connection' objects>"
        'setNoDelay': None, # (!) real value is "<method 'setNoDelay' of 'panda3d.core.Connection' objects>"
        'setRecvBufferSize': None, # (!) real value is "<method 'setRecvBufferSize' of 'panda3d.core.Connection' objects>"
        'setReuseAddr': None, # (!) real value is "<method 'setReuseAddr' of 'panda3d.core.Connection' objects>"
        'setSendBufferSize': None, # (!) real value is "<method 'setSendBufferSize' of 'panda3d.core.Connection' objects>"
        'set_collect_tcp': None, # (!) real value is "<method 'set_collect_tcp' of 'panda3d.core.Connection' objects>"
        'set_collect_tcp_interval': None, # (!) real value is "<method 'set_collect_tcp_interval' of 'panda3d.core.Connection' objects>"
        'set_ip_time_to_live': None, # (!) real value is "<method 'set_ip_time_to_live' of 'panda3d.core.Connection' objects>"
        'set_ip_type_of_service': None, # (!) real value is "<method 'set_ip_type_of_service' of 'panda3d.core.Connection' objects>"
        'set_keep_alive': None, # (!) real value is "<method 'set_keep_alive' of 'panda3d.core.Connection' objects>"
        'set_linger': None, # (!) real value is "<method 'set_linger' of 'panda3d.core.Connection' objects>"
        'set_max_segment': None, # (!) real value is "<method 'set_max_segment' of 'panda3d.core.Connection' objects>"
        'set_no_delay': None, # (!) real value is "<method 'set_no_delay' of 'panda3d.core.Connection' objects>"
        'set_recv_buffer_size': None, # (!) real value is "<method 'set_recv_buffer_size' of 'panda3d.core.Connection' objects>"
        'set_reuse_addr': None, # (!) real value is "<method 'set_reuse_addr' of 'panda3d.core.Connection' objects>"
        'set_send_buffer_size': None, # (!) real value is "<method 'set_send_buffer_size' of 'panda3d.core.Connection' objects>"
    }


