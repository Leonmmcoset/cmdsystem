# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .StreamWrapperBase import StreamWrapperBase

class IStreamWrapper(StreamWrapperBase):
    """
    /**
     * This class provides a locking wrapper around an arbitrary istream pointer.
     * A thread may use this class to perform an atomic seek/read/gcount
     * operation.
     */
    """
    def getIstream(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_istream(IStreamWrapper self)
        
        /**
         * Returns the istream this object is wrapping.
         */
        """
        pass

    def get_istream(self, IStreamWrapper_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_istream(IStreamWrapper self)
        
        /**
         * Returns the istream this object is wrapping.
         */
        """
        pass

    def upcastToStreamWrapperBase(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_StreamWrapperBase(const IStreamWrapper self)
        
        upcast from IStreamWrapper to StreamWrapperBase
        """
        pass

    def upcast_to_StreamWrapperBase(self, const_IStreamWrapper_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_StreamWrapperBase(const IStreamWrapper self)
        
        upcast from IStreamWrapper to StreamWrapperBase
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    istream = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * This class provides a locking wrapper around an arbitrary istream pointer.\n * A thread may use this class to perform an atomic seek/read/gcount\n * operation.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.IStreamWrapper' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE264A60>'
        'getIstream': None, # (!) real value is "<method 'getIstream' of 'panda3d.core.IStreamWrapper' objects>"
        'get_istream': None, # (!) real value is "<method 'get_istream' of 'panda3d.core.IStreamWrapper' objects>"
        'istream': None, # (!) real value is "<attribute 'istream' of 'panda3d.core.IStreamWrapper' objects>"
        'upcastToStreamWrapperBase': None, # (!) real value is "<method 'upcastToStreamWrapperBase' of 'panda3d.core.IStreamWrapper' objects>"
        'upcast_to_StreamWrapperBase': None, # (!) real value is "<method 'upcast_to_StreamWrapperBase' of 'panda3d.core.IStreamWrapper' objects>"
    }


