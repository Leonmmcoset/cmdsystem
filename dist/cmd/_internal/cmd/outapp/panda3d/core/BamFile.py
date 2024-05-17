# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .BamEnums import BamEnums

class BamFile(BamEnums):
    """
    /**
     * The principle public interface to reading and writing Bam disk files.  See
     * also BamReader and BamWriter, the more general implementation of this
     * class.
     *
     * Bam files are most often used to store scene graphs or subgraphs, and by
     * convention they are given filenames ending in the extension ".bam" when
     * they are used for this purpose.  However, a Bam file may store any
     * arbitrary list of TypedWritable objects; in this more general usage, they
     * are given filenames ending in ".boo" to differentiate them from the more
     * common scene graph files.
     */
    """
    def close(self, const_BamFile_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        close(const BamFile self)
        
        /**
         * Closes the input or output stream.
         */
        """
        pass

    def getCurrentMajorVer(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_current_major_ver(const BamFile self)
        
        /**
         * Returns the system current major version number.  This is the version
         * number that will be assigned to any generated Bam files.
         */
        """
        pass

    def getCurrentMinorVer(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_current_minor_ver(const BamFile self)
        
        /**
         * Returns the system current minor version number.  This is the version
         * number that will be assigned to any generated Bam files.
         */
        """
        pass

    def getFileEndian(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_file_endian(BamFile self)
        
        /**
         * Returns the endian preference indicated by the Bam file currently being
         * read or written.
         */
        """
        pass

    def getFileMajorVer(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_file_major_ver(const BamFile self)
        
        /**
         * Returns the major version number of the file currently being read, or the
         * system current major version number if no file is currently open for
         * reading.
         */
        """
        pass

    def getFileMinorVer(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_file_minor_ver(const BamFile self)
        
        /**
         * Returns the minor version number of the file currently being read, or the
         * system current minor version number if no file is currently open for
         * reading.
         */
        """
        pass

    def getFileStdfloatDouble(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_file_stdfloat_double(BamFile self)
        
        /**
         * Returns true if the file stores all "standard" floats as 64-bit doubles, or
         * false if they are 32-bit floats.
         */
        """
        pass

    def getReader(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_reader(const BamFile self)
        
        /**
         * Returns the BamReader in charge of performing the read operations.  This
         * will return NULL unless open_read() was called.
         */
        """
        pass

    def getWriter(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_writer(const BamFile self)
        
        /**
         * Returns the BamWriter in charge of performing the write operations.  This
         * will return NULL unless open_write() was called.
         */
        """
        pass

    def get_current_major_ver(self, const_BamFile_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_current_major_ver(const BamFile self)
        
        /**
         * Returns the system current major version number.  This is the version
         * number that will be assigned to any generated Bam files.
         */
        """
        pass

    def get_current_minor_ver(self, const_BamFile_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_current_minor_ver(const BamFile self)
        
        /**
         * Returns the system current minor version number.  This is the version
         * number that will be assigned to any generated Bam files.
         */
        """
        pass

    def get_file_endian(self, BamFile_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_file_endian(BamFile self)
        
        /**
         * Returns the endian preference indicated by the Bam file currently being
         * read or written.
         */
        """
        pass

    def get_file_major_ver(self, const_BamFile_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_file_major_ver(const BamFile self)
        
        /**
         * Returns the major version number of the file currently being read, or the
         * system current major version number if no file is currently open for
         * reading.
         */
        """
        pass

    def get_file_minor_ver(self, const_BamFile_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_file_minor_ver(const BamFile self)
        
        /**
         * Returns the minor version number of the file currently being read, or the
         * system current minor version number if no file is currently open for
         * reading.
         */
        """
        pass

    def get_file_stdfloat_double(self, BamFile_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_file_stdfloat_double(BamFile self)
        
        /**
         * Returns true if the file stores all "standard" floats as 64-bit doubles, or
         * false if they are 32-bit floats.
         */
        """
        pass

    def get_reader(self, const_BamFile_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_reader(const BamFile self)
        
        /**
         * Returns the BamReader in charge of performing the read operations.  This
         * will return NULL unless open_read() was called.
         */
        """
        pass

    def get_writer(self, const_BamFile_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_writer(const BamFile self)
        
        /**
         * Returns the BamWriter in charge of performing the write operations.  This
         * will return NULL unless open_write() was called.
         */
        """
        pass

    def isEof(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_eof(BamFile self)
        
        /**
         * Returns true if the reader has reached end-of-file, false otherwise.  This
         * call is only valid after a call to read_object().
         */
        """
        pass

    def isValidRead(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_valid_read(BamFile self)
        
        /**
         * Returns true if the Bam file is open and ready for reading with no errors
         * so far detected, or false otherwise.
         */
        """
        pass

    def isValidWrite(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_valid_write(BamFile self)
        
        /**
         * Returns true if the Bam file is open and ready for writing with no errors
         * so far detected, or false otherwise.
         */
        """
        pass

    def is_eof(self, BamFile_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_eof(BamFile self)
        
        /**
         * Returns true if the reader has reached end-of-file, false otherwise.  This
         * call is only valid after a call to read_object().
         */
        """
        pass

    def is_valid_read(self, BamFile_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_valid_read(BamFile self)
        
        /**
         * Returns true if the Bam file is open and ready for reading with no errors
         * so far detected, or false otherwise.
         */
        """
        pass

    def is_valid_write(self, BamFile_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_valid_write(BamFile self)
        
        /**
         * Returns true if the Bam file is open and ready for writing with no errors
         * so far detected, or false otherwise.
         */
        """
        pass

    def openRead(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        open_read(const BamFile self, istream in, str bam_filename, bool report_errors)
        
        /**
         * Attempts to open the indicated filename for reading.  Returns true if
         * successful, false on error.
         */
        
        /**
         * Attempts to open the indicated stream for reading.  The filename is just
         * for information purposes only.  Returns true if successful, false on error.
         */
        """
        pass

    def openWrite(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        open_write(const BamFile self, ostream out, str bam_filename, bool report_errors)
        
        /**
         * Attempts to open the indicated file for writing.  If another file by the
         * same name already exists, it will be silently removed.  Returns true if
         * successful, false otherwise.
         */
        
        /**
         * Attempts to open the indicated stream for writing.  The filename is just
         * for information purposes only.  Returns true if successful, false on error.
         */
        """
        pass

    def open_read(self, const_BamFile_self, istream_in, str_bam_filename, bool_report_errors): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        open_read(const BamFile self, istream in, str bam_filename, bool report_errors)
        
        /**
         * Attempts to open the indicated filename for reading.  Returns true if
         * successful, false on error.
         */
        
        /**
         * Attempts to open the indicated stream for reading.  The filename is just
         * for information purposes only.  Returns true if successful, false on error.
         */
        """
        pass

    def open_write(self, const_BamFile_self, ostream_out, str_bam_filename, bool_report_errors): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        open_write(const BamFile self, ostream out, str bam_filename, bool report_errors)
        
        /**
         * Attempts to open the indicated file for writing.  If another file by the
         * same name already exists, it will be silently removed.  Returns true if
         * successful, false otherwise.
         */
        
        /**
         * Attempts to open the indicated stream for writing.  The filename is just
         * for information purposes only.  Returns true if successful, false on error.
         */
        """
        pass

    def readNode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        read_node(const BamFile self, bool report_errors)
        
        /**
         * Although the bam file format is general enough to store a list of objects
         * of arbitrary type, bam files on disk usually contain just one object, a
         * PandaNode that is the root of a scene graph.  (Bam files that store other
         * kinds of things are usually given the extension "boo", for "binary other
         * objects", to differentiate them from the normal scene graph type file.)
         *
         * This is a convenience method for when you believe you are reading a scene
         * graph bam file.  It reads the one PandaNode and returns it.  It also calls
         * resolve() to fully resolve the object, since we expect this will be the
         * only object in the file.
         *
         * If the bam file contains something other than a PandaNode, an error is
         * printed and NULL is returned.
         */
        """
        pass

    def readObject(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        read_object(const BamFile self)
        
        /**
         * Reads and returns the next object from the Bam file, or NULL if the end of
         * the file has been reached, or if there is an error condition.  Use is_eof()
         * to differentiate these two cases.
         *
         * The pointers returned by this method will not be valid for use until
         * resolve() is subsequently called.
         */
        """
        pass

    def read_node(self, const_BamFile_self, bool_report_errors): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        read_node(const BamFile self, bool report_errors)
        
        /**
         * Although the bam file format is general enough to store a list of objects
         * of arbitrary type, bam files on disk usually contain just one object, a
         * PandaNode that is the root of a scene graph.  (Bam files that store other
         * kinds of things are usually given the extension "boo", for "binary other
         * objects", to differentiate them from the normal scene graph type file.)
         *
         * This is a convenience method for when you believe you are reading a scene
         * graph bam file.  It reads the one PandaNode and returns it.  It also calls
         * resolve() to fully resolve the object, since we expect this will be the
         * only object in the file.
         *
         * If the bam file contains something other than a PandaNode, an error is
         * printed and NULL is returned.
         */
        """
        pass

    def read_object(self, const_BamFile_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        read_object(const BamFile self)
        
        /**
         * Reads and returns the next object from the Bam file, or NULL if the end of
         * the file has been reached, or if there is an error condition.  Use is_eof()
         * to differentiate these two cases.
         *
         * The pointers returned by this method will not be valid for use until
         * resolve() is subsequently called.
         */
        """
        pass

    def resolve(self, const_BamFile_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        resolve(const BamFile self)
        
        /**
         * This must be called after one or more objects have been read via calls to
         * read_object() in order to resolve all internal pointer references in the
         * objects read and make all the pointers valid.  It returns true if all
         * objects are successfully resolved, or false if some have not been (in which
         * case you must call resolve() again later).
         */
        """
        pass

    def writeObject(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        write_object(const BamFile self, const TypedWritable object)
        
        /**
         * Writes the indicated object to the Bam file.  Returns true if successful,
         * false on error.
         */
        """
        pass

    def write_object(self, const_BamFile_self, const_TypedWritable_object): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write_object(const BamFile self, const TypedWritable object)
        
        /**
         * Writes the indicated object to the Bam file.  Returns true if successful,
         * false on error.
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    file_endian = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    file_stdfloat_double = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    file_version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    reader = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    writer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * The principle public interface to reading and writing Bam disk files.  See\n * also BamReader and BamWriter, the more general implementation of this\n * class.\n *\n * Bam files are most often used to store scene graphs or subgraphs, and by\n * convention they are given filenames ending in the extension ".bam" when\n * they are used for this purpose.  However, a Bam file may store any\n * arbitrary list of TypedWritable objects; in this more general usage, they\n * are given filenames ending in ".boo" to differentiate them from the more\n * common scene graph files.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.BamFile' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE294550>'
        'close': None, # (!) real value is "<method 'close' of 'panda3d.core.BamFile' objects>"
        'file_endian': None, # (!) real value is "<attribute 'file_endian' of 'panda3d.core.BamFile' objects>"
        'file_stdfloat_double': None, # (!) real value is "<attribute 'file_stdfloat_double' of 'panda3d.core.BamFile' objects>"
        'file_version': None, # (!) real value is "<attribute 'file_version' of 'panda3d.core.BamFile' objects>"
        'getCurrentMajorVer': None, # (!) real value is "<method 'getCurrentMajorVer' of 'panda3d.core.BamFile' objects>"
        'getCurrentMinorVer': None, # (!) real value is "<method 'getCurrentMinorVer' of 'panda3d.core.BamFile' objects>"
        'getFileEndian': None, # (!) real value is "<method 'getFileEndian' of 'panda3d.core.BamFile' objects>"
        'getFileMajorVer': None, # (!) real value is "<method 'getFileMajorVer' of 'panda3d.core.BamFile' objects>"
        'getFileMinorVer': None, # (!) real value is "<method 'getFileMinorVer' of 'panda3d.core.BamFile' objects>"
        'getFileStdfloatDouble': None, # (!) real value is "<method 'getFileStdfloatDouble' of 'panda3d.core.BamFile' objects>"
        'getReader': None, # (!) real value is "<method 'getReader' of 'panda3d.core.BamFile' objects>"
        'getWriter': None, # (!) real value is "<method 'getWriter' of 'panda3d.core.BamFile' objects>"
        'get_current_major_ver': None, # (!) real value is "<method 'get_current_major_ver' of 'panda3d.core.BamFile' objects>"
        'get_current_minor_ver': None, # (!) real value is "<method 'get_current_minor_ver' of 'panda3d.core.BamFile' objects>"
        'get_file_endian': None, # (!) real value is "<method 'get_file_endian' of 'panda3d.core.BamFile' objects>"
        'get_file_major_ver': None, # (!) real value is "<method 'get_file_major_ver' of 'panda3d.core.BamFile' objects>"
        'get_file_minor_ver': None, # (!) real value is "<method 'get_file_minor_ver' of 'panda3d.core.BamFile' objects>"
        'get_file_stdfloat_double': None, # (!) real value is "<method 'get_file_stdfloat_double' of 'panda3d.core.BamFile' objects>"
        'get_reader': None, # (!) real value is "<method 'get_reader' of 'panda3d.core.BamFile' objects>"
        'get_writer': None, # (!) real value is "<method 'get_writer' of 'panda3d.core.BamFile' objects>"
        'isEof': None, # (!) real value is "<method 'isEof' of 'panda3d.core.BamFile' objects>"
        'isValidRead': None, # (!) real value is "<method 'isValidRead' of 'panda3d.core.BamFile' objects>"
        'isValidWrite': None, # (!) real value is "<method 'isValidWrite' of 'panda3d.core.BamFile' objects>"
        'is_eof': None, # (!) real value is "<method 'is_eof' of 'panda3d.core.BamFile' objects>"
        'is_valid_read': None, # (!) real value is "<method 'is_valid_read' of 'panda3d.core.BamFile' objects>"
        'is_valid_write': None, # (!) real value is "<method 'is_valid_write' of 'panda3d.core.BamFile' objects>"
        'openRead': None, # (!) real value is "<method 'openRead' of 'panda3d.core.BamFile' objects>"
        'openWrite': None, # (!) real value is "<method 'openWrite' of 'panda3d.core.BamFile' objects>"
        'open_read': None, # (!) real value is "<method 'open_read' of 'panda3d.core.BamFile' objects>"
        'open_write': None, # (!) real value is "<method 'open_write' of 'panda3d.core.BamFile' objects>"
        'readNode': None, # (!) real value is "<method 'readNode' of 'panda3d.core.BamFile' objects>"
        'readObject': None, # (!) real value is "<method 'readObject' of 'panda3d.core.BamFile' objects>"
        'read_node': None, # (!) real value is "<method 'read_node' of 'panda3d.core.BamFile' objects>"
        'read_object': None, # (!) real value is "<method 'read_object' of 'panda3d.core.BamFile' objects>"
        'reader': None, # (!) real value is "<attribute 'reader' of 'panda3d.core.BamFile' objects>"
        'resolve': None, # (!) real value is "<method 'resolve' of 'panda3d.core.BamFile' objects>"
        'writeObject': None, # (!) real value is "<method 'writeObject' of 'panda3d.core.BamFile' objects>"
        'write_object': None, # (!) real value is "<method 'write_object' of 'panda3d.core.BamFile' objects>"
        'writer': None, # (!) real value is "<attribute 'writer' of 'panda3d.core.BamFile' objects>"
    }


