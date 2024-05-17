# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .istream import istream

from .SSReader import SSReader

class ISocketStream(istream, SSReader):
    """
    /**
     * This is a base class for istreams implemented in Panda that read from a
     * (possibly non-blocking) socket.  It adds is_closed(), which can be called
     * after an eof condition to check whether the socket has been closed, or
     * whether more data may be available later.
     */
    """
    def close(self, const_ISocketStream_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        close(const ISocketStream self)
        """
        pass

    def getReadState(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_read_state(const ISocketStream self)
        """
        pass

    def get_read_state(self, const_ISocketStream_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_read_state(const ISocketStream self)
        """
        pass

    def isClosed(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_closed(const ISocketStream self)
        """
        pass

    def is_closed(self, const_ISocketStream_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_closed(const ISocketStream self)
        """
        pass

    def upcastToIstream(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_istream(const ISocketStream self)
        
        upcast from ISocketStream to istream
        """
        pass

    def upcastToSSReader(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_SSReader(const ISocketStream self)
        
        upcast from ISocketStream to SSReader
        """
        pass

    def upcast_to_istream(self, const_ISocketStream_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_istream(const ISocketStream self)
        
        upcast from ISocketStream to istream
        """
        pass

    def upcast_to_SSReader(self, const_ISocketStream_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_SSReader(const ISocketStream self)
        
        upcast from ISocketStream to SSReader
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
        'RSComplete': 2,
        'RSError': 3,
        'RSInitial': 0,
        'RSReading': 1,
        'RS_complete': 2,
        'RS_error': 3,
        'RS_initial': 0,
        'RS_reading': 1,
        '__doc__': '/**\n * This is a base class for istreams implemented in Panda that read from a\n * (possibly non-blocking) socket.  It adds is_closed(), which can be called\n * after an eof condition to check whether the socket has been closed, or\n * whether more data may be available later.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.ISocketStream' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE26BC60>'
        'close': None, # (!) real value is "<method 'close' of 'panda3d.core.ISocketStream' objects>"
        'getReadState': None, # (!) real value is "<method 'getReadState' of 'panda3d.core.ISocketStream' objects>"
        'get_read_state': None, # (!) real value is "<method 'get_read_state' of 'panda3d.core.ISocketStream' objects>"
        'isClosed': None, # (!) real value is "<method 'isClosed' of 'panda3d.core.ISocketStream' objects>"
        'is_closed': None, # (!) real value is "<method 'is_closed' of 'panda3d.core.ISocketStream' objects>"
        'upcastToIstream': None, # (!) real value is "<method 'upcastToIstream' of 'panda3d.core.ISocketStream' objects>"
        'upcastToSSReader': None, # (!) real value is "<method 'upcastToSSReader' of 'panda3d.core.ISocketStream' objects>"
        'upcast_to_SSReader': None, # (!) real value is "<method 'upcast_to_SSReader' of 'panda3d.core.ISocketStream' objects>"
        'upcast_to_istream': None, # (!) real value is "<method 'upcast_to_istream' of 'panda3d.core.ISocketStream' objects>"
    }
    RSComplete = 2
    RSError = 3
    RSInitial = 0
    RSReading = 1
    RS_complete = 2
    RS_error = 3
    RS_initial = 0
    RS_reading = 1


