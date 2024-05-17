# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class BamCache(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * This class maintains a cache of Bam and/or Txo objects generated from model
     * files and texture images (as well as possibly other kinds of loadable
     * objects that can be stored in bam file format).
     *
     * This class also maintains a persistent index that lists all of the cached
     * objects (see BamCacheIndex). We go through some considerable effort to make
     * sure this index gets saved correctly to disk, even in the presence of
     * multiple different processes writing to the same index, and without relying
     * too heavily on low-level os-provided file locks (which work poorly with C++
     * iostreams).
     */
    """
    def considerFlushGlobalIndex(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        consider_flush_global_index()
        
        /**
         * If there is a global BamCache object, calls consider_flush_index() on it.
         */
        """
        pass

    def considerFlushIndex(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        consider_flush_index(const BamCache self)
        
        /**
         * Flushes the index if enough time has elapsed since the index was last
         * flushed.
         */
        """
        pass

    def consider_flush_global_index(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        consider_flush_global_index()
        
        /**
         * If there is a global BamCache object, calls consider_flush_index() on it.
         */
        """
        pass

    def consider_flush_index(self, const_BamCache_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        consider_flush_index(const BamCache self)
        
        /**
         * Flushes the index if enough time has elapsed since the index was last
         * flushed.
         */
        """
        pass

    def flushGlobalIndex(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        flush_global_index()
        
        /**
         * If there is a global BamCache object, calls flush_index() on it.
         */
        """
        pass

    def flushIndex(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        flush_index(const BamCache self)
        
        /**
         * Ensures the index is written to disk.
         */
        """
        pass

    def flush_global_index(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        flush_global_index()
        
        /**
         * If there is a global BamCache object, calls flush_index() on it.
         */
        """
        pass

    def flush_index(self, const_BamCache_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        flush_index(const BamCache self)
        
        /**
         * Ensures the index is written to disk.
         */
        """
        pass

    def getActive(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_active(BamCache self)
        
        /**
         * Returns true if the BamCache is currently active, false if it is not.
         * "active" means that the cache should be consulted automatically on loads,
         * "not active" means that objects should be loaded directly without
         * consulting the cache.
         *
         * This represents the global flag.  Also see the individual cache_models,
         * cache_textures, cache_compressed_textures flags.
         */
        """
        pass

    def getCacheCompiledShaders(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_cache_compiled_shaders(BamCache self)
        
        /**
         * Returns whether compiled shader programs will be stored in the cache, as
         * binary .txo files.  See set_cache_compiled_shaders().
         *
         * This also returns false if get_active() is false.
         */
        """
        pass

    def getCacheCompressedTextures(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_cache_compressed_textures(BamCache self)
        
        /**
         * Returns whether compressed texture files will be stored in the cache, as
         * compressed txo files.  See set_cache_compressed_textures().
         *
         * This also returns false if get_active() is false.
         */
        """
        pass

    def getCacheMaxKbytes(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_cache_max_kbytes(BamCache self)
        
        /**
         * Returns the maximum size, in kilobytes, which the cache is allowed to grow
         * to.  See set_cache_max_kbytes().
         */
        """
        pass

    def getCacheModels(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_cache_models(BamCache self)
        
        /**
         * Returns whether model files (e.g.  egg files and bam files) will be stored
         * in the cache, as bam files.
         *
         * This also returns false if get_active() is false.
         */
        """
        pass

    def getCacheTextures(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_cache_textures(BamCache self)
        
        /**
         * Returns whether texture files (e.g.  egg files and bam files) will be
         * stored in the cache, as txo files.
         *
         * This also returns false if get_active() is false.
         */
        """
        pass

    def getFlushTime(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_flush_time(BamCache self)
        
        /**
         * Returns the time in seconds between automatic flushes of the cache index.
         */
        """
        pass

    def getGlobalPtr(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_global_ptr()
        
        /**
         * Returns a pointer to the global BamCache object, which is used
         * automatically by the ModelPool and TexturePool.
         */
        """
        pass

    def getReadOnly(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_read_only(BamCache self)
        
        /**
         * Returns true if the cache is in read-only mode.  Normally, the cache starts
         * in read-write mode.  It can put itself into read-only mode automatically if
         * it discovers that it does not have write access to the cache.
         */
        """
        pass

    def getRoot(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_root(BamCache self)
        
        /**
         * Returns the current root pathname of the cache.  See set_root().
         */
        """
        pass

    def get_active(self, BamCache_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_active(BamCache self)
        
        /**
         * Returns true if the BamCache is currently active, false if it is not.
         * "active" means that the cache should be consulted automatically on loads,
         * "not active" means that objects should be loaded directly without
         * consulting the cache.
         *
         * This represents the global flag.  Also see the individual cache_models,
         * cache_textures, cache_compressed_textures flags.
         */
        """
        pass

    def get_cache_compiled_shaders(self, BamCache_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_cache_compiled_shaders(BamCache self)
        
        /**
         * Returns whether compiled shader programs will be stored in the cache, as
         * binary .txo files.  See set_cache_compiled_shaders().
         *
         * This also returns false if get_active() is false.
         */
        """
        pass

    def get_cache_compressed_textures(self, BamCache_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_cache_compressed_textures(BamCache self)
        
        /**
         * Returns whether compressed texture files will be stored in the cache, as
         * compressed txo files.  See set_cache_compressed_textures().
         *
         * This also returns false if get_active() is false.
         */
        """
        pass

    def get_cache_max_kbytes(self, BamCache_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_cache_max_kbytes(BamCache self)
        
        /**
         * Returns the maximum size, in kilobytes, which the cache is allowed to grow
         * to.  See set_cache_max_kbytes().
         */
        """
        pass

    def get_cache_models(self, BamCache_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_cache_models(BamCache self)
        
        /**
         * Returns whether model files (e.g.  egg files and bam files) will be stored
         * in the cache, as bam files.
         *
         * This also returns false if get_active() is false.
         */
        """
        pass

    def get_cache_textures(self, BamCache_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_cache_textures(BamCache self)
        
        /**
         * Returns whether texture files (e.g.  egg files and bam files) will be
         * stored in the cache, as txo files.
         *
         * This also returns false if get_active() is false.
         */
        """
        pass

    def get_flush_time(self, BamCache_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_flush_time(BamCache self)
        
        /**
         * Returns the time in seconds between automatic flushes of the cache index.
         */
        """
        pass

    def get_global_ptr(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_global_ptr()
        
        /**
         * Returns a pointer to the global BamCache object, which is used
         * automatically by the ModelPool and TexturePool.
         */
        """
        pass

    def get_read_only(self, BamCache_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_read_only(BamCache self)
        
        /**
         * Returns true if the cache is in read-only mode.  Normally, the cache starts
         * in read-write mode.  It can put itself into read-only mode automatically if
         * it discovers that it does not have write access to the cache.
         */
        """
        pass

    def get_root(self, BamCache_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_root(BamCache self)
        
        /**
         * Returns the current root pathname of the cache.  See set_root().
         */
        """
        pass

    def listIndex(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        list_index(BamCache self, ostream out, int indent_level)
        
        /**
         * Writes the contents of the index to standard output.
         */
        """
        pass

    def list_index(self, BamCache_self, ostream_out, int_indent_level): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        list_index(BamCache self, ostream out, int indent_level)
        
        /**
         * Writes the contents of the index to standard output.
         */
        """
        pass

    def lookup(self, const_BamCache_self, const_Filename_source_filename, str_cache_extension): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        lookup(const BamCache self, const Filename source_filename, str cache_extension)
        
        /**
         * Looks up a file in the cache.
         *
         * If the file is cacheable, then regardless of whether the file is found in
         * the cache or not, this returns a BamCacheRecord.  On the other hand, if the
         * file cannot be cached, returns NULL.
         *
         * If record->has_data() returns true, then the file was found in the cache,
         * and you may call record->extract_data() to get the object.  If
         * record->has_data() returns false, then the file was not found in the cache
         * or the cache was stale; and you should reload the source file (calling
         * record->add_dependent_file() for each file loaded, including the original
         * source file), and then call record->set_data() to record the resulting
         * loaded object; and finally, you should call store() to write the cached
         * record to disk.
         */
        """
        pass

    def setActive(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_active(const BamCache self, bool flag)
        
        /**
         * Changes the state of the active flag.  "active" means that the cache should
         * be consulted automatically on loads, "not active" means that objects should
         * be loaded directly without consulting the cache.
         *
         * This represents the global flag.  Also see the individual cache_models,
         * cache_textures, cache_compressed_textures flags.
         */
        """
        pass

    def setCacheCompiledShaders(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_cache_compiled_shaders(const BamCache self, bool flag)
        
        /**
         * Indicates whether compiled shader programs will be stored in the cache, as
         * binary .sho files.  This may not be supported by all shader languages or
         * graphics renderers.
         */
        """
        pass

    def setCacheCompressedTextures(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_cache_compressed_textures(const BamCache self, bool flag)
        
        /**
         * Indicates whether compressed texture files will be stored in the cache, as
         * compressed txo files.  The compressed data may either be generated in-CPU,
         * via the squish library, or it may be extracted from the GSG after the
         * texture has been loaded.
         *
         * This may be set in conjunction with set_cache_textures(), or independently
         * of it.  If set_cache_textures() is true and this is false, all textures
         * will be cached in their uncompressed form.  If set_cache_textures() is
         * false and this is true, only compressed textures will be cached, and they
         * will be cached in their compressed form.  If both are true, all textures
         * will be cached, in their uncompressed or compressed form appropriately.
         */
        """
        pass

    def setCacheMaxKbytes(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_cache_max_kbytes(const BamCache self, int max_kbytes)
        
        /**
         * Specifies the maximum size, in kilobytes, which the cache is allowed to
         * grow to.  If a newly cached file would exceed this size, an older file is
         * removed from the cache.
         *
         * Note that in the case of multiple different processes simultaneously
         * operating on the same cache directory, the actual cache size may slightly
         * exceed this value from time to time due to latency in checking between the
         * processes.
         */
        """
        pass

    def setCacheModels(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_cache_models(const BamCache self, bool flag)
        
        /**
         * Indicates whether model files (e.g.  egg files and bam files) will be
         * stored in the cache, as bam files.
         */
        """
        pass

    def setCacheTextures(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_cache_textures(const BamCache self, bool flag)
        
        /**
         * Indicates whether texture files will be stored in the cache, as
         * uncompressed txo files.
         */
        """
        pass

    def setFlushTime(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_flush_time(const BamCache self, int flush_time)
        
        /**
         * Specifies the time in seconds between automatic flushes of the cache index.
         */
        """
        pass

    def setReadOnly(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_read_only(const BamCache self, bool ro)
        
        /**
         * Can be used to put the cache in read-only mode, or take it out of read-only
         * mode.  Note that if you put it into read-write mode, and it discovers that
         * it does not have write access, it will put itself right back into read-only
         * mode.
         */
        """
        pass

    def setRoot(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_root(const BamCache self, const Filename root)
        
        /**
         * Changes the current root pathname of the cache.  This specifies where the
         * cache files are stored on disk.  This should name a directory that is on a
         * disk local to the machine (not on a network-mounted disk), for instance,
         * /tmp/panda-cache or /c/panda-cache.
         *
         * If the directory does not already exist, it will be created as a result of
         * this call.
         */
        """
        pass

    def set_active(self, const_BamCache_self, bool_flag): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_active(const BamCache self, bool flag)
        
        /**
         * Changes the state of the active flag.  "active" means that the cache should
         * be consulted automatically on loads, "not active" means that objects should
         * be loaded directly without consulting the cache.
         *
         * This represents the global flag.  Also see the individual cache_models,
         * cache_textures, cache_compressed_textures flags.
         */
        """
        pass

    def set_cache_compiled_shaders(self, const_BamCache_self, bool_flag): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_cache_compiled_shaders(const BamCache self, bool flag)
        
        /**
         * Indicates whether compiled shader programs will be stored in the cache, as
         * binary .sho files.  This may not be supported by all shader languages or
         * graphics renderers.
         */
        """
        pass

    def set_cache_compressed_textures(self, const_BamCache_self, bool_flag): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_cache_compressed_textures(const BamCache self, bool flag)
        
        /**
         * Indicates whether compressed texture files will be stored in the cache, as
         * compressed txo files.  The compressed data may either be generated in-CPU,
         * via the squish library, or it may be extracted from the GSG after the
         * texture has been loaded.
         *
         * This may be set in conjunction with set_cache_textures(), or independently
         * of it.  If set_cache_textures() is true and this is false, all textures
         * will be cached in their uncompressed form.  If set_cache_textures() is
         * false and this is true, only compressed textures will be cached, and they
         * will be cached in their compressed form.  If both are true, all textures
         * will be cached, in their uncompressed or compressed form appropriately.
         */
        """
        pass

    def set_cache_max_kbytes(self, const_BamCache_self, int_max_kbytes): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_cache_max_kbytes(const BamCache self, int max_kbytes)
        
        /**
         * Specifies the maximum size, in kilobytes, which the cache is allowed to
         * grow to.  If a newly cached file would exceed this size, an older file is
         * removed from the cache.
         *
         * Note that in the case of multiple different processes simultaneously
         * operating on the same cache directory, the actual cache size may slightly
         * exceed this value from time to time due to latency in checking between the
         * processes.
         */
        """
        pass

    def set_cache_models(self, const_BamCache_self, bool_flag): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_cache_models(const BamCache self, bool flag)
        
        /**
         * Indicates whether model files (e.g.  egg files and bam files) will be
         * stored in the cache, as bam files.
         */
        """
        pass

    def set_cache_textures(self, const_BamCache_self, bool_flag): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_cache_textures(const BamCache self, bool flag)
        
        /**
         * Indicates whether texture files will be stored in the cache, as
         * uncompressed txo files.
         */
        """
        pass

    def set_flush_time(self, const_BamCache_self, int_flush_time): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_flush_time(const BamCache self, int flush_time)
        
        /**
         * Specifies the time in seconds between automatic flushes of the cache index.
         */
        """
        pass

    def set_read_only(self, const_BamCache_self, bool_ro): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_read_only(const BamCache self, bool ro)
        
        /**
         * Can be used to put the cache in read-only mode, or take it out of read-only
         * mode.  Note that if you put it into read-write mode, and it discovers that
         * it does not have write access, it will put itself right back into read-only
         * mode.
         */
        """
        pass

    def set_root(self, const_BamCache_self, const_Filename_root): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_root(const BamCache self, const Filename root)
        
        /**
         * Changes the current root pathname of the cache.  This specifies where the
         * cache files are stored on disk.  This should name a directory that is on a
         * disk local to the machine (not on a network-mounted disk), for instance,
         * /tmp/panda-cache or /c/panda-cache.
         *
         * If the directory does not already exist, it will be created as a result of
         * this call.
         */
        """
        pass

    def store(self, const_BamCache_self, BamCacheRecord_record): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        store(const BamCache self, BamCacheRecord record)
        
        /**
         * Flushes a cache entry to disk.  You must have retrieved the cache record
         * via a prior call to lookup(), and then stored the data via
         * record->set_data().  Returns true on success, false on failure.
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    active = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    cache_compiled_shaders = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    cache_compressed_textures = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    cache_max_kbytes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    cache_models = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    cache_textures = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    flush_time = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    read_only = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    root = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * This class maintains a cache of Bam and/or Txo objects generated from model\n * files and texture images (as well as possibly other kinds of loadable\n * objects that can be stored in bam file format).\n *\n * This class also maintains a persistent index that lists all of the cached\n * objects (see BamCacheIndex). We go through some considerable effort to make\n * sure this index gets saved correctly to disk, even in the presence of\n * multiple different processes writing to the same index, and without relying\n * too heavily on low-level os-provided file locks (which work poorly with C++\n * iostreams).\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.BamCache' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE36FAA0>'
        'active': None, # (!) real value is "<attribute 'active' of 'panda3d.core.BamCache' objects>"
        'cache_compiled_shaders': None, # (!) real value is "<attribute 'cache_compiled_shaders' of 'panda3d.core.BamCache' objects>"
        'cache_compressed_textures': None, # (!) real value is "<attribute 'cache_compressed_textures' of 'panda3d.core.BamCache' objects>"
        'cache_max_kbytes': None, # (!) real value is "<attribute 'cache_max_kbytes' of 'panda3d.core.BamCache' objects>"
        'cache_models': None, # (!) real value is "<attribute 'cache_models' of 'panda3d.core.BamCache' objects>"
        'cache_textures': None, # (!) real value is "<attribute 'cache_textures' of 'panda3d.core.BamCache' objects>"
        'considerFlushGlobalIndex': None, # (!) real value is '<staticmethod(<built-in method considerFlushGlobalIndex of type object at 0x00007FFCFE36FAA0>)>'
        'considerFlushIndex': None, # (!) real value is "<method 'considerFlushIndex' of 'panda3d.core.BamCache' objects>"
        'consider_flush_global_index': None, # (!) real value is '<staticmethod(<built-in method consider_flush_global_index of type object at 0x00007FFCFE36FAA0>)>'
        'consider_flush_index': None, # (!) real value is "<method 'consider_flush_index' of 'panda3d.core.BamCache' objects>"
        'flushGlobalIndex': None, # (!) real value is '<staticmethod(<built-in method flushGlobalIndex of type object at 0x00007FFCFE36FAA0>)>'
        'flushIndex': None, # (!) real value is "<method 'flushIndex' of 'panda3d.core.BamCache' objects>"
        'flush_global_index': None, # (!) real value is '<staticmethod(<built-in method flush_global_index of type object at 0x00007FFCFE36FAA0>)>'
        'flush_index': None, # (!) real value is "<method 'flush_index' of 'panda3d.core.BamCache' objects>"
        'flush_time': None, # (!) real value is "<attribute 'flush_time' of 'panda3d.core.BamCache' objects>"
        'getActive': None, # (!) real value is "<method 'getActive' of 'panda3d.core.BamCache' objects>"
        'getCacheCompiledShaders': None, # (!) real value is "<method 'getCacheCompiledShaders' of 'panda3d.core.BamCache' objects>"
        'getCacheCompressedTextures': None, # (!) real value is "<method 'getCacheCompressedTextures' of 'panda3d.core.BamCache' objects>"
        'getCacheMaxKbytes': None, # (!) real value is "<method 'getCacheMaxKbytes' of 'panda3d.core.BamCache' objects>"
        'getCacheModels': None, # (!) real value is "<method 'getCacheModels' of 'panda3d.core.BamCache' objects>"
        'getCacheTextures': None, # (!) real value is "<method 'getCacheTextures' of 'panda3d.core.BamCache' objects>"
        'getFlushTime': None, # (!) real value is "<method 'getFlushTime' of 'panda3d.core.BamCache' objects>"
        'getGlobalPtr': None, # (!) real value is '<staticmethod(<built-in method getGlobalPtr of type object at 0x00007FFCFE36FAA0>)>'
        'getReadOnly': None, # (!) real value is "<method 'getReadOnly' of 'panda3d.core.BamCache' objects>"
        'getRoot': None, # (!) real value is "<method 'getRoot' of 'panda3d.core.BamCache' objects>"
        'get_active': None, # (!) real value is "<method 'get_active' of 'panda3d.core.BamCache' objects>"
        'get_cache_compiled_shaders': None, # (!) real value is "<method 'get_cache_compiled_shaders' of 'panda3d.core.BamCache' objects>"
        'get_cache_compressed_textures': None, # (!) real value is "<method 'get_cache_compressed_textures' of 'panda3d.core.BamCache' objects>"
        'get_cache_max_kbytes': None, # (!) real value is "<method 'get_cache_max_kbytes' of 'panda3d.core.BamCache' objects>"
        'get_cache_models': None, # (!) real value is "<method 'get_cache_models' of 'panda3d.core.BamCache' objects>"
        'get_cache_textures': None, # (!) real value is "<method 'get_cache_textures' of 'panda3d.core.BamCache' objects>"
        'get_flush_time': None, # (!) real value is "<method 'get_flush_time' of 'panda3d.core.BamCache' objects>"
        'get_global_ptr': None, # (!) real value is '<staticmethod(<built-in method get_global_ptr of type object at 0x00007FFCFE36FAA0>)>'
        'get_read_only': None, # (!) real value is "<method 'get_read_only' of 'panda3d.core.BamCache' objects>"
        'get_root': None, # (!) real value is "<method 'get_root' of 'panda3d.core.BamCache' objects>"
        'listIndex': None, # (!) real value is "<method 'listIndex' of 'panda3d.core.BamCache' objects>"
        'list_index': None, # (!) real value is "<method 'list_index' of 'panda3d.core.BamCache' objects>"
        'lookup': None, # (!) real value is "<method 'lookup' of 'panda3d.core.BamCache' objects>"
        'read_only': None, # (!) real value is "<attribute 'read_only' of 'panda3d.core.BamCache' objects>"
        'root': None, # (!) real value is "<attribute 'root' of 'panda3d.core.BamCache' objects>"
        'setActive': None, # (!) real value is "<method 'setActive' of 'panda3d.core.BamCache' objects>"
        'setCacheCompiledShaders': None, # (!) real value is "<method 'setCacheCompiledShaders' of 'panda3d.core.BamCache' objects>"
        'setCacheCompressedTextures': None, # (!) real value is "<method 'setCacheCompressedTextures' of 'panda3d.core.BamCache' objects>"
        'setCacheMaxKbytes': None, # (!) real value is "<method 'setCacheMaxKbytes' of 'panda3d.core.BamCache' objects>"
        'setCacheModels': None, # (!) real value is "<method 'setCacheModels' of 'panda3d.core.BamCache' objects>"
        'setCacheTextures': None, # (!) real value is "<method 'setCacheTextures' of 'panda3d.core.BamCache' objects>"
        'setFlushTime': None, # (!) real value is "<method 'setFlushTime' of 'panda3d.core.BamCache' objects>"
        'setReadOnly': None, # (!) real value is "<method 'setReadOnly' of 'panda3d.core.BamCache' objects>"
        'setRoot': None, # (!) real value is "<method 'setRoot' of 'panda3d.core.BamCache' objects>"
        'set_active': None, # (!) real value is "<method 'set_active' of 'panda3d.core.BamCache' objects>"
        'set_cache_compiled_shaders': None, # (!) real value is "<method 'set_cache_compiled_shaders' of 'panda3d.core.BamCache' objects>"
        'set_cache_compressed_textures': None, # (!) real value is "<method 'set_cache_compressed_textures' of 'panda3d.core.BamCache' objects>"
        'set_cache_max_kbytes': None, # (!) real value is "<method 'set_cache_max_kbytes' of 'panda3d.core.BamCache' objects>"
        'set_cache_models': None, # (!) real value is "<method 'set_cache_models' of 'panda3d.core.BamCache' objects>"
        'set_cache_textures': None, # (!) real value is "<method 'set_cache_textures' of 'panda3d.core.BamCache' objects>"
        'set_flush_time': None, # (!) real value is "<method 'set_flush_time' of 'panda3d.core.BamCache' objects>"
        'set_read_only': None, # (!) real value is "<method 'set_read_only' of 'panda3d.core.BamCache' objects>"
        'set_root': None, # (!) real value is "<method 'set_root' of 'panda3d.core.BamCache' objects>"
        'store': None, # (!) real value is "<method 'store' of 'panda3d.core.BamCache' objects>"
    }


