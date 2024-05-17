# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class Ramfile(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * An in-memory buffer specifically designed for downloading files to memory.
     */
    """
    def clear(self, const_Ramfile_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear(const Ramfile self)
        
        /**
         * Empties the current buffer contents.
         */
        """
        pass

    def getData(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_data(Ramfile self)
        
        /**
         * Returns the entire buffer contents as a string, regardless of the current
         * data pointer.
         */
        """
        pass

    def getDataSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_data_size(Ramfile self)
        
        /**
         * Returns the size of the entire buffer contents.
         */
        """
        pass

    def get_data(self, Ramfile_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_data(Ramfile self)
        
        /**
         * Returns the entire buffer contents as a string, regardless of the current
         * data pointer.
         */
        """
        pass

    def get_data_size(self, Ramfile_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_data_size(Ramfile self)
        
        /**
         * Returns the size of the entire buffer contents.
         */
        """
        pass

    def read(self, const_Ramfile_self, int_length): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        read(const Ramfile self, int length)
        
        /**
         * Extracts and returns the indicated number of characters from the current
         * data pointer, and advances the data pointer.  If the data pointer exceeds
         * the end of the buffer, returns empty string.
         *
         * The interface here is intentionally designed to be similar to that for
         * Python's file.read() function.
         */
        """
        pass

    def readline(self, const_Ramfile_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        readline(const Ramfile self)
        
        /**
         * Assumes the stream represents a text file, and extracts one line up to and
         * including the trailing newline character.  Returns empty string when the
         * end of file is reached.
         *
         * The interface here is intentionally designed to be similar to that for
         * Python's file.readline() function.
         */
        """
        pass

    def readlines(self, const_Ramfile_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        readlines(const Ramfile self)
        """
        pass

    def seek(self, const_Ramfile_self, int_pos): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        seek(const Ramfile self, int pos)
        
        /**
         * Moves the data pointer to the indicated byte position.  It is not an error
         * to move the pointer past the end of data.
         */
        """
        pass

    def tell(self, Ramfile_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        tell(Ramfile self)
        
        /**
         * Returns the current data pointer position as a byte offset from the
         * beginning of the stream.
         */
        """
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __deepcopy__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.Ramfile' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.Ramfile' objects>"
        '__doc__': '/**\n * An in-memory buffer specifically designed for downloading files to memory.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.Ramfile' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE278430>'
        'clear': None, # (!) real value is "<method 'clear' of 'panda3d.core.Ramfile' objects>"
        'getData': None, # (!) real value is "<method 'getData' of 'panda3d.core.Ramfile' objects>"
        'getDataSize': None, # (!) real value is "<method 'getDataSize' of 'panda3d.core.Ramfile' objects>"
        'get_data': None, # (!) real value is "<method 'get_data' of 'panda3d.core.Ramfile' objects>"
        'get_data_size': None, # (!) real value is "<method 'get_data_size' of 'panda3d.core.Ramfile' objects>"
        'read': None, # (!) real value is "<method 'read' of 'panda3d.core.Ramfile' objects>"
        'readline': None, # (!) real value is "<method 'readline' of 'panda3d.core.Ramfile' objects>"
        'readlines': None, # (!) real value is "<method 'readlines' of 'panda3d.core.Ramfile' objects>"
        'seek': None, # (!) real value is "<method 'seek' of 'panda3d.core.Ramfile' objects>"
        'tell': None, # (!) real value is "<method 'tell' of 'panda3d.core.Ramfile' objects>"
    }


