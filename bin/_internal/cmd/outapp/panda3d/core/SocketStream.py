# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .iostream import iostream

from .SSReader import SSReader

from .SSWriter import SSWriter

class SocketStream(iostream, SSReader, SSWriter):
    """
    /**
     * A base class for iostreams that read and write to a (possibly non-blocking)
     * socket.
     */
    """
    def close(self, const_SocketStream_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        close(const SocketStream self)
        """
        pass

    def flush(self, const_SocketStream_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        flush(const SocketStream self)
        
        /**
         * Sends the most recently queued data now.  This only has meaning if
         * set_collect_tcp() has been set to true.
         */
        """
        pass

    def getTcpHeaderSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_tcp_header_size(SocketStream self)
        
        /**
         * Returns the header size for datagrams.  See set_tcp_header_size().
         */
        """
        pass

    def get_tcp_header_size(self, SocketStream_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_tcp_header_size(SocketStream self)
        
        /**
         * Returns the header size for datagrams.  See set_tcp_header_size().
         */
        """
        pass

    def isClosed(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_closed(const SocketStream self)
        """
        pass

    def is_closed(self, const_SocketStream_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_closed(const SocketStream self)
        """
        pass

    def setTcpHeaderSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_tcp_header_size(const SocketStream self, int tcp_header_size)
        
        /**
         * Sets the header size for datagrams.  At the present, legal values for this
         * are 0, 2, or 4; this specifies the number of bytes to use encode the
         * datagram length at the start of each TCP datagram.  Sender and receiver
         * must independently agree on this.
         */
        """
        pass

    def set_tcp_header_size(self, const_SocketStream_self, int_tcp_header_size): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_tcp_header_size(const SocketStream self, int tcp_header_size)
        
        /**
         * Sets the header size for datagrams.  At the present, legal values for this
         * are 0, 2, or 4; this specifies the number of bytes to use encode the
         * datagram length at the start of each TCP datagram.  Sender and receiver
         * must independently agree on this.
         */
        """
        pass

    def upcastToIostream(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_iostream(const SocketStream self)
        
        upcast from SocketStream to iostream
        """
        pass

    def upcastToSSReader(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_SSReader(const SocketStream self)
        
        upcast from SocketStream to SSReader
        """
        pass

    def upcastToSSWriter(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_SSWriter(const SocketStream self)
        
        upcast from SocketStream to SSWriter
        """
        pass

    def upcast_to_iostream(self, const_SocketStream_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_iostream(const SocketStream self)
        
        upcast from SocketStream to iostream
        """
        pass

    def upcast_to_SSReader(self, const_SocketStream_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_SSReader(const SocketStream self)
        
        upcast from SocketStream to SSReader
        """
        pass

    def upcast_to_SSWriter(self, const_SocketStream_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_SSWriter(const SocketStream self)
        
        upcast from SocketStream to SSWriter
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
        '__doc__': '/**\n * A base class for iostreams that read and write to a (possibly non-blocking)\n * socket.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.SocketStream' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE26C000>'
        'close': None, # (!) real value is "<method 'close' of 'panda3d.core.SocketStream' objects>"
        'flush': None, # (!) real value is "<method 'flush' of 'panda3d.core.SocketStream' objects>"
        'getTcpHeaderSize': None, # (!) real value is "<method 'getTcpHeaderSize' of 'panda3d.core.SocketStream' objects>"
        'get_tcp_header_size': None, # (!) real value is "<method 'get_tcp_header_size' of 'panda3d.core.SocketStream' objects>"
        'isClosed': None, # (!) real value is "<method 'isClosed' of 'panda3d.core.SocketStream' objects>"
        'is_closed': None, # (!) real value is "<method 'is_closed' of 'panda3d.core.SocketStream' objects>"
        'setTcpHeaderSize': None, # (!) real value is "<method 'setTcpHeaderSize' of 'panda3d.core.SocketStream' objects>"
        'set_tcp_header_size': None, # (!) real value is "<method 'set_tcp_header_size' of 'panda3d.core.SocketStream' objects>"
        'upcastToIostream': None, # (!) real value is "<method 'upcastToIostream' of 'panda3d.core.SocketStream' objects>"
        'upcastToSSReader': None, # (!) real value is "<method 'upcastToSSReader' of 'panda3d.core.SocketStream' objects>"
        'upcastToSSWriter': None, # (!) real value is "<method 'upcastToSSWriter' of 'panda3d.core.SocketStream' objects>"
        'upcast_to_SSReader': None, # (!) real value is "<method 'upcast_to_SSReader' of 'panda3d.core.SocketStream' objects>"
        'upcast_to_SSWriter': None, # (!) real value is "<method 'upcast_to_SSWriter' of 'panda3d.core.SocketStream' objects>"
        'upcast_to_iostream': None, # (!) real value is "<method 'upcast_to_iostream' of 'panda3d.core.SocketStream' objects>"
    }


