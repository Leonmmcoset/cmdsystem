# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class DatagramSink(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * This class defines the abstract interface to sending datagrams to any
     * target, whether it be into a file or across the net
     */
    """
    def copyDatagram(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        copy_datagram(const DatagramSink self, SubfileInfo result, const Filename filename)
        copy_datagram(const DatagramSink self, SubfileInfo result, const SubfileInfo source)
        
        /**
         * Copies the file data from the entire indicated file (via the vfs) as the
         * next datagram.  This is intended to support potentially very large
         * datagrams.
         *
         * Returns true on success, false on failure or if this method is
         * unimplemented.  On true, fills "result" with the information that
         * references the copied file, if possible.
         */
        
        /**
         * Copies the file data from the range of the indicated file (outside of the
         * vfs) as the next datagram.  This is intended to support potentially very
         * large datagrams.
         *
         * Returns true on success, false on failure or if this method is
         * unimplemented.  On true, fills "result" with the information that
         * references the copied file, if possible.
         */
        """
        pass

    def copy_datagram(self, const_DatagramSink_self, SubfileInfo_result, const_Filename_filename): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        copy_datagram(const DatagramSink self, SubfileInfo result, const Filename filename)
        copy_datagram(const DatagramSink self, SubfileInfo result, const SubfileInfo source)
        
        /**
         * Copies the file data from the entire indicated file (via the vfs) as the
         * next datagram.  This is intended to support potentially very large
         * datagrams.
         *
         * Returns true on success, false on failure or if this method is
         * unimplemented.  On true, fills "result" with the information that
         * references the copied file, if possible.
         */
        
        /**
         * Copies the file data from the range of the indicated file (outside of the
         * vfs) as the next datagram.  This is intended to support potentially very
         * large datagrams.
         *
         * Returns true on success, false on failure or if this method is
         * unimplemented.  On true, fills "result" with the information that
         * references the copied file, if possible.
         */
        """
        pass

    def flush(self, const_DatagramSink_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        flush(const DatagramSink self)
        """
        pass

    def getFile(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_file(const DatagramSink self)
        
        /**
         * Returns the FileReference that provides the target for these datagrams, if
         * any, or NULL if the datagrams do not written to a file on disk.
         */
        """
        pass

    def getFilename(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_filename(const DatagramSink self)
        
        /**
         * Returns the filename that provides the target for these datagrams, if any,
         * or empty string if the datagrams do not get written to a file on disk.
         */
        """
        pass

    def getFilePos(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_file_pos(const DatagramSink self)
        
        /**
         * Returns the current file position within the data stream, if any, or 0 if
         * the file position is not meaningful or cannot be determined.
         *
         * For DatagramSinks that return a meaningful file position, this will be
         * pointing to the first byte following the datagram returned after a call to
         * put_datagram().
         */
        """
        pass

    def get_file(self, const_DatagramSink_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_file(const DatagramSink self)
        
        /**
         * Returns the FileReference that provides the target for these datagrams, if
         * any, or NULL if the datagrams do not written to a file on disk.
         */
        """
        pass

    def get_filename(self, const_DatagramSink_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_filename(const DatagramSink self)
        
        /**
         * Returns the filename that provides the target for these datagrams, if any,
         * or empty string if the datagrams do not get written to a file on disk.
         */
        """
        pass

    def get_file_pos(self, const_DatagramSink_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_file_pos(const DatagramSink self)
        
        /**
         * Returns the current file position within the data stream, if any, or 0 if
         * the file position is not meaningful or cannot be determined.
         *
         * For DatagramSinks that return a meaningful file position, this will be
         * pointing to the first byte following the datagram returned after a call to
         * put_datagram().
         */
        """
        pass

    def isError(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_error(const DatagramSink self)
        """
        pass

    def is_error(self, const_DatagramSink_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_error(const DatagramSink self)
        """
        pass

    def putDatagram(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        put_datagram(const DatagramSink self, const Datagram data)
        """
        pass

    def put_datagram(self, const_DatagramSink_self, const_Datagram_data): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        put_datagram(const DatagramSink self, const Datagram data)
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    file = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    filename = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    file_pos = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * This class defines the abstract interface to sending datagrams to any\n * target, whether it be into a file or across the net\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.DatagramSink' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE277EC0>'
        'copyDatagram': None, # (!) real value is "<method 'copyDatagram' of 'panda3d.core.DatagramSink' objects>"
        'copy_datagram': None, # (!) real value is "<method 'copy_datagram' of 'panda3d.core.DatagramSink' objects>"
        'file': None, # (!) real value is "<attribute 'file' of 'panda3d.core.DatagramSink' objects>"
        'file_pos': None, # (!) real value is "<attribute 'file_pos' of 'panda3d.core.DatagramSink' objects>"
        'filename': None, # (!) real value is "<attribute 'filename' of 'panda3d.core.DatagramSink' objects>"
        'flush': None, # (!) real value is "<method 'flush' of 'panda3d.core.DatagramSink' objects>"
        'getFile': None, # (!) real value is "<method 'getFile' of 'panda3d.core.DatagramSink' objects>"
        'getFilePos': None, # (!) real value is "<method 'getFilePos' of 'panda3d.core.DatagramSink' objects>"
        'getFilename': None, # (!) real value is "<method 'getFilename' of 'panda3d.core.DatagramSink' objects>"
        'get_file': None, # (!) real value is "<method 'get_file' of 'panda3d.core.DatagramSink' objects>"
        'get_file_pos': None, # (!) real value is "<method 'get_file_pos' of 'panda3d.core.DatagramSink' objects>"
        'get_filename': None, # (!) real value is "<method 'get_filename' of 'panda3d.core.DatagramSink' objects>"
        'isError': None, # (!) real value is "<method 'isError' of 'panda3d.core.DatagramSink' objects>"
        'is_error': None, # (!) real value is "<method 'is_error' of 'panda3d.core.DatagramSink' objects>"
        'putDatagram': None, # (!) real value is "<method 'putDatagram' of 'panda3d.core.DatagramSink' objects>"
        'put_datagram': None, # (!) real value is "<method 'put_datagram' of 'panda3d.core.DatagramSink' objects>"
    }


