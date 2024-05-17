# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class DatagramGenerator(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * This class defines the abstract interace to any source of datagrams,
     * whether it be from a file or from the net.
     */
    """
    def getDatagram(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_datagram(const DatagramGenerator self, Datagram data)
        """
        pass

    def getFile(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_file(const DatagramGenerator self)
        
        /**
         * Returns the FileReference that provides the source for these datagrams, if
         * any, or NULL if the datagrams do not originate from a file on disk.
         */
        """
        pass

    def getFilename(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_filename(const DatagramGenerator self)
        
        /**
         * Returns the filename that provides the source for these datagrams, if any,
         * or empty string if the datagrams do not originate from a file on disk.
         */
        """
        pass

    def getFilePos(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_file_pos(const DatagramGenerator self)
        
        /**
         * Returns the current file position within the data stream, if any, or 0 if
         * the file position is not meaningful or cannot be determined.
         *
         * For DatagramGenerators that return a meaningful file position, this will be
         * pointing to the first byte following the datagram returned after a call to
         * get_datagram().
         */
        """
        pass

    def getTimestamp(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_timestamp(DatagramGenerator self)
        
        /**
         * Returns the on-disk timestamp of the file that was read, at the time it was
         * opened, if that is available, or 0 if it is not.
         */
        """
        pass

    def getVfile(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_vfile(const DatagramGenerator self)
        
        /**
         * Returns the VirtualFile that provides the source for these datagrams, if
         * any, or NULL if the datagrams do not originate from a VirtualFile.
         */
        """
        pass

    def get_datagram(self, const_DatagramGenerator_self, Datagram_data): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_datagram(const DatagramGenerator self, Datagram data)
        """
        pass

    def get_file(self, const_DatagramGenerator_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_file(const DatagramGenerator self)
        
        /**
         * Returns the FileReference that provides the source for these datagrams, if
         * any, or NULL if the datagrams do not originate from a file on disk.
         */
        """
        pass

    def get_filename(self, const_DatagramGenerator_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_filename(const DatagramGenerator self)
        
        /**
         * Returns the filename that provides the source for these datagrams, if any,
         * or empty string if the datagrams do not originate from a file on disk.
         */
        """
        pass

    def get_file_pos(self, const_DatagramGenerator_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_file_pos(const DatagramGenerator self)
        
        /**
         * Returns the current file position within the data stream, if any, or 0 if
         * the file position is not meaningful or cannot be determined.
         *
         * For DatagramGenerators that return a meaningful file position, this will be
         * pointing to the first byte following the datagram returned after a call to
         * get_datagram().
         */
        """
        pass

    def get_timestamp(self, DatagramGenerator_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_timestamp(DatagramGenerator self)
        
        /**
         * Returns the on-disk timestamp of the file that was read, at the time it was
         * opened, if that is available, or 0 if it is not.
         */
        """
        pass

    def get_vfile(self, const_DatagramGenerator_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_vfile(const DatagramGenerator self)
        
        /**
         * Returns the VirtualFile that provides the source for these datagrams, if
         * any, or NULL if the datagrams do not originate from a VirtualFile.
         */
        """
        pass

    def isEof(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_eof(const DatagramGenerator self)
        """
        pass

    def isError(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_error(const DatagramGenerator self)
        """
        pass

    def is_eof(self, const_DatagramGenerator_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_eof(const DatagramGenerator self)
        """
        pass

    def is_error(self, const_DatagramGenerator_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_error(const DatagramGenerator self)
        """
        pass

    def saveDatagram(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        save_datagram(const DatagramGenerator self, SubfileInfo info)
        
        /**
         * Skips over the next datagram without extracting it, but saves the relevant
         * file information in the SubfileInfo object so that its data may be read
         * later.  For non-file-based datagram generators, this may mean creating a
         * temporary file and copying the contents of the datagram to disk.
         *
         * Returns true on success, false on failure or if this method is
         * unimplemented.
         */
        """
        pass

    def save_datagram(self, const_DatagramGenerator_self, SubfileInfo_info): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        save_datagram(const DatagramGenerator self, SubfileInfo info)
        
        /**
         * Skips over the next datagram without extracting it, but saves the relevant
         * file information in the SubfileInfo object so that its data may be read
         * later.  For non-file-based datagram generators, this may mean creating a
         * temporary file and copying the contents of the datagram to disk.
         *
         * Returns true on success, false on failure or if this method is
         * unimplemented.
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
        '__doc__': '/**\n * This class defines the abstract interace to any source of datagrams,\n * whether it be from a file or from the net.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.DatagramGenerator' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE277B20>'
        'getDatagram': None, # (!) real value is "<method 'getDatagram' of 'panda3d.core.DatagramGenerator' objects>"
        'getFile': None, # (!) real value is "<method 'getFile' of 'panda3d.core.DatagramGenerator' objects>"
        'getFilePos': None, # (!) real value is "<method 'getFilePos' of 'panda3d.core.DatagramGenerator' objects>"
        'getFilename': None, # (!) real value is "<method 'getFilename' of 'panda3d.core.DatagramGenerator' objects>"
        'getTimestamp': None, # (!) real value is "<method 'getTimestamp' of 'panda3d.core.DatagramGenerator' objects>"
        'getVfile': None, # (!) real value is "<method 'getVfile' of 'panda3d.core.DatagramGenerator' objects>"
        'get_datagram': None, # (!) real value is "<method 'get_datagram' of 'panda3d.core.DatagramGenerator' objects>"
        'get_file': None, # (!) real value is "<method 'get_file' of 'panda3d.core.DatagramGenerator' objects>"
        'get_file_pos': None, # (!) real value is "<method 'get_file_pos' of 'panda3d.core.DatagramGenerator' objects>"
        'get_filename': None, # (!) real value is "<method 'get_filename' of 'panda3d.core.DatagramGenerator' objects>"
        'get_timestamp': None, # (!) real value is "<method 'get_timestamp' of 'panda3d.core.DatagramGenerator' objects>"
        'get_vfile': None, # (!) real value is "<method 'get_vfile' of 'panda3d.core.DatagramGenerator' objects>"
        'isEof': None, # (!) real value is "<method 'isEof' of 'panda3d.core.DatagramGenerator' objects>"
        'isError': None, # (!) real value is "<method 'isError' of 'panda3d.core.DatagramGenerator' objects>"
        'is_eof': None, # (!) real value is "<method 'is_eof' of 'panda3d.core.DatagramGenerator' objects>"
        'is_error': None, # (!) real value is "<method 'is_error' of 'panda3d.core.DatagramGenerator' objects>"
        'saveDatagram': None, # (!) real value is "<method 'saveDatagram' of 'panda3d.core.DatagramGenerator' objects>"
        'save_datagram': None, # (!) real value is "<method 'save_datagram' of 'panda3d.core.DatagramGenerator' objects>"
    }


