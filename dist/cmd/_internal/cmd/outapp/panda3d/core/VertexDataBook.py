# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class VertexDataBook(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * A collection of VertexDataPages, which can be used to allocate new
     * VertexDataBlock objects.
     */
    """
    def alloc(self, const_VertexDataBook_self, int_size): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        alloc(const VertexDataBook self, int size)
        
        /**
         * Allocates and returns a new VertexDataBuffer of the requested size.
         */
        """
        pass

    def countAllocatedSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        count_allocated_size(VertexDataBook self)
        count_allocated_size(VertexDataBook self, int ram_class)
        
        /**
         * Returns the total size of all bytes allocated within pages owned by this
         * book.
         */
        
        /**
         * Returns the total size of all bytes allocated within pages owned by this
         * book that have the indicated ram class.
         */
        """
        pass

    def countTotalPageSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        count_total_page_size(VertexDataBook self)
        count_total_page_size(VertexDataBook self, int ram_class)
        
        /**
         * Returns the total size of all bytes owned by all pages owned by this book.
         */
        
        /**
         * Returns the total size of all bytes owned by all pages owned by this book
         * that have the indicated ram class.
         */
        """
        pass

    def count_allocated_size(self, VertexDataBook_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        count_allocated_size(VertexDataBook self)
        count_allocated_size(VertexDataBook self, int ram_class)
        
        /**
         * Returns the total size of all bytes allocated within pages owned by this
         * book.
         */
        
        /**
         * Returns the total size of all bytes allocated within pages owned by this
         * book that have the indicated ram class.
         */
        """
        pass

    def count_total_page_size(self, VertexDataBook_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        count_total_page_size(VertexDataBook self)
        count_total_page_size(VertexDataBook self, int ram_class)
        
        /**
         * Returns the total size of all bytes owned by all pages owned by this book.
         */
        
        /**
         * Returns the total size of all bytes owned by all pages owned by this book
         * that have the indicated ram class.
         */
        """
        pass

    def getNumPages(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_pages(VertexDataBook self)
        
        /**
         * Returns the number of pages created for the book.
         */
        """
        pass

    def get_num_pages(self, VertexDataBook_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_pages(VertexDataBook self)
        
        /**
         * Returns the number of pages created for the book.
         */
        """
        pass

    def saveToDisk(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        save_to_disk(const VertexDataBook self)
        
        /**
         * Writes all pages to disk immediately, just in case they get evicted later.
         * It makes sense to make this call just before taking down a loading screen,
         * to minimize chugs from saving pages inadvertently later.
         */
        """
        pass

    def save_to_disk(self, const_VertexDataBook_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        save_to_disk(const VertexDataBook self)
        
        /**
         * Writes all pages to disk immediately, just in case they get evicted later.
         * It makes sense to make this call just before taking down a loading screen,
         * to minimize chugs from saving pages inadvertently later.
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
        '__doc__': '/**\n * A collection of VertexDataPages, which can be used to allocate new\n * VertexDataBlock objects.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.VertexDataBook' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2FAFA0>'
        'alloc': None, # (!) real value is "<method 'alloc' of 'panda3d.core.VertexDataBook' objects>"
        'countAllocatedSize': None, # (!) real value is "<method 'countAllocatedSize' of 'panda3d.core.VertexDataBook' objects>"
        'countTotalPageSize': None, # (!) real value is "<method 'countTotalPageSize' of 'panda3d.core.VertexDataBook' objects>"
        'count_allocated_size': None, # (!) real value is "<method 'count_allocated_size' of 'panda3d.core.VertexDataBook' objects>"
        'count_total_page_size': None, # (!) real value is "<method 'count_total_page_size' of 'panda3d.core.VertexDataBook' objects>"
        'getNumPages': None, # (!) real value is "<method 'getNumPages' of 'panda3d.core.VertexDataBook' objects>"
        'get_num_pages': None, # (!) real value is "<method 'get_num_pages' of 'panda3d.core.VertexDataBook' objects>"
        'saveToDisk': None, # (!) real value is "<method 'saveToDisk' of 'panda3d.core.VertexDataBook' objects>"
        'save_to_disk': None, # (!) real value is "<method 'save_to_disk' of 'panda3d.core.VertexDataBook' objects>"
    }


