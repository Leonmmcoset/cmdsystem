# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .TypedWritableReferenceCount import TypedWritableReferenceCount

class CachedTypedWritableReferenceCount(TypedWritableReferenceCount):
    """
    /**
     * This is a special extension to ReferenceCount that includes dual reference
     * counts: the standard reference count number, which includes all references
     * to the object, and a separate number (the cache reference count) that
     * counts the number of references to the object just within its cache alone.
     * When get_ref_count() == get_cache_ref_count(), the object is not referenced
     * outside the cache.
     *
     * The cache refs must be explicitly maintained; there is no PointerTo<> class
     * to maintain the cache reference counts automatically.  The cache reference
     * count is automatically included in the overall reference count: calling
     * cache_ref() and cache_unref() automatically calls ref() and unref().
     */
    """
    def cacheRef(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        cache_ref(CachedTypedWritableReferenceCount self)
        
        /**
         * Explicitly increments the cache reference count and the normal reference
         * count simultaneously.
         */
        """
        pass

    def cacheUnref(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        cache_unref(CachedTypedWritableReferenceCount self)
        
        /**
         * Explicitly decrements the cache reference count and the normal reference
         * count simultaneously.
         *
         * The return value is true if the new reference count is nonzero, false if it
         * is zero.
         */
        """
        pass

    def cache_ref(self, CachedTypedWritableReferenceCount_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        cache_ref(CachedTypedWritableReferenceCount self)
        
        /**
         * Explicitly increments the cache reference count and the normal reference
         * count simultaneously.
         */
        """
        pass

    def cache_unref(self, CachedTypedWritableReferenceCount_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        cache_unref(CachedTypedWritableReferenceCount self)
        
        /**
         * Explicitly decrements the cache reference count and the normal reference
         * count simultaneously.
         *
         * The return value is true if the new reference count is nonzero, false if it
         * is zero.
         */
        """
        pass

    def getCacheRefCount(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_cache_ref_count(CachedTypedWritableReferenceCount self)
        
        /**
         * Returns the current reference count.
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_cache_ref_count(self, CachedTypedWritableReferenceCount_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_cache_ref_count(CachedTypedWritableReferenceCount self)
        
        /**
         * Returns the current reference count.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def testRefCountIntegrity(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        test_ref_count_integrity(CachedTypedWritableReferenceCount self)
        
        /**
         * Does some easy checks to make sure that the reference count isn't
         * completely bogus.
         */
        """
        pass

    def test_ref_count_integrity(self, CachedTypedWritableReferenceCount_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        test_ref_count_integrity(CachedTypedWritableReferenceCount self)
        
        /**
         * Does some easy checks to make sure that the reference count isn't
         * completely bogus.
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    cache_ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * This is a special extension to ReferenceCount that includes dual reference\n * counts: the standard reference count number, which includes all references\n * to the object, and a separate number (the cache reference count) that\n * counts the number of references to the object just within its cache alone.\n * When get_ref_count() == get_cache_ref_count(), the object is not referenced\n * outside the cache.\n *\n * The cache refs must be explicitly maintained; there is no PointerTo<> class\n * to maintain the cache reference counts automatically.  The cache reference\n * count is automatically included in the overall reference count: calling\n * cache_ref() and cache_unref() automatically calls ref() and unref().\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.CachedTypedWritableReferenceCount' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE371230>'
        'cacheRef': None, # (!) real value is "<method 'cacheRef' of 'panda3d.core.CachedTypedWritableReferenceCount' objects>"
        'cacheUnref': None, # (!) real value is "<method 'cacheUnref' of 'panda3d.core.CachedTypedWritableReferenceCount' objects>"
        'cache_ref': None, # (!) real value is "<method 'cache_ref' of 'panda3d.core.CachedTypedWritableReferenceCount' objects>"
        'cache_ref_count': None, # (!) real value is "<attribute 'cache_ref_count' of 'panda3d.core.CachedTypedWritableReferenceCount' objects>"
        'cache_unref': None, # (!) real value is "<method 'cache_unref' of 'panda3d.core.CachedTypedWritableReferenceCount' objects>"
        'getCacheRefCount': None, # (!) real value is "<method 'getCacheRefCount' of 'panda3d.core.CachedTypedWritableReferenceCount' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE371230>)>'
        'get_cache_ref_count': None, # (!) real value is "<method 'get_cache_ref_count' of 'panda3d.core.CachedTypedWritableReferenceCount' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE371230>)>'
        'testRefCountIntegrity': None, # (!) real value is "<method 'testRefCountIntegrity' of 'panda3d.core.CachedTypedWritableReferenceCount' objects>"
        'test_ref_count_integrity': None, # (!) real value is "<method 'test_ref_count_integrity' of 'panda3d.core.CachedTypedWritableReferenceCount' objects>"
    }


