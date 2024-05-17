# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class VirtualFileSystem(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * A hierarchy of directories and files that appears to be one continuous file
     * system, even though the files may originate from several different sources
     * that may not be related to the actual OS's file system.
     *
     * For instance, a VirtualFileSystem can transparently mount one or more
     * Multifiles as their own subdirectory hierarchies.
     */
    """
    def chdir(self, const_VirtualFileSystem_self, const_Filename_new_directory): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        chdir(const VirtualFileSystem self, const Filename new_directory)
        
        /**
         * Changes the current directory.  This is used to resolve relative pathnames
         * in get_file() and/or find_file().  Returns true if successful, false
         * otherwise.
         */
        """
        pass

    def closeReadFile(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        close_read_file(istream stream)
        
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
        close_read_write_file(iostream stream)
        
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
        close_write_file(ostream stream)
        
        /**
         * Closes a file opened by a previous call to open_write_file().  This really
         * just deletes the ostream pointer, but it is recommended to use this
         * interface instead of deleting it explicitly, to help work around compiler
         * issues.
         */
        """
        pass

    def close_read_file(self, istream_stream): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        close_read_file(istream stream)
        
        /**
         * Closes a file opened by a previous call to open_read_file().  This really
         * just deletes the istream pointer, but it is recommended to use this
         * interface instead of deleting it explicitly, to help work around compiler
         * issues.
         */
        """
        pass

    def close_read_write_file(self, iostream_stream): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        close_read_write_file(iostream stream)
        
        /**
         * Closes a file opened by a previous call to open_read_write_file().  This
         * really just deletes the iostream pointer, but it is recommended to use this
         * interface instead of deleting it explicitly, to help work around compiler
         * issues.
         */
        """
        pass

    def close_write_file(self, ostream_stream): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        close_write_file(ostream stream)
        
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
        copy_file(const VirtualFileSystem self, const Filename orig_filename, const Filename new_filename)
        
        /**
         * Attempts to copy the contents of the indicated file to the indicated file.
         * Returns true on success, false on failure.
         */
        """
        pass

    def copy_file(self, const_VirtualFileSystem_self, const_Filename_orig_filename, const_Filename_new_filename): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        copy_file(const VirtualFileSystem self, const Filename orig_filename, const Filename new_filename)
        
        /**
         * Attempts to copy the contents of the indicated file to the indicated file.
         * Returns true on success, false on failure.
         */
        """
        pass

    def createFile(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        create_file(const VirtualFileSystem self, const Filename filename)
        
        /**
         * Attempts to create a file by the indicated name in the filesystem, if
         * possible, and returns it.  If a file by this name already exists, returns
         * the same thing as get_file().  If the filename is located within a read-
         * only directory, or the directory doesn't exist, returns NULL.
         */
        """
        pass

    def create_file(self, const_VirtualFileSystem_self, const_Filename_filename): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        create_file(const VirtualFileSystem self, const Filename filename)
        
        /**
         * Attempts to create a file by the indicated name in the filesystem, if
         * possible, and returns it.  If a file by this name already exists, returns
         * the same thing as get_file().  If the filename is located within a read-
         * only directory, or the directory doesn't exist, returns NULL.
         */
        """
        pass

    def deleteFile(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        delete_file(const VirtualFileSystem self, const Filename filename)
        
        /**
         * Attempts to delete the indicated file or directory.  This can remove a
         * single file or an empty directory.  It will not remove a nonempty
         * directory.  Returns true on success, false on failure.
         */
        """
        pass

    def delete_file(self, const_VirtualFileSystem_self, const_Filename_filename): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        delete_file(const VirtualFileSystem self, const Filename filename)
        
        /**
         * Attempts to delete the indicated file or directory.  This can remove a
         * single file or an empty directory.  It will not remove a nonempty
         * directory.  Returns true on success, false on failure.
         */
        """
        pass

    def exists(self, VirtualFileSystem_self, const_Filename_filename): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        exists(VirtualFileSystem self, const Filename filename)
        
        /**
         * Convenience function; returns true if the named file exists in the virtual
         * file system hierarchy.
         */
        """
        pass

    def findAllFiles(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        find_all_files(VirtualFileSystem self, const Filename filename, const DSearchPath searchpath, Results results)
        
        /**
         * Searches all the directories in the search list for the indicated file, in
         * order.  Fills up the results list with *all* of the matching filenames
         * found, if any.  Returns the number of matches found.
         *
         * It is the responsibility of the the caller to clear the results list first;
         * otherwise, the newly-found files will be appended to the list.
         */
        """
        pass

    def findFile(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        find_file(VirtualFileSystem self, const Filename filename, const DSearchPath searchpath, bool status_only)
        
        /**
         * Uses the indicated search path to find the file within the file system.
         * Returns the first occurrence of the file found, or NULL if the file cannot
         * be found.
         */
        """
        pass

    def find_all_files(self, VirtualFileSystem_self, const_Filename_filename, const_DSearchPath_searchpath, Results_results): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        find_all_files(VirtualFileSystem self, const Filename filename, const DSearchPath searchpath, Results results)
        
        /**
         * Searches all the directories in the search list for the indicated file, in
         * order.  Fills up the results list with *all* of the matching filenames
         * found, if any.  Returns the number of matches found.
         *
         * It is the responsibility of the the caller to clear the results list first;
         * otherwise, the newly-found files will be appended to the list.
         */
        """
        pass

    def find_file(self, VirtualFileSystem_self, const_Filename_filename, const_DSearchPath_searchpath, bool_status_only): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        find_file(VirtualFileSystem self, const Filename filename, const DSearchPath searchpath, bool status_only)
        
        /**
         * Uses the indicated search path to find the file within the file system.
         * Returns the first occurrence of the file found, or NULL if the file cannot
         * be found.
         */
        """
        pass

    def getCwd(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_cwd(VirtualFileSystem self)
        
        /**
         * Returns the current directory name.  See chdir().
         */
        """
        pass

    def getFile(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_file(VirtualFileSystem self, const Filename filename, bool status_only)
        
        /**
         * Looks up the file by the indicated name in the file system.  Returns a
         * VirtualFile pointer representing the file if it is found, or NULL if it is
         * not.
         *
         * If status_only is true, the file will be checked for existence and length
         * and so on, but the returned file's contents cannot be read.  This is an
         * optimization which is especially important for certain mount types, for
         * instance HTTP, for which opening a file to determine its status is
         * substantially less expensive than opening it to read its contents.
         */
        """
        pass

    def getGlobalPtr(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_global_ptr()
        
        /**
         * Returns the default global VirtualFileSystem.  You may create your own
         * personal VirtualFileSystem objects and use them for whatever you like, but
         * Panda will attempt to load models and stuff from this default object.
         *
         * Initially, the global VirtualFileSystem is set up to mount the OS
         * filesystem to root; i.e.  it is equivalent to the OS filesystem.  This may
         * be subsequently adjusted by the user.
         */
        """
        pass

    def getMount(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_mount(VirtualFileSystem self, int n)
        
        /**
         * Returns the nth mount in the system.
         */
        """
        pass

    def getMounts(self, *args, **kwargs): # real signature unknown
        pass

    def getNumMounts(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_mounts(VirtualFileSystem self)
        
        /**
         * Returns the number of individual mounts in the system.
         */
        """
        pass

    def get_cwd(self, VirtualFileSystem_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_cwd(VirtualFileSystem self)
        
        /**
         * Returns the current directory name.  See chdir().
         */
        """
        pass

    def get_file(self, VirtualFileSystem_self, const_Filename_filename, bool_status_only): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_file(VirtualFileSystem self, const Filename filename, bool status_only)
        
        /**
         * Looks up the file by the indicated name in the file system.  Returns a
         * VirtualFile pointer representing the file if it is found, or NULL if it is
         * not.
         *
         * If status_only is true, the file will be checked for existence and length
         * and so on, but the returned file's contents cannot be read.  This is an
         * optimization which is especially important for certain mount types, for
         * instance HTTP, for which opening a file to determine its status is
         * substantially less expensive than opening it to read its contents.
         */
        """
        pass

    def get_global_ptr(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_global_ptr()
        
        /**
         * Returns the default global VirtualFileSystem.  You may create your own
         * personal VirtualFileSystem objects and use them for whatever you like, but
         * Panda will attempt to load models and stuff from this default object.
         *
         * Initially, the global VirtualFileSystem is set up to mount the OS
         * filesystem to root; i.e.  it is equivalent to the OS filesystem.  This may
         * be subsequently adjusted by the user.
         */
        """
        pass

    def get_mount(self, VirtualFileSystem_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_mount(VirtualFileSystem self, int n)
        
        /**
         * Returns the nth mount in the system.
         */
        """
        pass

    def get_mounts(self, *args, **kwargs): # real signature unknown
        pass

    def get_num_mounts(self, VirtualFileSystem_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_mounts(VirtualFileSystem self)
        
        /**
         * Returns the number of individual mounts in the system.
         */
        """
        pass

    def isDirectory(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_directory(VirtualFileSystem self, const Filename filename)
        
        /**
         * Convenience function; returns true if the named file exists as a directory in
         * the virtual file system hierarchy.
         */
        """
        pass

    def isRegularFile(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_regular_file(VirtualFileSystem self, const Filename filename)
        
        /**
         * Convenience function; returns true if the named file exists as a regular file
         * in the virtual file system hierarchy.
         */
        """
        pass

    def is_directory(self, VirtualFileSystem_self, const_Filename_filename): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_directory(VirtualFileSystem self, const Filename filename)
        
        /**
         * Convenience function; returns true if the named file exists as a directory in
         * the virtual file system hierarchy.
         */
        """
        pass

    def is_regular_file(self, VirtualFileSystem_self, const_Filename_filename): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_regular_file(VirtualFileSystem self, const Filename filename)
        
        /**
         * Convenience function; returns true if the named file exists as a regular file
         * in the virtual file system hierarchy.
         */
        """
        pass

    def ls(self, VirtualFileSystem_self, const_Filename_filename): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        ls(VirtualFileSystem self, const Filename filename)
        
        /**
         * Convenience function; lists the files within the indicated directory.
         */
        """
        pass

    def lsAll(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        ls_all(VirtualFileSystem self, const Filename filename)
        
        /**
         * Convenience function; lists the files within the indicated directory, and
         * all files below, recursively.
         */
        """
        pass

    def ls_all(self, VirtualFileSystem_self, const_Filename_filename): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        ls_all(VirtualFileSystem self, const Filename filename)
        
        /**
         * Convenience function; lists the files within the indicated directory, and
         * all files below, recursively.
         */
        """
        pass

    def makeDirectory(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_directory(const VirtualFileSystem self, const Filename filename)
        
        /**
         * Attempts to create a directory within the file system.  Returns true on
         * success, false on failure (for instance, because the parent directory does
         * not exist, or is read-only).  If the directory already existed prior to
         * this call, returns true.
         */
        """
        pass

    def makeDirectoryFull(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_directory_full(const VirtualFileSystem self, const Filename filename)
        
        /**
         * Attempts to create a directory within the file system.  Will also create
         * any intervening directories needed.  Returns true on success, false on
         * failure.
         */
        """
        pass

    def make_directory(self, const_VirtualFileSystem_self, const_Filename_filename): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_directory(const VirtualFileSystem self, const Filename filename)
        
        /**
         * Attempts to create a directory within the file system.  Returns true on
         * success, false on failure (for instance, because the parent directory does
         * not exist, or is read-only).  If the directory already existed prior to
         * this call, returns true.
         */
        """
        pass

    def make_directory_full(self, const_VirtualFileSystem_self, const_Filename_filename): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_directory_full(const VirtualFileSystem self, const Filename filename)
        
        /**
         * Attempts to create a directory within the file system.  Will also create
         * any intervening directories needed.  Returns true on success, false on
         * failure.
         */
        """
        pass

    def mount(self, const_VirtualFileSystem_self, const_Filename_physical_filename, const_Filename_mount_point, int_flags, str_password): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        mount(const VirtualFileSystem self, const Filename physical_filename, const Filename mount_point, int flags, str password)
        mount(const VirtualFileSystem self, VirtualFileMount mount, const Filename mount_point, int flags)
        mount(const VirtualFileSystem self, Multifile multifile, const Filename mount_point, int flags)
        
        /**
         * Mounts the indicated Multifile at the given mount point.
         */
        
        /**
         * Mounts the indicated system file or directory at the given mount point.  If
         * the named file is a directory, mounts the directory.  If the named file is
         * a Multifile, mounts it as a Multifile.  Returns true on success, false on
         * failure.
         *
         * A given system directory may be mounted to multiple different mount point,
         * and the same mount point may share multiple system directories.  In the
         * case of ambiguities (that is, two different files with exactly the same
         * full pathname), the most-recently mounted system wins.
         *
         * The filename specified as the first parameter must refer to a real,
         * physical filename on disk; it cannot be a virtual file already appearing
         * within the vfs filespace.  However, it is possible to mount such a file;
         * see mount_loop() for this.
         *
         * Note that a mounted VirtualFileSystem directory is fully case-sensitive,
         * unlike the native Windows file system, so you must refer to files within
         * the virtual file system with exactly the right case.
         */
        
        /**
         * Adds the given VirtualFileMount object to the mount list.  This is a lower-
         * level function than the other flavors of mount(); it requires you to create
         * a VirtualFileMount object specifically.
         */
        """
        pass

    def mountLoop(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        mount_loop(const VirtualFileSystem self, const Filename virtual_filename, const Filename mount_point, int flags, str password)
        
        /**
         * This is similar to mount(), but it receives the name of a Multifile that
         * already appears within the virtual file system.  It can be used to mount a
         * Multifile that is itself hosted within a virtually-mounted Multifile.
         *
         * This interface can also be used to mount physical files (that appear within
         * the virtual filespace), but it cannot be used to mount directories.  Use
         * mount() if you need to mount a directory.
         *
         * Note that there is additional overhead, in the form of additional buffer
         * copies of the data, for recursively mounting a multifile like this.
         */
        """
        pass

    def mount_loop(self, const_VirtualFileSystem_self, const_Filename_virtual_filename, const_Filename_mount_point, int_flags, str_password): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        mount_loop(const VirtualFileSystem self, const Filename virtual_filename, const Filename mount_point, int flags, str password)
        
        /**
         * This is similar to mount(), but it receives the name of a Multifile that
         * already appears within the virtual file system.  It can be used to mount a
         * Multifile that is itself hosted within a virtually-mounted Multifile.
         *
         * This interface can also be used to mount physical files (that appear within
         * the virtual filespace), but it cannot be used to mount directories.  Use
         * mount() if you need to mount a directory.
         *
         * Note that there is additional overhead, in the form of additional buffer
         * copies of the data, for recursively mounting a multifile like this.
         */
        """
        pass

    def openAppendFile(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        open_append_file(const VirtualFileSystem self, const Filename filename)
        
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
        open_read_append_file(const VirtualFileSystem self, const Filename filename)
        
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
        open_read_file(VirtualFileSystem self, const Filename filename, bool auto_unwrap)
        
        /**
         * Convenience function; returns a newly allocated istream if the file exists
         * and can be read, or NULL otherwise.  Does not return an invalid istream.
         *
         * If auto_unwrap is true, an explicitly-named .pz file is automatically
         * decompressed and the decompressed contents are returned.  This is different
         * than vfs-implicit-pz, which will automatically decompress a file if the
         * extension .pz is *not* given.
         */
        """
        pass

    def openReadWriteFile(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        open_read_write_file(const VirtualFileSystem self, const Filename filename, bool truncate)
        
        /**
         * Convenience function; returns a newly allocated iostream if the file exists
         * and can be written, or NULL otherwise.  Does not return an invalid
         * iostream.
         */
        """
        pass

    def openWriteFile(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        open_write_file(const VirtualFileSystem self, const Filename filename, bool auto_wrap, bool truncate)
        
        /**
         * Convenience function; returns a newly allocated ostream if the file exists
         * and can be written, or NULL otherwise.  Does not return an invalid ostream.
         *
         * If auto_wrap is true, an explicitly-named .pz file is automatically
         * compressed while writing.  If truncate is true, the file is truncated to
         * zero length before writing.
         */
        """
        pass

    def open_append_file(self, const_VirtualFileSystem_self, const_Filename_filename): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        open_append_file(const VirtualFileSystem self, const Filename filename)
        
        /**
         * Works like open_write_file(), but the file is opened in append mode.  Like
         * open_write_file, the returned pointer should eventually be passed to
         * close_write_file().
         */
        """
        pass

    def open_read_append_file(self, const_VirtualFileSystem_self, const_Filename_filename): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        open_read_append_file(const VirtualFileSystem self, const Filename filename)
        
        /**
         * Works like open_read_write_file(), but the file is opened in append mode.
         * Like open_read_write_file, the returned pointer should eventually be passed
         * to close_read_write_file().
         */
        """
        pass

    def open_read_file(self, VirtualFileSystem_self, const_Filename_filename, bool_auto_unwrap): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        open_read_file(VirtualFileSystem self, const Filename filename, bool auto_unwrap)
        
        /**
         * Convenience function; returns a newly allocated istream if the file exists
         * and can be read, or NULL otherwise.  Does not return an invalid istream.
         *
         * If auto_unwrap is true, an explicitly-named .pz file is automatically
         * decompressed and the decompressed contents are returned.  This is different
         * than vfs-implicit-pz, which will automatically decompress a file if the
         * extension .pz is *not* given.
         */
        """
        pass

    def open_read_write_file(self, const_VirtualFileSystem_self, const_Filename_filename, bool_truncate): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        open_read_write_file(const VirtualFileSystem self, const Filename filename, bool truncate)
        
        /**
         * Convenience function; returns a newly allocated iostream if the file exists
         * and can be written, or NULL otherwise.  Does not return an invalid
         * iostream.
         */
        """
        pass

    def open_write_file(self, const_VirtualFileSystem_self, const_Filename_filename, bool_auto_wrap, bool_truncate): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        open_write_file(const VirtualFileSystem self, const Filename filename, bool auto_wrap, bool truncate)
        
        /**
         * Convenience function; returns a newly allocated ostream if the file exists
         * and can be written, or NULL otherwise.  Does not return an invalid ostream.
         *
         * If auto_wrap is true, an explicitly-named .pz file is automatically
         * compressed while writing.  If truncate is true, the file is truncated to
         * zero length before writing.
         */
        """
        pass

    def readFile(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        read_file(VirtualFileSystem self, const Filename filename, bool auto_unwrap)
        
        /**
         * Convenience function; returns the entire contents of the indicated file as
         * a string.
         *
         * If auto_unwrap is true, an explicitly-named .pz/.gz file is automatically
         * decompressed and the decompressed contents are returned.  This is different
         * than vfs-implicit-pz, which will automatically decompress a file if the
         * extension .pz is *not* given.
         */
        
        /**
         * Convenience function; fills the string up with the data from the indicated
         * file, if it exists and can be read.  Returns true on success, false
         * otherwise.
         *
         * If auto_unwrap is true, an explicitly-named .pz/.gz file is automatically
         * decompressed and the decompressed contents are returned.  This is different
         * than vfs-implicit-pz, which will automatically decompress a file if the
         * extension .pz is *not* given.
         */
        
        /**
         * Convenience function; fills the pvector up with the data from the indicated
         * file, if it exists and can be read.  Returns true on success, false
         * otherwise.
         *
         * If auto_unwrap is true, an explicitly-named .pz/.gz file is automatically
         * decompressed and the decompressed contents are returned.  This is different
         * than vfs-implicit-pz, which will automatically decompress a file if the
         * extension .pz is *not* given.
         */
        """
        pass

    def read_file(self, VirtualFileSystem_self, const_Filename_filename, bool_auto_unwrap): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        read_file(VirtualFileSystem self, const Filename filename, bool auto_unwrap)
        
        /**
         * Convenience function; returns the entire contents of the indicated file as
         * a string.
         *
         * If auto_unwrap is true, an explicitly-named .pz/.gz file is automatically
         * decompressed and the decompressed contents are returned.  This is different
         * than vfs-implicit-pz, which will automatically decompress a file if the
         * extension .pz is *not* given.
         */
        
        /**
         * Convenience function; fills the string up with the data from the indicated
         * file, if it exists and can be read.  Returns true on success, false
         * otherwise.
         *
         * If auto_unwrap is true, an explicitly-named .pz/.gz file is automatically
         * decompressed and the decompressed contents are returned.  This is different
         * than vfs-implicit-pz, which will automatically decompress a file if the
         * extension .pz is *not* given.
         */
        
        /**
         * Convenience function; fills the pvector up with the data from the indicated
         * file, if it exists and can be read.  Returns true on success, false
         * otherwise.
         *
         * If auto_unwrap is true, an explicitly-named .pz/.gz file is automatically
         * decompressed and the decompressed contents are returned.  This is different
         * than vfs-implicit-pz, which will automatically decompress a file if the
         * extension .pz is *not* given.
         */
        """
        pass

    def renameFile(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        rename_file(const VirtualFileSystem self, const Filename orig_filename, const Filename new_filename)
        
        /**
         * Attempts to move or rename the indicated file or directory.  If the
         * original file is an ordinary file, it will quietly replace any already-
         * existing file in the new filename (but not a directory).  If the original
         * file is a directory, the new filename must not already exist.
         *
         * If the file is a directory, the new filename must be within the same mount
         * point.  If the file is an ordinary file, the new filename may be anywhere;
         * but if it is not within the same mount point then the rename operation is
         * automatically performed as a two-step copy-and-delete operation.
         */
        """
        pass

    def rename_file(self, const_VirtualFileSystem_self, const_Filename_orig_filename, const_Filename_new_filename): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        rename_file(const VirtualFileSystem self, const Filename orig_filename, const Filename new_filename)
        
        /**
         * Attempts to move or rename the indicated file or directory.  If the
         * original file is an ordinary file, it will quietly replace any already-
         * existing file in the new filename (but not a directory).  If the original
         * file is a directory, the new filename must not already exist.
         *
         * If the file is a directory, the new filename must be within the same mount
         * point.  If the file is an ordinary file, the new filename may be anywhere;
         * but if it is not within the same mount point then the rename operation is
         * automatically performed as a two-step copy-and-delete operation.
         */
        """
        pass

    def resolveFilename(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        resolve_filename(VirtualFileSystem self, Filename filename, const DSearchPath searchpath, str default_extension)
        
        /**
         * Searches the given search path for the filename.  If it is found, updates
         * the filename to the full pathname found and returns true; otherwise,
         * returns false.
         */
        """
        pass

    def resolve_filename(self, VirtualFileSystem_self, Filename_filename, const_DSearchPath_searchpath, str_default_extension): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        resolve_filename(VirtualFileSystem self, Filename filename, const DSearchPath searchpath, str default_extension)
        
        /**
         * Searches the given search path for the filename.  If it is found, updates
         * the filename to the full pathname found and returns true; otherwise,
         * returns false.
         */
        """
        pass

    def scanDirectory(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        scan_directory(VirtualFileSystem self, const Filename filename)
        
        /**
         * If the file represents a directory (that is, is_directory() returns true),
         * this returns the list of files within the directory at the current time.
         * Returns NULL if the file is not a directory or if the directory cannot be
         * read.
         */
        """
        pass

    def scan_directory(self, VirtualFileSystem_self, const_Filename_filename): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        scan_directory(VirtualFileSystem self, const Filename filename)
        
        /**
         * If the file represents a directory (that is, is_directory() returns true),
         * this returns the list of files within the directory at the current time.
         * Returns NULL if the file is not a directory or if the directory cannot be
         * read.
         */
        """
        pass

    def unmount(self, const_VirtualFileSystem_self, VirtualFileMount_mount): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        unmount(const VirtualFileSystem self, VirtualFileMount mount)
        unmount(const VirtualFileSystem self, Multifile multifile)
        
        /**
         * Unmounts all appearances of the indicated Multifile from the file system.
         * Returns the number of appearances unmounted.
         */
        
        /**
         * Unmounts all appearances of the indicated directory name or multifile name
         * from the file system.  Returns the number of appearances unmounted.
         */
        
        /**
         * Unmounts the indicated VirtualFileMount object from the file system.
         * Returns the number of appearances unmounted.
         */
        """
        pass

    def unmountAll(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        unmount_all(const VirtualFileSystem self)
        
        /**
         * Unmounts all files from the file system.  Returns the number of systems
         * unmounted.
         */
        """
        pass

    def unmountPoint(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        unmount_point(const VirtualFileSystem self, const Filename mount_point)
        
        /**
         * Unmounts all systems attached to the given mount point from the file
         * system.  Returns the number of appearances unmounted.
         */
        """
        pass

    def unmount_all(self, const_VirtualFileSystem_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        unmount_all(const VirtualFileSystem self)
        
        /**
         * Unmounts all files from the file system.  Returns the number of systems
         * unmounted.
         */
        """
        pass

    def unmount_point(self, const_VirtualFileSystem_self, const_Filename_mount_point): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        unmount_point(const VirtualFileSystem self, const Filename mount_point)
        
        /**
         * Unmounts all systems attached to the given mount point from the file
         * system.  Returns the number of appearances unmounted.
         */
        """
        pass

    def write(self, VirtualFileSystem_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(VirtualFileSystem self, ostream out)
        
        /**
         * Print debugging information.  (e.g.  from Python or gdb prompt).
         */
        """
        pass

    def writeFile(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        write_file(const VirtualFileSystem self, const Filename filename, object data, bool auto_wrap)
        
        /**
         * Convenience function; writes the entire contents of the indicated file as a
         * string.
         *
         * If auto_wrap is true, an explicitly-named .pz file is automatically
         * compressed while writing.
         */
        
        /**
         * Convenience function; writes the entire contents of the indicated file as a
         * block of data.
         *
         * If auto_wrap is true, an explicitly-named .pz file is automatically
         * compressed while writing.
         */
        """
        pass

    def write_file(self, const_VirtualFileSystem_self, const_Filename_filename, object_data, bool_auto_wrap): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write_file(const VirtualFileSystem self, const Filename filename, object data, bool auto_wrap)
        
        /**
         * Convenience function; writes the entire contents of the indicated file as a
         * string.
         *
         * If auto_wrap is true, an explicitly-named .pz file is automatically
         * compressed while writing.
         */
        
        /**
         * Convenience function; writes the entire contents of the indicated file as a
         * block of data.
         *
         * If auto_wrap is true, an explicitly-named .pz file is automatically
         * compressed while writing.
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    mounts = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        'MFReadOnly': 2,
        'MF_read_only': 2,
        '__doc__': "/**\n * A hierarchy of directories and files that appears to be one continuous file\n * system, even though the files may originate from several different sources\n * that may not be related to the actual OS's file system.\n *\n * For instance, a VirtualFileSystem can transparently mount one or more\n * Multifiles as their own subdirectory hierarchies.\n */",
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.VirtualFileSystem' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE27AA40>'
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.VirtualFileSystem' objects>"
        'chdir': None, # (!) real value is "<method 'chdir' of 'panda3d.core.VirtualFileSystem' objects>"
        'closeReadFile': None, # (!) real value is '<staticmethod(<built-in method closeReadFile of type object at 0x00007FFCFE27AA40>)>'
        'closeReadWriteFile': None, # (!) real value is '<staticmethod(<built-in method closeReadWriteFile of type object at 0x00007FFCFE27AA40>)>'
        'closeWriteFile': None, # (!) real value is '<staticmethod(<built-in method closeWriteFile of type object at 0x00007FFCFE27AA40>)>'
        'close_read_file': None, # (!) real value is '<staticmethod(<built-in method close_read_file of type object at 0x00007FFCFE27AA40>)>'
        'close_read_write_file': None, # (!) real value is '<staticmethod(<built-in method close_read_write_file of type object at 0x00007FFCFE27AA40>)>'
        'close_write_file': None, # (!) real value is '<staticmethod(<built-in method close_write_file of type object at 0x00007FFCFE27AA40>)>'
        'copyFile': None, # (!) real value is "<method 'copyFile' of 'panda3d.core.VirtualFileSystem' objects>"
        'copy_file': None, # (!) real value is "<method 'copy_file' of 'panda3d.core.VirtualFileSystem' objects>"
        'createFile': None, # (!) real value is "<method 'createFile' of 'panda3d.core.VirtualFileSystem' objects>"
        'create_file': None, # (!) real value is "<method 'create_file' of 'panda3d.core.VirtualFileSystem' objects>"
        'deleteFile': None, # (!) real value is "<method 'deleteFile' of 'panda3d.core.VirtualFileSystem' objects>"
        'delete_file': None, # (!) real value is "<method 'delete_file' of 'panda3d.core.VirtualFileSystem' objects>"
        'exists': None, # (!) real value is "<method 'exists' of 'panda3d.core.VirtualFileSystem' objects>"
        'findAllFiles': None, # (!) real value is "<method 'findAllFiles' of 'panda3d.core.VirtualFileSystem' objects>"
        'findFile': None, # (!) real value is "<method 'findFile' of 'panda3d.core.VirtualFileSystem' objects>"
        'find_all_files': None, # (!) real value is "<method 'find_all_files' of 'panda3d.core.VirtualFileSystem' objects>"
        'find_file': None, # (!) real value is "<method 'find_file' of 'panda3d.core.VirtualFileSystem' objects>"
        'getCwd': None, # (!) real value is "<method 'getCwd' of 'panda3d.core.VirtualFileSystem' objects>"
        'getFile': None, # (!) real value is "<method 'getFile' of 'panda3d.core.VirtualFileSystem' objects>"
        'getGlobalPtr': None, # (!) real value is '<staticmethod(<built-in method getGlobalPtr of type object at 0x00007FFCFE27AA40>)>'
        'getMount': None, # (!) real value is "<method 'getMount' of 'panda3d.core.VirtualFileSystem' objects>"
        'getMounts': None, # (!) real value is "<method 'getMounts' of 'panda3d.core.VirtualFileSystem' objects>"
        'getNumMounts': None, # (!) real value is "<method 'getNumMounts' of 'panda3d.core.VirtualFileSystem' objects>"
        'get_cwd': None, # (!) real value is "<method 'get_cwd' of 'panda3d.core.VirtualFileSystem' objects>"
        'get_file': None, # (!) real value is "<method 'get_file' of 'panda3d.core.VirtualFileSystem' objects>"
        'get_global_ptr': None, # (!) real value is '<staticmethod(<built-in method get_global_ptr of type object at 0x00007FFCFE27AA40>)>'
        'get_mount': None, # (!) real value is "<method 'get_mount' of 'panda3d.core.VirtualFileSystem' objects>"
        'get_mounts': None, # (!) real value is "<method 'get_mounts' of 'panda3d.core.VirtualFileSystem' objects>"
        'get_num_mounts': None, # (!) real value is "<method 'get_num_mounts' of 'panda3d.core.VirtualFileSystem' objects>"
        'isDirectory': None, # (!) real value is "<method 'isDirectory' of 'panda3d.core.VirtualFileSystem' objects>"
        'isRegularFile': None, # (!) real value is "<method 'isRegularFile' of 'panda3d.core.VirtualFileSystem' objects>"
        'is_directory': None, # (!) real value is "<method 'is_directory' of 'panda3d.core.VirtualFileSystem' objects>"
        'is_regular_file': None, # (!) real value is "<method 'is_regular_file' of 'panda3d.core.VirtualFileSystem' objects>"
        'ls': None, # (!) real value is "<method 'ls' of 'panda3d.core.VirtualFileSystem' objects>"
        'lsAll': None, # (!) real value is "<method 'lsAll' of 'panda3d.core.VirtualFileSystem' objects>"
        'ls_all': None, # (!) real value is "<method 'ls_all' of 'panda3d.core.VirtualFileSystem' objects>"
        'makeDirectory': None, # (!) real value is "<method 'makeDirectory' of 'panda3d.core.VirtualFileSystem' objects>"
        'makeDirectoryFull': None, # (!) real value is "<method 'makeDirectoryFull' of 'panda3d.core.VirtualFileSystem' objects>"
        'make_directory': None, # (!) real value is "<method 'make_directory' of 'panda3d.core.VirtualFileSystem' objects>"
        'make_directory_full': None, # (!) real value is "<method 'make_directory_full' of 'panda3d.core.VirtualFileSystem' objects>"
        'mount': None, # (!) real value is "<method 'mount' of 'panda3d.core.VirtualFileSystem' objects>"
        'mountLoop': None, # (!) real value is "<method 'mountLoop' of 'panda3d.core.VirtualFileSystem' objects>"
        'mount_loop': None, # (!) real value is "<method 'mount_loop' of 'panda3d.core.VirtualFileSystem' objects>"
        'mounts': None, # (!) real value is "<attribute 'mounts' of 'panda3d.core.VirtualFileSystem' objects>"
        'openAppendFile': None, # (!) real value is "<method 'openAppendFile' of 'panda3d.core.VirtualFileSystem' objects>"
        'openReadAppendFile': None, # (!) real value is "<method 'openReadAppendFile' of 'panda3d.core.VirtualFileSystem' objects>"
        'openReadFile': None, # (!) real value is "<method 'openReadFile' of 'panda3d.core.VirtualFileSystem' objects>"
        'openReadWriteFile': None, # (!) real value is "<method 'openReadWriteFile' of 'panda3d.core.VirtualFileSystem' objects>"
        'openWriteFile': None, # (!) real value is "<method 'openWriteFile' of 'panda3d.core.VirtualFileSystem' objects>"
        'open_append_file': None, # (!) real value is "<method 'open_append_file' of 'panda3d.core.VirtualFileSystem' objects>"
        'open_read_append_file': None, # (!) real value is "<method 'open_read_append_file' of 'panda3d.core.VirtualFileSystem' objects>"
        'open_read_file': None, # (!) real value is "<method 'open_read_file' of 'panda3d.core.VirtualFileSystem' objects>"
        'open_read_write_file': None, # (!) real value is "<method 'open_read_write_file' of 'panda3d.core.VirtualFileSystem' objects>"
        'open_write_file': None, # (!) real value is "<method 'open_write_file' of 'panda3d.core.VirtualFileSystem' objects>"
        'readFile': None, # (!) real value is "<method 'readFile' of 'panda3d.core.VirtualFileSystem' objects>"
        'read_file': None, # (!) real value is "<method 'read_file' of 'panda3d.core.VirtualFileSystem' objects>"
        'renameFile': None, # (!) real value is "<method 'renameFile' of 'panda3d.core.VirtualFileSystem' objects>"
        'rename_file': None, # (!) real value is "<method 'rename_file' of 'panda3d.core.VirtualFileSystem' objects>"
        'resolveFilename': None, # (!) real value is "<method 'resolveFilename' of 'panda3d.core.VirtualFileSystem' objects>"
        'resolve_filename': None, # (!) real value is "<method 'resolve_filename' of 'panda3d.core.VirtualFileSystem' objects>"
        'scanDirectory': None, # (!) real value is "<method 'scanDirectory' of 'panda3d.core.VirtualFileSystem' objects>"
        'scan_directory': None, # (!) real value is "<method 'scan_directory' of 'panda3d.core.VirtualFileSystem' objects>"
        'unmount': None, # (!) real value is "<method 'unmount' of 'panda3d.core.VirtualFileSystem' objects>"
        'unmountAll': None, # (!) real value is "<method 'unmountAll' of 'panda3d.core.VirtualFileSystem' objects>"
        'unmountPoint': None, # (!) real value is "<method 'unmountPoint' of 'panda3d.core.VirtualFileSystem' objects>"
        'unmount_all': None, # (!) real value is "<method 'unmount_all' of 'panda3d.core.VirtualFileSystem' objects>"
        'unmount_point': None, # (!) real value is "<method 'unmount_point' of 'panda3d.core.VirtualFileSystem' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.core.VirtualFileSystem' objects>"
        'writeFile': None, # (!) real value is "<method 'writeFile' of 'panda3d.core.VirtualFileSystem' objects>"
        'write_file': None, # (!) real value is "<method 'write_file' of 'panda3d.core.VirtualFileSystem' objects>"
    }
    MFReadOnly = 2
    MF_read_only = 2


