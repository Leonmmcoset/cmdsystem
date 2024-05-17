# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .CachedTypedWritableReferenceCount import CachedTypedWritableReferenceCount

class CopyOnWriteObject(CachedTypedWritableReferenceCount):
    """
    /**
     * This base class provides basic reference counting, but also can be used
     * with a CopyOnWritePointer to provide get_read_pointer() and
     * get_write_pointer().
     */
    """
    def cacheRef(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        cache_ref(CopyOnWriteObject self)
        
        /**
         * @see CachedTypedWritableReferenceCount::cache_ref()
         */
        """
        pass

    def cacheUnref(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        cache_unref(CopyOnWriteObject self)
        
        /**
         * @see CachedTypedWritableReferenceCount::cache_unref()
         */
        """
        pass

    def cache_ref(self, CopyOnWriteObject_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        cache_ref(CopyOnWriteObject self)
        
        /**
         * @see CachedTypedWritableReferenceCount::cache_ref()
         */
        """
        pass

    def cache_unref(self, CopyOnWriteObject_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        cache_unref(CopyOnWriteObject self)
        
        /**
         * @see CachedTypedWritableReferenceCount::cache_unref()
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
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
        '__doc__': '/**\n * This base class provides basic reference counting, but also can be used\n * with a CopyOnWritePointer to provide get_read_pointer() and\n * get_write_pointer().\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.CopyOnWriteObject' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE371B40>'
        'cacheRef': None, # (!) real value is "<method 'cacheRef' of 'panda3d.core.CopyOnWriteObject' objects>"
        'cacheUnref': None, # (!) real value is "<method 'cacheUnref' of 'panda3d.core.CopyOnWriteObject' objects>"
        'cache_ref': None, # (!) real value is "<method 'cache_ref' of 'panda3d.core.CopyOnWriteObject' objects>"
        'cache_unref': None, # (!) real value is "<method 'cache_unref' of 'panda3d.core.CopyOnWriteObject' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE371B40>)>'
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE371B40>)>'
    }


