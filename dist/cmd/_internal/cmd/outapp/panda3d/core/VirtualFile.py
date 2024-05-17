# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .TypedReferenceCount import TypedReferenceCount

class VirtualFile(TypedReferenceCount):
    """
    /**
     * The abstract base class for a file or directory within the
     * VirtualFileSystem.
     */
    """
    def closeReadFile(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        close_read_file(VirtualFile self, istream stream)
        
        /**
         * Closes a file opened by a previous call to open_read_file().  This really
         * just deletes the istream pointer, but it is recommended to use this
         * interface instead of deleting it explicitly, to help work around compiler
         * issues.
         */
        """
        pass

    def closeReadWriteFile(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        close_read_write_file(const VirtualFile self, iostream stream)
        
        /**
         * Closes a file opened by a previous call to open_read_write_file().  This
         * really just deletes the iostream pointer, but it is recommended to use this
         * interface instead of deleting it explicitly, to help work around compiler
         * issues.
         */
        """
        pass

    def closeWriteFile(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        close_write_file(const VirtualFile self, ostream stream)
        
        /**
         * Closes a file opened by a previous call to open_write_file().  This really
         * just deletes the ostream pointer, but it is recommended to use this
         * interface instead of deleting it explicitly, to help work around compiler
         * issues.
         */
        """
        pass

    def close_read_file(self, VirtualFile_self, istream_stream): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        close_read_file(VirtualFile self, istream stream)
        
        /**
         * Closes a file opened by a previous call to open_read_file().  This really
         * just deletes the istream pointer, but it is recommended to use this
         * interface instead of deleting it explicitly, to help work around compiler
         * issues.
         */
        """
        pass

    def close_read_write_file(self, const_VirtualFile_self, iostream_stream): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        close_read_write_file(const VirtualFile self, iostream stream)
        
        /**
         * Closes a file opened by a previous call to open_read_write_file().  This
         * really just deletes the iostream pointer, but it is recommended to use this
         * interface instead of deleting it explicitly, to help work around compiler
         * issues.
         */
        """
        pass

    def close_write_file(self, const_VirtualFile_self, ostream_stream): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        close_write_file(const VirtualFile self, ostream stream)
        
        /**
         * Closes a file opened by a previous call to open_write_file().  This really
         * just deletes the ostream pointer, but it is recommended to use this
         * interface instead of deleting it explicitly, to help work around compiler
         * issues.
         */
        """
        pass

    def copyFile(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        copy_file(const VirtualFile self, VirtualFile new_file)
        
        /**
         * Attempts to copy the contents of this file to the indicated file.  Returns
         * true on success, false on failure.
         */
        """
        pass

    def copy_file(self, const_VirtualFile_self, VirtualFile_new_file): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        copy_file(const VirtualFile self, VirtualFile new_file)
        
        /**
         * Attempts to copy the contents of this file to the indicated file.  Returns
         * true on success, false on failure.
         */
        """
        pass

    def deleteFile(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        delete_file(const VirtualFile self)
        
        /**
         * Attempts to delete this file or directory.  This can remove a single file
         * or an empty directory.  It will not remove a nonempty directory.  Returns
         * true on success, false on failure.
         */
        """
        pass

    def delete_file(self, const_VirtualFile_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        delete_file(const VirtualFile self)
        
        /**
         * Attempts to delete this file or directory.  This can remove a single file
         * or an empty directory.  It will not remove a nonempty directory.  Returns
         * true on success, false on failure.
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getFilename(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_filename(VirtualFile self)
        """
        pass

    def getFileSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_file_size(VirtualFile self)
        get_file_size(VirtualFile self, istream stream)
        
        /**
         * Returns the current size on disk (or wherever it is) of the already-open
         * file.  Pass in the stream that was returned by open_read_file(); some
         * implementations may require this stream to determine the size.
         */
        
        /**
         * Returns the current size on disk (or wherever it is) of the file before it
         * has been opened.
         */
        """
        pass

    def getFileSystem(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_file_system(VirtualFile self)
        """
        pass

    def getOriginalFilename(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_original_filename(VirtualFile self)
        
        /**
         * Returns the original filename as it was used to locate this VirtualFile.
         * This is usually, but not always, the same string returned by
         * get_filename().
         */
        """
        pass

    def getSystemInfo(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_system_info(const VirtualFile self, SubfileInfo info)
        
        /**
         * Populates the SubfileInfo structure with the data representing where the
         * file actually resides on disk, if this is knowable.  Returns true if the
         * file might reside on disk, and the info is populated, or false if it does
         * not (or it is not known where the file resides), in which case the info is
         * meaningless.
         */
        """
        pass

    def getTimestamp(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_timestamp(VirtualFile self)
        
        /**
         * Returns a time_t value that represents the time the file was last modified,
         * to within whatever precision the operating system records this information
         * (on a Windows95 system, for instance, this may only be accurate to within 2
         * seconds).
         *
         * If the timestamp cannot be determined, either because it is not supported
         * by the operating system or because there is some error (such as file not
         * found), returns 0.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_filename(self, VirtualFile_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_filename(VirtualFile self)
        """
        pass

    def get_file_size(self, VirtualFile_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_file_size(VirtualFile self)
        get_file_size(VirtualFile self, istream stream)
        
        /**
         * Returns the current size on disk (or wherever it is) of the already-open
         * file.  Pass in the stream that was returned by open_read_file(); some
         * implementations may require this stream to determine the size.
         */
        
        /**
         * Returns the current size on disk (or wherever it is) of the file before it
         * has been opened.
         */
        """
        pass

    def get_file_system(self, VirtualFile_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_file_system(VirtualFile self)
        """
        pass

    def get_original_filename(self, VirtualFile_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_original_filename(VirtualFile self)
        
        /**
         * Returns the original filename as it was used to locate this VirtualFile.
         * This is usually, but not always, the same string returned by
         * get_filename().
         */
        """
        pass

    def get_system_info(self, const_VirtualFile_self, SubfileInfo_info): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_system_info(const VirtualFile self, SubfileInfo info)
        
        /**
         * Populates the SubfileInfo structure with the data representing where the
         * file actually resides on disk, if this is knowable.  Returns true if the
         * file might reside on disk, and the info is populated, or false if it does
         * not (or it is not known where the file resides), in which case the info is
         * meaningless.
         */
        """
        pass

    def get_timestamp(self, VirtualFile_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_timestamp(VirtualFile self)
        
        /**
         * Returns a time_t value that represents the time the file was last modified,
         * to within whatever precision the operating system records this information
         * (on a Windows95 system, for instance, this may only be accurate to within 2
         * seconds).
         *
         * If the timestamp cannot be determined, either because it is not supported
         * by the operating system or because there is some error (such as file not
         * found), returns 0.
         */
        """
        pass

    def hasFile(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_file(VirtualFile self)
        
        /**
         * Returns true if this file exists, false otherwise.
         */
        """
        pass

    def has_file(self, VirtualFile_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_file(VirtualFile self)
        
        /**
         * Returns true if this file exists, false otherwise.
         */
        """
        pass

    def isDirectory(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_directory(VirtualFile self)
        
        /**
         * Returns true if this file represents a directory (and scan_directory() may
         * be called), false otherwise.
         */
        """
        pass

    def isRegularFile(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_regular_file(VirtualFile self)
        
        /**
         * Returns true if this file represents a regular file (and read_file() may be
         * called), false otherwise.
         */
        """
        pass

    def isWritable(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_writable(VirtualFile self)
        
        /**
         * Returns true if this file may be written to, which implies write_file() may
         * be called (unless it is a directory instead of a regular file).
         */
        """
        pass

    def is_directory(self, VirtualFile_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_directory(VirtualFile self)
        
        /**
         * Returns true if this file represents a directory (and scan_directory() may
         * be called), false otherwise.
         */
        """
        pass

    def is_regular_file(self, VirtualFile_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_regular_file(VirtualFile self)
        
        /**
         * Returns true if this file represents a regular file (and read_file() may be
         * called), false otherwise.
         */
        """
        pass

    def is_writable(self, VirtualFile_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_writable(VirtualFile self)
        
        /**
         * Returns true if this file may be written to, which implies write_file() may
         * be called (unless it is a directory instead of a regular file).
         */
        """
        pass

    def ls(self, VirtualFile_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        ls(VirtualFile self, ostream out)
        
        /**
         * If the file represents a directory, lists its contents.
         */
        """
        pass

    def lsAll(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        ls_all(VirtualFile self, ostream out)
        
        /**
         * If the file represents a directory, recursively lists its contents and
         * those of all subdirectories.
         */
        """
        pass

    def ls_all(self, VirtualFile_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        ls_all(VirtualFile self, ostream out)
        
        /**
         * If the file represents a directory, recursively lists its contents and
         * those of all subdirectories.
         */
        """
        pass

    def openAppendFile(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        open_append_file(const VirtualFile self)
        
        /**
         * Works like open_write_file(), but the file is opened in append mode.  Like
         * open_write_file, the returned pointer should eventually be passed to
         * close_write_file().
         */
        """
        pass

    def openReadAppendFile(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        open_read_append_file(const VirtualFile self)
        
        /**
         * Works like open_read_write_file(), but the file is opened in append mode.
         * Like open_read_write_file, the returned pointer should eventually be passed
         * to close_read_write_file().
         */
        """
        pass

    def openReadFile(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        open_read_file(VirtualFile self, bool auto_unwrap)
        
        /**
         * Opens the file for reading.  Returns a newly allocated istream on success
         * (which you should eventually delete when you are done reading). Returns
         * NULL on failure.
         */
        """
        pass

    def openReadWriteFile(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        open_read_write_file(const VirtualFile self, bool truncate)
        
        /**
         * Opens the file for writing.  Returns a newly allocated iostream on success
         * (which you should eventually delete when you are done writing). Returns
         * NULL on failure.
         */
        """
        pass

    def openWriteFile(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        open_write_file(const VirtualFile self, bool auto_wrap, bool truncate)
        
        /**
         * Opens the file for writing.  Returns a newly allocated ostream on success
         * (which you should eventually delete when you are done writing). Returns
         * NULL on failure.
         */
        """
        pass

    def open_append_file(self, const_VirtualFile_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        open_append_file(const VirtualFile self)
        
        /**
         * Works like open_write_file(), but the file is opened in append mode.  Like
         * open_write_file, the returned pointer should eventually be passed to
         * close_write_file().
         */
        """
        pass

    def open_read_append_file(self, const_VirtualFile_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        open_read_append_file(const VirtualFile self)
        
        /**
         * Works like open_read_write_file(), but the file is opened in append mode.
         * Like open_read_write_file, the returned pointer should eventually be passed
         * to close_read_write_file().
         */
        """
        pass

    def open_read_file(self, VirtualFile_self, bool_auto_unwrap): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        open_read_file(VirtualFile self, bool auto_unwrap)
        
        /**
         * Opens the file for reading.  Returns a newly allocated istream on success
         * (which you should eventually delete when you are done reading). Returns
         * NULL on failure.
         */
        """
        pass

    def open_read_write_file(self, const_VirtualFile_self, bool_truncate): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        open_read_write_file(const VirtualFile self, bool truncate)
        
        /**
         * Opens the file for writing.  Returns a newly allocated iostream on success
         * (which you should eventually delete when you are done writing). Returns
         * NULL on failure.
         */
        """
        pass

    def open_write_file(self, const_VirtualFile_self, bool_auto_wrap, bool_truncate): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        open_write_file(const VirtualFile self, bool auto_wrap, bool truncate)
        
        /**
         * Opens the file for writing.  Returns a newly allocated ostream on success
         * (which you should eventually delete when you are done writing). Returns
         * NULL on failure.
         */
        """
        pass

    def output(self, VirtualFile_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(VirtualFile self, ostream out)
        
        /**
         *
         */
        """
        pass

    def readFile(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        read_file(VirtualFile self, bool auto_unwrap)
        
        /**
         * Returns the entire contents of the file as a string.
         */
        
        /**
         * Fills up the indicated string with the contents of the file, if it is a
         * regular file.  Returns true on success, false otherwise.
         */
        
        /**
         * Fills up the indicated pvector with the contents of the file, if it is a
         * regular file.  Returns true on success, false otherwise.
         */
        """
        pass

    def read_file(self, VirtualFile_self, bool_auto_unwrap): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        read_file(VirtualFile self, bool auto_unwrap)
        
        /**
         * Returns the entire contents of the file as a string.
         */
        
        /**
         * Fills up the indicated string with the contents of the file, if it is a
         * regular file.  Returns true on success, false otherwise.
         */
        
        /**
         * Fills up the indicated pvector with the contents of the file, if it is a
         * regular file.  Returns true on success, false otherwise.
         */
        """
        pass

    def renameFile(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        rename_file(const VirtualFile self, VirtualFile new_file)
        
        /**
         * Attempts to move or rename this file or directory.  If the original file is
         * an ordinary file, it will quietly replace any already-existing file in the
         * new filename (but not a directory).  If the original file is a directory,
         * the new filename must not already exist.
         *
         * If the file is a directory, the new filename must be within the same mount
         * point.  If the file is an ordinary file, the new filename may be anywhere;
         * but if it is not within the same mount point then the rename operation is
         * automatically performed as a two-step copy-and-delete operation.
         */
        """
        pass

    def rename_file(self, const_VirtualFile_self, VirtualFile_new_file): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        rename_file(const VirtualFile self, VirtualFile new_file)
        
        /**
         * Attempts to move or rename this file or directory.  If the original file is
         * an ordinary file, it will quietly replace any already-existing file in the
         * new filename (but not a directory).  If the original file is a directory,
         * the new filename must not already exist.
         *
         * If the file is a directory, the new filename must be within the same mount
         * point.  If the file is an ordinary file, the new filename may be anywhere;
         * but if it is not within the same mount point then the rename operation is
         * automatically performed as a two-step copy-and-delete operation.
         */
        """
        pass

    def scanDirectory(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        scan_directory(VirtualFile self)
        
        /**
         * If the file represents a directory (that is, is_directory() returns true),
         * this returns the list of files within the directory at the current time.
         * Returns NULL if the file is not a directory or if the directory cannot be
         * read.
         */
        """
        pass

    def scan_directory(self, VirtualFile_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        scan_directory(VirtualFile self)
        
        /**
         * If the file represents a directory (that is, is_directory() returns true),
         * this returns the list of files within the directory at the current time.
         * Returns NULL if the file is not a directory or if the directory cannot be
         * read.
         */
        """
        pass

    def wasReadSuccessful(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        was_read_successful(VirtualFile self)
        
        /**
         * Call this method after a reading the istream returned by open_read_file()
         * to completion.  If it returns true, the file was read completely and
         * without error; if it returns false, there may have been some errors or a
         * truncated file read.  This is particularly likely if the stream is a
         * VirtualFileHTTP.
         */
        """
        pass

    def was_read_successful(self, VirtualFile_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        was_read_successful(VirtualFile self)
        
        /**
         * Call this method after a reading the istream returned by open_read_file()
         * to completion.  If it returns true, the file was read completely and
         * without error; if it returns false, there may have been some errors or a
         * truncated file read.  This is particularly likely if the stream is a
         * VirtualFileHTTP.
         */
        """
        pass

    def writeFile(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        write_file(const VirtualFile self, object data, bool auto_wrap)
        
        /**
         * Writes the entire contents of the file as a string, if it is writable.
         */
        
        /**
         * Writes the indicated data to the file, if it is writable.  Returns true on
         * success, false otherwise.
         */
        """
        pass

    def write_file(self, const_VirtualFile_self, object_data, bool_auto_wrap): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write_file(const VirtualFile self, object data, bool auto_wrap)
        
        /**
         * Writes the entire contents of the file as a string, if it is writable.
         */
        
        /**
         * Writes the indicated data to the file, if it is writable.  Returns true on
         * success, false otherwise.
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * The abstract base class for a file or directory within the\n * VirtualFileSystem.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.VirtualFile' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE279650>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.VirtualFile' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.VirtualFile' objects>"
        'closeReadFile': None, # (!) real value is "<method 'closeReadFile' of 'panda3d.core.VirtualFile' objects>"
        'closeReadWriteFile': None, # (!) real value is "<method 'closeReadWriteFile' of 'panda3d.core.VirtualFile' objects>"
        'closeWriteFile': None, # (!) real value is "<method 'closeWriteFile' of 'panda3d.core.VirtualFile' objects>"
        'close_read_file': None, # (!) real value is "<method 'close_read_file' of 'panda3d.core.VirtualFile' objects>"
        'close_read_write_file': None, # (!) real value is "<method 'close_read_write_file' of 'panda3d.core.VirtualFile' objects>"
        'close_write_file': None, # (!) real value is "<method 'close_write_file' of 'panda3d.core.VirtualFile' objects>"
        'copyFile': None, # (!) real value is "<method 'copyFile' of 'panda3d.core.VirtualFile' objects>"
        'copy_file': None, # (!) real value is "<method 'copy_file' of 'panda3d.core.VirtualFile' objects>"
        'deleteFile': None, # (!) real value is "<method 'deleteFile' of 'panda3d.core.VirtualFile' objects>"
        'delete_file': None, # (!) real value is "<method 'delete_file' of 'panda3d.core.VirtualFile' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE279650>)>'
        'getFileSize': None, # (!) real value is "<method 'getFileSize' of 'panda3d.core.VirtualFile' objects>"
        'getFileSystem': None, # (!) real value is "<method 'getFileSystem' of 'panda3d.core.VirtualFile' objects>"
        'getFilename': None, # (!) real value is "<method 'getFilename' of 'panda3d.core.VirtualFile' objects>"
        'getOriginalFilename': None, # (!) real value is "<method 'getOriginalFilename' of 'panda3d.core.VirtualFile' objects>"
        'getSystemInfo': None, # (!) real value is "<method 'getSystemInfo' of 'panda3d.core.VirtualFile' objects>"
        'getTimestamp': None, # (!) real value is "<method 'getTimestamp' of 'panda3d.core.VirtualFile' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE279650>)>'
        'get_file_size': None, # (!) real value is "<method 'get_file_size' of 'panda3d.core.VirtualFile' objects>"
        'get_file_system': None, # (!) real value is "<method 'get_file_system' of 'panda3d.core.VirtualFile' objects>"
        'get_filename': None, # (!) real value is "<method 'get_filename' of 'panda3d.core.VirtualFile' objects>"
        'get_original_filename': None, # (!) real value is "<method 'get_original_filename' of 'panda3d.core.VirtualFile' objects>"
        'get_system_info': None, # (!) real value is "<method 'get_system_info' of 'panda3d.core.VirtualFile' objects>"
        'get_timestamp': None, # (!) real value is "<method 'get_timestamp' of 'panda3d.core.VirtualFile' objects>"
        'hasFile': None, # (!) real value is "<method 'hasFile' of 'panda3d.core.VirtualFile' objects>"
        'has_file': None, # (!) real value is "<method 'has_file' of 'panda3d.core.VirtualFile' objects>"
        'isDirectory': None, # (!) real value is "<method 'isDirectory' of 'panda3d.core.VirtualFile' objects>"
        'isRegularFile': None, # (!) real value is "<method 'isRegularFile' of 'panda3d.core.VirtualFile' objects>"
        'isWritable': None, # (!) real value is "<method 'isWritable' of 'panda3d.core.VirtualFile' objects>"
        'is_directory': None, # (!) real value is "<method 'is_directory' of 'panda3d.core.VirtualFile' objects>"
        'is_regular_file': None, # (!) real value is "<method 'is_regular_file' of 'panda3d.core.VirtualFile' objects>"
        'is_writable': None, # (!) real value is "<method 'is_writable' of 'panda3d.core.VirtualFile' objects>"
        'ls': None, # (!) real value is "<method 'ls' of 'panda3d.core.VirtualFile' objects>"
        'lsAll': None, # (!) real value is "<method 'lsAll' of 'panda3d.core.VirtualFile' objects>"
        'ls_all': None, # (!) real value is "<method 'ls_all' of 'panda3d.core.VirtualFile' objects>"
        'openAppendFile': None, # (!) real value is "<method 'openAppendFile' of 'panda3d.core.VirtualFile' objects>"
        'openReadAppendFile': None, # (!) real value is "<method 'openReadAppendFile' of 'panda3d.core.VirtualFile' objects>"
        'openReadFile': None, # (!) real value is "<method 'openReadFile' of 'panda3d.core.VirtualFile' objects>"
        'openReadWriteFile': None, # (!) real value is "<method 'openReadWriteFile' of 'panda3d.core.VirtualFile' objects>"
        'openWriteFile': None, # (!) real value is "<method 'openWriteFile' of 'panda3d.core.VirtualFile' objects>"
        'open_append_file': None, # (!) real value is "<method 'open_append_file' of 'panda3d.core.VirtualFile' objects>"
        'open_read_append_file': None, # (!) real value is "<method 'open_read_append_file' of 'panda3d.core.VirtualFile' objects>"
        'open_read_file': None, # (!) real value is "<method 'open_read_file' of 'panda3d.core.VirtualFile' objects>"
        'open_read_write_file': None, # (!) real value is "<method 'open_read_write_file' of 'panda3d.core.VirtualFile' objects>"
        'open_write_file': None, # (!) real value is "<method 'open_write_file' of 'panda3d.core.VirtualFile' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.VirtualFile' objects>"
        'readFile': None, # (!) real value is "<method 'readFile' of 'panda3d.core.VirtualFile' objects>"
        'read_file': None, # (!) real value is "<method 'read_file' of 'panda3d.core.VirtualFile' objects>"
        'renameFile': None, # (!) real value is "<method 'renameFile' of 'panda3d.core.VirtualFile' objects>"
        'rename_file': None, # (!) real value is "<method 'rename_file' of 'panda3d.core.VirtualFile' objects>"
        'scanDirectory': None, # (!) real value is "<method 'scanDirectory' of 'panda3d.core.VirtualFile' objects>"
        'scan_directory': None, # (!) real value is "<method 'scan_directory' of 'panda3d.core.VirtualFile' objects>"
        'wasReadSuccessful': None, # (!) real value is "<method 'wasReadSuccessful' of 'panda3d.core.VirtualFile' objects>"
        'was_read_successful': None, # (!) real value is "<method 'was_read_successful' of 'panda3d.core.VirtualFile' objects>"
        'writeFile': None, # (!) real value is "<method 'writeFile' of 'panda3d.core.VirtualFile' objects>"
        'write_file': None, # (!) real value is "<method 'write_file' of 'panda3d.core.VirtualFile' objects>"
    }


