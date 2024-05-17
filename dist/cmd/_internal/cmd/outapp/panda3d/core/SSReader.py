# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class SSReader(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * An internal class for reading from a socket stream.  This serves as a base
     * class for both ISocketStream and SocketStream; its purpose is to minimize
     * redundant code between them.  Do not use it directly.
     */
    """
    def close(self, const_SSReader_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        close(const SSReader self)
        """
        pass

    def getTcpHeaderSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_tcp_header_size(SSReader self)
        
        /**
         * Returns the header size for datagrams.  See set_tcp_header_size().
         */
        """
        pass

    def get_tcp_header_size(self, SSReader_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_tcp_header_size(SSReader self)
        
        /**
         * Returns the header size for datagrams.  See set_tcp_header_size().
         */
        """
        pass

    def isClosed(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_closed(const SSReader self)
        """
        pass

    def is_closed(self, const_SSReader_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_closed(const SSReader self)
        """
        pass

    def receiveDatagram(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        receive_datagram(const SSReader self, Datagram dg)
        
        /**
         * Receives a datagram over the socket by expecting a little-endian 16-bit
         * byte count as a prefix.  If the socket stream is non-blocking, may return
         * false if the data is not available; otherwise, returns false only if the
         * socket closes.
         */
        """
        pass

    def receive_datagram(self, const_SSReader_self, Datagram_dg): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        receive_datagram(const SSReader self, Datagram dg)
        
        /**
         * Receives a datagram over the socket by expecting a little-endian 16-bit
         * byte count as a prefix.  If the socket stream is non-blocking, may return
         * false if the data is not available; otherwise, returns false only if the
         * socket closes.
         */
        """
        pass

    def setTcpHeaderSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_tcp_header_size(const SSReader self, int tcp_header_size)
        
        /**
         * Sets the header size for datagrams.  At the present, legal values for this
         * are 0, 2, or 4; this specifies the number of bytes to use encode the
         * datagram length at the start of each TCP datagram.  Sender and receiver
         * must independently agree on this.
         */
        """
        pass

    def set_tcp_header_size(self, const_SSReader_self, int_tcp_header_size): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_tcp_header_size(const SSReader self, int tcp_header_size)
        
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
        '__doc__': '/**\n * An internal class for reading from a socket stream.  This serves as a base\n * class for both ISocketStream and SocketStream; its purpose is to minimize\n * redundant code between them.  Do not use it directly.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.SSReader' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE26B8B0>'
        'close': None, # (!) real value is "<method 'close' of 'panda3d.core.SSReader' objects>"
        'getTcpHeaderSize': None, # (!) real value is "<method 'getTcpHeaderSize' of 'panda3d.core.SSReader' objects>"
        'get_tcp_header_size': None, # (!) real value is "<method 'get_tcp_header_size' of 'panda3d.core.SSReader' objects>"
        'isClosed': None, # (!) real value is "<method 'isClosed' of 'panda3d.core.SSReader' objects>"
        'is_closed': None, # (!) real value is "<method 'is_closed' of 'panda3d.core.SSReader' objects>"
        'receiveDatagram': None, # (!) real value is "<method 'receiveDatagram' of 'panda3d.core.SSReader' objects>"
        'receive_datagram': None, # (!) real value is "<method 'receive_datagram' of 'panda3d.core.SSReader' objects>"
        'setTcpHeaderSize': None, # (!) real value is "<method 'setTcpHeaderSize' of 'panda3d.core.SSReader' objects>"
        'set_tcp_header_size': None, # (!) real value is "<method 'set_tcp_header_size' of 'panda3d.core.SSReader' objects>"
    }


