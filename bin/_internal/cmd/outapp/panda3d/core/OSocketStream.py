# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .ostream import ostream

from .SSWriter import SSWriter

class OSocketStream(ostream, SSWriter):
    """
    /**
     * A base class for ostreams that write to a (possibly non-blocking) socket.
     * It adds is_closed(), which can be called after any write operation fails to
     * check whether the socket has been closed, or whether more data may be sent
     * later.
     */
    """
    def close(self, const_OSocketStream_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        close(const OSocketStream self)
        """
        pass

    def flush(self, const_OSocketStream_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        flush(const OSocketStream self)
        
        /**
         * Sends the most recently queued data now.  This only has meaning if
         * set_collect_tcp() has been set to true.
         */
        """
        pass

    def isClosed(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_closed(const OSocketStream self)
        """
        pass

    def is_closed(self, const_OSocketStream_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_closed(const OSocketStream self)
        """
        pass

    def upcastToOstream(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_ostream(const OSocketStream self)
        
        upcast from OSocketStream to ostream
        """
        pass

    def upcastToSSWriter(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_SSWriter(const OSocketStream self)
        
        upcast from OSocketStream to SSWriter
        """
        pass

    def upcast_to_ostream(self, const_OSocketStream_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_ostream(const OSocketStream self)
        
        upcast from OSocketStream to ostream
        """
        pass

    def upcast_to_SSWriter(self, const_OSocketStream_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_SSWriter(const OSocketStream self)
        
        upcast from OSocketStream to SSWriter
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
        '__doc__': '/**\n * A base class for ostreams that write to a (possibly non-blocking) socket.\n * It adds is_closed(), which can be called after any write operation fails to\n * check whether the socket has been closed, or whether more data may be sent\n * later.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.OSocketStream' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE26BE30>'
        'close': None, # (!) real value is "<method 'close' of 'panda3d.core.OSocketStream' objects>"
        'flush': None, # (!) real value is "<method 'flush' of 'panda3d.core.OSocketStream' objects>"
        'isClosed': None, # (!) real value is "<method 'isClosed' of 'panda3d.core.OSocketStream' objects>"
        'is_closed': None, # (!) real value is "<method 'is_closed' of 'panda3d.core.OSocketStream' objects>"
        'upcastToOstream': None, # (!) real value is "<method 'upcastToOstream' of 'panda3d.core.OSocketStream' objects>"
        'upcastToSSWriter': None, # (!) real value is "<method 'upcastToSSWriter' of 'panda3d.core.OSocketStream' objects>"
        'upcast_to_SSWriter': None, # (!) real value is "<method 'upcast_to_SSWriter' of 'panda3d.core.OSocketStream' objects>"
        'upcast_to_ostream': None, # (!) real value is "<method 'upcast_to_ostream' of 'panda3d.core.OSocketStream' objects>"
    }


