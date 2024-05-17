# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .DatagramGenerator import DatagramGenerator

from .ConnectionReader import ConnectionReader

from .QueuedReturn_Datagram import QueuedReturn_Datagram

class DatagramGeneratorNet(DatagramGenerator, ConnectionReader, QueuedReturn_Datagram):
    """
    /**
     * This class provides datagrams one-at-a-time as read directly from the net,
     * via a TCP connection.  If a datagram is not available, get_datagram() will
     * block until one is.
     */
    """
    def getDatagram(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_datagram(const DatagramGeneratorNet self, Datagram data)
        
        // Inherited from DatagramGenerator
        
        /**
         * Reads the next datagram from the stream.  Blocks until a datagram is
         * available.  Returns true on success, false on stream closed or error.
         */
        """
        pass

    def get_datagram(self, const_DatagramGeneratorNet_self, Datagram_data): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_datagram(const DatagramGeneratorNet self, Datagram data)
        
        // Inherited from DatagramGenerator
        
        /**
         * Reads the next datagram from the stream.  Blocks until a datagram is
         * available.  Returns true on success, false on stream closed or error.
         */
        """
        pass

    def isEof(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_eof(const DatagramGeneratorNet self)
        
        /**
         * Returns true if the stream has been closed normally.  This test may only be
         * made after a call to get_datagram() has failed.
         */
        """
        pass

    def isError(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_error(const DatagramGeneratorNet self)
        
        /**
         * Returns true if the stream has an error condition.
         */
        """
        pass

    def is_eof(self, const_DatagramGeneratorNet_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_eof(const DatagramGeneratorNet self)
        
        /**
         * Returns true if the stream has been closed normally.  This test may only be
         * made after a call to get_datagram() has failed.
         */
        """
        pass

    def is_error(self, const_DatagramGeneratorNet_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_error(const DatagramGeneratorNet self)
        
        /**
         * Returns true if the stream has an error condition.
         */
        """
        pass

    def upcastToConnectionReader(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_ConnectionReader(const DatagramGeneratorNet self)
        
        upcast from DatagramGeneratorNet to ConnectionReader
        """
        pass

    def upcastToDatagramGenerator(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_DatagramGenerator(const DatagramGeneratorNet self)
        
        upcast from DatagramGeneratorNet to DatagramGenerator
        """
        pass

    def upcastToQueuedReturnDatagram(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_QueuedReturn_Datagram(const DatagramGeneratorNet self)
        
        upcast from DatagramGeneratorNet to QueuedReturn< Datagram >
        """
        pass

    def upcast_to_ConnectionReader(self, const_DatagramGeneratorNet_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_ConnectionReader(const DatagramGeneratorNet self)
        
        upcast from DatagramGeneratorNet to ConnectionReader
        """
        pass

    def upcast_to_DatagramGenerator(self, const_DatagramGeneratorNet_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_DatagramGenerator(const DatagramGeneratorNet self)
        
        upcast from DatagramGeneratorNet to DatagramGenerator
        """
        pass

    def upcast_to_QueuedReturn_Datagram(self, const_DatagramGeneratorNet_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_QueuedReturn_Datagram(const DatagramGeneratorNet self)
        
        upcast from DatagramGeneratorNet to QueuedReturn< Datagram >
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
        '__doc__': '/**\n * This class provides datagrams one-at-a-time as read directly from the net,\n * via a TCP connection.  If a datagram is not available, get_datagram() will\n * block until one is.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.DatagramGeneratorNet' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE38A5A0>'
        'getDatagram': None, # (!) real value is "<method 'getDatagram' of 'panda3d.core.DatagramGeneratorNet' objects>"
        'get_datagram': None, # (!) real value is "<method 'get_datagram' of 'panda3d.core.DatagramGeneratorNet' objects>"
        'isEof': None, # (!) real value is "<method 'isEof' of 'panda3d.core.DatagramGeneratorNet' objects>"
        'isError': None, # (!) real value is "<method 'isError' of 'panda3d.core.DatagramGeneratorNet' objects>"
        'is_eof': None, # (!) real value is "<method 'is_eof' of 'panda3d.core.DatagramGeneratorNet' objects>"
        'is_error': None, # (!) real value is "<method 'is_error' of 'panda3d.core.DatagramGeneratorNet' objects>"
        'upcastToConnectionReader': None, # (!) real value is "<method 'upcastToConnectionReader' of 'panda3d.core.DatagramGeneratorNet' objects>"
        'upcastToDatagramGenerator': None, # (!) real value is "<method 'upcastToDatagramGenerator' of 'panda3d.core.DatagramGeneratorNet' objects>"
        'upcastToQueuedReturnDatagram': None, # (!) real value is "<method 'upcastToQueuedReturnDatagram' of 'panda3d.core.DatagramGeneratorNet' objects>"
        'upcast_to_ConnectionReader': None, # (!) real value is "<method 'upcast_to_ConnectionReader' of 'panda3d.core.DatagramGeneratorNet' objects>"
        'upcast_to_DatagramGenerator': None, # (!) real value is "<method 'upcast_to_DatagramGenerator' of 'panda3d.core.DatagramGeneratorNet' objects>"
        'upcast_to_QueuedReturn_Datagram': None, # (!) real value is "<method 'upcast_to_QueuedReturn_Datagram' of 'panda3d.core.DatagramGeneratorNet' objects>"
    }


