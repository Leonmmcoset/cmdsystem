# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .ConnectionReader import ConnectionReader

class RecentConnectionReader(ConnectionReader):
    """
    /**
     * This flavor of ConnectionReader will read from its sockets and retain only
     * the single most recent datagram for inspection by client code.  It's useful
     * particularly for reading telemetry-type data from UDP sockets where you
     * don't care about getting every last socket, and in fact if the sockets are
     * coming too fast you'd prefer to skip some of them.
     *
     * This class will always create one thread for itself.
     */
    """
    def dataAvailable(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        data_available(const RecentConnectionReader self)
        
        /**
         * Returns true if a datagram is available on the queue; call get_data() to
         * extract the datagram.
         */
        """
        pass

    def data_available(self, const_RecentConnectionReader_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        data_available(const RecentConnectionReader self)
        
        /**
         * Returns true if a datagram is available on the queue; call get_data() to
         * extract the datagram.
         */
        """
        pass

    def getData(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_data(const RecentConnectionReader self, NetDatagram result)
        get_data(const RecentConnectionReader self, Datagram result)
        
        /**
         * If a previous call to data_available() returned true, this function will
         * return the datagram that has become available.
         *
         * The return value is true if a datagram was successfully returned, or false
         * if there was, in fact, no datagram available.  (This may happen if there
         * are multiple threads accessing the RecentConnectionReader).
         */
        
        /**
         * This flavor of RecentConnectionReader::get_data(), works like the other,
         * except that it only fills a Datagram object, not a NetDatagram object.
         * This means that the Datagram cannot be queried for its source Connection
         * and/or NetAddress, but it is useful in all other respects.
         */
        """
        pass

    def get_data(self, const_RecentConnectionReader_self, NetDatagram_result): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_data(const RecentConnectionReader self, NetDatagram result)
        get_data(const RecentConnectionReader self, Datagram result)
        
        /**
         * If a previous call to data_available() returned true, this function will
         * return the datagram that has become available.
         *
         * The return value is true if a datagram was successfully returned, or false
         * if there was, in fact, no datagram available.  (This may happen if there
         * are multiple threads accessing the RecentConnectionReader).
         */
        
        /**
         * This flavor of RecentConnectionReader::get_data(), works like the other,
         * except that it only fills a Datagram object, not a NetDatagram object.
         * This means that the Datagram cannot be queried for its source Connection
         * and/or NetAddress, but it is useful in all other respects.
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
        '__doc__': "/**\n * This flavor of ConnectionReader will read from its sockets and retain only\n * the single most recent datagram for inspection by client code.  It's useful\n * particularly for reading telemetry-type data from UDP sockets where you\n * don't care about getting every last socket, and in fact if the sockets are\n * coming too fast you'd prefer to skip some of them.\n *\n * This class will always create one thread for itself.\n */",
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.RecentConnectionReader' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE38B5F0>'
        'dataAvailable': None, # (!) real value is "<method 'dataAvailable' of 'panda3d.core.RecentConnectionReader' objects>"
        'data_available': None, # (!) real value is "<method 'data_available' of 'panda3d.core.RecentConnectionReader' objects>"
        'getData': None, # (!) real value is "<method 'getData' of 'panda3d.core.RecentConnectionReader' objects>"
        'get_data': None, # (!) real value is "<method 'get_data' of 'panda3d.core.RecentConnectionReader' objects>"
    }


