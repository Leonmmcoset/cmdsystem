# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .iostream import iostream

class StringStream(iostream):
    """
    /**
     * A bi-directional stream object that reads and writes data to an internal
     * buffer, which can be retrieved and/or set as a string in Python 2 or a
     * bytes object in Python 3.
     */
    """
    def clearData(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_data(const StringStream self)
        
        /**
         * Empties the buffer.
         */
        """
        pass

    def clear_data(self, const_StringStream_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_data(const StringStream self)
        
        /**
         * Empties the buffer.
         */
        """
        pass

    def getData(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_data(const StringStream self)
        
        /**
         * Returns the contents of the data stream as a string.
         */
        """
        pass

    def getDataSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_data_size(const StringStream self)
        
        /**
         * Returns the number of characters available to be read from the data stream.
         */
        """
        pass

    def get_data(self, const_StringStream_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_data(const StringStream self)
        
        /**
         * Returns the contents of the data stream as a string.
         */
        """
        pass

    def get_data_size(self, const_StringStream_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_data_size(const StringStream self)
        
        /**
         * Returns the number of characters available to be read from the data stream.
         */
        """
        pass

    def setData(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_data(const StringStream self, object data)
        
        /**
         * Replaces the contents of the data stream.  This implicitly reseeks to 0.
         */
        
        /**
         * Replaces the contents of the data stream.  This implicitly reseeks to 0.
         */
        """
        pass

    def set_data(self, const_StringStream_self, object_data): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_data(const StringStream self, object data)
        
        /**
         * Replaces the contents of the data stream.  This implicitly reseeks to 0.
         */
        
        /**
         * Replaces the contents of the data stream.  This implicitly reseeks to 0.
         */
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
        '__doc__': '/**\n * A bi-directional stream object that reads and writes data to an internal\n * buffer, which can be retrieved and/or set as a string in Python 2 or a\n * bytes object in Python 3.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.StringStream' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE26DD00>'
        'clearData': None, # (!) real value is "<method 'clearData' of 'panda3d.core.StringStream' objects>"
        'clear_data': None, # (!) real value is "<method 'clear_data' of 'panda3d.core.StringStream' objects>"
        'data': None, # (!) real value is "<attribute 'data' of 'panda3d.core.StringStream' objects>"
        'getData': None, # (!) real value is "<method 'getData' of 'panda3d.core.StringStream' objects>"
        'getDataSize': None, # (!) real value is "<method 'getDataSize' of 'panda3d.core.StringStream' objects>"
        'get_data': None, # (!) real value is "<method 'get_data' of 'panda3d.core.StringStream' objects>"
        'get_data_size': None, # (!) real value is "<method 'get_data_size' of 'panda3d.core.StringStream' objects>"
        'setData': None, # (!) real value is "<method 'setData' of 'panda3d.core.StringStream' objects>"
        'set_data': None, # (!) real value is "<method 'set_data' of 'panda3d.core.StringStream' objects>"
    }


