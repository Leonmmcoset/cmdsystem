# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class Filename(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * The name of a file, such as a texture file or an Egg file.  Stores the full
     * pathname, and includes functions for extracting out the directory prefix
     * part and the file extension and stuff.
     *
     * A Filename is also aware of the mapping between the Unix-like filename
     * convention we use internally, and the local OS's specific filename
     * convention, and it knows how to perform basic OS-specific I/O, like testing
     * for file existence and searching a searchpath, as well as the best way to
     * open an fstream for reading or writing.
     *
     * Note that the methods of Filename that interact with the filesystem (such
     * as exists(), open_read(), etc.) directly interface with the operating system
     * and are not aware of Panda's virtual file system.  To interact with the VFS,
     * use the methods on VirtualFileSystem instead.
     */
    """
    def assign(self, const_Filename_self, const_Filename_copy): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        assign(const Filename self, const Filename copy)
        assign(const Filename self, unicode filename)
        assign(const Filename self, str filename)
        assign(const Filename self, str filename)
        
        // Assignment is via the = operator.
        
        /**
         *
         */
        
        /**
         *
         */
        
        /**
         *
         */
        
        /**
         *
         */
        
        /**
         *
         */
        
        /**
         *
         */
        """
        pass

    def binaryFilename(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        binary_filename(const Filename filename)
        binary_filename(str filename)
        
        /**
         *
         */
        
        /**
         *
         */
        """
        pass

    def binary_filename(self, const_Filename_filename): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        binary_filename(const Filename filename)
        binary_filename(str filename)
        
        /**
         *
         */
        
        /**
         *
         */
        """
        pass

    def chdir(self, Filename_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        chdir(Filename self)
        
        /**
         * Changes directory to the specified location.  Returns true if successful,
         * false if failure.
         */
        """
        pass

    def compareTimestamps(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        compare_timestamps(Filename self, const Filename other, bool this_missing_is_old, bool other_missing_is_old)
        
        /**
         * Returns a number less than zero if the file named by this object is older
         * than the given file, zero if they have the same timestamp, or greater than
         * zero if this one is newer.
         *
         * If this_missing_is_old is true, it indicates that a missing file will be
         * treated as if it were older than any other file; otherwise, a missing file
         * will be treated as if it were newer than any other file.  Similarly for
         * other_missing_is_old.
         */
        """
        pass

    def compareTo(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        compare_to(Filename self, const Filename other)
        
        /**
         *
         */
        """
        pass

    def compare_timestamps(self, Filename_self, const_Filename_other, bool_this_missing_is_old, bool_other_missing_is_old): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        compare_timestamps(Filename self, const Filename other, bool this_missing_is_old, bool other_missing_is_old)
        
        /**
         * Returns a number less than zero if the file named by this object is older
         * than the given file, zero if they have the same timestamp, or greater than
         * zero if this one is newer.
         *
         * If this_missing_is_old is true, it indicates that a missing file will be
         * treated as if it were older than any other file; otherwise, a missing file
         * will be treated as if it were newer than any other file.  Similarly for
         * other_missing_is_old.
         */
        """
        pass

    def compare_to(self, Filename_self, const_Filename_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        compare_to(Filename self, const Filename other)
        
        /**
         *
         */
        """
        pass

    def copyTo(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        copy_to(Filename self, const Filename other)
        
        /**
         * Copies the file to the indicated new filename, by reading the contents and
         * writing it to the new file.  Returns true if successful, false on failure.
         * The copy is always binary, regardless of the filename settings.
         */
        """
        pass

    def copy_to(self, Filename_self, const_Filename_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        copy_to(Filename self, const Filename other)
        
        /**
         * Copies the file to the indicated new filename, by reading the contents and
         * writing it to the new file.  Returns true if successful, false on failure.
         * The copy is always binary, regardless of the filename settings.
         */
        """
        pass

    def cStr(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        c_str(Filename self)
        
        /**
         *
         */
        """
        pass

    def c_str(self, Filename_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        c_str(Filename self)
        
        /**
         *
         */
        """
        pass

    def dsoFilename(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        dso_filename(str filename)
        
        /**
         *
         */
        """
        pass

    def dso_filename(self, str_filename): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        dso_filename(str filename)
        
        /**
         *
         */
        """
        pass

    def empty(self, Filename_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        empty(Filename self)
        
        /**
         *
         */
        """
        pass

    def executableFilename(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        executable_filename(str filename)
        
        /**
         *
         */
        """
        pass

    def executable_filename(self, str_filename): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        executable_filename(str filename)
        
        /**
         *
         */
        """
        pass

    def exists(self, Filename_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        exists(Filename self)
        
        /**
         * Returns true if the filename exists on the physical disk, false otherwise.
         * If the type is indicated to be executable, this also tests that the file has
         * execute permission.
         *
         * @see VirtualFileSystem::exists() for checking whether the filename exists in
         * the virtual file system.
         */
        """
        pass

    def expandFrom(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        expand_from(str user_string, int type)
        
        /**
         * Returns the same thing as from_os_specific(), but embedded environment
         * variable references (e.g.  "$DMODELS/foo.txt") are expanded out.  It also
         * automatically elevates the file to its true case if needed.
         */
        """
        pass

    def expand_from(self, str_user_string, int_type): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        expand_from(str user_string, int type)
        
        /**
         * Returns the same thing as from_os_specific(), but embedded environment
         * variable references (e.g.  "$DMODELS/foo.txt") are expanded out.  It also
         * automatically elevates the file to its true case if needed.
         */
        """
        pass

    def findOnSearchpath(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        find_on_searchpath(const Filename self, const DSearchPath searchpath)
        
        /**
         * Performs the reverse of the resolve_filename() operation: assuming that the
         * current filename is fully-specified pathname (i.e.  beginning with '/'),
         * look on the indicated search path for a directory under which the file can
         * be found.  When found, adjust the Filename to be relative to the indicated
         * directory name.
         *
         * Returns the index of the directory on the searchpath at which the file was
         * found, or -1 if it was not found.
         */
        """
        pass

    def find_on_searchpath(self, const_Filename_self, const_DSearchPath_searchpath): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        find_on_searchpath(const Filename self, const DSearchPath searchpath)
        
        /**
         * Performs the reverse of the resolve_filename() operation: assuming that the
         * current filename is fully-specified pathname (i.e.  beginning with '/'),
         * look on the indicated search path for a directory under which the file can
         * be found.  When found, adjust the Filename to be relative to the indicated
         * directory name.
         *
         * Returns the index of the directory on the searchpath at which the file was
         * found, or -1 if it was not found.
         */
        """
        pass

    def fromOsSpecific(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        from_os_specific(str os_specific, int type)
        
        /**
         * This named constructor returns a Panda-style filename (that is, using
         * forward slashes, and no drive letter) based on the supplied filename string
         * that describes a filename in the local system conventions (for instance, on
         * Windows, it may use backslashes or begin with a drive letter and a colon).
         *
         * Use this function to create a Filename from an externally-given filename
         * string.  Use to_os_specific() again later to reconvert it back to the local
         * operating system's conventions.
         *
         * This function will do the right thing even if the filename is partially
         * local conventions and partially Panda conventions; e.g.  some backslashes
         * and some forward slashes.
         */
        """
        pass

    def fromOsSpecificW(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        from_os_specific_w(unicode os_specific, int type)
        
        /**
         * The wide-string variant of from_os_specific(). Returns a new Filename,
         * converted from an os-specific wide-character string.
         */
        """
        pass

    def from_os_specific(self, str_os_specific, int_type): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        from_os_specific(str os_specific, int type)
        
        /**
         * This named constructor returns a Panda-style filename (that is, using
         * forward slashes, and no drive letter) based on the supplied filename string
         * that describes a filename in the local system conventions (for instance, on
         * Windows, it may use backslashes or begin with a drive letter and a colon).
         *
         * Use this function to create a Filename from an externally-given filename
         * string.  Use to_os_specific() again later to reconvert it back to the local
         * operating system's conventions.
         *
         * This function will do the right thing even if the filename is partially
         * local conventions and partially Panda conventions; e.g.  some backslashes
         * and some forward slashes.
         */
        """
        pass

    def from_os_specific_w(self, unicode_os_specific, int_type): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        from_os_specific_w(unicode os_specific, int type)
        
        /**
         * The wide-string variant of from_os_specific(). Returns a new Filename,
         * converted from an os-specific wide-character string.
         */
        """
        pass

    def Fspath(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        __fspath__(Filename self)
        """
        pass

    def getAccessTimestamp(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_access_timestamp(Filename self)
        
        /**
         * Returns a time_t value that represents the time the file was last accessed,
         * if this information is available.  See also get_timestamp(), which returns
         * the last modification time.
         */
        """
        pass

    def getBasename(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_basename(Filename self)
        
        /**
         * Returns the basename part of the filename.  This is everything in the
         * filename after the rightmost slash, including any extensions.
         */
        """
        pass

    def getBasenameWoExtension(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_basename_wo_extension(Filename self)
        
        /**
         * Returns the basename part of the filename, without the file extension.
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getCommonAppdataDirectory(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_common_appdata_directory()
        
        /**
         * Returns a path to a system-defined directory appropriate for creating a
         * subdirectory for storing application-specific data, common to all users.
         */
        """
        pass

    def getDirname(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_dirname(Filename self)
        
        /**
         * Returns the directory part of the filename.  This is everything in the
         * filename up to, but not including the rightmost slash.
         */
        """
        pass

    def getExtension(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_extension(Filename self)
        
        /**
         * Returns the file extension.  This is everything after the rightmost dot, if
         * there is one, or the empty string if there is not.
         */
        """
        pass

    def getFilenameIndex(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_filename_index(Filename self, int index)
        
        /**
         * If the pattern flag is set for this Filename and the filename string
         * actually includes a sequence of hash marks, then this returns a new
         * Filename with the sequence of hash marks replaced by the indicated index
         * number.
         *
         * If the pattern flag is not set for this Filename or it does not contain a
         * sequence of hash marks, this quietly returns the original filename.
         */
        """
        pass

    def getFileSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_file_size(Filename self)
        
        /**
         * Returns the size of the file in bytes, or 0 if there is an error.
         */
        """
        pass

    def getFilesystemEncoding(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_filesystem_encoding()
        
        /**
         * Specifies the default encoding to be used for all subsequent Filenames
         * objects.  See set_filesystem_encoding().
         */
        """
        pass

    def getFullpath(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_fullpath(Filename self)
        
        // Or, you can use any of these.
        
        /**
         * Returns the entire filename: directory, basename, extension.  This is the
         * same thing returned by the string typecast operator.
         */
        """
        pass

    def getFullpathW(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_fullpath_w(Filename self)
        
        /**
         * Returns the entire filename as a wide-character string.
         */
        """
        pass

    def getFullpathWoExtension(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_fullpath_wo_extension(Filename self)
        
        /**
         * Returns the full filename--directory and basename parts--except for the
         * extension.
         */
        """
        pass

    def getHash(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_hash(Filename self)
        
        /**
         * Returns a hash code that attempts to be mostly unique for different
         * Filenames.
         */
        """
        pass

    def getHashToEnd(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_hash_to_end(Filename self)
        
        /**
         * Returns the part of the filename beginning at the hash sequence (if any),
         * and continuing to the end of the filename.
         */
        """
        pass

    def getHomeDirectory(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_home_directory()
        
        /**
         * Returns a path to the user's home directory, if such a thing makes sense in
         * the current OS, or to the nearest equivalent.  This may or may not be
         * directly writable by the application.
         */
        """
        pass

    def getPattern(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_pattern(Filename self)
        
        /**
         * Returns the flag indicating whether this is a filename pattern.  See
         * set_pattern().
         */
        """
        pass

    def getTempDirectory(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_temp_directory()
        
        /**
         * Returns a path to a system-defined temporary directory.
         */
        """
        pass

    def getTimestamp(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_timestamp(Filename self)
        
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

    def getType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_type(Filename self)
        
        /**
         * Returns the type of the file represented by the filename, as previously set
         * by set_type().
         */
        """
        pass

    def getUserAppdataDirectory(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_user_appdata_directory()
        
        /**
         * Returns a path to a system-defined directory appropriate for creating a
         * subdirectory for storing application-specific data, specific to the current
         * user.
         */
        """
        pass

    def get_access_timestamp(self, Filename_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_access_timestamp(Filename self)
        
        /**
         * Returns a time_t value that represents the time the file was last accessed,
         * if this information is available.  See also get_timestamp(), which returns
         * the last modification time.
         */
        """
        pass

    def get_basename(self, Filename_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_basename(Filename self)
        
        /**
         * Returns the basename part of the filename.  This is everything in the
         * filename after the rightmost slash, including any extensions.
         */
        """
        pass

    def get_basename_wo_extension(self, Filename_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_basename_wo_extension(Filename self)
        
        /**
         * Returns the basename part of the filename, without the file extension.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_common_appdata_directory(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_common_appdata_directory()
        
        /**
         * Returns a path to a system-defined directory appropriate for creating a
         * subdirectory for storing application-specific data, common to all users.
         */
        """
        pass

    def get_dirname(self, Filename_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_dirname(Filename self)
        
        /**
         * Returns the directory part of the filename.  This is everything in the
         * filename up to, but not including the rightmost slash.
         */
        """
        pass

    def get_extension(self, Filename_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_extension(Filename self)
        
        /**
         * Returns the file extension.  This is everything after the rightmost dot, if
         * there is one, or the empty string if there is not.
         */
        """
        pass

    def get_filename_index(self, Filename_self, int_index): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_filename_index(Filename self, int index)
        
        /**
         * If the pattern flag is set for this Filename and the filename string
         * actually includes a sequence of hash marks, then this returns a new
         * Filename with the sequence of hash marks replaced by the indicated index
         * number.
         *
         * If the pattern flag is not set for this Filename or it does not contain a
         * sequence of hash marks, this quietly returns the original filename.
         */
        """
        pass

    def get_filesystem_encoding(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_filesystem_encoding()
        
        /**
         * Specifies the default encoding to be used for all subsequent Filenames
         * objects.  See set_filesystem_encoding().
         */
        """
        pass

    def get_file_size(self, Filename_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_file_size(Filename self)
        
        /**
         * Returns the size of the file in bytes, or 0 if there is an error.
         */
        """
        pass

    def get_fullpath(self, Filename_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_fullpath(Filename self)
        
        // Or, you can use any of these.
        
        /**
         * Returns the entire filename: directory, basename, extension.  This is the
         * same thing returned by the string typecast operator.
         */
        """
        pass

    def get_fullpath_w(self, Filename_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_fullpath_w(Filename self)
        
        /**
         * Returns the entire filename as a wide-character string.
         */
        """
        pass

    def get_fullpath_wo_extension(self, Filename_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_fullpath_wo_extension(Filename self)
        
        /**
         * Returns the full filename--directory and basename parts--except for the
         * extension.
         */
        """
        pass

    def get_hash(self, Filename_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_hash(Filename self)
        
        /**
         * Returns a hash code that attempts to be mostly unique for different
         * Filenames.
         */
        """
        pass

    def get_hash_to_end(self, Filename_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_hash_to_end(Filename self)
        
        /**
         * Returns the part of the filename beginning at the hash sequence (if any),
         * and continuing to the end of the filename.
         */
        """
        pass

    def get_home_directory(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_home_directory()
        
        /**
         * Returns a path to the user's home directory, if such a thing makes sense in
         * the current OS, or to the nearest equivalent.  This may or may not be
         * directly writable by the application.
         */
        """
        pass

    def get_pattern(self, Filename_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_pattern(Filename self)
        
        /**
         * Returns the flag indicating whether this is a filename pattern.  See
         * set_pattern().
         */
        """
        pass

    def get_temp_directory(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_temp_directory()
        
        /**
         * Returns a path to a system-defined temporary directory.
         */
        """
        pass

    def get_timestamp(self, Filename_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_timestamp(Filename self)
        
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

    def get_type(self, Filename_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_type(Filename self)
        
        /**
         * Returns the type of the file represented by the filename, as previously set
         * by set_type().
         */
        """
        pass

    def get_user_appdata_directory(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_user_appdata_directory()
        
        /**
         * Returns a path to a system-defined directory appropriate for creating a
         * subdirectory for storing application-specific data, specific to the current
         * user.
         */
        """
        pass

    def hasHash(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_hash(Filename self)
        
        /**
         * Returns true if the filename is indicated to be a filename pattern (that
         * is, set_pattern(true) was called), and the filename pattern did include a
         * sequence of hash marks, or false if it was not a filename pattern or did
         * not include hash marks.  If this is true, then get_filename_index() will
         * return a different filename each time.
         */
        """
        pass

    def has_hash(self, Filename_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_hash(Filename self)
        
        /**
         * Returns true if the filename is indicated to be a filename pattern (that
         * is, set_pattern(true) was called), and the filename pattern did include a
         * sequence of hash marks, or false if it was not a filename pattern or did
         * not include hash marks.  If this is true, then get_filename_index() will
         * return a different filename each time.
         */
        """
        pass

    def isBinary(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_binary(Filename self)
        
        /**
         * Returns true if the Filename has been indicated to represent a binary file
         * via a previous call to set_binary().  It is possible that neither
         * is_binary() nor is_text() will be true, if neither set_binary() nor
         * set_text() was ever called.
         */
        """
        pass

    def isBinaryOrText(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_binary_or_text(Filename self)
        
        /**
         * Returns true either is_binary() or is_text() is true; that is, that the
         * filename has been specified as either binary or text.  If this is false,
         * the filename has not been specified.
         */
        """
        pass

    def isDirectory(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_directory(Filename self)
        
        /**
         * Returns true if the filename exists on the physical disk and is a directory
         * name, false otherwise.
         *
         * @see VirtualFileSystem::is_directory() for checking whether the filename
         * exists as a directory in the virtual file system.
         */
        """
        pass

    def isExecutable(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_executable(Filename self)
        
        /**
         * Returns true if the filename exists and is executable
         */
        """
        pass

    def isFullyQualified(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_fully_qualified(Filename self)
        
        /**
         * Returns true if the filename is fully qualified, e.g.  begins with a slash.
         * This is almost, but not quite, the same thing as !is_local().  It's not
         * exactly the same because a special case is made for filenames that begin
         * with a single dot followed by a slash--these are considered to be fully
         * qualified (they are explicitly relative to the current directory, and do
         * not refer to a filename on a search path somewhere).
         */
        """
        pass

    def isLocal(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_local(Filename self)
        
        /**
         * Returns true if the filename is local, e.g.  does not begin with a slash,
         * or false if the filename is fully specified from the root.
         */
        """
        pass

    def isRegularFile(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_regular_file(Filename self)
        
        /**
         * Returns true if the filename exists on the physical disk and is the name of
         * a regular file (i.e. not a directory or device), false otherwise.
         *
         * @see VirtualFileSystem::is_regular_file() for checking whether the filename
         * exists and is a regular file in the virtual file system.
         */
        """
        pass

    def isText(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_text(Filename self)
        
        /**
         * Returns true if the Filename has been indicated to represent a text file
         * via a previous call to set_text().  It is possible that neither is_binary()
         * nor is_text() will be true, if neither set_binary() nor set_text() was ever
         * called.
         */
        """
        pass

    def isWritable(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_writable(Filename self)
        
        /**
         * Returns true if the filename exists on the physical disk and is either a
         * directory or a regular file that can be written to, or false otherwise.
         */
        """
        pass

    def is_binary(self, Filename_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_binary(Filename self)
        
        /**
         * Returns true if the Filename has been indicated to represent a binary file
         * via a previous call to set_binary().  It is possible that neither
         * is_binary() nor is_text() will be true, if neither set_binary() nor
         * set_text() was ever called.
         */
        """
        pass

    def is_binary_or_text(self, Filename_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_binary_or_text(Filename self)
        
        /**
         * Returns true either is_binary() or is_text() is true; that is, that the
         * filename has been specified as either binary or text.  If this is false,
         * the filename has not been specified.
         */
        """
        pass

    def is_directory(self, Filename_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_directory(Filename self)
        
        /**
         * Returns true if the filename exists on the physical disk and is a directory
         * name, false otherwise.
         *
         * @see VirtualFileSystem::is_directory() for checking whether the filename
         * exists as a directory in the virtual file system.
         */
        """
        pass

    def is_executable(self, Filename_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_executable(Filename self)
        
        /**
         * Returns true if the filename exists and is executable
         */
        """
        pass

    def is_fully_qualified(self, Filename_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_fully_qualified(Filename self)
        
        /**
         * Returns true if the filename is fully qualified, e.g.  begins with a slash.
         * This is almost, but not quite, the same thing as !is_local().  It's not
         * exactly the same because a special case is made for filenames that begin
         * with a single dot followed by a slash--these are considered to be fully
         * qualified (they are explicitly relative to the current directory, and do
         * not refer to a filename on a search path somewhere).
         */
        """
        pass

    def is_local(self, Filename_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_local(Filename self)
        
        /**
         * Returns true if the filename is local, e.g.  does not begin with a slash,
         * or false if the filename is fully specified from the root.
         */
        """
        pass

    def is_regular_file(self, Filename_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_regular_file(Filename self)
        
        /**
         * Returns true if the filename exists on the physical disk and is the name of
         * a regular file (i.e. not a directory or device), false otherwise.
         *
         * @see VirtualFileSystem::is_regular_file() for checking whether the filename
         * exists and is a regular file in the virtual file system.
         */
        """
        pass

    def is_text(self, Filename_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_text(Filename self)
        
        /**
         * Returns true if the Filename has been indicated to represent a text file
         * via a previous call to set_text().  It is possible that neither is_binary()
         * nor is_text() will be true, if neither set_binary() nor set_text() was ever
         * called.
         */
        """
        pass

    def is_writable(self, Filename_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_writable(Filename self)
        
        /**
         * Returns true if the filename exists on the physical disk and is either a
         * directory or a regular file that can be written to, or false otherwise.
         */
        """
        pass

    def length(self, Filename_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        length(Filename self)
        
        /**
         *
         */
        """
        pass

    def makeAbsolute(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_absolute(const Filename self)
        make_absolute(const Filename self, const Filename start_directory)
        
        /**
         * Converts the filename to a fully-qualified pathname from the root (if it is
         * a relative pathname), and then standardizes it (see standardize()).
         *
         * This is sometimes a little problematic, since it may convert the file to
         * its 'true' absolute pathname, which could be an ugly NFS-named file,
         * irrespective of symbolic links (e.g.
         * /.automount/dimbo/root/usr2/fit/people/drose instead of /fit/people/drose);
         * besides being ugly, filenames like this may not be consistent across
         * multiple different platforms.
         */
        
        /**
         * Converts the filename to a fully-qualified filename from the root (if it is
         * a relative filename), and then standardizes it (see standardize()).  This
         * flavor accepts a specific starting directory that the filename is known to
         * be relative to.
         */
        """
        pass

    def makeCanonical(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_canonical(const Filename self)
        
        /**
         * Converts this filename to a canonical name by replacing the directory part
         * with the fully-qualified directory part.  This is done by changing to that
         * directory and calling getcwd().
         *
         * This has the effect of (a) converting relative paths to absolute paths (but
         * see make_absolute() if this is the only effect you want), and (b) always
         * resolving a given directory name to the same string, even if different
         * symbolic links are traversed, and (c) changing nice symbolic-link paths
         * like fit/people/drose to ugly NFS automounter names like
         * hosts/dimbo/usr2/fit/people/drose.  This can be troubling, but sometimes
         * this is exactly what you want, particularly if you're about to call
         * make_relative_to() between two filenames.
         *
         * The return value is true if successful, or false on failure (usually
         * because the directory name does not exist or cannot be chdir'ed into).
         */
        """
        pass

    def makeDir(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_dir(Filename self)
        
        /**
         * Creates all the directories in the path to the file specified in the
         * filename, except for the basename itself.  This assumes that the Filename
         * contains the name of a file, not a directory name; it ensures that the
         * directory containing the file exists.
         *
         * However, if the filename ends in a slash, it assumes the Filename
         * represents the name of a directory, and creates all the paths.
         */
        """
        pass

    def makeRelativeTo(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_relative_to(const Filename self, Filename directory, bool allow_backups)
        
        /**
         * Adjusts this filename, which must be a fully-specified pathname beginning
         * with a slash, to make it a relative filename, relative to the fully-
         * specified directory indicated (which must also begin with, and may or may
         * not end with, a slash--a terminating slash is ignored).
         *
         * This only performs a string comparsion, so it may be wise to call
         * make_canonical() on both filenames before calling make_relative_to().
         *
         * If allow_backups is false, the filename will only be adjusted to be made
         * relative if it is already somewhere within or below the indicated
         * directory.  If allow_backups is true, it will be adjusted in all cases,
         * even if this requires putting a series of .. characters before the filename
         * --unless it would have to back all the way up to the root.
         *
         * Returns true if the file was adjusted, false if it was not.
         */
        """
        pass

    def makeTrueCase(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_true_case(const Filename self)
        
        /**
         * On a case-insensitive operating system (e.g.  Windows), this method looks
         * up the file in the file system and resets the Filename to represent the
         * actual case of the file as it exists on the disk.  The return value is true
         * if the file exists and the conversion can be made, or false if there is
         * some error.
         *
         * On a case-sensitive operating system, this method does nothing and always
         * returns true.
         *
         * An empty filename is considered to exist in this case.
         */
        """
        pass

    def make_absolute(self, const_Filename_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_absolute(const Filename self)
        make_absolute(const Filename self, const Filename start_directory)
        
        /**
         * Converts the filename to a fully-qualified pathname from the root (if it is
         * a relative pathname), and then standardizes it (see standardize()).
         *
         * This is sometimes a little problematic, since it may convert the file to
         * its 'true' absolute pathname, which could be an ugly NFS-named file,
         * irrespective of symbolic links (e.g.
         * /.automount/dimbo/root/usr2/fit/people/drose instead of /fit/people/drose);
         * besides being ugly, filenames like this may not be consistent across
         * multiple different platforms.
         */
        
        /**
         * Converts the filename to a fully-qualified filename from the root (if it is
         * a relative filename), and then standardizes it (see standardize()).  This
         * flavor accepts a specific starting directory that the filename is known to
         * be relative to.
         */
        """
        pass

    def make_canonical(self, const_Filename_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_canonical(const Filename self)
        
        /**
         * Converts this filename to a canonical name by replacing the directory part
         * with the fully-qualified directory part.  This is done by changing to that
         * directory and calling getcwd().
         *
         * This has the effect of (a) converting relative paths to absolute paths (but
         * see make_absolute() if this is the only effect you want), and (b) always
         * resolving a given directory name to the same string, even if different
         * symbolic links are traversed, and (c) changing nice symbolic-link paths
         * like fit/people/drose to ugly NFS automounter names like
         * hosts/dimbo/usr2/fit/people/drose.  This can be troubling, but sometimes
         * this is exactly what you want, particularly if you're about to call
         * make_relative_to() between two filenames.
         *
         * The return value is true if successful, or false on failure (usually
         * because the directory name does not exist or cannot be chdir'ed into).
         */
        """
        pass

    def make_dir(self, Filename_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_dir(Filename self)
        
        /**
         * Creates all the directories in the path to the file specified in the
         * filename, except for the basename itself.  This assumes that the Filename
         * contains the name of a file, not a directory name; it ensures that the
         * directory containing the file exists.
         *
         * However, if the filename ends in a slash, it assumes the Filename
         * represents the name of a directory, and creates all the paths.
         */
        """
        pass

    def make_relative_to(self, const_Filename_self, Filename_directory, bool_allow_backups): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_relative_to(const Filename self, Filename directory, bool allow_backups)
        
        /**
         * Adjusts this filename, which must be a fully-specified pathname beginning
         * with a slash, to make it a relative filename, relative to the fully-
         * specified directory indicated (which must also begin with, and may or may
         * not end with, a slash--a terminating slash is ignored).
         *
         * This only performs a string comparsion, so it may be wise to call
         * make_canonical() on both filenames before calling make_relative_to().
         *
         * If allow_backups is false, the filename will only be adjusted to be made
         * relative if it is already somewhere within or below the indicated
         * directory.  If allow_backups is true, it will be adjusted in all cases,
         * even if this requires putting a series of .. characters before the filename
         * --unless it would have to back all the way up to the root.
         *
         * Returns true if the file was adjusted, false if it was not.
         */
        """
        pass

    def make_true_case(self, const_Filename_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_true_case(const Filename self)
        
        /**
         * On a case-insensitive operating system (e.g.  Windows), this method looks
         * up the file in the file system and resets the Filename to represent the
         * actual case of the file as it exists on the disk.  The return value is true
         * if the file exists and the conversion can be made, or false if there is
         * some error.
         *
         * On a case-sensitive operating system, this method does nothing and always
         * returns true.
         *
         * An empty filename is considered to exist in this case.
         */
        """
        pass

    def mkdir(self, Filename_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        mkdir(Filename self)
        
        /**
         * Creates the directory named by this filename.  Unlike make_dir(), this
         * assumes that the Filename contains the directory name itself.  Also, parent
         * directories are not automatically created; this function fails if any
         * parent directory is missing.
         */
        """
        pass

    def openAppend(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        open_append(Filename self, ofstream stream)
        open_append(Filename self, OFileStream stream)
        
        /**
         * Opens the indicated ofstream for writing the file, if possible.  Returns
         * true if successful, false otherwise.  This requires the setting of the
         * set_text()/set_binary() flags to open the file appropriately as indicated;
         * it is an error to call open_read() without first calling one of set_text()
         * or set_binary().
         */
        
        /**
         * Opens the indicated pifstream for writing the file, if possible.  Returns
         * true if successful, false otherwise.  This requires the setting of the
         * set_text()/set_binary() flags to open the file appropriately as indicated;
         * it is an error to call open_read() without first calling one of set_text()
         * or set_binary().
         */
        """
        pass

    def openRead(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        open_read(Filename self, ifstream stream)
        open_read(Filename self, IFileStream stream)
        
        /**
         * Opens the indicated ifstream for reading the file, if possible.  Returns
         * true if successful, false otherwise.  This requires the setting of the
         * set_text()/set_binary() flags to open the file appropriately as indicated;
         * it is an error to call open_read() without first calling one of set_text()
         * or set_binary().
         */
        
        /**
         * Opens the indicated pifstream for reading the file, if possible.  Returns
         * true if successful, false otherwise.  This requires the setting of the
         * set_text()/set_binary() flags to open the file appropriately as indicated;
         * it is an error to call open_read() without first calling one of set_text()
         * or set_binary().
         */
        """
        pass

    def openReadAppend(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        open_read_append(Filename self, FileStream stream)
        open_read_append(Filename self, fstream stream)
        
        /**
         * Opens the indicated ifstream for reading and writing the file, if possible;
         * writes are appended to the end of the file.  Returns true if successful,
         * false otherwise.  This requires the setting of the set_text()/set_binary()
         * flags to open the file appropriately as indicated; it is an error to call
         * open_read() without first calling one of set_text() or set_binary().
         */
        
        /**
         * Opens the indicated pfstream for reading and writing the file, if possible;
         * writes are appended to the end of the file.  Returns true if successful,
         * false otherwise.  This requires the setting of the set_text()/set_binary()
         * flags to open the file appropriately as indicated; it is an error to call
         * open_read() without first calling one of set_text() or set_binary().
         */
        """
        pass

    def openReadWrite(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        open_read_write(Filename self, fstream stream, bool truncate)
        open_read_write(Filename self, FileStream stream, bool truncate)
        
        /**
         * Opens the indicated fstream for read/write access to the file, if possible.
         * Returns true if successful, false otherwise.  This requires the setting of
         * the set_text()/set_binary() flags to open the file appropriately as
         * indicated; it is an error to call open_read_write() without first calling
         * one of set_text() or set_binary().
         */
        
        /**
         * Opens the indicated fstream for read/write access to the file, if possible.
         * Returns true if successful, false otherwise.  This requires the setting of
         * the set_text()/set_binary() flags to open the file appropriately as
         * indicated; it is an error to call open_read_write() without first calling
         * one of set_text() or set_binary().
         */
        """
        pass

    def openWrite(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        open_write(Filename self, ofstream stream, bool truncate)
        open_write(Filename self, OFileStream stream, bool truncate)
        
        /**
         * Opens the indicated ifstream for writing the file, if possible.  Returns
         * true if successful, false otherwise.  This requires the setting of the
         * set_text()/set_binary() flags to open the file appropriately as indicated;
         * it is an error to call open_read() without first calling one of set_text()
         * or set_binary().
         *
         * If truncate is true, the file is truncated to zero length upon opening it,
         * if it already exists.  Otherwise, the file is kept at its original length.
         */
        
        /**
         * Opens the indicated pifstream for writing the file, if possible.  Returns
         * true if successful, false otherwise.  This requires the setting of the
         * set_text()/set_binary() flags to open the file appropriately as indicated;
         * it is an error to call open_read() without first calling one of set_text()
         * or set_binary().
         *
         * If truncate is true, the file is truncated to zero length upon opening it,
         * if it already exists.  Otherwise, the file is kept at its original length.
         */
        """
        pass

    def open_append(self, Filename_self, ofstream_stream): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        open_append(Filename self, ofstream stream)
        open_append(Filename self, OFileStream stream)
        
        /**
         * Opens the indicated ofstream for writing the file, if possible.  Returns
         * true if successful, false otherwise.  This requires the setting of the
         * set_text()/set_binary() flags to open the file appropriately as indicated;
         * it is an error to call open_read() without first calling one of set_text()
         * or set_binary().
         */
        
        /**
         * Opens the indicated pifstream for writing the file, if possible.  Returns
         * true if successful, false otherwise.  This requires the setting of the
         * set_text()/set_binary() flags to open the file appropriately as indicated;
         * it is an error to call open_read() without first calling one of set_text()
         * or set_binary().
         */
        """
        pass

    def open_read(self, Filename_self, ifstream_stream): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        open_read(Filename self, ifstream stream)
        open_read(Filename self, IFileStream stream)
        
        /**
         * Opens the indicated ifstream for reading the file, if possible.  Returns
         * true if successful, false otherwise.  This requires the setting of the
         * set_text()/set_binary() flags to open the file appropriately as indicated;
         * it is an error to call open_read() without first calling one of set_text()
         * or set_binary().
         */
        
        /**
         * Opens the indicated pifstream for reading the file, if possible.  Returns
         * true if successful, false otherwise.  This requires the setting of the
         * set_text()/set_binary() flags to open the file appropriately as indicated;
         * it is an error to call open_read() without first calling one of set_text()
         * or set_binary().
         */
        """
        pass

    def open_read_append(self, Filename_self, FileStream_stream): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        open_read_append(Filename self, FileStream stream)
        open_read_append(Filename self, fstream stream)
        
        /**
         * Opens the indicated ifstream for reading and writing the file, if possible;
         * writes are appended to the end of the file.  Returns true if successful,
         * false otherwise.  This requires the setting of the set_text()/set_binary()
         * flags to open the file appropriately as indicated; it is an error to call
         * open_read() without first calling one of set_text() or set_binary().
         */
        
        /**
         * Opens the indicated pfstream for reading and writing the file, if possible;
         * writes are appended to the end of the file.  Returns true if successful,
         * false otherwise.  This requires the setting of the set_text()/set_binary()
         * flags to open the file appropriately as indicated; it is an error to call
         * open_read() without first calling one of set_text() or set_binary().
         */
        """
        pass

    def open_read_write(self, Filename_self, fstream_stream, bool_truncate): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        open_read_write(Filename self, fstream stream, bool truncate)
        open_read_write(Filename self, FileStream stream, bool truncate)
        
        /**
         * Opens the indicated fstream for read/write access to the file, if possible.
         * Returns true if successful, false otherwise.  This requires the setting of
         * the set_text()/set_binary() flags to open the file appropriately as
         * indicated; it is an error to call open_read_write() without first calling
         * one of set_text() or set_binary().
         */
        
        /**
         * Opens the indicated fstream for read/write access to the file, if possible.
         * Returns true if successful, false otherwise.  This requires the setting of
         * the set_text()/set_binary() flags to open the file appropriately as
         * indicated; it is an error to call open_read_write() without first calling
         * one of set_text() or set_binary().
         */
        """
        pass

    def open_write(self, Filename_self, ofstream_stream, bool_truncate): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        open_write(Filename self, ofstream stream, bool truncate)
        open_write(Filename self, OFileStream stream, bool truncate)
        
        /**
         * Opens the indicated ifstream for writing the file, if possible.  Returns
         * true if successful, false otherwise.  This requires the setting of the
         * set_text()/set_binary() flags to open the file appropriately as indicated;
         * it is an error to call open_read() without first calling one of set_text()
         * or set_binary().
         *
         * If truncate is true, the file is truncated to zero length upon opening it,
         * if it already exists.  Otherwise, the file is kept at its original length.
         */
        
        /**
         * Opens the indicated pifstream for writing the file, if possible.  Returns
         * true if successful, false otherwise.  This requires the setting of the
         * set_text()/set_binary() flags to open the file appropriately as indicated;
         * it is an error to call open_read() without first calling one of set_text()
         * or set_binary().
         *
         * If truncate is true, the file is truncated to zero length upon opening it,
         * if it already exists.  Otherwise, the file is kept at its original length.
         */
        """
        pass

    def output(self, Filename_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(Filename self, ostream out)
        
        /**
         *
         */
        """
        pass

    def patternFilename(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        pattern_filename(str filename)
        
        /**
         * Constructs a filename that represents a sequence of numbered files.  See
         * set_pattern().
         */
        """
        pass

    def pattern_filename(self, str_filename): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        pattern_filename(str filename)
        
        /**
         * Constructs a filename that represents a sequence of numbered files.  See
         * set_pattern().
         */
        """
        pass

    def renameTo(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        rename_to(Filename self, const Filename other)
        
        /**
         * Renames the file to the indicated new filename.  If the new filename is in
         * a different directory, this will perform a move.  Returns true if
         * successful, false on failure.
         */
        """
        pass

    def rename_to(self, Filename_self, const_Filename_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        rename_to(Filename self, const Filename other)
        
        /**
         * Renames the file to the indicated new filename.  If the new filename is in
         * a different directory, this will perform a move.  Returns true if
         * successful, false on failure.
         */
        """
        pass

    def resolveFilename(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        resolve_filename(const Filename self, const DSearchPath searchpath, str default_extension)
        
        /**
         * Searches the given search path for the filename.  If it is found, updates
         * the filename to the full pathname found and returns true; otherwise,
         * returns false.
         */
        """
        pass

    def resolve_filename(self, const_Filename_self, const_DSearchPath_searchpath, str_default_extension): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        resolve_filename(const Filename self, const DSearchPath searchpath, str default_extension)
        
        /**
         * Searches the given search path for the filename.  If it is found, updates
         * the filename to the full pathname found and returns true; otherwise,
         * returns false.
         */
        """
        pass

    def rmdir(self, Filename_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        rmdir(Filename self)
        
        /**
         * The inverse of mkdir(): this removes the directory named by this Filename,
         * if it is in fact a directory.
         */
        """
        pass

    def scanDirectory(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        scan_directory(Filename self)
        
        /**
         * Attempts to open the named filename as if it were a directory and looks for
         * the non-hidden files within the directory.  Fills the given vector up with
         * the sorted list of filenames that are local to this directory.
         *
         * It is the user's responsibility to ensure that the contents vector is empty
         * before making this call; otherwise, the new files will be appended to it.
         *
         * Returns true on success, false if the directory could not be read for some
         * reason.
         */
        """
        pass

    def scan_directory(self, Filename_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        scan_directory(Filename self)
        
        /**
         * Attempts to open the named filename as if it were a directory and looks for
         * the non-hidden files within the directory.  Fills the given vector up with
         * the sorted list of filenames that are local to this directory.
         *
         * It is the user's responsibility to ensure that the contents vector is empty
         * before making this call; otherwise, the new files will be appended to it.
         *
         * Returns true on success, false if the directory could not be read for some
         * reason.
         */
        """
        pass

    def setBasename(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_basename(const Filename self, str s)
        
        /**
         * Replaces the basename part of the filename.  This is everything in the
         * filename after the rightmost slash, including any extensions.
         */
        """
        pass

    def setBasenameWoExtension(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_basename_wo_extension(const Filename self, str s)
        
        /**
         * Replaces the basename part of the filename, without the file extension.
         */
        """
        pass

    def setBinary(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_binary(const Filename self)
        
        // Setting these flags appropriately is helpful when opening or searching
        // for a file; it helps the Filename resolve OS-specific conventions (for
        // instance, that dynamic library names should perhaps be changed from .so
        // to .dll).
        
        /**
         * Indicates that the filename represents a binary file.  This is primarily
         * relevant to the read_file() and write_file() methods, so they can set the
         * appropriate flags to the OS.
         */
        """
        pass

    def setDirname(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_dirname(const Filename self, str s)
        
        /**
         * Replaces the directory part of the filename.  This is everything in the
         * filename up to, but not including the rightmost slash.
         */
        """
        pass

    def setExtension(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_extension(const Filename self, str s)
        
        /**
         * Replaces the file extension.  This is everything after the rightmost dot,
         * if there is one, or the empty string if there is not.
         */
        """
        pass

    def setFilesystemEncoding(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_filesystem_encoding(int encoding)
        
        /**
         * Specifies the default encoding to be used for all subsequent Filenames.
         * This is used to represent wide-character (Unicode) filenames internally.
         * On non-Windows-based systems, the encoded filename is also passed to the
         * underlying operating system.
         */
        """
        pass

    def setFullpath(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_fullpath(const Filename self, str s)
        
        // You can also use any of these to reassign pieces of the filename.
        
        /**
         * Replaces the entire filename: directory, basename, extension.  This can
         * also be achieved with the assignment operator.
         */
        """
        pass

    def setFullpathWoExtension(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_fullpath_wo_extension(const Filename self, str s)
        
        /**
         * Replaces the full filename--directory and basename parts--except for the
         * extension.
         */
        """
        pass

    def setHashToEnd(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_hash_to_end(const Filename self, str s)
        
        /**
         * Replaces the part of the filename from the beginning of the hash sequence
         * to the end of the filename.
         */
        """
        pass

    def setPattern(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_pattern(const Filename self, bool pattern)
        
        /**
         * Sets the flag indicating whether this is a filename pattern.  When this is
         * true, the filename is understood to be a placeholder for a numbered
         * sequence of filename, such as an image sequence.  In this case, a sequence
         * of one or more hash characters ("#") should appear in the filename string;
         * these characters will be filled in with the corresponding number (or more)
         * of digits representing the sequence number.  Sequence numbers always begin
         * counting at 0.
         *
         * When this is true, methods like has_hash() and get_hash_to_end() and
         * get_filename_index() may be called.  Methods like is_exists() will
         * implicitly test for existance of filename sequence 0.
         */
        """
        pass

    def setText(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_text(const Filename self)
        
        /**
         * Indicates that the filename represents a text file.  This is primarily
         * relevant to the read_file() and write_file() methods, so they can set the
         * appropriate flags to the OS.
         */
        """
        pass

    def setType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_type(const Filename self, int type)
        
        /**
         * Sets the type of the file represented by the filename.  This is useful for
         * to_os_specific(), resolve_filename(), test_existence(), and all such real-
         * world access functions.  It helps the Filename know how to map the internal
         * filename to the OS-specific filename (for instance, maybe executables
         * should have an .exe extension).
         */
        """
        pass

    def set_basename(self, const_Filename_self, str_s): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_basename(const Filename self, str s)
        
        /**
         * Replaces the basename part of the filename.  This is everything in the
         * filename after the rightmost slash, including any extensions.
         */
        """
        pass

    def set_basename_wo_extension(self, const_Filename_self, str_s): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_basename_wo_extension(const Filename self, str s)
        
        /**
         * Replaces the basename part of the filename, without the file extension.
         */
        """
        pass

    def set_binary(self, const_Filename_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_binary(const Filename self)
        
        // Setting these flags appropriately is helpful when opening or searching
        // for a file; it helps the Filename resolve OS-specific conventions (for
        // instance, that dynamic library names should perhaps be changed from .so
        // to .dll).
        
        /**
         * Indicates that the filename represents a binary file.  This is primarily
         * relevant to the read_file() and write_file() methods, so they can set the
         * appropriate flags to the OS.
         */
        """
        pass

    def set_dirname(self, const_Filename_self, str_s): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_dirname(const Filename self, str s)
        
        /**
         * Replaces the directory part of the filename.  This is everything in the
         * filename up to, but not including the rightmost slash.
         */
        """
        pass

    def set_extension(self, const_Filename_self, str_s): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_extension(const Filename self, str s)
        
        /**
         * Replaces the file extension.  This is everything after the rightmost dot,
         * if there is one, or the empty string if there is not.
         */
        """
        pass

    def set_filesystem_encoding(self, int_encoding): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_filesystem_encoding(int encoding)
        
        /**
         * Specifies the default encoding to be used for all subsequent Filenames.
         * This is used to represent wide-character (Unicode) filenames internally.
         * On non-Windows-based systems, the encoded filename is also passed to the
         * underlying operating system.
         */
        """
        pass

    def set_fullpath(self, const_Filename_self, str_s): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_fullpath(const Filename self, str s)
        
        // You can also use any of these to reassign pieces of the filename.
        
        /**
         * Replaces the entire filename: directory, basename, extension.  This can
         * also be achieved with the assignment operator.
         */
        """
        pass

    def set_fullpath_wo_extension(self, const_Filename_self, str_s): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_fullpath_wo_extension(const Filename self, str s)
        
        /**
         * Replaces the full filename--directory and basename parts--except for the
         * extension.
         */
        """
        pass

    def set_hash_to_end(self, const_Filename_self, str_s): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_hash_to_end(const Filename self, str s)
        
        /**
         * Replaces the part of the filename from the beginning of the hash sequence
         * to the end of the filename.
         */
        """
        pass

    def set_pattern(self, const_Filename_self, bool_pattern): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_pattern(const Filename self, bool pattern)
        
        /**
         * Sets the flag indicating whether this is a filename pattern.  When this is
         * true, the filename is understood to be a placeholder for a numbered
         * sequence of filename, such as an image sequence.  In this case, a sequence
         * of one or more hash characters ("#") should appear in the filename string;
         * these characters will be filled in with the corresponding number (or more)
         * of digits representing the sequence number.  Sequence numbers always begin
         * counting at 0.
         *
         * When this is true, methods like has_hash() and get_hash_to_end() and
         * get_filename_index() may be called.  Methods like is_exists() will
         * implicitly test for existance of filename sequence 0.
         */
        """
        pass

    def set_text(self, const_Filename_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_text(const Filename self)
        
        /**
         * Indicates that the filename represents a text file.  This is primarily
         * relevant to the read_file() and write_file() methods, so they can set the
         * appropriate flags to the OS.
         */
        """
        pass

    def set_type(self, const_Filename_self, int_type): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_type(const Filename self, int type)
        
        /**
         * Sets the type of the file represented by the filename.  This is useful for
         * to_os_specific(), resolve_filename(), test_existence(), and all such real-
         * world access functions.  It helps the Filename know how to map the internal
         * filename to the OS-specific filename (for instance, maybe executables
         * should have an .exe extension).
         */
        """
        pass

    def standardize(self, const_Filename_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        standardize(const Filename self)
        
        /**
         * Converts the filename to standard form by replacing consecutive slashes
         * with a single slash, removing a trailing slash if present, and backing up
         * over .. sequences within the filename where possible.
         */
        """
        pass

    def substr(self, Filename_self, int_begin): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        substr(Filename self, int begin)
        substr(Filename self, int begin, int end)
        
        /**
         *
         */
        
        /**
         *
         */
        """
        pass

    def temporary(self, str_dirname, str_prefix, str_suffix, int_type): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        temporary(str dirname, str prefix, str suffix, int type)
        
        /**
         * Generates a temporary filename within the indicated directory, using the
         * indicated prefix.  If the directory is empty, a system-defined directory is
         * chosen instead.
         *
         * The generated filename did not exist when the Filename checked, but since
         * it does not specifically create the file, it is possible that another
         * process could simultaneously create a file by the same name.
         */
        """
        pass

    def textFilename(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        text_filename(const Filename filename)
        text_filename(str filename)
        
        // Static constructors to explicitly create a filename that refers to a text
        // or binary file.  This is in lieu of calling set_text() or set_binary() or
        // set_type().
        
        /**
         *
         */
        
        /**
         *
         */
        """
        pass

    def text_filename(self, const_Filename_filename): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        text_filename(const Filename filename)
        text_filename(str filename)
        
        // Static constructors to explicitly create a filename that refers to a text
        // or binary file.  This is in lieu of calling set_text() or set_binary() or
        // set_type().
        
        /**
         *
         */
        
        /**
         *
         */
        """
        pass

    def toOsGeneric(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        to_os_generic(Filename self)
        
        /**
         * This is similar to to_os_specific(), but it is designed to generate a
         * filename that can be understood on as many platforms as possible.  Since
         * Windows can usually understand a forward-slash-delimited filename, this
         * means it does the same thing as to_os_specific(), but it uses forward
         * slashes instead of backslashes.
         *
         * This method has a pretty limited use; it should generally be used for
         * writing file references to a file that might be read on any operating
         * system.
         */
        """
        pass

    def toOsLongName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        to_os_long_name(Filename self)
        
        /**
         * This is the opposite of to_os_short_name(): it returns the "long name" of
         * the filename, if the filename exists.  On non-Windows platforms, this
         * returns the same thing as to_os_specific().
         */
        """
        pass

    def toOsShortName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        to_os_short_name(Filename self)
        
        /**
         * This works like to_os_generic(), but it returns the "short name" version of
         * the filename, if it exists, or the original filename otherwise.
         *
         * On Windows platforms, this returns the 8.3 filename version of the given
         * filename, if the file exists, and the same thing as to_os_specific()
         * otherwise.  On non-Windows platforms, this always returns the same thing as
         * to_os_specific().
         */
        """
        pass

    def toOsSpecific(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        to_os_specific(Filename self)
        
        /**
         * Converts the filename from our generic Unix-like convention (forward
         * slashes starting with the root at '/') to the corresponding filename in the
         * local operating system (slashes in the appropriate direction, starting with
         * the root at C:\, for instance).  Returns the string representing the
         * converted filename, but does not change the Filename itself.
         *
         * See also from_os_specific().
         */
        """
        pass

    def toOsSpecificW(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        to_os_specific_w(Filename self)
        
        /**
         * The wide-string variant on to_os_specific().
         */
        """
        pass

    def touch(self, Filename_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        touch(Filename self)
        
        /**
         * Updates the modification time of the file to the current time.  If the file
         * does not already exist, it will be created.  Returns true if successful,
         * false if there is an error.
         */
        """
        pass

    def to_os_generic(self, Filename_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        to_os_generic(Filename self)
        
        /**
         * This is similar to to_os_specific(), but it is designed to generate a
         * filename that can be understood on as many platforms as possible.  Since
         * Windows can usually understand a forward-slash-delimited filename, this
         * means it does the same thing as to_os_specific(), but it uses forward
         * slashes instead of backslashes.
         *
         * This method has a pretty limited use; it should generally be used for
         * writing file references to a file that might be read on any operating
         * system.
         */
        """
        pass

    def to_os_long_name(self, Filename_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        to_os_long_name(Filename self)
        
        /**
         * This is the opposite of to_os_short_name(): it returns the "long name" of
         * the filename, if the filename exists.  On non-Windows platforms, this
         * returns the same thing as to_os_specific().
         */
        """
        pass

    def to_os_short_name(self, Filename_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        to_os_short_name(Filename self)
        
        /**
         * This works like to_os_generic(), but it returns the "short name" version of
         * the filename, if it exists, or the original filename otherwise.
         *
         * On Windows platforms, this returns the 8.3 filename version of the given
         * filename, if the file exists, and the same thing as to_os_specific()
         * otherwise.  On non-Windows platforms, this always returns the same thing as
         * to_os_specific().
         */
        """
        pass

    def to_os_specific(self, Filename_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        to_os_specific(Filename self)
        
        /**
         * Converts the filename from our generic Unix-like convention (forward
         * slashes starting with the root at '/') to the corresponding filename in the
         * local operating system (slashes in the appropriate direction, starting with
         * the root at C:\, for instance).  Returns the string representing the
         * converted filename, but does not change the Filename itself.
         *
         * See also from_os_specific().
         */
        """
        pass

    def to_os_specific_w(self, Filename_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        to_os_specific_w(Filename self)
        
        /**
         * The wide-string variant on to_os_specific().
         */
        """
        pass

    def unlink(self, Filename_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        unlink(Filename self)
        
        /**
         * Permanently deletes the file associated with the filename, if possible.
         * Returns true if successful, false if failure (for instance, because the
         * file did not exist, or because permissions were inadequate).
         */
        """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ True if self else False """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __fspath__(self, Filename_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        __fspath__(Filename self)
        """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __iadd__(self, *args, **kwargs): # real signature unknown
        """ Return self+=value. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __reduce__(self, Filename_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        __reduce__(Filename self)
        """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rtruediv__(self, *args, **kwargs): # real signature unknown
        """ Return value/self. """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    def __truediv__(self, *args, **kwargs): # real signature unknown
        """ Return self/value. """
        pass

    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        'Fspath': None, # (!) real value is "<method 'Fspath' of 'panda3d.core.Filename' objects>"
        'TDso': 1,
        'TExecutable': 2,
        'TGeneral': 0,
        'T_dso': 1,
        'T_executable': 2,
        'T_general': 0,
        '__add__': None, # (!) real value is "<slot wrapper '__add__' of 'panda3d.core.Filename' objects>"
        '__bool__': None, # (!) real value is "<slot wrapper '__bool__' of 'panda3d.core.Filename' objects>"
        '__doc__': "/**\n * The name of a file, such as a texture file or an Egg file.  Stores the full\n * pathname, and includes functions for extracting out the directory prefix\n * part and the file extension and stuff.\n *\n * A Filename is also aware of the mapping between the Unix-like filename\n * convention we use internally, and the local OS's specific filename\n * convention, and it knows how to perform basic OS-specific I/O, like testing\n * for file existence and searching a searchpath, as well as the best way to\n * open an fstream for reading or writing.\n *\n * Note that the methods of Filename that interact with the filesystem (such\n * as exists(), open_read(), etc.) directly interface with the operating system\n * and are not aware of Panda's virtual file system.  To interact with the VFS,\n * use the methods on VirtualFileSystem instead.\n */",
        '__eq__': None, # (!) real value is "<slot wrapper '__eq__' of 'panda3d.core.Filename' objects>"
        '__fspath__': None, # (!) real value is "<method '__fspath__' of 'panda3d.core.Filename' objects>"
        '__ge__': None, # (!) real value is "<slot wrapper '__ge__' of 'panda3d.core.Filename' objects>"
        '__getitem__': None, # (!) real value is "<slot wrapper '__getitem__' of 'panda3d.core.Filename' objects>"
        '__gt__': None, # (!) real value is "<slot wrapper '__gt__' of 'panda3d.core.Filename' objects>"
        '__hash__': None, # (!) real value is "<slot wrapper '__hash__' of 'panda3d.core.Filename' objects>"
        '__iadd__': None, # (!) real value is "<slot wrapper '__iadd__' of 'panda3d.core.Filename' objects>"
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.Filename' objects>"
        '__le__': None, # (!) real value is "<slot wrapper '__le__' of 'panda3d.core.Filename' objects>"
        '__lt__': None, # (!) real value is "<slot wrapper '__lt__' of 'panda3d.core.Filename' objects>"
        '__ne__': None, # (!) real value is "<slot wrapper '__ne__' of 'panda3d.core.Filename' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE25BA20>'
        '__radd__': None, # (!) real value is "<slot wrapper '__radd__' of 'panda3d.core.Filename' objects>"
        '__reduce__': None, # (!) real value is "<method '__reduce__' of 'panda3d.core.Filename' objects>"
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.Filename' objects>"
        '__rtruediv__': None, # (!) real value is "<slot wrapper '__rtruediv__' of 'panda3d.core.Filename' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.Filename' objects>"
        '__truediv__': None, # (!) real value is "<slot wrapper '__truediv__' of 'panda3d.core.Filename' objects>"
        'assign': None, # (!) real value is "<method 'assign' of 'panda3d.core.Filename' objects>"
        'binaryFilename': None, # (!) real value is '<staticmethod(<built-in method binaryFilename of type object at 0x00007FFCFE25BA20>)>'
        'binary_filename': None, # (!) real value is '<staticmethod(<built-in method binary_filename of type object at 0x00007FFCFE25BA20>)>'
        'cStr': None, # (!) real value is "<method 'cStr' of 'panda3d.core.Filename' objects>"
        'c_str': None, # (!) real value is "<method 'c_str' of 'panda3d.core.Filename' objects>"
        'chdir': None, # (!) real value is "<method 'chdir' of 'panda3d.core.Filename' objects>"
        'compareTimestamps': None, # (!) real value is "<method 'compareTimestamps' of 'panda3d.core.Filename' objects>"
        'compareTo': None, # (!) real value is "<method 'compareTo' of 'panda3d.core.Filename' objects>"
        'compare_timestamps': None, # (!) real value is "<method 'compare_timestamps' of 'panda3d.core.Filename' objects>"
        'compare_to': None, # (!) real value is "<method 'compare_to' of 'panda3d.core.Filename' objects>"
        'copyTo': None, # (!) real value is "<method 'copyTo' of 'panda3d.core.Filename' objects>"
        'copy_to': None, # (!) real value is "<method 'copy_to' of 'panda3d.core.Filename' objects>"
        'dsoFilename': None, # (!) real value is '<staticmethod(<built-in method dsoFilename of type object at 0x00007FFCFE25BA20>)>'
        'dso_filename': None, # (!) real value is '<staticmethod(<built-in method dso_filename of type object at 0x00007FFCFE25BA20>)>'
        'empty': None, # (!) real value is "<method 'empty' of 'panda3d.core.Filename' objects>"
        'executableFilename': None, # (!) real value is '<staticmethod(<built-in method executableFilename of type object at 0x00007FFCFE25BA20>)>'
        'executable_filename': None, # (!) real value is '<staticmethod(<built-in method executable_filename of type object at 0x00007FFCFE25BA20>)>'
        'exists': None, # (!) real value is "<method 'exists' of 'panda3d.core.Filename' objects>"
        'expandFrom': None, # (!) real value is '<staticmethod(<built-in method expandFrom of type object at 0x00007FFCFE25BA20>)>'
        'expand_from': None, # (!) real value is '<staticmethod(<built-in method expand_from of type object at 0x00007FFCFE25BA20>)>'
        'findOnSearchpath': None, # (!) real value is "<method 'findOnSearchpath' of 'panda3d.core.Filename' objects>"
        'find_on_searchpath': None, # (!) real value is "<method 'find_on_searchpath' of 'panda3d.core.Filename' objects>"
        'fromOsSpecific': None, # (!) real value is '<staticmethod(<built-in method fromOsSpecific of type object at 0x00007FFCFE25BA20>)>'
        'fromOsSpecificW': None, # (!) real value is '<staticmethod(<built-in method fromOsSpecificW of type object at 0x00007FFCFE25BA20>)>'
        'from_os_specific': None, # (!) real value is '<staticmethod(<built-in method from_os_specific of type object at 0x00007FFCFE25BA20>)>'
        'from_os_specific_w': None, # (!) real value is '<staticmethod(<built-in method from_os_specific_w of type object at 0x00007FFCFE25BA20>)>'
        'getAccessTimestamp': None, # (!) real value is "<method 'getAccessTimestamp' of 'panda3d.core.Filename' objects>"
        'getBasename': None, # (!) real value is "<method 'getBasename' of 'panda3d.core.Filename' objects>"
        'getBasenameWoExtension': None, # (!) real value is "<method 'getBasenameWoExtension' of 'panda3d.core.Filename' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE25BA20>)>'
        'getCommonAppdataDirectory': None, # (!) real value is '<staticmethod(<built-in method getCommonAppdataDirectory of type object at 0x00007FFCFE25BA20>)>'
        'getDirname': None, # (!) real value is "<method 'getDirname' of 'panda3d.core.Filename' objects>"
        'getExtension': None, # (!) real value is "<method 'getExtension' of 'panda3d.core.Filename' objects>"
        'getFileSize': None, # (!) real value is "<method 'getFileSize' of 'panda3d.core.Filename' objects>"
        'getFilenameIndex': None, # (!) real value is "<method 'getFilenameIndex' of 'panda3d.core.Filename' objects>"
        'getFilesystemEncoding': None, # (!) real value is '<staticmethod(<built-in method getFilesystemEncoding of type object at 0x00007FFCFE25BA20>)>'
        'getFullpath': None, # (!) real value is "<method 'getFullpath' of 'panda3d.core.Filename' objects>"
        'getFullpathW': None, # (!) real value is "<method 'getFullpathW' of 'panda3d.core.Filename' objects>"
        'getFullpathWoExtension': None, # (!) real value is "<method 'getFullpathWoExtension' of 'panda3d.core.Filename' objects>"
        'getHash': None, # (!) real value is "<method 'getHash' of 'panda3d.core.Filename' objects>"
        'getHashToEnd': None, # (!) real value is "<method 'getHashToEnd' of 'panda3d.core.Filename' objects>"
        'getHomeDirectory': None, # (!) real value is '<staticmethod(<built-in method getHomeDirectory of type object at 0x00007FFCFE25BA20>)>'
        'getPattern': None, # (!) real value is "<method 'getPattern' of 'panda3d.core.Filename' objects>"
        'getTempDirectory': None, # (!) real value is '<staticmethod(<built-in method getTempDirectory of type object at 0x00007FFCFE25BA20>)>'
        'getTimestamp': None, # (!) real value is "<method 'getTimestamp' of 'panda3d.core.Filename' objects>"
        'getType': None, # (!) real value is "<method 'getType' of 'panda3d.core.Filename' objects>"
        'getUserAppdataDirectory': None, # (!) real value is '<staticmethod(<built-in method getUserAppdataDirectory of type object at 0x00007FFCFE25BA20>)>'
        'get_access_timestamp': None, # (!) real value is "<method 'get_access_timestamp' of 'panda3d.core.Filename' objects>"
        'get_basename': None, # (!) real value is "<method 'get_basename' of 'panda3d.core.Filename' objects>"
        'get_basename_wo_extension': None, # (!) real value is "<method 'get_basename_wo_extension' of 'panda3d.core.Filename' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE25BA20>)>'
        'get_common_appdata_directory': None, # (!) real value is '<staticmethod(<built-in method get_common_appdata_directory of type object at 0x00007FFCFE25BA20>)>'
        'get_dirname': None, # (!) real value is "<method 'get_dirname' of 'panda3d.core.Filename' objects>"
        'get_extension': None, # (!) real value is "<method 'get_extension' of 'panda3d.core.Filename' objects>"
        'get_file_size': None, # (!) real value is "<method 'get_file_size' of 'panda3d.core.Filename' objects>"
        'get_filename_index': None, # (!) real value is "<method 'get_filename_index' of 'panda3d.core.Filename' objects>"
        'get_filesystem_encoding': None, # (!) real value is '<staticmethod(<built-in method get_filesystem_encoding of type object at 0x00007FFCFE25BA20>)>'
        'get_fullpath': None, # (!) real value is "<method 'get_fullpath' of 'panda3d.core.Filename' objects>"
        'get_fullpath_w': None, # (!) real value is "<method 'get_fullpath_w' of 'panda3d.core.Filename' objects>"
        'get_fullpath_wo_extension': None, # (!) real value is "<method 'get_fullpath_wo_extension' of 'panda3d.core.Filename' objects>"
        'get_hash': None, # (!) real value is "<method 'get_hash' of 'panda3d.core.Filename' objects>"
        'get_hash_to_end': None, # (!) real value is "<method 'get_hash_to_end' of 'panda3d.core.Filename' objects>"
        'get_home_directory': None, # (!) real value is '<staticmethod(<built-in method get_home_directory of type object at 0x00007FFCFE25BA20>)>'
        'get_pattern': None, # (!) real value is "<method 'get_pattern' of 'panda3d.core.Filename' objects>"
        'get_temp_directory': None, # (!) real value is '<staticmethod(<built-in method get_temp_directory of type object at 0x00007FFCFE25BA20>)>'
        'get_timestamp': None, # (!) real value is "<method 'get_timestamp' of 'panda3d.core.Filename' objects>"
        'get_type': None, # (!) real value is "<method 'get_type' of 'panda3d.core.Filename' objects>"
        'get_user_appdata_directory': None, # (!) real value is '<staticmethod(<built-in method get_user_appdata_directory of type object at 0x00007FFCFE25BA20>)>'
        'hasHash': None, # (!) real value is "<method 'hasHash' of 'panda3d.core.Filename' objects>"
        'has_hash': None, # (!) real value is "<method 'has_hash' of 'panda3d.core.Filename' objects>"
        'isBinary': None, # (!) real value is "<method 'isBinary' of 'panda3d.core.Filename' objects>"
        'isBinaryOrText': None, # (!) real value is "<method 'isBinaryOrText' of 'panda3d.core.Filename' objects>"
        'isDirectory': None, # (!) real value is "<method 'isDirectory' of 'panda3d.core.Filename' objects>"
        'isExecutable': None, # (!) real value is "<method 'isExecutable' of 'panda3d.core.Filename' objects>"
        'isFullyQualified': None, # (!) real value is "<method 'isFullyQualified' of 'panda3d.core.Filename' objects>"
        'isLocal': None, # (!) real value is "<method 'isLocal' of 'panda3d.core.Filename' objects>"
        'isRegularFile': None, # (!) real value is "<method 'isRegularFile' of 'panda3d.core.Filename' objects>"
        'isText': None, # (!) real value is "<method 'isText' of 'panda3d.core.Filename' objects>"
        'isWritable': None, # (!) real value is "<method 'isWritable' of 'panda3d.core.Filename' objects>"
        'is_binary': None, # (!) real value is "<method 'is_binary' of 'panda3d.core.Filename' objects>"
        'is_binary_or_text': None, # (!) real value is "<method 'is_binary_or_text' of 'panda3d.core.Filename' objects>"
        'is_directory': None, # (!) real value is "<method 'is_directory' of 'panda3d.core.Filename' objects>"
        'is_executable': None, # (!) real value is "<method 'is_executable' of 'panda3d.core.Filename' objects>"
        'is_fully_qualified': None, # (!) real value is "<method 'is_fully_qualified' of 'panda3d.core.Filename' objects>"
        'is_local': None, # (!) real value is "<method 'is_local' of 'panda3d.core.Filename' objects>"
        'is_regular_file': None, # (!) real value is "<method 'is_regular_file' of 'panda3d.core.Filename' objects>"
        'is_text': None, # (!) real value is "<method 'is_text' of 'panda3d.core.Filename' objects>"
        'is_writable': None, # (!) real value is "<method 'is_writable' of 'panda3d.core.Filename' objects>"
        'length': None, # (!) real value is "<method 'length' of 'panda3d.core.Filename' objects>"
        'makeAbsolute': None, # (!) real value is "<method 'makeAbsolute' of 'panda3d.core.Filename' objects>"
        'makeCanonical': None, # (!) real value is "<method 'makeCanonical' of 'panda3d.core.Filename' objects>"
        'makeDir': None, # (!) real value is "<method 'makeDir' of 'panda3d.core.Filename' objects>"
        'makeRelativeTo': None, # (!) real value is "<method 'makeRelativeTo' of 'panda3d.core.Filename' objects>"
        'makeTrueCase': None, # (!) real value is "<method 'makeTrueCase' of 'panda3d.core.Filename' objects>"
        'make_absolute': None, # (!) real value is "<method 'make_absolute' of 'panda3d.core.Filename' objects>"
        'make_canonical': None, # (!) real value is "<method 'make_canonical' of 'panda3d.core.Filename' objects>"
        'make_dir': None, # (!) real value is "<method 'make_dir' of 'panda3d.core.Filename' objects>"
        'make_relative_to': None, # (!) real value is "<method 'make_relative_to' of 'panda3d.core.Filename' objects>"
        'make_true_case': None, # (!) real value is "<method 'make_true_case' of 'panda3d.core.Filename' objects>"
        'mkdir': None, # (!) real value is "<method 'mkdir' of 'panda3d.core.Filename' objects>"
        'openAppend': None, # (!) real value is "<method 'openAppend' of 'panda3d.core.Filename' objects>"
        'openRead': None, # (!) real value is "<method 'openRead' of 'panda3d.core.Filename' objects>"
        'openReadAppend': None, # (!) real value is "<method 'openReadAppend' of 'panda3d.core.Filename' objects>"
        'openReadWrite': None, # (!) real value is "<method 'openReadWrite' of 'panda3d.core.Filename' objects>"
        'openWrite': None, # (!) real value is "<method 'openWrite' of 'panda3d.core.Filename' objects>"
        'open_append': None, # (!) real value is "<method 'open_append' of 'panda3d.core.Filename' objects>"
        'open_read': None, # (!) real value is "<method 'open_read' of 'panda3d.core.Filename' objects>"
        'open_read_append': None, # (!) real value is "<method 'open_read_append' of 'panda3d.core.Filename' objects>"
        'open_read_write': None, # (!) real value is "<method 'open_read_write' of 'panda3d.core.Filename' objects>"
        'open_write': None, # (!) real value is "<method 'open_write' of 'panda3d.core.Filename' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.Filename' objects>"
        'patternFilename': None, # (!) real value is '<staticmethod(<built-in method patternFilename of type object at 0x00007FFCFE25BA20>)>'
        'pattern_filename': None, # (!) real value is '<staticmethod(<built-in method pattern_filename of type object at 0x00007FFCFE25BA20>)>'
        'renameTo': None, # (!) real value is "<method 'renameTo' of 'panda3d.core.Filename' objects>"
        'rename_to': None, # (!) real value is "<method 'rename_to' of 'panda3d.core.Filename' objects>"
        'resolveFilename': None, # (!) real value is "<method 'resolveFilename' of 'panda3d.core.Filename' objects>"
        'resolve_filename': None, # (!) real value is "<method 'resolve_filename' of 'panda3d.core.Filename' objects>"
        'rmdir': None, # (!) real value is "<method 'rmdir' of 'panda3d.core.Filename' objects>"
        'scanDirectory': None, # (!) real value is "<method 'scanDirectory' of 'panda3d.core.Filename' objects>"
        'scan_directory': None, # (!) real value is "<method 'scan_directory' of 'panda3d.core.Filename' objects>"
        'setBasename': None, # (!) real value is "<method 'setBasename' of 'panda3d.core.Filename' objects>"
        'setBasenameWoExtension': None, # (!) real value is "<method 'setBasenameWoExtension' of 'panda3d.core.Filename' objects>"
        'setBinary': None, # (!) real value is "<method 'setBinary' of 'panda3d.core.Filename' objects>"
        'setDirname': None, # (!) real value is "<method 'setDirname' of 'panda3d.core.Filename' objects>"
        'setExtension': None, # (!) real value is "<method 'setExtension' of 'panda3d.core.Filename' objects>"
        'setFilesystemEncoding': None, # (!) real value is '<staticmethod(<built-in method setFilesystemEncoding of type object at 0x00007FFCFE25BA20>)>'
        'setFullpath': None, # (!) real value is "<method 'setFullpath' of 'panda3d.core.Filename' objects>"
        'setFullpathWoExtension': None, # (!) real value is "<method 'setFullpathWoExtension' of 'panda3d.core.Filename' objects>"
        'setHashToEnd': None, # (!) real value is "<method 'setHashToEnd' of 'panda3d.core.Filename' objects>"
        'setPattern': None, # (!) real value is "<method 'setPattern' of 'panda3d.core.Filename' objects>"
        'setText': None, # (!) real value is "<method 'setText' of 'panda3d.core.Filename' objects>"
        'setType': None, # (!) real value is "<method 'setType' of 'panda3d.core.Filename' objects>"
        'set_basename': None, # (!) real value is "<method 'set_basename' of 'panda3d.core.Filename' objects>"
        'set_basename_wo_extension': None, # (!) real value is "<method 'set_basename_wo_extension' of 'panda3d.core.Filename' objects>"
        'set_binary': None, # (!) real value is "<method 'set_binary' of 'panda3d.core.Filename' objects>"
        'set_dirname': None, # (!) real value is "<method 'set_dirname' of 'panda3d.core.Filename' objects>"
        'set_extension': None, # (!) real value is "<method 'set_extension' of 'panda3d.core.Filename' objects>"
        'set_filesystem_encoding': None, # (!) real value is '<staticmethod(<built-in method set_filesystem_encoding of type object at 0x00007FFCFE25BA20>)>'
        'set_fullpath': None, # (!) real value is "<method 'set_fullpath' of 'panda3d.core.Filename' objects>"
        'set_fullpath_wo_extension': None, # (!) real value is "<method 'set_fullpath_wo_extension' of 'panda3d.core.Filename' objects>"
        'set_hash_to_end': None, # (!) real value is "<method 'set_hash_to_end' of 'panda3d.core.Filename' objects>"
        'set_pattern': None, # (!) real value is "<method 'set_pattern' of 'panda3d.core.Filename' objects>"
        'set_text': None, # (!) real value is "<method 'set_text' of 'panda3d.core.Filename' objects>"
        'set_type': None, # (!) real value is "<method 'set_type' of 'panda3d.core.Filename' objects>"
        'standardize': None, # (!) real value is "<method 'standardize' of 'panda3d.core.Filename' objects>"
        'substr': None, # (!) real value is "<method 'substr' of 'panda3d.core.Filename' objects>"
        'temporary': None, # (!) real value is '<staticmethod(<built-in method temporary of type object at 0x00007FFCFE25BA20>)>'
        'textFilename': None, # (!) real value is '<staticmethod(<built-in method textFilename of type object at 0x00007FFCFE25BA20>)>'
        'text_filename': None, # (!) real value is '<staticmethod(<built-in method text_filename of type object at 0x00007FFCFE25BA20>)>'
        'toOsGeneric': None, # (!) real value is "<method 'toOsGeneric' of 'panda3d.core.Filename' objects>"
        'toOsLongName': None, # (!) real value is "<method 'toOsLongName' of 'panda3d.core.Filename' objects>"
        'toOsShortName': None, # (!) real value is "<method 'toOsShortName' of 'panda3d.core.Filename' objects>"
        'toOsSpecific': None, # (!) real value is "<method 'toOsSpecific' of 'panda3d.core.Filename' objects>"
        'toOsSpecificW': None, # (!) real value is "<method 'toOsSpecificW' of 'panda3d.core.Filename' objects>"
        'to_os_generic': None, # (!) real value is "<method 'to_os_generic' of 'panda3d.core.Filename' objects>"
        'to_os_long_name': None, # (!) real value is "<method 'to_os_long_name' of 'panda3d.core.Filename' objects>"
        'to_os_short_name': None, # (!) real value is "<method 'to_os_short_name' of 'panda3d.core.Filename' objects>"
        'to_os_specific': None, # (!) real value is "<method 'to_os_specific' of 'panda3d.core.Filename' objects>"
        'to_os_specific_w': None, # (!) real value is "<method 'to_os_specific_w' of 'panda3d.core.Filename' objects>"
        'touch': None, # (!) real value is "<method 'touch' of 'panda3d.core.Filename' objects>"
        'unlink': None, # (!) real value is "<method 'unlink' of 'panda3d.core.Filename' objects>"
    }
    TDso = 1
    TExecutable = 2
    TGeneral = 0
    T_dso = 1
    T_executable = 2
    T_general = 0


