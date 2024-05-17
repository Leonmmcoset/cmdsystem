# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .RecorderBase import RecorderBase

from .ReferenceCount import ReferenceCount

class SocketStreamRecorder(RecorderBase, ReferenceCount):
    """
    /**
     * Records any data received from the indicated socket stream.  On playback,
     * it will act as if the incoming data is coming over the wire again even if
     * an actual connection is not available.
     *
     * Outbound data will not be recorded, but will be sent straight through to
     * the socket if it is connected, or silently ignored if it is not.
     */
    """
    def close(self, const_SocketStreamRecorder_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        close(const SocketStreamRecorder self)
        
        /**
         * See SocketStream::close().
         */
        """
        pass

    def considerFlush(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        consider_flush(const SocketStreamRecorder self)
        
        /**
         * See SocketStream::consider_flush()
         */
        """
        pass

    def consider_flush(self, const_SocketStreamRecorder_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        consider_flush(const SocketStreamRecorder self)
        
        /**
         * See SocketStream::consider_flush()
         */
        """
        pass

    def flush(self, const_SocketStreamRecorder_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        flush(const SocketStreamRecorder self)
        
        /**
         * See SocketStream::flush()
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getCollectTcp(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_collect_tcp(SocketStreamRecorder self)
        
        /**
         * See SocketStream::get_collect_tcp().
         */
        """
        pass

    def getCollectTcpInterval(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_collect_tcp_interval(SocketStreamRecorder self)
        
        /**
         * See SocketStream::get_collect_tcp_interval().
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_collect_tcp(self, SocketStreamRecorder_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_collect_tcp(SocketStreamRecorder self)
        
        /**
         * See SocketStream::get_collect_tcp().
         */
        """
        pass

    def get_collect_tcp_interval(self, SocketStreamRecorder_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_collect_tcp_interval(SocketStreamRecorder self)
        
        /**
         * See SocketStream::get_collect_tcp_interval().
         */
        """
        pass

    def isClosed(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_closed(const SocketStreamRecorder self)
        
        /**
         * See SocketStream::is_closed().
         */
        """
        pass

    def is_closed(self, const_SocketStreamRecorder_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_closed(const SocketStreamRecorder self)
        
        /**
         * See SocketStream::is_closed().
         */
        """
        pass

    def receiveDatagram(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        receive_datagram(const SocketStreamRecorder self, Datagram dg)
        
        /**
         * Receives a datagram over the socket by expecting a little-endian 16-bit
         * byte count as a prefix.  If the socket stream is non-blocking, may return
         * false if the data is not available; otherwise, returns false only if the
         * socket closes.
         */
        """
        pass

    def receive_datagram(self, const_SocketStreamRecorder_self, Datagram_dg): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        receive_datagram(const SocketStreamRecorder self, Datagram dg)
        
        /**
         * Receives a datagram over the socket by expecting a little-endian 16-bit
         * byte count as a prefix.  If the socket stream is non-blocking, may return
         * false if the data is not available; otherwise, returns false only if the
         * socket closes.
         */
        """
        pass

    def sendDatagram(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        send_datagram(const SocketStreamRecorder self, const Datagram dg)
        
        /**
         * See SocketStream::send_datagram().
         */
        """
        pass

    def send_datagram(self, const_SocketStreamRecorder_self, const_Datagram_dg): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        send_datagram(const SocketStreamRecorder self, const Datagram dg)
        
        /**
         * See SocketStream::send_datagram().
         */
        """
        pass

    def setCollectTcp(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_collect_tcp(const SocketStreamRecorder self, bool collect_tcp)
        
        /**
         * See SocketStream::set_collect_tcp().
         */
        """
        pass

    def setCollectTcpInterval(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_collect_tcp_interval(const SocketStreamRecorder self, double interval)
        
        /**
         * See SocketStream::set_collect_tcp_interval().
         */
        """
        pass

    def set_collect_tcp(self, const_SocketStreamRecorder_self, bool_collect_tcp): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_collect_tcp(const SocketStreamRecorder self, bool collect_tcp)
        
        /**
         * See SocketStream::set_collect_tcp().
         */
        """
        pass

    def set_collect_tcp_interval(self, const_SocketStreamRecorder_self, double_interval): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_collect_tcp_interval(const SocketStreamRecorder self, double interval)
        
        /**
         * See SocketStream::set_collect_tcp_interval().
         */
        """
        pass

    def upcastToRecorderBase(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_RecorderBase(const SocketStreamRecorder self)
        
        upcast from SocketStreamRecorder to RecorderBase
        """
        pass

    def upcastToReferenceCount(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_ReferenceCount(const SocketStreamRecorder self)
        
        upcast from SocketStreamRecorder to ReferenceCount
        """
        pass

    def upcast_to_RecorderBase(self, const_SocketStreamRecorder_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_RecorderBase(const SocketStreamRecorder self)
        
        upcast from SocketStreamRecorder to RecorderBase
        """
        pass

    def upcast_to_ReferenceCount(self, const_SocketStreamRecorder_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_ReferenceCount(const SocketStreamRecorder self)
        
        upcast from SocketStreamRecorder to ReferenceCount
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
        '__doc__': '/**\n * Records any data received from the indicated socket stream.  On playback,\n * it will act as if the incoming data is coming over the wire again even if\n * an actual connection is not available.\n *\n * Outbound data will not be recorded, but will be sent straight through to\n * the socket if it is connected, or silently ignored if it is not.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.SocketStreamRecorder' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2853C0>'
        'close': None, # (!) real value is "<method 'close' of 'panda3d.core.SocketStreamRecorder' objects>"
        'considerFlush': None, # (!) real value is "<method 'considerFlush' of 'panda3d.core.SocketStreamRecorder' objects>"
        'consider_flush': None, # (!) real value is "<method 'consider_flush' of 'panda3d.core.SocketStreamRecorder' objects>"
        'flush': None, # (!) real value is "<method 'flush' of 'panda3d.core.SocketStreamRecorder' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2853C0>)>'
        'getCollectTcp': None, # (!) real value is "<method 'getCollectTcp' of 'panda3d.core.SocketStreamRecorder' objects>"
        'getCollectTcpInterval': None, # (!) real value is "<method 'getCollectTcpInterval' of 'panda3d.core.SocketStreamRecorder' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2853C0>)>'
        'get_collect_tcp': None, # (!) real value is "<method 'get_collect_tcp' of 'panda3d.core.SocketStreamRecorder' objects>"
        'get_collect_tcp_interval': None, # (!) real value is "<method 'get_collect_tcp_interval' of 'panda3d.core.SocketStreamRecorder' objects>"
        'isClosed': None, # (!) real value is "<method 'isClosed' of 'panda3d.core.SocketStreamRecorder' objects>"
        'is_closed': None, # (!) real value is "<method 'is_closed' of 'panda3d.core.SocketStreamRecorder' objects>"
        'receiveDatagram': None, # (!) real value is "<method 'receiveDatagram' of 'panda3d.core.SocketStreamRecorder' objects>"
        'receive_datagram': None, # (!) real value is "<method 'receive_datagram' of 'panda3d.core.SocketStreamRecorder' objects>"
        'sendDatagram': None, # (!) real value is "<method 'sendDatagram' of 'panda3d.core.SocketStreamRecorder' objects>"
        'send_datagram': None, # (!) real value is "<method 'send_datagram' of 'panda3d.core.SocketStreamRecorder' objects>"
        'setCollectTcp': None, # (!) real value is "<method 'setCollectTcp' of 'panda3d.core.SocketStreamRecorder' objects>"
        'setCollectTcpInterval': None, # (!) real value is "<method 'setCollectTcpInterval' of 'panda3d.core.SocketStreamRecorder' objects>"
        'set_collect_tcp': None, # (!) real value is "<method 'set_collect_tcp' of 'panda3d.core.SocketStreamRecorder' objects>"
        'set_collect_tcp_interval': None, # (!) real value is "<method 'set_collect_tcp_interval' of 'panda3d.core.SocketStreamRecorder' objects>"
        'upcastToRecorderBase': None, # (!) real value is "<method 'upcastToRecorderBase' of 'panda3d.core.SocketStreamRecorder' objects>"
        'upcastToReferenceCount': None, # (!) real value is "<method 'upcastToReferenceCount' of 'panda3d.core.SocketStreamRecorder' objects>"
        'upcast_to_RecorderBase': None, # (!) real value is "<method 'upcast_to_RecorderBase' of 'panda3d.core.SocketStreamRecorder' objects>"
        'upcast_to_ReferenceCount': None, # (!) real value is "<method 'upcast_to_ReferenceCount' of 'panda3d.core.SocketStreamRecorder' objects>"
    }


