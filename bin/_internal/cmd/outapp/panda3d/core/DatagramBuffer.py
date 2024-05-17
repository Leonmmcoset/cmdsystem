# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .DatagramSink import DatagramSink

from .DatagramGenerator import DatagramGenerator

class DatagramBuffer(DatagramSink, DatagramGenerator):
    """
    /**
     * This class can be used to write a series of datagrams into a memory buffer.
     * It acts as both a datagram sink and generator; you can fill it up with
     * datagrams and then read as many datagrams from it.
     *
     * This uses the same format as DatagramInputFile and DatagramOutputFile,
     * meaning that Datagram sizes are always stored little-endian.
     */
    """
    def clear(self, const_DatagramBuffer_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear(const DatagramBuffer self)
        
        /**
         * Clears the internal buffer.
         */
        """
        pass

    def upcastToDatagramGenerator(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_DatagramGenerator(const DatagramBuffer self)
        
        upcast from DatagramBuffer to DatagramGenerator
        """
        pass

    def upcastToDatagramSink(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_DatagramSink(const DatagramBuffer self)
        
        upcast from DatagramBuffer to DatagramSink
        """
        pass

    def upcast_to_DatagramGenerator(self, const_DatagramBuffer_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_DatagramGenerator(const DatagramBuffer self)
        
        upcast from DatagramBuffer to DatagramGenerator
        """
        pass

    def upcast_to_DatagramSink(self, const_DatagramBuffer_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_DatagramSink(const DatagramBuffer self)
        
        upcast from DatagramBuffer to DatagramSink
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * This class can be used to write a series of datagrams into a memory buffer.\n * It acts as both a datagram sink and generator; you can fill it up with\n * datagrams and then read as many datagrams from it.\n *\n * This uses the same format as DatagramInputFile and DatagramOutputFile,\n * meaning that Datagram sizes are always stored little-endian.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.DatagramBuffer' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE371D10>'
        'clear': None, # (!) real value is "<method 'clear' of 'panda3d.core.DatagramBuffer' objects>"
        'data': None, # (!) real value is "<attribute 'data' of 'panda3d.core.DatagramBuffer' objects>"
        'upcastToDatagramGenerator': None, # (!) real value is "<method 'upcastToDatagramGenerator' of 'panda3d.core.DatagramBuffer' objects>"
        'upcastToDatagramSink': None, # (!) real value is "<method 'upcastToDatagramSink' of 'panda3d.core.DatagramBuffer' objects>"
        'upcast_to_DatagramGenerator': None, # (!) real value is "<method 'upcast_to_DatagramGenerator' of 'panda3d.core.DatagramBuffer' objects>"
        'upcast_to_DatagramSink': None, # (!) real value is "<method 'upcast_to_DatagramSink' of 'panda3d.core.DatagramBuffer' objects>"
    }


