# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class SSWriter(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * An internal class for writing to a socket stream.  This serves as a base
     * class for both OSocketStream and SocketStream; its purpose is to minimize
     * redundant code between them.  Do not use it directly.
     */
    """
    def close(self, const_SSWriter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        close(const SSWriter self)
        """
        pass

    def considerFlush(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        consider_flush(const SSWriter self)
        
        /**
         * Sends the most recently queued data if enough time has elapsed.  This only
         * has meaning if set_collect_tcp() has been set to true.
         */
        """
        pass

    def consider_flush(self, const_SSWriter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        consider_flush(const SSWriter self)
        
        /**
         * Sends the most recently queued data if enough time has elapsed.  This only
         * has meaning if set_collect_tcp() has been set to true.
         */
        """
        pass

    def flush(self, const_SSWriter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        flush(const SSWriter self)
        
        /**
         * Sends the most recently queued data now.  This only has meaning if
         * set_collect_tcp() has been set to true.
         */
        """
        pass

    def getCollectTcp(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_collect_tcp(SSWriter self)
        
        /**
         * Returns the current setting of "collect-tcp" mode.  See set_collect_tcp().
         */
        """
        pass

    def getCollectTcpInterval(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_collect_tcp_interval(SSWriter self)
        
        /**
         * Returns the interval in time, in seconds, for which to hold TCP packets
         * before sending all of the recently received packets at once.  This only has
         * meaning if "collect-tcp" mode is enabled; see set_collect_tcp().
         */
        """
        pass

    def getTcpHeaderSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_tcp_header_size(SSWriter self)
        
        /**
         * Returns the header size for datagrams.  See set_tcp_header_size().
         */
        """
        pass

    def get_collect_tcp(self, SSWriter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_collect_tcp(SSWriter self)
        
        /**
         * Returns the current setting of "collect-tcp" mode.  See set_collect_tcp().
         */
        """
        pass

    def get_collect_tcp_interval(self, SSWriter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_collect_tcp_interval(SSWriter self)
        
        /**
         * Returns the interval in time, in seconds, for which to hold TCP packets
         * before sending all of the recently received packets at once.  This only has
         * meaning if "collect-tcp" mode is enabled; see set_collect_tcp().
         */
        """
        pass

    def get_tcp_header_size(self, SSWriter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_tcp_header_size(SSWriter self)
        
        /**
         * Returns the header size for datagrams.  See set_tcp_header_size().
         */
        """
        pass

    def isClosed(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_closed(const SSWriter self)
        """
        pass

    def is_closed(self, const_SSWriter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_closed(const SSWriter self)
        """
        pass

    def sendDatagram(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        send_datagram(const SSWriter self, const Datagram dg)
        
        /**
         * Transmits the indicated datagram over the socket by prepending it with a
         * little-endian 16-bit byte count.  Does not return until the data is sent or
         * the connection is closed, even if the socket stream is non-blocking.
         */
        """
        pass

    def send_datagram(self, const_SSWriter_self, const_Datagram_dg): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        send_datagram(const SSWriter self, const Datagram dg)
        
        /**
         * Transmits the indicated datagram over the socket by prepending it with a
         * little-endian 16-bit byte count.  Does not return until the data is sent or
         * the connection is closed, even if the socket stream is non-blocking.
         */
        """
        pass

    def setCollectTcp(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_collect_tcp(const SSWriter self, bool collect_tcp)
        
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
        set_collect_tcp_interval(const SSWriter self, double interval)
        
        /**
         * Specifies the interval in time, in seconds, for which to hold TCP packets
         * before sending all of the recently received packets at once.  This only has
         * meaning if "collect-tcp" mode is enabled; see set_collect_tcp().
         */
        """
        pass

    def setTcpHeaderSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_tcp_header_size(const SSWriter self, int tcp_header_size)
        
        /**
         * Sets the header size for datagrams.  At the present, legal values for this
         * are 0, 2, or 4; this specifies the number of bytes to use encode the
         * datagram length at the start of each TCP datagram.  Sender and receiver
         * must independently agree on this.
         */
        """
        pass

    def set_collect_tcp(self, const_SSWriter_self, bool_collect_tcp): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_collect_tcp(const SSWriter self, bool collect_tcp)
        
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

    def set_collect_tcp_interval(self, const_SSWriter_self, double_interval): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_collect_tcp_interval(const SSWriter self, double interval)
        
        /**
         * Specifies the interval in time, in seconds, for which to hold TCP packets
         * before sending all of the recently received packets at once.  This only has
         * meaning if "collect-tcp" mode is enabled; see set_collect_tcp().
         */
        """
        pass

    def set_tcp_header_size(self, const_SSWriter_self, int_tcp_header_size): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_tcp_header_size(const SSWriter self, int tcp_header_size)
        
        /**
         * Sets the header size for datagrams.  At the present, legal values for this
         * are 0, 2, or 4; this specifies the number of bytes to use encode the
         * datagram length at the start of each TCP datagram.  Sender and receiver
         * must independently agree on this.
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
        '__doc__': '/**\n * An internal class for writing to a socket stream.  This serves as a base\n * class for both OSocketStream and SocketStream; its purpose is to minimize\n * redundant code between them.  Do not use it directly.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.SSWriter' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE26BA90>'
        'close': None, # (!) real value is "<method 'close' of 'panda3d.core.SSWriter' objects>"
        'considerFlush': None, # (!) real value is "<method 'considerFlush' of 'panda3d.core.SSWriter' objects>"
        'consider_flush': None, # (!) real value is "<method 'consider_flush' of 'panda3d.core.SSWriter' objects>"
        'flush': None, # (!) real value is "<method 'flush' of 'panda3d.core.SSWriter' objects>"
        'getCollectTcp': None, # (!) real value is "<method 'getCollectTcp' of 'panda3d.core.SSWriter' objects>"
        'getCollectTcpInterval': None, # (!) real value is "<method 'getCollectTcpInterval' of 'panda3d.core.SSWriter' objects>"
        'getTcpHeaderSize': None, # (!) real value is "<method 'getTcpHeaderSize' of 'panda3d.core.SSWriter' objects>"
        'get_collect_tcp': None, # (!) real value is "<method 'get_collect_tcp' of 'panda3d.core.SSWriter' objects>"
        'get_collect_tcp_interval': None, # (!) real value is "<method 'get_collect_tcp_interval' of 'panda3d.core.SSWriter' objects>"
        'get_tcp_header_size': None, # (!) real value is "<method 'get_tcp_header_size' of 'panda3d.core.SSWriter' objects>"
        'isClosed': None, # (!) real value is "<method 'isClosed' of 'panda3d.core.SSWriter' objects>"
        'is_closed': None, # (!) real value is "<method 'is_closed' of 'panda3d.core.SSWriter' objects>"
        'sendDatagram': None, # (!) real value is "<method 'sendDatagram' of 'panda3d.core.SSWriter' objects>"
        'send_datagram': None, # (!) real value is "<method 'send_datagram' of 'panda3d.core.SSWriter' objects>"
        'setCollectTcp': None, # (!) real value is "<method 'setCollectTcp' of 'panda3d.core.SSWriter' objects>"
        'setCollectTcpInterval': None, # (!) real value is "<method 'setCollectTcpInterval' of 'panda3d.core.SSWriter' objects>"
        'setTcpHeaderSize': None, # (!) real value is "<method 'setTcpHeaderSize' of 'panda3d.core.SSWriter' objects>"
        'set_collect_tcp': None, # (!) real value is "<method 'set_collect_tcp' of 'panda3d.core.SSWriter' objects>"
        'set_collect_tcp_interval': None, # (!) real value is "<method 'set_collect_tcp_interval' of 'panda3d.core.SSWriter' objects>"
        'set_tcp_header_size': None, # (!) real value is "<method 'set_tcp_header_size' of 'panda3d.core.SSWriter' objects>"
    }


