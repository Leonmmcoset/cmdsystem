# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class DownloadDb(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * A listing of files within multifiles for management of client-side
     * synchronization with a server-provided set of files.
     *
     * This class manages one copy of the database for the client, representing
     * the files on the client system, and another copy for the server,
     * representing the files the server has available.
     */
    """
    def addClientMultifile(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_client_multifile(const DownloadDb self, str server_mfname)
        
        /**
         *
         */
        """
        pass

    def addVersion(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_version(const DownloadDb self, const Filename name, const HashVal hash, int version)
        
        /**
         * Appends a new version of the file onto the end of the list, or changes the
         * hash associated with a version previously added.
         *
         * Note: version numbers start at 1
         */
        """
        pass

    def add_client_multifile(self, const_DownloadDb_self, str_server_mfname): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_client_multifile(const DownloadDb self, str server_mfname)
        
        /**
         *
         */
        """
        pass

    def add_version(self, const_DownloadDb_self, const_Filename_name, const_HashVal_hash, int_version): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_version(const DownloadDb self, const Filename name, const HashVal hash, int version)
        
        /**
         * Appends a new version of the file onto the end of the list, or changes the
         * hash associated with a version previously added.
         *
         * Note: version numbers start at 1
         */
        """
        pass

    def clientMultifileComplete(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        client_multifile_complete(DownloadDb self, str mfname)
        
        /**
         * A multifile is complete when it is completely downloaded.  Note: it may
         * already be decompressed or extracted and it is still complete
         */
        """
        pass

    def clientMultifileDecompressed(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        client_multifile_decompressed(DownloadDb self, str mfname)
        
        /**
         *
         */
        """
        pass

    def clientMultifileExists(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        client_multifile_exists(DownloadDb self, str mfname)
        
        // Queries from the Launcher
        
        /**
         *
         */
        """
        pass

    def clientMultifileExtracted(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        client_multifile_extracted(DownloadDb self, str mfname)
        
        /**
         *
         */
        """
        pass

    def client_multifile_complete(self, DownloadDb_self, str_mfname): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        client_multifile_complete(DownloadDb self, str mfname)
        
        /**
         * A multifile is complete when it is completely downloaded.  Note: it may
         * already be decompressed or extracted and it is still complete
         */
        """
        pass

    def client_multifile_decompressed(self, DownloadDb_self, str_mfname): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        client_multifile_decompressed(DownloadDb self, str mfname)
        
        /**
         *
         */
        """
        pass

    def client_multifile_exists(self, DownloadDb_self, str_mfname): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        client_multifile_exists(DownloadDb self, str mfname)
        
        // Queries from the Launcher
        
        /**
         *
         */
        """
        pass

    def client_multifile_extracted(self, DownloadDb_self, str_mfname): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        client_multifile_extracted(DownloadDb self, str mfname)
        
        /**
         *
         */
        """
        pass

    def createNewServerDb(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        create_new_server_db(const DownloadDb self)
        
        // Server side operations to create multifile records
        
        /**
         * Used on the server side makefiles to create a new clean server db
         */
        """
        pass

    def create_new_server_db(self, const_DownloadDb_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        create_new_server_db(const DownloadDb self)
        
        // Server side operations to create multifile records
        
        /**
         * Used on the server side makefiles to create a new clean server db
         */
        """
        pass

    def deleteClientMultifile(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        delete_client_multifile(const DownloadDb self, str mfname)
        
        // Operations on multifiles
        
        /**
         *
         */
        """
        pass

    def delete_client_multifile(self, const_DownloadDb_self, str_mfname): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        delete_client_multifile(const DownloadDb self, str mfname)
        
        // Operations on multifiles
        
        /**
         *
         */
        """
        pass

    def expandClientMultifile(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        expand_client_multifile(const DownloadDb self, str mfname)
        
        /**
         *
         */
        """
        pass

    def expand_client_multifile(self, const_DownloadDb_self, str_mfname): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        expand_client_multifile(const DownloadDb self, str mfname)
        
        /**
         *
         */
        """
        pass

    def getClientMultifileHash(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_client_multifile_hash(DownloadDb self, str mfname)
        
        // Ask what version (told with the hash) this multifile is
        
        /**
         * Return the hash value of the file we are working on
         */
        """
        pass

    def getClientMultifileName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_client_multifile_name(DownloadDb self, int index)
        
        /**
         *
         */
        """
        pass

    def getClientMultifilePhase(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_client_multifile_phase(DownloadDb self, str mfname)
        
        /**
         *
         */
        """
        pass

    def getClientMultifileSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_client_multifile_size(DownloadDb self, str mfname)
        
        /**
         *
         */
        """
        pass

    def getClientNumMultifiles(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_client_num_multifiles(DownloadDb self)
        
        /**
         *
         */
        """
        pass

    def getHash(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_hash(DownloadDb self, const Filename name, int version)
        
        /**
         * Returns the MD5 hash associated with the indicated version of the indicated
         * file.
         */
        """
        pass

    def getNumVersions(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_versions(DownloadDb self, const Filename name)
        
        /**
         * Returns the number of versions stored for the indicated file.
         */
        """
        pass

    def getServerFileName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_server_file_name(DownloadDb self, str mfname, int index)
        
        /**
         *
         */
        """
        pass

    def getServerMultifileHash(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_server_multifile_hash(DownloadDb self, str mfname)
        
        /**
         * Return the hash value of the server file
         */
        """
        pass

    def getServerMultifileName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_server_multifile_name(DownloadDb self, int index)
        
        /**
         *
         */
        """
        pass

    def getServerMultifilePhase(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_server_multifile_phase(DownloadDb self, str mfname)
        
        /**
         *
         */
        """
        pass

    def getServerMultifileSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_server_multifile_size(DownloadDb self, str mfname)
        
        /**
         *
         */
        """
        pass

    def getServerNumFiles(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_server_num_files(DownloadDb self, str mfname)
        
        /**
         *
         */
        """
        pass

    def getServerNumMultifiles(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_server_num_multifiles(DownloadDb self)
        
        /**
         *
         */
        """
        pass

    def getVersion(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_version(DownloadDb self, const Filename name, const HashVal hash)
        
        /**
         * Returns the version number of this particular file, determined by looking
         * up the hash generated from the file.  Returns -1 if the version number
         * cannot be determined.
         */
        """
        pass

    def get_client_multifile_hash(self, DownloadDb_self, str_mfname): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_client_multifile_hash(DownloadDb self, str mfname)
        
        // Ask what version (told with the hash) this multifile is
        
        /**
         * Return the hash value of the file we are working on
         */
        """
        pass

    def get_client_multifile_name(self, DownloadDb_self, int_index): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_client_multifile_name(DownloadDb self, int index)
        
        /**
         *
         */
        """
        pass

    def get_client_multifile_phase(self, DownloadDb_self, str_mfname): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_client_multifile_phase(DownloadDb self, str mfname)
        
        /**
         *
         */
        """
        pass

    def get_client_multifile_size(self, DownloadDb_self, str_mfname): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_client_multifile_size(DownloadDb self, str mfname)
        
        /**
         *
         */
        """
        pass

    def get_client_num_multifiles(self, DownloadDb_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_client_num_multifiles(DownloadDb self)
        
        /**
         *
         */
        """
        pass

    def get_hash(self, DownloadDb_self, const_Filename_name, int_version): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_hash(DownloadDb self, const Filename name, int version)
        
        /**
         * Returns the MD5 hash associated with the indicated version of the indicated
         * file.
         */
        """
        pass

    def get_num_versions(self, DownloadDb_self, const_Filename_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_versions(DownloadDb self, const Filename name)
        
        /**
         * Returns the number of versions stored for the indicated file.
         */
        """
        pass

    def get_server_file_name(self, DownloadDb_self, str_mfname, int_index): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_server_file_name(DownloadDb self, str mfname, int index)
        
        /**
         *
         */
        """
        pass

    def get_server_multifile_hash(self, DownloadDb_self, str_mfname): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_server_multifile_hash(DownloadDb self, str mfname)
        
        /**
         * Return the hash value of the server file
         */
        """
        pass

    def get_server_multifile_name(self, DownloadDb_self, int_index): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_server_multifile_name(DownloadDb self, int index)
        
        /**
         *
         */
        """
        pass

    def get_server_multifile_phase(self, DownloadDb_self, str_mfname): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_server_multifile_phase(DownloadDb self, str mfname)
        
        /**
         *
         */
        """
        pass

    def get_server_multifile_size(self, DownloadDb_self, str_mfname): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_server_multifile_size(DownloadDb self, str mfname)
        
        /**
         *
         */
        """
        pass

    def get_server_num_files(self, DownloadDb_self, str_mfname): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_server_num_files(DownloadDb self, str mfname)
        
        /**
         *
         */
        """
        pass

    def get_server_num_multifiles(self, DownloadDb_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_server_num_multifiles(DownloadDb self)
        
        /**
         *
         */
        """
        pass

    def get_version(self, DownloadDb_self, const_Filename_name, const_HashVal_hash): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_version(DownloadDb self, const Filename name, const HashVal hash)
        
        /**
         * Returns the version number of this particular file, determined by looking
         * up the hash generated from the file.  Returns -1 if the version number
         * cannot be determined.
         */
        """
        pass

    def hasVersion(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_version(DownloadDb self, const Filename name)
        
        /**
         * Returns true if the indicated file has version information, false
         * otherwise.  Some files recorded in the database may not bother to track
         * versions.
         */
        """
        pass

    def has_version(self, DownloadDb_self, const_Filename_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_version(DownloadDb self, const Filename name)
        
        /**
         * Returns true if the indicated file has version information, false
         * otherwise.  Some files recorded in the database may not bother to track
         * versions.
         */
        """
        pass

    def insertNewVersion(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        insert_new_version(const DownloadDb self, const Filename name, const HashVal hash)
        
        /**
         * Inserts a new version 1 copy of the file, sliding all the other versions up
         * by one.
         */
        """
        pass

    def insert_new_version(self, const_DownloadDb_self, const_Filename_name, const_HashVal_hash): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        insert_new_version(const DownloadDb self, const Filename name, const HashVal hash)
        
        /**
         * Inserts a new version 1 copy of the file, sliding all the other versions up
         * by one.
         */
        """
        pass

    def output(self, DownloadDb_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(DownloadDb self, ostream out)
        
        /**
         *
         */
        """
        pass

    def serverAddFile(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        server_add_file(const DownloadDb self, str mfname, str fname)
        
        /**
         *
         */
        """
        pass

    def serverAddMultifile(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        server_add_multifile(const DownloadDb self, str mfname, float phase, int size, int status)
        
        /**
         *
         */
        """
        pass

    def server_add_file(self, const_DownloadDb_self, str_mfname, str_fname): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        server_add_file(const DownloadDb self, str mfname, str fname)
        
        /**
         *
         */
        """
        pass

    def server_add_multifile(self, const_DownloadDb_self, str_mfname, float_phase, int_size, int_status): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        server_add_multifile(const DownloadDb self, str mfname, float phase, int size, int status)
        
        /**
         *
         */
        """
        pass

    def setClientMultifileComplete(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_client_multifile_complete(const DownloadDb self, str mfname)
        
        /**
         *
         */
        """
        pass

    def setClientMultifileDecompressed(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_client_multifile_decompressed(const DownloadDb self, str mfname)
        
        /**
         *
         */
        """
        pass

    def setClientMultifileDeltaSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_client_multifile_delta_size(const DownloadDb self, str mfname, int size)
        
        /**
         *
         */
        """
        pass

    def setClientMultifileExtracted(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_client_multifile_extracted(const DownloadDb self, str mfname)
        
        /**
         *
         */
        """
        pass

    def setClientMultifileHash(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_client_multifile_hash(const DownloadDb self, str mfname, HashVal val)
        
        /**
         * Set the hash value of file we are working on
         */
        """
        pass

    def setClientMultifileIncomplete(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_client_multifile_incomplete(const DownloadDb self, str mfname)
        
        /**
         *
         */
        """
        pass

    def setClientMultifileSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_client_multifile_size(const DownloadDb self, str mfname, int size)
        
        /**
         *
         */
        """
        pass

    def setNumVersions(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_num_versions(const DownloadDb self, const Filename name, int num_versions)
        
        /**
         * Reduces the number of versions of a particular file stored in the ddb by
         * throwing away all versions higher than the indicated index.
         */
        """
        pass

    def setServerMultifileHash(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_server_multifile_hash(const DownloadDb self, str mfname, HashVal val)
        
        /**
         * Set the hash value of file we are working on
         */
        """
        pass

    def setServerMultifileSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_server_multifile_size(const DownloadDb self, str mfname, int size)
        
        /**
         *
         */
        """
        pass

    def set_client_multifile_complete(self, const_DownloadDb_self, str_mfname): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_client_multifile_complete(const DownloadDb self, str mfname)
        
        /**
         *
         */
        """
        pass

    def set_client_multifile_decompressed(self, const_DownloadDb_self, str_mfname): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_client_multifile_decompressed(const DownloadDb self, str mfname)
        
        /**
         *
         */
        """
        pass

    def set_client_multifile_delta_size(self, const_DownloadDb_self, str_mfname, int_size): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_client_multifile_delta_size(const DownloadDb self, str mfname, int size)
        
        /**
         *
         */
        """
        pass

    def set_client_multifile_extracted(self, const_DownloadDb_self, str_mfname): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_client_multifile_extracted(const DownloadDb self, str mfname)
        
        /**
         *
         */
        """
        pass

    def set_client_multifile_hash(self, const_DownloadDb_self, str_mfname, HashVal_val): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_client_multifile_hash(const DownloadDb self, str mfname, HashVal val)
        
        /**
         * Set the hash value of file we are working on
         */
        """
        pass

    def set_client_multifile_incomplete(self, const_DownloadDb_self, str_mfname): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_client_multifile_incomplete(const DownloadDb self, str mfname)
        
        /**
         *
         */
        """
        pass

    def set_client_multifile_size(self, const_DownloadDb_self, str_mfname, int_size): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_client_multifile_size(const DownloadDb self, str mfname, int size)
        
        /**
         *
         */
        """
        pass

    def set_num_versions(self, const_DownloadDb_self, const_Filename_name, int_num_versions): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_num_versions(const DownloadDb self, const Filename name, int num_versions)
        
        /**
         * Reduces the number of versions of a particular file stored in the ddb by
         * throwing away all versions higher than the indicated index.
         */
        """
        pass

    def set_server_multifile_hash(self, const_DownloadDb_self, str_mfname, HashVal_val): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_server_multifile_hash(const DownloadDb self, str mfname, HashVal val)
        
        /**
         * Set the hash value of file we are working on
         */
        """
        pass

    def set_server_multifile_size(self, const_DownloadDb_self, str_mfname, int_size): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_server_multifile_size(const DownloadDb self, str mfname, int size)
        
        /**
         *
         */
        """
        pass

    def write(self, DownloadDb_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(DownloadDb self, ostream out)
        
        /**
         *
         */
        """
        pass

    def writeClientDb(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        write_client_db(const DownloadDb self, Filename file)
        
        // Write a database file
        
        /**
         *
         */
        """
        pass

    def writeServerDb(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        write_server_db(const DownloadDb self, Filename file)
        
        /**
         *
         */
        """
        pass

    def writeVersionMap(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        write_version_map(DownloadDb self, ostream out)
        
        /**
         *
         */
        
        /**
         *
         */
        """
        pass

    def write_client_db(self, const_DownloadDb_self, Filename_file): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write_client_db(const DownloadDb self, Filename file)
        
        // Write a database file
        
        /**
         *
         */
        """
        pass

    def write_server_db(self, const_DownloadDb_self, Filename_file): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write_server_db(const DownloadDb self, Filename file)
        
        /**
         *
         */
        """
        pass

    def write_version_map(self, DownloadDb_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write_version_map(DownloadDb self, ostream out)
        
        /**
         *
         */
        
        /**
         *
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

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        'StatusComplete': 1,
        'StatusDecompressed': 2,
        'StatusExtracted': 3,
        'StatusIncomplete': 0,
        'Status_complete': 1,
        'Status_decompressed': 2,
        'Status_extracted': 3,
        'Status_incomplete': 0,
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.DownloadDb' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.DownloadDb' objects>"
        '__doc__': '/**\n * A listing of files within multifiles for management of client-side\n * synchronization with a server-provided set of files.\n *\n * This class manages one copy of the database for the client, representing\n * the files on the client system, and another copy for the server,\n * representing the files the server has available.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.DownloadDb' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE26D220>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.DownloadDb' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.DownloadDb' objects>"
        'addClientMultifile': None, # (!) real value is "<method 'addClientMultifile' of 'panda3d.core.DownloadDb' objects>"
        'addVersion': None, # (!) real value is "<method 'addVersion' of 'panda3d.core.DownloadDb' objects>"
        'add_client_multifile': None, # (!) real value is "<method 'add_client_multifile' of 'panda3d.core.DownloadDb' objects>"
        'add_version': None, # (!) real value is "<method 'add_version' of 'panda3d.core.DownloadDb' objects>"
        'clientMultifileComplete': None, # (!) real value is "<method 'clientMultifileComplete' of 'panda3d.core.DownloadDb' objects>"
        'clientMultifileDecompressed': None, # (!) real value is "<method 'clientMultifileDecompressed' of 'panda3d.core.DownloadDb' objects>"
        'clientMultifileExists': None, # (!) real value is "<method 'clientMultifileExists' of 'panda3d.core.DownloadDb' objects>"
        'clientMultifileExtracted': None, # (!) real value is "<method 'clientMultifileExtracted' of 'panda3d.core.DownloadDb' objects>"
        'client_multifile_complete': None, # (!) real value is "<method 'client_multifile_complete' of 'panda3d.core.DownloadDb' objects>"
        'client_multifile_decompressed': None, # (!) real value is "<method 'client_multifile_decompressed' of 'panda3d.core.DownloadDb' objects>"
        'client_multifile_exists': None, # (!) real value is "<method 'client_multifile_exists' of 'panda3d.core.DownloadDb' objects>"
        'client_multifile_extracted': None, # (!) real value is "<method 'client_multifile_extracted' of 'panda3d.core.DownloadDb' objects>"
        'createNewServerDb': None, # (!) real value is "<method 'createNewServerDb' of 'panda3d.core.DownloadDb' objects>"
        'create_new_server_db': None, # (!) real value is "<method 'create_new_server_db' of 'panda3d.core.DownloadDb' objects>"
        'deleteClientMultifile': None, # (!) real value is "<method 'deleteClientMultifile' of 'panda3d.core.DownloadDb' objects>"
        'delete_client_multifile': None, # (!) real value is "<method 'delete_client_multifile' of 'panda3d.core.DownloadDb' objects>"
        'expandClientMultifile': None, # (!) real value is "<method 'expandClientMultifile' of 'panda3d.core.DownloadDb' objects>"
        'expand_client_multifile': None, # (!) real value is "<method 'expand_client_multifile' of 'panda3d.core.DownloadDb' objects>"
        'getClientMultifileHash': None, # (!) real value is "<method 'getClientMultifileHash' of 'panda3d.core.DownloadDb' objects>"
        'getClientMultifileName': None, # (!) real value is "<method 'getClientMultifileName' of 'panda3d.core.DownloadDb' objects>"
        'getClientMultifilePhase': None, # (!) real value is "<method 'getClientMultifilePhase' of 'panda3d.core.DownloadDb' objects>"
        'getClientMultifileSize': None, # (!) real value is "<method 'getClientMultifileSize' of 'panda3d.core.DownloadDb' objects>"
        'getClientNumMultifiles': None, # (!) real value is "<method 'getClientNumMultifiles' of 'panda3d.core.DownloadDb' objects>"
        'getHash': None, # (!) real value is "<method 'getHash' of 'panda3d.core.DownloadDb' objects>"
        'getNumVersions': None, # (!) real value is "<method 'getNumVersions' of 'panda3d.core.DownloadDb' objects>"
        'getServerFileName': None, # (!) real value is "<method 'getServerFileName' of 'panda3d.core.DownloadDb' objects>"
        'getServerMultifileHash': None, # (!) real value is "<method 'getServerMultifileHash' of 'panda3d.core.DownloadDb' objects>"
        'getServerMultifileName': None, # (!) real value is "<method 'getServerMultifileName' of 'panda3d.core.DownloadDb' objects>"
        'getServerMultifilePhase': None, # (!) real value is "<method 'getServerMultifilePhase' of 'panda3d.core.DownloadDb' objects>"
        'getServerMultifileSize': None, # (!) real value is "<method 'getServerMultifileSize' of 'panda3d.core.DownloadDb' objects>"
        'getServerNumFiles': None, # (!) real value is "<method 'getServerNumFiles' of 'panda3d.core.DownloadDb' objects>"
        'getServerNumMultifiles': None, # (!) real value is "<method 'getServerNumMultifiles' of 'panda3d.core.DownloadDb' objects>"
        'getVersion': None, # (!) real value is "<method 'getVersion' of 'panda3d.core.DownloadDb' objects>"
        'get_client_multifile_hash': None, # (!) real value is "<method 'get_client_multifile_hash' of 'panda3d.core.DownloadDb' objects>"
        'get_client_multifile_name': None, # (!) real value is "<method 'get_client_multifile_name' of 'panda3d.core.DownloadDb' objects>"
        'get_client_multifile_phase': None, # (!) real value is "<method 'get_client_multifile_phase' of 'panda3d.core.DownloadDb' objects>"
        'get_client_multifile_size': None, # (!) real value is "<method 'get_client_multifile_size' of 'panda3d.core.DownloadDb' objects>"
        'get_client_num_multifiles': None, # (!) real value is "<method 'get_client_num_multifiles' of 'panda3d.core.DownloadDb' objects>"
        'get_hash': None, # (!) real value is "<method 'get_hash' of 'panda3d.core.DownloadDb' objects>"
        'get_num_versions': None, # (!) real value is "<method 'get_num_versions' of 'panda3d.core.DownloadDb' objects>"
        'get_server_file_name': None, # (!) real value is "<method 'get_server_file_name' of 'panda3d.core.DownloadDb' objects>"
        'get_server_multifile_hash': None, # (!) real value is "<method 'get_server_multifile_hash' of 'panda3d.core.DownloadDb' objects>"
        'get_server_multifile_name': None, # (!) real value is "<method 'get_server_multifile_name' of 'panda3d.core.DownloadDb' objects>"
        'get_server_multifile_phase': None, # (!) real value is "<method 'get_server_multifile_phase' of 'panda3d.core.DownloadDb' objects>"
        'get_server_multifile_size': None, # (!) real value is "<method 'get_server_multifile_size' of 'panda3d.core.DownloadDb' objects>"
        'get_server_num_files': None, # (!) real value is "<method 'get_server_num_files' of 'panda3d.core.DownloadDb' objects>"
        'get_server_num_multifiles': None, # (!) real value is "<method 'get_server_num_multifiles' of 'panda3d.core.DownloadDb' objects>"
        'get_version': None, # (!) real value is "<method 'get_version' of 'panda3d.core.DownloadDb' objects>"
        'hasVersion': None, # (!) real value is "<method 'hasVersion' of 'panda3d.core.DownloadDb' objects>"
        'has_version': None, # (!) real value is "<method 'has_version' of 'panda3d.core.DownloadDb' objects>"
        'insertNewVersion': None, # (!) real value is "<method 'insertNewVersion' of 'panda3d.core.DownloadDb' objects>"
        'insert_new_version': None, # (!) real value is "<method 'insert_new_version' of 'panda3d.core.DownloadDb' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.DownloadDb' objects>"
        'serverAddFile': None, # (!) real value is "<method 'serverAddFile' of 'panda3d.core.DownloadDb' objects>"
        'serverAddMultifile': None, # (!) real value is "<method 'serverAddMultifile' of 'panda3d.core.DownloadDb' objects>"
        'server_add_file': None, # (!) real value is "<method 'server_add_file' of 'panda3d.core.DownloadDb' objects>"
        'server_add_multifile': None, # (!) real value is "<method 'server_add_multifile' of 'panda3d.core.DownloadDb' objects>"
        'setClientMultifileComplete': None, # (!) real value is "<method 'setClientMultifileComplete' of 'panda3d.core.DownloadDb' objects>"
        'setClientMultifileDecompressed': None, # (!) real value is "<method 'setClientMultifileDecompressed' of 'panda3d.core.DownloadDb' objects>"
        'setClientMultifileDeltaSize': None, # (!) real value is "<method 'setClientMultifileDeltaSize' of 'panda3d.core.DownloadDb' objects>"
        'setClientMultifileExtracted': None, # (!) real value is "<method 'setClientMultifileExtracted' of 'panda3d.core.DownloadDb' objects>"
        'setClientMultifileHash': None, # (!) real value is "<method 'setClientMultifileHash' of 'panda3d.core.DownloadDb' objects>"
        'setClientMultifileIncomplete': None, # (!) real value is "<method 'setClientMultifileIncomplete' of 'panda3d.core.DownloadDb' objects>"
        'setClientMultifileSize': None, # (!) real value is "<method 'setClientMultifileSize' of 'panda3d.core.DownloadDb' objects>"
        'setNumVersions': None, # (!) real value is "<method 'setNumVersions' of 'panda3d.core.DownloadDb' objects>"
        'setServerMultifileHash': None, # (!) real value is "<method 'setServerMultifileHash' of 'panda3d.core.DownloadDb' objects>"
        'setServerMultifileSize': None, # (!) real value is "<method 'setServerMultifileSize' of 'panda3d.core.DownloadDb' objects>"
        'set_client_multifile_complete': None, # (!) real value is "<method 'set_client_multifile_complete' of 'panda3d.core.DownloadDb' objects>"
        'set_client_multifile_decompressed': None, # (!) real value is "<method 'set_client_multifile_decompressed' of 'panda3d.core.DownloadDb' objects>"
        'set_client_multifile_delta_size': None, # (!) real value is "<method 'set_client_multifile_delta_size' of 'panda3d.core.DownloadDb' objects>"
        'set_client_multifile_extracted': None, # (!) real value is "<method 'set_client_multifile_extracted' of 'panda3d.core.DownloadDb' objects>"
        'set_client_multifile_hash': None, # (!) real value is "<method 'set_client_multifile_hash' of 'panda3d.core.DownloadDb' objects>"
        'set_client_multifile_incomplete': None, # (!) real value is "<method 'set_client_multifile_incomplete' of 'panda3d.core.DownloadDb' objects>"
        'set_client_multifile_size': None, # (!) real value is "<method 'set_client_multifile_size' of 'panda3d.core.DownloadDb' objects>"
        'set_num_versions': None, # (!) real value is "<method 'set_num_versions' of 'panda3d.core.DownloadDb' objects>"
        'set_server_multifile_hash': None, # (!) real value is "<method 'set_server_multifile_hash' of 'panda3d.core.DownloadDb' objects>"
        'set_server_multifile_size': None, # (!) real value is "<method 'set_server_multifile_size' of 'panda3d.core.DownloadDb' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.core.DownloadDb' objects>"
        'writeClientDb': None, # (!) real value is "<method 'writeClientDb' of 'panda3d.core.DownloadDb' objects>"
        'writeServerDb': None, # (!) real value is "<method 'writeServerDb' of 'panda3d.core.DownloadDb' objects>"
        'writeVersionMap': None, # (!) real value is "<method 'writeVersionMap' of 'panda3d.core.DownloadDb' objects>"
        'write_client_db': None, # (!) real value is "<method 'write_client_db' of 'panda3d.core.DownloadDb' objects>"
        'write_server_db': None, # (!) real value is "<method 'write_server_db' of 'panda3d.core.DownloadDb' objects>"
        'write_version_map': None, # (!) real value is "<method 'write_version_map' of 'panda3d.core.DownloadDb' objects>"
    }
    StatusComplete = 1
    StatusDecompressed = 2
    StatusExtracted = 3
    StatusIncomplete = 0
    Status_complete = 1
    Status_decompressed = 2
    Status_extracted = 3
    Status_incomplete = 0


