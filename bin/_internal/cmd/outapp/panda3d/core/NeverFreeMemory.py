# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class NeverFreeMemory(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * This class is used to allocate bytes of memory from a pool that is never
     * intended to be freed.  It is particularly useful to support DeletedChain,
     * which allocates memory in just such a fashion.
     *
     * When it is known that memory will not be freed, it is preferable to use
     * this instead of the standard malloc() (or global_operator_new()) call,
     * since this will help reduce fragmentation problems in the dynamic heap.
     * Also, memory allocated from here will exhibit less wasted space.
     */
    """
    def getTotalAlloc(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_total_alloc()
        
        /**
         * Returns the total number of bytes consumed by all the pages allocated
         * internally by this object.
         */
        """
        pass

    def getTotalUnused(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_total_unused()
        
        /**
         * Returns the difference between get_total_alloc() and get_total_used().
         * This represents bytes in allocated pages that have not (yet) been used by
         * the application.
         */
        """
        pass

    def getTotalUsed(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_total_used()
        
        /**
         * Returns the total number of bytes requested by the application in calls to
         * NeverFreeMemory::alloc().
         */
        """
        pass

    def get_total_alloc(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_total_alloc()
        
        /**
         * Returns the total number of bytes consumed by all the pages allocated
         * internally by this object.
         */
        """
        pass

    def get_total_unused(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_total_unused()
        
        /**
         * Returns the difference between get_total_alloc() and get_total_used().
         * This represents bytes in allocated pages that have not (yet) been used by
         * the application.
         */
        """
        pass

    def get_total_used(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_total_used()
        
        /**
         * Returns the total number of bytes requested by the application in calls to
         * NeverFreeMemory::alloc().
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
        '__doc__': '/**\n * This class is used to allocate bytes of memory from a pool that is never\n * intended to be freed.  It is particularly useful to support DeletedChain,\n * which allocates memory in just such a fashion.\n *\n * When it is known that memory will not be freed, it is preferable to use\n * this instead of the standard malloc() (or global_operator_new()) call,\n * since this will help reduce fragmentation problems in the dynamic heap.\n * Also, memory allocated from here will exhibit less wasted space.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.NeverFreeMemory' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2584A0>'
        'getTotalAlloc': None, # (!) real value is '<staticmethod(<built-in method getTotalAlloc of type object at 0x00007FFCFE2584A0>)>'
        'getTotalUnused': None, # (!) real value is '<staticmethod(<built-in method getTotalUnused of type object at 0x00007FFCFE2584A0>)>'
        'getTotalUsed': None, # (!) real value is '<staticmethod(<built-in method getTotalUsed of type object at 0x00007FFCFE2584A0>)>'
        'get_total_alloc': None, # (!) real value is '<staticmethod(<built-in method get_total_alloc of type object at 0x00007FFCFE2584A0>)>'
        'get_total_unused': None, # (!) real value is '<staticmethod(<built-in method get_total_unused of type object at 0x00007FFCFE2584A0>)>'
        'get_total_used': None, # (!) real value is '<staticmethod(<built-in method get_total_used of type object at 0x00007FFCFE2584A0>)>'
    }


