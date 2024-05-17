# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .IStreamWrapper import IStreamWrapper

from .OStreamWrapper import OStreamWrapper

class StreamWrapper(IStreamWrapper, OStreamWrapper):
    """
    /**
     * This class provides a locking wrapper around a combination ostream/istream
     * pointer.
     */
    """
    def getIostream(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_iostream(StreamWrapper self)
        
        /**
         * Returns the iostream this object is wrapping.
         */
        """
        pass

    def get_iostream(self, StreamWrapper_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_iostream(StreamWrapper self)
        
        /**
         * Returns the iostream this object is wrapping.
         */
        """
        pass

    def upcastToIStreamWrapper(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_IStreamWrapper(const StreamWrapper self)
        
        upcast from StreamWrapper to IStreamWrapper
        """
        pass

    def upcastToOStreamWrapper(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_OStreamWrapper(const StreamWrapper self)
        
        upcast from StreamWrapper to OStreamWrapper
        """
        pass

    def upcast_to_IStreamWrapper(self, const_StreamWrapper_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_IStreamWrapper(const StreamWrapper self)
        
        upcast from StreamWrapper to IStreamWrapper
        """
        pass

    def upcast_to_OStreamWrapper(self, const_StreamWrapper_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_OStreamWrapper(const StreamWrapper self)
        
        upcast from StreamWrapper to OStreamWrapper
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    iostream = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * This class provides a locking wrapper around a combination ostream/istream\n * pointer.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.StreamWrapper' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE264E00>'
        'getIostream': None, # (!) real value is "<method 'getIostream' of 'panda3d.core.StreamWrapper' objects>"
        'get_iostream': None, # (!) real value is "<method 'get_iostream' of 'panda3d.core.StreamWrapper' objects>"
        'iostream': None, # (!) real value is "<attribute 'iostream' of 'panda3d.core.StreamWrapper' objects>"
        'upcastToIStreamWrapper': None, # (!) real value is "<method 'upcastToIStreamWrapper' of 'panda3d.core.StreamWrapper' objects>"
        'upcastToOStreamWrapper': None, # (!) real value is "<method 'upcastToOStreamWrapper' of 'panda3d.core.StreamWrapper' objects>"
        'upcast_to_IStreamWrapper': None, # (!) real value is "<method 'upcast_to_IStreamWrapper' of 'panda3d.core.StreamWrapper' objects>"
        'upcast_to_OStreamWrapper': None, # (!) real value is "<method 'upcast_to_OStreamWrapper' of 'panda3d.core.StreamWrapper' objects>"
    }


