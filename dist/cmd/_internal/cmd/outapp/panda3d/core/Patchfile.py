# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class Patchfile(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     *
     */
    """
    def apply(self, const_Patchfile_self, Filename_patch_file, Filename_file): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        apply(const Patchfile self, Filename patch_file, Filename file)
        apply(const Patchfile self, Filename patch_file, Filename orig_file, const Filename target_file)
        
        /**
         * Patches the entire file in one call returns true on success and false on
         * error
         *
         * This version will delete the patch file and overwrite the original file.
         */
        
        /**
         * Patches the entire file in one call returns true on success and false on
         * error
         *
         * This version will not delete any files.
         */
        """
        pass

    def build(self, const_Patchfile_self, Filename_file_orig, Filename_file_new, Filename_patch_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        build(const Patchfile self, Filename file_orig, Filename file_new, Filename patch_name)
        
        /**
         *
         * This implementation uses the "greedy differencing algorithm" described in
         * the masters thesis "Differential Compression: A Generalized Solution for
         * Binary Files" by Randal C. Burns (p.13). For an original file of size M and
         * a new file of size N, this algorithm is O(M) in space and O(M*N) (worst-
         * case) in time.  return false on error
         */
        """
        pass

    def getAllowMultifile(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_allow_multifile(const Patchfile self)
        
        /**
         * See set_allow_multifile().
         */
        """
        pass

    def getFootprintLength(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_footprint_length(const Patchfile self)
        
        /**
         *
         */
        """
        pass

    def getProgress(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_progress(Patchfile self)
        
        /**
         * Returns a value in the range 0..1, representing the amount of progress
         * through the patchfile, during a session.
         */
        """
        pass

    def getResultHash(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_result_hash(Patchfile self)
        
        /**
         * Returns the MD5 hash for the file after the patch has been applied.
         */
        """
        pass

    def getSourceHash(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_source_hash(Patchfile self)
        
        /**
         * Returns the MD5 hash for the source file.
         */
        """
        pass

    def get_allow_multifile(self, const_Patchfile_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_allow_multifile(const Patchfile self)
        
        /**
         * See set_allow_multifile().
         */
        """
        pass

    def get_footprint_length(self, const_Patchfile_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_footprint_length(const Patchfile self)
        
        /**
         *
         */
        """
        pass

    def get_progress(self, Patchfile_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_progress(Patchfile self)
        
        /**
         * Returns a value in the range 0..1, representing the amount of progress
         * through the patchfile, during a session.
         */
        """
        pass

    def get_result_hash(self, Patchfile_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_result_hash(Patchfile self)
        
        /**
         * Returns the MD5 hash for the file after the patch has been applied.
         */
        """
        pass

    def get_source_hash(self, Patchfile_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_source_hash(Patchfile self)
        
        /**
         * Returns the MD5 hash for the source file.
         */
        """
        pass

    def hasSourceHash(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_source_hash(Patchfile self)
        
        /**
         * Returns true if the MD5 hash for the source file is known.  (Some early
         * versions of the patch file did not store this information.)
         */
        """
        pass

    def has_source_hash(self, Patchfile_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_source_hash(Patchfile self)
        
        /**
         * Returns true if the MD5 hash for the source file is known.  (Some early
         * versions of the patch file did not store this information.)
         */
        """
        pass

    def initiate(self, const_Patchfile_self, const_Filename_patch_file, const_Filename_file): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        initiate(const Patchfile self, const Filename patch_file, const Filename file)
        initiate(const Patchfile self, const Filename patch_file, const Filename orig_file, const Filename target_file)
        
        /**
         * Set up to apply the patch to the file (original file and patch are
         * destroyed in the process).
         */
        
        /**
         * Set up to apply the patch to the file.  In this form, neither the original
         * file nor the patch file are destroyed.
         */
        """
        pass

    def readHeader(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        read_header(const Patchfile self, const Filename patch_file)
        
        /**
         * Opens the patch file for reading, and gets the header information from the
         * file but does not begin to do any real work.  This can be used to query the
         * data stored in the patch.
         */
        """
        pass

    def read_header(self, const_Patchfile_self, const_Filename_patch_file): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        read_header(const Patchfile self, const Filename patch_file)
        
        /**
         * Opens the patch file for reading, and gets the header information from the
         * file but does not begin to do any real work.  This can be used to query the
         * data stored in the patch.
         */
        """
        pass

    def resetFootprintLength(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        reset_footprint_length(const Patchfile self)
        
        /**
         *
         */
        """
        pass

    def reset_footprint_length(self, const_Patchfile_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        reset_footprint_length(const Patchfile self)
        
        /**
         *
         */
        """
        pass

    def run(self, const_Patchfile_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        run(const Patchfile self)
        
        /**
         * Perform one buffer's worth of patching.
         * Returns one of the following values:
         * @li @c EU_ok : while patching
         * @li @c EU_success : when done
         * @li @c EU_error_abort : Patching has not been initiated
         * @li @c EU_error_file_invalid : file is corrupted
         * @li @c EU_error_invalid_checksum : incompatible patch file
         * @li @c EU_error_write_file_rename : could not rename file
         */
        """
        pass

    def setAllowMultifile(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_allow_multifile(const Patchfile self, bool allow_multifile)
        
        /**
         * If this flag is set true, the Patchfile will make a special case for
         * patching Panda Multifiles, if detected, and attempt to patch them on a
         * subfile-by-subfile basis.  If this flag is false, the Patchfile will always
         * patch the file on a full-file basis.
         *
         * This has effect only when building patches; it is not used for applying
         * patches.
         */
        """
        pass

    def setFootprintLength(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_footprint_length(const Patchfile self, int length)
        
        /**
         *
         */
        """
        pass

    def set_allow_multifile(self, const_Patchfile_self, bool_allow_multifile): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_allow_multifile(const Patchfile self, bool allow_multifile)
        
        /**
         * If this flag is set true, the Patchfile will make a special case for
         * patching Panda Multifiles, if detected, and attempt to patch them on a
         * subfile-by-subfile basis.  If this flag is false, the Patchfile will always
         * patch the file on a full-file basis.
         *
         * This has effect only when building patches; it is not used for applying
         * patches.
         */
        """
        pass

    def set_footprint_length(self, const_Patchfile_self, int_length): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_footprint_length(const Patchfile self, int length)
        
        /**
         *
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    allow_multifile = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    footprint_length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    progress = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    result_hash = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    source_hash = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n *\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.Patchfile' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE27B180>'
        'allow_multifile': None, # (!) real value is "<attribute 'allow_multifile' of 'panda3d.core.Patchfile' objects>"
        'apply': None, # (!) real value is "<method 'apply' of 'panda3d.core.Patchfile' objects>"
        'build': None, # (!) real value is "<method 'build' of 'panda3d.core.Patchfile' objects>"
        'footprint_length': None, # (!) real value is "<attribute 'footprint_length' of 'panda3d.core.Patchfile' objects>"
        'getAllowMultifile': None, # (!) real value is "<method 'getAllowMultifile' of 'panda3d.core.Patchfile' objects>"
        'getFootprintLength': None, # (!) real value is "<method 'getFootprintLength' of 'panda3d.core.Patchfile' objects>"
        'getProgress': None, # (!) real value is "<method 'getProgress' of 'panda3d.core.Patchfile' objects>"
        'getResultHash': None, # (!) real value is "<method 'getResultHash' of 'panda3d.core.Patchfile' objects>"
        'getSourceHash': None, # (!) real value is "<method 'getSourceHash' of 'panda3d.core.Patchfile' objects>"
        'get_allow_multifile': None, # (!) real value is "<method 'get_allow_multifile' of 'panda3d.core.Patchfile' objects>"
        'get_footprint_length': None, # (!) real value is "<method 'get_footprint_length' of 'panda3d.core.Patchfile' objects>"
        'get_progress': None, # (!) real value is "<method 'get_progress' of 'panda3d.core.Patchfile' objects>"
        'get_result_hash': None, # (!) real value is "<method 'get_result_hash' of 'panda3d.core.Patchfile' objects>"
        'get_source_hash': None, # (!) real value is "<method 'get_source_hash' of 'panda3d.core.Patchfile' objects>"
        'hasSourceHash': None, # (!) real value is "<method 'hasSourceHash' of 'panda3d.core.Patchfile' objects>"
        'has_source_hash': None, # (!) real value is "<method 'has_source_hash' of 'panda3d.core.Patchfile' objects>"
        'initiate': None, # (!) real value is "<method 'initiate' of 'panda3d.core.Patchfile' objects>"
        'progress': None, # (!) real value is "<attribute 'progress' of 'panda3d.core.Patchfile' objects>"
        'readHeader': None, # (!) real value is "<method 'readHeader' of 'panda3d.core.Patchfile' objects>"
        'read_header': None, # (!) real value is "<method 'read_header' of 'panda3d.core.Patchfile' objects>"
        'resetFootprintLength': None, # (!) real value is "<method 'resetFootprintLength' of 'panda3d.core.Patchfile' objects>"
        'reset_footprint_length': None, # (!) real value is "<method 'reset_footprint_length' of 'panda3d.core.Patchfile' objects>"
        'result_hash': None, # (!) real value is "<attribute 'result_hash' of 'panda3d.core.Patchfile' objects>"
        'run': None, # (!) real value is "<method 'run' of 'panda3d.core.Patchfile' objects>"
        'setAllowMultifile': None, # (!) real value is "<method 'setAllowMultifile' of 'panda3d.core.Patchfile' objects>"
        'setFootprintLength': None, # (!) real value is "<method 'setFootprintLength' of 'panda3d.core.Patchfile' objects>"
        'set_allow_multifile': None, # (!) real value is "<method 'set_allow_multifile' of 'panda3d.core.Patchfile' objects>"
        'set_footprint_length': None, # (!) real value is "<method 'set_footprint_length' of 'panda3d.core.Patchfile' objects>"
        'source_hash': None, # (!) real value is "<attribute 'source_hash' of 'panda3d.core.Patchfile' objects>"
    }


