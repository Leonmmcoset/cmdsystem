# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .DatagramSink import DatagramSink

class DatagramOutputFile(DatagramSink):
    """
    /**
     * This class can be used to write a binary file that consists of an arbitrary
     * header followed by a number of datagrams.
     */
    """
    def close(self, const_DatagramOutputFile_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        close(const DatagramOutputFile self)
        
        /**
         * Closes the file.  This is also implicitly done when the DatagramOutputFile
         * destructs.
         */
        """
        pass

    def open(self, const_DatagramOutputFile_self, ostream_out, const_Filename_filename): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        open(const DatagramOutputFile self, ostream out, const Filename filename)
        open(const DatagramOutputFile self, const FileReference file)
        open(const DatagramOutputFile self, const Filename filename)
        
        /**
         * Opens the indicated filename for writing.  Returns true on success, false
         * on failure.
         */
        
        /**
         * Opens the indicated filename for writing.  Returns true if successful,
         * false on failure.
         */
        
        /**
         * Starts writing to the indicated stream.  Returns true on success, false on
         * failure.  The DatagramOutputFile does not take ownership of the stream; you
         * are responsible for closing or deleting it when you are done.
         */
        """
        pass

    def writeHeader(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        write_header(const DatagramOutputFile self, bytes header)
        write_header(const DatagramOutputFile self, str header)
        
        /**
         * Writes a sequence of bytes to the beginning of the datagram file.  This may
         * be called any number of times after the file has been opened and before the
         * first datagram is written.  It may not be called once the first datagram is
         * written.
         */
        
        /**
         * Writes a sequence of bytes to the beginning of the datagram file.  This may
         * be called any number of times after the file has been opened and before the
         * first datagram is written.  It may not be called once the first datagram is
         * written.
         */
        """
        pass

    def write_header(self, const_DatagramOutputFile_self, bytes_header): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write_header(const DatagramOutputFile self, bytes header)
        write_header(const DatagramOutputFile self, str header)
        
        /**
         * Writes a sequence of bytes to the beginning of the datagram file.  This may
         * be called any number of times after the file has been opened and before the
         * first datagram is written.  It may not be called once the first datagram is
         * written.
         */
        
        /**
         * Writes a sequence of bytes to the beginning of the datagram file.  This may
         * be called any number of times after the file has been opened and before the
         * first datagram is written.  It may not be called once the first datagram is
         * written.
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    stream = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * This class can be used to write a binary file that consists of an arbitrary\n * header followed by a number of datagrams.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.DatagramOutputFile' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE3720B0>'
        'close': None, # (!) real value is "<method 'close' of 'panda3d.core.DatagramOutputFile' objects>"
        'open': None, # (!) real value is "<method 'open' of 'panda3d.core.DatagramOutputFile' objects>"
        'stream': None, # (!) real value is "<attribute 'stream' of 'panda3d.core.DatagramOutputFile' objects>"
        'writeHeader': None, # (!) real value is "<method 'writeHeader' of 'panda3d.core.DatagramOutputFile' objects>"
        'write_header': None, # (!) real value is "<method 'write_header' of 'panda3d.core.DatagramOutputFile' objects>"
    }


