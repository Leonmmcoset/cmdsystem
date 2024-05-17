# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class MemoryUsage(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * This class is used strictly for debugging purposes, specifically for
     * tracking memory leaks of reference-counted objects: it keeps a record of
     * every such object currently allocated.
     *
     * When compiled with NDEBUG set, this entire class does nothing and compiles
     * to a stub.
     */
    """
    def freeze(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        freeze()
        
        /**
         * 'Freezes' all pointers currently stored so that they are no longer
         * reported; only newly allocate pointers from this point on will appear in
         * future information requests.  This makes it easier to differentiate between
         * continuous leaks and one-time memory allocations.
         */
        """
        pass

    def getCurrentCppSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_current_cpp_size()
        
        /**
         * Returns the total number of bytes of allocated memory consumed by C++
         * objects, not including the memory previously frozen.
         */
        """
        pass

    def getExternalSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_external_size()
        
        /**
         * Returns the total number of bytes of allocated memory in the heap that
         * Panda didn't seem to be responsible for.  This includes a few bytes for
         * very low-level objects (like ConfigVariables) that cannot use Panda memory
         * tracking because they are so very low-level.
         *
         * This also includes all of the memory that might have been allocated by a
         * high-level interpreter, like Python.
         *
         * This number is only available if Panda is able to hook into the actual heap
         * callback.
         */
        """
        pass

    def getNumPointers(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_pointers()
        
        /**
         * Returns the number of pointers currently active.
         */
        """
        pass

    def getPandaHeapArraySize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_panda_heap_array_size()
        
        /**
         * Returns the total number of bytes allocated from the heap from code within
         * Panda, for arrays.
         */
        """
        pass

    def getPandaHeapOverhead(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_panda_heap_overhead()
        
        /**
         * Returns the extra bytes allocated from the system that are not immediately
         * used for holding allocated objects.  This can only be determined if
         * ALTERNATIVE_MALLOC is enabled.
         */
        """
        pass

    def getPandaHeapSingleSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_panda_heap_single_size()
        
        /**
         * Returns the total number of bytes allocated from the heap from code within
         * Panda, for individual objects.
         */
        """
        pass

    def getPandaMmapSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_panda_mmap_size()
        
        /**
         * Returns the total number of bytes allocated from the virtual memory pool
         * from code within Panda.
         */
        """
        pass

    def getPointers(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_pointers(MemoryUsagePointers result)
        
        /**
         * Fills the indicated MemoryUsagePointers with the set of all pointers
         * currently active.
         */
        """
        pass

    def getPointersOfAge(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_pointers_of_age(MemoryUsagePointers result, double from, double to)
        
        /**
         * Fills the indicated MemoryUsagePointers with the set of all pointers that
         * were allocated within the range of the indicated number of seconds ago.
         */
        """
        pass

    def getPointersOfType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_pointers_of_type(MemoryUsagePointers result, TypeHandle type)
        
        /**
         * Fills the indicated MemoryUsagePointers with the set of all pointers of the
         * indicated type currently active.
         */
        """
        pass

    def getPointersWithZeroCount(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_pointers_with_zero_count(MemoryUsagePointers result)
        
        /**
         * Fills the indicated MemoryUsagePointers with the set of all currently
         * active pointers (that is, pointers allocated since the last call to
         * freeze(), and not yet freed) that have a zero reference count.
         *
         * Generally, an undeleted pointer with a zero reference count means its
         * reference count has never been incremented beyond zero (since once it has
         * been incremented, the only way it can return to zero would free the
         * pointer).  This may include objects that are allocated statically or on the
         * stack, which are never intended to be deleted.  Or, it might represent a
         * programmer or compiler error.
         *
         * This function has the side-effect of incrementing each of their reference
         * counts by one, thus preventing them from ever being freed--but since they
         * hadn't been freed anyway, probably no additional harm is done.
         */
        """
        pass

    def getTotalCppSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_total_cpp_size()
        
        /**
         * Returns the total number of bytes of allocated memory consumed by C++
         * objects, including the memory previously frozen.
         */
        """
        pass

    def getTotalSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_total_size()
        
        /**
         * Returns the total size of allocated memory consumed by the process, as
         * nearly as can be determined.
         */
        """
        pass

    def get_current_cpp_size(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_current_cpp_size()
        
        /**
         * Returns the total number of bytes of allocated memory consumed by C++
         * objects, not including the memory previously frozen.
         */
        """
        pass

    def get_external_size(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_external_size()
        
        /**
         * Returns the total number of bytes of allocated memory in the heap that
         * Panda didn't seem to be responsible for.  This includes a few bytes for
         * very low-level objects (like ConfigVariables) that cannot use Panda memory
         * tracking because they are so very low-level.
         *
         * This also includes all of the memory that might have been allocated by a
         * high-level interpreter, like Python.
         *
         * This number is only available if Panda is able to hook into the actual heap
         * callback.
         */
        """
        pass

    def get_num_pointers(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_pointers()
        
        /**
         * Returns the number of pointers currently active.
         */
        """
        pass

    def get_panda_heap_array_size(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_panda_heap_array_size()
        
        /**
         * Returns the total number of bytes allocated from the heap from code within
         * Panda, for arrays.
         */
        """
        pass

    def get_panda_heap_overhead(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_panda_heap_overhead()
        
        /**
         * Returns the extra bytes allocated from the system that are not immediately
         * used for holding allocated objects.  This can only be determined if
         * ALTERNATIVE_MALLOC is enabled.
         */
        """
        pass

    def get_panda_heap_single_size(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_panda_heap_single_size()
        
        /**
         * Returns the total number of bytes allocated from the heap from code within
         * Panda, for individual objects.
         */
        """
        pass

    def get_panda_mmap_size(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_panda_mmap_size()
        
        /**
         * Returns the total number of bytes allocated from the virtual memory pool
         * from code within Panda.
         */
        """
        pass

    def get_pointers(self, MemoryUsagePointers_result): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_pointers(MemoryUsagePointers result)
        
        /**
         * Fills the indicated MemoryUsagePointers with the set of all pointers
         * currently active.
         */
        """
        pass

    def get_pointers_of_age(self, MemoryUsagePointers_result, double_from, double_to): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_pointers_of_age(MemoryUsagePointers result, double from, double to)
        
        /**
         * Fills the indicated MemoryUsagePointers with the set of all pointers that
         * were allocated within the range of the indicated number of seconds ago.
         */
        """
        pass

    def get_pointers_of_type(self, MemoryUsagePointers_result, TypeHandle_type): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_pointers_of_type(MemoryUsagePointers result, TypeHandle type)
        
        /**
         * Fills the indicated MemoryUsagePointers with the set of all pointers of the
         * indicated type currently active.
         */
        """
        pass

    def get_pointers_with_zero_count(self, MemoryUsagePointers_result): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_pointers_with_zero_count(MemoryUsagePointers result)
        
        /**
         * Fills the indicated MemoryUsagePointers with the set of all currently
         * active pointers (that is, pointers allocated since the last call to
         * freeze(), and not yet freed) that have a zero reference count.
         *
         * Generally, an undeleted pointer with a zero reference count means its
         * reference count has never been incremented beyond zero (since once it has
         * been incremented, the only way it can return to zero would free the
         * pointer).  This may include objects that are allocated statically or on the
         * stack, which are never intended to be deleted.  Or, it might represent a
         * programmer or compiler error.
         *
         * This function has the side-effect of incrementing each of their reference
         * counts by one, thus preventing them from ever being freed--but since they
         * hadn't been freed anyway, probably no additional harm is done.
         */
        """
        pass

    def get_total_cpp_size(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_total_cpp_size()
        
        /**
         * Returns the total number of bytes of allocated memory consumed by C++
         * objects, including the memory previously frozen.
         */
        """
        pass

    def get_total_size(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_total_size()
        
        /**
         * Returns the total size of allocated memory consumed by the process, as
         * nearly as can be determined.
         */
        """
        pass

    def isCounting(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_counting()
        
        /**
         * Returns true if the MemoryUsage object is currently at least counting
         * memory (e.g.  this is a Windows debug build), even if it's not fully
         * tracking it.
         */
        """
        pass

    def isTracking(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_tracking()
        
        /**
         * Returns true if the MemoryUsage object is currently tracking memory (e.g.
         * track-memory-usage is configured #t).
         */
        """
        pass

    def is_counting(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_counting()
        
        /**
         * Returns true if the MemoryUsage object is currently at least counting
         * memory (e.g.  this is a Windows debug build), even if it's not fully
         * tracking it.
         */
        """
        pass

    def is_tracking(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_tracking()
        
        /**
         * Returns true if the MemoryUsage object is currently tracking memory (e.g.
         * track-memory-usage is configured #t).
         */
        """
        pass

    def showCurrentAges(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        show_current_ages()
        
        /**
         * Shows the breakdown of ages of all of the active pointers.
         */
        """
        pass

    def showCurrentTypes(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        show_current_types()
        
        /**
         * Shows the breakdown of types of all of the active pointers.
         */
        """
        pass

    def showTrendAges(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        show_trend_ages()
        
        /**
         * Shows the breakdown of ages of all of the pointers allocated and freed
         * since the last call to freeze().
         */
        """
        pass

    def showTrendTypes(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        show_trend_types()
        
        /**
         * Shows the breakdown of types of all of the pointers allocated and freed
         * since the last call to freeze().
         */
        """
        pass

    def show_current_ages(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        show_current_ages()
        
        /**
         * Shows the breakdown of ages of all of the active pointers.
         */
        """
        pass

    def show_current_types(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        show_current_types()
        
        /**
         * Shows the breakdown of types of all of the active pointers.
         */
        """
        pass

    def show_trend_ages(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        show_trend_ages()
        
        /**
         * Shows the breakdown of ages of all of the pointers allocated and freed
         * since the last call to freeze().
         */
        """
        pass

    def show_trend_types(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        show_trend_types()
        
        /**
         * Shows the breakdown of types of all of the pointers allocated and freed
         * since the last call to freeze().
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

    counting = False
    current_cpp_size = 0
    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.MemoryUsage' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.MemoryUsage' objects>"
        '__doc__': '/**\n * This class is used strictly for debugging purposes, specifically for\n * tracking memory leaks of reference-counted objects: it keeps a record of\n * every such object currently allocated.\n *\n * When compiled with NDEBUG set, this entire class does nothing and compiles\n * to a stub.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.MemoryUsage' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE277040>'
        'counting': None, # (!) real value is "<attribute 'counting' of 'panda3d.core.MemoryUsage'>"
        'current_cpp_size': None, # (!) real value is "<attribute 'current_cpp_size' of 'panda3d.core.MemoryUsage'>"
        'external_size': None, # (!) real value is "<attribute 'external_size' of 'panda3d.core.MemoryUsage'>"
        'freeze': None, # (!) real value is '<staticmethod(<built-in method freeze of type object at 0x00007FFCFE277040>)>'
        'getCurrentCppSize': None, # (!) real value is '<staticmethod(<built-in method getCurrentCppSize of type object at 0x00007FFCFE277040>)>'
        'getExternalSize': None, # (!) real value is '<staticmethod(<built-in method getExternalSize of type object at 0x00007FFCFE277040>)>'
        'getNumPointers': None, # (!) real value is '<staticmethod(<built-in method getNumPointers of type object at 0x00007FFCFE277040>)>'
        'getPandaHeapArraySize': None, # (!) real value is '<staticmethod(<built-in method getPandaHeapArraySize of type object at 0x00007FFCFE277040>)>'
        'getPandaHeapOverhead': None, # (!) real value is '<staticmethod(<built-in method getPandaHeapOverhead of type object at 0x00007FFCFE277040>)>'
        'getPandaHeapSingleSize': None, # (!) real value is '<staticmethod(<built-in method getPandaHeapSingleSize of type object at 0x00007FFCFE277040>)>'
        'getPandaMmapSize': None, # (!) real value is '<staticmethod(<built-in method getPandaMmapSize of type object at 0x00007FFCFE277040>)>'
        'getPointers': None, # (!) real value is '<staticmethod(<built-in method getPointers of type object at 0x00007FFCFE277040>)>'
        'getPointersOfAge': None, # (!) real value is '<staticmethod(<built-in method getPointersOfAge of type object at 0x00007FFCFE277040>)>'
        'getPointersOfType': None, # (!) real value is '<staticmethod(<built-in method getPointersOfType of type object at 0x00007FFCFE277040>)>'
        'getPointersWithZeroCount': None, # (!) real value is '<staticmethod(<built-in method getPointersWithZeroCount of type object at 0x00007FFCFE277040>)>'
        'getTotalCppSize': None, # (!) real value is '<staticmethod(<built-in method getTotalCppSize of type object at 0x00007FFCFE277040>)>'
        'getTotalSize': None, # (!) real value is '<staticmethod(<built-in method getTotalSize of type object at 0x00007FFCFE277040>)>'
        'get_current_cpp_size': None, # (!) real value is '<staticmethod(<built-in method get_current_cpp_size of type object at 0x00007FFCFE277040>)>'
        'get_external_size': None, # (!) real value is '<staticmethod(<built-in method get_external_size of type object at 0x00007FFCFE277040>)>'
        'get_num_pointers': None, # (!) real value is '<staticmethod(<built-in method get_num_pointers of type object at 0x00007FFCFE277040>)>'
        'get_panda_heap_array_size': None, # (!) real value is '<staticmethod(<built-in method get_panda_heap_array_size of type object at 0x00007FFCFE277040>)>'
        'get_panda_heap_overhead': None, # (!) real value is '<staticmethod(<built-in method get_panda_heap_overhead of type object at 0x00007FFCFE277040>)>'
        'get_panda_heap_single_size': None, # (!) real value is '<staticmethod(<built-in method get_panda_heap_single_size of type object at 0x00007FFCFE277040>)>'
        'get_panda_mmap_size': None, # (!) real value is '<staticmethod(<built-in method get_panda_mmap_size of type object at 0x00007FFCFE277040>)>'
        'get_pointers': None, # (!) real value is '<staticmethod(<built-in method get_pointers of type object at 0x00007FFCFE277040>)>'
        'get_pointers_of_age': None, # (!) real value is '<staticmethod(<built-in method get_pointers_of_age of type object at 0x00007FFCFE277040>)>'
        'get_pointers_of_type': None, # (!) real value is '<staticmethod(<built-in method get_pointers_of_type of type object at 0x00007FFCFE277040>)>'
        'get_pointers_with_zero_count': None, # (!) real value is '<staticmethod(<built-in method get_pointers_with_zero_count of type object at 0x00007FFCFE277040>)>'
        'get_total_cpp_size': None, # (!) real value is '<staticmethod(<built-in method get_total_cpp_size of type object at 0x00007FFCFE277040>)>'
        'get_total_size': None, # (!) real value is '<staticmethod(<built-in method get_total_size of type object at 0x00007FFCFE277040>)>'
        'isCounting': None, # (!) real value is '<staticmethod(<built-in method isCounting of type object at 0x00007FFCFE277040>)>'
        'isTracking': None, # (!) real value is '<staticmethod(<built-in method isTracking of type object at 0x00007FFCFE277040>)>'
        'is_counting': None, # (!) real value is '<staticmethod(<built-in method is_counting of type object at 0x00007FFCFE277040>)>'
        'is_tracking': None, # (!) real value is '<staticmethod(<built-in method is_tracking of type object at 0x00007FFCFE277040>)>'
        'panda_heap_array_size': None, # (!) real value is "<attribute 'panda_heap_array_size' of 'panda3d.core.MemoryUsage'>"
        'panda_heap_overhead': None, # (!) real value is "<attribute 'panda_heap_overhead' of 'panda3d.core.MemoryUsage'>"
        'panda_heap_single_size': None, # (!) real value is "<attribute 'panda_heap_single_size' of 'panda3d.core.MemoryUsage'>"
        'panda_mmap_size': None, # (!) real value is "<attribute 'panda_mmap_size' of 'panda3d.core.MemoryUsage'>"
        'showCurrentAges': None, # (!) real value is '<staticmethod(<built-in method showCurrentAges of type object at 0x00007FFCFE277040>)>'
        'showCurrentTypes': None, # (!) real value is '<staticmethod(<built-in method showCurrentTypes of type object at 0x00007FFCFE277040>)>'
        'showTrendAges': None, # (!) real value is '<staticmethod(<built-in method showTrendAges of type object at 0x00007FFCFE277040>)>'
        'showTrendTypes': None, # (!) real value is '<staticmethod(<built-in method showTrendTypes of type object at 0x00007FFCFE277040>)>'
        'show_current_ages': None, # (!) real value is '<staticmethod(<built-in method show_current_ages of type object at 0x00007FFCFE277040>)>'
        'show_current_types': None, # (!) real value is '<staticmethod(<built-in method show_current_types of type object at 0x00007FFCFE277040>)>'
        'show_trend_ages': None, # (!) real value is '<staticmethod(<built-in method show_trend_ages of type object at 0x00007FFCFE277040>)>'
        'show_trend_types': None, # (!) real value is '<staticmethod(<built-in method show_trend_types of type object at 0x00007FFCFE277040>)>'
        'total_cpp_size': None, # (!) real value is "<attribute 'total_cpp_size' of 'panda3d.core.MemoryUsage'>"
        'total_size': None, # (!) real value is "<attribute 'total_size' of 'panda3d.core.MemoryUsage'>"
        'tracking': None, # (!) real value is "<attribute 'tracking' of 'panda3d.core.MemoryUsage'>"
    }
    external_size = 0
    panda_heap_array_size = 76292
    panda_heap_overhead = 0
    panda_heap_single_size = 15424
    panda_mmap_size = 262144
    total_cpp_size = 0
    total_size = 91716
    tracking = False


