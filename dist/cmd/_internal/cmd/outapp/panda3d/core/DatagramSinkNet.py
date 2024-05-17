# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .DatagramSink import DatagramSink

from .ConnectionWriter import ConnectionWriter

class DatagramSinkNet(DatagramSink, ConnectionWriter):
    """
    /**
     * This class accepts datagrams one-at-a-time and sends them over the net, via
     * a TCP connection.
     */
    """
    def flush(self, const_DatagramSinkNet_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        flush(const DatagramSinkNet self)
        
        /**
         * Ensures that all datagrams previously written will be visible on the
         * stream.
         */
        """
        pass

    def getTarget(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_target(DatagramSinkNet self)
        
        /**
         * Returns the current target Connection, or NULL if the target has not yet
         * been set.  See set_target().
         */
        """
        pass

    def get_target(self, DatagramSinkNet_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_target(DatagramSinkNet self)
        
        /**
         * Returns the current target Connection, or NULL if the target has not yet
         * been set.  See set_target().
         */
        """
        pass

    def isError(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_error(const DatagramSinkNet self)
        
        /**
         * Returns true if there is an error on the target connection, or if the
         * target has never been set.
         */
        """
        pass

    def is_error(self, const_DatagramSinkNet_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_error(const DatagramSinkNet self)
        
        /**
         * Returns true if there is an error on the target connection, or if the
         * target has never been set.
         */
        """
        pass

    def putDatagram(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        put_datagram(const DatagramSinkNet self, const Datagram data)
        
        // Inherited from DatagramSink
        
        /**
         * Sends the given datagram to the target.  Returns true on success, false if
         * there is an error.  Blocks if necessary until the target is ready.
         */
        """
        pass

    def put_datagram(self, const_DatagramSinkNet_self, const_Datagram_data): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        put_datagram(const DatagramSinkNet self, const Datagram data)
        
        // Inherited from DatagramSink
        
        /**
         * Sends the given datagram to the target.  Returns true on success, false if
         * there is an error.  Blocks if necessary until the target is ready.
         */
        """
        pass

    def setTarget(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_target(const DatagramSinkNet self, Connection connection)
        
        /**
         * Specifies the Connection that will receive all future Datagrams sent.
         */
        """
        pass

    def set_target(self, const_DatagramSinkNet_self, Connection_connection): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_target(const DatagramSinkNet self, Connection connection)
        
        /**
         * Specifies the Connection that will receive all future Datagrams sent.
         */
        """
        pass

    def upcastToConnectionWriter(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_ConnectionWriter(const DatagramSinkNet self)
        
        upcast from DatagramSinkNet to ConnectionWriter
        """
        pass

    def upcastToDatagramSink(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_DatagramSink(const DatagramSinkNet self)
        
        upcast from DatagramSinkNet to DatagramSink
        """
        pass

    def upcast_to_ConnectionWriter(self, const_DatagramSinkNet_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_ConnectionWriter(const DatagramSinkNet self)
        
        upcast from DatagramSinkNet to ConnectionWriter
        """
        pass

    def upcast_to_DatagramSink(self, const_DatagramSinkNet_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_DatagramSink(const DatagramSinkNet self)
        
        upcast from DatagramSinkNet to DatagramSink
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
        '__doc__': '/**\n * This class accepts datagrams one-at-a-time and sends them over the net, via\n * a TCP connection.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.DatagramSinkNet' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE38A940>'
        'flush': None, # (!) real value is "<method 'flush' of 'panda3d.core.DatagramSinkNet' objects>"
        'getTarget': None, # (!) real value is "<method 'getTarget' of 'panda3d.core.DatagramSinkNet' objects>"
        'get_target': None, # (!) real value is "<method 'get_target' of 'panda3d.core.DatagramSinkNet' objects>"
        'isError': None, # (!) real value is "<method 'isError' of 'panda3d.core.DatagramSinkNet' objects>"
        'is_error': None, # (!) real value is "<method 'is_error' of 'panda3d.core.DatagramSinkNet' objects>"
        'putDatagram': None, # (!) real value is "<method 'putDatagram' of 'panda3d.core.DatagramSinkNet' objects>"
        'put_datagram': None, # (!) real value is "<method 'put_datagram' of 'panda3d.core.DatagramSinkNet' objects>"
        'setTarget': None, # (!) real value is "<method 'setTarget' of 'panda3d.core.DatagramSinkNet' objects>"
        'set_target': None, # (!) real value is "<method 'set_target' of 'panda3d.core.DatagramSinkNet' objects>"
        'upcastToConnectionWriter': None, # (!) real value is "<method 'upcastToConnectionWriter' of 'panda3d.core.DatagramSinkNet' objects>"
        'upcastToDatagramSink': None, # (!) real value is "<method 'upcastToDatagramSink' of 'panda3d.core.DatagramSinkNet' objects>"
        'upcast_to_ConnectionWriter': None, # (!) real value is "<method 'upcast_to_ConnectionWriter' of 'panda3d.core.DatagramSinkNet' objects>"
        'upcast_to_DatagramSink': None, # (!) real value is "<method 'upcast_to_DatagramSink' of 'panda3d.core.DatagramSinkNet' objects>"
    }


