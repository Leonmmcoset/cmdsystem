# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .CullBinEnums import CullBinEnums

class CullBinManager(CullBinEnums):
    """
    /**
     * This is a global object that maintains the collection of named CullBins in
     * the world.
     */
    """
    def addBin(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_bin(const CullBinManager self, str name, int type, int sort)
        
        /**
         * Defines a new bin with the indicated name, and returns the new bin_index.
         * If there is already a bin with the same name returns its bin_index if it
         * had the same properties; otherwise, reports an error and returns -1.
         */
        """
        pass

    def add_bin(self, const_CullBinManager_self, str_name, int_type, int_sort): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_bin(const CullBinManager self, str name, int type, int sort)
        
        /**
         * Defines a new bin with the indicated name, and returns the new bin_index.
         * If there is already a bin with the same name returns its bin_index if it
         * had the same properties; otherwise, reports an error and returns -1.
         */
        """
        pass

    def findBin(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        find_bin(CullBinManager self, str name)
        
        /**
         * Returns the bin_index associated with the bin of the given name, or -1 if
         * no bin has that name.
         */
        """
        pass

    def find_bin(self, CullBinManager_self, str_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        find_bin(CullBinManager self, str name)
        
        /**
         * Returns the bin_index associated with the bin of the given name, or -1 if
         * no bin has that name.
         */
        """
        pass

    def getBin(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_bin(CullBinManager self, int n)
        
        /**
         * Returns the bin_index of the nth bin in the set, where n is a number
         * between 0 and get_num_bins(). This returns the list of bin_index numbers,
         * in sorted order (that is, in the order in which the bins should be
         * rendered).
         */
        """
        pass

    def getBinActive(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_bin_active(CullBinManager self, str name)
        get_bin_active(CullBinManager self, int bin_index)
        
        /**
         * Returns the active flag of the bin with the indicated bin_index (where
         * bin_index was retrieved by get_bin() or find_bin()).
         *
         * When a bin is marked inactive, all geometry assigned to it is not rendered.
         */
        
        /**
         * Returns the active flag of the bin with the indicated name.
         *
         * When a bin is marked inactive, all geometry assigned to it is not rendered.
         */
        """
        pass

    def getBinFlashActive(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_bin_flash_active(CullBinManager self, int bin_index)
        
        /**
         * Returns true if the bin with the given bin_index is configured to flash at
         * a predetermined color (where bin_index was retrieved by get_bin() or
         * find_bin()).
         *
         * This method is not available in release builds.
         */
        """
        pass

    def getBinFlashColor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_bin_flash_color(CullBinManager self, int bin_index)
        
        /**
         * Returns the color that this bin has been configured to flash to, if
         * configured.
         *
         * This method is not available in release builds.
         */
        """
        pass

    def getBinName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_bin_name(CullBinManager self, int bin_index)
        
        /**
         * Returns the name of the bin with the indicated bin_index (where bin_index
         * was retrieved by get_bin() or find_bin()).  The bin's name may not be
         * changed during the life of the bin.
         */
        """
        pass

    def getBins(self, *args, **kwargs): # real signature unknown
        pass

    def getBinSort(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_bin_sort(CullBinManager self, str name)
        get_bin_sort(CullBinManager self, int bin_index)
        
        /**
         * Returns the sort order of the bin with the indicated bin_index (where
         * bin_index was retrieved by get_bin() or find_bin()).
         *
         * The bins are rendered in increasing order by their sort order; this number
         * may be changed from time to time to reorder the bins.
         */
        
        /**
         * Returns the sort order of the bin with the indicated name.
         *
         * The bins are rendered in increasing order by their sort order; this number
         * may be changed from time to time to reorder the bins.
         */
        """
        pass

    def getBinType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_bin_type(CullBinManager self, str name)
        get_bin_type(CullBinManager self, int bin_index)
        
        /**
         * Returns the type of the bin with the indicated bin_index (where bin_index
         * was retrieved by get_bin() or find_bin()).
         */
        
        /**
         * Returns the type of the bin with the indicated name.
         */
        """
        pass

    def getGlobalPtr(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_global_ptr()
        
        /**
         * Returns the pointer to the global CullBinManager object.
         */
        """
        pass

    def getNumBins(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_bins(CullBinManager self)
        
        /**
         * Returns the number of bins in the world.
         */
        """
        pass

    def get_bin(self, CullBinManager_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_bin(CullBinManager self, int n)
        
        /**
         * Returns the bin_index of the nth bin in the set, where n is a number
         * between 0 and get_num_bins(). This returns the list of bin_index numbers,
         * in sorted order (that is, in the order in which the bins should be
         * rendered).
         */
        """
        pass

    def get_bins(self, *args, **kwargs): # real signature unknown
        pass

    def get_bin_active(self, CullBinManager_self, str_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_bin_active(CullBinManager self, str name)
        get_bin_active(CullBinManager self, int bin_index)
        
        /**
         * Returns the active flag of the bin with the indicated bin_index (where
         * bin_index was retrieved by get_bin() or find_bin()).
         *
         * When a bin is marked inactive, all geometry assigned to it is not rendered.
         */
        
        /**
         * Returns the active flag of the bin with the indicated name.
         *
         * When a bin is marked inactive, all geometry assigned to it is not rendered.
         */
        """
        pass

    def get_bin_flash_active(self, CullBinManager_self, int_bin_index): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_bin_flash_active(CullBinManager self, int bin_index)
        
        /**
         * Returns true if the bin with the given bin_index is configured to flash at
         * a predetermined color (where bin_index was retrieved by get_bin() or
         * find_bin()).
         *
         * This method is not available in release builds.
         */
        """
        pass

    def get_bin_flash_color(self, CullBinManager_self, int_bin_index): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_bin_flash_color(CullBinManager self, int bin_index)
        
        /**
         * Returns the color that this bin has been configured to flash to, if
         * configured.
         *
         * This method is not available in release builds.
         */
        """
        pass

    def get_bin_name(self, CullBinManager_self, int_bin_index): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_bin_name(CullBinManager self, int bin_index)
        
        /**
         * Returns the name of the bin with the indicated bin_index (where bin_index
         * was retrieved by get_bin() or find_bin()).  The bin's name may not be
         * changed during the life of the bin.
         */
        """
        pass

    def get_bin_sort(self, CullBinManager_self, str_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_bin_sort(CullBinManager self, str name)
        get_bin_sort(CullBinManager self, int bin_index)
        
        /**
         * Returns the sort order of the bin with the indicated bin_index (where
         * bin_index was retrieved by get_bin() or find_bin()).
         *
         * The bins are rendered in increasing order by their sort order; this number
         * may be changed from time to time to reorder the bins.
         */
        
        /**
         * Returns the sort order of the bin with the indicated name.
         *
         * The bins are rendered in increasing order by their sort order; this number
         * may be changed from time to time to reorder the bins.
         */
        """
        pass

    def get_bin_type(self, CullBinManager_self, str_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_bin_type(CullBinManager self, str name)
        get_bin_type(CullBinManager self, int bin_index)
        
        /**
         * Returns the type of the bin with the indicated bin_index (where bin_index
         * was retrieved by get_bin() or find_bin()).
         */
        
        /**
         * Returns the type of the bin with the indicated name.
         */
        """
        pass

    def get_global_ptr(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_global_ptr()
        
        /**
         * Returns the pointer to the global CullBinManager object.
         */
        """
        pass

    def get_num_bins(self, CullBinManager_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_bins(CullBinManager self)
        
        /**
         * Returns the number of bins in the world.
         */
        """
        pass

    def removeBin(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_bin(const CullBinManager self, int bin_index)
        
        /**
         * Permanently removes the indicated bin.  This operation is not protected
         * from the pipeline and will disturb whatever is currently rendering in draw.
         * You should not call this during the normal course of rendering a frame; it
         * is intended only as an aid to development, to allow the developer to
         * interactively fiddle with the set of bins.
         */
        """
        pass

    def remove_bin(self, const_CullBinManager_self, int_bin_index): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_bin(const CullBinManager self, int bin_index)
        
        /**
         * Permanently removes the indicated bin.  This operation is not protected
         * from the pipeline and will disturb whatever is currently rendering in draw.
         * You should not call this during the normal course of rendering a frame; it
         * is intended only as an aid to development, to allow the developer to
         * interactively fiddle with the set of bins.
         */
        """
        pass

    def setBinActive(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_bin_active(const CullBinManager self, str name, bool active)
        set_bin_active(const CullBinManager self, int bin_index, bool active)
        
        /**
         * Changes the active flag of the bin with the indicated bin_index (where
         * bin_index was retrieved by get_bin() or find_bin()).
         *
         * When a bin is marked inactive, all geometry assigned to it is not rendered.
         */
        
        /**
         * Changes the active flag of the bin with the indicated name.
         *
         * When a bin is marked inactive, all geometry assigned to it is not rendered.
         */
        """
        pass

    def setBinFlashActive(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_bin_flash_active(const CullBinManager self, int bin_index, bool active)
        
        /**
         * When set to true, the given bin_index is configured to flash at a
         * predetermined color (where bin_index was retrieved by get_bin() or
         * find_bin()).
         *
         * This method is not available in release builds.
         */
        """
        pass

    def setBinFlashColor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_bin_flash_color(const CullBinManager self, int bin_index, const LVecBase4f color)
        
        /**
         * Changes the flash color for the given bin index.
         *
         * This method is not available in release builds.
         */
        """
        pass

    def setBinSort(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_bin_sort(const CullBinManager self, str name, int sort)
        set_bin_sort(const CullBinManager self, int bin_index, int sort)
        
        /**
         * Changes the sort order of the bin with the indicated bin_index (where
         * bin_index was retrieved by get_bin() or find_bin()).
         *
         * The bins are rendered in increasing order by their sort order; this number
         * may be changed from time to time to reorder the bins.
         */
        
        /**
         * Changes the sort order of the bin with the indicated name.
         *
         * The bins are rendered in increasing order by their sort order; this number
         * may be changed from time to time to reorder the bins.
         */
        """
        pass

    def setBinType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_bin_type(const CullBinManager self, str name, int type)
        set_bin_type(const CullBinManager self, int bin_index, int type)
        
        /**
         * Changes the type of the bin with the indicated bin_index (where bin_index
         * was retrieved by get_bin() or find_bin()).
         *
         * The change might be effective immediately, or it might take place next
         * frame, depending on the bin type.
         */
        
        /**
         * Changes the type of the bin with the indicated name.
         *
         * The change might be effective immediately, or it might take place next
         * frame, depending on the bin type.
         */
        """
        pass

    def set_bin_active(self, const_CullBinManager_self, str_name, bool_active): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_bin_active(const CullBinManager self, str name, bool active)
        set_bin_active(const CullBinManager self, int bin_index, bool active)
        
        /**
         * Changes the active flag of the bin with the indicated bin_index (where
         * bin_index was retrieved by get_bin() or find_bin()).
         *
         * When a bin is marked inactive, all geometry assigned to it is not rendered.
         */
        
        /**
         * Changes the active flag of the bin with the indicated name.
         *
         * When a bin is marked inactive, all geometry assigned to it is not rendered.
         */
        """
        pass

    def set_bin_flash_active(self, const_CullBinManager_self, int_bin_index, bool_active): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_bin_flash_active(const CullBinManager self, int bin_index, bool active)
        
        /**
         * When set to true, the given bin_index is configured to flash at a
         * predetermined color (where bin_index was retrieved by get_bin() or
         * find_bin()).
         *
         * This method is not available in release builds.
         */
        """
        pass

    def set_bin_flash_color(self, const_CullBinManager_self, int_bin_index, const_LVecBase4f_color): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_bin_flash_color(const CullBinManager self, int bin_index, const LVecBase4f color)
        
        /**
         * Changes the flash color for the given bin index.
         *
         * This method is not available in release builds.
         */
        """
        pass

    def set_bin_sort(self, const_CullBinManager_self, str_name, int_sort): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_bin_sort(const CullBinManager self, str name, int sort)
        set_bin_sort(const CullBinManager self, int bin_index, int sort)
        
        /**
         * Changes the sort order of the bin with the indicated bin_index (where
         * bin_index was retrieved by get_bin() or find_bin()).
         *
         * The bins are rendered in increasing order by their sort order; this number
         * may be changed from time to time to reorder the bins.
         */
        
        /**
         * Changes the sort order of the bin with the indicated name.
         *
         * The bins are rendered in increasing order by their sort order; this number
         * may be changed from time to time to reorder the bins.
         */
        """
        pass

    def set_bin_type(self, const_CullBinManager_self, str_name, int_type): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_bin_type(const CullBinManager self, str name, int type)
        set_bin_type(const CullBinManager self, int bin_index, int type)
        
        /**
         * Changes the type of the bin with the indicated bin_index (where bin_index
         * was retrieved by get_bin() or find_bin()).
         *
         * The change might be effective immediately, or it might take place next
         * frame, depending on the bin type.
         */
        
        /**
         * Changes the type of the bin with the indicated name.
         *
         * The change might be effective immediately, or it might take place next
         * frame, depending on the bin type.
         */
        """
        pass

    def write(self, CullBinManager_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(CullBinManager self, ostream out)
        
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

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * This is a global object that maintains the collection of named CullBins in\n * the world.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.CullBinManager' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE296080>'
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.CullBinManager' objects>"
        'addBin': None, # (!) real value is "<method 'addBin' of 'panda3d.core.CullBinManager' objects>"
        'add_bin': None, # (!) real value is "<method 'add_bin' of 'panda3d.core.CullBinManager' objects>"
        'findBin': None, # (!) real value is "<method 'findBin' of 'panda3d.core.CullBinManager' objects>"
        'find_bin': None, # (!) real value is "<method 'find_bin' of 'panda3d.core.CullBinManager' objects>"
        'getBin': None, # (!) real value is "<method 'getBin' of 'panda3d.core.CullBinManager' objects>"
        'getBinActive': None, # (!) real value is "<method 'getBinActive' of 'panda3d.core.CullBinManager' objects>"
        'getBinFlashActive': None, # (!) real value is "<method 'getBinFlashActive' of 'panda3d.core.CullBinManager' objects>"
        'getBinFlashColor': None, # (!) real value is "<method 'getBinFlashColor' of 'panda3d.core.CullBinManager' objects>"
        'getBinName': None, # (!) real value is "<method 'getBinName' of 'panda3d.core.CullBinManager' objects>"
        'getBinSort': None, # (!) real value is "<method 'getBinSort' of 'panda3d.core.CullBinManager' objects>"
        'getBinType': None, # (!) real value is "<method 'getBinType' of 'panda3d.core.CullBinManager' objects>"
        'getBins': None, # (!) real value is "<method 'getBins' of 'panda3d.core.CullBinManager' objects>"
        'getGlobalPtr': None, # (!) real value is '<staticmethod(<built-in method getGlobalPtr of type object at 0x00007FFCFE296080>)>'
        'getNumBins': None, # (!) real value is "<method 'getNumBins' of 'panda3d.core.CullBinManager' objects>"
        'get_bin': None, # (!) real value is "<method 'get_bin' of 'panda3d.core.CullBinManager' objects>"
        'get_bin_active': None, # (!) real value is "<method 'get_bin_active' of 'panda3d.core.CullBinManager' objects>"
        'get_bin_flash_active': None, # (!) real value is "<method 'get_bin_flash_active' of 'panda3d.core.CullBinManager' objects>"
        'get_bin_flash_color': None, # (!) real value is "<method 'get_bin_flash_color' of 'panda3d.core.CullBinManager' objects>"
        'get_bin_name': None, # (!) real value is "<method 'get_bin_name' of 'panda3d.core.CullBinManager' objects>"
        'get_bin_sort': None, # (!) real value is "<method 'get_bin_sort' of 'panda3d.core.CullBinManager' objects>"
        'get_bin_type': None, # (!) real value is "<method 'get_bin_type' of 'panda3d.core.CullBinManager' objects>"
        'get_bins': None, # (!) real value is "<method 'get_bins' of 'panda3d.core.CullBinManager' objects>"
        'get_global_ptr': None, # (!) real value is '<staticmethod(<built-in method get_global_ptr of type object at 0x00007FFCFE296080>)>'
        'get_num_bins': None, # (!) real value is "<method 'get_num_bins' of 'panda3d.core.CullBinManager' objects>"
        'removeBin': None, # (!) real value is "<method 'removeBin' of 'panda3d.core.CullBinManager' objects>"
        'remove_bin': None, # (!) real value is "<method 'remove_bin' of 'panda3d.core.CullBinManager' objects>"
        'setBinActive': None, # (!) real value is "<method 'setBinActive' of 'panda3d.core.CullBinManager' objects>"
        'setBinFlashActive': None, # (!) real value is "<method 'setBinFlashActive' of 'panda3d.core.CullBinManager' objects>"
        'setBinFlashColor': None, # (!) real value is "<method 'setBinFlashColor' of 'panda3d.core.CullBinManager' objects>"
        'setBinSort': None, # (!) real value is "<method 'setBinSort' of 'panda3d.core.CullBinManager' objects>"
        'setBinType': None, # (!) real value is "<method 'setBinType' of 'panda3d.core.CullBinManager' objects>"
        'set_bin_active': None, # (!) real value is "<method 'set_bin_active' of 'panda3d.core.CullBinManager' objects>"
        'set_bin_flash_active': None, # (!) real value is "<method 'set_bin_flash_active' of 'panda3d.core.CullBinManager' objects>"
        'set_bin_flash_color': None, # (!) real value is "<method 'set_bin_flash_color' of 'panda3d.core.CullBinManager' objects>"
        'set_bin_sort': None, # (!) real value is "<method 'set_bin_sort' of 'panda3d.core.CullBinManager' objects>"
        'set_bin_type': None, # (!) real value is "<method 'set_bin_type' of 'panda3d.core.CullBinManager' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.core.CullBinManager' objects>"
    }


