# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .StreamWrapperBase import StreamWrapperBase

class OStreamWrapper(StreamWrapperBase):
    """
    /**
     * This class provides a locking wrapper around an arbitrary ostream pointer.
     * A thread may use this class to perform an atomic seek/write operation.
     */
    """
    def getOstream(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_ostream(OStreamWrapper self)
        
        /**
         * Returns the ostream this object is wrapping.
         */
        """
        pass

    def get_ostream(self, OStreamWrapper_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_ostream(OStreamWrapper self)
        
        /**
         * Returns the ostream this object is wrapping.
         */
        """
        pass

    def upcastToStreamWrapperBase(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_StreamWrapperBase(const OStreamWrapper self)
        
        upcast from OStreamWrapper to StreamWrapperBase
        """
        pass

    def upcast_to_StreamWrapperBase(self, const_OStreamWrapper_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_StreamWrapperBase(const OStreamWrapper self)
        
        upcast from OStreamWrapper to StreamWrapperBase
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    ostream = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * This class provides a locking wrapper around an arbitrary ostream pointer.\n * A thread may use this class to perform an atomic seek/write operation.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.OStreamWrapper' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE264C30>'
        'getOstream': None, # (!) real value is "<method 'getOstream' of 'panda3d.core.OStreamWrapper' objects>"
        'get_ostream': None, # (!) real value is "<method 'get_ostream' of 'panda3d.core.OStreamWrapper' objects>"
        'ostream': None, # (!) real value is "<attribute 'ostream' of 'panda3d.core.OStreamWrapper' objects>"
        'upcastToStreamWrapperBase': None, # (!) real value is "<method 'upcastToStreamWrapperBase' of 'panda3d.core.OStreamWrapper' objects>"
        'upcast_to_StreamWrapperBase': None, # (!) real value is "<method 'upcast_to_StreamWrapperBase' of 'panda3d.core.OStreamWrapper' objects>"
    }


