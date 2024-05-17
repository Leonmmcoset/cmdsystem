# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class GeomCacheManager(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * This is used to keep track of, and limit the size of, the cache of munged
     * vertices, which would otherwise be distributed through all of the
     * GeomVertexData objects in the system.
     *
     * The actual data in the cache is not stored here, but rather it is
     * distributed among the various GeomVertexData source objects.  This allows
     * the cache data to propagate through the multiprocess pipeline.
     *
     * This structure actually caches any of a number of different types of
     * pointers, and mixes them all up in the same LRU cache list.  Some of them
     * (such as GeomMunger) are reference-counted here in the cache; most are not.
     */
    """
    def flush(self, const_GeomCacheManager_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        flush(const GeomCacheManager self)
        
        /**
         * Immediately empties all elements in the cache.
         */
        """
        pass

    def getGlobalPtr(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_global_ptr()
        
        /**
         * Returns the global cache manager pointer.
         */
        """
        pass

    def getMaxSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_max_size(GeomCacheManager self)
        
        /**
         * Returns the maximum number of entries in the cache for storing pre-
         * processed data for rendering vertices.  See set_max_size().
         */
        """
        pass

    def getTotalSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_total_size(GeomCacheManager self)
        
        /**
         * Returns the number of entries currently in the cache.
         */
        """
        pass

    def get_global_ptr(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_global_ptr()
        
        /**
         * Returns the global cache manager pointer.
         */
        """
        pass

    def get_max_size(self, GeomCacheManager_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_max_size(GeomCacheManager self)
        
        /**
         * Returns the maximum number of entries in the cache for storing pre-
         * processed data for rendering vertices.  See set_max_size().
         */
        """
        pass

    def get_total_size(self, GeomCacheManager_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_total_size(GeomCacheManager self)
        
        /**
         * Returns the number of entries currently in the cache.
         */
        """
        pass

    def setMaxSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_max_size(GeomCacheManager self, int max_size)
        
        /**
         * Specifies the maximum number of entries in the cache for storing pre-
         * processed data for rendering vertices.  This limit is flexible, and may be
         * temporarily exceeded if many different Geoms are pre-processed during the
         * space of a single frame.
         *
         * This is not a limit on the actual vertex data, which is what it is; it is
         * also not a limit on the amount of memory used by the video driver or the
         * system graphics interface, which Panda has no control over.
         */
        """
        pass

    def set_max_size(self, GeomCacheManager_self, int_max_size): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_max_size(GeomCacheManager self, int max_size)
        
        /**
         * Specifies the maximum number of entries in the cache for storing pre-
         * processed data for rendering vertices.  This limit is flexible, and may be
         * temporarily exceeded if many different Geoms are pre-processed during the
         * space of a single frame.
         *
         * This is not a limit on the actual vertex data, which is what it is; it is
         * also not a limit on the amount of memory used by the video driver or the
         * system graphics interface, which Panda has no control over.
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
        '__doc__': '/**\n * This is used to keep track of, and limit the size of, the cache of munged\n * vertices, which would otherwise be distributed through all of the\n * GeomVertexData objects in the system.\n *\n * The actual data in the cache is not stored here, but rather it is\n * distributed among the various GeomVertexData source objects.  This allows\n * the cache data to propagate through the multiprocess pipeline.\n *\n * This structure actually caches any of a number of different types of\n * pointers, and mixes them all up in the same LRU cache list.  Some of them\n * (such as GeomMunger) are reference-counted here in the cache; most are not.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.GeomCacheManager' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2FB6E0>'
        'flush': None, # (!) real value is "<method 'flush' of 'panda3d.core.GeomCacheManager' objects>"
        'getGlobalPtr': None, # (!) real value is '<staticmethod(<built-in method getGlobalPtr of type object at 0x00007FFCFE2FB6E0>)>'
        'getMaxSize': None, # (!) real value is "<method 'getMaxSize' of 'panda3d.core.GeomCacheManager' objects>"
        'getTotalSize': None, # (!) real value is "<method 'getTotalSize' of 'panda3d.core.GeomCacheManager' objects>"
        'get_global_ptr': None, # (!) real value is '<staticmethod(<built-in method get_global_ptr of type object at 0x00007FFCFE2FB6E0>)>'
        'get_max_size': None, # (!) real value is "<method 'get_max_size' of 'panda3d.core.GeomCacheManager' objects>"
        'get_total_size': None, # (!) real value is "<method 'get_total_size' of 'panda3d.core.GeomCacheManager' objects>"
        'setMaxSize': None, # (!) real value is "<method 'setMaxSize' of 'panda3d.core.GeomCacheManager' objects>"
        'set_max_size': None, # (!) real value is "<method 'set_max_size' of 'panda3d.core.GeomCacheManager' objects>"
    }


