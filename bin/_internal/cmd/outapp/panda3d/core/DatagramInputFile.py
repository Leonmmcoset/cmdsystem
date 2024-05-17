# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .DatagramGenerator import DatagramGenerator

class DatagramInputFile(DatagramGenerator):
    """
    /**
     * This class can be used to read a binary file that consists of an arbitrary
     * header followed by a number of datagrams.
     */
    """
    def close(self, const_DatagramInputFile_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        close(const DatagramInputFile self)
        
        /**
         * Closes the file.  This is also implicitly done when the DatagramInputFile
         * destructs.
         */
        """
        pass

    def getStream(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_stream(const DatagramInputFile self)
        
        /**
         * Returns the istream represented by the input file.
         */
        """
        pass

    def get_stream(self, const_DatagramInputFile_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_stream(const DatagramInputFile self)
        
        /**
         * Returns the istream represented by the input file.
         */
        """
        pass

    def open(self, const_DatagramInputFile_self, istream_in, const_Filename_filename): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        open(const DatagramInputFile self, istream in, const Filename filename)
        open(const DatagramInputFile self, const FileReference file)
        open(const DatagramInputFile self, const Filename filename)
        
        /**
         * Opens the indicated filename for reading.  Returns true on success, false
         * on failure.
         */
        
        /**
         * Opens the indicated filename for reading.  Returns true on success, false
         * on failure.
         */
        
        /**
         * Starts reading from the indicated stream.  Returns true on success, false
         * on failure.  The DatagramInputFile does not take ownership of the stream;
         * you are responsible for closing or deleting it when you are done.
         */
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
        '__doc__': '/**\n * This class can be used to read a binary file that consists of an arbitrary\n * header followed by a number of datagrams.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.DatagramInputFile' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE371EE0>'
        'close': None, # (!) real value is "<method 'close' of 'panda3d.core.DatagramInputFile' objects>"
        'getStream': None, # (!) real value is "<method 'getStream' of 'panda3d.core.DatagramInputFile' objects>"
        'get_stream': None, # (!) real value is "<method 'get_stream' of 'panda3d.core.DatagramInputFile' objects>"
        'open': None, # (!) real value is "<method 'open' of 'panda3d.core.DatagramInputFile' objects>"
    }


