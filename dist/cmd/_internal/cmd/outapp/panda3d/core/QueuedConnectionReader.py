# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .ConnectionReader import ConnectionReader

from .QueuedReturn_NetDatagram import QueuedReturn_NetDatagram

class QueuedConnectionReader(ConnectionReader, QueuedReturn_NetDatagram):
    """
    /**
     * This flavor of ConnectionReader will read from its sockets and queue up all
     * of the datagrams read for later receipt by the client code.  This class is
     * useful for client code that doesn't want to deal with threading and is
     * willing to poll for datagrams at its convenience.
     */
    """
    def dataAvailable(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        data_available(const QueuedConnectionReader self)
        
        /**
         * Returns true if a datagram is available on the queue; call get_data() to
         * extract the datagram.
         */
        """
        pass

    def data_available(self, const_QueuedConnectionReader_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        data_available(const QueuedConnectionReader self)
        
        /**
         * Returns true if a datagram is available on the queue; call get_data() to
         * extract the datagram.
         */
        """
        pass

    def getData(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_data(const QueuedConnectionReader self, NetDatagram result)
        get_data(const QueuedConnectionReader self, Datagram result)
        
        /**
         * If a previous call to data_available() returned true, this function will
         * return the datagram that has become available.
         *
         * The return value is true if a datagram was successfully returned, or false
         * if there was, in fact, no datagram available.  (This may happen if there
         * are multiple threads accessing the QueuedConnectionReader).
         */
        
        /**
         * This flavor of QueuedConnectionReader::get_data(), works like the other,
         * except that it only fills a Datagram object, not a NetDatagram object.
         * This means that the Datagram cannot be queried for its source Connection
         * and/or NetAddress, but it is useful in all other respects.
         */
        """
        pass

    def get_data(self, const_QueuedConnectionReader_self, NetDatagram_result): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_data(const QueuedConnectionReader self, NetDatagram result)
        get_data(const QueuedConnectionReader self, Datagram result)
        
        /**
         * If a previous call to data_available() returned true, this function will
         * return the datagram that has become available.
         *
         * The return value is true if a datagram was successfully returned, or false
         * if there was, in fact, no datagram available.  (This may happen if there
         * are multiple threads accessing the QueuedConnectionReader).
         */
        
        /**
         * This flavor of QueuedConnectionReader::get_data(), works like the other,
         * except that it only fills a Datagram object, not a NetDatagram object.
         * This means that the Datagram cannot be queried for its source Connection
         * and/or NetAddress, but it is useful in all other respects.
         */
        """
        pass

    def upcastToConnectionReader(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_ConnectionReader(const QueuedConnectionReader self)
        
        upcast from QueuedConnectionReader to ConnectionReader
        """
        pass

    def upcastToQueuedReturnNetDatagram(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_QueuedReturn_NetDatagram(const QueuedConnectionReader self)
        
        upcast from QueuedConnectionReader to QueuedReturn< NetDatagram >
        """
        pass

    def upcast_to_ConnectionReader(self, const_QueuedConnectionReader_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_ConnectionReader(const QueuedConnectionReader self)
        
        upcast from QueuedConnectionReader to ConnectionReader
        """
        pass

    def upcast_to_QueuedReturn_NetDatagram(self, const_QueuedConnectionReader_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_QueuedReturn_NetDatagram(const QueuedConnectionReader self)
        
        upcast from QueuedConnectionReader to QueuedReturn< NetDatagram >
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
        '__doc__': "/**\n * This flavor of ConnectionReader will read from its sockets and queue up all\n * of the datagrams read for later receipt by the client code.  This class is\n * useful for client code that doesn't want to deal with threading and is\n * willing to poll for datagrams at its convenience.\n */",
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.QueuedConnectionReader' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE38B250>'
        'dataAvailable': None, # (!) real value is "<method 'dataAvailable' of 'panda3d.core.QueuedConnectionReader' objects>"
        'data_available': None, # (!) real value is "<method 'data_available' of 'panda3d.core.QueuedConnectionReader' objects>"
        'getData': None, # (!) real value is "<method 'getData' of 'panda3d.core.QueuedConnectionReader' objects>"
        'get_data': None, # (!) real value is "<method 'get_data' of 'panda3d.core.QueuedConnectionReader' objects>"
        'upcastToConnectionReader': None, # (!) real value is "<method 'upcastToConnectionReader' of 'panda3d.core.QueuedConnectionReader' objects>"
        'upcastToQueuedReturnNetDatagram': None, # (!) real value is "<method 'upcastToQueuedReturnNetDatagram' of 'panda3d.core.QueuedConnectionReader' objects>"
        'upcast_to_ConnectionReader': None, # (!) real value is "<method 'upcast_to_ConnectionReader' of 'panda3d.core.QueuedConnectionReader' objects>"
        'upcast_to_QueuedReturn_NetDatagram': None, # (!) real value is "<method 'upcast_to_QueuedReturn_NetDatagram' of 'panda3d.core.QueuedConnectionReader' objects>"
    }


